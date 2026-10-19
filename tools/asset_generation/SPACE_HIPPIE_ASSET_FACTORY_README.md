# Space Hippie Procedural Asset Factory

This generator creates individually exported low-poly GLB models for use in Godot 4. It is designed as a broad first-pass library that can be curated and rearranged manually in the Godot editor.

## Requirements

- Blender 4.x installed
- No pip packages required
- Run commands from the repository root

## Generate assets

Generate 10 of each supported category:

```bash
blender --background --python tools/asset_generation/generate_space_hippie_asset_factory.py -- --category all --count 10 --seed 100
```

Generate larger batches:

```bash
blender --background --python tools/asset_generation/generate_space_hippie_asset_factory.py -- --category buildings --count 40 --seed 2026
blender --background --python tools/asset_generation/generate_space_hippie_asset_factory.py -- --category vehicles --count 25 --seed 42
blender --background --python tools/asset_generation/generate_space_hippie_asset_factory.py -- --category street --count 80 --seed 77
blender --background --python tools/asset_generation/generate_space_hippie_asset_factory.py -- --category npcs --count 40 --seed 11
```

Categories:
- `buildings`: varied building massing, window layouts, facade details, rooftop equipment, and accent lighting.
- `vehicles`: civilian hovercars, taxis, cargo vehicles, patrol cars, scrap vehicles, and shuttles.
- `street`: kiosks, vending machines, market stalls, benches, lamps, signs, barriers, vents, generators, antennas, trash/junk piles, charging pillars, bollards, crates, and drone docks.
- `npcs`: stylized humans, aliens, and robots with randomized proportions, outfits, skin tones, alien heads/features, accessories, and colors.

## Output folders

```
assets/3d/generated/
  buildings/
  vehicles/
  street/
  npcs/
```

Every output is an individual GLB. Import the folders into Godot and curate models by previewing them. The seed is included in each filename. A different seed generates a different batch; the same seed and settings are intended to reproduce the same batch. Running the same seed and category again overwrites that batch, so keep favorites in a separate curated folder or use a new seed.

## Important limitations

- These are procedural low-poly drafts, not finished art. Inspect silhouettes, proportions, shading, and scale before shipping.
- NPCs are static pose meshes and are **not rigged or animated**. They are useful as placeholders, crowd silhouettes, or visual targets. Rigging and animation should be a separate next step.
- This generator focuses on reusable props and asset variety; it does not automatically place assets into the city or make vehicles/NPCs interactive.
- Large asset counts should be curated. Hundreds of exports do not guarantee hundreds of good or visually distinct models.
