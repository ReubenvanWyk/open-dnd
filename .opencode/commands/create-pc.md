---
description: "Interactive character creation — name, race, class, stats, equipment"
agent: dm-assistant
subtask: true
---
The DM wants to create a new player character. Use the question tool at each step to guide the process interactively.

1. **Name** — Ask for character name via question tool with a text input option.

2. **Player** — Ask who the player is via question tool with text input.

3. **Race** — Ask via question tool:
   Human | Elf | Dwarf | Halfling | Gnome | Dragonborn | Tiefling | Orc | Half-Elf | Half-Orc | Goliath | Aasimar | Firbolg | Tabaxi | Custom

4. **Subrace** — If the chosen race has subraces (Elf → High/Wood/Dark, Dwarf → Hill/Mountain, Gnome → Forest/Rock, Halfling → Lightfoot/Stout, Dragonborn → Chromatic/Metallic/Gem, Tiefling → Infernal/Abyssal/Chthonic), ask via question tool.

5. **Class** — Ask via question tool:
   Barbarian | Bard | Cleric | Druid | Fighter | Monk | Paladin | Ranger | Rogue | Sorcerer | Warlock | Wizard

6. **Subclass** — If the class gets a subclass at level 1 (Cleric → Domain, Sorcerer → Origin, Warlock → Patron, Wizard → School), ask via question tool.

7. **Background** — Ask via question tool:
   Acolyte | Charlatan | Criminal | Entertainer | Folk Hero | Guild Artisan | Hermit | Noble | Outlander | Sage | Sailor | Soldier | Urchin | Custom

8. **Alignment** — Ask via question tool:
   LG | NG | CG | LN | N | CN | LE | NE | CE

9. **Ability Scores** — Roll `python3 dice.py 4d6dl1` six times. Present the six numbers. For each stat (STR, DEX, CON, INT, WIS, CHA in order), ask the DM to assign one of the rolled numbers via question tool. Remove assigned numbers from the pool.

10. **Skills** — Based on class and background, list the available skill proficiencies. Ask the DM to pick via question tool.

11. **Starting Equipment** — Ask the DM to choose starting equipment package or custom items via question tool.

12. **Personality** — Ask for personality traits, ideals, bonds, flaws via question tool (present examples, allow text input).

13. **Backstory** — Ask for brief backstory notes via question tool. Generate a 2-3 paragraph backstory based on their input.

14. **Save** — Calculate all derived values (HP, AC, proficiency bonus, saving throws, etc.) and save to characters/pcs/{name}.md using the pc-template format.
