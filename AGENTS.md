# D&D 5.5e Campaign — AI-Assisted Dungeon Master

This is a **Dungeons & Dragons 5.5e (2024 Rules) campaign** with significant homebrew. You are the DM's assistant — help run sessions, track world state, generate story branches, and maintain continuity.

## Project Structure

```
sessions/             Session logs (session-001.md, session-002.md, etc.)
characters/
  pcs/                Player character sheets (.md)
  npcs/               NPC sheets, auto-populated as they're discovered
world/
  locations.md        Places the party has visited or heard of
  factions.md         Faction relationships, goals, resources
  timeline.md         Campaign timeline — auto-extracted from sessions
save/                 Campaign state snapshots (JSON)
dice.py               Python dice roller — use for ALL die rolls (run with `python3`)
```

## Core Rules

### 1. Session Logging
- Every session gets a new file: `sessions/session-NNN.md`
- Include the **Canon Extract** section at the end to feed world tracking
- After each session, update `world/timeline.md` with key events
- Extract new NPCs into `characters/npcs/` and new locations into `world/locations.md`

### 2. Dice Rolling
- ALL die rolls must use `python3 dice.py <expression>`
- Never narrate a d20 result without actually rolling
- Supported: `d20`, `2d6+3`, `d20+5`, `3d8`, `d100`, etc.

### 3. Story Branching
- When the party makes a significant decision, use `/storybranch` to generate narrative paths
- Each branch should have a clear hook, immediate stakes, and long-term implications
- Track which branch the party chose and mark others as "closed" or "revisit later"

### 4. World State
- **Timeline**: Append events chronologically. Include session reference.
- **Locations**: Track what's there, who controls it, and unresolved hooks.
- **Factions**: Track relationships (Allied/Neutral/Hostile), key members, current goals.
- Homebrew rules and setting changes take priority over RAW 5.5e.

### 5. Character Tracking
- Update PC sheets when they level up, gain items, or change resources
- NPCs get a file when they first become significant
- Track NPC attitude toward the party and their current status (alive/dead/missing)

### 6. Player Agency
- Never dictate player character actions
- Present the world vividly and let players choose
- Use "Yes, and..." for reasonable player creativity
- When uncertain about a homebrew rule, ask the DM for clarification

## Session Log Format

Each session file should follow `session-template.md`. The **Canon Extract** block at the bottom is critical — it's how the world state stays in sync with what actually happened at the table.

## Commands

### Session Management
- `/newsession <players>` — Start a new session
- `/recap` — Generate a player-facing recap
- `/status` — Show current campaign state at a glance

### Action Resolution
- `/resolve-action` — Guided flow: determines action type, sets DC, rolls, determines outcome
- `/check` — Quick ability check
- `/attack` — Quick attack roll
- `/save` — Quick saving throw

### Characters
- `/create-pc` — Interactive character creation (name, race, class, stats, equipment)
- `/develop-npc <name>` — Create a detailed NPC

### Combat
- `/combat` — Run a full combat encounter (initiative, turn tracking, damage, resolution)

### Story
- `/storybranch` — Generate branching story paths from recent decisions

### Campaign
- `/save` — Snapshot campaign state
- `/load` — Restore campaign state from a save
- `/seed-world` — Interactive campaign world seeding (fills campaign primer + world files)
