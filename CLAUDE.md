# CLAUDE.md — Space Hippie Project Rules

## Current phase
Pre-production. This repository contains a design blueprint, not permission to implement the game.

**Do not write production gameplay code, create a production engine project, or generate bulk assets until the owner explicitly approves both the technical direction and vertical-slice plan.** Documentation, research, risk analysis, and proposed design edits are allowed.

## Read before substantial work
- `docs/MASTER_BLUEPRINT.md`
- `docs/GDD.md`
- `docs/WORLD_DESIGN.md`
- `docs/CHARACTERS_DIALOGUE.md`
- `docs/SYSTEMS.md`
- `docs/ART_BIBLE_ASSET_PIPELINE.md`
- `docs/TECHNICAL_DECISIONS.md`
- `docs/ROADMAP_TESTING.md`

If documents conflict, stop and identify the contradiction. Approved owner decisions outrank provisional proposals. Record major decisions in the decision log.

## Non-negotiable principles
- Build a small, beautiful, playable game first.
- Single-player/offline-first. No required backend, multiplayer, or recurring service costs in the initial scope.
- Do not add unapproved major features or silently replace functioning systems.
- Prefer small, modular, comprehensible changes.
- Support keyboard/mouse and controller from the beginning; mobile is not a target.
- Protect the art bible and use fictional sci-fi contraband, not real-world manufacturing instructions.
- Console releases are goals, not guarantees.
- Mark assumptions as assumptions. Never claim untested code works.

## Workflow after implementation is authorized
1. Read the relevant specification.
2. State task scope, expected files, dependencies, risks, and acceptance criteria.
3. Implement a bounded change.
4. Run the relevant build/tests that are actually available.
5. Report exact checks and outcomes. A successful build is not proof of correct gameplay.
6. Include manual test steps, known issues, and next steps.
7. Update documentation and preserve a known-good Git state.
8. Never rewrite or discard unrelated changes.

## Approval required
Ask before changing engine, rendering strategy, save format, input architecture, world scale, core loop, or approved scope. Put new ideas in a backlog with cost/dependencies rather than implementing them automatically.

## Conventions once coding is authorized
- Use descriptive names and focused modules.
- Separate domain rules from presentation and engine integration where practical.
- Use stable IDs for items, missions, NPCs, recipes, and upgrades.
- Use data assets for tunable content where helpful; avoid needless abstraction.
- Make portal transitions and save/load failure-safe.
- Keep secrets, tokens, proprietary SDKs, and credentials out of Git.
- Track third-party asset source, license, and commercial-use rights.
- Use branches for substantial work; never force-push without approval.

## Definition of done
A feature is complete only when its specified behavior exists, relevant checks have been run, manual test paths are recorded, limitations are documented, and unrelated systems were not silently changed.
