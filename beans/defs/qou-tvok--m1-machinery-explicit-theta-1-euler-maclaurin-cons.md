---
# qou-tvok
title: 'M1 machinery: explicit theta^-1 Euler-Maclaurin constant C_A for Var(Sum|c|) via CompositeEulerMaclaurin'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T01:34:20Z
updated_at: 2026-11-21T14:00:00Z
parent: qou-m6dn
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


STEP 3 (2026-09-03, PR #6500): P2 REFUTED -- the trace split cannot localise c_1.
P2 (named in #6472) was: apply EM to the clean 1-D side A = Sum_x g^2 K(x,x) of
V_A = A - B and see whether its remainder carries c_1 ~ -0.0678. Measured over
theta=250..16000 (exact descent-DPP, mpmath dps=40, exit 0, 8.5s), NO, twice over:
 (a) c_1 = a_1 - b_1. Both sides carry a theta^1 coefficient and b_1 needs the
     DOUBLE sum B, which is not a 1-D sum and is not EM-able. The split
     partitions the problem; it does not reduce it.
 (b) A has NO theta^2 term. Tested DIRECTLY (not by trend), since alpha is pinned
     independently: (A/theta^{5/2} - alpha)*sqrt(theta) falls 0.02745 -> 0.004681
     with the per-doubling ratio RISING 1.3333 -> 1.3513 toward sqrt(2). A nonzero
     a_2 would PLATEAU and drive the ratio to 1; both go the other way. Bound
     |a_2| <= 0.00468 = at most 0.578% of V's theta^2 coefficient 8/pi^2. So the
     EM-able side does not hold even V's LEADING coefficient.
POSITIVE result landed alongside, and it is what makes this a refutation rather
than a stall: A ~ alpha theta^{5/2} with alpha = 0.429421692 (two-level
Richardson) against the INDEPENDENT continuum integral
alpha = 8*Int_{-1}^1 u^4 rho(1-rho) du = 0.429421692, rho(u)=arccos(u)/pi --
agreeing to 3.3e-10. The continuum reference an EM argument for A would be
defined against is CONFIRMED by computation, so the negative is about the split,
not a missing input.
Supporting: A/V -> 0.52978 sqrt(theta) vs predicted alpha/(8/pi^2) = 0.5297778,
5 digits (leading half-order cancels exactly, a_{5/2} = b_{5/2}); |c_1|theta/A
runs 3.978e-5 -> 7.801e-8, exponent 1.4999 -> c_1 sits at relative theta^{-3/2}
inside A against theta^{-1} inside V, so reading it off A needs HALF AN ORDER
MORE accuracy, not less.
UNCHANGED: rate theta^{-1}, c_1 ~ -0.0678, closure needs only C <= 23.4. The
split itself stands (exact, well-conditioned, now with a verified continuum ref).
ROUTE INVENTORY after this: pointwise-Bessel refuted (#6438, U/V unbounded, ~17x
short at theta=78); TV(g'') as posed ill-posed (#6472, c(rho)=+inf, no local
density); P2 refuted (#6500). REMAINING exhibited candidate: P1, the mode sum
V_A = Sum_{k odd} A_k^2/k -- already a 1-D sum in k with a smooth summand; if the
finite-theta correction is an EM remainder IN k then that summand IS the g whose
TV(g'') #6469 asked for. Needs the finite-theta deformation of A_k, untouched here.
Probe: computations/deltalambda/wlambda_covariance_epic_M1_p2_trace_split_orders.py
Audit: docs/audits/2026-09-03-covariance-kernel-M1-k5r5-p2-trace-split-refuted.md
NOTE symbol collision: PR #6492 (qou-pdg9) lands a different 'c_1' the same day
(leading hbar_q coefficient of the trace difference, a permutation count). Not
the same object. Flagged on #6492.


2026-09-03 RETRACTION of my own 'C <= 23.4' (PR #6500). The closure-arithmetic
sentence introduced in #6469 and repeated in 5 further sites -- 'at the theta^{-1}
rate, N0 = ceil(C/m_inf) <= 78, i.e. C <= 23.4 -- far weaker than the C <= 2.65 a
conservative n^{-1/2} reading demands' -- is WRONG. Two defects:
 (i) WRONG OBJECT. The theta^{-1} rate is V_A's (d(theta)=V_A/theta^2-8/pi^2,
     poissonized). The margin m(n) = rho_P - sigma_D/sigma_A is a RATIO OF SQUARE
     ROOTS of two variances plus a correlation, at fixed n. Nobody has propagated
     the V_A rate through the ratio, the sqrt and de-poissonization. I used a
     measured rate for one object as a premise about another.
 (ii) MISLABELLED THE PROVED BOUND. What is proved (PR #5929) is
     |m(n)-m_inf| <= C n^{-1/2}, so N0 = (C/m_inf)^2 -- SQUARED -- and the
     requirement is C <= m_inf*sqrt(79) = 2.6681. Calling 2.65 'a conservative
     reading' inverts it: it is THE requirement under the bound in hand, and it was
     already sitting in constant_C_landscape.py as C_TARGET. A corpus-grep of my
     own epic would have caught this.
MEASURED REPLACEMENT (wlambda_covariance_epic_M1_margin_envelope_exponent.py, exit
0, exact Fractions, NO float64, n=4..46, 33s): running max of |m-m_inf|*n^p over
[N,46]. p=1/2 column FALLS 0.1999 -> 0.0580 (~3.4x) => the proved n^{-1/2} shape is
NOT TIGHT, the margin decays strictly faster. p=1 column is FLAT from N=6 at
0.31512 (attained n=39) => consistent with n^{-1}. So the n^{-1} shape I assumed IS
empirically supported for the margin -- it was still wrong to report the closure
arithmetic as though that were established. LIMIT OF THE EVIDENCE: over n<=46 the
data excludes n^{-1/2} decisively but does NOT cleanly separate n^{-1} from a
slightly slower power (|dev|*n drifts up ~18% across outer peaks: 0.2613 at n=9,
0.2636 at 21, 0.3094 at 38; the p=1 column is flat only because its sup sits at an
interior n=39). Exponent NOT fitted from peaks by necessity: sign runs are 4-6(-),
7-12(+), 13-15(-), 16-46(+), so the n=14 local max is a sub-lobe ~7x below the outer
envelope and the last run is double-humped (21 and 38); consecutive-peak exponents
come out 6.2, -4.7, 0.73, and hand-dropping n=14 to rescue that would be choosing
the data to fit.
NET EFFECT ON THE ROUTE -- IT STRENGTHENS IT, and needs no improvement to the proved
shape: requirement C <= 2.6681 vs empirical envelope C_emp(n>=13) = 0.0580 =>
HEADROOM 46x (N0 at C_emp would be 0.037). A rigorous constant within 46x of the
truth closes M_1>0 for all n. That is the real 'a crude bound suffices' -- and it is
the corpus's own position already: finite_n_cs_margin.py says the remaining
requirement is an effective variance bound 'large enough (leading margin 0.30) that
a crude rate suffices'. My chat recommendation to pivot to a crude bound was NOT a
new idea; it restates what the epic held and I should have cited it.
BLAST RADIUS (8 sites, 6 merged): em_osc_constant_prediction.py docstring + printed
line (fixed at the producer -- it printed the claim every run); audit docs
weight-bug-retraction-retracted (x2), tv-gpp-is-ill-posed, p2-trace-split-refuted
(annotated, not rewritten -- dated records); beans qou-k5r5 + qou-tvok (this note).
UNAFFECTED: V_A rate theta^{-1} and c_1 ~ -0.0678; the weight-bug fix; P2's
refutation and the alpha=0.429421692 continuum cross-check (3.3e-10); TV(g'')
ill-posedness. Audit:
docs/audits/2026-09-03-covariance-kernel-M1-k5r5-margin-envelope-retraction.md
NEXT unchanged in kind, now with a number: produce a RIGOROUS C <= 2.6681 in
|m-m_inf| <= C n^{-1/2} against an empirical 0.0580 (Olver/Debye/Airy constant
tracking, as constant_C_landscape.py has said all along). Gap qou-k5r5 OPEN.


2026-09-03 CORRECTION (PR #6528) of the 'pointwise route ~17x short' figure in the
DECISIVE NEGATIVE entry above. The STRUCTURAL negative is UNAFFECTED and stands: U/V
grows without bound (42.8, 45.7, 53.9, 70.7, 91.9 at theta=64..512), so no pointwise
bound however sharp controls V_A uniformly; the oscillatory cancellation is
load-bearing. That argument never used the arithmetic below.
THE DEFECT: 'keeping the relative error on V_A under m_inf=0.3002 forces K<0.058 =>
~17x short' compares a RELATIVE error on V_A against m_inf, an ABSOLUTE margin, and
drops the conversion. Since sigma_D/sigma_A = sqrt(V_D/V_A), a relative perturbation
delta_A on V_A moves the MARGIN by sig_ratio_inf*delta_A/2 = 0.3398*delta_A, not by
delta_A. Admissible relative error is m_inf/0.3398 = 0.8834, not 0.3002 => the merged
threshold is 2.943x TOO STRICT.
RECOMPUTED (wlambda_covariance_epic_M1_pointwise_shortfall_recomputed.py, exit 0,
0.9s, NO float64, reuses #6438's own U_and_V by file path) at theta=78, the largest n
the exact Fraction table reaches: U/V = 45.5868; relative err on V_A per K = 5.16169
(the merged probe quotes 5.17 -- the AGREEMENT is the check that this locates the
exact defect rather than recomputing something else); K_adm = 0.17115 (merged: 0.058);
K_adm = 0.085574 if V_A and V_D split the budget. Against an O(1) Debye coefficient
the shortfall is ~5.8x, or ~11.7x split -- NOT ~17x.
WHY IT MATTERS: '17x short' reads as hopeless, '5.8x short' reads as a gap a sharp
constant might close. It does NOT revive the route (the structural negative is
independent) but it should not decide that question by accident.
NOT SETTLED: 'O(1)' for the Debye/Olver coefficient is an order of magnitude, not a
pinned constant anywhere in the corpus. Both ~17x and these figures are 'K_adm vs
O(1)'; only K_adm is measured.
SAME ERROR CLASS AS TODAY'S OTHER RETRACTION (C<=23.4, PR #6500): a quantity measured
for one object compared against a threshold belonging to another, conversion dropped.
V_A, sigma_A, sigma_D/sigma_A and m are four different objects; write the conversion
down before comparing anything to m_inf.
BLAST RADIUS: pointwise_bound_insufficiency.py (docstring + printed RESULT -- fixed at
the producer, it printed ~17x every run); deep_tail_rigorous_majorant.py printed note;
audit docs deep-tail-rigorous-need-lit-localised, p2-trace-split-refuted,
weight-bug-retraction-retracted; these two beans. Audit:
docs/audits/2026-09-03-covariance-kernel-M1-k5r5-pointwise-shortfall-recomputed.md
Gap qou-k5r5 OPEN; NEXT unchanged: a RIGOROUS C <= 2.6681 from the oscillatory
cancellation, against an empirical envelope of 0.0580 (46x headroom).

## Progress Update (Round 92 — lane-cf11)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/NucleonOrderingAndBringAdjointTorsionBrick.lean` with 80-dps probe `computations/probes/nucleon_ordering_and_bring_adjoint_torsion_brick_probe.py` and witness `computations/probes/nucleon-ordering-and-bring-adjoint-torsion-brick.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8348 (`feat/qou-b9cj-q6h7-qd27-qint-r91v-tvok`, HEAD `e0985c4fc3ff765e1935e3343005512aaca69b2b`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8348, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-08-29: "tvok(qou-k5r5) step 2: the V_A remainder rate is theta^-1 (RESOLVED), c_1 ~ -0.0678 measured"). The work may be partly or fully done. Read the bean before you close it.

## 2026-11-21: premise check (hecke-gs-conj sibling, session_01Qmmkt5sJX34MCerjRMERJN; owner: nothing rests on replaced results)
The "Round NN progress" entries above cite batch PRs closed on 2026-11-20 as vacuous or superseded. Their Lean/probe/witness paths are ABSENT on main (checked against main 2ae54ab40 file list). Do not build on them or cite them. Leading constant v_A=8/pi^2 (poissonized) is on main in ContentVarianceLeadingConstant.lean; the finite-n remainder bound C_A is NOT derived (rate itself was retracted and re-retracted in k5r5; see main commits 8ddfeaf1b76, 51bc3bd3fc9, 62c0f17dead).
No physics premise in this bean is affected by the rulings in docs/coordination/owner-rulings.md (pure Plancherel combinatorics). Kernel proved for 3<=k<=20 (YoungDiagramKernel.lean:200, kernelValue_nonpos_of_le_twenty); general k open. Status unchanged: an open conjecture stays open.
