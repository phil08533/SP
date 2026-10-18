# Space Hippie

**Pre-production blueprint** for a stylized polygonal open-world science-fiction crime sandbox.

> Build a small, beautiful, playable game first. Expand only after its core is fun.

## Start here
1. [Project Status](docs/PROJECT_STATUS.md)
2. [Master Blueprint](docs/MASTER_BLUEPRINT.md)
3. [Game Design Document](docs/GDD.md)
4. [World Design and Maps](docs/WORLD_DESIGN.md)
5. [Town Greybox Blockout Specification](docs/TOWN_BLOCKOUT_SPEC.md)
6. [Characters and Dialogue](docs/CHARACTERS_DIALOGUE.md)
7. [Gameplay Systems](docs/SYSTEMS.md)
8. [Missions and Progression](docs/MISSIONS_AND_PROGRESSION.md)
9. [Portals and Dimensions](docs/PORTALS_AND_DIMENSIONS.md)
10. [Player Flow and Interaction UX](docs/PLAYER_FLOW_AND_UX.md)
11. [Save Data and Recovery Specification](docs/SAVE_DATA_AND_RECOVERY.md)
12. [Art Bible and Asset Pipeline](docs/ART_BIBLE_ASSET_PIPELINE.md)
13. [Concept Art Briefs](docs/CONCEPT_ART_BRIEFS.md)
14. [Initial Asset Catalog](docs/ASSET_CATALOG.md)
15. [Technical Decision Log](docs/TECHNICAL_DECISIONS.md)
16. [Engine Decision Matrix](docs/ENGINE_DECISION_MATRIX.md)
17. [First-Slice Dependency and Build Order](docs/FIRST_SLICE_DEPENDENCIES.md)
18. [Consistency Audit](docs/CONSISTENCY_AUDIT.md)
19. [Roadmap and Acceptance Tests](docs/ROADMAP_TESTING.md)
20. [Definition of Done and Change Control](docs/DEFINITION_OF_DONE_AND_CHANGE_CONTROL.md)
21. [Claude Code Instructions](CLAUDE.md)
22. [Claude Execution Playbook](docs/CLAUDE_EXECUTION_PLAYBOOK.md)
23. [Claude Code Starting Prompt](docs/CLAUDE_START_PROMPT.md)

## Visual maps
- [Dusty Junction SVG map](docs/assets/dusty-junction-map.svg)
- [The Bloom SVG map](docs/assets/the-bloom-map.svg)

## Local diagnostic tool
`tools/engine-readiness-check.sh` is a read-only Linux system report for the later engine trial. It does not install packages or change system settings. When ready, run it from the repository with:

```bash
bash tools/engine-readiness-check.sh
```

Review its output before sharing it; it can report hardware and software details.

## Status
Pre-production only. Engine is not selected. Unreal Engine 5 is the first candidate to validate; Godot 4 is the fallback if the real Linux setup/build workflow makes Unreal too cumbersome. This is a test plan, not a final engine decision.

PC/Linux is the first development target; PlayStation and Xbox are goals subject to access, porting, feasibility, and certification. Production gameplay code and bulk final assets remain gated until the technical direction and vertical-slice plan have been explicitly approved.

## How to use this repository
Start with [Project Status](docs/PROJECT_STATUS.md), then follow the Master Blueprint and linked design documents. Use `CLAUDE.md` as persistent instructions for Claude Code and `docs/CLAUDE_START_PROMPT.md` as the initial task prompt. Keep changes small, reviewable, and on a branch; run real checks and report what was not tested.

Creative details are proposed first-version canon. Change them through explicit decision-log entries, not silently during implementation.
