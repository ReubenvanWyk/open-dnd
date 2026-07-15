---
description: Start a new session log with context from previous sessions
agent: dm-assistant
---
Create a new session log for today's D&D 5.5e session.

First, list all existing files in sessions/ to find the highest session number. The new file should be session-NNN.md where NNN is the highest existing number + 1, padded to 3 digits (e.g. 001, 002, 010).

Read the most recent session file, world/timeline.md, world/locations.md, world/factions.md, and world/branches.md for current world state and any open story branches.

Then create the new session file using the session-template.md format.

Players present: $ARGUMENTS

Set the scene based on where the party ended last session.
