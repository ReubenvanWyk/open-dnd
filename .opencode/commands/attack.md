---
description: "Quick attack roll — target, roll to hit, roll damage, determine outcome"
agent: dm-assistant
subtask: true
---
The DM needs an attack roll resolved.

1. Use the question tool to ask: who is attacking, what weapon/spell, what target?
2. Ask for the attack modifier via question tool.
3. Roll: python3 dice.py d20+<modifier>
4. Ask for target AC via question tool.
5. If hit: roll damage via python3 dice.py <damage expression>
   If miss: describe the miss.
6. Present outcome options via question tool.
7. Record in session log. Update target's HP on their sheet if applicable.
