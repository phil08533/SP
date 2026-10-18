# Space Hippie — first asset generation pack

This folder starts the **actual mesh-asset pipeline**, not concept-image generation.

## Generate the first props

Requires Blender 4.x installed locally. From the repository root, run:

```bash
blender --background --python tools/asset_generation/generate_dusty_junction_props.py
```

The script creates `assets/3d/dusty_junction/` and exports six independent glTF Binary (`.glb`) files:

- `dj_motel_sign.glb` — roadside motel sign and support posts
- `dj_fuel_pump.glb` — stylized pump, display, hose and nozzle
- `dj_street_lamp.glb` — low-poly street lamp
- `dj_supply_crate.glb` — reusable supply/storage crate
- `bloom_lumen_pod.glb` — faceted luminous alien resource
- `dj_portal_relay_frame.glb` — modular industrial relay frame

These are first-pass, procedural mesh assets with assigned materials, intended to be editable and easy to iterate. They are **not yet approved production assets**: inspect scale, pivots, normals, material appearance, and collision in Blender and in the eventual engine before use. The portal relay frame is a kit piece, not the final traversable portal.

## Conventions

- World scale: meters; upright assets use Z as up.
- Origin: currently generated around each asset's construction origin; inspect and adjust pivots for gameplay placement.
- Materials: named, cohesive stylized palette; no external textures required.
- Export: one GLB per prop so an engine importer can handle each item independently.
- No network calls, package installs, or project changes outside the generated asset output directory.

## Current limitation

The script is committed to the repository, but the GLB binaries are produced only when Blender runs it. No claim is made that the generator has been executed or engine-tested on Phil's machine. Run the command above and share any console errors if a correction is needed.
