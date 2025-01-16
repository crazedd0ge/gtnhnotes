# Blood Magic Guide for GTNH Modpack

## Complex Mining Spell

| Spell Type | Blocks Mined | LP per cast | Orb/Altar |
|-----------|--------------|-------------|-----------|
| Unstable | 6 | 11 | Tier 4 |
| Standard | 24 | 52 | Tier 5 |
| Reinforced | 83 | 205 | Tier 5 |
| Imbued | 289 | 756 | Tier 6 |

### Notes
1. Effect and cost of the Blood Magic complex spell combination (Projectile -> Earth -> Environment)
2. The questbook erroneously claims the Unstable tier only requires a T3 blood orb, but Power/Reduction/Potency Cores require at least a T4 blood orb
3. LP cost assumes the maximum amount of Spell Dampeners to reduce the LP cost
4. Minimum tier of Blood Orb (and Altar) required to craft this tier of complex spell

## Blood Altar LP Generation

| Tool | LP | (S)Sac. Bonus | Blood Rune | Speed Rune | (Self-)Sacrifice Rune | Augmented Capacity | Rune of the Orb | Superior Capacity | Dislocation | Acceleration | Quickness |
|------|-----|---------------|------------|------------|----------------------|-------------------|-----------------|------------------|--------------|--------------|-----------|
| Sacrificial Knife | 125 | 15 | 40 | 168 | 668 | 5566.666667 | 908 | 7872 | 7856 | 668 | 22708 | 66108 |
| Sacrificial Knife (Wood Ash) | 360 | 43 | 13.88888889 | 58.33333333 | 231.9444444 | 1941.860465 | 315.2777778 | 2733.333333 | 2727.777778 | 231.9444444 | 7884.722222 | 22954.16667 |
| Sacrificial Knife (Byrrus) | 480 | 57 | 10.41666667 | 43.75 | 173.9583333 | 1464.912281 | 236.4583333 | 2050 | 2045.833333 | 173.9583333 | 5913.541667 | 17215.625 |
| Sacrificial Knife (Livens) | 660 | 79 | 7.575757576 | 31.81818182 | 126.5151515 | 1056.962025 | 171.969697 | 1490.909091 | 1487.878788 | 126.5151515 | 4300.757576 | 12520.45455 |
| Sacrificial Knife (Viridis) | 900 | 108 | 5.555555556 | 23.33333333 | 92.77777778 | 773.1481481 | 126.1111111 | 1093.333333 | 1091.111111 | 92.77777778 | 3153.888889 | 9181.666667 |
| Sacrificial Knife (Purpura) | 1200 | 144 | 4.166666667 | 17.5 | 69.58333333 | 579.8611111 | 94.58333333 | 820 | 818.3333333 | 69.58333333 | 2365.416667 | 6886.25 |
| Glass Sacrificial Dagger | 500 | 60 | 10 | 42 | 167 | 1391.666667 | 227 | 1968 | 1964 | 167 | 5677 | 16527 |
| Dagger of Sacrifice (Animals) | 250 | 30 | 20 | 84 | 334 | 2783.333333 | 454 | 3936 | 3928 | 334 | 11354 | 33054 |
| Dagger of Sacrifice (Hostile mobs) | 500 | 60 | 10 | 42 | 167 | 1391.666667 | 227 | 1968 | 1964 | 167 | 5677 | 16527 |
| Dagger of Sacrifice (Villagers) | 1000 | 120 | 5 | 21 | 83.5 | 695.8333333 | 113.5 | 984 | 982 | 83.5 | 2838.5 | 8263.5 |

### Notes
1. LP received per heart/mob sacrificed (assumes zero Runes of (Self-)Sacrifice)
2. Incense Crucible reagents
   - Must be activated in order
   - Can be set up in a line
   - Automatically trigger incenses
   - Emit flame particles when activating
3. Incense causes high LP generation but leaves you with low health
4. LP listed is per heart sacrificed
5. Glass Sacrificial Dagger can inflict Blindness and Bleeding debuffs
6. Blood Rune shows hearts/mobs needed to craft runes
7. (Self-)Sacrifice Rune shows crafting and payback costs
8. Superior Capacity becomes more efficient at 15 runes
9. Approximate LP cost of crafting runes
10. Quickness Rune reduces Blood Altar crafting time delay by 20% per rune

## Blood Magic Progression

### The WoS (Will of Sacrifice) Rush

Blood Magic progression in GTNH can be summed up in two words: **WoS Rush**. The LP costs are incredibly high, so the only reasonable path is rushing automated LP generation.

#### Requirements for WoS Setup
- T4 Blood Altar (Dusk inscription tool)
- T3/Magician's Blood Orb (50K LP network storage)
- Weak Activation Crystal
- Master Ritual Stone
- 36 Ritual Stones
- Titanium Screws
- Robust Thaumcraft infrastructure
- Void Metal blocks (16 needed for T4 altar)

#### Total Setup Cost
Approximately 1,924,500 LP or 15,396 sacrificial dagger stabs.

### Progression Tips

1. **Follow the Questbook**
   - Yields coins and lootbags
   - 10 Vampire coins can save ~9000 LP on Blank slates

2. **Patience is Key**
   - Don't rush
   - Build Thaumcraft infrastructure
   - Gain more hearts

3. **Sacrifice Strategy**
   - Upgrade to Dagger of Sacrifice ASAP
   - Set up Alien Villager spawner
   - Avoid self-sacrifice if possible

4. **If Self-Sacrificing**
   - Use Incense
   - Rush Glass Dagger of Sacrifice
   - Minimize health loss

5. **Rune Optimization**
   - Runes of (Self-)Sacrifice can pay off
   - Consider their crafting cost

6. **Thaumcraft Infusion**
   - Ritual Stones have two recipes
   - Arcane Workbench: 109,500 LP/stone
   - Infusion: 25,000 LP/stone
   - Recommended: Use Infusion recipe

## Alchemical Reagent Routing

### Tools for Ritual Boosting

1. **Alchemic Calcinator**
   - Furnace-type block
   - Converts solid reagents into ritual booster fuel
   - Requires bound blood orb and LP
   - Can receive reagents manually or via pipes

2. **Alchemic Cleanser**
   - Removes destinations from senders
   - Works across all reagent types
   - Right-click senders to clear linked receivers

3. **Alchemy Relay**
   - Can receive reagents from 16+ senders
   - Can send to up to 5 receivers
   - Limited to 2 reagent tanks

4. **Alchemic Router**
   - Designates senders and receivers
   - Shift-right click to bind reagent types
   - Right-click to set sender/receiver connections

5. **Alchemic Segmenter**
   - Limits reagent "tanks" for specific reagent types
   - Shift-right click to bind reagent type
   - Right-click to cycle through tank numbers

6. **Crystal Belljar**
   - Stores prepared reagents
   - Holds 16K worth of prepared reagent
   - Retains inventory when broken

### Routing Setup Process

1. Set up Alchemic Calcinator with bound Blood Orb
2. Feed solid reagents (manually or via hopper)
3. Use Alchemic Router:
   - Shift-right click air to clear prior connections
   - Shift-right click Alchemic Calcinator to bind reagent type
   - Right-click Alchemic Calcinator to set as sender
   - Right-click Master Ritual Stone or Belljar to set as receiver
   - Shift-right click air again to clear connections

**Pro Tip**: Orbis Terrae is the best reagent for boosting Mark of the Falling Tower ritual, providing +2 radius to summoned meteors.

## Blood Money: External LP Storage

### Functionality
- Available with T3 altar
- Can be compressed into 4x, 16x, and 64x versions
- Right-click to add LP to network
  - 10K per sheet (10K, 40K, 160K, or 640K depending on compression)

### Strategic Use
- Instantly adds LP to network
- Prevents wasting excess LP generation
- Allows storing LP outside primary network
- Useful for preparing for high-LP rituals like meteor summoning

## Optimizing Blood Flow

### Rune Configuration

#### T5 Altar Setup
- 16 Orb Runes
- 2 Augmented Capacity Runes
- 43 Sacrifice Runes
- 47 Speed Runes
- Produces/consumes 15,400 LP per WoS tick

#### T5 Altar with HV World Accelerator
- 16 Orb Runes
- 6 Augmented Capacity Runes
- 86 Sacrifice Runes
- Produces/consumes 28,300 LP per WoS tick

### Crafting Configurations
- 30 Sacrifice Runes
- 60 Speed Runes
- Can use Transvector Dislocators to swap rune configurations

### T6 Altar Strategies
1. Individual altars with separate WoS rituals
2. Centralized control with single altar
3. Dedicated LP generation altar feeding other altars

#### Sample T6 Generation Altar
- 19 Acceleration Runes
- 11 Augmented Capacity Runes
- 12 Dislocation Runes
- 142 Sacrifice Runes
- Produces 45,100 LP per WoS tick (≈1,804 LP/t)

## Early Blood Shards

### Weak Blood Shard Acquisition
- Use Bound Blades
  - Apply Weakness IV debuff
  - Killing debuffed enemy has chance to drop shard
  - Looting increases drop chance

### Alternative Methods
1. Thaumcraft Pech's Curse
   - Requires Potency IV
   - Nightshade upgrade ensures Weakness IV

2. Witchery Weakness Potion
   - Complex brewing system
   - Requires Attuned Stone (Charged)
   - Recommended to buff duration and extent

**Brewing Recipe**:
1. Nether Wart
2. Fermented Spider Eye
3. Glowstone Dust
4. Blaze Rod
5. Attuned Stone (Charged)
6. Redstone Dust
7. Obsidian
8. Blaze Powder
9. Wood Ash
10. Cocoa Beans
11. Gunpowder

## Runes of the Orb

### LP Capacity Considerations

| Blood Orb | LP Capacity | LP per Rune | Meteor LP Cost | Runes Needed |
|-----------|-------------|-------------|---------------|--------------|
| Archmage (T5) | 10M | 400K | 12.5M | 7 |
| Transcendent (T6) | 30M | 1.2M | 44M | 12 |
| Eldritch (T7?) | 80M | 3.2M | 90M | 4 |

**Note**: Minimum runes shown. More runes can be added for additional LP storage and meteor summoning flexibility.

## Meteor Summoning Tips

### Placement Strategy
- Place Master Ritual Stone at chunk border for optimal mining
- Use 4x Multiblock Miners (16-block range)
- Allows efficient meteor mining
- Consider mining fluid, item output, and mining pipe logistics

### Additional Considerations
- Mining time varies (6.5+ hours for large meteors)
- Multiblock Miners auto-disable when out of blocks
- Use Warding Focus to protect stopper block
- Balance investment in miners and mining speed

## Spell of the Diligent Tinkerer

- Adds modifier slot to Tinker's tools
- Requires Dusk runes
- Consumes 100K LP per tool
- Each tool can only go through ritual once
- Questionable value with Tungstensteel tools

## Meteor Catalysts Overview

### Detailed Meteor Catalysts Table

| Catalyst | LP Cost | Base Radius | Stone | Notable Output |
|----------|---------|-------------|-------|---------------|
| Melon | 123,456 | 8 | Yes | 16 different Stained Glass colors |
| Emitter (LV) | 300,000 | 16 | Yes | Pre-space ores (Tantalite, Copper) |
| Sensor (LV) | 300,000 | 18 | Yes | Oilsand |
| Exquisite Diamond | 420,000 | 13 | Yes | Large Graphite, Coal, Diamond |
| End Stone | 500,000 | 12 | Yes | HEE ores (including Stardust Ore) |
| Firestone Lens | 500,000 | 12 | Yes | Various gemstone ores |
| Sensor (HV) | 500,000 | 13 | No | T1/T2 ores (Bastnasite, Molybdenum, etc.) |
| Heavy Duty Alloy Ingot T1 | 500,000 | 20 | Yes | Moon Rock and related materials |
| Field Generator (LV) | 600,000 | 20 | No | Mica and Sodalite ores |
| Cheese | 650,000 | 15 | Yes | Unique ores (Cassiterite Sand, Diatomine, etc.) |
| Nether Star | 750,000 | 9 | No | Rutile ore |
| Heavy Duty Alloy Ingot T2 | 750,000 | 20 | Yes | Mars, Deimos, Phobos rocks |
| TNT | 775,000 | 20 | Yes | Marble, Basalt, Granite varieties |
| Sanitizing Soap | 800,000 | 15 | Yes | Rare Thaumcraft and Shadow Metal ores |
| Heavy Duty Alloy Ingot T3 | 1,000,000 | 20 | Yes | Callisto Ice, Ledox, Chrome, Iridium ores |
| Field Generator (HV) | 1,000,000 | 18 | Yes | Tricalcium Phosphate, Apatite, Tantalite |
| Heavy Duty Plate | 1,000,000 | 20 | Yes | T3 planet stones |
| Advanced Replicator | 1,200,000 | 18 | No | Nether ores, Firestone |
| Field Generator (IV) | 1,500,000 | 16 | Yes | T3 ores, Adamantium, Ardite |
| Advanced Assembling Machine III | 2,000,000 | 9 | No | End versions of Galena, Lead, Silver ores |
| Emitter (HV) | 2,000,000 | 16 | No | Moon ores |
| Advanced Mass Fabricator IV | 2,500,000 | 12 | No | Endstone Thorium, Uranium ores |
| Advanced Circuit Assembler II | 3,250,000 | 18 | Yes | Various pre-space to T3 ores |
| Soul Sand | 5,000,000 | 16 | Yes | Soul Sand only |
| Advanced Mass Fabricator II | 6,000,000 | 24 | No | T1 and T2 ores (Titanium, Tungsten, Indium) |
| Pufferfish | 6,666,666 | 16 | Yes | Saltpeter Ore |
| Heavy Duty Plate Tier 4 | 7,500,000 | 20 | Yes | T4 planet stones |
| Boxinator | 10,000,000 | 18 | No | Ross128b Bartworks ores |
| Heavy Duty Plate Tier 5 | 10,000,000 | 20 | Yes | T5 planet stones |
| Advanced Scanner IV | 12,500,000 | 14 | No | Platline-related ores |
| Heavy Duty Plate Tier 6 | 15,000,000 | 20 | Yes | T6 planet stones (moons) |
| Crystalprocessor Mainframe | 25,000,000 | 16 | No | Naquadah and related ores |
| Heavy Duty Plate Tier 7 | 30,000,000 | 20 | Yes | T7 planet stones |
| Elite Recycler | 44,000,000 | 16 | Yes | Enceladus Snow, Mysterious Crystal Dust |
| Wetware Supercomputer | 50,000,000 | 14 | No | Endstone Galena and Sphalerite ores |
| Heavy Duty Plate Tier 8 | 50,000,000 | 20 | Yes | T8 planet stones |
| Advanced Circuit Assembler VI | 80,000,000 | 16 | No | Rare Earth and advanced chemical ores |
| Bloody Ichorium Fusion Casing | 90,000,000 | 32 | No | Endstone gem-type ores |
| Elite Mass Fabricator II | 100,000,000 | 22 | No | T3-ish materials, Cosmic Neutronium |
| Advanced Crop Synthesiser VII | 125,000,000 | 18 | No | Endstone precious materials |
| Ion Thruster Jet | 1,000,000,001 | 16 | No | Raw Tengam Ore, Salt |
| Space Mining Module MK-III | 1,000,000,001 | 16 | No | Tartarite Ore |

**Note**: LP costs and outputs are subject to game balance and may change with modpack updates.
