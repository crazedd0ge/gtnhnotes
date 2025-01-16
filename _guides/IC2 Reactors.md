---
title: IC2 Reactors
game: "GT New Horizons"
category: "Guide"
created: 2025-01-16
layout: default
nav_order: 10
parent: Guides
---

# IC2 Reactors

EU Reactors: 0 chamber 2x quad thorium, 320 EU/t

## Reactor Code:

An experimental "cheap" design, the idea being a reactor that was going to be used to power a fledgeling AE2 digital storage terminal, and thus (given the lack of autocrafting that is implied there) should be as cheap and simple to craft as possible. The result, as is the case with most of these experiments, was a failure of a design looking for an actual problem to solve or a big enough shift in mechanics to actually make it relevant. All the same, if you need the cheapest starter reactor possible, this is a candidate at least

0 chamber/3 chamber 3x quad thorium, 520 EU/t Reactor Code (0c):

## Reactor Code (3c):

A testament to the design challenge that is only using low tier reactor components. What's possible with 0 chamber and good components takes 3 chambers to do with basic ones

0 chamber 2x dual uranium, 600 EU/t

## Reactor Code:

It's possible to get uranium in small quantities from Nether Thorium ores, and from there various magical shenaniganry can yield 235 to create uranium fuel rods. That said this, like it's Thorium version before it, is an experiment offering a solution that's looking for a problem to solve

6 chamber 16x quad thorium, 2560 EU/t

## Reactor Code:

The, to my knowledge, highest EU/t output mark 1 (as in can run 24/7 without overheating and/or needing maintenance) EU reactor design that uses Thorium fuel cells. Extremely useful in early EV to supplement power to EBFs, which takes a major load off of your (probably strained) fuel pipeline

Fluid Reactors: 6 chamber 6x quad uranium pulse, ~1714.43 HU/s | Neutron Reflector version, ~1.667.56 HU/s Reactor Code:

## Reactor Code (R):

The culmination of all of my experimenting with pulse reactors - as in reactors that have a timed on period and timed off period, pulsing between the two continuously - and how to get maximum output out of them. This "Joker V2" design is the best I came up with, able to put out more HU/s on average than a single LHE is able to process. While that's impressive on paper it's not necessarily a good design - burning fuel for byproducts is half the reason you use reactors in modded, and producing more than you can process is likewise not beneficial. All the same it stands as a testament that if you're willing to taunt Death and replace sanity with redstone control pulse fluid reactors can, in theory, work

The version with neutron reflectors is more expensive and can't manage as much output due to the way that the heat numbers work out. All the same, if you want the singular most efficient fluid reactor possible, there you have it. If IC2 mechanics can do better I don't know how you'd manage it For the record, I calculated the neutron reflector version to draw a total of ~44.99G EU out of a full fuel cycle though Large HSS-E rotors, or 1874593000 EU per individual single uranium rod. If the 40x quad rod vacuum design was that energy dense it would output ~749837 EU/t instead of 43600 EU/t

6 chamber 16x single MOX/8x dual MOX heat neutral, 768 HU/s Reactor Code (s):

## Reactor Code (d):

After a brief stint of testing heat neutral MOX designs this is the best I could come up with for fluid reactors. MOX fluid reactors work differently from EU reactors in that rather than producing more power gradually MOX fuel cells in fluid reactors produce 2x heat if the reactor heat is >50%. Dealing with

## that much heat in a heat neutral manner is...hard

6 chamber 3x quad uranium, 1120 HU/s

## Reactor Code:

A "stable" fluid reactor design, meaning that aside from a single startup tick it should always produce exactly 1120 HU/s. Not as powerful as unstable designs, and despite the term supposedly "unstable" designs aren't actually unstable in any relevant sense of the word. But I like to edge on the side

## of paranoia with nuclear reactors

6 chamber 16x quad thorium, 1280 HU/s

## Reactor Code:

A "stable" Thorium fuelled fluid reactor design that maximizes output at the cost of...everything else. "Hideously inefficient" would be a compliment to this thing, but in GT reactor fuel efficiency is never the concern, only raw power output

6 chamber 7x quad thorium, 792 HU/s

## Reactor Code:

At one point I experimented with the concept of a "starter" fluid reactor, and this was the (least stupid) result. This design outputs as much regular steam as I could get a reasonable(-ish) design to manage, and processed through 5 Medium Shadow Metal rotors (underfed 3168/3200) produces 9370 EU/t Using Medium Terrasteel rotors, if you're that invested into Botania in GTNH for some incomprehensible reason, would push the output to a flat 5A EV or 10240 EU/t. The design is "cheap" insofar that it doesn't require Tungstensteel (Terrasteel needs Radon for an EV PLE), but the titanium cost of the reactor and Large Heat Exhanger combine to around 15-16 single block EV combustion gens, or around 20-21 single block EV gas gens. I trust that 5<15 doesn't need further explanation? Of course not. The failure of this design - of fluid nukes in general in GTNH - is probably self evident

Uranium/Thorium Breeders: 6 chamber 20× mixed, 2400/4000 EU/t

## Reactor Code:

An old breeder design able to run Quad Thorium or Dual Uranium cells. There's ways to stuff more rods inside a single reactor, but this one is cheap(-ish)/easy to automate

0 chamber 12x single Thorium, 320 EU/t

## Reactor Code:

There's few situations where you'd reasonably run a reactor like this, but in the event that you wanted to power your early digital storage terminal off of a 0 chamber reactor while burning single thorium rods for their unique byproducts (no, you can't just cut depleted dual/quad rods into singles, that would

## make far too much sense) it's one you could use

Lithium Breeders (cold): 6 chamber 3x lithium 10x quad thorium, 1200 EU/t

## Reactor Code:

A 2.2.3 Sunnarium Breeder/power reactor hybrid design due to a bug with glowstone rods in that version, now still working as a lithium breeder as they have the mechanics that glowstone rods had, but shouldn't have had in 2.2.3. This design is as automation friendly as lithium breeders get, just mind the fact that lithium breeders are completely useless

0 chamber 5x lithium 4x dual thorium, 160 EU/t

## Reactor Code:

A less automation friendly, but highly compact and still reasonably automation friendly design. Turns the centre lithium rod every 1250 seconds, and the others every 2500 seconds. If your automation is on point this will effectively convert 6 rods every 2500 seconds, and 120 rods per Thorium fuel cycle

5 chamber 15x lithium 15x single thorium, 150 EU/t

## Reactor Code:

Bigger 5 chamber version of the "standard" 2 chamber lithium breeder design(?). Less automation friendly than the two above, but if that's your jam here's a bigger version

Note: The way that Lithium fuel rods work is that they act as neutron reflectors for the purposes of reactor heat calculations, hence why the reactor designs include them where you would normally place lithium fuel rods. It makes it easier to design the reactor, since the heat calculations are the same

Glowstone Breeders (cold): 6 chamber 5-10x glowstone 14x quad thorium, 1680 EU/t

## Reactor Code:

A retrofit of the 2.2.3 breeder/EU reactor hybrid. If you want maximum automation friendliness keep the reactor platings, if you want maximum sunnarium breeding at the cost of automation complications replace the reactor platings with glowstone rods. They won't turn as quickly as the ones that are completely surrounded by quad rods, but they will turn

0 chamber 5x glowstone 4x quad thorium, 480 EU/t

## Reactor Code:

Retrofit of the compact zero chamber 2.2.3 design. Note that as-is this design is not expandable - adding more chambers and expanding the setup will result in a meltdown. More specifically this design extracts exactly as much heat as it generates. Adding another slice adds 75% more heat, but less

## than 75% more cooling. Then explosions ensue...

6 chamber 14x glowstone 13x quad thorium, 1560 EU/t

## Reactor Code:

The above design expanded and fixed to support six chambers worth of fuel/glowstone rods. Not the most automation friendly, but an upgrade if you started with the prior design

6 chamber 21x glowstone 21x dual thorium, 840 EU/t

## Reactor Code:

Retrofit of the 2.2.3 "just throw everything at the reactor and see what sticks" design. Very automation unfriendly, but if you want as many rods in a reactor as possible, viola

Note: The above designs have only been tested in the reactor planner and briefly in survival, they have not been stress-tested to confirm they can run continuously I'd say "prepare accordingly", but if you're the type to plop down reactors out in the open in any event than frankly I don't know what to tell you, let stand how to convince you

Glowstone Breeders (hot): 0 chamber, 2x glowstone, 4x quad thorium, heat neutral, 480 EU/t | 6 chamber, 6x glowstone, 12x quad thorium, heat neutral, 1440 EU/t Reactor Code (0c):

## Reactor Code (6c):

One mechanic you might have missed, despite it being mentioned in both the questbook and NEI, is that lithium/glowstone rods gain a 100% progress bonus for every 3000 heat units a reactor hull has while the glowstone/lithium is running. This bonus applies to every 3K heat regardless of a reactor's maximum temperature (well...so long as you don't exceed a reactor's maximum temperature limit, of course), so adding Heat-Capacity Reactor Plating to get more heat to get a bigger bonus is a perfectly valid (if risky) strategy

Once heated up to 15K (o chamber)/27K (6 chamber) these reactor designs will turn two rods every 209s/six rods every 125s respectively. The six chamber reactor could go as high as 33K heat, but at 85% of a reactor's maximum heat capacity it starts to damage the environment, so I decided to use that as a safety cutoff point (for a given definition of "safety")

You can use dual uranium rods instead of quad thorium rods in these designs. It would increase power output to 800 EU/t/2400 EU/t, but halve the production rate of sunnarium

Note: For whatever reason the reactor planner thinks that Heat-Capacity Reactor Plating only adds 1700 heat capacity to a reactor, when ingame testing confirms it actually adds 2000 per plate. The above reactor designs will work regardless, but with the lower heat capacity 15K/27K will be in excess of 85% of the total capacity in both cases. Remember to use a Portable Scanner on a reactor to double-check it's maximum heat capacity before heating one up

Hybrid Breeders (hot): 6 chamber, 6x glowstone/lithium, 24x quad thorium/uranium, heat neutral, coolant cells, 3.440 EU/t (Thorium) / 17.200 EU/t (uranium)

## Reactor Code:

In a moment of mad inspiration I realized that breeding glowstone/lithium in a heat neutral reactor, and vacuum reactors, are not mutually exclusive concepts. Thus, behold the final word in glowstone/lithium breeders: A vacuum/breeder hybrid capable of turning 6 rods every 63s...minus the requisite downtime to replace rods and/or coolant cells. Not sure how long that step takes, but you can have extra coolant cells on hand so that the vacuum freezer process, at least, doesn't cost additional time overall

If prior designs were solutions looking for problems to solve, this design is a flashing neon sign highlighting the sheer powerlessness of glowstone/lithium breeder reactors. Yes, on the glowstone/sunnarium side 6 sunnarium every 63+ seconds is much faster than 2 every 325s using the IV autoclave recipe, and doesn't require a ton of power/UUM besides. But setting up a reactor like this would be an ordeal not even remotely worth the reward it offers, assuming you can keep this volatile monster running stable for any length of time

On the lithium/trinium side...well, I've got bad news and I've got worse news. The bad news is that, assuming you can keep the reactor running 98.4375% of the time, you'd need just over 52 of these hybrid breeder reactors to keep one fusion reactor fed, producing one of the weakest (but cheapest) plasmas for power production. The worse news is that if you run this recipe for longer than eight minutes continuous you'd have been better off using a different recipe altogether. For the record, eight minutes is nothing to fusion reactors

If you want to undertake the redstone challenge that is setting up and optimizing a vacuum/breeder hybrid reactor like this, go for it. But efficiently? Laugh at this joke and move on

Tips and tricks: Transvector Interfaces can be used to insert steam into steam tubrines remotely, allowing multiple fluid regulators to stack effectively. That said these days Fluid P2P is able to feed regulated amounts of steam so long as the input amount is correct, so this particular bit of trivia is sadly a relic

IC2 reactors (which is shared with other IC2 power generators, I believe) are really weird and bizarre in how it provides - not sends - power. You can connect a 2A EV cable to two sides of the 2.560 EU/t reactor (this does matter, as each side can only output 1A max), and send this power into an EV Battery Buffer. This will extract all the power (minus 2EU/t lost to cable loss) the reactor produces despite it producing more than 1A EV total, and it sending the power into an EV battery buffer. Hell, you can feed an HV battery buffer the same way if you can connect to enough sides. Transformers also work, although note they will run into the 1A per side limit just as much as cables will

When hooking up IC2 reactors always double-check that it is outputting the full amount of power it produces. They are very finicky, and prone to not registering valid power outputs/requestors without breaking/replacing transformers and/or cutting/resetting cable connections

Never place an IC2 reactor, of any variety, out in the open without something to stop it from exploding your entire base in the event that it does explode. Yes, you're using "safe" designs that shouldn't ever explode and all of that jazz. Still cover your reactor in either blocks warded by the Warding Focus, outright Warded Glass, or another sufficiently explosion proof block. Something is going to go horribly wrong before all is said and done. And if that is an unshielded IC2 reactor you'll be send right back to the stone age

Redstone Free Vacuum Nukes (an amount of Stainless Steel/Diamonds required)

Always wanted to try your hand at vacuum nukes, but were put off by the idea of needing to program half of a computer with redstone to run it? There is a way to brute force vacuum reactors with zero redstone, although it has more than a few problems/shortcomings. "Not safe from TPS lag" included

The idea is simple: Use Extra Utilities Transfer Nodes with a full stack of Speed Upgrades, a valid inventory to export/import items from directly next to them (to minimize time spend looking for said inventory), and a filter on the extract. Transfer nodes with full speed upgrades are so fast they can move even multiple items sub 1 second, which is the rate at which an IC2 reactor runs, so you can swap out coolant cells for new ones without having to stop the reactor

Of course I mentioned downsides, and yes, there are many. For one this speed is dependant on the reactor, transfer node and relevant inventory being directly adjacent, so don't expect this setup to expand beyond one reactor. Extra Utilities Filters also cannot be copied or filled with NEI ghost items, like EnderIO filters can, so you have to keep samples around to set more filters manually if you want to set up more reactors. Those speed upgrades are also not cheap,  and you're going to need two stacks (at most, I've not tested the minimum amount required and frankly I don't want to) per reactor. In addition to all of that this filtering system cannot handle inputting and outputting more than one type of item, since the only method it has to determine where to put an item is "there's no item there", whether that slot should be a fuel rod or something else. And when a reactor design, by definition, requires fuel rods and coolant cells to be cycled at minimum...well, you can see where this limitation becomes a problem. And, of course, the idea of "transfer nodes work faster than a reactor" relies on a stable TPS to actually make that the case. If it isn't, well, hope you warded your reactor

Now, adding a bit of redstone could solve some of these issues - tranfer nodes do turn off when given a redstone signal, so you could have a system that turns off coolant cells input/output when empty fuel cells are detected, switches on a separate system to swap the fuel rods, and than toggles both again before turning the reactor back on - but at that point there's less merit to using transfer nodes. Their big claim to vacuum nuke fame is being fast enough to hotswap items while a reactor is running, if a reactor is turned off to swap items you could be using much cheaper item conduits instead

So in what circumstances would one consider using transfer nodes to hotswap reactor components? Well, if you're fine with swapping fuel rods manually I could see them being used for sunnarium breeder reactors, of all things. The hot glowstone breeder that doesn't rely on coolant cells needs to swap glowstone rods every 63 seconds, whereas it needs to swap quad thorium fuel rods every 50000 seconds, or ~13 hours and 53 minutes. Using transfer nodes to hotswap glowstone rods automatically while changing the fuel manually every almost 14 hours seems halfway reasonable if you don't want to set up some kind of redstone automation to automate it fully

For the record, the six chamber hot glowstone breeder design above produces 2394 sunnarium dust worth of rods every 50000 second fuel cycle, producing 1.44G EU in total. About 2.5% of this will be needed to thermally centrifuge the glowstone rods using three (really ~2.38) LV thermal centrifuges For contrast, the IV autoclave recipe needs 448875 seconds (124.6875 days) worth of processing time to produce that amount of sunnarium, as well as 68.9472G EU and 1197mb UUM (itself 985178880 EU unless using UUA, which ~quarters the EU cost). And a source of Glowcoral, of course

## LZH Cooling (Lapis EIG Vac Nukes)

Something you may have heard about is the idea of using LZH Condensators to run vacuum nukes instead of traditional coolant cells. Rather than being ran through a Vacuum Freezer like traditional coolant cells, LZH is cooled by crafting it with 8 lapis dust to reset it to full durability. An Extreme Industrial Greenhouse running Lazulia - a Thaumic Bases plant that grows lapis, if you were unaware - alongside a Maceration Stack can be used to supply bulk amounts of lapis passively, enough to supply many vacuum nukes. The only cost is power. So, is it worth using LZH Condensators?

Assuming the standard 40 quad fuel rods design (the design is on the official wiki, if you wish to look at it), using uranium fuel rods to produces 17.44G EU across one full fuel cycle, you'll run through either 2292 LZH Zondensators or 640 360K NaK coolant cells (this number includes partially damaged condensators/coolant cells left in the reactor after the fuel rods have run out). Using an EV EIG and MV T2 Maceration Stack it'll cost 25881.5 EU per LZH refill, for a total of 59320398 EU. NaK coolant cells instead consume 43200 EU per refill, for a total of 27648000 EU. ~0.34% and ~0.16% of the total amount of power produced spend on coolant maintenance by LZH Condensators and traditional coolant cells respectively

Being little over twice as expensive EU-wise seems like a good reason not to use LZH Condensators, so in what strange circumstances might they be useful anyway? The only argument I could make for them is scale. Being twice as expensive is never good, and if you're scaling up through overclocking that of course isn't going to get any better, but 1.36% percent in maintenance is still very solid as far as energy investment to payoff ratios are concerned, and it's not like vacuum freezers can escape overclocking either (they theoretically could with a redstone controlled Mega Vacuum Freezer, but...no)

So, scale: 360K coolant cells take 18s to be refilled at MV power, meaning you need 11520s worth of refill per 20000s worth of fuel cycle. Thus, in theory, one MV vacuum freezer should be able to support ~1.7 vac nukes. LZH needs 18336 lapis dust per fuel cycle, and an EV EIG will produce lapis at a rate of 64 every 100 ticks, or 12.8/s. Meaning 1432.5s per 20000s fuel cycle, or ~13.9 vacuum nukes per EV EIG/MV T2 Maceration Stack combo. For context, each 40x quad rod vacuum nuke puts out 43600 EU/t with uranium, or up to 99184 EU/t with MOX at 8499/10000 reactor hull heat

"How am I supposed to automatically craft LZH Condensators to refill them", you ask? Transfer Nodes with a World Interaction upgrade can do that sort of crafting quite well. Or you could use a Molecular Assembler as a standaslone autocrafting table. Just make sure that what you use is fast enough

