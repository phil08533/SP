# Save Data and Recovery Specification

**Status:** Logical requirements only. No serialization format, engine subsystem, or implementation is selected.

## Goal

Define what a save must preserve before implementation begins. A save is successful only if the player can continue the mission and economy without duplicated rewards, lost inventory, or impossible world states.

## Minimum logical save contents

### Profile
- Save schema version.
- Stable player/profile identifier generated locally.
- Save timestamp and game build/version identifier.
- Last known safe spawn/respawn location.

### Player state
- Position, rotation, movement mode, and health/status fields only if those systems exist in the approved slice.
- Currency.
- Inventory item IDs and quantities.
- Inventory/storage capacity and purchased upgrades.
- Current equipped/selected items if relevant.

### Progression
- Active mission ID and stage ID.
- Completed mission IDs.
- Objective flags needed to resume an interrupted mission.
- One-time reward-claim flags.
- Unlocked recipes/upgrades and persistent tutorial acknowledgements.

### World state
- Resource-node depletion or regeneration state.
- Persistent interactable states that affect progression.
- Vehicle stable ID, last valid transform, ownership/availability, and recovery state.
- Relevant suspicion/law state only if the design intends it to persist between sessions.
- Portal/dimension return anchor or other data required to recover safely.

Do not save transient presentation state such as particles, temporary UI notifications, or cosmetic animation frames unless a later requirement proves it necessary.

## Stable identifiers and migrations

- Items, recipes, missions, upgrades, resource nodes, vehicles, and persistent interactables use stable IDs, not display names or array positions.
- Renaming a display label must not invalidate a save.
- Missing/unknown IDs must be handled safely and logged for diagnosis.
- Schema changes require an explicit version increment and a migration or documented safe rejection strategy.
- Never silently reinterpret an old field with a different meaning.

## Save timing and transaction boundaries

Save at deliberate checkpoints such as mission-stage changes, confirmed transactions, crafting completion, upgrade purchase, and safe portal return. Exact timing and frequency depend on engine and design tests.

Treat economy actions as atomic transactions:
- Sale: validate inventory and price, remove items, grant currency, then commit one consistent state.
- Crafting: validate recipe/inputs/capacity, consume inputs, produce output, then commit one consistent state.
- Purchase: validate funds and eligibility, deduct cost, apply upgrade, then commit one consistent state.
- Reward: mark the reward as claimed in the same logical transaction that grants it.

A crash must not leave both the input and output of a craft, duplicate a payout, or charge for an upgrade that was not applied.

## Failure and recovery policy

| Failure | Required behavior |
|---|---|
| Player requests save in an invalid/transient state | Defer until a safe state or explain why saving is unavailable |
| Save interrupted while writing | Preserve the last known-good save |
| Save file corrupt or incomplete | Do not silently overwrite it; report the issue and offer a safe fallback if available |
| Unknown future schema version | Do not destructively downgrade it |
| Missing optional asset/content ID | Load a safe fallback or skip nonessential content with a diagnostic |
| Missing critical mission/item ID | Fail safely with a clear diagnostic; do not invent progression |
| Player/vehicle transform inside geometry | Recover to a validated nearby safe point |
| Portal transition interrupted | Load at a valid source or destination anchor, never in an invalid transition state |
| Reward action retried | Stable transaction/claim state prevents duplicate payout |
| No valid save exists | Offer a new game without deleting unrelated files |

## Slot and backup policy

The first slice needs only a simple local save policy. Multiple slots, cloud sync, cross-device transfer, and mod compatibility are not required. Keep the last known-good save separate from an in-progress write where practical. Never require a network connection to load a save.

## Acceptance tests

- [ ] Save and reload at every opening mission stage.
- [ ] Save with a partial Lumen Pod collection and resume correctly.
- [ ] Complete courier payout, save/reload, and verify the payout occurs exactly once.
- [ ] Craft Glow Resin, save/reload, and verify inputs/output/currency are consistent.
- [ ] Purchase storage upgrade, save/reload, and verify cost/effect occur exactly once.
- [ ] Deplete a resource node, save/reload, and verify it cannot be harvested twice.
- [ ] Simulate invalid player/vehicle position and verify safe recovery.
- [ ] Verify a corrupt or interrupted save does not overwrite the last known-good state.
- [ ] Verify unsupported schema versions are not silently modified.
- [ ] Confirm the game can start and load local saves offline.

## Decisions intentionally deferred

- File format and serialization library.
- Autosave frequency and user-facing save indicator.
- Number of save slots.
- Whether suspicion state persists across sessions.
- Whether vehicle state saves exactly or respawns at a safe recovery point.

Resolve these only after engine selection and a small save/load prototype.
