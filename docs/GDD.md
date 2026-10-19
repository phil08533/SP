# Game Design Document

## Product definition
Genre: single-player open-world crime sandbox with exploration, light simulation, and psychedelic sci-fi. Perspective: third-person. PC first, Linux development; console release is conditional. Sessions combine free exploration with short jobs and longer resource runs.

## Player fantasy
Become a capable local operator in a strange, overlooked town. Players can lean toward legitimate work, exploration, gray-market trading, or a blend. Violence is not the default answer.

## Core loop
Observe opportunity → prepare → travel → interact/gather/deliver → manage risk → return → sell/process → spend/upgrade → unlock new opportunities. Travel must offer scenery, shortcuts, encounters, or choices, never empty padding.

## Player verbs
Move, sprint, look, drive, park, inspect, talk, accept, collect, carry, process, buy, sell, hide, evade, report, repair, upgrade, save. Every verb needs clear feedback and controller-equivalent input.

## Player state
Position/rotation, world ID, currency, inventory, active job/objectives, equipment/unlocks, relationship flags, suspicion, vehicle state, hideout upgrades, and save version. Defer hunger/thirst/sleep meters until the core loop is proven.

## Missions
Use reusable objective types: talk, reach area, collect, deliver, inspect, process, sell, evade, return, choose. Each mission has prerequisites, optional branches, completion/failure rules, reward, and world-state effects. It must survive save/load, avoid duplicated rewards, and have recoverable failure paths.

## Crime and authority
Initial crime categories: restricted-site trespass and exposure of restricted fictional cargo. Theft/assault are later candidates. Detection uses plausible range, line of sight, awareness, and evidence; no omniscient police. First response is an officer investigating, warning, fining modestly, or confiscating exposed cargo. Full pursuits/arrests are deferred.

## NPC behavior
Named NPCs have small authored schedules and state machines: routine, available, reacting, investigating/reporting, fleeing/help-seeking, returning to routine. Ambient actors use simplified loops. Mission-critical characters need fallback locations/interactions so schedule or navigation bugs cannot soft-lock progress.

## Economy
Three income lanes: legal jobs, exploration/salvage, and risky fictional-product deliveries. Start with fixed prices and understandable choices. Add demand modifiers only after playtests. Always preserve a viable way to earn basic repair money.

## Inventory/crafting
Stack-based inventory with stable item IDs, stack limits, values, category, description, tags, and optional asset references. Recipes define inputs, outputs, station, duration if relevant, and unlock conditions. The fictional recipe system must not imitate real-world manufacturing.

## Vehicle
One starter vehicle. Prefer polished arcade handling over simulation. Prioritize readable steering, braking/reversing, stable camera, entry/exit, forgiving collision, and recovery if trapped or rolled over. Missions cannot depend on the vehicle staying at one coordinate.

## Portals
Controlled level transition, not seamless streaming. Validate destination and active mission state, preserve allowed inventory and objective flags, spawn at a safe marker, and recover to the source world if loading fails.

## UI/accessibility
Consistent interaction prompts, short objective text, controller-navigable inventory/vendor menus, subtitle support, readable text, and feedback for pickups, sales, crafting, suspicion, and blocked actions. Critical information cannot rely on color alone or hover-only UI.

## Audio
Town: wind, cables, electrical buzz, distant traffic, muffled radio, diner chatter. Dimension: glassy organic resonance, soft pulses, spatial ambience, restrained unease. Music supports retro roadside mood with cosmic strangeness; dialogue and warning sounds remain intelligible.

## Difficulty
Failure costs time, resources, or opportunities rather than arbitrarily erasing progress. Early hazards teach rules. No mandatory combat gate in the first slice.

## First-slice definition
Complete one authored resource-to-profit loop, one optional reward branch, one portal, one dimension route, one hideout upgrade, basic save/load, and one understandable enforcement response. Add content only after this is fun.
