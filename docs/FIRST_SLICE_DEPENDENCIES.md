# First-Slice Dependency and Build Order

**Status:** Engine-agnostic implementation plan. It is not authorization to start production code.
**Rule:** Do not implement a dependent feature before its prerequisite contract and test are in place. Build a thin end-to-end loop before polishing individual systems.

## Dependency map

```text
Project/build foundation
        |
Input abstraction + player movement/camera
        |
Interaction contract + UI feedback
        |
Stable item IDs + inventory + local save
        |
Mission state machine + objective feedback
        |
Town greybox + hideout + Mara + starter vehicle
        |
Pumpworks gate + portal transition contract
        |
The Bloom greybox + safe return anchor
        |
Resource pickup + inventory capacity
        |
Hideout workbench + recipe + trade counter
        |
Courier reward + first upgrade
        |
Suspicion event + witness/Officer Vale response
        |
Controller pass + save/load fault tests + performance review
```

This is a dependency order, not a mandate to build each component as a separate large subsystem. Prefer small vertical increments that can be run and tested after each change.

## Milestone 0 — Project foundation

**Prerequisite:** Owner approves the engine and vertical-slice plan.

Deliver:
- Reproducible project setup instructions for Linux.
- Version-controlled project settings and a documented asset folder convention.
- A clean launchable project with a basic test scene.
- Input abstraction created before gameplay input is scattered across scripts.
- Build/run/test commands documented.

Acceptance:
- A clean checkout can be opened and launched following the README.
- No credentials, platform SDK files, or local absolute paths are committed.
- The baseline commit can be restored without losing user work.

## Milestone 1 — Player feel and interaction

Deliver:
- Third-person player movement and camera collision.
- Keyboard/mouse and controller action mapping.
- One interactable test object, contextual prompt, and clear success/failure feedback.
- Basic pause menu and settings access if needed to test input.

Acceptance:
- Camera remains usable near walls and in tight spaces.
- Controller can navigate prompts and confirm/back out.
- Interaction does not depend on pixel-perfect targeting.
- The player can recover from a bad test position without restarting the project.

## Milestone 2 — State and persistence

Deliver:
- Stable IDs for items, missions, NPCs, recipes, and upgrades.
- Inventory with stack limits and full-inventory feedback.
- Versioned local save/load.
- Mission-state data model and idempotent reward handling.

Acceptance:
- Save/load restores world ID, safe player transform, inventory, currency, active mission, objective flags, hideout state, and vehicle safe transform.
- Repeating a reward interaction cannot pay twice.
- Invalid/missing item IDs recover safely.
- Portal transition can be tested later without redesigning the save model.

## Milestone 3 — Town greybox and vehicle

Deliver:
- Hideout interior and exit.
- Main Drag, garage, trade counter, Pumpworks route, back trail, and simple boundary.
- Mara NPC with stable fallback interaction point.
- One placeholder drivable vehicle with enter/exit and recovery.
- Landmark signage and blockout lighting only.

Acceptance:
- Player finds Mara, the trade counter, and Pumpworks without a map.
- Main road and shortcut are distinct.
- Vehicle cannot be permanently lost or trapped.
- Mission-critical routes work on foot and by vehicle.

## Milestone 4 — Portal and The Bloom

Deliver:
- Portal interaction and guarded transition state.
- Source/return anchors and a safe destination spawn.
- The Bloom greybox with Entry Shelf, Lumen Grove, Crystal Cut, return arch, and optional specimen nook.
- One slow, clearly telegraphed environmental hazard.

Acceptance:
- Duplicate portal input cannot trigger duplicate transitions.
- Return portal is visible and always usable.
- Transition failure preserves mission and inventory state.
- Hazard can be understood and avoided without frame-perfect timing.

## Milestone 5 — Economy and complete mission

Deliver:
- Sealed-case courier objective.
- Three Lumen Pod pickups.
- Hideout workbench recipe: three pods become one Glow Resin.
- Trade counter sale for raw pods or Glow Resin.
- Courier fee, storage upgrade, and clear money-change feedback.
- Objective tracker and mission completion/recovery rules.

Acceptance:
- The full mission can be completed in one session and after saving/reloading.
- Raw sale and processing cannot duplicate currency or items.
- Prices are visible before confirming.
- First storage upgrade can be reached with the planned default path (25-credit courier fee plus 15-credit raw sale equals 40 credits before penalties).
- Leaving mid-mission is resumable and does not erase collected items.

## Milestone 6 — First suspicion response

Deliver:
- Restricted Pumpworks boundary.
- Exposed Glow Resin as the initial restricted-cargo event.
- Simple witness/Officer Vale investigation state.
- Warning, modest fine, or cargo confiscation; no pursuit/arrest system.

Acceptance:
- Detection uses understandable distance/visibility/evidence rules.
- UI/audio/text communicates what caused the response.
- Consequences are reversible and do not make the game unwinnable.
- Player can choose cooperation or leave before identification where the scenario allows it.

## Milestone 7 — Art and feel anchor review

Only after the complete greybox loop is stable:
- Replace one garage facade with the first art anchor.
- Add Mara's first-pass model/animation.
- Add starter vehicle art.
- Add one Lumen Pod and one crystal.
- Add portal material/effect and audio.
- Review town and dimension under target camera and lighting.

Acceptance:
- The scene reads as “Roadside Americana after the universe developed a strange leak.”
- Player, pickup, portal, and routes remain readable at gameplay distance.
- Style can be reproduced with modular assets, not one-off hero modeling.
- Asset sources and rights are documented.

## Milestone 8 — Hardening and decision to expand

Deliver:
- Controller usability pass.
- Save corruption/version tests.
- Mission recovery tests.
- Town/dimension performance measurements.
- A list of known defects and deferred features.

Expansion is permitted only after the owner reviews the playable slice and agrees that the core loop is enjoyable. Do not add extra dimensions, crowds, deep combat, multiplayer, or online persistence before that review.

## Required test record

For each milestone, maintain:
- Build/commit identifier.
- Exact commands or editor steps used.
- Automated checks run and outcomes.
- Manual test path and outcome.
- Known issues and reproduction steps.
- Performance measurement conditions where relevant.
- Screenshots or short capture when useful.

Never use “done” to mean merely that code was written. It means the acceptance checks were actually performed and results are recorded.
