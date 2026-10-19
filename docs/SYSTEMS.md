# Gameplay Systems Specification

## 1. Player movement and camera
Third-person movement is responsive and readable, with walk, sprint, camera orbit, and jump only if level design needs it. No stamina meter in the first slice. Camera collision prevents major clipping and remains stable around vehicles and portals. Provide recovery for test builds and remappable actions where practical.

## 2. Interaction
All interactions share a contract: test availability → show prompt → accept input → validate → change state → provide feedback. Target priority considers distance and visibility; controller focus is supported. Failed interactions explain why when useful. Mission progress cannot depend on tiny hitboxes.

## 3. Vehicle
One starter vehicle with forgiving arcade handling. Enter/exit safely; state includes transform, ownership, and upgrade/condition IDs if used. Missions cannot assume it stays in one location. Provide a reset/recovery option if trapped or rolled over. No detailed maintenance simulation.

## 4. Inventory and items
Stack-based container with stable IDs, stack limits, base values, category, description, tags, and optional visual references. Pickup fails cleanly if full. Sale and crafting are atomic: inputs removed and outputs/currency applied exactly once. Proposed items:
- **Lumen Pod:** common alien botanical sample, low hazard, low raw value.
- **Resonant Shard:** valuable mineral sample sensitive to resonance.
- **Odd Spore:** uncommon organic sample requested by research contact.
- **Glow Resin:** fictional processed product made from Lumen Pods; higher value, restricted status in town.
- **Survey Tag:** mission item, not normally sellable.

## 5. Fictional processing and economy
Abstract crafting UI only; no real-world manufacturing steps. First recipe: 3 Lumen Pods → 1 Glow Resin. Raw pods are legal/low-risk and less profitable; Glow Resin has higher value but increases suspicion if carried openly near witnesses.

**First-slice location rule:** the first processing interaction happens at the hideout workbench. The trade counter is a buyer, not a crafting station. The player brings collected pods home, chooses raw sale or processing, then takes the resulting goods to a buyer. Carrying Glow Resin through town creates the intended risk window; processing itself does not trigger suspicion. A future public processing station is possible but not part of the first slice.

Provisional balance values, to be tested:
- Basic courier job: 25 credits.
- Lumen Pod raw sale: 5 credits.
- 3 pods processed to Glow Resin: 24 credits gross before fees.
- Storage crate upgrade: 40 credits.
- Basic vehicle repair: 15 credits.
- Optional rare specimen: 20 credits to research buyer.

Values are placeholders; playtest whether the first upgrade is reachable after one loop plus a small optional activity. The basic courier fee plus sale of three raw pods equals 40 credits before penalties or fees. Processing yields 49 credits total before any processing costs or penalties.

## 6. Crime, witnesses, and enforcement
First-slice categories: trespass at restricted Pumpworks and exposure of restricted fictional cargo. The public-facing service drop is authorized for the courier job; crossing the marked inner boundary toward the portal chamber is restricted. The first mission can trigger a warning here, but enforcement must not block the required portal interaction or strand the player. Later crime candidates: theft and assault. Suspicion states: Clear → Noticed → Investigating → Resolved. Detection needs plausible range, line of sight, awareness, and an evidence event unless a scripted exception is documented. Witnesses can report after a delay; no omniscient global alert.

Officer response: investigate or approach. Player may cooperate, leave before identification, surrender cargo, or ignore instructions and accept a larger consequence. First consequences are mild/reversible: warning, modest fine, or exposed-cargo confiscation. The opening trespass response defaults to a warning/tutorial beat; later incidents may fine the player. Exposed Glow Resin can be confiscated if identified. Full pursuits/arrests are deferred. Communicate what triggered the response through UI/audio/text; never rely on color alone.

## 7. NPC routines
Named NPCs use authored states: work, idle, travel, converse, react, investigate/report, flee/help, return. Ambient actors use simple waypoint loops. Off-screen actors may update less often. Mission-critical NPCs need fallback points or an alternate interaction if navigation/schedules fail.

## 8. Missions
Objective types: talk, enter area, collect, deliver, inspect, process, sell, evade, return, choose. Missions define prerequisites, optional objectives, success/failure, rewards, and world-state changes. Progress and rewards must be idempotent and save-safe.

## 9. Portal transitions
Treat travel as a controlled level/world change. Validate destination, store departure anchor and allowed carried state, resolve active interaction, preserve mission/inventory, block duplicate input during transition, spawn at safe marker, restore UI. If destination load fails, return to source and preserve inventory.

## 10. Hideout upgrades
Hideout is save anchor, storage, processing point, and visual progression hub. First upgrade is a storage crate with increased capacity and a visible environmental change. Later options may add a better workbench, portal scanner, or vehicle bay; not first-slice requirements.

## 11. Save/load
Local, versioned save. Prefer safe write: write temporary data, validate, then replace prior save when platform supports it. Store schema version, player/world, inventory, currency, mission, unlocks, relationships, suspicion, hideout upgrades, and vehicle safe transform. Avoid persisting unstable physics internals. Validate IDs on load; unknown content should be skipped/recovered safely. Test corrupt save, older version, interrupted write, and portal-transition edges.

## 12. UI/input
One input-action layer maps keyboard/mouse and controller. Menus support directional focus and confirm/back. Prompts show current bindings. Inventory/vendor screens do not require hover. Provide subtitle support and readable text. Show objective, money change, inventory-full feedback, reward, suspicion, and blocked interactions.

## 13. Audio and feedback
Priority cues: pickup, sale, craft, portal, witness alert, vehicle recovery, objective completion. Ambience is layered but restrained. Dialogue subtitles must be synchronized enough for comprehension.

## 14. Performance/robustness
Set numeric frame-time budgets after benchmarking on the actual development PC. Profile town and dimension separately. Use simple collision proxies, reuse materials, avoid per-frame work across every NPC, and scale update frequency for distant actors. Invalid state should fail safely.

## 15. System interactions
- Inventory capacity affects resource-run decisions.
- Portal transitions preserve mission and inventory.
- Crafting changes item mix and suspicion exposure.
- Witnesses feed the same event/suspicion system as trespass.
- Reputation alters jobs and buyers.
- Vehicle upgrades open rough routes, not only speed.
- Hideout upgrades change storage/processing.
- Save/load restores a consistent snapshot.

Systems communicate through documented interfaces/events; avoid directly mutating another system's private state.
