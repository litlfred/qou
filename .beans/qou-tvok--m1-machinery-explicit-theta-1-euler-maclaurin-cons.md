---
# qou-tvok
title: 'M1 machinery: explicit theta^-1 Euler-Maclaurin constant C_A for Var(Sum|c|) via CompositeEulerMaclaurin'
status: todo
type: task
priority: normal
created_at: 2026-08-29T01:34:20Z
updated_at: 2026-08-29T02:52:33Z
---

SCOPE UPDATE (2026-08-29): 'kink cancels => clean theta^{-1} bulk' is RETRACTED (qou-8quz refuted).
Handle the Airy-EDGE contribution explicitly (plausibly theta^{-5/6}); sub-leading exponent open
(best single power ~0.94). Robust: correction small (|coeff|~0.05) => any rate >= theta^{-1/2}
suffices for closure. Bulk via CompositeEulerMaclaurin; edge via GaussianTailBound/GaussianSumBound.

STEP 1 DONE (2026-08-29): the exact LEADING constant v_A = lim Var(Sum|c|)/theta^2 = 8/pi^2, DERIVED
(rigorous modulo the IO Kerov CLT) + triple-verified.
  IO CLT: v_A = sum_k hat_A_k^2/k. Closed form (elementary integral): hat_A_{2m+1}=8(-1)^{m+1}/(pi((2m+1)^2-4)),
  even k vanish. => v_A=(64/pi^2) sum_{n odd} 1/[n(n^2-4)^2]; and that series = 1/8 by partial fractions +
  telescoping (divergent Sum 1/odd AND pi^2/8 tails both cancel; 1/16+1/16). => v_A=8/pi^2.
Verified: closed form vs integral 1e-42; sum_k hat^2/k vs 8/pi^2 8e-17; series vs 1/8 exact;
descent-DPP Richardson 9e-8. Lean: ContentVarianceLeadingConstant.vA_summand_partial_fractions
(sorry-free, the partial-fraction algebra over a char-0 field).
REMAINING in qou-tvok: the remainder constant C_A + rate (bulk EM via CompositeEulerMaclaurin + Airy
edge via Gaussian bounds); sub-leading exponent still open (PR #5939 retraction).
