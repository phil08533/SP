# Missions, Progression, and Content Blueprint

## Mission design contract
Every mission must have: premise, giver, starting conditions, primary objective, optional objective, clear completion feedback, reward, consequence, failure/recovery path, save/load behavior, and reusable system dependencies. Missions should combine systems rather than introduce a unique mechanic for every story beat.

## First mission — A Small Favor
**Purpose:** teach driving, navigation, interaction, portal discovery, gathering, inventory, risk, sale/crafting, and spending in a single connected arc.
**Giver:** Mara Venn.
**Premise:** move a sealed service case to Pumpworks. It reacts to the portal.
**Primary path:** accept case → drive to gate → discover the breach → enter The Bloom → collect three Lumen Pods → return → deliver pods or process/sell → collect reward.
**Optional:** retrieve a rare specimen from the nook; take the Drain Cut route; cooperate with Officer Vale if noticed.
**Reward:** enough combined job/resource income to approach the first 40-credit storage upgrade; tune after playtest.
**Failure recovery:** if player abandons the case or leaves the area, Mara remains available; the objective can be restarted or resumed. Do not delete collected resources or strand the player in a dimension.
**State flags:** accepted, reached_pumpworks, portal_discovered, entered_bloom, pods_collected, returned, sale_or_processing_complete, mission_complete, optional_specimen_found.
**System coverage:** dialogue, vehicle, interaction, portal, resource nodes, inventory, economy, suspicion, save/load.

## Follow-up missions (backlog, not first-slice commitments)
### 2. “The Invoice That Wasn't”
Mara asks the player to locate a service invoice that appears in two places with different dates. Explore garage shelves and an abandoned office; reward is a repair discount and a Pumpworks access hint. Introduces inspect/evidence without combat.

### 3. “Weather Advisory”
Jo Sable needs a delivery made during a strange local “weather event.” The road is clear, but visibility and sound behave oddly near the relay mast. Choice: take the fast road or safe back trail. Reward: money and a relationship flag with Jo.

### 4. “A Fair Price”
Rook Calder offers to buy Glow Resin. The player can sell immediately, compare with Sera's research offer, or decline. The mission teaches that legal status and price are separate from moral labels; no option should be secretly mandatory.

### 5. “Keep the Gate Closed”
Officer Vale asks the player to inspect a sensor line around Pumpworks. Find signs of trespass and decide whether to report a broker's involvement, omit it, or ask for more evidence. Outcomes shift trust with Vale and Calder's Exchange, but do not lock the entire game into one route.

### 6. “Three Notes in the Static”
Finch asks the player to visit three locations when the relay mast emits a repeating pattern. This is an exploration mission with visual/audio clues, not a pixel-hunt. Reward: a new portal signature and a future dimension lead.

## Progression tiers
### Tier 0 — New Arrival
Basic vehicle, tiny inventory, hideout storage, one contact. Access to legal odd jobs and first portal.
### Tier 1 — Known Face
Earned through completing first mission and one optional job. Unlock storage crate, basic repairs, and a second buyer.
### Tier 2 — Trusted Operator
Earned through repeated jobs and one meaningful relationship. Unlock specialized collection tool and a rough-route vehicle upgrade.
### Tier 3 — Local Power
Future release tier: larger hideout capacity, multiple supply contacts, more complex jobs and reputation tradeoffs. Not required for the first slice.

## Meaningful upgrades
- **Storage crate:** expands capacity and changes hideout dressing.
- **Insulated gloves:** permit a small class of hazardous specimen pickups.
- **Suspension kit:** opens rough trails and improves vehicle recovery.
- **Portal scanner:** gives advance warning of hazard timing.
- **Workbench upgrade:** improves fictional processing yield or reduces station time.
Each upgrade changes an available action, route, risk, or visible environment; avoid upgrades that only add tiny percentage bonuses.

## Mission state and anti-softlock rules
- Mission rewards are idempotent.
- Required objects have recovery/fallback states.
- Mission-critical NPCs cannot permanently disappear due to routine schedules.
- Portal transition cannot erase active objectives.
- Optional choices are genuinely optional and don't silently invalidate the main path.
- Failure feedback states what happened and how to resume.
