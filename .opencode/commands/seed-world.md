---
description: "Interactive campaign world seeding — fill out the campaign primer and propagate to world files"
agent: dm-assistant
---
The DM wants to seed the campaign world. Use the question tool at each step.

## Step 1 — Campaign Overview
Ask each question via question tool:
1. **Campaign Name** — text input
2. **Setting / Genre** — options: High Fantasy / Grimdark / Swashbuckling / Political Intrigue / Horror / Comedy / Epic / Other
3. **Tone** — text input
4. **Starting Region** — text input
5. **Starting Location** — text input (the first town, tavern, dungeon entrance, etc.)

## Step 2 — The World
6. **Brief world description** — what makes this setting unique? Text input.
7. **Important homebrew rules** — setting changes that override RAW 5.5e. Text input.

## Step 3 — Starting Situation
8. **Initial hook** — what are the players doing at the start? What's the inciting incident? Text input.

## Step 4 — Initial Factions
9. **Faction list** — ask how many initial factions the DM wants (1-5 via question tool). For each faction, ask:
   - Name, description, current goal, starting relationship with party (Allied/Neutral/Hostile)

## Step 5 — Initial Locations
10. **Location list** — ask how many initial locations the DM wants (1-5 via question tool). For each, ask:
    - Name, description, notable features, controlled by which faction (if any)

## Step 6 — Save Everything
11. Save the filled-out primer to `sessions/session-000-campaign-primer.md`.
12. Propagate factions to `world/factions.md` (overwrite with the new data).
13. Propagate locations to `world/locations.md` (overwrite with the new data).
14. Add a starting timeline entry to `world/timeline.md`: "Campaign begins — [campaign name]".
15. Confirm to the DM what was created and where.
