# Player Flow and Interaction UX Specification

**Status:** Proposed pre-production specification; engine-neutral.

## Purpose

Reduce implementation guesswork by defining what the player should understand and what every core interaction must communicate. This is not a final UI mockup and does not select an engine.

## First-session flow

1. **Hideout:** Player learns movement, camera, interact, inventory, and job objective. Mara Venn provides the sealed service case.
2. **Vehicle:** Player can approach, enter, drive, stop, exit, and recover if stuck. The route to Pumpworks is visually legible without a map marker being the only clue.
3. **Pumpworks public drop:** Player sees the legal delivery point, delivers the case once, and receives clear confirmation.
4. **Restricted inner boundary:** Boundary markings, signage, and environmental cues signal that the inner area is restricted before crossing. The first warning must not block the required portal interaction.
5. **The Bloom:** A distinct visual/audio transition communicates arrival. The player sees the exit portal and a safe return route before being encouraged to explore.
6. **Resource collection:** Lumen Pods have a readable silhouette and pickup affordance. The UI confirms item name, quantity, and inventory/capacity result.
7. **Return and payout:** The player can return even if they collect fewer than three pods. Mission state persists; Mara pays the full courier fee after the return condition is met.
8. **Choice:** The hideout workbench explains the three-pod recipe and gross value before processing. The trade counter shows item quantities and proceeds before confirming a sale.
9. **Upgrade:** The storage upgrade clearly shows cost, effect, and whether the player can afford it.

## Interaction contract

Every interactable should define:
- Stable ID and interaction type.
- Range and line-of-sight policy.
- Prompt text and available action.
- Preconditions (distance, mission state, inventory, capacity, ownership).
- Success feedback.
- Failure feedback with a reason.
- Whether repeated activation is safe.
- Whether state persists through save/load.

No required progression should depend on tiny text, color alone, or a single hidden pixel-perfect interaction point.

## Input principles

- Keyboard/mouse and controller use the same action map and gameplay rules.
- Prompts adapt to the active input device without changing action semantics.
- Core actions should be remappable where the chosen engine permits practical support.
- UI focus must not cause gameplay actions to fire behind menus.
- Hold/tap behavior must be consistent and explained; avoid using long holds for routine interactions.
- Never require simultaneous keyboard and controller input.

**Bindings are intentionally not finalized** until the engine/input abstraction is tested. Keep action names semantic (Interact, Confirm, Cancel, Inventory, Map, VehicleEnterExit, Brake/Reverse) rather than hard-coding a key into gameplay logic.

## Feedback rules

- Mission state changes produce a short objective update and a world-facing cue where practical.
- Pickups show the exact quantity gained or explain why collection failed.
- Currency changes show source and amount.
- Restricted-area warnings explain the boundary crossed and immediate consequence.
- Suspicion warnings identify the witnessed behavior when safe to do so.
- Portal transitions have an unmistakable sound/visual cue and preserve player orientation enough to avoid disorientation.
- Critical warnings use text/icon/shape plus color, never color alone.

## Accessibility baseline

- Subtitles for spoken dialogue and important voiced cues.
- Adjustable dialogue/subtitle text size where feasible.
- Separate dialogue, ambience, effects, and music volume controls.
- Avoid mandatory rapid button mashing or timing-only progression in the first slice.
- Do not encode essential clues solely through audio, color, or fine visual detail.
- Test legibility at normal gameplay camera distance and on a typical 1080p display.

## Edge cases that must have designed outcomes

| Situation | Expected behavior |
|---|---|
| Player has full inventory | Explain capacity; do not delete or silently replace items |
| Player leaves mid-mission | Preserve active mission and allow resumption |
| Player returns with fewer than three pods | Keep mission resumable; don't strand or invalidate the courier job |
| Player interacts repeatedly with a pickup | Grant the item once per resource node |
| Player tries to process with insufficient inputs | Explain missing quantity; no inventory changes |
| Player tries to buy an unaffordable upgrade | Show shortfall; no partial charge |
| Player exits vehicle during a mission | Mission remains completable on foot |
| Portal transition fails | Preserve inventory and mission state; recover to source side |
| Player is warned for trespass | Keep required opening interaction possible |
| Player sells items then saves/reloads | Sale and currency change remain exactly once |

## Acceptance checklist

- [ ] Each required first-slice interaction has a prompt, preconditions, success feedback, and failure feedback.
- [ ] Every required objective is understandable without relying on a map marker alone.
- [ ] Keyboard/mouse and controller can complete the same full mission.
- [ ] Every listed edge case has a test case.
- [ ] No color-only information communicates a critical state.
- [ ] UI focus and repeated activation cannot duplicate rewards or trigger actions behind menus.
