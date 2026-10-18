# Technical Evaluation and Decision Log

## Current decisions
| ID | Decision | Status | Rationale |
|---|---|---|---|
| D-001 | Compare Unreal Engine 5 and Godot before choosing | Open | Affects rendering, tools, architecture, assets, console path |
| D-002 | C++-first is preferred | Provisional | Owner wants explicit maintainable code and AI-assisted implementation |
| D-003 | PC/Linux is first development target | Constraint | Primary development environment |
| D-004 | PlayStation/Xbox are goals, not guarantees | Constraint | SDK access, porting, testing and certification are external dependencies |
| D-005 | Single-player/offline-first | Approved | Avoid backend costs and operations |
| D-006 | One town, one hideout, one dimension in first slice | Approved scope | Prove the loop before expanding |
| D-007 | No production code before explicit approval | Approved process | Pre-production must be coherent first |

## Scoring model
Weighting proposal: artistic quality/iteration 25%; Linux compatibility/performance 20%; C++ and Claude Code workflow 20%; console feasibility 20%; solo-developer productivity/maintenance 15%. Score each candidate 1–5 only after evidence is collected. Record confidence and blockers; do not turn guesses into measured scores.

## Unreal Engine 5 questions
- Does the current supported Linux toolchain work on the actual distribution and GPU driver?
- Can a small C++ project compile and launch without an unreasonable setup burden?
- Can the target stylized look be achieved without expensive rendering features?
- Can Claude safely edit C++ while keeping editor-authored data stable?
- What access/platform requirements apply to each console?
- Is the editor responsive enough for solo iteration?

Potential strengths: integrated 3D editor, C++ gameplay framework, visual scripting, broad content pipeline. Risks: editor/build footprint, configuration complexity, performance overhead, and merge friction for editor-authored binary assets.

## Godot 4 questions
- Is its renderer/lighting sufficient for the art target?
- How much custom vehicle, character, interaction, and editor tooling is needed?
- Would C++ GDExtension add friction for frequent gameplay iteration?
- What console porting partners exist, what do they cost, and what support do they provide?
- Can data and scenes remain maintainable under AI-assisted editing?

Potential strengths: lightweight editor, open-source engine, straightforward project structure. Risks: custom work for integrated 3D workflows, C++ extension boundary, and less direct console publishing route.

## Bounded validation experiment (only after authorization)
Use disposable test projects, not the production game. Demonstrate:
1. Third-person movement and camera collision.
2. One interactable object and input abstraction.
3. A simple vehicle/physics test.
4. One imported stylized model.
5. Small lit environment with fog and readable silhouettes.
6. Build/run loop plus at least one repeatable test.
7. Controller input path.

Measure setup/build time, editor responsiveness, runtime frame rate, iteration friction, and custom-system count. Do not expand into a production prototype without approval.

## Architecture direction after engine selection
Separate domain rules from presentation where practical. Use stable IDs for items, missions, NPCs, recipes, upgrades. Data assets/resources define content; code defines behavior. Abstract input from physical devices. Make portal transitions and save/load transactional and failure-safe. Communicate across systems through documented interfaces/events. Keep local single-player state authoritative; no server abstractions unless later approved.

## Open risks
- Exact Linux distribution, driver, disk space, and compiler toolchain not yet verified.
- Console access and porting costs unknown.
- Numeric performance targets and rendering features unknown.
- Commercial asset license/provenance must be verified.
- Schedule estimate needs engine choice and realistic weekly availability.

## Decision record template
ID; date; decision; status; alternatives; rationale; evidence; consequences; revisit trigger. Engine, save format, world scale, and core-loop changes require explicit owner approval.
