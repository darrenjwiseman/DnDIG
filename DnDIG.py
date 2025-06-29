# By Darren Wiseman 5/18
import random
from dataclasses import dataclass
import re
import os
import argparse
import pathlib
import csv

def clear_screen():
    """Clear terminal screen cross-platform"""
    os.system('cls' if os.name == 'nt' else 'clear')

@dataclass
class Item:
    name: str
    cost: str 
    damage: str
    weight: float
    mastery: str = ''
    properties: str = ''
    material: str = ''

@dataclass
class Special:
    name: str
    category: str
    rarity: int
    price_mod: float
    weight_mod: float
    effect: str = ''

def load_categories_from_files(data_dir="weapon_data"):
    categories = {}
    data_path = pathlib.Path(data_dir)

    # Filter out material_data.txt from processing
    for file_path in [f for f in data_path.glob("*.txt") if f.name != "Material_Data.txt"]:
        category_name = file_path.stem.replace("_", " ")
        items = []
        
        with open(file_path, "r") as f:
            reader = csv.reader(f, skipinitialspace=True)
            for line_num, parts in enumerate(reader, 1):
                if not parts or parts[0].startswith("#"):
                    continue
                
                if len(parts) < 4:
                    print(f"WARNING: Skipping invalid line {line_num} in {file_path}")
                    continue
                
                try:
                    items.append(Item(
                        name=parts[0],
                        cost=parts[1],
                        damage=parts[2],
                        weight=float(parts[3]),
                        mastery=parts[4] if len(parts) > 4 else "",
                        properties=parts[5] if len(parts) > 5 else "",
                        material=parts[6] if len(parts) > 6 else ""
                    ))
                except Exception as e:
                    print(f"ERROR: Failed to parse line {line_num}: {e}")
                    continue
        
        categories[category_name] = items
    
    return categories

categories = load_categories_from_files()

def load_material_data(data_dir="weapon_data"):
    materials = []
    data_path = pathlib.Path(data_dir) / "Material_Data.txt"
    
    if not data_path.exists():
        return {'Special Materials': materials}
    
    with open(data_path, "r") as f:
        reader = csv.reader(f, skipinitialspace=True)
        for line_num, parts in enumerate(reader, 1):
            if not parts or parts[0].startswith("#"):
                continue
            
            if len(parts) < 5:
                print(f"WARNING: Skipping invalid line {line_num} in {data_path}")
                continue
            
            try:
                # Join all properties beyond index 4 into a single effect string
                effect_str = ",".join(parts[5:]) if len(parts) > 5 else ""
                materials.append(Special(
                    name=parts[0],
                    category=parts[1],
                    rarity=int(parts[2]),
                    price_mod=float(parts[3]),
                    weight_mod=float(parts[4]),
                    effect=effect_str
                ))
            except Exception as e:
                print(f"ERROR: Failed to parse line {line_num}: {e}")
                continue
    
    return {'Special Materials': materials}

# Replace hardcoded material_data with file-loaded version
material_data = load_material_data()

def get_material(item):
    # Add global declaration to access the flag
    global SPECIAL_MATERIALS_ENABLED
    if not SPECIAL_MATERIALS_ENABLED:
        return None
    # Check if item material matches category (W/M)
    eligible = [m for m in material_data['Special Materials'] if m.category == item.material]
    
    # Roll for materials
    results = []
    for mat in eligible:
        if random.randint(1, 100) <= mat.rarity:
            results.append(mat)
    
    if not results:
        return None
    
    # Return rarest material (lowest rarity value)
    return min(results, key=lambda x: x.rarity)

def strip_ansi_codes(s):
    return re.sub(r'\033\[[\d;]*m', '', s)

def get_random_item(category):
    clear_screen()  # Added screen clear before display
    
    random.shuffle(categories[category])
    item = categories[category][0]
    
    material = get_material(item)
    if material:
        weapon_name = f"{material.name} {item.name}"
    else:
        weapon_name = item.name
    
    content_lines = [
        f"\033[1m{weapon_name}\033[0m",
        f"Proficiency: {category.strip()}",
        f"Damage: {item.damage}",
    ]
    
    # Handle cost and weight modification from material
    if material:
        item_cost, item_denom = item.cost.split()
        item_cost = float(item_cost)
        modified_cost = f"{material.price_mod * item_cost:g} {item_denom.rstrip('.')}."  # Use original denomination and remove trailing "."
        actual_cost = f" (Base: {item.cost})"
        actual_weight = f" (Base: {item.weight} lbs)"
        modified_weight = f"{material.weight_mod * item.weight:g} lbs".rstrip(".0")
        content_lines += [
            f"Cost: \033[38;5;178m{modified_cost}\033[0m{actual_cost}",
            f"Weight: {modified_weight}{actual_weight}",
        ]
    else:
        content_lines += [
            f"Cost: \033[38;5;178m{item.cost}\033[0m",
            f"Weight: {item.weight} lbs.",
        ]
    
    content_lines += [f"Mastery: {item.mastery}"]
    
    # Handle properties as bullet points only
    content_lines.append("Properties:")
    if item.properties:
        content_lines += [f"  - {prop.strip()}" for prop in item.properties.split(',')]
    else:
        content_lines += ["  - none"]

    # Add Material section if applicable
    if material:
        content_lines.append("")
        content_lines.append("Material Effects:")
        content_lines += [f"  - {eff.strip()}" for eff in material.effect.split(',')]

    # Ensure max_content_width is not too narrow
    max_content_width = 2 # minimum width to ensure it doesn't go below 2
    for line in content_lines:
        visible_length = len(strip_ansi_codes(line))
        if '"' in line: # Adjust width for wrapping
            max_content_width = max(max_content_width, visible_length // 2)
        else:
            max_content_width = max(max_content_width, visible_length)

    box_width = max_content_width + 4
    horizontal = '═' * (box_width - 2)

    template = [
        f"╔{horizontal}╗",
    ]
    
    # Process title line
    visible_length = len(strip_ansi_codes(content_lines[0]))
    visible = strip_ansi_codes(content_lines[0]).center(box_width - 4)
    template.append(f"║ {content_lines[0].replace(strip_ansi_codes(content_lines[0]), visible)} ║")
    template.append(f"╠{horizontal}╣")  # Moved separator here

    # Process remaining lines
    for line in content_lines[1:]:
        visible_length = len(strip_ansi_codes(line))
        padding_needed = box_width - 4 - visible_length
        template.append(f"║ {line}{' ' * padding_needed} ║")

    template.append(f"╚{horizontal}╝")
    
    print('\n'.join(template))
    
    return item

if __name__ == "__main__":
    # Add argument parsing
    parser = argparse.ArgumentParser(description='Generate random D&D weapons')
    parser.add_argument('-nm', action='store_false', dest='materials_enabled',
                        help='Disable special material effects')
    args = parser.parse_args()
    
    # Set global flag based on command line argument
    SPECIAL_MATERIALS_ENABLED = args.materials_enabled
    
    # Generate and display random item
    get_random_item(random.choice(list(categories.keys())))

# Generate and display random item
get_random_item(random.choice(list(categories.keys())))