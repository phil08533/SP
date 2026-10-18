# Space Hippie

**Pre-production blueprint** for a stylized polygonal open-world science-fiction crime sandbox.

> Build a small, beautiful, playable game first. Expand only after its core is fun.

## Start here
1. [Master Blueprint](docs/MASTER_BLUEPRINT.md)
2. [Game Design Document](docs/GDD.md)
3. [World Design and Maps](docs/WORLD_DESIGN.md)
4. [Town Greybox Blockout Specification](docs/TOWN_BLOCKOUT_SPEC.md)
5. [Characters and Dialogue](docs/CHARACTERS_DIALOGUE.md)
6. [Gameplay Systems](docs/SYSTEMS.md)
7. [Missions and Progression](docs/MISSIONS_AND_PROGRESSION.md)
8. [Portals and Dimensions](docs/PORTALS_AND_DIMENSIONS.md)
9. [Art Bible and Asset Pipeline](docs/ART_BIBLE_ASSET_PIPELINE.md)
10. [Concept Art Briefs](docs/CONCEPT_ART_BRIEFS.md)
11. [Initial Asset Catalog](docs/ASSET_CATALOG.md)
12. [Technical Decision Log](docs/TECHNICAL_DECISIONS.md)
13. [Engine Decision Matrix](docs/ENGINE_DECISION_MATRIX.md)
14. [Roadmap and Acceptance Tests](docs/ROADMAP_TESTING.md)
15. [Claude Code Instructions](CLAUDE.md)
16. [Claude Execution Playbook](docs/CLAUDE_EXECUTION_PLAYBOOK.md)

## Status
Pre-production only. Engine is not selected. Unreal Engine 5 is the first candidate to validate; Godot 4 is the fallback if the real Linux setup/build workflow makes Unreal too cumbersome. This is a test plan, not a final engine decision.

PC/Linux is the first development target; PlayStation and Xbox are goals subject to access, porting, feasibility, and certification. Production gameplay code and bulk final assets remain gated until the technical direction and vertical-slice plan have been explicitly approved.

## How to use this repository
Start with the Master Blueprint, then follow the linked design and execution documents. Use `CLAUDE.md` as persistent instructions for Claude Code. Ask the coding agent to work in small, reviewable steps, keep changes on a branch, run real checks, and report what was not tested.

Creative details are proposed first-version canon. Change them through explicit decision-log entries, not silently during implementation.
