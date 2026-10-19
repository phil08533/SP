# Roadmap, Vertical Slice, and Acceptance Tests

## Gate 0 — Pre-production approval (current)
Complete GDD, world layout, cast/dialogue, system specifications, art bible, asset pipeline, engine comparison plan, roadmap, and Claude rules. Resolve contradictions. No production code.

## Gate 1 — Engine validation
After explicit authorization, validate Linux editor/build workflow, C++ path, target visual quality, input/controller, character/camera, physics, asset import, and performance. Document console pathway and costs/risks. Owner approves engine and implementation model.

## Gate 2 — Greybox slice
Only: small town blockout, player movement/camera, one vehicle, hideout, portal transition, small dimension blockout, interaction, one resource, one sale/crafting choice, one mission, save/load. Greybox art is intentional. Goal is to prove the loop.

## Gate 3 — Feel and art approval
Tune movement, camera, vehicle, interaction feedback, portal, and readability. Approve one building, character, vehicle, plant, and crystal as style anchors. No bulk production before approval.

## Gate 4 — Polished vertical slice
Finish the bounded route, one authored mission plus optional branch, initial suspicion response, UI/audio feedback, controller support, robust save/load, and acceptance/performance checks.

## Gate 5 — Expansion decision
Only if slice is fun and stable, decide whether to add more missions, district content, buyers, NPC schedules, vehicle upgrades, or a second dimension. Review costs and dependencies first.

## Vertical slice player journey
Leave hideout → take a job from Mara → drive to Pumpworks → enter The Bloom → collect at least three Lumen Pods → optionally risk a rare specimen → return → sell raw materials or process into Glow Resin → resolve simple witness/enforcement response if triggered → buy one meaningful upgrade.

## Acceptance tests
### Movement/camera
- Player cannot fall through valid ground.
- Camera avoids major wall clipping.
- Keyboard/mouse and controller perform the same core actions.
- Test-build recovery exists for trapped/invalid state.

### Vehicle
- Enter/exit can be repeated without duplication/loss.
- Steering, braking, reversing, camera are understandable.
- Recovery exists if trapped.
- Mission remains completable if vehicle is left elsewhere.

### Mission/interactions
- Every required objective has clear feedback.
- Mission completes after save/load.
- Leaving objective area does not soft-lock progress.
- Repeated interaction cannot duplicate rewards/items.

### Portal/resources
- Safe spawn in destination.
- Inventory and mission state persist across travel.
- Failed transition preserves inventory and returns to source.
- Pickup respects capacity and cannot be repeated from a depleted node.

### Economy
- Sale consumes correct items and grants currency exactly once.
- Crafting consumes inputs and produces output atomically.
- Player can earn basic repair money.
- Risk/reward is communicated.

### Crime/NPCs
- Suspicion only rises from defined events.
- Witness detection is plausible unless a scripted exception is documented.
- Player understands what triggered the response.
- Response can be resolved without mandatory combat.

### Save/load
- Currency, inventory, mission, upgrades, and world restore consistently.
- Unknown IDs/old versions fail safely.
- Corrupt/interrupted save does not silently overwrite last valid save.
- Vehicle does not load inside geometry.

### Art/performance
- Landmarks read from gameplay camera.
- Materials, lighting, proportions match art bible.
- Collision uses simplified geometry where appropriate.
- Profile town and dimension separately on target PC.
- Set numeric performance target after baseline benchmark, then enforce it.

## Test report template
Scope/files changed; build command/result; automated checks/results; manual steps/results; performance/hardware/settings; acceptance criteria passed/failed/not tested; known issues; next recommendation.

## Risk register
| Risk | Impact | Mitigation |
|---|---|---|
| Choosing engine by reputation | High | Bounded comparative validation |
| Art scope overwhelms solo developer | High | Approve style anchors and modular kits |
| Vehicle physics consumes schedule | High | Arcade handling, one vehicle, recovery |
| Open-world AI expands uncontrollably | High | Bounded states and off-screen simplification |
| Economy becomes spreadsheet-heavy | Medium | Fixed prices until core loop is fun |
| Portal transition corrupts state | High | Transactional transition tests |
| AI changes unrelated systems | High | Small tasks, explicit file scope, Git checkpoints |
| Console goal creates false confidence | High | Research access/porting early; no guarantees |
| Generated asset licensing/style problems | High | Review and provenance register |
| Scope creep | High | Backlog ideas and require gate approval |

## Suggested implementation order after approval
1. Toolchain and empty project validation.
2. Character/camera/ground/collision.
3. Interaction and input abstraction.
4. Vehicle enter/drive/exit/recovery.
5. Town greybox and hideout.
6. Inventory/currency and pickup/sale.
7. Portal transition and dimension blockout.
8. Mission objectives and save/load.
9. First mission end-to-end.
10. Suspicion/witness/enforcement response.
11. Art anchors and audio feedback.
12. Polished slice, controller QA, performance pass.

Reorder only when a validated dependency requires it, and document the reason.
