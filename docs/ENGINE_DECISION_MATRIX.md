# Engine Decision Matrix — Practical Recommendation

**Status:** Decision support only. No engine has been selected.
**Owner priority:** Make development as easy as reasonably possible for a solo creator using AI coding assistance, while preserving a credible path to a polished 3D game.

## Executive recommendation

Treat **Unreal Engine 5 as the first candidate to test**, not as a permanent commitment. It offers an integrated 3D production environment, a mature character/vehicle/rendering toolset, C++ gameplay, controller support, and a strong visual-art pipeline. These fit the intended game better than choosing an engine solely because its codebase is smaller.

Keep **Godot 4 as the fallback** if the Unreal Linux setup, editor responsiveness, C++ build loop, or asset workflow becomes a major obstacle. Godot is lighter and its editor/project format can be simpler, but a C++-first workflow uses GDExtension boundaries and some high-end 3D production conveniences may need more custom work. Console releases in either engine are not automatic.

This is a hypothesis to test with a tiny disposable project. Do not build production content in either engine before the owner approves the result.

## Weighted comparison (initial hypotheses, not measured scores)

Weights: visual iteration 25%, Linux compatibility/performance 20%, C++/Claude workflow 20%, console path 20%, solo maintenance 15%.

| Criterion | Unreal Engine 5 | Godot 4 | What evidence is needed |
|---|---|---|---|
| Visual quality and iteration | Likely strongest integrated 3D authoring and lighting workflow | Capable stylized 3D; may require more custom presentation work | Build the same small street corner and alien clearing in each |
| Linux setup | Potentially heavier; distro/toolchain compatibility must be checked | Usually lighter; native Linux editor is a strength | Install/launch editor and compile a minimal native gameplay component |
| C++ workflow | C++ is a first-class gameplay path, but project builds and editor integration can be complex | C++ via godot-cpp/GDExtension; engine rebuild usually not required, but API boundary matters | Implement one interactable and one gameplay state in each |
| AI-assisted edits | Many examples and conventions; editor-authored assets need care | Text-friendly project files can be easier to diff; extension boundary can complicate iteration | Ask Claude to make a bounded change, inspect diff, run build, revert and repeat |
| Vehicle and character workflow | Mature integrated tools; still requires tuning and testing | Feasible, but may require more bespoke implementation | One walkable character, camera, drivable placeholder vehicle, recovery |
| Console feasibility | Established commercial console ecosystem, but SDK access, source builds, approval and certification remain separate | Usually involves platform-specific porting/partners; must be researched before promising releases | Document actual requirements and likely cost for each target platform |
| Solo project maintenance | Large tool surface and potentially large project/build footprint | Smaller, open-source, potentially easier to keep lean | Record setup time, edit/build iteration time, memory use, failure recovery |

**Do not assign numeric winner scores yet.** A guessed score would create false precision.

## Machine-specific risk to verify

The available project context indicates a Linux Mint desktop with an Intel i7-11700, 32 GB RAM, and RTX 3060 Ti (8 GB VRAM). That is a credible starting point for stylized 3D development, but the exact Mint version, graphics driver, free disk space, and installed compiler are unverified. Unreal's published Linux requirements may name specific Ubuntu/Rocky versions; Linux Mint compatibility must be tested rather than assumed.

Before installing a large engine or downloading assets, check:
- Distribution and version: `cat /etc/os-release`
- GPU and driver: `nvidia-smi`
- Free disk space: `df -h`
- Compiler: `clang++ --version` and `g++ --version`
- Vulkan availability: `vulkaninfo --summary` if installed

These commands are diagnostic only. Do not change system packages, drivers, BIOS settings, or disk partitions as part of an engine trial without explicit approval.

## Fair, bounded trial

Use disposable projects outside the production repository. Limit the experiment to the same five deliverables:
1. One small stylized street corner with fog and readable lighting.
2. One third-person character with camera collision and controller input.
3. One placeholder vehicle with enter/exit and basic driving.
4. One interactable object and one inventory item.
5. A reproducible Linux build/run procedure and one automated or scripted sanity check.

Record:
- Time to install/open editor and reach first run.
- Time to compile after a small C++ edit.
- Time to make and test a gameplay change with Claude.
- Editor responsiveness and runtime frame rate on the same scene.
- How cleanly changes appear in Git diffs.
- Any missing features that require custom tools.
- Console publishing prerequisites and unanswered questions.

Do not optimize graphics, create final assets, or build the town during this trial.

## Decision rule

Choose Unreal if it runs reliably on the actual Linux setup and the integrated 3D workflow meaningfully reduces the work needed for the intended art direction. Choose Godot if Unreal's setup/build/editor overhead repeatedly blocks progress and Godot reaches the same minimum visual and gameplay test with materially less friction. If neither trial is successful, stop and resolve the environment issue before starting production.

The owner should only need to review a concise report with screenshots, build results, setup friction, and a recommendation. No need to understand every technical detail.

## Sources to re-check at decision time

- Epic Linux quickstart: https://dev.epicgames.com/documentation/unreal-engine/linux-development-quickstart-for-unreal-engine
- Epic Linux requirements: https://dev.epicgames.com/documentation/unreal-engine/linux-development-requirements-for-unreal-engine
- Epic installation and platform notes: https://dev.epicgames.com/documentation/unreal-engine/install-unreal-engine
- Godot C++ bindings: https://docs.godotengine.org/en/stable/tutorials/scripting/cpp/
- Godot GDExtension configuration: https://docs.godotengine.org/en/stable/engine_details/engine_api/gdextension/gdextension_file.html
- Godot console guidance: https://docs.godotengine.org/en/stable/tutorials/platform/consoles.html

Links and requirements may change. Verify the engine version and platform-specific details at the time of the trial.
