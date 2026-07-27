---
# bwsa
title: 'bwS0-closure: interpolation-rigidity engine + distinct root points (DONE)'
status: completed
type: task
priority: high
created_at: 2026-07-27T00:30:00Z
updated_at: 2026-07-27T00:30:00Z
---

Parent: bws0. DONE on PR #4365 (sorry-free, lean-direct exit 0):
- `KeystoneGaugeRowRigidity.eq_of_eval_agree_card`: two polynomials of degree < s.card agreeing on
  a finset s of distinct points are equal.
- `KeystoneGaugeRowRigidity.bwS0_eq_hecke_of_rigidity`: the conditional reduction (bounded-degree +
  root agreement ⇒ equal at t₀).
- `KeystoneHabiroRootFamily`: `foldValue_injOn` (2cos(kπ/N) injective on [1,N-1]) + `foldPoints_card`
  (N-1 distinct points) + `eq_of_root_family_agreement` (agreement across level-N fold points +
  degree < N-1 ⇒ equal). The root family supplies arbitrarily many distinct interpolation points.
