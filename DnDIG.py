# %%
# By Darren Wiseman 5/18
import random
from dataclasses import dataclass

@dataclass
class Item:
    name: str
    cost: str
    damage: str
    weight: int
    properties: str

categories = {
    'Simple Melee weapon   ': [
        Item("Club", "1 sp.", "1d4 bludgeon", 2, "Light"),
    	Item("Dagger", "2 gp.", "1d4 pierce", 1, "Finesse, Light,\n| Thrown (range 20/60)"),
		Item("Greatclub", "2 sp.", "1d8 bludgeoning", 10, "Two-handed"),
		Item("Handaxe", "5 gp.", "1d6 slashing", 2, "Light,\n| Thrown (range 20/60)"),
		Item("Javelin", "5 sp.", "1d6 piercing", 2, "Thrown (range 30/120)"),
		Item("Hammer, Light", "2 gp.", "1d bludgeoning", 2, "Light,\n| Thrown (range 20/60)"),
		Item("Mace", "5 gp.", "1d6 bludgeoning", 4, "-"),
		Item("Quarterstaff", "2 sp.", "1d6 bludgeoning", 4, "Versatile (1d8)"),
		Item("Sickle", "1 gp.", "1d4 slashing", 2, "Light")
        # ... other items in SimpleMelee category
    ],
    'Simple Ranged weapon  ': [
        Item("Crossbow, Light", "25 gp.", "1d8 piercing", 5, "Ammunition (range 80/320),\n| Loading, Two-handed"),
		Item("Dart", "5 cp.", "1d4 piercing", 0.25, "Finesse,\n| Thrown (range 20/60)"),
		Item("Shortbow", "25 gp.", "1d6 piercing", 2, "Ammunition (range 80/320),\n| Two-handed"),
		Item("Sling", "1 sp.", "1d4 bludgeoning", 0, "Ammunition (range 30/120)")
        # ... other items in Simpleranged category
    ],
    'Martial Melee weapon  ': [
		Item("Battleaxe", "10 gp", "1d8 slashing", 4, "Versatile (1d10)"),
		Item("Flail", "10 gp", "1d8 bludgeoning", 2, "-"),
		Item("Glaive", "20 gp", "1d10 slashing", 6, "Heavy, Reach, Two-handed"),
		Item("Greataxe", "30 gp", "1d12 slashing", 7, "Heavy, Two-handed"),
		Item("Greatsword", "50 gp", "2d6 slashing", 6, "Heavy, Two-handed"),
		Item("Halberd", "20 gp", "1d10 slashing", 6, "Heavy, Reach, Two-handed"),
		Item("Lance", "10 gp", "1d12 piercing", 6, "Reach, special"),
		Item("Longsword", "15 gp", "1d8 slashing", 3, "Versatile (1d10)"),
		Item("Morningstar", "15 gp", "1d8 piercing", 4, "-"),
		Item("Pike", "5 gp", "1d10 piercing", 18, "Heavy, Reach, Two-handed"),
		Item("Rapier", "25 gp", "1d8 piercing", 2, "Finesse"),
		Item("Scimitar", "25 gp", "1d6 slashing", 3, "Finesse, Light"),
		Item("Shortsword", "10 gp", "1d6 piercing", 2, "Finesse, Light"),
		Item("Trident", "5 gp", "1d6 piercing", 4, "Thrown (range 20/60),\n| Versatile (1d8)"),
		Item("War pick", "5 gp", "1d8 piercing", 2, "-"),
		Item("War hammer", "15 gp", "1d8 bludgeoning", 2, "-")
        # ... other items in MartialMelee category
    ],
    'Martial Ranged weapon ': [
		Item("Blowgun", "10 gp.", "1 piercing", 1, "Ammunition (range 25/100),\n| Loading"),
		Item("Crossbow, hand", "75 gp.", "1d6 piercing", 3, "Ammunition (range 30/120),\n| Light, Loading"),
		Item("Crossbow, heavy", "50 gp.", "1d10 piercing", 18, "Ammunition (range 100/400),\n| Heavy, Loading, Two-handed"),
		Item("Longbow", "50 gp.", "1d8 piercing", 2, "Ammunition (range 150/600),\n| Heavy, Two-handed")
        # ... other items in MartrialRanged category
    ]
}

def get_random_item(category):
    random.shuffle(categories[category])
    item = categories[category][0]
    
    template = f"""
+===========================================+\n| Thoust hath found a {category}|\n+===========================================+\n| {item.name}\n+-------------------------------------------+\n| Cost:    {item.cost}\n| Damage:  {item.damage}\n| Weight:  {item.weight} lbs.\n| Properties:  {item.properties}\n+===========================================+\n"""
    
    print(template)

# Generate a random D&D item
get_random_item(random.choice(list(categories.keys())))


