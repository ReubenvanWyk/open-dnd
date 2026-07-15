---
name: action-resolution
description: "Guided flow for resolving PC actions — ability checks, attack rolls, and saving throws"
---

Loaded when the DM needs to resolve a player character's action.

## Step 1 — Understand the Action
Use the question tool to ask the DM what the PC is trying to do.
Present example options, or let them type freely.

## Step 2 — Determine the Action Type
From the DM's description, classify the action:

### If it's an ABILITY CHECK (investigating, persuading, sneaking, etc.):
a) Use the question tool to ask which ability/skill applies
   - Present relevant skill options based on context
   - Or let the DM pick from the full skill list
b) Propose a DC with the question tool:
   - DC 10 (Easy) | DC 15 (Medium) | DC 20 (Hard) | DC 25 (Very Hard) | DC 30 (Nearly Impossible)
   - Let the DM confirm or choose custom
c) Roll via: python3 dice.py d20+[modifier]
d) On success: describe what happens. Present 2-3 outcome options via question tool.
   On failure: describe consequences. Present 2-3 complication options.
e) Record result in session log. Update world state if relevant.

### If it's an ATTACK ROLL:
a) Use the question tool to ask: target creature, weapon/spell, modifiers
b) Roll attack: python3 dice.py d20+[attack bonus]
c) Ask target AC via question tool (with estimate suggestion)
d) If hit: roll damage via python3 dice.py [damage dice]+[mod]
   If miss: describe the miss
e) Record in session log. Update HP on target NPC/PC sheet.

### If it's a SAVING THROW:
a) Ask: who is making the save? What's the DC and source?
b) Roll: python3 dice.py d20+[save modifier]
c) Describe effect based on success/failure
d) Record in session log.

## Step 3 — Auto-Record
After every resolution, append a brief entry to the current session file's scene.
If the outcome significantly changes world state, update the relevant world file.
