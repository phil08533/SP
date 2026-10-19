# Definition of Done and Change Control

**Status:** Process specification for AI-assisted development.

## Why this exists

A coding agent can produce many files quickly while leaving the game hard to build, test, or reason about. Completion is measured by verified behavior, not lines of code or number of commits.

## Definition of done for a task

A task is complete only when all applicable items are true:

1. **Scope:** The change matches the approved task and does not silently add features.
2. **Specification:** Expected behavior and edge cases are documented.
3. **Implementation:** Changes are modular and named clearly; stable IDs are used for persistent content.
4. **Build:** The relevant build was run, or the report explicitly says it was not run and why.
5. **Tests:** Automated checks and relevant manual test steps were executed; results are reported exactly.
6. **Regression:** Nearby existing behavior was checked for breakage.
7. **Visual review:** For visual changes, a screenshot or short capture is reviewed at normal gameplay distance.
8. **Performance:** For representative scene changes, performance impact is measured once a baseline exists.
9. **Assets:** Every added third-party or generated asset has provenance, usage rights, source files where applicable, and import/collision/material checks.
10. **Documentation:** Controls, tuning, known limitations, and affected docs are updated.
11. **Repository hygiene:** No credentials, unrelated edits, generated caches, or accidental binaries are committed.
12. **Honest report:** Passed, failed, skipped, and untested checks are distinct.

Not every task requires every check. The task report must mark irrelevant items as N/A rather than pretending they passed.

## Change classes

### Class A — Safe routine change
Examples: typo correction, broken link fix, adding a missing test for already-specified behavior.
- AI may proceed within approved scope.
- Report changed files and checks.

### Class B — Reversible design or implementation choice
Examples: local variable naming, internal module boundary, a small UI layout detail within approved UX.
- AI may choose a sensible default, document it, and continue.
- Avoid asking the owner to adjudicate inconsequential choices.

### Class C — Owner decision required
Examples: engine/rendering strategy, save-format commitment, world scale, core loop, combat model, controller architecture, production asset style anchor, paid service, online feature, or scope expansion.
- Stop before making the consequential change.
- Present one recommended default, evidence, cost/risk, and the smallest decision needed.

### Class D — Prohibited without explicit authorization
Examples: production gameplay code before the gates pass, installing/updating system packages or drivers, destructive filesystem operations, changing partitions, adding credentials, merging the pre-production PR, or claiming console readiness without platform validation.
- Do not perform the action.
- Offer a safe preparation step instead.

## AI task contract

Before a coding task, record:
- Goal and player-visible outcome.
- Files expected to change.
- Dependencies and assumptions.
- Acceptance criteria.
- Validation command(s) and manual test path.
- Explicit out-of-scope items.

After the task, report:
- Files changed and why.
- Exact commands/checks run and results.
- What was not tested.
- Regressions or unresolved issues.
- Whether any decision gate was reached.

## Scope-change procedure

1. Add the idea to a backlog with player benefit, estimated complexity, dependencies, and risks.
2. Identify what it displaces or delays.
3. Decide whether it belongs in the first slice or post-slice.
4. If it changes an approved gate or owner decision, ask before implementing.
5. Update the roadmap and decision log only after the choice is made.

## Quality gate before a milestone is called complete

- No known blocker that prevents the required player journey.
- Acceptance tests have evidence, not just a checklist.
- All failures have an owner or next action.
- No unreviewed large asset batch.
- The branch builds from a clean checkout using documented steps.
- The milestone summary distinguishes implemented, tested, and merely planned work.
