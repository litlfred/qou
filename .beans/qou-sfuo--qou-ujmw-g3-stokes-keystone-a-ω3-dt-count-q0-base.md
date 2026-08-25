---
# qou-sfuo
title: 'qou-ujmw G3 Stokes keystone: A_ω=3 DT-count — q→0 base case landed (PR #4534); internal categorical derivation still open'
status: completed
type: task
created_at: 2026-08-01T23:39:37Z
updated_at: 2026-08-01T23:39:37Z
---


## Status (PR #4534, 2026-08-01)

**A_ω = 3 IS a DT/3d-index count — established, not assumed.** GGM 2012.00062
Conjecture 4 (a theorem for 4₁) identifies the Stokes constants with the
rotated-3d-index / DT–BPS invariants of T[4₁]; the value is certified through
q⁴⁰⁰ (`qbeta_g3_ggm_stokes_41.py`) and its distinguished reading is the exact
symmetry constant `(S₁₂+S₂₁)/S₁₁ = 3` (`StokesSymmetryConstant.lean`, conditional).

**Landed this PR:** `QOU/QBeta/StokesQZeroDTCount.lean` (sorry-free) — the
unconditional q→0 base case: `W₋₁(0)=[[0,-2],[1,1]]` (det=2, GGM Thm 9), sandwich
`A·W₋₁·B·W₋₁ᵀ·C = -2·S⁺(0)`, `S⁺(0)=[[1,3],[0,1]]`, off-diagonal DT constant = 3.
Witness `aomega-qzero-dt-count.witness.json`; audit
`docs/audits/2026-08-01-ujmw-aomega-dt-index-derivation.md`.

## Open (the two remaining legs — verdict: reduced-to-named-sub-obstruction)

1. **Internal derivation of the integer 3** (parent gap `qou-qnnq`): derive the
   symmetry constant 3 (= the 4₁ DT/BPS invariant) from the QOU categorical
   drivers (Hecke H₃ / Bring / Wedderburn) rather than importing GGM's theorem.
   The DT spectrum `{3,4}` (GGM eq 98) is the object; a `3 = disc`/`#connections`
   shortcut is a single-knot coincidence (5₂ block is 3×3) — do NOT assert it.
2. **Value normalization** `Im 𝔙_q → N_odd`, magnitude `A′ ≈ 2.37` (beans
   `qou-2cvs`, `qou-q95i`; one-instanton map audit 2026-07-25).

Note: parent bean `qou-ujmw` was created on a sibling branch and is not in this
branch's `.beans`; this bean tracks the same scope from PR #4534.
