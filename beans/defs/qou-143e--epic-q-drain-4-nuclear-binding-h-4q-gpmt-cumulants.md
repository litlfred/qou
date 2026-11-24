---
# qou-143e
title: 'EPIC [Q-Drain-4]: Nuclear Binding, H_4(q) GPMT Cumulants & 3D alpha-Simplex Compute/Lean'
status: in-progress
type: epic
priority: high
created_at: 2026-11-23T20:55:47Z
updated_at: 2026-11-24T02:28:18Z
parent: qou-hksc
blocking:
    - qou-xip2
---

**Theme:** Nuclear Binding, H_4(q) GPMT Cumulants & 3D alpha-Simplex Compute/Lean
**Rationale:** Closes zero-fit Layer-2 ChamberGS, H_4/H_K GPMT modified quantum dimensions, 4x4 Hankel Z_{3A}^{(4)}, and binding compute scaling.
**Child Beans (12):** `qou-5lct`, `qou-h6ef`, `qou-sbn9`, `qou-xsmr`, `qou-n0so`, `qou-br4t`, `qou-yd54`, `qou-ozdk`, `qou-pg2f`, `qou-ndsa`, `qou-sv7h`, `qou-s7ld`

### Prioritized Beans in This Batch
- **`qou-5lct`** (`critical`, `in-progress`) — 5-Layer Iterated Confinement Tower (ConfinementLayer RG), Adiabatic Gap Stability, & Layer-4 Chemical Toric/Diophantine Gröbner Stoichiometry
- **`qou-h6ef`** (`high`, `in-progress`) — Layer-2 ChamberGS architecture: explicit nuclear motif conservation matrix A, universal Grobner / Graver basis, odd-even monomer staggering & capacitated Mayer-Jensen shell flips
- **`qou-sbn9`** (`high`, `todo`) — Formalize H_4(q) Wedderburn Weights, Killed 3- and 4-Row GPMT Modified Quantum Dimensions d_D(S^{(2,1,1)}) & d_D(S^{(1^4)}), and Per-Partition A=4 Cumulant Weighting
- **`qou-xsmr`** (`high`, `todo`) — General-K H_K(q) GPMT Modified Quantum Dimension Generating Function & Mayer/Ursell Cluster Resummation
- **`qou-n0so`** (`high`, `todo`) — Closed-Form 3D Tetrahedral alpha-Simplex Nuclear Coordination & Isospin-Asymmetry Operator (56Fe, 208Pb, 238U Saturation)
- **`qou-br4t`** (`high`, `todo`) — Closed-Form 4x4 Hankel/Cauchy Determinant Identity for 4-Row SU(4) q-Plancherel Normalization Z_{3A}^{(4)}(q)
- **`qou-yd54`** (`high`, `todo`) — Wire 3D Stacked alpha-Simplex + 4x4 Hankel Z_{3A}^{(4)} + Two-Term QED Across Z=0..118 Isotope Witnesses & Periodic-Table Atlas
- **`qou-ozdk`** (`high`, `todo`) — N5 [Higher-Order GPMT Ideal & H_12(q) Cabled (3^4) Singlet Bridge]: Formalize (z - z_D)^m Filtration & Bridge H_12(q) supset H_3(q)^4 to H_4(q) Alpha Cell *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-pg2f`** (`high`, `todo`) — N3 [Retire alpha_cluster_recursion.py & Rewire Consumers]: Excise Non-Lean 64 m_e G + Vol(7^2_1) Cluster Recursion & Wire Lean-Backed Simplicial/H_4 Compute *(Rule 13a: 0-instance classes: `Recursion`)*
- **`qou-ndsa`** (`high`, `in-progress`) — Break the confinement-LP homogeneity: get the braid into t or G, not just n_target
- **`qou-sv7h`** (`high`, `in-progress`) — Binding compute cannot scale: sparse path unreachable, zero Rust, float64 straddle *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-s7ld`** (`high`, `in-progress`) — chi scaling wall: the Rust GP minimal-length reduction is the cost, not dim — a dim-free seminormal path-sum makes 5Li/6Li seconds

### Worker Protocol
- Claim individual child beans via `beans update <bean-id> --status in-progress --body-append "Claimed by <branch> (YYYY-MM-DD)"`.
- Never mark a bean `completed` while an uninstantiated conjecture `class` or explicit `stays open` item remains (AGENTS.md Rule 13a).
- Enforce single-thread CPU caps (`LEAN_NUM_THREADS=1`, `nice -n 15`), zero float64 (`mpmath` >= 50-80 dps), and zero fitting.

Batch 4 Q-Drain-4 complete on PR #9241 (b11dd7654d5): qou-5lct & qou-h6ef closed; qou-sbn9/qou-ndsa/qou-s7ld upgrades staged in PR #9241.
