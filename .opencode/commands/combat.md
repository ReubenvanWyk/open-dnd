---
description: "Run a combat encounter — initiative, turn tracking, damage, resolution"
agent: dm-assistant
---
The DM wants to run a combat encounter. Use the question tool at each step.

## Phase 1 — Setup
1. Ask which PCs are participating via question tool (list available PCs from characters/pcs/).
2. Ask what enemies are present. Let the DM describe them (name, count, AC, HP, any special traits).
3. For each participant (PCs + enemies), roll initiative: `python3 dice.py d20+<dex modifier>`.
   - For groups of identical enemies, roll once per group or individually — ask the DM.
4. Display the initiative order (highest to lowest) with a clear turn tracker.

## Phase 2 — Combat Rounds
For each round, for each participant in initiative order:

1. **Announce** whose turn it is.
2. **Ask** what the participant does via question tool:
   - Options: Attack / Cast a Spell / Use an Ability / Dash / Disengage / Dodge / Help / Hide / Ready / Search / Use an Object / Other
3. **Resolve the action**:
   - If it's an attack, roll `python3 dice.py d20+<attack bonus>`, ask target AC, on hit roll damage.
   - If it's a spell, ask what spell and handle its effects.
   - If it's a save, determine DC and have the target roll.
   - Track all damage dealt to each participant.
4. **Check for death/unconsciousness**: If a creature drops to 0 HP, note it and describe.
5. **After the turn**: Update and display current HP for any damaged participants.

At the start of each new round, announce the round number.

## Phase 3 — End Combat
When the DM indicates combat is over (all enemies defeated/fled/surrendered, or PCs flee):

1. Ask the DM for the outcome via question tool.
2. Calculate XP award: sum enemy XP values and present to DM for confirmation.
3. Suggest any loot or rewards based on enemies defeated.
4. Record in session log: participants, rounds, key moments, damage taken, resources spent.
5. Update PC sheets: adjust HP, spent spell slots, expended features.
