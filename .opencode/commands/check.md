---
description: "Quick ability check — pick a skill, set DC, roll, determine outcome"
agent: dm-assistant
subtask: true
---
The DM needs an ability check resolved.

1. Use the question tool to ask which ability/skill applies. Present options based on the current context.
2. Propose a DC via question tool with these options:
   - DC 10 (Easy) | DC 15 (Medium) | DC 20 (Hard) | DC 25 (Very Hard) | DC 30 (Nearly Impossible) | Custom
3. Roll: python3 dice.py d20+<modifier>
4. Present 2-3 outcome options via question tool based on the result.
5. Record the outcome in the current session log.
6. Update world state if anything significant changed.
