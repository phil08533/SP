# Documentation Consistency Audit

**Date:** 2026-10-18
**Branch:** `preproduction/space-hippie-blueprint`
**Scope:** Cross-check opening mission, economy, crime boundaries, world layout, and production gates. This is a documentation audit, not a game test.

## Findings resolved

### 1. Courier case versus alien resource loop
**Issue:** Earlier text blurred delivery of Mara's sealed service case with delivery/sale of Lumen Pods. Dialogue also implied the player could finish the delivery instead of following the intended first-session portal loop.

**Resolution:** The case is an ordinary service component delivered to the marked Pumpworks drop point and left there. Its indicator reacts to the anomaly and reveals the portal. The player gathers Lumen Pods as a separate activity, returns, claims the courier fee, and chooses whether to sell raw pods or process them into Glow Resin. The mission is resumable and the player cannot be stranded.

### 2. First-upgrade economy arithmetic
**Issue:** The original text said the first storage upgrade should be “approachable” without showing how the first loop reaches its price.

**Resolution:** Current placeholder values are 25 credits for the courier job, 5 credits per raw Lumen Pod, 24 credits gross for one Glow Resin made from three pods, and 40 credits for the storage upgrade. Courier fee plus raw sales equals 40 credits before penalties or fees. Processing yields 49 credits total before any costs or penalties. These numbers still require playtesting.

### 3. Processing location and risk window
**Issue:** It was unclear whether the trade counter also processed goods.

**Resolution:** First processing happens at the hideout workbench. The trade counter buys raw pods, Glow Resin, and ordinary salvage; it does not process goods. This makes returning home useful and creates a readable risk window when carrying restricted Glow Resin through town.

### 4. Abandonment and reward rules
**Issue:** The first mission did not clearly say what happens if the player leaves after delivering the case but before completing the resource run.

**Resolution:** The mission remains active and resumable. The full 25-credit courier fee is claimed from Mara after the player returns from The Bloom. There is no partial payout or abandonment penalty in the first slice. This keeps the rule simple and avoids a softlock.

### 5. Required portal discovery versus trespass
**Issue:** The player must discover and enter the portal during the opening loop, while Pumpworks is a restricted site.

**Resolution:** The courier may legally reach the public-facing service drop. The inner portal boundary is clearly marked restricted. Crossing it can trigger a warning/tutorial beat, but enforcement must not block the required portal interaction or strand the player. Later trespass can carry a fine.

## Remaining open items

- Verify whether the target engine supports the desired art style and iteration workflow on the actual Linux setup. No local machine test has been performed.
- Confirm exact dimensions and travel times through greyboxing rather than treating early map estimates as final.
- Establish the initial controller mapping and interaction prompt behavior during the engine trial.
- Playtest the opening economy and adjust prices if the storage upgrade feels automatic or too far away.
- Verify third-party asset rights and provenance for every asset selected for production.

## Validation boundary

This audit checks design-text coherence only. It does not validate gameplay, save/load, balance, performance, console readiness, asset licensing, or engine compatibility. Those require implementation or source-specific verification.
