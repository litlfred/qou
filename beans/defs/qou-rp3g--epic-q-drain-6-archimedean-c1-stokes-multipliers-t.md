---
# qou-rp3g
title: 'EPIC [Q-Drain-6]: Archimedean / C1 Stokes Multipliers, theta_K Channel & Hyperbolic Volume Bridges'
status: in-progress
type: epic
priority: high
created_at: 2026-11-23T20:55:48Z
updated_at: 2026-11-24T03:03:20Z
parent: qou-hksc
blocking:
    - qou-xip2
---

**Theme:** Archimedean / C1 Stokes Multipliers, theta_K Channel & Hyperbolic Volume Bridges
**Rationale:** Defines theta_K off-lattice, discharges numerical-only C1 Stokes/theta connection results in Lean, and connects 3-manifold triangulation volume.
**Child Beans (13):** `qou-8vt2`, `qou-offl`, `qou-c1ln`, `qou-odh5`, `qou-wgnx`, `qou-qbe9x`, `qou-vr3q`, `qou-3ent`, `qou-vdvE`, `qou-8mtd`, `qou-eptr`, `qou-slpd`, `qou-slvl`

### Prioritized Beans in This Batch
- **`qou-8vt2`** (`critical`, `todo`) — DEFINE ϑ_K: the channel has no definition for it, only a docstring phrase *(Rule 13a: 0-instance classes: `SDeformedVolumeChannel`)*
- **`qou-offl`** (`high`, `in-progress`) — Route 1 (parent: qnnq): off-lattice ϑ_K = cone-manifold / generalized-Dehn-filling deformation. Non-integer (m,ℓ) is standard geometry: Thurston generalized Dehn surgery coefficients ∈ ℝ², Hodgson–Kerckhoff cone-manifold rigidity, Gukov/Murakami generalized volume conjecture (continuous parameter u off the complete structure). Probe: fit probed ϑ values (4₁: proton 0.203, muon 0.059) to real filling coefficients on the NZ volume function; Lean: conditional NZ dVol/du statement. *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-c1ln`** (`high`, `todo`) — LEAN: discharge the C1 connection results that are only numerical
- **`qou-odh5`** (`high`, `in-progress`) — C1 infinity: extract the TWO Stokes multipliers via q-Borel/theta resummation (leading blocks now known)
- **`qou-wgnx`** (`high`, `in-progress`) — GAP: theta-normalised canonical solutions for C1 — the genuine untried route to the Stokes multipliers
- **`qou-qbe9x`** (`high`, `in-progress`) — Geometry gap: C1 has a THIRD singular site at x = q^-2 (orbit [1] on E_q) that no analysis has examined
- **`qou-vr3q`** (`high`, `todo`) — Deep-dive 1: G3 monodromy/Stokes-constant keystone — derive A_ω (odd-face Q_β/Φ_b) as GGM 3d-index integer count *(Rule 13a: 0-instance classes: `FaddeevPhi, FaddeevPhiPhysical`)*
- **`qou-3ent`** (`high`, `in-progress`) — CORRECTION: A_omega = 3 is the OFF-DIAGONAL Stokes constant, NOT a 3d-index coefficient — eq (21) is diagonal-only *(Rule 13a: 0-instance classes: `StokesDTBPSBridge`)*
- **`qou-vdvE`** (`high`, `in-progress`) — Bridge step 2: test van der Veen E against |tau_DG|^{-1/2} — the Gukov-Murakami conjecture, for links *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-8mtd`** (`high`, `in-progress`) — Define the volume of a topological 3-manifold and connect it to the triangulation volume *(Rule 13a: 0-instance classes: `HyperbolicVolumeBridge`; Rule 13a `stays open`/conjecture guard)*
- **`qou-eptr`** (`high`, `todo`) — EP/canonical decomposition as the non-pair-local extensive carrier for b_3 — aim, and the hard blocker at the light end *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-slpd`** (`high`, `todo`) — ROAST: slope ½ is a definition, not a derivation — and the two ½s are order vs level
- **`qou-slvl`** (`medium`, `in-progress`) — slope = q-Gevrey level in general; and the two recursions still defined-to-match

### Worker Protocol
- Claim individual child beans via `beans update <bean-id> --status in-progress --body-append "Claimed by <branch> (YYYY-MM-DD)"`.
- Never mark a bean `completed` while an uninstantiated conjecture `class` or explicit `stays open` item remains (AGENTS.md Rule 13a).
- Enforce single-thread CPU caps (`LEAN_NUM_THREADS=1`, `nice -n 15`), zero float64 (`mpmath` >= 50-80 dps), and zero fitting.

Batch 6 Q-Drain-6 complete on origin/claude/backlog-drain-batch6-20261123 (5d406fc68a3): C1ConnectionAlgebraicIdentities.lean (42 decls, 0 sorry) + StokesDTBPSBridge fix staged.
