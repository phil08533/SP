# Initial Asset and Concept Catalog

This is a production-planning list, not an instruction to generate everything immediately. Build greybox first, then approve a tiny visual anchor set.

**Tracking:** Use [Asset Manifest (CSV)](ASSET_MANIFEST.csv) to track each candidate's stable ID, source/provenance, rights, technical requirements, and review state. The catalog describes what may be needed; it is not a request to generate every listed asset.

## Style anchor set — required before scale-up
1. **ENV_Town_Garage_A:** Mara's two-bay garage exterior with one readable sign and repair clutter.
2. **CHR_MaraVenn:** full-body stylized character with clear silhouette and one interaction idle.
3. **VEH_StarterCompact_A:** battered compact vehicle with exaggerated lamps and clear wheel placement.
4. **PROP_PortalBrace_A:** modular industrial ring brace and portal surface.
5. **FLORA_LumenPod_A:** luminous plant with a readable pickup state.
6. **ENV_Bloom_Crystal_A:** faceted crystal with controlled emissive material.
7. **PROP_StorageCrate_A:** hideout upgrade prop.
8. **CHR_Player_Base:** neutral player rig/proxy to validate scale, animation, and camera.

## Town modular kit
- storefront shell (small, medium, corner);
- garage bay and service door;
- motel room module and office window;
- Pumpworks shed, fence, gate, warning signage;
- utility poles, cable runs, street lamps;
- road edges, curb segments, parking markings;
- roadside sign frames and interchangeable sign faces;
- junk piles, tire stacks, vehicle shells, salvage racks;
- diner canopy, counter, booth, kitchen pass-through;
- hideout bed, fridge, map board, workbench, storage crate.

## Dimension kit
- Lumen Pod plant (idle, ready, depleted states);
- small/medium/large crystal formations;
- root bridge segments and root arch;
- mineral pool rim and hazard marker;
- suspended shards;
- return arch;
- rare specimen cluster;
- ground/path tiles with controlled variation.

## Character list by priority
**Slice:** player, Mara Venn, Officer Imani Vale, and at most one ambient resident for the initial slice. Finch Rill is a near-term candidate only if the approved mission needs him.  
**Near-term:** Finch Rill, Jo Sable, Rook Calder, Tamsin Pike, Bex and Boro.  
**Later:** Dr. Sera Quill (can initially appear via notes/audio), Nell-7, Quiet Customer.

## Vehicle and prop priority
Slice vehicle: one compact road car. Required props: sealed case, processing bench, trade counter, storage crate, warning sign, portal brace/return arch, Lumen Pod resource. Resource basket, patrol marker, repair tool set, and survey tag are candidates only if they communicate required gameplay or help the player read the scene.

## Asset metadata record
Every imported asset should have:
- stable asset ID and descriptive name;
- source file and creator/tool;
- license and commercial-use confirmation;
- scale/pivot convention;
- material/texture list;
- collision setup;
- rig/animation requirements;
- expected memory and rendering cost;
- import settings and known defects;
- review status (greybox, candidate, approved, rejected).

## Visual review checklist
- Is the silhouette readable at gameplay distance?
- Does it use the approved palette and material language?
- Does its scale match the reference mannequin?
- Is the topology/normals/material setup sound?
- Is collision simpler than render geometry where possible?
- Does it need a rig, LOD, or reduced texture size?
- Is commercial use permitted and documented?
- Does it create more cleanup work than a modular/procedural alternative?
- Does it work under town and dimension lighting, not just a beauty render?
