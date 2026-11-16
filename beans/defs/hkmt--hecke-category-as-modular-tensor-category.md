---
# hkmt
title: 'BWH-1: the Hecke category as a modular tensor category (S,T from Markov trace)'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T09:20:00Z
updated_at: 2026-11-16T18:35:00Z
parent: qou-rtxm
---

Parent: rtep. TIER: ACHIEVABLE INCREMENTALLY. Formalize the Hecke/Temperley-Lieb side AS a modular
category: simple objects = Hecke blocks λ, qDim = the corpus d_q (Markov-trace/Hoefsmit, already in
QOU.HeckeAlgebra.MarkovTrace / Hoefsmit), twist θ_λ=q^{2c(λ)} (KeystoneModularTwist.theta, proved),
S-matrix from the double-braiding trace. Prove the modular-data relations we can (S_{0λ}=d_λ/D done;
θ conjugation-antisymmetry done). This makes the *target* of BW=Hecke a concrete formalized MTC, so
the identification bwhk becomes "BW output = THIS explicit MTC". Does NOT close bwse (that's bwhk).

## Progress (2026-11-16, PR `litlfred/qou#8150` — `status: in-progress`)
- **Lean 4 formalization (`0` `sorry`, `0` custom axioms):** Added Part III of `folio/quantum-observable-universe/lean/QOU/Brings/BringLiftingObstructionRoutes.lean` (complementing `QOU.BraidKnot.KeystoneHeckeMTC` and `QOU.BraidKnot.KeystoneModularTwist`, verified with Lean v4.24.0 `-DautoImplicit=false`), proving:
  - `hecke_content_sum_transpose_antisymmetry`: explicit signed content-sum evaluation `c(λ) = ∑_{(r,c)∈λ}(c - r)` and transpose antisymmetry `c(λ') = -c(λ)` across `n = 1, 2, 3, 4` partitions (`c([]) = 0`, `c([2]) = 1 = -c([1,1])`, `c([3]) = 3 = -c([1,1,1])`, `c([2,1]) = 0`, `c([4]) = 6 = -c([1,1,1,1])`, `c([3,1]) = 2 = -c([2,1,1])`, `c([2,2]) = 0`).
  - `sl2z_modular_relations` and `ising_su2_level2_S_sq_eq_D_sq_id`: exact `SL₂(ℤ)` relations `S² = -I`, `S⁴ = I`, `(ST)³ = S²` and rank-3 `SU(2)₂` / Ising `(2S)² = 4I = D² C` (`D² = 1² + 1² + (√2)² = 4`).
  - `one_sub_mul_qIntegerPoly`, `qIntegerPoly_at_one`, and `qIntegerPoly_at_two_positive`: proves the telescoping identity `(1 - q)[k]_q = 1 - q^k` separating roots of unity (`q^k = 1`, `[k]_q = 0`, finite-rank `MTC_k` truncation) from `q ≥ 1` (`[k]_1 = k > 0`, `[k]_2 = 2^k - 1 > 0`, infinite-rank non-truncation at generic real `q₀ > 1`).
- **50-dps / Exact Probe + Witness:** `computations/probes/bring_lifting_obstruction_routes_z2_vs_z_probe.py` and `.witness.json` (12/12 assertions passed, including 50-dps verification of `(ST)³ = p₊ S²`, `S² = C`, and `S_{0,a} = d_a / D` for `SU(2)₂` and `SU(2)₃`).
