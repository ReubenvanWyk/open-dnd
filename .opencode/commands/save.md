---
description: "Quick saving throw — set DC, roll save, determine effect"
agent: dm-assistant
subtask: true
---
The DM needs a saving throw resolved.

1. Use the question tool to ask: who is making the save, what ability, what's the DC, what's the source?
2. Roll: python3 dice.py d20+<save modifier>
3. Describe effect based on success/failure.
4. Present outcome options via question tool.
5. Record in session log.
