# %%
# By Darren Wiseman 5/18
import random
from dataclasses import dataclass
import re

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

categories = {
    'Simple Melee': [
        Item("Club", "1 sp.", "1d4 bludgeon", 2, "Slow", "Light", "W"),
        Item("Dagger", "2 gp.", "1d4 pierce", 1, "Nick", "Finesse, Light, Thrown (range 20/60)", "M"),
        Item("Greatclub", "2 sp.", "1d8 bludgeoning", 10, "Push", "Two-handed", "W"),
        Item("Handaxe", "5 gp.", "1d6 slashing", 2, "Vex", "Light, Thrown (range 20/60)", "M"),
        Item("Javelin", "5 sp.", "1d6 piercing", 2, "Slow", "Thrown (range 30/120)", "M"),
        Item("Hammer, Light", "2 gp.", "1d bludgeoning", 2, "Nick", "Light, Thrown (range 20/60)", "M"),
        Item("Mace", "5 gp.", "1d6 bludgeoning", 4, "Sap", "none", "M"),
        Item("Quarterstaff", "2 sp.", "1d6 bludgeoning", 4, "Topple", "Versatile (1d8)", "W"),
        Item("Sickle", "1 gp.", "1d4 slashing", 2, "Nick", "Light", "M"),
        Item("Spear", "1 gp.", "1d6 piercing", 3, "Sap", "Versatile (1d8), Thrown (range 20/60)", "M")
    ],
    'Simple Ranged': [
        Item("Crossbow, Light", "25 gp.", "1d8 piercing", 5, "Slow", "Loading, Two-handed, Ammunition (range 80/320)", "W"), 
        Item("Dart", "5 cp.", "1d4 piercing", 0.25, "Vex", "Finesse, Thrown (range 20/60)", "M"),
        Item("Shortbow", "25 gp.", "1d6 piercing", 2, "Vex", "Two-handed, Ammunition (range 80/320)", "W"),
        Item("Sling", "1 sp.", "1d4 bludgeoning", 0, "Slow", "Ammunition (range 30/120)", "O")
    ],
    'Martial Melee': [
        Item("Battleaxe", "10 gp", "1d8 slashing", 4, "Topple", "Versatile (1d10)", "M"),
        Item("Flail", "10 gp", "1d8 bludgeoning", 2, "Sap", "none", "M"),
        Item("Glaive", "20 gp", "1d10 slashing", 6, "Graze", "Heavy, Reach, Two-handed", "M"),
        Item("Greataxe", "30 gp", "1d12 slashing", 7, "Cleave", "Heavy, Two-handed", "M"),
        Item("Greatsword", "50 gp", "2d6 slashing", 6, "Graze", "Heavy, Two-handed", "M"),
        Item("Halberd", "20 gp", "1d10 slashing", 6, "Cleave", "Heavy, Reach, Two-handed", "M"),
        Item("Lance", "10 gp", "1d12 piercing", 6, "Topple", "Heavy, Reach, Two-handed", "W"),
        Item("Longsword", "15 gp", "1d8 slashing", 3, "Sap", "Versatile (1d10)", "M"),
        Item("Morningstar", "15 gp", "1d8 piercing", 4, "Sap", "none", "M"),
        Item("Pike", "5 gp", "1d10 piercing", 18, "Push", "Heavy, Reach, Two-handed (unless mounted)", "M"),
        Item("Rapier", "25 gp", "1d8 piercing", 2, "Vex", "Finesse", "M"),
        Item("Scimitar", "25 gp", "1d6 slashing", 3, "Nick", "Finesse, Light", "M"),
        Item("Shortsword", "10 gp", "1d6 piercing", 2, "Vex", "Finesse, Light", "M"),
        Item("Trident", "5 gp", "1d6 piercing", 4, "Topple", "Versatile (1d8), Thrown (range 20/60)", "M"),
        Item("War hammer", "15 gp", "1d8 bludgeoning", 2, "Push", "none", "M"),
        Item("War pick", "5 gp", "1d8 piercing", 2, "Sap", "none", "M"),
        Item("Whip", "5 gp", "1d4 slashing", 2, "Slow", "Finesse, Reach", "O"),
    ],
    'Martial Ranged': [
        Item("Blowgun", "10 gp.", "1 piercing", 1, "Vex", "Loading, Ammunition (range 25/100)", "W"),
        Item("Crossbow, hand", "75 gp.", "1d6 piercing", 3, "Vex", "Light, Loading, Ammunition (range 30/120)", "W"),
        Item("Crossbow, heavy", "50 gp.", "1d10 piercing", 18, "Push","Heavy, Loading, Two-handed, Ammunition (range 100/400)", "W"),
        Item("Longbow", "50 gp.", "1d8 piercing", 2, "Slow","Heavy, Two-handed, Ammunition (range 150/600)", "W"),
        Item("Musket", "500 gp.", "1d12 piercing", 10, "Slow","Loading, Two-Handed, Ammunition (Range 40/120)", "M"),
        Item("Pistol", "250 gp.", "1d10 piercing", 3, "Vex","Loading, Ammunition (range 30/90)", "M")
    ]
}

material_data = {
    'Special Materials': [
        Special("Flametouched Iron", "M", 3, 7, 1.5, "[+1] save against spells/abilities from Evil outsiders, Negate DR: Evil outsiders"),
        Special("Adamantine", "M", 5, 5, 1.75, "piercing weapons get [+1] damage, Negate DR: Constructs"),
        Special("Byeshk", "M", 2, 10, 1.25, "bludgeoning weapons get [+1] damage, Negate DR: Aberrations"),
        Special("Mournlode", "M", 2, 7, 1.0, "[+1] to hit against Undead, Undead cannot reanimate if destroyed"),
        Special("Densewood", "W", 10, 2, 2.0, "bludgeoning weapons get [+1] damage, +5 DC to break/destroy"),
        Special("Eldritch Whorlwood", "W", 5, 4, 1.0, "No penalty to hit: Ethereal creatures")
    ]
}

def get_material(item):
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

def create_material_frame(material):
    content_lines = [
        f"\033[1m{material.name}\033[0m",
        f"Price Modifier: \033[38;5;178m×{material.price_mod}\033[0m",
        f"Weight Modifier: ×{material.weight_mod}",
        "Effects:"
    ]
    
    # Handle effects as bullet points
    if material.effect:
        content_lines += [f"  - {eff.strip()}" for eff in material.effect.split(',')]
    else:
        content_lines += ["  - none"]

    max_content_width = max(len(strip_ansi_codes(line)) for line in content_lines)
    box_width = max_content_width + 4
    horizontal = '═' * (box_width - 2)

    template = [
        f"╔{horizontal}╗",
        f"║ {content_lines[0].center(box_width - 4)} ║",
        f"╠{horizontal}╣"
    ]
    
    for line in content_lines[1:]:
        visible_length = len(strip_ansi_codes(line))
        padding_needed = box_width - 4 - visible_length
        template.append(f"║ {line}{' ' * padding_needed} ║")

    template.append(f"╚{horizontal}╝")
    return '\n'.join(template)

def strip_ansi_codes(s):
    return re.sub(r'\033\[[\d;]*m', '', s)

def get_random_item(category):
    random.shuffle(categories[category])
    item = categories[category][0]
    
    content_lines = [
        f"\033[1m{item.name}\033[0m",
        f"Proficiency: {category.strip()}",
        f"Damage: {item.damage}",
        f"Cost: \033[38;5;178m{item.cost}\033[0m",
        f"Weight: {item.weight} lbs",
        f"Mastery: {item.mastery}"
    ]
    
    # Handle properties as bullet points only
    content_lines.append("Properties:")
    if item.properties:
        content_lines += [f"  - {prop.strip()}" for prop in item.properties.split(',')]
    else:
        content_lines += ["  - none"]

    max_content_width = max(len(strip_ansi_codes(line)) for line in content_lines)
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
    
    material = get_material(item)
    item_box = '\n'.join(template)
    
    if material:
        material_box = create_material_frame(material)
        item_lines = item_box.split('\n')
        material_lines = material_box.split('\n')
        
        # Calculate maximum VISIBLE width of item box (stripping ANSI)
        max_item_width = max(len(strip_ansi_codes(line)) for line in item_lines)
        
        # Combine boxes with proper ANSI-aware padding
        combined = []
        for i in range(max(len(item_lines), len(material_lines))):
            item_line = item_lines[i] if i < len(item_lines) else ''
            mat_line = material_lines[i] if i < len(material_lines) else ''
            
            # Calculate padding based on VISIBLE characters only
            padding_needed = max_item_width - len(strip_ansi_codes(item_line))
            combined_line = f"{item_line}{' ' * padding_needed}{mat_line}"
            combined.append(combined_line)

        print('\n'.join(combined))
    else:
        print(item_box)
        
    return item

# Generate and display random item
get_random_item(random.choice(list(categories.keys())))