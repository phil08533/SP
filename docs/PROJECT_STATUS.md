# Space Hippie — Project Status

**Last updated:** 2026-10-18
**Current phase:** Pre-production documentation
**Production engine:** Not selected
**Production gameplay code:** Not started
**Current working branch:** `preproduction/space-hippie-blueprint`
**Review pull request:** https://github.com/phil08533/SP/pull/1

## What exists

- Core game concept, pillars, first-session arc, and bounded first playable scope.
- Dusty Junction town design and The Bloom dimension, with a measurable greybox blockout brief.
- Character roster and dialogue, mission/progression, portal, economy, crime/suspicion, save/load, and interaction concepts.
- Art direction, concept-art briefs, initial asset catalog, and asset provenance expectations.
- Technical decision log, engine decision matrix, engine trial protocol, and staged roadmap.
- Claude Code project rules, autonomous execution playbook, and copyable starting prompt.
- Consistency audit that corrected the opening courier/resource loop, economy arithmetic, processing location, and mission resumption rules.
- README's 19 linked project documents were individually fetched successfully from the working branch.

## Current recommendation

Test Unreal Engine 5 first, with Godot 4 as a fallback. This is not yet a production-engine decision. The first test should use a disposable project and answer whether the editor, C++ build loop, and visual workflow are practical on the actual Linux machine.

## Current approval boundary

The owner has asked for autonomous progress where possible. This authorizes continued planning, documentation, research, consistency checks, and reversible pre-production work. It does **not** silently approve a production engine, production gameplay code, bulk final assets, system changes, or a larger game scope. Those should be presented as one concise recommendation when evidence is ready.

## Completed this session

1. Added an engine decision matrix with explicit evidence requirements instead of invented numeric scores.
2. Added a town greybox specification with routes, landmark requirements, scale targets, and acceptance checks.
3. Added Claude's execution playbook and a copyable starting prompt.
4. Audited the opening mission and made the sealed-case delivery, portal discovery, resource loop, processing location, and first-upgrade math consistent.
5. Updated the README and draft PR description to index the new material.

## Highest-value next work

1. Finish a broader consistency pass across progression, crime, save/load, and asset requirements.
2. Complete a first-slice dependency list so implementation order is unambiguous.
3. Prepare a tiny engine trial with identical acceptance criteria for Unreal and Godot.
4. Verify the actual Linux distribution, driver, disk space, and compiler before recommending an install path.
5. Present a short owner-facing decision brief with a recommended default and the few remaining risks.

## Risks still open

- Linux Mint version and toolchain compatibility have not been verified.
- The engine has not been installed or tested in this workflow.
- Console development access, porting costs, and certification remain unverified.
- No playable build or performance measurement exists yet.
- Final asset rights/provenance must be checked individually.

## Honest status rule

Documentation and plans are not a playable game. Do not describe the game as implemented, tested, performant, or console-ready until the corresponding work and checks have actually happened.
