# Claude Code Execution Playbook

**Purpose:** Make the work as low-friction as possible for the owner while preventing a coding agent from turning a small game into an untestable pile of features.

This playbook supplements `CLAUDE.md`. If instructions conflict, follow the stricter approval gate in `CLAUDE.md`.

## Working style

The owner should not have to micromanage filenames, routine implementation choices, or every small design detail. Claude should make reversible, low-risk decisions independently, document assumptions, and present only decisions that truly affect the project direction.

### Claude may do independently
- Read project documents and identify contradictions, missing requirements, and duplicated concepts.
- Research engine/version requirements and summarize trustworthy sources.
- Improve pre-production documents and cross-link the documentation.
- Create mock layouts, task lists, acceptance criteria, test plans, and asset briefs.
- Suggest low-cost/offline tools and identify license/provenance risks.
- Prepare a bounded implementation plan and list expected files before any authorized coding.
- Once implementation is authorized, make small scoped changes, run available checks, and report exact results.
- Use temporary/disposable experiments after they are authorized, without mixing them into production.

### Claude must not do without the required approval
- Silently choose the production engine or change it later.
- Start production gameplay code or generate bulk final assets before the documented gates are approved.
- Add multiplayer, online persistence, paid services, analytics, or a developer-operated backend.
- Expand the first slice beyond its approved boundaries.
- Install/update system packages, drivers, or destructive tools; alter disk partitions; or expose credentials.
- Claim builds, tests, performance, console support, or gameplay work without evidence.
- Add assets with unclear licensing or provenance.

## Low-effort approval format

When the project reaches an approval gate, give the owner a short report with:
1. **Recommendation** in plain language.
2. **What was tested** and what was not.
3. **Screenshots or a short capture** where useful.
4. **Known problems and likely costs.**
5. **One clear decision request**, with a recommended default.

Do not ask the owner to choose between many technical alternatives if a sensible default can be recommended. If the decision is reversible and within approved scope, choose the default and record it.

## Safe autonomous workflow

1. Read `CLAUDE.md` and the relevant design documents.
2. Check the current Git branch, status, and latest commits before editing.
3. Keep documentation changes on a dedicated branch until reviewed.
4. State the narrow objective, expected files, risks, and acceptance criteria.
5. Make the smallest useful change; preserve unrelated work.
6. Run available validation. If an engine/editor is unavailable, say so explicitly.
7. Inspect the diff for accidental changes, duplicated content, and broken links.
8. Update documentation and the change log if decisions or behavior changed.
9. Report what changed, checks actually run, known limitations, and the next low-effort step.

## AI-assisted asset workflow

- First establish a visual target using a small number of style-anchor assets.
- Use generated concept art as reference only unless the output is intentionally suitable as a final asset and its rights/provenance are acceptable.
- For game-ready geometry, verify scale, silhouette, pivots, collision, material count, texture sizes, and import behavior in-engine.
- Keep a source manifest for every third-party or generated asset: source/tool, date, license/terms, modifications, and intended use.
- Prefer modular, reusable props over one-off detail.
- Never bulk-produce content until one building, one character, one vehicle, one alien plant, and one crystal have passed an in-engine style review.

## Definition of a useful progress update

A useful update says:
- what durable artifact changed,
- where it is in Git,
- which checks actually passed,
- what remains blocked,
- what decision (if any) is needed from the owner.

Avoid generic progress messages, repeated summaries, and false certainty.
