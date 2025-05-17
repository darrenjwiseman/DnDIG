# D&D 5e Random Weapon Generator
# By Darren Wiseman & Borea-Phi-3.5-mini-Instruct-Coding.Q4_K_M
# 5/16/2025

class Item {
    [string]$Name
    [string]$Cost
    [string]$Damage
    [int]$Weight
    [string]$Properties

    Item([string]$name, [string]$cost, [string]$damage, [int]$weight, [string]$properties) {
        $this.Name = $name
        $this.Cost = $cost
        $this.Damage = $damage
        $this.Weight = $weight
        $this.Properties = $properties
    }
}

$categories = @('Simple Melee', 'Simple Ranged', 'Martial Melee', 'Martial Ranged')

$SimpleMelee = @(
    [Item]::new("Club", "1 sp.", "1d4 bludgeon", 2, "Light"),
    [Item]::new("Dagger", "2 gp.", "1d4 pierce", 1, "Finesse, Light, Thrown (range 20/60)")
	[Item]::new("Greatclub", "2 sp.", "1d8 bludgeoning", 10, "Two-handed"),
    [Item]::new("Handaxe", "5 gp.", "1d6 slashing", 2, "Light, thrown (range 20/60)"),
    [Item]::new("Javelin", "5 sp.", "1d6 piercing", 2, "Thrown (range 30/120)"),
    [Item]::new("Hammer, light", "2 gp.", "1d4 bludgeoning", 2, "Light, thrown (range 20/60)"),
    [Item]::new("Mace", "5 gp.", "1d6 bludgeoning", 4, "-"),
    [Item]::new("Quarterstaff", "2 sp.", "1d6 bludgeoning", 4, "Versatile (1d8)"),
    [Item]::new("Sickle", "1 gp.", "1d4 slashing", 2, "Light")
    )

$SimpleRanged = @(
    [Item]::new("Crossbow, light", "25 gp.", "1d8 piercing", 5, "Ammunition (range 80/320), loading, two-handed"),
    [Item]::new("Dart", "5 cp.", "1d4 piercing", 0.25, "Finesse, thrown (range 20/60)"),
    [Item]::new("Shortbow", "25 gp.", "1d6 piercing", 2, "Ammunition (range 80/320), two-handed"),
    [Item]::new("Sling", "1 sp.", "1d4 bludgeoning", 0, "Ammunition (range 30/120)")
)

$MartialMelee = @(
    [Item]::new("Battleaxe", "10 gp", "1d8 slashing", 4, "Versatile (1d10)")
    [Item]::new("Flail", "10 gp", "1d8 bludgeoning", 2, "-")
    [Item]::new("Glaive", "20 gp", "1d10 slashing", 6, "Heavy, reach, two-handed")
    [Item]::new("Greataxe", "30 gp", "1d12 slashing", 7, "Heavy, two-handed")
    [Item]::new("Greatsword", "50 gp", "2d6 slashing", 6, "Heavy, two-handed")
    [Item]::new("Halberd", "20 gp", "1d10 slashing", 6, "Heavy, reach, two-handed")
    [Item]::new("Lance", "10 gp", "1d12 piercing", 6, "Reach, special")
    [Item]::new("Longsword", "15 gp", "1d8 slashing", 3, "Versatile (1d10)")
    [Item]::new("Morningstar", "15 gp", "1d8 piercing", 4, "-")
    [Item]::new("Pike", "5 gp", "1d10 piercing", 18, "Heavy, reach, two-handed")
    [Item]::new("Rapier", "25 gp", "1d8 piercing", 2, "Finesse")
    [Item]::new("Scimitar", "25 gp", "1d6 slashing", 3, "Finesse, light")
    [Item]::new("Shortsword", "10 gp", "1d6 piercing", 2, "Finesse, light")
    [Item]::new("Trident", "5 gp", "1d6 piercing", 4, "Thrown (range 20/60), versatile (1d8)")
    [Item]::new("War pick", "5 gp", "1d8 piercing", 2, "-")
    [Item]::new("War hammer", "15 gp", "1d8 bludgeoning", 2, "-")
)

$MartialRanged = @(
    [Item]::new("Blowgun", "10 gp.", "1 piercing", 1, "Ammunition (range 25/100), loading"),
    [Item]::new("Crossbow, hand", "75 gp.", "1d6 piercing", 3, "Ammunition (range 30/120), light, loading"),
    [Item]::new("Crossbow, heavy", "50 gp.", "1d10 piercing", 18, "Ammunition (range 100/400), heavy, loading, two-handed"),
    [Item]::new("Longbow", "50 gp.", "1d8 piercing", 2, "Ammunition (range 150/600), heavy, two-handed")
)    

function Get-DnDItem {
    $itemType = Get-Random -InputObject $categories

    switch ($itemType) {
        'Simple Melee' {
            $item = Get-Random -InputObject $SimpleMelee
            $itemName = $item.Name
            $itemCost = $item.Cost
            $itemDamage = $item.Damage
            $itemWeight = $item.Weight
            $itemProperties = $item.Properties
        }
		
        'Simple Ranged' {
            $item = Get-Random -InputObject $SimpleRanged
            $itemName = $item.Name
            $itemCost = $item.Cost
            $itemDamage = $item.Damage
            $itemWeight = $item.Weight
            $itemProperties = $item.Properties
		}	
		
		'Martial Melee' {
            $item = Get-Random -InputObject $MartialMelee
            $itemName = $item.Name
            $itemCost = $item.Cost
            $itemDamage = $item.Damage
            $itemWeight = $item.Weight
            $itemProperties = $item.Properties
		}	

        'Martial Ranged' {
            $item = Get-Random -InputObject $MartialMelee
            $itemName = $item.Name
            $itemCost = $item.Cost
            $itemDamage = $item.Damage
            $itemWeight = $item.Weight
            $itemProperties = $item.Properties
		}	
	}	
    # Consistent formatted output box
    $template = @"
	
 o()xxxx[{::::::::::::::::::::::::::::>

+=======================================================+
| Thoust hath found a $itemType Weapon: 
+=======================================================+

+=======================================================+
| $itemName |                        
|-------------------------------------------------------+
| Cost:   $itemCost                           
| Damage: $itemDamage     
| Weight: $itemWeight lbs.
| Properties: $itemProperties  
+=======================================================+

+=======================================================+
| Thanks for generating loot! 
+=======================================================+

 o()xxxx[{::::::::::::::::::::::::::::>

"@

    # Display the formatted item information
    Write-Host $template
}

# Generate a random D&D item
Get-DnDItem