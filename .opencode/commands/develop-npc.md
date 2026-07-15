---
description: Generate a detailed NPC with personality, goals, and plot hooks
agent: dm-assistant
subtask: true
---
Read world/locations.md and world/factions.md for context. Create a detailed D&D 5.5e NPC with:

Name: $ARGUMENTS

Include:
- Race, class (if any), appearance
- Personality traits, ideals, bonds, flaws
- Short-term and long-term goals
- How they connect to existing factions/locations
- 3 plot hooks involving this NPC
- Stat block reference (CR, key abilities)

Save to characters/npcs/{name}.md
