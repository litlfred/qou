---
# qou-uvqk
title: 'PROVE(lean): cauchyMul_order — theorem cauchyMul_order {q s t : ℝ} {a b : ℕ → K} (ha : IsQGevreyOrder q s a) (hb : IsQGev [cited ramis-sauloy-zhang2013]'
status: completed
pr: 8224
updated_at: 2026-11-21T12:40:00Z
type: task
priority: normal
tags:
    - lean
    - cited-sorry
    - paper-qou
    - repo-infra
    - cite-ramis-sauloy-zhang2013
    - reorg-2026-10-04
created_at: 2026-08-01T23:31:06Z
updated_at: 2026-10-04T15:22:24Z
parent: qou-u2al
---

**File:** `QOU/Mathlib/QGevreyOrder.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/folio/quantum-observable-universe/lean/QOU/Mathlib/QGevreyOrder.lean

### `cauchyMul_order`  —  line 268  ·  tier **P** (repo-infra-dependent)
- **Proposition:** `theorem cauchyMul_order {q s t : ℝ} {a b : ℕ → K} (ha : IsQGevreyOrder q s a) (hb : IsQGevreyOrder q t b) (hq : 1 < q) : IsQGevreyOrder q (cauchyEnvelope s t) (cauchyMul a b) `
- **Cited:** `[ramis-sauloy-zhang2013]`
  - [ramis-sauloy-zhang2013] Ramis, Sauloy, Zhang (2013), *Local analytic classification of q-difference equations* — https://arxiv.org/abs/0903.0853
- **Tractability:** Gevrey order of a Cauchy product cauchyMul_order; repo-internal envelope estimate. Overlaps PR #4140.
- **Next step:** Blocked on in-repo scaffolding (not Mathlib). Complete/route the named repo infra, then discharge; do NOT weaken the statement.

## Progress Update (PR #8224)
- **Status**: `in-progress` (awaiting Merge Manager merge of `litlfred/qou#8224` at `9725d15463b70fb5b273b6c495db79723640032c`).
- **Lean Formalization**: `QOU.QBeta.FaddeevHalvesSelectionAndQGevreyCauchyEnvelope.q_gevrey_cauchy_mul_quadratic_envelope_identity` (Exact completion of the square for the q-Gevrey Cauchy convolution exponent with harmonic-mean lower envelope s*t/(s+t).)
- **80-dps Witness**: `computations/probes/faddeev-halves-selection-and-q-gevrey-cauchy-envelope.witness.json` (`scriptHash: cea527e5468d`, `scriptCommitSha: 9d85aecf9640ed04a9fa33fe94c3662500eae503`).


## 2026-11-21T12:40:00Z — alien-calculus drain (thread "Build the q-native alien calculus")

**Done on main; closing.** `QOU.Mathlib.QGevreyOrder.cauchyMul_order` is proved sorry-free on main 2ae54ab401: re-verified here with lean-direct (exit 0), `#print axioms` = [propext, Classical.choice, Quot.sound]. Note the statement this bean quotes is FALSE as written: main proves `cauchyMul_order_unhypothesised_false` and `cauchyMul_order_noCancellation_insufficient` (b ≡ 0 counterexample). The proved theorem adds NoCancellation and everywhere-nonzero factors, which the two refutations show are necessary, so this is a correction of the statement, not a weakening. The batch PR #8224 cited above is not needed for this. Superseded-premise check: none.
