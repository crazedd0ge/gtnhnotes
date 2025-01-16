---
layout: default
title: Botania
---

# Botania

As with the bee tab, just some random observations and things discovered during testing. Botania's implementation in GTNH is...eccentric, let's say, so I don't have much to say about it

| Generating Flora | Mana produced | ManaRF/t output (estimated) | Notes |
|:---|:---|:---|:---|:---|:---|
| Daybloom | 60000 RF/full life cycle | | 0.05 | | The amount of mana produced assume an entire lifecycle of continuous production. Note that Dayblooms require visible access to the sky in order to operate, Nightshades only care about it being nighttime |
| Nightshade | 60000 RF/full life cycle | | 0.05 | | Dayblooms and Nightshades are passive flowers, and will die after an hour. The one time you're forced to use passive flowers it's advisable to use Nightshades in the Twilight Forest, where it's always night |
| Beegonia | ~1000-6500 RF/drone | | 10 | | Beegonia's appear to generate a flat amount of mana, with the quality of the drone changing how long it takes for a new drone to be consumed. Meadow drones take 5 seconds to be consumed |
| Endoflame | 1500 RF/200 burn time | | 15 | | Endoflames don't fully benefit from fuels that have more than a listed burn time of 64000 on a solid fuel's tooltip, and cannot burn buckets/cells of fuel. Seems to burn fuel at a rate of 2 burn time per tick? |
| Hydroangeas | ~351000 RF/full life cycle | | 10 | | Hydroangeas is considered a "passive" flower, and will die after one hour of being planted. You could use them alongside Blood Magic's water ritual, but realistically Hydroangeas are straight useless in GTNH |
| Gourmaryllis | 77400 RF/Cucumber Salad (max) | | 700 | | The food value to mana calculation is - to put it politely - "interesting", making Cucumber Salad the best foodstock I've found that's easy to produce - you'll need one Lettuce and two Cucumber per salad |
| Narslimmus | (unknown, likely highly variable based on specific setup) | | | | Exclusively eats slimes that spawned naturally, not from mob spawners/spawn eggs/etc. Note, BTW, that Cursed Earth doesn't seem to like spawning stuff in light, and slimes don't spawn in dark underground |
| Rosa Arcana | 850 RF/xp | | 500 | | Cannot collect loose XP, and I don't know if it can draw experience from anything other than a player. As such likely to be manual, but powerful given a passive source of XP (mob farm, EEC, etc.) |
| Soarleander | 0 | | 0 | | Completely useless. It's a joke item that does nothing and has never done anything, the GTNH quest is either ignorant or trolling you. Though worth doing, still, if you're desperate for a chicken trophy |
| Thermalilly | 180000 RF/lava source block | | 26.08695652 | | Once fed lava produces mana for 45 seconds, then has a 300 second cooldown period. Produces 200 mana/t when actively running, making it an effective flower for bust production (in theory) |
| Entropinnyum | 65000 RF/TNT or Powderbarrel | | 600 | | Cannot consume exploding ITNT, IC2 Dynamite or creeper explosions. If you wish to run these flowers on other types of explosions you'll have you source your own research (and maybe an insurance policy) |
| Munchdew | 1600 RF/leaf | | 480 | | Can consume at least some of the leaves of non-vanilla trees (including Natura, Twilight Forest, Forestry and Pam's Harvestcraft)...for what that's worth... |
| Tainthistle | Very little per flux consumed | | ??? | | Tainthistles have a very hard time keeping up with 3x Transduction Aplifiers from Thaumic Horizons, if you were thinking of trying out that combination. Still useful as automatic, free flux cleanup, mind |
| Kekimurus | 108000 RF/cake | | 225 | | Will happily chow down on Pam's various cakes, but does not consume Blood Cake (Blood Arsenal) or Thaumic Cake (Forbidden Magic) |
| Rafflowsia | 21000 RF/flower | | 550 | | Only eats Dayblooms, Nightshades and Hydroangeas in this version. "How to get a passive supply of Goldenrod/Miner's Delight/Blue Hydrangea" you ask? Good joke. "Ingenious sages" my Endoflame foot... |
| Spectrolus | 3000 RF/wool | | 300 | | Try to source all colors of dyed wool using Chromatic Sheep from Thaumic Horizons and an unholy timer/redstone contraption if you really want a clown tier turbo masochistic build challenge, I guess? |

Dandelifeon

## Asgardandelion

Notes: [1] Flowers are listed by tier - red doesn't require anything, yellow requires mana, green requires runic altar, pink requires Titanium, blue requires elven trade (which, in turn, requires an IV Precision Laser Engraver), purple requires Gaia Spirits (Naquadah Plates), and Asgardandelion requires Infinity [2] Output is listed in RF because Botania hates giving you actual numbers, so alternative means are needed to figure them out. Or looking stuff up online/in the code, but where's the fun in that?

BTW, don't take the above table as confirmation that mana generation in GTNH isn't a problem easily brute forced. Botania is very much an afterthought, so in stark contrast to say Blood Magic's insane LP requirements Botania can get away with vanilla-tier setups...or slightly better, if you're impatient

| Mana Spreaders        | Basic | Elven | Gaia  |     |     |
| :-------------------- | :---: | :---: | :---: | :-- | :-- |
| Velocity lens         | 1200  | 1800  | 4800  |     |     |
| No lens               | 1600  | 2400  | 6400  |     |     |
| Potency/Velocity lens | 2400  | 3600  | 9600  |     |     |
| Potency lens          | 3200  | 4800  | 12800 |     |     |

The amount of RF worth of mana contained per burst depending on spreader tier and lens. Potency/Velocity transports mana the fastest, even when the spreader and target are directly adjacent Mana spreaders directly adjacent to their target, with Potency/Velocity lens, have a rough throughput limit of 800RF/t (basic), 1200RF/t (elven) and 3200RF/t (gaia). A regular Mana Spreader without a lens has a throughput limit of ~320RF/t, though of course if throughput is a concern you should lens it A regular mana pool holds ~5375000 RF worth of mana. Mana Tablets hold half that amount, and Diluted Mana Pools (apparently) hold one hundreth the amount of a regular mana pool

Note: Directly adjacent means directly. Binding a spreader to a mana pool next to it still has the slightest travel time that'll about halve transfer speed. Place a mana pool above the spreader instead if you don't feel like manually targeting a spreader to directly target an adjacent mana pool Using a Mana Distributor? Don't be fooled by it looking like a full block, if a mana spreader is bound to a distributor it has to shoot through the entire block to actually hit it, again greatly reducing potential mana throughput. You can manually target the edge of a distributor as you can a mana pool, though If you do manually target a mana spreader check that it's actually getting minimum travel distance on mana bursts. Even the slightest extra bit of distance will reduce the maximum throughput substantially - twice the distance = half the transfer rate, and you need minimum distance for max throughput

## Gourmaryllis details

A few more detailed notes about Gourmaryllis and how to automate them, given that they are a likely candidate for being your primary mana producer if you don't set up a massive Endoflame field (you could, but one optimal Gourmaryllis is worth ~46 endoflames, so...consider Gourmaryllis, perhaps):

First, and perhaps most critically, is the concept of Gourmaryllis' digestion system. It's explained broadly in the Lexica Botania, but there's two key details that are left out of the Lexica. One, Gourmaryllis have an internal mana buffer of 80K ManaRF, and as such cannot produce more mana per piece of food than that. "Is that a problem?" you ask, and the answer is a resounding "I have no idea who coded this". As mentioned above Cucumber Salad - a 2.5 hunger, 1 saturation food - is worth 77400 ManaRF per serving. Doesn't really leave a whole lot of room for, say, Epic Bacon to produce more, huh? But wait, there's more. Rice Soup, another food item worth 2.5 hunger and 1 saturation you would expect to be worth the same amount of mana, right? Nope, it's randomly worth only about a third as much mana per bowl of soup than cucumber salad is worth. Why? El turbo shruggo, basically

The second point left out is that Gourmaryllis can, in some cases, be bottlenecked on the mana spreader it's attached to rather than the speed at which it can digest food. For example Cucumber Salad takes 110 ticks or 5.5 seconds to digest, and produces an amount of mana that equates to the listed 700 manaRF/t output. Is your regular Potency/Velocity lens spreader not directly facing it's mana pool/distributor/fluxfield/etc., or perhaps missing said lens? If so you will be bottlenecked on mana output speed, and will have to slow down the feeding timer to avoid wasting mana production

So, TL;DR: for how to set up a good Gourmaryllis? Make sure that your basic mana spreader has minimal travel time between it and its target (there's some wiggle room, but not much), and has a Potency/Velocity combo lens. Do not bother upgrading the spreader to Elven, it will not allow you to put two Gourmaryllis on a single spreader unless you slow down their food consumption rate. Speaking of which, if the spreader is correctly set feed the Gourmaryllis a Cucumber Salad every 110 ticks or 5.5 seconds. If you later upgrade to Gaia spreaders you can support 4 Gourmaryllis per spreader

Tips and tricks: You can plant mystical petals on dirt/grass, apply fertilizer to grow it (it won't grow naturally) into a tall flower, and then harvest the tall flower with shears (which are required) to get it. This process functionally turns fertilizer into mystic petals, as each tall flower can be extracted into four mystical petals Note that IC2 fertilizer will not work for this, but bonemeal and Forestry fertilizer will

Goldenrod appear to be abundant in Prairie biomes, whereas Miner's Delight spawns in caves underground

Managlass is considered an EV tier glass, meaning you can use it in place of Reinforced Glass in recipes which need any EV tier glass. Alfglass is similarly considered an IV tier glass, but crafting an Elven Portal to trade for Alfglass requires an IV Precision Laser Engraver, so don't count on it saving you much (if any) effort crafting the IV tier Borosilicate glass instead
