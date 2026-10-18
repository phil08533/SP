# Space Hippie — Project Status

**Last updated:** 2026-10-18
**Current phase:** Pre-production documentation
**Production engine:** Not selected
**Production gameplay code:** Not started
**Current working branch:** `preproduction/space-hippie-blueprint`
**Review pull request:** https://github.com/phil08533/SP/pull/1

## What exists

- Core game concept, pillars, first-session arc, and bounded first playable scope.
- Dusty Junction town design and The Bloom dimension, with measurable greybox requirements and two SVG schematic maps.
- Character roster and dialogue, mission/progression, portal, economy, crime/suspicion, save/load, and interaction concepts.
- Player-flow and interaction UX specification, including keyboard/mouse-controller parity and common failure cases.
- Logical save-data and recovery specification, including transaction safety, schema migration requirements, and corruption recovery. Actual save format remains undecided.
- Art direction, concept-art briefs, initial asset catalog, and asset provenance expectations.
- Technical decision log, engine decision matrix, engine trial protocol, and staged roadmap.
- First-slice dependency/build order with milestone acceptance criteria.
- Definition of Done and change-control rules for AI-assisted development.
- Read-only Linux engine-readiness diagnostic script; shell syntax was checked, but it has not been run on the owner's machine.
- Claude Code project rules, autonomous execution playbook, and copyable starting prompt.
- Consistency audit that corrected the opening courier/resource loop, economy arithmetic, processing location, and mission resumption rules.
- README links to the pre-production documents, maps, and diagnostic script.

## Current recommendation

Test Unreal Engine 5 first, with Godot 4 as a fallback. This is not yet a production-engine decision. The first test should use a disposable project and answer whether the editor, C++ build loop, and visual workflow are practical on the actual Linux machine.

## Current approval boundary

The owner has asked for autonomous progress where possible. This authorizes continued planning, documentation, research, consistency checks, and reversible pre-production work. It does **not** silently approve a production engine, production gameplay code, bulk final assets, system changes, or a larger game scope. Those should be presented as one concise recommendation when evidence is ready.

## Completed pre-production work

1. Added an engine decision matrix with evidence requirements instead of invented numeric scores.
2. Added a town greybox specification with routes, landmark requirements, scale targets, acceptance checks, and SVG maps for both worlds.
3. Added Claude's execution playbook and a copyable starting prompt.
4. Audited the opening mission and made the sealed-case delivery, portal discovery, resource loop, processing location, mission resumption, and first-upgrade math consistent.
5. Added a dependency-aware first-slice build order with acceptance criteria for each milestone.
6. Added a read-only Linux readiness script and validated its Bash syntax without running it on the owner's computer.
7. Added player-flow/UX rules and edge-case outcomes.
8. Added logical save-data requirements and failure/recovery acceptance tests without prematurely selecting a save format.
9. Added AI task completion, change-control, and milestone quality-gate rules.
10. Updated the README to index the new documents.

## Highest-value next work

1. Finish a broader consistency pass across crime/suspicion, progression, asset requirements, and save persistence.
2. Prepare the exact disposable engine trial and plain-language decision report.
3. Verify the actual Linux distribution, driver, disk space, and compiler before recommending an install path.
4. Create an asset provenance manifest template and a bounded first-slice content inventory.
5. Present a short owner-facing decision brief with a recommended default and the few remaining risks.

## Risks still open

- Linux Mint version and toolchain compatibility have not been verified.
- The engine has not been installed or tested in this workflow.
- Console development access, porting costs, and certification remain unverified.
- No playable build or performance measurement exists yet.
- Final asset rights/provenance must be checked individually.
- Exact input bindings, save serialization format, autosave behavior, and numeric performance budget remain deliberately open until the engine trial.

## Honest status rule

Documentation and plans are not a playable game. Do not describe the game as implemented, tested, performant, or console-ready until the corresponding work and checks have actually happened.
