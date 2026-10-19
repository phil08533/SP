# Documentation Consistency Audit

**Date:** 2026-10-18
**Branch:** `preproduction/space-hippie-blueprint`
**Scope:** Cross-check opening mission, economy, crime boundaries, world layout, player interaction, save/recovery, asset priorities, and production gates. This is a documentation audit, not a game test.

## Findings resolved

### 1. Courier case versus alien resource loop
**Issue:** Earlier text blurred delivery of Mara's sealed service case with delivery/sale of Lumen Pods. Dialogue also implied the player could finish the delivery instead of following the intended first-session portal loop.

**Resolution:** The case is an ordinary service component delivered to the marked Pumpworks drop point and left there. Its indicator reacts to the anomaly and reveals the portal. The player gathers Lumen Pods as a separate activity, returns, claims the courier fee, and chooses whether to sell raw pods or process them into Glow Resin. The mission is resumable and the player cannot be stranded.

### 2. First-upgrade economy arithmetic
**Issue:** The original text implied the optional rare specimen might be needed to afford the first upgrade, despite the base route already reaching its placeholder price.

**Resolution:** Current placeholder values are 25 credits for the courier job, 5 credits per raw pod, 24 credits gross for one Glow Resin made from three pods, and 40 credits for the storage upgrade. Courier fee plus raw sales equals 40 credits before penalties or fees. Processing yields 49 credits total before costs or penalties. The optional rare specimen is extra income, not a requirement. These values still require playtesting.

### 3. Processing location and risk window
**Issue:** It was unclear whether the trade counter also processed goods.

**Resolution:** First processing happens at the hideout workbench. The trade counter buys raw pods, Glow Resin, and ordinary salvage; it does not process goods. This makes returning home useful and creates a readable risk window when carrying restricted Glow Resin through town.

### 4. Abandonment and reward rules
**Issue:** The first mission did not clearly say what happens if the player leaves after delivering the case but before completing the resource run.

**Resolution:** The mission remains active and resumable. The full 25-credit courier fee is claimed from Mara after returning to Dusty Junction. There is no partial payout or abandonment penalty in the first slice. Collected resources are not deleted, and the player cannot be stranded in a dimension.

### 5. Required portal discovery versus trespass
**Issue:** The player must discover and enter the portal during the opening loop, while Pumpworks is a restricted site.

**Resolution:** The courier may legally reach the public-facing service drop. The inner portal boundary is clearly marked restricted. Crossing it can trigger a warning/tutorial beat, but enforcement must not block the required portal interaction or strand the player. Later trespass can carry a fine.

### 6. Interaction behavior and failure feedback
**Issue:** A generic interaction system could leave prompts, invalid actions, full inventory, repeated activation, or controller focus behavior to guesswork.

**Resolution:** The UX specification now requires explicit preconditions, prompts, success/failure feedback, repeated-activation safety, and keyboard/mouse-controller parity. Exact bindings remain deferred until the engine trial.

### 7. Save/load and transaction safety
**Issue:** A list of saved fields alone would not prevent duplicate rewards, partial crafting transactions, or destructive handling of corrupt saves.

**Resolution:** The save specification now requires stable IDs, versioning, atomic economy operations, safe handling of interrupted/corrupt saves, and mission-stage acceptance tests. The actual file format and autosave cadence remain open until an engine-specific prototype.

### 8. Asset scope versus asset wish list
**Issue:** The broad concept catalog could be interpreted as requiring every listed character, prop, and environment for the first slice.

**Resolution:** The catalog now points to the asset manifest and distinguishes required assets from candidates. The first slice is limited to one compact vehicle, core town landmarks, the portal, The Bloom's first resource loop, and only the characters needed for the approved journey. Bulk assets remain gated on in-engine style anchors.

### 9. Registry and document drift
**Issue:** Item values, mission stages, and crime triggers can drift if each document or script becomes its own independent source.

**Resolution:** A proposed first-slice data/rule registry now consolidates stable IDs, placeholder prices, recipe arithmetic, mission stage concepts, and crime event IDs. When implementation is approved, tunable data should come from one authoritative data definition where practical. Registry values are not yet playtested.

## Remaining open items

- Verify engine support and iteration workflow on the actual Linux setup. No local machine test has been performed.
- Confirm exact dimensions and travel times through greyboxing rather than treating map estimates as final.
- Finalize controller bindings during the engine trial.
- Keep early-return behavior explicit in implementation: after returning to town, the courier fee may be claimed once if the case was delivered; the three-pod resource objective remains active until complete.
- Define witness distance/visibility and suspicion cooldown before implementing crime response.
- Establish exact save format, autosave policy, and whether suspicion persists across sessions after engine selection.
- Playtest the opening economy and adjust prices if the storage upgrade feels automatic or too far away.
- Verify third-party asset rights and provenance for every asset selected for production.
- Validate the asset CSV with a proper CSV parser and check all README links before calling documentation QA complete.

## Validation boundary

This audit checks design-text coherence only. It does not validate gameplay, save/load, balance, performance, console readiness, asset licensing, or engine compatibility. Those require implementation or source-specific verification.
