# %%
# By Darren Wiseman 5/18
import random
from dataclasses import dataclass
import random

@dataclass
class Item:
	name: str
	cost: str
	damage: str
	weight: int
	mastery: str = ''
	properties: str = ''

categories = {
	'Simple Melee weapon   ': [
		Item("Club", "1 sp.", "1d4 bludgeon", 2, "Slow", "Light"),
		Item("Dagger", "2 gp.", "1d4 pierce", 1, "Nick", "Finesse, Light, Thrown (range 20/60)"),
		Item("Greatclub", "2 sp.", "1d8 bludgeoning", 10, "Push", "Two-handed"),
		Item("Handaxe", "5 gp.", "1d6 slashing", 2, "Vex", "Light, Thrown (range 20/60)"),
		Item("Javelin", "5 sp.", "1d6 piercing", 2, "Slow", "Thrown (range 30/120)"),
		Item("Hammer, Light", "2 gp.", "1d bludgeoning", 2, "Nick", "Light, Thrown (range 20/60)"),
		Item("Mace", "5 gp.", "1d6 bludgeoning", 4, "Sap", "none"),
		Item("Quarterstaff", "2 sp.", "1d6 bludgeoning", 4, "Topple", "Versatile (1d8)"),
		Item("Sickle", "1 gp.", "1d4 slashing", 2, "Nick", "Light"),
		Item("Spear", "1 gp.", "1d6 piercing", 3, "Sap", "Thrown (range 20/60), Versatile (1d8)")
	],
	'Simple Ranged weapon  ': [
        Item("Crossbow, Light", "25 gp.", "1d8 piercing", 5, "Slow", "Ammunition (range 80/320), Loading, Two-handed"),
		Item("Dart", "5 cp.", "1d4 piercing", 0.25, "Vex", "Finesse, Thrown (range 20/60)"),
		Item("Shortbow", "25 gp.", "1d6 piercing", 2, "Vex", "Ammunition (range 80/320), Two-handed"),
		Item("Sling", "1 sp.", "1d4 bludgeoning", 0, "Slow", "Ammunition (range 30/120)")
	],
	'Martial Melee weapon  ': [
        Item("Battleaxe", "10 gp", "1d8 slashing", 4, "Topple", "Versatile (1d10)"),
        Item("Flail", "10 gp", "1d8 bludgeoning", 2, "Sap", "none"),
        Item("Glaive", "20 gp", "1d10 slashing", 6, "Graze", "Heavy, Reach, Two-handed"),
        Item("Greataxe", "30 gp", "1d12 slashing", 7, "Cleave", "Heavy, Two-handed"),
        Item("Greatsword", "50 gp", "2d6 slashing", 6, "Graze", "Heavy, Two-handed"),
        Item("Halberd", "20 gp", "1d10 slashing", 6, "Cleave", "Heavy, Reach, Two-handed"),
        Item("Lance", "10 gp", "1d12 piercing", 6, "Topple", "Reach, special"),
        Item("Longsword", "15 gp", "1d8 slashing", 3, "Sap", "Versatile (1d10)"),
        Item("Maul", "10 gp", "2d6 bludgeoning", 10, "Topple", "Heavy, Two-Handed"),
        Item("Morningstar", "15 gp", "1d8 piercing", 4, "Sap", "none"),
        Item("Pike", "5 gp", "1d10 piercing", 18, "Push", "Heavy, Reach, Two-handed"),
        Item("Rapier", "25 gp", "1d8 piercing", 2, "Vex", "Finesse"),
        Item("Scimitar", "25 gp", "1d6 slashing", 3, "Nick", "Finesse, Light"),
        Item("Shortsword", "10 gp", "1d6 piercing", 2, "Vex", "Finesse, Light"),
        Item("Trident", "5 gp", "1d6 piercing", 4, "Topple", "Thrown (range 20/60), Versatile (1d8)"),
        Item("War hammer", "15 gp", "1d8 bludgeoning", 2, "Push", "none"),
        Item("War pick", "5 gp", "1d8 piercing", 2, "Sap", "none"),
        Item("Whip", "5 gp", "1d4 slashing", 2, "Slow", "Finesse, Reach"),
	],
	'Martial Ranged weapon ': [
		Item("Blowgun", "10 gp.", "1 piercing", 1, "Vex", "Ammunition (range 25/100), Loading"),
		Item("Crossbow, hand", "75 gp.", "1d6 piercing", 3, "Vex", "Ammunition (range 30/120), Light, Loading"),
		Item("Crossbow, heavy", "50 gp.", "1d10 piercing", 18, "Push","Ammunition (range 100/400), Heavy, Loading, Two-handed"),
		Item("Longbow", "50 gp.", "1d8 piercing", 2, "Slow","Ammunition (range 150/600), Heavy, Two-handed"),
		Item("Musket", "500 gp.", "1d12 piercing", 10, "Slow","Ammunition (Range 40/120), Loading, Two-Handed"),
		Item("Pistol", "250 gp.", "1d10 piercing", 3, "Vex","Ammunition (range 30/90), Loading")
	]
}

def get_random_item(category):
	random.shuffle(categories[category])
	item = categories[category][0]
	
	content_lines = [
		f"Thoust hath found a {category.strip()}",
		f"Name: {item.name}",
		f"Damage: {item.damage}",
		f"Cost: {item.cost}",
		f"Weight: {item.weight} lbs",
		f"Mastery: {item.mastery}", 
		f"Properties: {item.properties}"
	]
	
	max_content_width = max(len(line) for line in content_lines)
	box_width = max_content_width + 4  # Accounts for borders and padding
	horizontal = '═' * (box_width - 2)  # Now correct for "║X...X║" format

	template = [
		f"╔{horizontal}╗",
		f"║ {content_lines[0].center(box_width - 4)} ║",
		f"╠{horizontal}╣",
		*[f"║ {line.ljust(box_width - 4)} ║" for line in content_lines[1:]],
		f"╚{horizontal}╝"
	]

	print('\n'.join(template))
	return item

# Generate and display random item
get_random_item(random.choice(list(categories.keys())))