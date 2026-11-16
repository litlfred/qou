---
# qou-z4ba
title: The c1 mirror asymmetry has the WRONG SIGN, 0/230 against AME -- and it is scale-free
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T02:08:08Z
updated_at: 2026-10-04T15:15:07Z
parent: qou-v2om
---

Successor to qou-pdg9 (c1 derived, PR #6492) and qou-i719 (PR #6541). The derived closed form c1(Z,N) = (21Z+16N)(2^-(A+1) - 4^-A) - 4(I_pp - I_nn) 4^-A gives an EXACT mirror difference c1(Z,N) - c1(N,Z) = (Z-N)(5*2^-(A+1) - 13*4^-A), positive for Z>N whenever A>=3 (the bracket is 4^-A(5*2^(A-1) - 13), negative only at A=2). So the trace channel says the PROTON-RICH mirror binds MORE. AME says the opposite in all 230 mirror pairs with A>=3: 0/230 sign agreement. Parameter-free (no fit anywhere) and SCALE-FREE (any positive energy scale preserves a sign), so this survives the unpinned-E_0 problem qou-59j5 documents -- unlike every magnitude claim in this lane. Localises what is missing as a charge-dependent REPULSIVE term, i.e. the Coulomb term the corpus records as nowhere derived (CoulombFromCrossingCounts scope: 'a_C is nowhere').


---

## Round 48 Execution Update (2026-11-16, PR #8181)

- **PR:** https://github.com/litlfred/qou/pull/8181 (`e3a0c2e1773d8a4bc1635ead95154cb8d9babb4d`)
- **Lean 4 Formalisation (`0` `sorry`, `0` `axiom`, wired into `QOU.lean`):**
  - Wired `QOU.MassTheory.MirrorAsymmetrySign` into `folio/quantum-observable-universe/lean/QOU.lean` (fixing its orphan status).
  - Added `folio/quantum-observable-universe/lean/QOU/MassTheory/MirrorAsymmetryGapInvariance.lean` (wired into `QOU.lean`), proving:
    - `c1Scaled_mirror_diff_general`: `c1Scaled P Q Z N A - c1Scaled P Q N Z A = (Z - N) * ((P - Q) * (2^A - 2) - 16)` for arbitrary `(P, Q : Int)`.
    - `c1Scaled_mirror_diff_of_gap_five` & `c1Scaled_mirror_diff_grouped_eq_borromean`: exact equality of the mirror difference `(Z - N) * (5 * 2^A - 26)` across both the historical `(21, 16)` `grouped` word and the canonical `(3, -2)` `borromean` word (`P - Q = 5`).
    - `mirrorFactorFive_neg_at_two` & `mirrorFactorFive_pos_of_ge_three`: sign flip at `A = 2` (`-6 < 0`) and strict positivity (`≥ 14 > 0`) for all `A ≥ 3`.
    - `repulsive_coulomb_flips_scaled_mirror_sign`: necessary and sufficient repulsive Coulomb threshold `ΔC_ZN - ΔC_NZ > E₀ · (Z - N) · (5 · 2^A - 26)` to flip the mirror sign.
- **Probe & 50-dps Witness:**
  - `computations/probes/spin_orbit_magic_rstar_mirror_probe.py`
  - `computations/probes/spin-orbit-magic-rstar-mirror-probe.witness.json`
- **Status:** Kept at `in-progress` pending owner review and PR merge.
