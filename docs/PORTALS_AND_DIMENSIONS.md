# Portals and Alternate Dimensions

## Narrative premise
A municipal energy project at Pumpworks exposed a boundary between adjacent physical spaces. The breach is not a magic doorway with a known creator. It behaves like a place where different environments overlap. The town has rationalized the event through budget language, weather reports, and paperwork.

## Portal visual design
A vertical tear held inside a ring of repurposed industrial braces. Liquid-glass surface, subtle refraction, suspended dust, a harmonic tone that changes slightly with player proximity. Nearby shadows occasionally point a few degrees in the wrong direction. Keep the effect readable and performant; it must not obscure interaction or turn the portal into a giant particle effect.

## Travel contract
1. Player approaches the portal and receives an interaction prompt.
2. System validates destination and checks for transition-blocking state.
3. If needed, show a concise warning (for example, active delivery or unsold cargo).
4. Save a transition snapshot: source world, return anchor, inventory, mission state, player equipment.
5. Fade or stylized distortion; prevent duplicate activation.
6. Load destination and place player at a safe arrival marker.
7. Validate ground/collision, restore UI, and set current world.
8. Return portal reverses the flow. If loading fails, restore source snapshot without losing items.

Do not attempt seamless world streaming in the first version. Do not carry vehicle physics across worlds; the vehicle remains in the town at a safe persisted transform.

## Dimension 1 — The Bloom
**Theme:** luminous ecology around a mineral fracture.  
**Emotional sequence:** wonder → curiosity → mild unease → small risk → relief at return.  
**Silhouette language:** oversized petals, branching root bridges, tall faceted crystals, suspended mineral shards.  
**Palette:** indigo/petrol, mint/lime, amber, small coral accents.  
**Audio:** glassy resonance, soft organic pulses, distant wind that seems to move against the plants.

### Resource types
- **Lumen Pod:** common, visible at a distance, low risk. Pulses gently before collection.
- **Resonant Shard:** mineral resource near a slow hazard field; moderate value.
- **Odd Spore:** uncommon specimen, often found in shaded root pockets; research value.
- **First Bloom Specimen:** one optional rare item, high value but guarded by a clear environmental warning.

### Hazard language
Hazards telegraph through a consistent sequence: visual precursor → audio cue → active window → cooldown. The first hazard is a slow resonance wave that changes the glow pattern along the ground. It should be avoidable by waiting or taking a short alternate path. Do not require frame-perfect dodging.

### Return safety
The return arch is visible from the entry shelf and identifiable elsewhere by its warm amber edge light and familiar harmonic. The player can always retreat without completing every collectible objective.

## Future dimension concepts (backlog)
### The Hush
A wide, pale forest where sound arrives before its source. Gameplay hook: follow audio echoes to reveal safe routes. Palette: bone white, faded lavender, cold cyan. Mood: quiet, lonely, not horror by default.
### The Tilt
A canyon where gravity vectors lean around mineral spires. Gameplay hook: small local gravity changes and alternate paths, not free-flight simulation. Palette: rust, black glass, bright cobalt.
### The Aftergarden
An overgrown architectural space where alien plants mimic familiar town objects. Gameplay hook: identify false landmarks and recover artifacts. Palette: muted peach, deep green, electric pink accents.
### The Static Sea
A flat mineral plain with distant structures that appear only at certain resonance states. Gameplay hook: activate repeatable environmental signals to reveal paths. This is a late expansion concept.

Each dimension must have a distinct navigation grammar, resource family, hazard language, and emotional tone. Do not build multiple dimensions until The Bloom is fun, stable, and visually approved.
