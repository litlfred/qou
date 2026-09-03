---
# qou-tvok
title: 'M1 machinery: explicit theta^-1 Euler-Maclaurin constant C_A for Var(Sum|c|) via CompositeEulerMaclaurin'
status: todo
type: task
priority: normal
created_at: 2026-08-29T01:34:20Z
updated_at: 2026-09-03T05:09:35Z
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

STEP 2 (2026-08-29): the REMAINDER rate is RESOLVED. With v_A=8/pi^2 subtracted exactly,
d(theta)=V_A/theta^2-8/pi^2 has exponent p in [0.95,1.02] over 5 doublings theta=1000..32000 =>
theta^{-1} (unambiguous now the v_A confound is removed; this legitimately resolves what the #5939
retraction left open). Sign: d<0 (from below). Coefficient c_1=lim theta*d ~ -0.0678 (measured;
candidate -2/(3pi^2)=-0.06755 REJECTED, near-miss 2.2e-4; no clean closed form). Rigorous bound
|d|<=C_A/theta NOT yet derived (needs EM bulk + Airy edge); target C_A~0.07-0.1. c_1 measured !=
C_A bounded. Probe: wlambda_covariance_epic_M1_tvok_remainder_rate.py; audit:
docs/audits/2026-08-29-covariance-kernel-M1-tvok-remainder-rate.md

2026-08-29: qou-po72 sibling (PR #5969) pins the de-poissonized CS constants; clarified that step-1 v_A=8/pi^2 is POISSONIZED (k>=1), CS uses V_A=8/(9pi^2) (k>=2). C_A finite-n rate bound still open (Olver-Bessel wall).

2026-09-03: 'compute TV(g'')' is ILL-POSED as stated -- measured, not asserted. The EM-osc target set in PR #6469 (TV(g'')>=48|c_1|~3.25) presumes a local integrand g whose second derivative one takes. TEST 1: the leading variance is a MODE functional, V_A = Sum_{k odd} A_k^2/k with A_k=8(-1)^{(k+1)/2}/(pi(k^2-4)), verified converging to 8/pi^2 to 1.3e-15 at K=5001 -- an H^{1/2}-type NONLOCAL object, not an integral of a pointwise density. TEST 2: the candidate local density c(rho)=Sum_{k!=0}k^2 S(k;rho)^2 = Sum sin^2(pi rho k)/pi^2 DIVERGES -- partial sums 10.132/101.32/1013.2/10132.0 at K=1e2..1e5, exactly linear (ratio 10.0), identical for rho=0.25,0.5,0.75. So c(rho)=+infinity and there is NO local variance density (g')^2 c(rho); the corpus phrasing in rigorous-finite-n-bound.md that suggests one is too loose to hand over a g. CONSEQUENCE: TV(g'') not computable because there is no g. The theta^{-1} RATE is unaffected (c_1~-0.0678 stands, closure needs only C<=23.4). h^2=1/(4theta) scaling is CONSISTENT with EM but consistency is NOT identification -- many mechanisms give theta^{-1}; picking a plausible integrand to check against 3.25 would be fitting a target, so it was not done. WELL-POSED REFORMULATION (TEST 3, verified): for a projection kernel V_A = Sum_x g^2 K(x,x) - Sum_{x!=y} g g K^2 = A-B, exact to ~1e-36 at dps=40 against the (1/2)Sum(dg)^2K^2 form (confirms K^2=K), and A/(A-B) = 4.302 -> 5.352 as theta 64->100 vs sqrt(100/64)=1.25 predicted / 1.244 observed, so the split cancels only by O(sqrt theta) and is numerically viable. NEXT: (P1) EM in the MODE variable k on Sum A_k^2/k, needing the finite-theta deformation of A_k; or (P2) EM on A=Sum g^2 K(x,x) (clean 1-D smooth integrand g^2 rho) to see whether its remainder carries c_1. Probe: wlambda_covariance_epic_M1_tv_gpp_wellposedness.py (exit 0, NO float64). Audit: docs/audits/2026-09-03-covariance-kernel-M1-k5r5-tv-gpp-is-ill-posed.md
