---
description: "Generate branching story paths from recent player decisions"
agent: dm-assistant
---
Read the last session file from sessions/, world/locations.md, world/factions.md, world/timeline.md, and world/branches.md.

Then spawn story-weaver as a creative subagent: give it the session's key decisions and ask it to generate 3-5 distinct branching story paths. For each branch, have it describe:
- The hook that presents this path
- Immediate consequences
- Potential longer-term outcomes
- Which factions/NPCs would react

Once story-weaver returns the branches, write them into world/branches.md using the existing format. Record the session number, the player decision that triggered it, and note all branches as 'open'.

Format as a clear list the DM can reference during play.
