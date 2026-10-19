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
- Engine trial scorecard with evidence fields and a fair comparison procedure.
- Art direction, concept-art briefs, initial asset catalog, and asset provenance expectations.
- Technical decision log, engine decision matrix, and staged roadmap.
- First-slice dependency/build order with acceptance criteria.
- Definition of Done and change-control rules for AI-assisted development.
- Read-only Linux engine-readiness diagnostic script; shell syntax was checked, but it has not been run on the owner's machine.
- Claude Code project rules, autonomous execution playbook, and copyable starting prompt.
- Expanded consistency audit across mission/economy, trespass, UX, save/recovery, asset scope, and data-registry drift.

## Current recommendation

Test Unreal Engine 5 first, with Godot 4 as a fallback. This is not yet a production-engine decision. The first test should use a disposable project and answer whether the editor, C++ build loop, and visual workflow are practical on the actual Linux machine.

## Current approval boundary

The owner has asked for autonomous progress where possible. This authorizes continued planning, documentation, research, consistency checks, and reversible pre-production work. It does **not** silently approve a production engine, production gameplay code, bulk final assets, system changes, or a larger game scope. Those should be presented as one concise recommendation when evidence is ready.

## Workflow now underway

1. **Specification hardening:** asset manifest, player UX, save/recovery, rule registry, and milestone checklist are drafted.
2. **Cross-document reconciliation:** mission, economy, crime, save persistence, asset requirements, and implementation gates are being reconciled. The audit is updated; CSV and link validation remain.
3. **Engine readiness evidence:** inspect the actual Linux setup before proposing any install or engine trial. The read-only diagnostic has not yet been run on the owner's machine.
4. **Engine trial recommendation:** use the scorecard to compare a disposable Unreal project against a Godot project with the same minimum deliverables.
5. **After approval only:** create/run the disposable trial; production implementation remains separately gated.

## Completed in the current workflow

- Added an asset manifest starter and gated first-slice production checklist.
- Added a first-slice data/rule registry to reduce conflicting item values, mission flags, and crime triggers.
- Corrected opening mission prose so the first upgrade's base arithmetic is clear and optional specimen income is genuinely optional.
- Narrowed asset catalog wording so every listed character/prop is not mistakenly treated as mandatory for the slice.
- Expanded the consistency audit to cover interaction UX, save transactions, asset scope, and data-registry drift.
- Added a repeatable engine trial scorecard without inventing measurements.
- Updated README and project status to index the workflow artifacts.

## Highest-value next work

1. CSV syntax has been parsed and validated; the newly added README-linked files, maps, and diagnostic script were fetched successfully from the working branch. The rest of the README links still need a complete sweep.
2. The early-return edge case is now specified: courier payout is earned independently after case delivery and return; the resource objective remains resumable until three pods are collected.
3. Run the read-only Linux diagnostic and inspect results before choosing an engine trial route.
4. Present one concise engine recommendation when the machine-specific evidence is available.

## Risks still open

- Linux Mint version and toolchain compatibility have not been verified.
- The engine has not been installed or tested in this workflow.
- Console development access, porting costs, and certification remain unverified.
- No playable build or performance measurement exists yet.
- Final asset rights/provenance must be checked individually.
- Exact input bindings, save serialization format, autosave behavior, witness detection distances, and numeric performance budget remain deliberately open until the relevant test/design gate.
- First-slice economy numbers are placeholders and need playtesting.

## Honest status rule

Documentation and plans are not a playable game. Do not describe the game as implemented, tested, performant, or console-ready until the corresponding work and checks have actually happened.
