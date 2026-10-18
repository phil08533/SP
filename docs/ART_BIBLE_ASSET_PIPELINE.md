# Art Bible and Asset Pipeline

## Visual thesis
**Roadside Americana after the universe developed a strange leak.** The town is practical, sun-faded, tactile, and a little shabby. The dimension is organic, luminous, and quietly impossible. Both share chunky silhouettes, deliberate color grouping, stylized materials, and retro-futurist details.

## Shape language
- **Town:** rectangular shells softened by rounded corners, exaggerated rooflines, chunky utility hardware, visible repairs and improvised add-ons.
- **Vehicles:** compact boxy bodies, readable wheel placement, bold bumpers and oversized lamps; limited tiny trim.
- **Characters:** clear head/torso/limb separation, readable gameplay silhouettes, expressive posture, restrained micro-detail.
- **Dimension:** large organic arcs, faceted crystals, root bridges, layered petals, asymmetrical growth. Avoid random noisy forms.
- **Crime props:** improvised, repaired, repurposed; avoid generic tactical gear.

## Palette
**Town:** dust ochre, faded teal, warm concrete, oxidized red, smoky violet, deep asphalt blue. Selective saturation belongs to signs, shop accents, and anomalous effects.
**The Bloom:** indigo/petrol shadows, mint and lime bioluminescence, amber mineral cores, small coral accents. Preserve dark negative space so luminous forms matter.
**UI:** near-black blue-gray panels, warm off-white text, muted teal focus, amber warnings, restrained violet for dimension data. Critical states cannot be communicated by color alone.

## Materials and lighting
Controlled material vocabulary: painted metal, dusty plastic, faded fabric, rough concrete, glass, rubber, alien translucent/bioluminescent surface, mineral crystal. Value and roughness do more work than tiny textures. Avoid glossy-everything, noisy grunge, or physically realistic materials that clash with stylization.

Town: broad warm key light, cool ambient fill, local practicals, selective fog, portal light as accent. The Bloom can be theatrical but must preserve silhouette and route readability. Do not make expensive rendering features mandatory until the Linux hardware test proves them viable.

## Camera and proportions
Provisional third-person target: player occupies roughly 8–15% of screen height during normal traversal. Important props must read at gameplay distance. A human reference mannequin is approximately 1.7–1.9 m tall; confirm unit conventions after engine choice. Doors and vehicle dimensions should read believably against this scale.

## Asset quality bar
Review every asset for silhouette/style, scale and pivot, topology/normals, material assignment, texture size, collision proxy, LOD/visibility strategy, rig/animation needs, license/provenance, memory/draw/shader cost, import and packaging behavior. AI-generated models are starting points, not automatically production-ready. Reject assets whose cleanup cost exceeds a modular/procedural alternative.

## Pipeline
1. Greybox layout with primitives.
2. Approve a tiny reference set: one building, one character, one vehicle, three props, one plant, one crystal.
3. Test in-engine under target camera and lighting.
4. Revise proportions, materials, palette, and complexity.
5. Document export/import presets, scale, naming, collision, and material rules.
6. Expand only after style anchors are approved.
7. Profile representative scenes and check for visual consistency.

## Formats and naming
Exact formats follow engine choice. Candidate interchange formats include glTF/GLB or FBX for meshes/rigs, PNG/TGA for textures, WAV/OGG for audio, subject to importer tests and licenses. Keep editable source assets outside engine caches. Naming examples: `ENV_Town_Garage_A`, `CHR_MaraVenn`, `VEH_StarterCompact_A`, `PROP_PortalBrace_A`, `MAT_PaintedMetal_Teal`.

## Animation priorities
Idle weight shifts, walk/run, turn, interact/pickup, enter/exit vehicle, talk, startled reaction. A limited first-slice set is acceptable, but the player should not feel like a mannequin. Wheel/suspension movement should sell vehicle weight; NPC idle timing should vary.

## Sound identity
Town: wind through cables, electrical buzz, distant engines, sign transformer, muffled diner chatter. Dimension: resonant plants, glassy mineral tones, soft pulses, spatial ambience. Portal audio should be recognizable at distance. UI and warnings must not overpower dialogue.

## Performance budgets
Numeric frame-time and memory budgets are deliberately unset until the first engine benchmark. Prioritize smooth play on the actual development PC, simple collision, reused materials, modest NPC counts, scalable settings, and avoiding unique high-resolution textures for every prop. No mandatory ray tracing or high-cost rendering feature without evidence.

## Reference principles
Study readability and composition in stylized open-world games, chunky low-poly silhouettes, retro roadside architecture, analog sci-fi interfaces, and psychedelic botanical illustration. References are for principles, not copying protected characters, logos, exact environments, or distinctive assets.
