# First-Slice Production Checklist

**Status:** Pre-production checklist. No item below authorizes implementation by itself.
**Scope:** One hideout, one compact town route, one vehicle, Pumpworks, one portal, The Bloom, one mission, one resource/crafting/sale choice, one simple suspicion response, local save/load.

## Gate A — Ready to create the test project

- [ ] Owner approves the engine and vertical-slice plan.
- [ ] Actual Linux distribution, kernel, GPU/driver, free disk, compiler, and Vulkan availability are checked.
- [ ] Engine install/build route is confirmed for that exact system; no driver/system changes without separate approval.
- [ ] Disposable project trial proves editor opens, C++ build runs, project launches, and a clean checkout can be rebuilt.
- [ ] Keyboard/mouse and controller action-map feasibility is demonstrated.
- [ ] Third-person camera/movement, simple vehicle physics, stylized lighting, and a representative imported asset are tested.
- [ ] Baseline performance capture is recorded at declared resolution/settings.
- [ ] Console assumptions are documented as unverified unless platform access and an actual porting route are confirmed.
- [ ] Owner explicitly approves engine, implementation model, and slice boundary.

## Gate B — Project foundation

- [ ] Clean repository and engine version are pinned/documented.
- [ ] Linux setup, build, launch, test, and recovery instructions are reproducible.
- [ ] Input actions are semantic, not scattered hard-coded key checks.
- [ ] Stable ID conventions and folder/naming conventions are established.
- [ ] Logging and a safe test recovery path exist.
- [ ] A clean checkout builds and launches before feature work begins.

## Gate C — Core feel

- [ ] Third-person movement and camera collision work near walls and in tight spaces.
- [ ] Controller and keyboard/mouse complete the same core actions.
- [ ] Interaction prompt supports success, unavailable, out-of-range, and invalid-state feedback.
- [ ] Pause/settings focus cannot activate gameplay actions behind menus.
- [ ] Player can recover from a trapped test position.
- [ ] One graybox character, building, vehicle, plant, and crystal are evaluated at gameplay distance before asset expansion.

## Gate D — State and persistence

- [ ] Item, mission, recipe, upgrade, NPC, resource-node, and vehicle IDs are stable.
- [ ] Inventory stack limits and full-capacity behavior are defined.
- [ ] Mission state machine supports resume after leaving and save/load.
- [ ] Sale, craft, upgrade, and reward operations are atomic and idempotent.
- [ ] Save schema is versioned; last known-good save survives interrupted writes where practical.
- [ ] Corrupt/unknown saves fail safely without destructive overwrite.
- [ ] Save/load tests cover every opening mission stage and economy transaction.

## Gate E — Greybox town and vehicle

- [ ] Hideout spawn, Mara interaction, workbench, storage, and trade counter are reachable.
- [ ] Main road and optional rough shortcut are visually distinct.
- [ ] Player can find Pumpworks without depending exclusively on a map marker.
- [ ] Public courier drop and restricted inner boundary are visibly different.
- [ ] One compact vehicle can be entered/exited repeatedly without duplication/loss.
- [ ] Vehicle recovery exists; leaving it elsewhere never blocks mission completion.
- [ ] Required landmarks read from the normal gameplay camera.
- [ ] Greybox scale and travel times are measured in-engine, not treated as final from map estimates.

## Gate F — Portal and The Bloom

- [ ] Portal transition validates state and prevents duplicate activation.
- [ ] Player arrival point is safe and ground/collision is validated.
- [ ] Return portal is visible from the arrival shelf and identifiable from elsewhere.
- [ ] Inventory, mission, and world state survive both travel directions.
- [ ] Failed transition restores a valid source state without losing items.
- [ ] Vehicle remains safely persisted in town; no vehicle physics is carried between dimensions.
- [ ] Lumen Pod pickup has idle/ready/depleted state and cannot be harvested twice.
- [ ] The first hazard has visible/audio precursor, active window, and cooldown; no frame-perfect dodge required.
- [ ] Player can return without collecting every optional item.

## Gate G — Mission, economy, and crime

- [ ] “A Small Favor” can start, pause/resume, complete, and recover from interruption.
- [ ] Sealed case is delivered to Pumpworks and is not required in The Bloom.
- [ ] Courier fee is claimed once, from Mara after return.
- [ ] Three raw pods sell for 15 credits at placeholder prices.
- [ ] Three pods craft into one Glow Resin for 24 gross credits; inputs/output commit atomically.
- [ ] Courier plus raw sale yields 40 credits before fees/penalties; values are playtest placeholders.
- [ ] Storage upgrade costs 40 and applies exactly once.
- [ ] Workbench crafts; trade counter buys only.
- [ ] Restricted inner boundary can warn the player without blocking the required portal interaction.
- [ ] Glow Resin suspicion is triggered only by defined witness/exposure rules.
- [ ] Enforcement response is understandable and can be resolved without mandatory combat.
- [ ] Player can complete the required route without optional specimen or optional character content.

## Gate H — Art, audio, accessibility, and polish

- [ ] Style anchors are approved in-engine before bulk asset creation.
- [ ] Asset manifest records source/tool, date, license/terms, modifications, source file, import notes, and review status.
- [ ] Character, building, vehicle, plant, and crystal pass scale/silhouette/material/collision checks.
- [ ] Critical prompts communicate with text/icon/shape plus color, never color alone.
- [ ] Dialogue and important voiced cues have subtitles.
- [ ] Dialogue, ambience, effects, and music volumes are independently adjustable where feasible.
- [ ] Town and Bloom ambience have distinct identities without masking important cues.
- [ ] Visual effects do not obscure interaction, pickups, hazards, or return portal.
- [ ] Numeric performance targets are set only after baseline measurement.
- [ ] No required ray tracing or untested expensive effect is assumed.

## Gate I — Release candidate for the slice

- [ ] Clean checkout build succeeds using documented steps.
- [ ] Full first-session player journey passes from new game to first upgrade.
- [ ] Keyboard/mouse and controller both pass the full journey.
- [ ] Save/load fault and transaction tests pass.
- [ ] No known issue blocks mission completion or traps the player.
- [ ] Manual test report records environment, settings, results, screenshots, and untested items.
- [ ] Performance is measured in town and The Bloom on the target development PC.
- [ ] All shipped assets have reviewed provenance and commercial-use rights.
- [ ] Owner reviews a playable build and approves the expansion decision separately.

## Explicitly out of scope for this slice

- Multiplayer, public servers, online persistence, and developer-operated backend.
- More than one dimension.
- Large-scale world streaming or a seamless portal transition.
- Multiple player vehicles, deep vehicle maintenance, or complex driving simulation.
- Full combat system, police simulation, faction system, or large NPC schedules.
- Bulk final art before style anchors are approved.
- Console-ready claims without access, porting, and certification validation.
