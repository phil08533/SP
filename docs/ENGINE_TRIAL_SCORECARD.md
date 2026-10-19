# Engine Trial Scorecard

**Purpose:** Capture evidence from a bounded Unreal Engine 5 vs Godot 4 trial.
**Status:** Blank template. Do not fill unknowns with estimates or use this scorecard as permission to install an engine.
**Rule:** Use disposable projects outside the production repository. Test the same minimum deliverables and record failures as evidence.

## Trial metadata

- Date:
- Tester:
- Linux distribution/version:
- Kernel:
- CPU/RAM:
- GPU/driver/VRAM:
- Free disk before trial:
- Display resolution:
- Controller tested:
- Engine version/build:
- Project storage location:
- Trial start/end time:
- Commands/log locations:

## Gate 0 — Machine readiness

| Check | Result | Evidence / exact output | Blocker? |
|---|---|---|---|
| Distribution matches documented support route | Not tested | | |
| GPU and driver identified | Not tested | | |
| Vulkan tools/device report available | Not tested | | |
| Required compiler/toolchain available | Not tested | | |
| Sufficient free disk for editor, source/build artifacts, and sample assets | Not tested | | |
| No system changes needed without owner approval | Not tested | | |

## Identical deliverables for each engine

For each deliverable, record **Pass / Partial / Fail / Not tested**, elapsed time, exact issue, and evidence path.

| Deliverable | Unreal result/time | Godot result/time | Evidence |
|---|---|---|---|
| Editor installs/opens and creates a disposable project | Not tested | Not tested | |
| Project launches from documented steps | Not tested | Not tested | |
| Third-person movement and camera collision | Not tested | Not tested | |
| Keyboard/mouse and controller action parity | Not tested | Not tested | |
| One interactable object with prompt and feedback | Not tested | Not tested | |
| One inventory item and a simple state change | Not tested | Not tested | |
| One placeholder vehicle can enter/exit and drive | Not tested | Not tested | |
| One stylized street corner with fog/readable light | Not tested | Not tested | |
| One imported model follows the documented pipeline | Not tested | Not tested | |
| Small gameplay code edit by Claude compiles and works | Not tested | Not tested | |
| Clean build/run procedure works after closing editor | Not tested | Not tested | |
| One repeatable sanity test/check runs | Not tested | Not tested | |
| Project changes are understandable in Git diff | Not tested | Not tested | |

## Measurements (record, do not infer)

| Measurement | Unreal | Godot | Notes |
|---|---:|---:|---|
| Download/install time | | | Exclude time spent researching unsupported routes; note separately |
| Time to first successful launch | | | |
| Time to first successful C++ gameplay build | | | |
| Time for one Claude-assisted edit → test cycle | | | |
| Editor idle memory use | | | Same machine conditions where possible |
| Runtime FPS in agreed test scene | | | Record resolution/settings and warm-up |
| Largest recurring friction point | | | |
| Custom systems needed for minimum slice | | | |
| Recovery after a failed build/edit | | | |

## Console path check

Do not claim console readiness from a desktop prototype. For each target platform, record official prerequisites, developer access requirements, source-build/porting requirements, likely third-party help, and cost information only when sourced.

| Platform | Official route/source | Access prerequisites | Porting/approval uncertainty | Status |
|---|---|---|---|---|
| PlayStation | | | | Unverified |
| Xbox | | | | Unverified |

## Decision summary

- **Hard blockers:**
- **Best evidence for Unreal:**
- **Best evidence for Godot:**
- **Which engine reached all required deliverables with less friction?**
- **Visual quality comparison:**
- **Build and iteration comparison:**
- **Controller and vehicle comparison:**
- **Known risks:**
- **Recommendation:**
- **Confidence:** Low / Medium / High, with reason
- **What has not been tested:**
- **Owner approval required before next phase:** Yes

## Decision rule

1. A hard blocker means the engine cannot be used on the actual setup without a separately approved fix.
2. Prefer the engine that passes the minimum deliverables reliably and reduces repeated setup/iteration friction.
3. Visual quality is judged in the actual test scene, not feature lists or marketing screenshots.
4. Console pathways remain separate risks until platform-specific evidence is gathered.
5. Do not turn a blank or incomplete trial into a winner by assigning guessed scores.
6. After the owner approves a candidate, retain the other disposable project only as a reference; do not start production work until the vertical-slice plan is also approved.
