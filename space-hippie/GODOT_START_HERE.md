# Godot Starter — Dusty Junction

This is a first editable environment blockout for the Space Hippie Godot trial. It uses native Godot mesh nodes so you can select and reposition the main pieces in the editor. It is deliberately a blockout, not final art.

## Open the Godot project

Open the **space-hippie/** folder in Godot, not the repository root. The Godot project file is `space-hippie/project.godot`.

## Get the generated models into the Godot project

The six original GLB exports are stored at the repository root under `assets/3d/dusty_junction/`.

From the repository root, copy them into `space-hippie/assets/models/dusty_junction/`. Create the destination folder if it does not exist. Copy, do not move, the originals. In Godot, wait for the FileSystem import to finish. The current blockout intentionally does not depend on these files yet, so the scene can run before the models are copied.

## Edit the blockout

Open `scenes/worlds/dusty_junction.tscn`. Expand the scene tree and select named groups such as `Motel`, `MaraGarage`, `Diner`, `TradeCounter`, `Pumpworks`, and `DesertRocks`. Use the Move (W), Rotate (E), and Scale (R) tools in the 3D viewport. Save with Ctrl+S.

The camera is an overview camera for the initial map layout, not a player camera. The buildings are simple primitive meshes that can be replaced piece by piece with the generated GLB props.

## Important

- This blockout is a visual layout only: no player controller, collision, missions, or vehicle are implemented yet.
- The map is intentionally compact for fast iteration.
- Commit changes in Git as you go. Keep the existing Three.js/pre-production work intact until the Godot trial has been evaluated.
