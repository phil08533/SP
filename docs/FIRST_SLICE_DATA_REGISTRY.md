# First-Slice Data and Rule Registry

**Status:** Proposed canonical design registry for the first playable slice. Values and behaviors marked provisional require playtesting; this file does not authorize production implementation.
**Purpose:** Reduce drift between mission, systems, UI, save/load, and AI-generated code. Once the engine is approved, implementation data should be sourced from one data-driven definition where practical rather than duplicated as literals across scripts.

## 1. Item registry

| Stable ID | Display name | Category | Stack / role | Base value | Sale rule | Notes |
|---|---|---|---|---:|---|---|
| `item.lumen_pod` | Lumen Pod | Alien botanical | Stackable resource | 5 credits each | Trade counter buys | Common, low hazard; first resource |
| `item.glow_resin` | Glow Resin | Processed fictional good | Stackable processed good | 24 credits each | Trade counter buys; restricted status | Crafted from three Lumen Pods; carrying openly near witnesses can raise suspicion |
| `item.resonant_shard` | Resonant Shard | Mineral resource | Future resource | TBD | TBD | Not required for first mission |
| `item.odd_spore` | Odd Spore | Organic specimen | Future resource | TBD | TBD | Not required for first mission |
| `item.first_bloom_specimen` | First Bloom Specimen | Optional rare specimen | Unique/stack policy TBD | 20 credits (placeholder) | Research buyer only if included | Optional; never required to complete first slice |
| `item.sealed_service_case` | Sealed service case | Mission item | Unique mission item | Not for sale | Not sellable | Ordinary pump component; deliver to public-facing Pumpworks drop |
| `item.survey_tag` | Survey Tag | Mission item | Unique mission item | Not for sale | Not sellable | Include only if the approved objective needs it |

## 2. Recipe and economy registry

| Stable ID | Inputs | Output / effect | Cost/value | Status |
|---|---|---|---:|---|
| `recipe.glow_resin` | 3 × `item.lumen_pod` | 1 × `item.glow_resin` | 24 credits gross sale value | Provisional; test actual value and any fees |
| `job.small_favor` | Complete courier delivery, enter The Bloom, return to Dusty Junction, claim at Mara | Courier payout | 25 credits, once | Provisional |
| `upgrade.storage_crate_01` | Currency | Increased storage capacity | 40 credits | Provisional |
| `service.vehicle_repair_basic` | Currency | Restore basic vehicle condition if condition exists in slice | 15 credits | Out of required loop unless needed for recovery |
| `sale.first_bloom_specimen` | 1 × `item.first_bloom_specimen` | Currency | 20 credits | Optional and not required |

**Arithmetic check:** Three raw Lumen Pods sell for 15 credits. Courier payout plus raw sale is 40 credits before fees or penalties. Processing three pods produces one Glow Resin worth 24 credits gross, for 49 total with the courier payout. These are gross placeholder values, not tested balance. The rare specimen is not necessary to afford the first storage upgrade.

## 3. Mission registry

Mission ID: `mission.a_small_favor`

| Stage ID | Entry condition | Required action | Persistent result | Recovery |
|---|---|---|---|---|
| `stage.accept_job` | Mission not active | Accept from Mara | Mission active; case available | Re-interact with Mara if case is not carried |
| `stage.deliver_case` | Case carried | Deliver to public-facing Pumpworks drop | Case remains at drop; delivery flag set | Do not require carrying case into The Bloom |
| `stage.discover_portal` | Case delivered / anomaly revealed | Investigate portal | Portal discovered | Portal remains discoverable |
| `stage.enter_bloom` | Portal usable | Enter The Bloom | Current world and return anchor saved | Failed transition restores source state |
| `stage.collect_pods` | In The Bloom | Collect up to three Lumen Pods for primary objective | Collected count and node depletion persist | Return is always allowed; partial progress persists |
| `stage.return_town` | Return portal usable | Return to Dusty Junction | Return condition set | Safe spawn on source side |
| `stage.claim_courier_fee` | Returned and job eligible | Claim from Mara | 25-credit reward claimed exactly once | Re-interaction reports already claimed |
| `stage.choose_resource_path` | Has pods or has returned | Sell raw pods or process at hideout workbench | Transaction state committed | No duplicate items/currency on repeat |
| `stage.purchase_upgrade` | At least 40 credits and upgrade not owned | Buy storage upgrade | Currency deducted and upgrade applied once | Failed purchase changes nothing |
| `stage.complete` | Required objectives complete | Confirm completion | Mission completed | Save/load retains completion |

The courier fee is tied to delivering the sealed case and returning to Dusty Junction, not to the number of pods collected. If the player returns with fewer than three pods, Mara can pay the full 25-credit courier fee once; the resource objective remains active and resumable until three pods have been collected. The player may re-enter The Bloom to finish it. This separates payment for the courier job from the optional timing of resource collection. Do not add a partial payout or abandonment penalty to this slice.

## 4. Crime and witness event IDs

| Event ID | Trigger | First-slice response | Guardrail |
|---|---|---|---|
| `crime.pumpworks_inner_trespass` | Cross marked restricted inner boundary | One clear warning/tutorial beat on first encounter; later response can be a fine | Must never block required portal interaction or soft-lock mission |
| `crime.expose_glow_resin` | Restricted Glow Resin is carried openly within defined witness detection conditions | Suspicion may rise | Define witness distance/visibility and cooldown before implementation; don't make suspicion random or opaque |
| `crime.optional_rare_specimen` | Player acquires optional specimen | No automatic crime unless a separate rule is explicitly approved | Optional content must not create an unavoidable penalty |

## 5. Stable world and content IDs

- `world.dusty_junction`
- `world.the_bloom`
- `location.hideout`
- `location.pumpworks_public_drop`
- `location.pumpworks_inner_boundary`
- `location.bloom_entry_shelf`
- `location.bloom_return_arch`
- `npc.mara_venn`
- `npc.officer_imani_vale`
- `vehicle.starter_compact`
- `resource.bloom_lumen_pod_01` (unique suffix for each resource node)
- `interactable.hideout_workbench`
- `interactable.trade_counter`
- `interactable.storage_crate`

These are proposed stable identifiers. They should be validated for uniqueness and used consistently once implementation is approved; player-facing labels can change without changing IDs.

## 6. Registry change rules

1. If a price, recipe, mission stage, or trigger changes, update this registry first and record the reason.
2. Update explanatory design documents in the same change when their prose becomes stale.
3. Do not duplicate tunable values as independent constants across systems.
4. Add a migration/test note if a change affects saved progression.
5. Mark values as **provisional** until playtested; documentation agreement is not balance validation.
6. Do not implement optional content solely because an ID appears in this registry.
