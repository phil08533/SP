# Documentation Consistency Audit

**Date:** 2026-10-18
**Branch:** `preproduction/space-hippie-blueprint`
**Scope:** Cross-check opening mission, economy, world layout, and production gates. This is a documentation audit, not a game test.

## Findings resolved

### 1. Courier case versus alien resource loop
**Issue:** The earlier opening-mission text blurred delivery of Mara's sealed service case with delivery/sale of the Lumen Pods. Dialogue also implied the player could simply finish the delivery instead of following the intended first-session portal loop.

**Resolution:** The case is now an ordinary service component delivered to the marked Pumpworks drop point and left there. Its indicator reacts to the anomaly and reveals the portal. The player gathers Lumen Pods as a separate activity, returns, claims the courier fee, and then chooses whether to sell raw pods or process them into Glow Resin. The objective is resumable and the player cannot be stranded.

### 2. First-upgrade economy arithmetic
**Issue:** The original text said the first storage upgrade should be “approachable” without showing how the first loop reaches its price.

**Resolution:** Current placeholder values are 25 credits for the courier job, 5 credits per raw Lumen Pod, 24 credits gross for one Glow Resin made from three pods, and 40 credits for the storage upgrade. Courier fee plus raw sales equals 40 credits before penalties or fees. Processing yields 49 credits total before any costs/penalties. These numbers still require playtesting.

## Remaining open questions (not blockers for design work)

- Decide whether processing occurs at the hideout workbench, a public station, or both. Recommended default: first processing occurs at the hideout workbench, while public buyers only purchase finished goods. This gives the player a clear reason to return home and creates a legible risk window when carrying restricted cargo through town.
- Decide whether the first mission's portal/resource segment is strictly required for completion or can be abandoned for a reduced courier fee. Recommended default: allow abandonment and resumption, but reserve the full courier reward for completing the round trip.
- Verify whether the target engine supports the desired art style and iteration workflow on the actual Linux setup. No local machine test has been performed.
- Confirm exact dimensions and travel times through greyboxing rather than treating early map estimates as final.
- Establish the initial controller mapping and interaction prompt behavior during the engine trial.

## Validation boundary

This audit checks the design text for coherence only. It does not validate gameplay, save/load, balance, performance, console readiness, asset licensing, or engine compatibility. Those require implementation or source-specific verification.
