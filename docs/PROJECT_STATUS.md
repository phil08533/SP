# Space Hippie — Project Status

**Last updated:** 2026-10-18
**Current phase:** Pre-production documentation and workflow preparation
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
- First-slice data/rule registry with proposed stable IDs, economy arithmetic, mission stages, and crime event IDs.
- Asset manifest starter CSV covering the style anchors and first-slice asset candidates.
- Gate-by-gate first-slice production checklist.
- Art direction, concept-art briefs, initial asset catalog, and asset provenance expectations.
- Technical decision log, engine decision matrix, engine trial protocol, and staged roadmap.
- First-slice dependency/build order with acceptance criteria.
- Definition of Done and change-control rules for AI-assisted development.
- Read-only Linux engine-readiness diagnostic script; shell syntax was checked, but it has not been run on the owner's machine.
- Claude Code project rules, autonomous execution playbook, and copyable starting prompt.
- Consistency audit that corrected the opening courier/resource loop, economy arithmetic, processing location, and mission resumption rules.

## Current recommendation

Test Unreal Engine 5 first, with Godot 4 as a fallback. This is not yet a production-engine decision. The first test should use a disposable project and answer whether the editor, C++ build loop, and visual workflow are practical on the actual Linux machine.

## Current approval boundary

The owner has asked for autonomous progress where possible. This authorizes continued planning, documentation, research, consistency checks, and reversible pre-production work. It does **not** silently approve a production engine, production gameplay code, bulk final assets, system changes, or a larger game scope. Those should be presented as one concise recommendation when evidence is ready.

## Completed pre-production work

1. Added engine decision matrix with evidence requirements instead of invented numeric scores.
2. Added town greybox specification and SVG maps.
3. Added Claude's execution playbook and copyable starting prompt.
4. Audited the opening mission and corrected the case delivery, portal discovery, resource loop, processing location, resumption, and upgrade arithmetic.
5. Added dependency-aware first-slice build order and acceptance criteria.
6. Added a read-only Linux readiness script and validated its Bash syntax without running it on the owner's computer.
7. Added player-flow/UX rules and edge-case outcomes.
8. Added logical save-data requirements and failure/recovery tests without prematurely selecting a save format.
9. Added AI task completion, change-control, and milestone quality-gate rules.
10. Added an asset manifest starter and a gated first-slice production checklist.
11. Added a first-slice data/rule registry to reduce conflicting item values, mission flags, and crime triggers.
12. Updated the README to index the current pre-production documents.

## Workflow now underway

- **Step 1: Specification hardening** — asset manifest, player UX, save/recovery, rule registry, and milestone checklist are drafted.
- **Step 2: Cross-document reconciliation** — check mission, economy, crime, save persistence, asset requirements, and implementation gates for conflicts.
- **Step 3: Engine readiness evidence** — inspect the actual Linux setup before proposing any install or engine trial. The read-only diagnostic has not yet been run on the owner's machine.
- **Step 4: Engine trial recommendation** — present one recommended default with test evidence, limitations, and the smallest approval needed.
- **Step 5: After approval only** — create the disposable trial and validate it; production implementation remains separately gated.

## Highest-value next work

1. Finish the broader consistency pass and correct any conflicting wording.
2. Validate the CSV manifest structure and all newly added README links.
3. Prepare the engine trial protocol and plain-language decision report.
4. Ask the owner to run the read-only machine diagnostic only when that local evidence is the next true blocker.

## Risks still open

- Linux Mint version and toolchain compatibility have not been verified.
- The engine has not been installed or tested in this workflow.
- Console development access, porting costs, and certification remain unverified.
- No playable build or performance measurement exists yet.
- Final asset rights/provenance must be checked individually.
- Exact input bindings, save serialization format, autosave behavior, and numeric performance budget remain deliberately open until the engine trial.
- First-slice economy numbers are placeholders and need playtesting.

## Honest status rule

Documentation and plans are not a playable game. Do not describe the game as implemented, tested, performant, or console-ready until the corresponding work and checks have actually happened.
