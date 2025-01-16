---
layout: default
title: Pollution
---

# Pollution

| Farm Type        | Filter Type |   Value |
| :--------------- | :---------- | ------: |
| **Tier 1 (3x3)** | LV, 85%     |      19 |
|                  | LV, 96%     |      21 |
|                  | MV, 96%     |      64 |
|                  | HV, 96%     |     162 |
|                  | HV, 105%    |     180 |
|                  | EV, 105%    |     468 |
|                  | EV, 130%    |     585 |
|                  | EV, 155%    |     702 |
|                  | EV, 175%    |   1,746 |
|                  | IV, 175%    |   1,978 |
|                  | IV, 206%    |   2,328 |
|                  | LuV, 206%   |   5,856 |
|                  | ZPM, 206%   |  14,640 |
|                  | UV, 206%    |  36,600 |
|                  | UHV, 206%   |  91,536 |
| **Tier 2 (5x5)** | HV, 96%     |     170 |
|                  | HV, 105%    |     188 |
|                  | EV, 105%    |     491 |
|                  | EV, 130%    |     614 |
|                  | EV, 155%    |     737 |
|                  | EV, 175%    |   1,833 |
|                  | IV, 175%    |   2,077 |
|                  | IV, 206%    |   2,444 |
|                  | LuV, 206%   |   6,148 |
|                  | ZPM, 206%   |  15,372 |
|                  | UV, 206%    |  38,429 |
|                  | UHV, 206%   |  96,112 |
| **Tier 3 (7x7)** | IV, 175%    |   2,176 |
|                  | IV, 206%    |   2,560 |
|                  | LuV, 206%   |   6,441 |
|                  | ZPM, 206%   |  16,104 |
|                  | UV, 206%    |  40,260 |
|                  | UHV, 206%   | 100,689 |

### Notes:

- Electric Air Filters are multiblock pollution scrubbers which clean a (tier-based) area around them. They're first craftable after building an EBF (for the Blue Steel for the Turbine Casing for the controller block). Chunks need to have 10K+ pollution for an air filter to start cleaning them [1] Note that EAFs only clean one chunk at a time, their working area is a maximum working range and not how large an area is cleaned at once. Working area is configurable with a screwdriver, which can be useful to only focus on a single chunk that produces a ton of pollution EAFs require a set amount of power to run, independantly of it's energy tier (as determined by the energy hatch(es)): T1 requires 30 EU/t, T2 requires 480 EU/t and T3 requires 7680 EU/t. The multi's energy tier and tier of muffler hatches should match, as the lower of the two matters EAFs can be given Absorption Filters, which double the amount of pollution being cleaned for as long as the filter lasts. Filters require stainless steel to craft and aren't perfectly recyclable until EV, so early on they are likely not worth using. Absorption Filters do stack to 64 EAFs also require a rotor inside the machine controller slot in order to function. Only the listed Turbine Efficiency stat matters for this rotor. It will not take durability damage, so it will not need to be replaced either If the numbers for pollution cleaned seem really low compared to pollution producers it's because Electric Air Filters measure in per tick whereas pollution producers are measured in per second. The numbers do assume the full eight muffler hatches one EAF can support
- Small steel rotors are the best you can make without an MV assembling machine and Magnalium. Although you need Magnalium and an EBF to make an electric air filter in the first place, so unless you're behind on making MV circuits there's little reason to bother with a steel rotor
- Blue Steel is probably the easiest small rotor to craft that has 96% efficiency, considering you need blue steel to make an electric air filter in the first place
- Manyullyn and Enhanced Galgadorian are your options for small rotors with 105% efficiency. Both require Nichrome Coils, meaning a Vacuum Freezer meaning Cleanroom, but one does not require an absolute truckload of stuff to craft. I'm sure you can figure out the rest
- With Titanium you're able to make medium rotors, which have higher efficiency than their small counterparts. You've got several options for getting 130% efficiency medium rotors, but Manyullun from before still works just fine as an option
- With only one ingot of Tungstensteel you're able to produce a Large rotor, which has greater efficiency still compared to it's medium counterparts. Manyullyn is, once again, the highest efficiency material you've got reasonble access to pre-T2 rocket
- Large HSS-E rotors, while not trivial and costly to produce, still offer a much cheaper upgrade for EV tier EAFs than upgrading to a T3 EAF. Elven Elementium has the same efficiency and might be easier to make, but it's not cheaper to make, so not a good option
- At this point there's a ton more options in terms of rotors, so figuring out the best one is difficult. HSS-S offers a small upgrade over HSS-E, Naquadah Line opens up a few materials better than HSS-E, Ichorium/Gaia Spirit Ingot is a crazy expensive (but good) upgrade, and more

### Tips and tricks:

- The GT++ Pollution Detection Device emits a redstone signal when the chunk it's in contains more than a specified amount of pollution. Use this to automate your EAF so they don't turn on when a chunk is below 10K pollution, draining power for no reason. To configure the Pollution Detection Device right-click the + or - signs on the front face of the machine to increase/decrease the detection range by 5000 gibbl. Right click below the + and - symbol to increment by 50000 instead

- Machines that output pollution do so on a time basis, not a per recipe bases. Overclocking machines to make them faster thus also reduces the amount of pollution they produce per recipe. The Implosion Compressor is one notable example, producing 75% less pollution per recipe ran at HV instead of LV. Combined with a decent tier muffler hatch you can reduce the pollution output per recipe far more than the tiers of muffler hatches you've got access to would suggest
