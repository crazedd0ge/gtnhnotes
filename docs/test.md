# GTNH Bees Guide

## Introduction

Just a few random notes/tips I found out experimenting with some bee-related stuff. I'm no master of bees (or Forestry for that matter), but maybe some of the information here will be of use.

## Bee Frames

### Detailed Frame Characteristics

| Frame Type | Durability | Territory | Mutation Rate | Lifespan | Production | Genetic Decay |
|-----------|------------|-----------|--------------|----------|------------|---------------|
| Untreated | 80 | 1 | 1 | 1 | +1 | 0.9 |
| Impregnated | 240 | 1 | 1 | 1 | +1 | 0.4 |
| Proven | 720 | 1 | 1 | 1 | +1 | 0.3 |
| Healing | 240 | 1 | 0.5 | 1.5 | -0.25 | 1 |
| Chocolate | 240 | 1 | 1 | 0.75 | +0.5 | 1 |
| Restrained | 240 | 0.5 | 1 | 0.75 | -0.25 | 1 |
| Soul | 80 | 1 | 1.5 | 0.75 | -0.75 | 1 |
| Nova [1] | 240 | 1 | 1 | 0.00001 | +0 | 1 |
| Magic | 240 | 1 | 1 | 1 | +2 | 0.6 |
| Temporal | 300 | 1 | 1 | 2.5 | +0 | 0.8 |
| Metabolic | 130 | 1 | 1.8 | 1 | +0.2 | 1 |
| Necrotic | 280 | 1 | 1 | 0.3 | -0.25 | 1.2 |
| Resiliant | 800 | 1 | 1 | 1 | +2 | 0.5 |
| Gentle | 200 | 1 | 0.7 | 1.5 | +0.4 | 0.01 |
| Oblivion [2] | 50 | 1 | 1 | 0.00001 | -9001 | 1 |
| Accelerated | 175 | 1 | 1.2 | 0.9 | +0.8 | 1 |
| Mutagenic [3] | 3 | 1 | 5 | 0.00001 | +9 | 1 |
| Working | 2000 | 1 | 0 | 3 | +3 | 1 |
| Decaying | 240 | 1 | 1 | 1 | +0 | 10 |
| Slowing | 175 | 0.5 | 2 | -0.5 | 1 |
| Blood [4] | 1 | 1 | 1 | 1 | +2 | 0.8 |
| Maddening Frame of Frenzy [4] | 1 | 1 | 10 | 0.00001 | -9001 | 10 |

### Frame Characteristics Explained

#### Durability
- Number of bee ticks before the frame breaks
- Frames in Alveary Fame Houses take 5 durability damage per bee tick
- Frames have no effect on the bee tick they break
- Forestry, Extra Bees, and Magic Bees Frames can be repaired in a Thaumic Restorer
- GT++ Frames cannot be repaired

#### Territory
- Radius for bee pollination of Forestry trees
- Likely does not affect flower searching/spreading area
- Bee Houses get Territory x3 by default

#### Mutation Rate
- Multiplier for bee mutation chance
- Useful for breeding but can be detrimental when trying to stabilize bee species

#### Lifespan
- Determines bee life cycle length
- Unclear if it affects number of ticks or length of each tick
- Short-lived bees are better for breeding
- Long-lived bees are marginally better for production

#### Production
- Multiplier for bee produce chance
- Caps at 200% for regular produce
- Caps at 100% for specialty produce
- High multipliers risk turning Pristine queens Ignoble

#### Genetic Decay
- Influences the chance that overworked Pristine bees turn Ignoble
- May affect Ignoble queen's ability to produce princesses

### Special Frame Notes

1. **Nova Frames**: Creative only, mostly for reference
2. **Oblivion Frames**:
   - Can be found as loot in Stronghold chests
   - Extremely expensive to craft
   - Be careful not to break them
3. **Mutagenic Frames**:
   - Risk of turning Pristine bees Ignoble
   - Cannot work in Alvearies due to durability mechanics
4. **Blood Magic Frames**:
   - Consume 1000 LP per cycle (5000 LP in Alveary Frame Housing)
   - Must be bound to a player's LP network
   - Without LP, they consume durability

### Bee Produce Mechanics

Bee produce is calculated in two stages:
1. First roll: Percentage chance with modifiers
2. Second roll: 50% of the first chance

This means regular produce should be about 1.5x more common than raw numbers suggest.

### Additional Notes

- As of version 2.7, WAILA can show average "Jubilant yields" per hour when hovering over bee blocks while holding Shift
- References in the Apimancy Thaumonomicon about frames draining Aura/releasing aspects are holdovers from TC3
