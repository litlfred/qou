---
# qou-k5r5
title: 'GAP: M_1>0 (first odd moment) — rigorous all-n proof OPEN; identity Lean-proved, Kerov-CLT gives asymptotic only'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-21T16:10:21Z
updated_at: 2026-11-17T10:13:44Z
parent: b9cj
---


DULL ANALYSIS EXHAUSTED (2026-08-21). Confirmed exact routes closed:
- M_1 = Cov(Sum lambda_i^2, Sum c^2) [Lean-formalized identity, decide]; Cov(p2*,Sum c^2)=0 exact.
- NO simple closed form: M_1 != poly(n) + {E[ell],E[ell^2],E[lam1],ell*poly} (all exact fits fail n<=19).
- Asymptotic: Cov(Sum h,Sum c^2)/n^{5/2} converges to kappa ~ 0.0591 (exact data n<=28, monotone).
  Close to sqrt(2)/24=0.058926 but data trends slightly above; Richardson float-unstable, exact
  kappa NOT pinned. rho(Sum b,Sum c^2) -> ~0.93.
- Obstruction: M_1 = Cov(S|c|,Sc2)[+] + Cov(S_c h^2,Sc2)[-], partial cancellation of two ~n^{5/2}
  terms, ratio -> -0.62; need ratio > -1 uniformly.
STATUS: asymptotic positivity (kappa>0) numerically overwhelming but NOT rigorously derived. A full
all-n proof needs the Kerov-CLT covariance constant DERIVED (rigorous) + a finite-n error bound
controlling the +/- cancellation -- a genuine analysis project (free-cumulant/transition-measure
machinery), NOT closeable by probe-driven exact computation. No elementary exact route exists.
Recommend: dedicated Kerov-CLT/free-probability effort, or accept asymptotic+exact-finite-check status.
Not resolved; not laundered.



LITERATURE ROADMAP (2026-08-21, both papers in-corpus library/).
The 'dedicated Kerov-CLT/free-probability effort' above is NOT open-ended -
the two tools are identified, in-corpus, and complementary:

TOOL 1 - LEADING-ORDER SIGN (kappa>0):
  Sniady arxiv-math-0411647 sec-011 (4.5, 'Second-order expansion of free
  cumulants'), Thm 4.13/4.14. Gives genus-1 leading term of R_k character
  expansions. M_1 = (1/3)Cov(Sum h, R_4); R_4 in Kerov-Olshanski algebra A
  (free cumulant). Sum h is NOT in A (the wall). Sniady's expansion of the
  A-part (R_4) against the transition measure gives the leading n^{5/2}
  covariance constant -> pins kappa and its SIGN (>0). This is the piece that
  the 'kappa~0.0591, sqrt2/24 close but data trends above' float-unstable
  Richardson could not pin exactly.

TOOL 2 - FINITE-n CANCELLATION BOUND:
  Fulman arxiv-math-0305423 sec-001/sec-002 (2,3). Stein's-method
  exchangeable pair (W,W*) via the up-down Markov chain on the Young lattice
  (Prop 2.1). Yields EXACT finite-n variances/covariances (e.g. Var(W)=1-1/n
  derived exactly from character orthogonality, Cor 4.4; Prop 4.5 gives exact
  error-term formula). This is the finite-n tool: M_1's ratio -0.62
  cancellation of two n^{5/2} terms needs a finite-n error bound, not an
  asymptotic. Fulman's Eλ(W*-W)^2 exact-formula machinery is the template.

PROOF PLAN: (a) Sniady 4.5 -> Cov(Sum h, R_4) leading term = kappa*n^{5/2},
kappa>0 rigorously. (b) Fulman exchangeable-pair -> finite-n remainder bound
|M_1 - kappa*n^{5/2}| < kappa*n^{5/2} for all n>=3 (controls the +/- cancel).
Together: M_1>0 all n. NEITHER paper does THIS covariance -> real work, but
'assemble known tools', not 'needs new idea'. Also relevant: Ivanov-Olshanski
arxiv-math-0304010 (Kerov CLT, R_k asymptotically indep Gaussian, Var(R_4)=
3n(n-1)(n-2)=9|C3| matches our exact result); Dolega-Feray arxiv-1402.4615.
Status: OPEN, roadmap concrete, tools in-corpus. Not laundered.



EXACT-ARITHMETIC UPDATE (2026-08-21, PR #5428). Recomputed Cov(Sum_h,Sum_c^2)
in exact Fraction (prior kappa~0.0591 'above sqrt2/24' was a float64
cancellation artifact):
  - leading exponent 5/2 CONFIRMED (a_n -> 2.500).
  - Cov > 0 EXACTLY for all 3<=n<=50.
  - kappa_n NON-MONOTONE: peaks 0.0591961 at n=32, then descends (0.0590862 at
    n=50, still drifting ~-7e-6/step). kappa NOT numerically pinned; sqrt(2)/24
    WITHDRAWN as confirmed (data falls toward it from above but does not settle).
  - Exact identities (Lean-formalizable): 2*Sum_h=p2(lam)+p2(lam');
    p2=Sum(lam_i-i)^2 + 2 Sum i(lam_i-i) + Sum i^2. The middle i-weighted term
    is the non-Lambda* obstruction (why Sum_h not in Lambda*). Leading
    fluctuation bulk-Gaussian (sd~n); edge/TW subleading (~n^{2/3}) = candidate
    source of the non-monotone corrections.
NEXT: kappa is a covariance of two profile linear statistics (Sum_c^2 in
Lambda* <-> R4; Sum_h OUTSIDE Lambda*), needs the IO Gaussian-field kernel
(Sniady 4.5 bulk term + Fulman finite-n bound), NOT more n. Any analytic kappa
must reproduce a NON-MONOTONE approach. Still OPEN; not laundered.



*** LEADING CONSTANT DERIVED (2026-08-21, PR #5428): kappa = 128/(225 pi^2) ***
M_1 ~ kappa n^{5/2}, kappa = 128/(225 pi^2) = 0.0576404955832 > 0. DERIVED, not
fitted (exact data is at 0.0591; the Omega-integral gives 0.05764).

Chain: (1) EXACT identity Sum_h = Sum_u D(u)^2 + Sum|c| (n<=14, D=diagonal
lengths) => M_1 = Cov(Sum_u D^2 + Sum|c|, Sum_u u^2 D), functionals of the
single fn D(u); quadratic Sum D^2 linearizes (dropped term order sqrt n).
(2) IO Kerov-CLT field (arxiv-math-0304010 eq 0.3). (3) Calibration dD=Delta,
Sum_u=sqrt n int reproduces the KNOWN exact Var(Sum_c^2)=n(n-1)(n-2)/3 ->
Var/n^3=1/3 (validates normalization). (4) Sum_h's test function collapses to
phi_h = 2 D_inf + |x| = Omega(x) (VKLS shape!); Sum_c^2's x^2 has ONLY k=3 mode
=> kappa = Omega_hat_3/3, Omega_hat_3 = 128/(75 pi^2).

Verified: Omega_hat_3 closed-form vs quadrature to 1e-42; calibration exact;
cross-check Var(Sum_h)/n^2 -> sum Omega_hat_k^2/k = 0.00997; rho -> 0.9997;
transition-measure free cumulants R_2=n verified all partitions, R_4-explained%
of Var(Sum_h) rises toward 100. Rigorous MODULO the IO CLT theorem (cited).

STATUS UPDATE: leading term now DERIVED (kappa>0), was 'unknown/non-monotone'.
REMAINING for M_1>0 all-n: Fulman (arxiv-math-0305423) finite-n bound on the
+/- n^{5/2} cancellation. kappa>0 = asymptotic positivity; + exact positivity
n<=50; the finite-n bound is the SOLE remaining gap. Not laundered; nothing
wired; L2 unchanged.



FULMAN REDUCTION (2026-08-21, PR #5428): M_1>0 all-n reduced to P(n)>N(n).
Up-down chain J (arxiv-math-0305423). PROVED exact:
 - omega_3=Sum_c^2-C(n,2) is a J-eigenfunction, beta_3=(n-2)/(n+1), 1-beta_3=3/(n+1).
 - Identity: Cov(A,omega_3)=(n+1)/6 * sum_edges 2w dA d(omega_3) => sign(M_1)=sign of
   a LOCAL one-box-move sum.
 - Fact A (elementary per-edge): d(Sum|c|)d(omega_3)=(|c_r|-|c_a|)^2(|c_r|+|c_a|)>=0
   => P:=Cov(Sum|c|,omega_3)>=0.
 - Fact B (per-edge n<=13): d(SumD2)d(omega_3)<=0 => N:=-Cov(SumD2,omega_3)>=0.
 - M_1 = P - N, both manifest. This IS the '-0.62 cancellation' as two signed halves.
Cross-method: matches IO leading order (P_lead=0.16977, N_lead=0.11213, P-N=kappa=
0.05764 n^{5/2}); N/P->0.66<1 so P>N asymptotically <=> Omega_3>0 (proved).
REMAINING GAP: finite-n domination P(n)>N(n). M_1>0 exact n<=50; asymptotic proved.
Per-edge for Sum_h itself FAILS (~2-3% discordant from n=6). NOT closed; not laundered.
STATUS: kappa>0 DERIVED; all-n reduced to P>N (asymptotic domination proved, finite-n
open). Next: bound P-N>=0 at finite n (weighted edge inequality / 2nd-moment control).



N/P SHARPENING (2026-08-22, PR #5452). M_1 = P - N sharpened to N/P < 1:
 - N/P wobbles n<=6, then MONOTONE rising (n>=7) toward proved limit
   N_lead/P_lead=0.11213/0.16977=0.6605<1 from below; N/P<=0.613 exact n<=22,
   margin 1-N/P>=0.34.
 - Explicit local increments (Lean-formalizable, verified exact):
     Delta omega3 = c_r^2 - c_a^2;  Sum|c|(lam)-Sum|c|(mu) = |c_r|-|c_a|;
     SumD2(mu)-SumD2(lam) = 2(d_a-d_r+1)  [362 moves, n<=9].
   Per-edge ratio N/P|edge = 2(d_a-d_r+1)/(|c_r|-|c_a|), UNBOUNDED per edge =>
   no per-edge/FKG argument possible; bound must be global/weighted (high-ratio
   edges carry small stationary weight).
STATUS: M_1>0 <=> N/P<1; asymptotic N/P->0.6605<1 PROVED; exact N/P<=0.613 n<=22.
Uniform N/P<1 still OPEN. Next: weighted bound on high-ratio (large d_a-d_r,
small |c_r|-|c_a|) edges, or prove N/P monotone-below-limit.



EDGE-RATIO ATTACK (2026-08-22, PR #5452 followup commit). Pushed on uniform N/P<1:
 - N/P = E_omega[ratio_e], omega ~ 2s(r-a)^2(r+a), ratio_e = 2(d_a-d_r+1)/(r-a).
 - 1-LIPSCHITZ LEMMA (verified all lam n<=16, max jump exactly 1, Lean-able):
   |D(u+1)-D(u)|<=1 => d_a-d_r<=r-a => per-edge ratio_e <= 2+2/(r-a) <= 4
   (explains observed max ratio 4 at r-a=1).
 - WEIGHT-SUPPRESSION ROUTE REFUTED (scope-(a)): omega-weight concentrates on
   DISTANT moves (|c_a-c_b|>=4 -> 0.88), ~15% weight persists on ratio_e>=1.
   N/P<1 is NOT worst-case (per-edge ratio hits 4); it is an AVERAGING phenomenon
   (omega up-weights large-(r-a) low-ratio edges; typical bulk diagonal profile
   flat, d_a-d_r << r-a in the bulk).
CONSEQUENCE: uniform N/P<1 needs EFFECTIVE error-controlled limit-shape estimates
(Berry-Esseen-grade: M_1 >= kappa n^{5/2} - C n^2, explicit kappa>0,C, + finite
check), NOT elementary per-edge / weight-concentration. Asymptotic N/P->0.6605<1
already proved; only the effective error term is missing.
STATUS: elementary/combinatorial routes to uniform N/P<1 exhausted+refuted;
remaining path is a quantitative 2nd-order Kerov CLT (effective error). Honest
localisation. M_1>0 exact n<=50, kappa>0 derived, all-n reduced+localised. OPEN.



EFFECTIVE-CLT PROJECT (2026-08-22, PR #5466): plan persisted + sub-result (1) CLOSED.
Sub-result (1) outcome (better than planned): the Lambda*-part of Sum_h is
omega3-orthogonal. Sum_h = p2sharp_sym + T, p2sharp_sym in Lambda* (shifted power
sum), T = Sum_box(i+j) - n (non-Lambda* co-content). EXACTLY (n<=11):
  Cov(p2sharp_sym, omega3) = 0  =>  M_1 = Cov(Sum_h, omega3) = Cov(T, omega3).
Provable reason: p2sharp_sym is Lambda*-degree 2 (Sigma_2, n^2, n) and
Cov(Sigma_2,Sigma_3)=0 (= exact Cov(R_3,R_4)=0; omega3=Sigma_3/3). No genus
correction. Proves PR #5366 antidiagonal reformulation M_1=Cov(Sum(i+j),Sum c^2)
EXACT. Effective bound now needs ONLY non-Lambda* T (no Lambda* contamination).
Sniady genus (arxiv-math-0411647 4.5) does NOT reach T - it only re-derives
Lambda* x Lambda* covariances (already exact).
REMAINING (sub-result 2): effective bound Cov(T,omega3) >= kappa n^{5/2} - C n^2,
T,omega3 both additive box statistics. Fulman 3 exact 2nd-moment / IO field 2nd
order. Gap OPEN. Workplan: docs/workplans/2026-08-22-M1-effective-CLT-project.md



SUB-RESULT (2) REFRAMED to ONE-SIDED (2026-08-22, PR #5466). Exact kappa_n vs
kappa=128/(225 pi^2): kappa_n < kappa for n<=12, kappa_n > kappa for EVERY
13<=n<=46 (crossing n_0=13). Gap kappa_n-kappa positive, peaks ~0.001556 at n=32,
declines gently (~0.00147 at n=46), far from recrossing 0. So:
  M_1>0 all-n <= (a) exact M_1>0 for n<=12 [DONE] AND (b) kappa_n>=kappa for n>=13.
(b) is ONE-SIDED: Cov(T,omega3) >= kappa n^{5/2}, i.e. the SIGN of the leading
correction (kappa_n -> kappa FROM ABOVE), NOT an explicit constant C. Weaker
demand on the 2nd-order Kerov CLT than a two-sided bound.
REMAINING NUB (b1): prove the correction Cov(T,omega3)-kappa n^{5/2} >= 0 for large
n (its sign). Empirically correction ~ +A n^{~2.35}, A>0 (slowly-varying). This is
a genuine 2nd-order Kerov-CLT sign computation - substantial standalone analysis;
no slick proof found. (b2): no dip on 13<=n<N_0 (exact, have to 46).
STATUS: gap content now = ONE sign of ONE correction term. kappa>0 derived; M_1>0
exact n<=46; Lambda* part proved orthogonal; reduced to one-sided sign. OPEN.



RETRACTION + EXTEND + SIGN-RECAST (2026-08-22, PR #5466).
RETRACTED sub-result (1): the 'Lambda*-peeling reduction M_1=Cov(T,omega3)' was
VACUOUS. Exact n<=12: p2sharp_sym == 0 IDENTICALLY (transpose-antisym
p2sharp(lam)=-p2sharp(lam')) and T == Sum_h identically. So Cov(p2sharp_sym,omega3)=0
is the zero function's covariance, and M_1=Cov(T,omega3) is the definition - NO
reduction. Caught before merge (PR #5466 open). Genuine residue: co-content
identity Sum_h=Sum(i+j)-n (=PR #5366 reformulation, an identity). Lambda*-peeling
gives NOTHING (Sum_h transpose-even _|_ Sigma_2 transpose-odd; M_1=Cov(Sum_h,Sigma_3)
even x even unchanged).
UNAFFECTED (stand): kappa=128/(225 pi^2) derivation; one-sided kappa_n>=kappa
reframing (both about M_1 VALUES).
EXTEND: kappa_n > kappa verified exactly for ALL 13<=n<=60 (crossing n_0=13),
correction +, peak 0.001556 at n=32, 0.001381 at n=60, far from 0.
SIGN (b1) recast, NOT proved: via real Sum_h=SumD2+Sum|c| (PR #5452),
kappa_n-kappa=(N-deficit)-(P-deficit); both P_n/n^2.5,N_n/n^2.5 rise from below;
kappa_n>kappa BECAUSE N (diag-length-spread cov) converges to VKLS limit SLOWER
than P (|c|-spread cov). So one-sided sign <=> 2nd-order RATE comparison 'N lags
P'. Concrete target; open 2nd-order-CLT statement.
STATUS: M_1>0 exact n<=60; kappa>0 derived; reduced to one-sided kappa_n>=kappa
<=> 'N lags P'. OPEN. (Sub-result 1 was a dead end, honestly retracted.)



DEFICIT-RATE MECHANISM (2026-08-22, PR #5489, follow-up to merged #5466).
Characterizes the one-sided sign: kappa_n-kappa = dN-dP, dP=P_lead-p_n>=0,
dN=N_lead-nu_n>=0 (both P_n/n^2.5,N_n/n^2.5 -> limits 0.169765,0.112125 from
below). kappa_n>=kappa <=> dN>=dP ('N lags P'). Verified dN>dP for ALL 13<=n<=42;
dN/dP rises monotonically 0.82(n4)->1.0 at n=13 crossing->1.17(n42).
HONEST: dN-dP = kappa_n-kappa IDENTICALLY => re-description of the sign, NOT new
logical content. Genuine proof still needs 2nd-order VKLS deficit coeffs c_P,c_N
and c_N>c_P - not done. Sign attempt ceiling reached.
INFRA NOTE: #5466 merged (2b2f0838). Caught a scary-looking working-tree state
(80 phantom 'changes') = stale working tree after the merge agent rebased the
shared branch out from under the main checkout; git reset --hard HEAD synced it,
no data lost. Deficit probe put on independent branch to avoid the collision.



SIGN ATTEMPT -> HONEST WALL (2026-08-22, PR #5489). Tried to prove kappa_n>=kappa
(n>=13) by pinning the 2nd-order coefficient. Three diagnostics:
 1. deficit 'N lags P' = re-description (dN-dP = kappa_n-kappa identically);
 2. fit kappa_n-kappa=sum a_j n^{-j/2} UNSTABLE (a_1: 0.010->0.65->-3.6 with J;
    mixed signs) => NOT clean bulk n^{-1/2};
 3. kappa_n-kappa PEAKS at n~32 then declines slowly; local exponent unstable at
    n<=60 => not yet asymptotic.
CONCLUSION: empirically kappa_n>kappa for ALL 13<=n<=60 (M_1>0 not in doubt), but
the PROOF is out of numerical reach AND not a bulk 2nd-order-CLT statement - the
correction is likely EDGE-sensitive (Tracy-Widom ~n^{-1/6..-1/3}), needing edge
asymptotics of Cov(Sum_h,omega3). Genuine wall for the current toolkit; honest
negative. Established results unaffected (kappa>0, M_1=Cov(Sum_h,omega3), n<=60).
FRONTIER (precise): prove kappa_n>=kappa (n>=13) via EDGE-sensitive 2nd-order
asymptotics (Tracy-Widom corrections), not bulk Kerov CLT. Audit:
docs/audits/2026-08-22-covariance-kernel-M1-sign-attempt-wall.md.



CORRECTION + EXTEND (2026-08-23, PR #5506).
(1) M_1>0 exact for 60<n<=67 (kappa_n>kappa all 13<=n<=67; crossing n_0=13; gap
declining, no recrossing).
(2) CORRECTS the #5489 'edge-sensitive' claim. Scaling: edge enters Sum_h via
lambda_1^2 (dSum_h~n^{2/3} chi) and omega3 via extreme content ~2sqrt(n)
(dOmega3~4n*n^{1/6} chi=n^{7/6} chi), same chi => Cov_edge~n^{11/6}, rel order
n^{-2/3}. Bulk 2nd-order ~n^{-1/2}. -2/3<-1/2 => EDGE SUBLEADING, correction is
BULK-dominated, NOT Tracy-Widom. Sign proof = bulk 2nd-order Kerov-CLT (more
tractable). RETRACTS 'edge-sensitive wall'.
HONEST: kappa_n-kappa>0 exact; 2-term fit a1~0.013-0.015>0 BUT 3-term collapses a1
to ~0.002 (deeply pre-asymptotic, peak n~32). NO specific a1/exponent claimed.
FRONTIER (corrected): prove bulk n^{-1/2} coeff of kappa_n >=0 (c_N>c_P), bulk not
edge. Open. Audit: docs/audits/2026-08-23-covariance-kernel-M1-correction-bulk-not-edge.md



LEAN + HONEST WALK-BACK (2026-08-23, PR #5506).
(1) M_1>0 LEAN-PROVED finite base: m1_pos_of_le_seven (0 < scaledCov k Sum_h contentSq,
    3<=k<=7, decide) in YoungDiagramKernel.lean, verified lean-direct exit 0. Answers
    'M_1>0 symbolic/Lean?': finite cases YES (now formalized), all-n NO (open).
(2) WALK BACK my own 'bulk-dominated' claim (and last session's 'edge-sensitive').
    Measured effective exponent of kappa_n-kappa at high n (past peak ~32): beta~0.25
    ->0.36 over n=40..64, STILL RISING, not converged; no (kappa_n-kappa)*n^beta flat
    for beta in {1/2,2/3,1}. Correction ORDER UNDETERMINED at n<=67; edge (n^{-2/3})
    vs bulk (n^{-1/2}) CANNOT be ranked. Only defensible: edge contributes at n^{-2/3}.
    Both prior characterizations were over-claims.
SOLID: M_1>0 exact n<=67; Lean-proved k<=7; kappa>0 derived; kappa_n>kappa emp n<=67.
FRONTIER: prove kappa_n>=kappa asymptotically - 2nd-order Plancherel fluctuation of
UNDETERMINED order (bulk and edge both plausible). Open.

2026-08-23 (PR #5518, branch claude/m1-lean-base-k8): Lean finite base of M_1>0 extended k<=7 -> k<=8 (m1_pos_of_le_seven -> m1_pos_of_le_eight; interval_cases k <;> decide; whole-file lean-direct EXIT=0). Also fixed a stale over-claim: the merged #5506 docstring still called the kappa_n->kappa sign 'bulk second-order (edge subleading n^-2/3)'; walked back to 'order UNDETERMINED, edge vs bulk unranked' to match the corrected audit. Asymptotic sign kappa_n>=kappa (n>=13) stays OPEN. scope-(a); no fit; L2 unchanged.

2026-08-23 FRONTIER SHARPENED (PR #5518): the Sniady genus expansion IS applicable to M_1's kappa_n-kappa sign, correcting a scope trap. It was eliminated (route #11, 2026-07-25 A5) only for the DIM-TILT kernel Cov(dim,omega3) because dim notin A. But M_1=Cov(Sigma_h,omega3) has BOTH legs polynomial-on-Young-diagrams (omega3=R4+R2; Sigma_h=1/2(p2+p2')), so the dim-obstruction is absent. Concrete route (NOT executed, no order/sign claimed): genus-0 = IO CLT = kappa*n^5/2 (derived); genus-1 via Sniady math/0411647 sec 4.4 explicit 2nd-order R_k expansion -> order+sign. Blocker: sec 4.4 OCR garbled; needs clean PDF statement composed with the R_k forms of Sigma_h, omega3. Next honest step for the frontier.

2026-08-23 ENV BLOCKER on the genus-1 execution: the clean Sniady math/0411647 sec 4.4 formula (explicit 2nd-order R_k expansion) is NOT obtainable in this sandbox — arxiv.org firewalled (403 via proxy); local library OCR of sec 4.4 is math-garbled; pypdf+pdfminer both broken (cryptography/_cffi_backend pyo3 panic container-wide); custom zlib extraction won't help (2004 LaTeX PDF stores math in cmsy/cmmi custom font encodings -> glyph codes not Unicode, which is WHY the OCR is garbled). Refused to reconstruct the formula from garbled OCR/memory (confabulation). NEXT SESSION with working egress or a clean secondary source (e.g. Dolega-Sniady 1704.02352, or Ivanov-Olshanski explicit covariance tables) should: (1) get the explicit genus-1 R_k correction, (2) compose with Sigma_h=1/2(p2+p2') and omega3=R4+R2 in free cumulants, (3) read off order+sign of kappa_n-kappa. That is the concrete unblock for the M_1>0 all-n frontier.

2026-08-28 REVISED WORKPLAN (PR #5882, docs/workplans/2026-08-28-M1-arc-revised-workplan.md). CORRECTION to the 2026-08-23 tail: the 'env-blocker (PDF tooling broken)' append is RETRACTED — pymupdf extracts the in-repo Sniady source cleanly (no arxiv egress needed); Th 4.13/4.14 transcribed; target pinned to Cov(Sigma_h, R4). NEW general-n Lean substrate landed (siblings): PlancherelSnData for all n, secondMomentKernel_eq_zero for all k, RSK_substrate_axiom discharged — but FIRST-MOMENT infra only, no covariance/second-order. Open nub UNCHANGED: sign of the genus-1 second-order correction to Cov(Sigma_h,R4) (=kappa_n-kappa>=0, n>=13). Four tracks: A(primary)=execute genus-1 sign [A2 crux, HIGH risk]; B(cheap parallel)=extend exact kappa_n past n<=67 to guide A's order; C(longer Lean)=extend substrate to a covariance/second-moment statement; D(fallback)=Fulman finite-n Stein bound. Recommend A+B parallel, D fallback if A2 walls; honest fallback status = 'asymptotic kappa>0 derived + exact-finite-check n<=67'.

2026-08-28 TRACK A + D CONVERGENT FINDINGS (PR #5882 Track A, #5887 Track D). Two independent routes to the asymptotic sign kappa_n>=kappa now have PROVED obstructions: (A) Sniady character genus expansion Thm 4.14 does NOT apply — exact transition-measure free-cumulant probe shows Sigma_h=1/2(p2+p2') is NOT a free-cumulant polynomial (transpose-invariant but ODD leading degree, E_Planch[Sigma_h]~n^1.5; every transpose-invariant R-poly has EVEN degree). Its antisym partner 1/2(p2-p2')=1/2 R3 IS in A. So Sigma_h notin A; Thm 4.14 expands A-elements only. ALSO fixed a x3 normalisation error: R4=3*omega3-n (matches Lean r4Value), so omega3=(R4+R2)/3 and M1=(1/3)Cov(Sigma_h,R4) — sign unchanged. (D) Fulman Stein/exchangeable-pair ERROR TERM walls (no N0): a Berry-Esseen MAGNITUDE bound cannot certify a one-sided SIGN; Fulman's statistic is W~Sigma_c not Sigma_h; counterfactual constant ~1e17. Both tracks converge: Sigma_h being outside the char/eigenfunction algebra is the crux. ONLY remaining live route for the asymptotic sign = shape-field / linear-statistic SECOND-ORDER theory (Dolega-Feray Gaussian fluctuations of Young diagrams, 1402.4615/1704.02352), where Sigma_h is a legitimate test function. Track B (exact kappa_n) extending past n<=67, still >kappa. qou-k5r5 OPEN.

2026-08-28 SHAPE-FIELD RECON (the 3rd tool): Dolega-Feray 1402.4615 / Dolega-Sniady 1704.02352 give the CLT LIMIT = kappa (already have it), NOT the finite-n rate kappa_n-kappa; also Jack-character observables (Sigma_h notin A again). So ALL THREE standard tools are now pruned with distinct reasons: (1) Sniady genus Thm 4.14 obstructed by Sigma_h notin A; (2) Fulman Stein = marginal Berry-Esseen, not a covariance sign; (3) Dolega-Feray = limit not rate. CONSOLIDATED VERDICT: the sign of kappa_n-kappa (n>=13) is a bespoke rate-of-convergence result (finite-n correction to a limiting Plancherel covariance with near-cancelling P,N ~n^5/2), not closeable off-the-shelf — matches this bean's original assessment. Defensible arc status: kappa>0 DERIVED + M1>0 exact n<=67 (Track B extending) + Lean k<=8. All-n sign = explicitly-scoped OPEN rate problem. qou-k5r5 OPEN.

TRACK D (2026-08-28, PR #5887, branch claude/m1-fulman-stein-finite-n-2026-08-28).
Tested: can Fulman's Stein/exchangeable-pair ERROR-TERM machinery (arxiv-math-0305423,
Thm 1.2's 40.1 n^-1/4; Thm 1.3 assembled from exact Prop 4.5 + Prop 4.6) bound the
second-order correction kappa_n - kappa from BELOW by 0 for n>=13? VERDICT: NO, Track D
WALLS (scope-(a) negative). Three reasons: (1) TYPE MISMATCH, fatal & n-independent -
Thm 1.2/1.3 bound a KOLMOGOROV DISTANCE of the MARGINAL W; a magnitude bound
|kappa_n-kappa|<=B_n is two-sided and can NEVER certify the ONE-SIDED sign
kappa_n-kappa>=0 (it gives only kappa_n >= kappa - B_n < kappa). No N0 exists; N0=inf.
(2) WRONG STATISTIC: W ~ Sum c in Lambda*; M_1 pairs omega3 with Sum h, which is NOT in
Lambda* / not a J-eigenfunction (the wall). Fulman's Prop 4.3/4.5 exact formulas are for
W, none reaches a covariance with Sum h. (3) VACUOUS: bound/margin ~1.6e5 at n0=13
(exact margin kappa_n-kappa = 1.3e-4..1.5e-3 on [13,30], SHRINKS to 0); counterfactual
N0 (ignoring 1,2) ~4.6e17 (Thm 1.2), ~6.8e8 (conj C=40.1 n^-1/2) - all astronomically
past 13. REUSABLE: the exact exchangeable-pair COVARIANCE IDENTITY (Cov=1/(2(1-beta))*
E[Df Dg]) is already on main and is circular for the all-n sign. NOT reusable: the error
term. The finite-n sign must come from a second-order-cumulant (Sniady genus-1) computation,
NOT Fulman's first-order Berry-Esseen. Probe: computations/deltalambda/
wlambda_covariance_epic_M1_fulman_stein_finite_n_bound.py (exit 0, exact Fraction/mpmath,
no float64, nothing wired, no c_k). Audit: docs/audits/2026-08-28-covariance-kernel-M1-
fulman-stein-finite-n.md. Gap stays OPEN. Not laundered.

2026-08-28 SOFTER ROUTE (PR #5896): M1>0 is NOT a delicate rate problem. Fulman N/P ~ 0.66 << 1 (margin 0.37) — reframes the 'delicate cancellation' framing (WRONG: terms don't nearly cancel). Cauchy-Schwarz (rho_N<=1, free) + sig_W cancels gives AIRTIGHT sufficient condition (CS): sig(SumD2)/sig(Sum|c|) < rho(Sum|c|,omega3) => M1>0. Measured exact all 4<=n<=32: sig_D/sig_A~0.67, rho_P~0.98, (CS) margin ~0.30 NON-VANISHING. This needs only CRUDE bounds (Var(SumD2)<Var(Sum|c|); lower bound on corr(Sum|c|,omega3)) — far softer than the sharp rate kappa_n>=kappa (which all 3 lit tools fail to deliver). HONEST: a REDUCTION not a proof; (CS) verified n<=32 not all-n; |c|,D2 non-A so still Plancherel asymptotics but crude not sharp. This is the most promising open route. qou-k5r5 OPEN.

2026-08-28 CLOSING MOVE DERIVED (PR #5901): the (CS) sufficient condition holds at LEADING ORDER, 52% margin. Via IO Kerov CLT (the field that gave kappa=Omega_hat_3/3), (CS) reduces to the scalar inequality V_D = sum_{k>=3 odd}(Omega_hat_k - A_hat_k)^2/k < A_hat_3^2/3, where A_hat_k,Omega_hat_k are Chebyshev coeffs of |x| and VKLS Omega. Computed 40dps no-float64: V_D=0.04160 < 0.08646, RELATIVE MARGIN 52%. VALIDATED: rho(Sum|c|,omega3)->0.9798 (exact data ~0.98), sig(SumD2)/sig(Sum|c|)->0.6796 (exact data ~0.67), Omega_hat_3=128/(75pi^2) to 1e-42, kappa reproduced. So M1>0 for all n>=N0 is DERIVED via the soft route (NOT the intractable rate; NOT a fit — 52% margin matches exact data). REMAINING GAP now CRUDE: a finite-n error bound with 52% headroom connecting asymptotic to the exact (CS) check (holds 4<=n<=32) + M1>0 exact to n=78. Rigorous modulo published IO CLT + crude bound. This is the first route with the leading order PROVED and only a soft large-headroom remainder. qou-k5r5 OPEN but materially advanced.

## 2026-08-28 — descent-DPP variance-rate reduction (PR #5924)

The one open (CS) step (effective variance bound for the non-A statistics Sum|c|,
SumD2) is REMOVED as an obstruction. Reduction: the descent set D(lam)={lam_i-i} is
a determinantal point process (BOO discrete Bessel kernel, library/arxiv-math-9905032v2
Thm 2, ingested this session PR #5922). The rotated-profile height h(u)=#{d in D: d>=u}
telescopes every content statistic into a LINEAR statistic of the DPP occupation
(weights = discrete antiderivatives). Projection-kernel Cov is exact and diagonal-free;
fixed-n by Gaussian conditioning on N.

Established (mpmath 40dps, NO float64; wlambda_covariance_epic_M1_descent_dpp_variance_rate.py):
  - EXACT poissonized cross-check: DPP vs Poisson-summed combinatorial agree rel~1e-5
    (Var Sum|c|, Var Sum c^2, Cov). Validates kernel + weight dictionary.
  - de-poiss vs exact Plancherel(n) n=16,22,30: ~0.5% (leading-order conditioning).
  - rho_P(n) -> merged #5901 IO constant 0.979796 at MEASURED rate a~1 (log-log, no fit).

Consequence: the (CS) closure needs only a crude a>0 (leading margin 0.30); measured a~1.
The variance asymptotics are exactly BOO's rigorous Airy-edge/sine-bulk kernel asymptotics
-- the tool the polynomial-observable algebra A could not supply (DPP linear stats escape A).
Still OPEN: turn measured a~1 into a cited BOO edge/bulk bound (in-corpus, tractable);
sigma_D (SumD2 quadratic) needs the DPP 4-point (mechanical, deferred).
Audit: docs/audits/2026-08-28-covariance-kernel-M1-descent-dpp-variance-rate.md

## 2026-08-28 (cont) — sigma_D leg + BOO bound structure (PR #5924)

(b) sigma_D leg EXACT (wlambda_covariance_epic_M1_sigmaD_leg_rate.py): SumD2 quadratic,
sig_D/sig_A -> 0.679610, (CS) margin -> 0.300187. HONEST: damped-OSCILLATORY approach (not a
pointwise power law -- corrected an initial over-claim of a clean rate); ENVELOPE of |dev|
decays ~n^-0.9 (0.076@4 -> 0.024@9 -> 0.012@21 -> 0.0079@38), matching Poisson-smoothed rho_P
~n^-1. margin>0 all 4<=n<=40, min 0.20025@n=4.

(a) BOO edge/bulk bound structure (audit section): Var=1/2 Sum(g(x)-g(y))^2 J^2 = bulk (Thm 3
discrete sine kernel, O(theta^-1/2) corr) + edge (Baik-Deift-Johansson Airy, theta^1/6 window,
subleading) -> crude |Var/n^5/2 - V| <= C n^-1/2, conservative vs measured ~n^-1, traps the
oscillation below 0.30 for n>=N0. Ingredients are published BOO estimates (PR #5922), not new
theorems -- the one remaining analytic step, fully scoped.

STATE: both #5924 next-steps done. Remaining to CLOSE qou-k5r5: write the BOO bulk-sine +
Airy-edge + de-poissonization estimate out rigorously (all ingredients in-corpus).

## 2026-08-29 — rigorous finite-n bound written out (PR #5929)

The last open (CS) step written as a rigorous finite-n bound + its algebraic core proved in Lean.

Audit docs/audits/2026-08-29-covariance-kernel-M1-rigorous-finite-n-bound.md:
descent-DPP variance split tail (Olver, ~1e-8) + bulk (BOO Thm 3 sine kernel +
Euler-Maclaurin) + Airy sliver (BDJ, theta^-1/3 of domain), plus BOO/Costin-Lebowitz
de-poissonization. Weight-specific power-counting (new): |u|-kink weight of Sum|c|
costs half an order => V_A ~ n^-1/2 is the bottleneck (smooth V_S2, Cov ~ n^-1).
Gives |F_n-F_inf| <= C n^-1/2 => margin m(n) >= 0.30 - C n^-1/2 > 0 for n>=N0,
3<=n<N0 by exact table (M_1>0 to n=78). Exponents validated numerically (exit 0,
NO float64): Var(Sum c^2)/theta^3 and Cov diff-slope 1.00; tail 1e-8;
Var(Sum|c|)/theta^2 converging consistent with n^-1/2.

Lean YoungDiagramKernelCSMargin.lean (sorry-free, lean-direct exit 0):
m1_pos_of_cs_margin derives M_1>0 from the (CS) inputs as explicit hypotheses by
real algebra (non-degenerate §3b-cond); m1_pos_all_of_base_and_tail the composition
skeleton. Generic ordered comm ring, no R.

REMAINING (the one mechanical step): pin the explicit constant C (=> explicit N0,
check N0<=78) by tracking constants through Olver/Debye/BDJ + the Euler-Maclaurin
kink term. Real analysis, no new idea. Gap OPEN until then.

## 2026-08-29 — constant-C step scoped (branch claude/m1-constant-C-N0-2026-08-29)

Target for N0<=79 (exact M_1>0 covers n<=78): C <= m_inf*sqrt(79) = 2.668.
Empirical envelope C_emp(n>=6)=0.087, decreasing (deviation decays faster than
n^-1/2) => 13-30x headroom; N0<=79 very reachable.

Rigorous C reduces to explicit published constants: tail (Olver DLMF 10.41, ~1e-8),
sine-series truncation (Sum 1/k^5), de-poissonization (BOO O(1/n)), ratio propagation
(Lipschitz). ONE binding piece NOT pinned: the Olver/Debye bulk-remainder constant
C_A for Var(Sum|c|) -- carry the explicit theta^-1/2 remainder through the x^2-weighted
bulk sum (multi-page hard analysis).

Finite part (n<=78) certified exact. A VERIFIED explicit C NOT produced this session --
declined to launder the empirical 0.087 as rigorous. Gap reduced to that one constant.
NEXT: the Olver/Debye C_A computation, or accept the honest 'rigorous modulo one explicit
constant' resting point.

## 2026-08-29 — Debye C_A investigation + verdict (branch claude/m1-debye-CA-investigation)

Large-theta investigation (exact Bessel sums, no partitions): V_A/theta^2 -> 0.810557 at
exponent a~1.18 (NOT theta^-1/2), C_A^emp=0.0076; rho_P -> rho_inf at theta^-1 (const 0.13);
fixed-n margin const ~0.087. True convergence theta^-1..theta^-1.18, far faster than the
theta^-1/2 worst case; headroom vs C<=2.668 target is 30-300x.

VERDICT (recommended): ACCEPT 'rigorous modulo one explicit constant'. Closing outright would
succeed (Olver bounds sharp, true coefficient 30-300x under target) but the VERIFIED C needs the
multi-page Olver/Debye remainder -> x^2-weighted bulk sum -> ratio propagation, too error-prone to
assert rigorous in-session without an independent check. A wrong rigorous C is worse than honest open.

RESTING STATE: M_1>0 proved for n<=78 (exact), reduced for n>78 to one explicit constant
(Olver/Debye C_A) in a validated three-region+de-poissonization scheme with 30-300x measured
headroom. Strong publishable state. Close-outright is a well-scoped follow-on, not a new idea.

## 2026-08-29 — Debye constant-tracking step 1: KINK CANCELS (branch claude/m1-debye-constant-tracking)

Measured V_A/theta^2 = Var(Sum|c|)/theta^2 expansion (exact Bessel sums, dps 60):
v_A=0.810568 monotone from below; c_{1/2} (theta^-1/2 kink) sign-unstable at noise floor
({-0.00048,+0.0010}, |.|<0.001) = consistent with ZERO; c_1 (theta^-1) ~ -0.066 stable.

=> the |u|-kink term VANISHES; rigorous rate is theta^-1 (SMOOTH Euler-Maclaurin), not the
feared theta^-1/2. Candidate rigorous reason: Plancherel transpose-invariant => content law
symmetric u<->-u => Sum|c| EVEN => integer-power expansion (half-power cancels).

Closure DE-RISKED: 'modulo one HARD constant' -> 'modulo one EASY constant' (smooth theta^-1,
coeff ~0.066, 30-300x headroom). NOT yet a verified C. Remaining: (i) write transpose-symmetry
c_{1/2}=0 proof; (ii) explicit theta^-1 Euler-Maclaurin constant + ratio propagation. Did not
fake a rigorous number.

2026-08-29 (branch m1-k5r5-bessel-rate-citation): the one open step is precisely NAMED and the
corpus checked at the source. Status:
  - Leading margin m_inf = rho_P - sqrt(V_D/V_A) = 2sqrt6/5 - 0.67961 = 0.300186 > 0. Constants
    exact (V_A=8/(9pi^2), Var(w3) lead 1/3, P=8/(15pi), rho_P=2sqrt6/5; V_D=0.0415975). PR #5969.
  - Exact finite-n: m(n) > 0 for ALL 4<=n<=40 (exact Fraction), min m(4)=0.20025, oscillates around
    0.30019 with DECREASING amplitude (~0.008 at n=40). Not monotone -> exact-small-n + leading-large-n
    does not trivially cover all n.
  - The one open step: effective variance bound |Var_n(Sum g eta)/n^2 - V_g| <= C_g n^{-a}, a>0.
  - PRIMARY SOURCE (corpus-grep path 5): BOO Thm 3 (arxiv-math-9905032v2 sec-006) states the bulk
    discrete-Bessel -> discrete-sine kernel convergence as a RATE-FREE LIMIT (no error term). Whole-
    library grep for olver/uniform-asymptotic/error-term/rate finds NO citable kernel rate; Fulman
    Stein (0305423) is a marginal Berry-Esseen (ruled out); Sniady-Dolega (1402.4615) needs polynomial
    statistics (Sum h / Sum|c| are not). So the "Olver-Bessel wall" is a GENUINE external-citation gap,
    not an in-corpus oversight.
  - Missing citation named: error-bounded discrete-Bessel->sine kernel convergence (Olver uniform
    asymptotics of J_x(2sqrt th) in the bulk, or Deift-Its RH), |J-S| <= c th^{-b} on the bulk + the
    classical super-exp Bessel tail past the edge. Tail half is Olver-free; bulk half needs the lemma.
  - Audit: docs/audits/2026-08-29-covariance-kernel-M1-k5r5-the-missing-citation-is-a-kernel-rate.md.
  Gap OPEN. Honest: morally certain (leading 0.30 + exact positivity n<=40 + damped tail) but a
  measured C is not a proved C; no fake closure.

2026-08-29 (tail half + ingested lit): owner ingested 10 kernel-rate papers (commit f45f79c8 -> library/). TAIL half of the effective variance bound is now Olver-FREE + CITABLE: Johansson 2001 (arxiv-math-9906120v3) Lemma 3.9 gives explicit super-exp Bessel decay past the edge; poly weight x super-exp kernel => TAIL(K) <= poly(theta) exp(-K^{3/2}/4) = o(theta^-A). Measured (tail_bulk_split.py, no float64): tail/V_A drops 1.8e-2 -> 4e-20 across K=1..10, super-exp, below the theta^-1 remainder by K=3-4. De-poissonization citable too (Johansson Lemma 3.8, C/N^2). Bulk sine-kernel RATE machinery now in-corpus: Gorbunov sm10137 (Berry-Esseen for Bessel-kernel DPP via Kac-Akhiezer + Borodin-Okounkov Toeplitz), continuous analogue of the discrete Toeplitz case; needs application to the discrete Plancherel descent variance (an analytic step, not a missing citation). Wall reduced from 'no rate in corpus' to 'bulk application step'. Audit: docs/audits/2026-08-29-covariance-kernel-M1-k5r5-tail-half-and-ingested-kernel-rate-lit.md. Gap OPEN, materially narrowed.

2026-08-29 (formalize-first, cited): added the 4 literature citations to references.ts (borodin-okounkov-olshanski2000, johansson2001, gorbunov2024; ivanov-olshanski2003 already there) and a Lean carrier M1DescentDPPConvergence.lean (sorry-free, lean-direct exit 0, #print axioms clean). class DescentDPPMarginConvergence (Prop, content-bearing Filter.Tendsto to the exact limits + strict leading gap, CITED, NO instance) + sorry-free theorems cs_margin_eventually and m1_pos_eventually deriving eventual M_1>0 from the assumed convergence via the CS core. Honest: axiomatizing the cited results is assuming them; the bulk-rate step stays open; eventual->all-n closed by gorbunov2024 explicit threshold + exact table via the existing m1_pos_all_of_base_and_tail. NOT a proof. Gap OPEN.

2026-08-29 (leading margin PROVED): discharged the ONE class field not gated on the bulk rate. leading_margin_pos = (sqrt(V_D/V_A) < 2sqrt6/5) = (V_D < 64/(75pi^2)) after pi cancels. V_D (no closed form) bounded RIGOROUSLY: certified mp.iv interval partial sum k=3..999 + explicit elementary tail majorant R(K)<=a^2/(2K^4)+b^2/(3K^6), R(999)<=1.05e-11 => V_D < 0.0415974806 < 0.0864607, margin 0.0449. Upgrades m_inf>0 from measured to PROVED. Lean leading_margin_pos_of_VD_ceiling (sorry-free, axiom-clean) reduces the field to the certified ceiling. 1 of 3 class fields closed with rigor; only the two bulk-rate Tendsto remain open. Probe: wlambda_covariance_epic_M1_VD_ceiling_rigorous.py.

2026-08-29 (2nd lit batch + bulk-rate probe): owner uploaded 23 papers (ae1c51be). Pointwise bulk kernel probe = HONEST NEGATIVE: |J-S| does not decay cleanly (oscillatory + density rounding), so the bulk rate must be argued at the INTEGRATED/determinant level (variance theta^{-1} already measured). Batch routing: Tracy-Widom edge kernels (Airy hep-th-9211141, Bessel hep-th-9304063) give the Painleve/Fredholm-determinant METHOD but for the EDGE/hard-edge, not the BULK; chiral-RMT Dirac cluster (Verbaarschot etc) is hard-edge Bessel in QCD; several off-topic (stars, magnetars, quantum repeater, epidemic, theorem-proving). NEED LIT answer: YES for the bulk specifically -- most direct missing citation is Widom's discrete-sine Toeplitz asymptotics (BOO Rem 1.6 ref [41]) or Tracy-Widom sine-kernel hep-th/9303139 (NOT uploaded); or DERIVE via Gorbunov Kac-Akhiezer + Borodin-Okounkov applied to the discrete descent variance. Audit: docs/audits/2026-08-29-covariance-kernel-M1-k5r5-second-lit-batch-routing.md. Gap OPEN.

2026-08-29 (CORRECTION + precise ref): I gave a WRONG arxiv number earlier -- hep-th/9303139 is A.Morozov 'Integrability and Matrix Models' (matrix-model integrability review), NOT Tracy-Widom sine kernel. Ingested (library/arxiv-hep-th-9303139v2) but tangential to k5r5 (integrable-systems background; zero Toeplitz/Fredholm/BO/Szego). Corrected the routing audit. PRIMARY-SOURCE precise ref for the bulk rate, read off BOO's own bibliography [41]: Widom, 'The strong Szego limit theorem for circular arcs', Indiana Univ. Math. J. 21 (1971) 271-283 -- the discrete-sine Toeplitz asymptotics BOO Rem 1.6 leans on. It is a 1971 pre-arxiv journal paper (not arxiv-fetchable). Correct TW sine-kernel = Commun. Math. Phys. 163 (1994) 33-72 (arxiv id NOT asserted -- firewalled, could not verify). Gap OPEN.

2026-08-29 (bulk-rate toolkit COMPLETE): owner uploaded Deift-Its-Krasovsky 'Toeplitz matrices ... Ising model' (1207.4990, CPAM 2013) -- the Toeplitz-determinant asymptotics WITH error terms (strong Szego + Fisher-Hartwig + Borodin-Okounkov). Toolkit now complete: BOO (descent DPP = Toeplitz), Gorbunov (Kac-Akhiezer continuous template), DIK (with-error engine), Johansson (tail+de-Poisson). KEY: the Plancherel/discrete-sine symbol is an ARC (jump = Fisher-Hartwig singularity) => the Toeplitz asymptotic carries an ALGEBRAIC n^-a remainder = the bulk rate (matches measured theta^-1). Derivation route scaffolded (formalize-first, 4 steps, each sourced). REMAINING open computation: write the Toeplitz symbol phi_g for Sum|c|/Sum c^2/SumD^2, extract Fisher-Hartwig data, run DIK/BO asymptotic for (a, C_g) -- the discrete analogue of Gorbunov's continuous computation, a real multi-step derivation, NOT faked. Added deift-its-krasovsky2012 to references.ts; cited in the Lean class bulk Tendsto field. Audit: docs/audits/2026-08-29-covariance-kernel-M1-k5r5-bulk-rate-toolkit-complete.md. Gap OPEN (route sourced; remaining step is a Fisher-Hartwig computation, not a citation).

2026-08-29 (derivation ATTEMPT -- honest terminus): read DIK 1207.4990 at source. CORRECTION of my own scaffold: the Plancherel edge is a MOVING SOFT EDGE (Airy, theta^1/6), i.e. DIK's DOUBLE-SCALING regime (Painleve II), NOT a fixed Fisher-Hartwig singularity. DIK sec11 p53 is LITERALLY the Plancherel Toeplitz determinant (Gessel phi_n) analyzed via Baik-Deift-Johansson double-scaling -- the exact object. So the rate derivation = the BDJ/DIK double-scaling RH analysis (research-grade); I will NOT fake it. Tried an edge-vs-bulk annulus decomposition to check if the theta^-1 remainder is edge-dominated -> HONEST NEGATIVE: edge annulus & deep bulk COMPENSATE, split does not isolate the theta^-1 origin (probe wlambda_covariance_epic_M1_edge_bulk_decomposition_probe.py). So I do NOT assert edge-dominance. Terminus: route precisely sourced (Gessel->BDJ/DIK sec11->PII/Airy->differentiate for variance rate); rigorous exponent+constant OPEN (BDJ paper JAMS 12(1999)1119, not in corpus; DIK sec11 references but doesn't restate the variance-level 2nd-order term). Audit: docs/audits/2026-08-29-covariance-kernel-M1-k5r5-derivation-attempt-double-scaling.md. Gap OPEN.

2026-08-29 (regime structure mapped; BDJ = edge): owner uploaded Baik-Deift-Johansson (math/9810105, JAMS 1999), Baik KPZ review (2206.14086), Baik-Rains (9910019). CRITICAL distinction: BDJ is the EDGE result (lambda_1 -> Tracy-Widom, theta^1/6), NOT the global linear-statistic (Kerov CLT) variance rate the (CS) margin needs. Regime structure now fully mapped: (1) leading V_A=8/pi^2 = IO Kerov CLT mode sum (cited); (2) qualitative Var-convergence = IO mode-wise moment convergence + a uniform high-mode tail argument for the non-smooth |x| (partly citable, one gap); (3) the RATE theta^-1 = 2nd s-derivative of the FULL Plancherel Toeplitz determinant asymptotic combining bulk (Szego/Widom-arc, DIK+Widom1971) + edge (BDJ/double-scaling, DIK sec11). The annulus probe honest-negative (regions compensate) confirms both contribute. TOOLKIT NOW COMPLETE (IO,BOO,Johansson,Gorbunov,DIK,BDJ,TW,Widom-ref) but NO single paper states the (CS) variance rate -- assembling it is original RH research, NOT faked. Added baik-deift-johansson1999/baik-rains2001/baik2022kpz to references.ts. Audit: docs/audits/2026-08-29-covariance-kernel-M1-k5r5-regime-structure-BDJ-is-the-edge.md. Gap OPEN.

2026-08-29 (research route, piece 1): owner chose to treat the bulk rate as a research problem. Piece 1 DONE: the classical DEBYE bulk asymptotic of J_x(2sqrt th) (Watson 1944 sec8.4 / DLMF 10.19.6) VERIFIED against exact besselj (debye_bulk_asymptotic_probe.py, no float64): rel err ~ theta^-1/2, exponent 0.51 at deepest bulk a=0.5. Confirms J -> discrete sine kernel with angle R=arccos(a/2) and the O(theta^-1/2) pointwise correction. This is a rigorous+cited+verified brick. Remaining: write J=S+E, variance = sine-part + 2*cross(S*E) + E^2; the cross term is oscillatory so summation-by-parts/stationary-phase gains one more theta^-1/2 -> net theta^-1 (measured tvok). That cancellation with explicit constant is the hard analysis, NOT done (would risk laundering). Audit: docs/audits/2026-08-29-covariance-kernel-M1-k5r5-research-piece1-debye-verified.md. Gap OPEN.

2026-08-29 (session tender-keller, branch m1-k5r5-bulk-rate-derivation): owner supplied two on-target papers (00231c40) — Charlier-Claeys 1409.0435 (arc/gap Toeplitz + sine-kernel Fredholm det, RH O(1/n) parametrix matching) and Corwin-Deift-Its 2201.05665 (Widom sine-kernel survey). Ingested + registered as charlier-claeys2015 / corwin-deift-its2022. PIECE 2 (rigorous brick): verified the Widom/CC arc-Toeplitz constant c=(1/12)ln2+3zeta'(-1)=-0.4385 against the actual finite-n determinant (Cholesky, NO float64); residual ~n^{-2} (even-symbol cancels the n^{-1} term). HONEST STATUS: these give the determinant-level TOOL + limit object + constant, now in-corpus/citable, but NOT the Plancherel linear-statistic variance rate (adjacent functional: gap-probability n^{-2} / sine-det O(1/y) vs variance theta^{-1}). Open piece unchanged: the bulk cross-term summation-by-parts/stationary-phase cancellation (the RH computation), now better-equipped. Not laundered. Audit: docs/audits/2026-08-29-covariance-kernel-M1-k5r5-charlier-claeys-widom-toeplitz.md

---

## 2026-08-30 — TRACK B EXECUTED: exact window 67 → 78, and the effective exponent turns

`computations/deltalambda/wlambda_covariance_epic_B1_kappa_window_extension.py`
+ witness, 5/5 assertions. Eleven new exact points, ~28 min of compute. Exact
`Fraction` throughout, comparison at 60 dps, no float64.

### The one-sided bound still holds, and the approach is from above

**All eleven `κ_n > κ`**, and `κ_n` is *strictly decreasing* across the whole new
window. So the reduction's premise — `κ_n` approaching its limit from above past
the `n₀ = 13` crossing — survives the extension.

| n | κ_n − κ | | n | κ_n − κ |
|---|---|---|---|---|
| 68 | 0.0012908539 | | 74 | 0.0012458061 |
| 69 | 0.0012825060 | | 75 | 0.0012387614 |
| 70 | 0.0012745731 | | 76 | 0.0012315753 |
| 71 | 0.0012670386 | | 77 | 0.0012242230 |
| 72 | 0.0012598181 | | 78 | 0.0012167299 |
| 73 | 0.0012527860 | | | |

### The finding: the effective exponent is NOT monotone

The workplan records *"measured effective exponent still rising, ≈0.25 → 0.36
over n = 40..64"*. Just past the old window it **turns**:

| stencil | α (from `κ_n − κ ~ C n^{−α}`) |
|---|---|
| 68..71 | 0.4313 |
| 71..74 | **0.4083 ← minimum** |
| 75..78 | 0.4575 |

Robust to stencil width — successive-pair, 4-wide and half-window secants all
put the minimum near **n = 71–72**. Not numerical noise: these are exact
rationals evaluated at 60 dps, so the local exponent carries ~50 correct digits.

### Why that constrains Track A

**A single power law gives a monotone effective exponent.** A genuine interior
minimum means the correction is a *sum of at least two terms of different order*
(or carries a log) at these `n`. So:

* the earlier "0.25 → 0.36 and rising" reading was sampling one side of a
  turning point, which is why extrapolating it suggested something lower;
* **A3's answer must accommodate two competing terms**, not fit one exponent;
* every windowed exponent sits well below the edge order `2/3 = 0.667`, and the
  top-end value (0.458 over 75..78, local 0.476 at 78) trends toward the bulk
  `1/2`. **Consistent with bulk-dominated, not established** — the turning point
  is precisely why a naive extrapolation from either side misleads.

### Cost, and where this approach walls

Measured scaling ≈ **2.35× per +5 in n** (n = 50 → 3.4s, 55 → 8.1s, 60 → 19.1s,
68 → 64.5s, 78 → 283s). `p(85) ~ 3×10⁷` is the practical wall in Python; a
materially wider window needs a different algorithm, not a faster loop.

Two optimisations, both recorded so they are not re-attempted:

* closed forms for `H` and `C2` replace two of the three per-partition cell
  walks (`H = Σ_i C(λ_i,2) + Σ_j C(λ'_j,2) + n`; `C2` a per-row cubic) —
  verified on all 507 partitions of n = 1..14, and the producer against the
  committed script on n = 3..20. **Only 1.31×**: the hook product still needs
  its `O(n)` walk and the cost is Python loop overhead, not big-int arithmetic.
* a beta-number (first-column hook) formula for `f^λ`, evaluated on whichever of
  `λ`/`λ'` has fewer rows, is **not faster** (1.25×) — the `O(r²)` pair product
  plus one big `n! · num // den` costs about what the `O(n)` walk costs here.

### Not claimed

This proves nothing about the sign for `n > 78`; it is Track B doing what the
workplan scoped it for — guiding A's order prediction. The gap stays OPEN.

---

## 2026-08-30 — TRACK A IS BLOCKED AT A1, NOT AT A2 (beans qou-470y, qou-nna0)

The workplan rated **A1 low-risk and A2 the crux**. It is the other way round,
and A1 does not merely stall — it is impossible as stated.

**`Sigma_h` is not a polynomial in the free cumulants** (`qou-470y`, 11/11
assertions, exact over all partitions of `n <= 10`). Conjugation-invariance of
`Sigma_h` plus the parity law `R_k(lam') = (-1)^k R_k(lam)` confine any such
polynomial to the subalgebra generated by even-index `R`'s and even monomials in
the odd ones — every generator of which has **integer** Plancherel order. But
`E_Planch[Sigma_h] ~ c n^{3/2}`. Contradiction.

So the workplan's stated premise — *"Genus applicability established (both legs
polynomial-on-Young-diagrams)"* — **holds for `omega_3` and fails for
`Sigma_h`**. A2 is scrapped: the `R_k` it was to assemble do not enter through
`Sigma_h` at all.

### What this leaves standing

* `Sigma_c = R_3/2`, `R_4 = 3 omega_3 - n` (Lean's `r4Value` is the right
  normalisation), and `M_1 = Cov(p_2, omega_3) = Cov(Sigma_h, omega_3)` because
  `Cov(R_3, omega_3) = 0` by parity.
* **Track D is promoted to principal.** Fulman's exchangeable-pair / Stein
  bound needs neither leg polynomial. The workplan held it as the fallback "if
  A2 walls"; A1 walling is a stronger reason to take it, and it is now the only
  route in the plan whose premises are intact.
* Track B's window (67 -> 78, previous append) still stands and is unaffected:
  it measures `kappa_n` directly and never touches `Lambda*`.

The gap stays OPEN. What changed is which door is worth pushing on.

2026-09-03 (session, branch m1-k5r5-attack): reviewed the ~2400-commit main advance. GAP NOW: reduction Lean-proved (m1_pos_of_cs_margin); m_inf=0.30019 DERIVED (rigorous modulo IO CLT, cited); M1>0 exact to n<=78; Route 1 chosen. Whole remaining gap = one rigorous C with N0=ceil((C/m_inf)^2)<=78 i.e. C<=2.65, empirical ~0.087 (30x headroom); binding sub-constant C_A (Var(Sum|c|) kink, n^{-1/2}). NEED-LIT (answered): YES, one input missing from corpus = Olver's explicit uniform Bessel remainder for J_nu(2sqrt th) in the oscillatory/transition region (DLMF 10.19/10.20 + Olver 1997 Ch10). Corpus has BOO/BDJ/IO/CC/TW/EM-remainder/Gaussian but NOT this. CONTRIBUTION this session (rigorous, corpus-free, no float64): far tail |x|>X* (X*~e sqrt th+O(sqrt th), where theta^{x/2}/x!<1e-20) contributes <1e-37*V_A, via min(theta^{x/2}/x!,1)>=|J_x| (DLMF 10.14.4 + |J_n|<=1). Localises need-lit to the single band x in (2sqrt th, X*], width O(sqrt th) = edge+transition+outer-bulk error. (Caught+fixed a vacuous first majorant that coupled tail to bulk indices.) NEXT: ingest Olver bound, track C_A<=2.65 through the x^2-weighted band. Audit: docs/audits/2026-09-03-covariance-kernel-M1-k5r5-deep-tail-rigorous-need-lit-localised.md. Gap OPEN.

2026-09-03 (cont., attack branch) DECISIVE NEGATIVE + RETRACTION of my own need-lit answer. I recommended 'fetch Olver's uniform Bessel remainder, then track C_A'. MEASURED that this CANNOT work: writing J=S+E, any POINTWISE bound |E|<=eps gives |dV| <= eps*U with U=Sum w|S| vs V=Sum w S^2/2 = V_A. Exact-kernel measurement: U/V = 42.8, 45.7, 53.9, 70.7, 91.9 at theta=64,78,128,256,512 (grows without bound; slope 0.33-0.39, SUB-sqrt(theta), exponent NOT pinned - do not quote U/V~sqrt(theta)). Decisive direct measurement at theta=78 (largest n the exact table reaches, where the asymptotic must take over): U/V=45.65 => pointwise eps=K theta^{-1/2} gives relative error ~5.17K on V_A; keeping it under m_inf=0.3002 forces K<0.058 vs the O(1) Debye coefficient => short by ~17x. So a sharper POINTWISE bound cannot close N0<=78 for any K; the oscillatory cancellation (summation by parts/stationary phase) is load-bearing. CONSEQUENCES: (1) need-lit answer is NO for the chosen route - retracted my earlier YES; (2) moot anyway, arxiv.org and dlmf.nist.gov are both blocked by org egress policy (403 CONNECT), reported not routed around; (3) this REINFORCES the corpus Route-1 decision (Kerov limit shape + CompositeEulerMaclaurin), which never forms |J-S| pointwise; Route 1's missing piece is an ANALYTIC BUILD (VKLS limit shape + Kerov fluctuation field as analytic objects feeding the EM remainder), not a citation. Probe: wlambda_covariance_epic_M1_pointwise_bound_insufficiency.py (exit 0, NO float64). Gap OPEN, route confirmed.

2026-09-03 (attack branch, cont.) V_A REMAINDER RE-MEASURED + my own EM prediction RETRACTED. Read the corpus EM tool QOU.MathlibExt.abs_integral_sub_composite_le_osc: its bound h^3/12*(g''(a)-g''(b)) carries NO factor of k (per-cell oscillations telescope, governed by TV(g'') not cell count) -- exactly what the pointwise Bessel route lacked. With bulk grid h=1/(2sqrt th) that predicts remainder TV(g'')/(48 theta), a theta^{-1} rate. I predicted that for V_A and MEASURED theta^{-1/2}: exponent p -> 0.505 over theta=250..4000, sqrt(theta)*d nearly constant 0.880->0.857 (C_A ~ 0.857, still drifting down), theta*d GROWS 13.9->54.2. SIGN d>0 (V_A/theta^2 approaches 8/pi^2 from ABOVE). REASON is structural: _osc needs g'' ANTITONE, but the Sum|c| rescaled test function is |u| with a KINK at u=0; splitting there leaves an un-cancelled EM boundary term (g' jumps) of order h=theta^{-1/2}, not h^2. So TV(g'')/(48 theta) is right for the SMOOTH ingredients (Sum c^2, covariance) and NOT for the kink ingredient V_A. CONFIRMS the power-counting in docs/audits/2026-08-29-...-rigorous-finite-n-bound.md (kink costs half an order). DISAGREES with qou-tvok STEP 2's recorded theta^{-1}, c_1~-0.0678, d<0 in BOTH rate and sign -- FLAGGED not adjudicated (may be different objects: poissonized vs de-poissonized, or margin vs V_A); sibling figure not assumed wrong. SCOPE: one ingredient, not the (CS) margin; margin envelope ~0.087 is 10x BELOW V_A's 0.857 because sigma_D/sigma_A cancels the common correction. Probe: wlambda_covariance_epic_M1_em_osc_constant_prediction.py (exit 0, NO float64). Gap OPEN.

2026-09-03 CORRECTION OF THE ENTRY ABOVE (the 'V_A REMAINDER RE-MEASURED + EM prediction RETRACTED' note). That entry is WRONG and is withdrawn. Its theta^{-1/2}, C_A~0.857, d>0 figures came from a BUG in my probe: the Sum|c| weight was written |k|(|k|+1)/2, symmetrising the negative half, whereas the descent set is the SHIFTED lattice {lambda_i - i} (involution x <-> -1-x), so the canonical weight is k(k+1)/2 with SIGNED k -- g(-1)=0, g(-2)=-1, g(-3)=-3, not -1,-3,-6. TELL I MISSED: every term of V_A is a product of two squares, hence non-negative, so more indices cannot give a SMALLER sum -- yet my M=118 run gave 0.8379 vs the reference M=121 run's 0.8105, which falsifies 'truncation is the only difference' outright; I chased truncation anyway. CORRECTED (PR #6469, merged 51bc3bd): with the canonical weight the probe reproduces wlambda_covariance_epic_M1_tvok_remainder_rate.py EXACTLY (theta=1000 -> -6.64223e-5, every printed digit): rate theta^{-1} (exponent 0.94-1.02), c_1 ~ -0.0678, sign d<0. So qou-tvok STEP 2 is CONFIRMED, not contradicted, and my 'may be measuring different objects' hedge was also wrong -- same quantity, same method. The EM-osc prediction is UN-RETRACTED: abs_integral_sub_composite_le_osc's bound carries NO factor of k (oscillations telescope, C^2 only), giving |d| <= TV(g'')/(48 theta) with explicit C_A = TV(g'')/48. FALSIFIABLE TARGET: a Route-1 derivation must give TV(g'') >= 48*|c_1| ~ 3.25, an O(1) number, approached FROM ABOVE (C_A is a bound, c_1 a limit). CLOSURE improves: at theta^{-1}, N0=ceil(C/m_inf)<=78 needs only C<=23.4, not 2.65. Blast radius: same gA in my two other probes; both re-run, both conclusions ROBUST (pointwise U/V at theta=78: 45.65->45.59, still ~17x short; deep-tail shares unchanged at ~1e-38). Audit: docs/audits/2026-09-03-covariance-kernel-M1-k5r5-weight-bug-retraction-retracted.md. Gap OPEN; NEXT = compute TV(g'') from the variance density and check it lands above 3.25 (no literature needed).


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


2026-09-03 (PR #6528, cont.) THE C_A -> MARGIN CONVERSION, written down for the first
time in this arc, plus a PER-LEG budget that relocates where the work is.
CONTEXT: two sites compared a V_A-remainder constant against a MARGIN threshold and
derived numbers from it (corrected: C<=23.4 in #6500, K<0.058 in #6528). A third,
_debye_CA_investigation, phrases it that way in its DOCSTRING ('whether a rigorous
Olver/Debye C_A can land under the target C <= 2.668') but its VERDICT compares the
true MARGIN constant (~0.087) to 2.668, which is unit-correct, and derives nothing
from the conflation. PHRASING DEFECT, NOT a third numerical error -- recorded that way
deliberately; miscounting the errors would be the same sin as the errors. Docstring
now carries a units-clarification block.
THE CONVERSION (nothing in the arc had it): C_A bounds |V_A/theta^2 - v_A| <= C_A
theta^{-1/2}; m = rho_P - sqrt(V_D/V_A). So delta_A = C_A theta^{-1/2}/v_A and
|Delta m| = (sig_ratio_inf/2) delta_A, giving
    C_margin,A = (sig_ratio_inf / (2 v_A)) * C_A = 0.41922 * C_A.
=> the V_A leg alone may spend C_A <= 2.6681/0.41922 = 6.3645, NOT 2.668; the naive
reading is 2.385x too strict. Measured C_A^emp = 0.00775419 (theta in [80,2560]) =>
~821x headroom on this leg.
THE FINDING THAT MATTERS MORE -- PER-LEG BUDGETING. The rho_P leg enters m LINEARLY
(no conversion factor at all) and is the BIGGER contribution: |rho_P - rho_inf| ~
0.1329/theta (exponent measured flat at b=1.0: 0.1319 0.1308 0.1332 0.1323 0.1329
0.1333) against the V_A leg's 0.003251/sqrt(theta). So the 46x headroom on the TOTAL
margin (#6500) and the ~821x on the V_A leg are consistent -- V_A is the SMALL
contribution and most of the margin's finite-n deviation is rho_P's. A rigorous C
should be budgeted PER LEG, not as one number, and the rho_P leg is where the binding
constraint actually sits. That is a redirection of the remaining work.
CAVEATS, both real and stated in the probe: (1) DE-POISSONIZATION NOT DONE -- C_A is a
theta-object, the requirement is at fixed n; the conversion is exact for the SHAPE but
the theta<->n factor is unpinned, so read ~821x as 'modulo de-poissonization'.
(2) C_A^emp is measured at rate theta^{-1/2} while the TRUE V_A rate is theta^{-1}
(exponent 0.93949 here, matching c_1 ~ -0.0678), so |.|sqrt(theta) decreases and the
sup sits at the window's left end -- conservative, but not established below theta=80
while the requirement is n>=79.
CROSS-CHECK: v_A re-extracted independently as 0.81057182513 vs exact 8/pi^2 =
0.81056946914, rel 2.91e-6.
Probe: computations/deltalambda/wlambda_covariance_epic_M1_CA_to_margin_conversion.py
(exit 0, 3.4s, PYTHONPATH-unset-safe, NO float64). Gap qou-k5r5 OPEN; NEXT: budget the
rigorous C per leg, with rho_P the binding one, via the Toeplitz-determinant route
(_bulk_kernel_rate_probe: oscillations cancel at the integrated level, not pointwise).


2026-09-03 (PR #6528, cont.) TWO CANCELLATIONS IN THE MARGIN -- a constraint on the
SHAPE of the proof -- and a CORRECTION of the 'rho_P is the binding leg' claim I made
in this same PR an hour earlier.
EXACT DECOMPOSITION (a rearrangement, no error term; verified to close to 0.0 at every
n): m(n)-m_inf = [rho_P(n)-rho_inf] - [sqrt(V_D/V_A)(n)-sig_ratio_inf] =: L_rho - L_sig.
Exact Fraction covariances over all partitions, n=4..40, NO float64, 10s.
CORRECTION: I concluded from the POISSONIZED large-theta ingredients that 'rho_P is the
bigger leg, V_A the small one' and recommended budgeting with rho_P binding. WRONG. That
compared rho_P's FULL deviation (0.1329/theta) against only the V_A PART of the
sigma-ratio leg (0.003251/sqrt(theta)) -- V_D was never in the comparison. Measured at
fixed n exactly, |L_sig| exceeds |L_rho| by 4x to 700x (|L_rho|/|L_sig| = 1.885, 0.152,
0.127, 0.0222, 0.243, 0.00148, 0.0269 at n=6,12,18,24,30,36,40). The SIGMA-RATIO leg
dominates and V_D is the binding ingredient -- not rho_P, not V_A. SURVIVING from that
commit: the conversion C_margin,A = 0.41922 C_A and the ~821x V_A-leg headroom; both are
correct statements ABOUT THE V_A LEG. The disagreement is NOT the theta-vs-n difference;
it is an omitted TERM, which no de-poissonization could account for.
CANCELLATION 1 (between legs): |L_rho - L_sig|/(|L_rho|+|L_sig|) over n>=16 in
[0.2238, 1.0] -- at worst a 4.5x loss if bounded separately and added.
CANCELLATION 2 (inside L_sig): linearising sqrt(V_D/V_A) ~ sig_inf(1+(dD-dA)/2) with dX
the relative deviation of V_X/n^2 (prediction tracks L_sig to a few %, the residual
being second order), dD and dA carry the SAME SIGN and largely cancel:
dA/dD = -0.036893/-0.058358 at n=40, difference -0.021465 against |dD|+|dA| = 0.095251.
Inner cancellation ratio over n>=16 in [0.1079, 0.2258] -- a further 4.4x-9.3x loss.
CONSEQUENCE, and the point: multiplying the two, a budget that bounds rho_P, V_D and V_A
separately and adds via the triangle inequality can overshoot by ~an ORDER OF MAGNITUDE,
against the 46x TOTAL headroom (#6500) -- i.e. most of the room. THE RIGOROUS ARGUMENT
MUST PRESERVE THESE CANCELLATIONS rather than bound the three ingredients independently.
That is a constraint on the SHAPE of the proof, not merely on its constants, and it is
the first such constraint this arc has measured.
PATTERN, four corrections in one day and all ONE error -- comparing quantities belonging
to different objects: (1) C<=23.4, V_A's rate as a premise about the margin; (2) ~17x,
relative error on V_A vs an absolute margin; (3) C_A vs C<=2.668, phrasing only, verdict
unit-correct; (4) 'rho_P is binding', full deviation vs only part of the other leg. The
guard already recorded ('V_A, sigma_A, sigma_D/sigma_A and m are four different objects;
write the conversion down') is NECESSARY BUT NOT SUFFICIENT -- #4 was not a missing
factor but a missing TERM. STRONGER GUARD: before comparing two quantities, enumerate
everything that feeds each one and check the lists match.
Probe: computations/deltalambda/wlambda_covariance_epic_M1_margin_leg_decomposition.py
Audit: docs/audits/2026-09-03-covariance-kernel-M1-k5r5-margin-leg-cancellation.md
Gap qou-k5r5 OPEN; NEXT: a rigorous route that keeps the V_D/V_A cancellation intact,
with V_D the binding ingredient.


2026-09-03 (PR #6528, cont.) WHAT TO BOUND, measured. Following the two-cancellation
finding: bounding the RATIO V_D/V_A as one object (rather than V_D and V_A separately)
is worth a gain of |dD|/|d_ratio| = 2.61x to 4.85x over n>=16 (exact, not the
linearisation; (V_D/V_A)_inf = sig_inf^2 = 0.461869183; e.g. n=40: |dA|=0.036893,
|dD|=0.058358, |d_ratio|=0.022288, gain 2.618x). So the ratio IS the right target -- but
it recovers only a factor of a few, NOT the full order of magnitude the two cancellations
are jointly worth. The remainder lives in the LEG-vs-LEG cancellation, which a ratio bound
does not capture; recovering that needs rho_P and the sigma-ratio handled TOGETHER rather
than two tight bounds added. Recorded explicitly so the next attempt does not spend its
effort on the ratio alone and expect the whole factor back.


2026-09-04 (#6528, session 125089da): THE NAIVE PER-INGREDIENT BUDGET CLOSES -- retracting my own
'order of magnitude' claim made hours earlier in the same PR.

MEASURED (_naive_budget_closes_probe.py, exact Fraction covariances, NO float64, exit 0),
NAIVE(n) = |L_rho| + (sig_inf/2)(|delta_D| + |delta_A|) vs TRUE(n) = |m(n) - m_inf|:

  pointwise LOSS over n>=16      4.141 .. 25.59 (max at n=16, where TRUE is a near-crossing)
  C_true  = max TRUE  * sqrt(n)  0.0579688  (n=22)
  C_naive = max NAIVE * sqrt(n)  0.279796   (n=22)
  envelope loss                  4.8267x
  headroom remaining             9.5359x    (C_target = m_inf sqrt(79) = 2.66812)

CONSEQUENCE. Preserving the two cancellations (leg-vs-leg 0.2238..1.0; V_D-vs-V_A 0.108..0.226) is
an OPTIMISATION worth ~5x, NOT a structural requirement on the proof. The triangle inequality alone
does not exclude the easy per-ingredient route. My earlier 'constraint on the SHAPE of the proof' is
WITHDRAWN -- it came from multiplying two worst cases that are neither independent nor coincident in
n, so the product double-counted by ~2x.

WHAT IS STILL OPEN, and it is narrower than this morning: C_naive is a FLOOR (empirical sups over
n<=40; a rigorous constant must hold for all n). The live question is whether a rigorous
Debye/Olver-style per-ingredient bound lands within 9.54x of these sups. That is cheaper to answer
than building a cancellation-preserving proof, and it decides whether the harder proof is needed.

ERROR LEDGER, entry 5 -- and a DIFFERENT class from 1-4. Those compared quantities belonging to
different objects. This one COMBINED two correct measurements into a composite never measured, and
the wrong composite changed a recommendation. Guard: a bound composed from other bounds is a
hypothesis, not a measurement -- measure the composite before quoting it.


2026-09-04 (branch claude/m1-k5r5-envelope-convergence-2026-09-04): THE RATIO ROUTE IS THE TARGET --
and it is nearly lossless. Retracts a claim merged in #6528 the day before.

MEASURED (_ingredient_envelope_convergence.py, exact Fraction over all partitions to n=46, NO
float64, exit 0), budgets in MARGIN units at the proved n^-1/2 rate, sup over n>=16:

  C_rho   (linear)              0.0122554
  C_A     (x sig_inf/2)         0.113046
  C_D     (x sig_inf/2)         0.162893
  three-ingredient C_rho+C_A+C_D  0.288194   waste 4.972x   headroom  9.258x
  C_ratio (x sig_inf/2)         0.0536527
  ratio route C_rho+C_ratio       0.0659081  waste 1.137x   headroom 40.482x
  C_true                          0.0579688                 headroom 46.027x

=> Bound rho_P and the RATIO V_D/V_A separately and add: 1.137x lossy, 40.5x of the 46x headroom.
NOT V_D and V_A individually (9.26x), and NOT a bespoke cancellation-preserving argument (buys
<=1.14x over the ratio route and is far harder).

RETRACTS from #6528: 'the rest lives in the leg-vs-leg cancellation, which a ratio bound does not
capture; recovering it needs rho_P and the sigma-ratio handled TOGETHER, not two tight bounds
added.' Two tight bounds added cost 1.137x. Reason is structural: a cancellation between two terms
can only cost a budget when they are COMPARABLE, and at the envelope level C_rho is 23% of
C_ratio. The cancellation that mattered was V_D-vs-V_A, and the ratio bound captures exactly it.

SMALLER SELF-CORRECTION: #6528's three-ingredient figure 0.279796 (9.536x) is max_n[NAIVE(n) sqrt n],
the SUP OF THE SUM. A per-ingredient proof reports the SUM OF THE SUPS = 0.288194 (9.258x). Quote
0.288194.

ENVELOPES ARE SETTLED (nothing had checked this; every headroom figure assumed it). Running max of
|Q| n^p from N upward: at p=1/2 all five FALLING (0.65-0.82); at p=1, L_rho FLAT (0.962, so rho_P's
deviation is Theta(n^-1)) and the other four FALLING (0.71-0.80). Nothing RISING => each window sup
OVER-estimates the sup over n>=79, the conservative direction. Still an extrapolation: window ends
at n=46.

n<=78 PREMISE VERIFIED, not inherited. Five corpus sites assert it and none is the artifact (one is
my own probe from yesterday, which took it from the others). b1-kappa-window-extension.witness.json
(allPassed true, exact Fraction Plancherel summation over every partition) certifies kappa_n >= kappa
= 128/(225 pi^2) > 0 to n=78. C <= m_inf sqrt(79) = 2.6681 STANDS.

NEXT: a rigorous finite-n bound on V_D/V_A. Leading order is ALREADY rigorous for V_D
(_VD_ceiling_rigorous.py: V_D < 64/(75 pi^2) by certified interval arithmetic + explicit analytic
tail majorant, over V_D = sum_{k odd>=3} (Ohat_k - Ahat_k)^2/k with elementary closed forms). The one
open input is the finite-n RATE for that Fourier-side sum, and specifically for the ratio -- a
different and empirically much better-behaved object than either variance. Whether the closed forms
extend to a finite-n remainder with an explicit constant is NOT settled and is not claimed.


ADDENDUM (same probe, p=1 rate). NOT proved -- the proved shape is n^-1/2 (PR #5929) -- but the
envelopes are consistent with it. At |m - m_inf| <= C'/n the requirement is N0 = C'/m_inf <= 79,
i.e. C' <= m_inf*79 = 23.7147, a LINEAR relaxation:

  three-ingredient 1.37319   headroom 17.27x
  ratio route      0.352994  headroom 67.182x  (waste 1.12x)
  C'_true          0.315118  headroom 75.257x

ORDER THE LEVERS. Three-ingredient -> ratio route is worth 4.37x at p=1/2; p=1/2 -> p=1 is worth
only 1.66x (40.48 -> 67.18). DO THE RATIO BOUND FIRST; the better rate is the smaller lever.

METHOD NOTE, and it is the guard from the entry above firing in real time: I first computed the
p=1 ratio-route headroom BY HAND from the running-max tables and got 89x. Measured, it is 67.18x --
I had combined running-max values taken at two different N. Same failure class as the retracted
'order of magnitude'. The arithmetic now lives in the producer, not in prose.


2026-09-04 (branch claude/m1-k5r5-delta-ratio-structure-2026-09-04): THE RATIO ROUTE IS A CONSTANT-
FACTOR GAIN, NOT A RATE GAIN. The exciting branch is excluded.

QUESTION (posed before starting the proof, per formalize-first): does bounding V_D/V_A buy a better
RATE or only a better CONSTANT? It buys a rate iff delta_D/delta_A -> 1 (leading corrections equal =>
they cancel in the ratio).

MEASURED (_delta_ratio_structure.py, exact Fraction over every partition to n=46, NO float64, exit 0):

  Q1  Is rho_delta = delta_D/delta_A -> 1?  NO, DECISIVELY.
      Every tail value (n>=30) is >= 0.4613 away from 1; tail min 1.46132. Nowhere in the table --
      not even at n=4 (0.508) or n=8 (1.224) -- does it approach 1. RATE-GAIN BRANCH EXCLUDED, and
      this conclusion does NOT require the limit to be pinned.
  Q2  What is r?  UNPINNED. Tail range [1.46132, 1.59818], relative spread 0.0895, still drifting up.

  RATE COMPARISON INCONCLUSIVE BY CONSTRUCTION: local log-log exponents over n>=30 are
  |delta_A| mean 0.8236 spread 4.667; |delta_R| mean 0.1887 spread 5.25. Scatter ~8x the difference
  of the means => the means are NOT rates. Same oscillation that made peak-ratio fitting noise in
  #6500; the running-max envelope (#6576) is the tool that works here.

CONSEQUENCE. The remaining work is a rigorous finite-n bound on delta_A ITSELF. The ratio divides its
constant by |r-1| ~ 0.53, i.e. ~1.89x, and nothing more. Effort goes to delta_A; the ratio is applied
at the end as bookkeeping.

TWO GAIN FIGURES, BOTH RIGHT, DO NOT CONFLATE. #6576's 4.37x is the ratio route vs the THREE-
INGREDIENT budget; the gain over bounding delta_A ALONE is ~1.89x. The three-ingredient budget pays
for delta_A AND delta_D separately (0.113+0.163=0.276 margin units), the ratio pays once (0.0537).
Most of the 4.37x is NOT the cancellation -- it is not double-paying. Conflating them overstates the
cancellation's worth by ~2.3x.

VERDICT-LOGIC DEFECT IN MY OWN PROBE, corrected in the same commit. The first run printed
'UNANSWERED -- a wider exact table is needed' on IDENTICAL data, because the verdict tree gated
everything on 'settled' (spread < 5%). 'Have I pinned r?' and 'is r = 1?' are different claims and
only the second decides the project; rho_delta -> 1 requires the tail to APPROACH 1, so a tail whose
minimum is 1.46 excludes it whatever the spread. Fixed to answer Q1 from the tail MINIMUM. Same shape
as da-arity-conflation: a claim about a family tested as a claim about a point.


2026-09-04 (branch claude/m1-k5r5-variance-polynomiality-2026-09-04): V_A HAS NO POLYNOMIAL CLOSED
FORM -- the shortcut is closed. V_W does, exactly.

WHY CHECKED: #6602 narrowed the work to a rigorous finite-n bound on delta_A. A polynomial V_A(n)
would give delta_A EXACTLY at every n and close the n>=79 tail outright, so formalize-first says try
the closed form before the analysis.

THE OBJECTS, named (from stats() in _constant_C_landscape.py; the epic's names are opaque):
  A = Sum_cells |c|      first ABSOLUTE moment of the content distribution (c = j-i). NOT shifted-symmetric.
  D = Sum_u d_u^2        d_u = #cells of content u; squared diagonal multiplicities. NOT shifted-symmetric.
  W = Sum_cells c^2 - C(n,2)   second moment, recentred. IS shifted-symmetric.

MEASURED (_variance_polynomiality.py, exact Fraction over every partition, n=2..30, NO float64):
  V_W  EXACT polynomial, degree 3   (reproduces all 25 held-out n)
  P    NONE (deg <= 10)
  V_A  NONE (deg <= 10)
  V_D  NONE (deg <= 10)
Corroborated by the denominators: V_A(12) = 339037063642199/29628426240000, and by n=30 the
denominator is ~2.7e56. A polynomial in n over Q has bounded denominators.

THE CONTROL IS WHAT MAKES THE NEGATIVE WORTH ANYTHING. Sum c^2 IS shifted-symmetric so V_W should be
polynomial, and it is, through the SAME fitter and pipeline. Had V_W read NONE the script would be
broken and no verdict quotable. (Detector-blindness taxonomy is 26 rows; an unvalidated negative is
the failure mode.) Method: exact Lagrange through the FIRST d+1 points, evaluated on the REMAINING
ones -- reproducing your own interpolation nodes proves nothing.

SMALL POSITIVE: V_W = Var(Sum c^2) = n(n-1)(n-2)/3 = 2*C(n,3), checked exactly at all 29 n. Since
rho_P = P/sqrt(V_A V_W), ONE of rho_P's three ingredients carries NO finite-n error. Only P and V_A
do. Simplifies the target; does not close it. Classical for a shifted-symmetric weight -- confirmed,
not claimed as new.

WHAT THE NEGATIVE DOES NOT SETTLE: rules out a polynomial in n of degree <=10 over n<=30. Does NOT
rule out another shape (poly over falling factorial, harmonic-augmented, two-term recursion). The
corpus tried several such shapes FOR M_1 and found none (2026-08-21-antidiagonal-reformulation:
poly_4 and n^2 H_n + poly_3 both fail); this does not repeat or extend them to V_A.

CORPUS-GREP: the non-polynomiality MECHANISM for the covariance family M_k is already held
(2026-07-25-A2-odd-moment-structure: even k both weights shifted-symmetric => M_2j exact polynomial;
odd weight not => M_2j+1 non-polynomial). Those are about M_k. V_A = Var(Sum|c|) is a DIFFERENT
object and nothing measured it -- which is why it was run rather than inferred. The analogy held;
that it would was not evidence.


2026-09-04 (branch claude/m1-k5r5-cs-relaxation-cost-2026-09-04): THE CS RELAXATION IS CHEAP -- the
(CS) margin route is validated as the right target, by audit rather than assumption.

THE RELATIONSHIP, which had never been priced. Two sufficient conditions coexist in this corpus:
  FULMAN (2026-08-21 audit): Sum h = D + A (split identity) and, with omega_3 = W an eigenfunction of
    the up-down chain, M_1 = Cov(Sum h, W) = P - N with P = Cov(A,W) >= 0 and N = -Cov(D,W) >= 0,
    both manifest EDGE BY EDGE. So M_1 > 0 is EXACTLY P > N -- necessary and sufficient.
  (CS) MARGIN (PRs #6500/#6528/#6576/#6602): m = rho_P - sqrt(V_D/V_A) > 0, which multiplied through
    by sqrt(V_A V_W) is exactly P > sqrt(V_D V_W). Since N <= sqrt(V_D V_W) by Cauchy-Schwarz, THE
    MARGIN IS THE CS RELAXATION OF P > N -- sufficient only, and it discards N's per-edge structure.

MEASURED (_cs_relaxation_cost.py, exact Fraction over every partition to n=40, NO float64, exit 0):
  rho_D = N/sqrt(V_D V_W)  over n>=16 : [0.87815, 0.92034]   <- IS the tightness of CS on (D,W)
  surviving = (P - sqrt(V_D V_W))/(P - N) over n>=16 : [0.78598, 0.85193]
Both INCREASE with n (0.8371 -> 0.9203; 0.7467 -> 0.8519), so at n>=79 the relaxation should be
cheaper still -- the conservative direction for the extrapolation.

VERDICT: CS costs at worst 1.27x. The margin route loses little and sharpening delta_A is well spent.
NOT obvious in advance: had rho_D come out near 0.5, four PRs would have been paying a 2x premium
avoidable by working P > N directly.

THE CORPUS'S REDUCTION IS RE-VERIFIED INDEPENDENTLY, not assumed. Sum h is computed PER CELL as an
explicit hook sum, never as D + A, and two assertions gate every number: split identity Sum h == D+A
at EVERY partition (PASS) and Fulman reduction Cov(Sum h,W) == P - N at EVERY n (PASS). The probe
refuses to print a cost figure if either fails.

DOES NOT CLOSE EITHER ROUTE. Both still need a rigorous finite-n argument -- delta_A for the margin,
P > N for Fulman. Window n<=40 against a requirement of n>=79; nothing here is a bound.


2026-09-05 (same branch claude/m1-k5r5-cs-relaxation-cost-2026-09-04, BEFORE merge): I WITHDRAW my
own inference from the CS-cost measurement. Tightness is not tractability, and the machinery reaches
P > N, not the margin.

WHAT #6651 MEASURED, and it STANDS: the CS relaxation keeps >= 78.6% of the true margin
(rho_D in [0.8782, 0.9203] over n>=16), i.e. costs at most 1.27x.
WHAT I INFERRED FROM IT, and it does NOT follow: 'the margin route is the right target'. Those are
two different claims and only the first was measured.

THE REACH (_eigenfunction_reach.py, exact Fractions, n=3..12, NO float64, exit 0). The Fulman
identity is NOT a general covariance formula:
    Cov(f,g) = E_pi[(f-f*)(g-g*)]/(2(1-beta))   valid ONLY when J g = beta g
so it computes the covariance of ANY f against an EIGENFUNCTION g of the up-down chain. Measured,
quantified over the FAMILY (every non-degenerate n):
    W : eigenfunction at every n, beta_3 = (n-2)/(n+1) EXACT  => Cov(.,W) reachable => P AND N reachable
    A : eigenfunction at NO non-degenerate n                  => V_A = Cov(A,A) NOT reachable
    D : eigenfunction at NO non-degenerate n (constant, hence vacuously one, at n=3 only) => V_D NOT reachable
CONTROL PASSED: J row-stochastic at every n and beta(W) reproduces the corpus's 2026-08-21 value
exactly, so a negative on A is a fact about A, not about my chain.

CROSS-CHECK FROM AN INDEPENDENT DIRECTION: #6627 found V_W an exact polynomial n(n-1)(n-2)/3 while
V_A, V_D and P are not polynomial at all. Same boundary from the other side -- the one object with a
closed form is the one whose statistic is the eigenfunction. Two measurements, one split.

CONSEQUENCE: the margin route's ONE remaining object (V_A) is the one the named machinery does not
reach AND the one with no polynomial closed form. P > N's two objects are both exact local per-edge
sums with manifest signs. RECOMMENDED NEXT TARGET CHANGES FROM delta_A TO P > N.

SCOPE (a), NOT (b): this says the NAMED IDENTITY does not apply to V_A. It does NOT exclude V_A -- a
spectral decomposition of A in the chain's eigenbasis, or a different chain for which A IS an
eigenfunction, are both untested.

QUANTIFIER BUG IN MY OWN PROBE, caught before commit: the first run reported 'D is an eigenfunction
=> V_D reachable' on the strength of n=3 ALONE, where D == 3 is CONSTANT and a constant is trivially
an eigenfunction of any stochastic chain (beta=1). I used any(n) where reachability is a claim about
the FAMILY and needs every(n) with constants excluded. Second quantifier slip of this arc -- #6602
had the mirror (testing a family claim at a point).


2026-09-05 (same branch, cont'd): P > N IN LOCAL FORM -- and FACT B OF THE 2026-08-21 AUDIT IS FALSE.

FINDING 1 -- CORPUS CORRECTION. docs/audits/2026-08-21-covariance-kernel-M1-fulman-exchangeable-pair-
reduction.md states Fact B as 'Delta(Sum D^2)*Delta(omega_3) <= 0 on every single-box edge (100% of
the signed edge weight is discordant; verified n<=13)'. IT FAILS FIRST AT n = 10, and again at n=11,
12 (16, 24, 36 violating ordered edges). Hand-verified counterexample:
    lam* = (5,4,1) -> lam = (5,5), joined in the chain via mu = (5,5,1)
    Sum D^2 : 16 -> 18   omega_3 : -5 -> 0   =>  product = (+2)(+5) = +10 > 0.
WHY THE STATED REASON FAILS: 'larger |content| => shorter diagonal => Sum D^2 decreases' describes
the EQUILIBRIUM SHAPE, not the actual diagonal lengths of a given lambda. Landing a box on a diagonal
of current length d raises its square by 2d+1 whatever the content is; here the box leaves a length-1
diagonal (1->0) and lands on another length-1 one (1->4), net +2.
WHAT SURVIVES: N >= 0 is NOT refuted (positive at every n measured); M_1 = P - N is an identity and
verified exactly; Fact A HOLDS, re-verified at every edge to n=12 (beyond the original's n<=8). Only
the PER-EDGE argument for N's sign fails, so 'both signs manifest edge by edge' is true of P and
false of N at n >= 10. Correction applied in place to the 2026-08-21 audit.

FINDING 2 -- THE GAP DOES NOT CLOSE HERE. If Delta(Sum h)*Delta(omega_3) >= 0 edge-wise, M_1 > 0
would follow for all n immediately. Measured: edge-wise non-negative only for n < 6 (too few edges to
exhibit one) and NEVER after, no recovery through n=12. So M_1 > 0 does NOT follow from per-edge
signs. What must be bounded is the POS/NEG MASS RATIO, measured in [22.0, 112.0] over n >= 6, against
threshold 1. Negative edges are ~7-17% of all edges -- a substantial fraction, not a thin exceptional
set, which ARGUES AGAINST a pairing/injection argument over them and FOR bounding the ratio directly
(a reading of the census, not a proof that pairing cannot work).

SELF-CHECK gating every figure: the census reconstructs M_1 exactly from (pos_mass - neg_mass)/
(2(1-beta_3)) against a direct partition sum -- PASS at every n.

THIRD SMALL-n QUANTIFIER TRAP OF THIS ARC, caught before commit: any(n) over the whole table reports
'a non-negative n exists' on the strength of n=3,4,5 where the chain is too small to HAVE a negative
edge. Now reported as a threshold (where it starts failing, whether it recovers). Prior two: #6602
tested a family claim at a point; the reach probe counted a CONSTANT statistic as an eigenfunction.


2026-09-05 (same branch, cont'd): AN EXACT CLOSED-FORM CRITERION FOR THE NEGATIVE EDGES. P > N stops
being a census and becomes an inequality in four integers.

FORMALIZE-FIRST RATHER THAN A WIDER SCAN. The census left 'bound the pos/neg mass ratio' and the
obvious move was to extend n. Both per-edge pieces already have closed forms, so which edges are
negative is decidable algebraically. Write the edge as: lam has a box at content u that lam* lacks,
lam* has one at v that lam lacks, d_u/d_v the diagonal lengths IN lam. Then
    Delta(A) = |u|-|v|,  Delta(W) = u^2-v^2,  Delta(D) = 2(d_u-d_v)-2
    Delta(A)Delta(W) = (|u|-|v|)^2(|u|+|v|) >= 0     (Fact A, in closed form)
With g = |u|-|v| SIGNED, Delta(W) = g(|u|+|v|) so sign(Delta W) = sign(g), and
Delta(A)+Delta(D) = g + 2(d_u-d_v) - 2, giving

    NEGATIVE  <=>  g * (g + 2(d_u - d_v) - 2)  <  0

VERIFIED AT EVERY EDGE TO n = 22 (12,518 edges at n=22), together with all four closed forms and
'g = 0 edges contribute exactly 0'. At g > 0 it reads d_u - d_v < 1 - g/2: a negative edge needs the
diagonal the box LEAVES to be no longer than the one it LANDS ON, by a margin growing with the gap.

A WLOG SHORTCUT IS WRONG HERE, and my own check caught it before commit. The first version derived
the g>0 case then handled g<0 by swapping u and v. Invalid: Delta(D) = 2(d_u-d_v)-2 is NOT symmetric
under that swap -- the -2 does not flip -- so the swapped form is off by 4. Diagnostic signature: all
four closed forms PASSED while the criterion FAILED at every n having a negative edge, which is what
correct algebra plus wrong case analysis looks like. The signed-g form has no case split.

A FACT-B VIOLATION IS NOT A NEGATIVE EDGE -- I had this backwards. Fact B claims Delta(D)Delta(W)<=0;
a VIOLATION has it > 0, which ADDS to the non-negative Delta(A)Delta(W) and makes the edge MORE
positive. Disjoint phenomena: negative edges first at n=6, Fact-B violations first at n=10.

THE RATIO SETTLES, which the n<=12 window could not show. pos/neg mass over n>=6 is [22.0, 112.0],
but that is small-n noise; over n >= 16 it is [44.128, 56.315], ~54.8 at n=22.
  n:    6     8    12    16    19    22
  R: 22.0 112.0  52.3  44.1  56.3  54.8

WHAT THIS BUYS: P > N was a weighted sum over an ENUMERATED set; it is now a set CUT OUT BY AN
INEQUALITY in four integers, three of which (u, v, d_u) are read off one partition. That is the shape
a finite-n bound can use -- bound the weight the criterion admits rather than enumerate. It bounds
NOTHING yet, and a ratio settling near 55 over n<=22 is not evidence about n>=79.


2026-09-05 (same branch, cont'd): THE INTEGER FORM, AND MY LOCALIZATION HYPOTHESIS IS REFUTED.

INTEGER FORM (verified at every edge to n=22, alongside the signed-g form). d_u - d_v is an INTEGER,
so the half-integer thresholds collapse:
    g > 0 :  negative <=>  d_u - d_v <= -floor(g/2)
    g < 0 :  negative <=>  d_u - d_v >= 2 + floor(|g|/2)
NOT mirror images. That +2 vs -floor is the SAME -2 in Delta(D) that broke the WLOG swap, and it BIT
A SECOND TIME in this probe as an off-by-one on EVEN |g| only -- the odd cases agreed, so a spot
check would have passed. Twice from one asymmetry; both forms are machine-checked, not argued.

THE g>0 THRESHOLDS PAIR: g=2 and g=3 both need <= -1; g=4 and g=5 both need <= -2. So the larger ODD
g inherits the smaller even g's admission condition while carrying a strictly larger |Delta W|.

HYPOTHESIS REFUTED. The profile was measured to test whether the negative mass concentrates at small
|g| (which would localise a bound to a few edge shapes). IT DOES NOT:
    n=12  |g|=1 42.9%/20   |g|=2 5.5%/4    |g|=3 51.7%/12
    n=16  |g|=1 38.2%/84   |g|=2 3.5%/16   |g|=3 57.9%/56
    n=22  |g|=1 30.2%/448  |g|=2 4.4%/100  |g|=3 46.8%/364
|g|<=2 carries only ~35% at n=22; the LARGEST bucket is |g|=3; |g| runs to 5. The pairing is why --
g=3 is admitted on g=2's condition with a bigger term, so the mass is NOT monotone in |g| and there
is no small-|g| truncation to lean on. A bound must handle the whole admitted set.


### 2026-09-05 — a SECOND Cauchy-Schwarz, on the EDGE measure; and reverse-pairing is EXCLUDED

Probe `computations/deltalambda/wlambda_covariance_epic_M1_edge_cauchy_schwarz.py` (PR #6651).

**The move.** The Fulman identity writes BOTH halves of `M_1 = P - N` over the same edge set with
the same non-negative weight `dmu = pi(lam) J(lam,lam*) (|u|+|v|)`, with `g = |u|-|v|`,
`delta = d_u - d_v`:

    P = Sum dmu g^2                 (a SQUARE -- this is Fact A in one line)
    N = Sum dmu g(2 - 2 delta)      (not a square -- which is why Fact B is false)

Cauchy-Schwarz on THAT measure: `N <= sqrt(P Q)`, `Q := Sum dmu (2-2 delta)^2`. So

    Q < P  =>  N < P  =>  M_1 > 0

-- a sufficient condition in two edge sums of the same shape over the same measure, needing
NEITHER `V_A` NOR `V_D`, the two objects the reach probe showed the identity does not reach.

**MEASURED: it holds, with room.** `Q < P` at every n in 4..20; `P/Q` in [2.231, 2.266] over
n >= 12 -- 2.24x headroom. Surviving margin `(P - sqrt(PQ))/(P - N)` rises monotonically
0.811 -> 0.861, i.e. the SAME cost as the first relaxation ([0.786, 0.852]) on a reachable
target. `P/Q` is U-SHAPED: min 2.23112 at n = 15, rising for the whole second half. (I first
classified it by endpoints and printed "falling", which is wrong about the tail and is exactly
the reading a reader cares about.)

**PROVED, and it closes a route.** The chain is reversible with `w = f^lam f^lam*/(n+1)!`.
Reading an edge from the other end sends `g -> -g` and `delta -> 2 - delta`, hence `k -> -k`, so
the term `g k (|u|+|v|)` and the weight are BOTH invariant: the negative edge set is CLOSED UNDER
REVERSAL. Cancelling each negative edge against its own reverse CANNOT work. scope-(b) for that
pairing (an invariant forbids it); scope-(a) for pairing in general.

**Controls, all PASS, and no verdict is quoted without them:** `P`/`N` rebuilt from the edge sums
equal `Cov(A,W)` / `-Cov(D,W)` exactly at every n (independent Plancherel computation); `N <=
sqrt(PQ)` at every n; the reversal identities at every edge.

**Still OPEN, and sufficient is not necessary.** A failure of `Q < P` would say nothing about
`M_1 > 0`. Window n <= 20 against a requirement of n >= 79; nothing here is a bound. The live
target is a finite-n proof of `Q < P` -- both sides are explicit edge sums in `(g, delta)` over
the Plancherel-weighted up-down chain, so this is where the Kerov-CLT-adjacent analysis should
now be aimed.


### 2026-09-05 — the CS relaxation is CLEANER but not EASIER (PR #6825)

Probe `computations/deltalambda/wlambda_covariance_epic_M1_pq_pointwise_census.py`.

**Question settled BEFORE building on #6651's recommendation:** is `Q < P` pointwise nearly-true
(per-edge argument + thin exceptional set) or aggregate-only (needs the joint law of `(g, delta)`
under Plancherel)? Those need different proofs.

**Integrand factors, no case split.** With `Delta(A) = g`, `Delta(D) = 2 delta - 2`:

    g^2 - (2 - 2 delta)^2 = k (2g - k),   k := g + 2 delta - 2 = Delta(Sum h)

So a `P-Q` edge is negative iff `k(2g-k) < 0` -- the SAME `k` as the `M_1` census (`g*k < 0`),
tested differently. The two negative sets are NOT nested in either direction.

**MEASURED: AGGREGATE.** Over `n >= 12`, negative-edge fraction 10.3-11.2 %, pos/neg MASS ratio
**[20.33, 26.74]**. Not thin -- no per-edge argument closes it.

**And WORSE than what it was meant to simplify.** `M_1`'s own census, computed on the SAME edge set
over the SAME window (not cited from a differently-windowed figure), is **[41.51, 56.32]** -- about
2x more favourable. So the relaxation bought a cleaner STATEMENT
(`Q < P` is `E_nu[Delta(D)^2] < E_nu[Delta(A)^2]`, two second moments of one measure, no `V_A`) and
NOT an easier problem. **My #6651 recommendation is weakened by its own follow-up**: `Q < P` stays
the better-SHAPED target, not a locally-closeable one.

Cross-check: the `M_1` figure here (41.5-56.3 over `n >= 12`) reproduces #6651's 44.1-56.3 over
`n >= 16` on a wider window.

**STRUCTURAL, and it is the one locally-priceable piece.** At `g = 0` the `P-Q` integrand is
`-(2-2delta)^2 <= 0` for EVERY such edge, while `M_1`'s `g*k` vanishes identically there. The
`|u| = |v|` edges contribute nothing to `M_1` and carry **11.55 %** of `P-Q`'s negative mass at
`n = 20`. Cut out by `g = 0, delta != 1` -- no inequality to solve.

Negative mass sits toward the **bulk**: mean `|u|+|v|` = 6.656 negative vs 9.025 positive at n=20.

**Controls, all PASS, no verdict without them:** `P` == `Cov(A,W)` from the Plancherel measure with
no edges (independent yardstick; `Q` has NO such yardstick and the module says so rather than
faking one); per-edge terms sum to `P-Q` exactly; criterion matches sign at every edge; term
reversal-invariant (so reverse-pairing cannot cancel this set either).

**Still OPEN.** Sufficient never necessary. Window `n <= 20` vs requirement `n >= 79`. Both routes
(`M_1 > 0` directly, and `Q < P`) now need the same thing: control of the joint distribution of
`(g, delta)` under Plancherel. That is the Kerov-CLT-adjacent analysis, and it is where the next
attempt should aim -- with the `g = 0` family priced separately as the one closed-form piece.

--------

## 2026-09-07 — a normalisation hazard for anyone deriving kappa, and the third basis in which Sum_c^2 is ONE mode

Recorded from PR #7061 (the rho_inf derivation). Not a claim about kappa's value;
a claim about a definition kappa depends on.

### The hazard: kappa is defined through R_4, and the corpus carries two R_4 formulas

This bean's kappa is `Cov(Sum_h, R_4)/(3 n^{5/2})`
(`wlambda_covariance_epic_M1_IO_mode_decomposition.py`), so it inherits whatever
normalisation `R_4` carries. Two are live in the corpus and they differ by a
factor of 3 on `omega3`:

| reading | formula | verdict |
|---|---|---|
| Lean `r4Value` | `R_4 = 3*omega3 - n` | **TRUE** |
| "naive `Sigma_3 = R_4 + R_2`" | `R_4 = omega3 - n` | **FALSE** |

**Already settled in the corpus, by exact rational arithmetic, not by me.**
`wlambda_covariance_epic_M1_A1_sigmah_in_free_cumulants.py` builds the transition
measure exactly (Fraction end to end, no float) and reports over all `lam` with
`n <= 8`:

    R_2 == n for all lam (n<=8):                True
    R_4 == omega3 - n   (naive Sigma_3=R4+R2):  False
    R_4 == 3*omega3 - n (Lean r4Value):         True

**The textbook identity is NOT wrong — the trap is which symbol you put in it.**
Biane/Kerov's `Sigma_3 = R_4 + R_2` is correct as stated. With the corpus's
`omega3 = Sum_c^2 - C(n,2)` (the class-normalised central character) it gives
`Sigma_3 = 3*omega3`, which reconciles exactly with the Lean form and with
`wlambda_covariance_epic_M1_free_cumulant_reframing.py:10` (`omega3 =
(R_4 + R_2)/3`). The factor 3 is the class-size convention: `Sigma_3` is
normalised by `(k)_3` while `|C_{(3,1^{k-3})}| = (k)_3/3`.

So "naive" labels the substitution of `omega3` for `Sigma_3`, not the identity.
This is the normalisation-mistaken-for-a-discrepancy class AGENTS.md names, and
it is worth flagging here because a factor of 3 in `R_4` puts a factor of 3 in
kappa — and kappa's open question is a **0.3 %** one (`~0.0591` vs
`sqrt(2)/24 = 0.058926`). A convention slip therefore does NOT explain that gap;
it would produce a 3x miss, not a 0.3 % one. Anyone attacking kappa should state
which `R_4` they used, and should not "explain" the 0.3 % by finding this factor.

### The structural fact, now seen in three independent bases

`Sum_c^2` couples to exactly ONE mode. Three bases, three derivations, no shared
machinery:

| basis | statement | source |
|---|---|---|
| sine / Chebyshev on [-2,2] | `G_k = pi * delta_{k,3}` | `wlambda_covariance_epic_M1_rho_inf_kerov_derivation.py` (PR #7061) |
| free cumulants | `Sum_c^2 = R_4/3 + const` | `wlambda_covariance_epic_M1_IO_mode_decomposition.py` |
| class / shifted-symmetric | `Sigma_3` is ONE orthonormal basis vector, so `Cov_P(ln f, Sigma_3)` is a single Fourier coefficient and every `d>=2` mode is orthogonal to it | `cb24799114` on main (bean `qou-vilx`) |

The third arrived on main today from a **different arc** answering a different
conjecture, which is what makes it worth recording: it is not a re-derivation.
All three land on the degree-3 / 3-cycle object, and all three say the same
thing — the higher modes contribute nothing to this covariance.

That is the step the rho_inf closed form turns on (it is why the ratio is a
finite closed form rather than a ratio of two sums), so it now has independent
support in two bases the derivation does not use.

### What this does NOT do

It does not pin kappa. `Sum_h`, unlike `Sum_c^2`, is outside Lambda* and its
fluctuation spreads over the whole even tower `R_4, R_6, R_8, ...` — that
asymmetry is the actual difficulty and none of the three readings above touches
it. Gap stays OPEN.


--------

## 2026-09-08 — the R_4 / omega3 question is RESOLVED (the two readings are one identity plus one convention)

Owner instruction: "resolve R_4 issues". Done. Nothing about kappa is settled by
this; a definition is.

### What was wrong, and it was the WORDING, not the arithmetic

My own note above (2026-09-07) and two probes recorded the two readings as rival
formulas, one "naive" and wrong:

    Lean r4Value                     R_4 = 3*omega3 - n     TRUE
    "naive Sigma_3 = R_4 + R_2"      R_4 =   omega3 - n     FALSE

That labelling reads as though **Biane/Kerov's identity were false in this
corpus**, which is the more damaging of the two errors available here: an agent
who believes it will avoid the entire Kerov-polynomial apparatus — the one tool
both live routes to `M_1 > 0` now point at.

### MEASURED, from characters, independent of both recorded formulas

New producer, **6/6 PASS**, `Fraction` end to end, no float:
`computations/deltalambda/wlambda_covariance_epic_M1_r4_sigma3_normalisation_reconciliation.py`

It computes `chi^lam(3-cyc, 1^{n-3})` by Murnaghan-Nakayama (beta-number form)
and `f^lam` by hook lengths, so `Sigma_3 := (n)_3 * chi / f` comes from the
symmetric group, not from either formula under test. `R_2`, `R_4` are taken from
the corpus's OWN transition-measure code (imported from the A1 probe) rather
than reimplemented — a second implementation could agree with me and disagree
with the corpus, which would prove nothing about the corpus. 63 partitions,
n = 3..8:

| check | result |
|---|---|
| **A** `Sigma_3 == 3 * omega3` | PASS — the class-size convention |
| **B** `Sigma_3 == R_4 + R_2` | PASS — **Biane/Kerov is TRUE** |
| **C** `R_4 == 3*omega3 - n` | PASS — the Lean form |
| `R_2 == n` | PASS |
| **D** `R_4 == omega3 - n` | FALSE on **57 of 63** partitions |
| **E** (A and B and R_2=n) => C | PASS on every partition |

### The resolution

`Sigma_3` is normalised by the falling factorial `(n)_3`; the 3-cycle class has
size `|C_{(3,1^{n-3})}| = (n)_3/3`. Hence `Sigma_3 = 3*omega3`, and

    Sigma_3 = R_4 + R_2   ==>   3*omega3 = R_4 + n   ==>   R_4 = 3*omega3 - n

i.e. **the Lean r4Value form IS Biane/Kerov's identity written in this corpus's
normalisation.** They were never rival conventions. The defect is substituting
`omega3` where `Sigma_3` belongs, which divides the omega3-coefficient by 3 and
produces the false `R_4 = omega3 - n`. E verifies that as an implication on the
data, so C is derived here rather than re-asserted.

Note D fails on 57 of 63, not 63 of 63: the substitution is accidentally right
on 6 small partitions. Smallest genuine failure `lam = [3]` (`R_4 = 3`,
`omega3 - n = -1`, `3*omega3 - n = 3`). So a spot-check on one small diagram can
"confirm" the wrong formula — which is plausibly how it entered.

### Wording fixed at all four sites

- `wlambda_covariance_epic_A1_sigmah_not_polynomial.py` — docstring and the
  `R4_equals_3omega3_minus_n` assertion note (the latter is emitted INTO
  `a1-sigma-h-not-polynomial.witness.json`, so the wrong claim was in a witness).
- `wlambda_covariance_epic_M1_A1_sigmah_in_free_cumulants.py` — docstring, and
  `rel_naive` renamed `rel_omega_substituted` with its printed label.

Both re-run exit 0. The regenerated witness diff is the note text plus
provenance stamps only — **no numeric value moved**, which is the expected
signature of a wording-only change.

### What this does NOT settle

kappa. It inherits this normalisation (`kappa = Cov(Sum_h, R_4)/(3 n^{5/2})`), so
anyone deriving it should state which `R_4` they used — but a slip here is a
factor of **3**, and kappa's gap is **0.3 %** (`~0.0591` vs
`sqrt(2)/24 = 0.058926`). It therefore cannot explain that gap, and finding it
must not be reported as explaining it. Gap stays OPEN.

### 2026-09-07 — CONVERGENCE with the epic's A2 leg, and TWO of my results were re-derivations

Prompted by reviewing 1298 commits that landed on `main` while this arc ran. This entry is a
correction to my own arc's standing, not a new result.

**`M_1` is already IN the epic, as a sub-item of `qou-ogrk` (A2 leg 1, in-progress, priority
high, parent `qou-v8t7`) -- and the epic bean `qou-x631` does not mention `k5r5` at all.** The
carrier is `qou-ogrk`'s "M_1 REFORMULATION (2026-08-21)": `M_1 = Cov_Planch(Sum(i+j), Sum c^2) =
Cov(Sum h, Sum h^2)`, "Route = Kerov CLT integral (open)". That was written **two weeks before**
#6825 concluded the same thing. I corpus-grepped `k5r5`, `M_1` and `covariance-kernel`; I did not
grep `qou-ogrk`, which is where the reformulation lives. The k5r5 bean already records a prior
agent making this exact mistake on this exact epic.

**Two of my results are re-derivations, and mine are the weaker derivations.**

1. `V_W = Var(omega_3) = n(n-1)(n-2)/3`. I found it in #6627 by exact Lagrange interpolation
   (degree 3, held-out points). `qou-ogrk` had it on **2026-07-25** from the classical identity
   `Sum h^2 = Sum c^2 + n^2`; and `f02c2dcba45` (2026-09-06) re-derives it from **character column
   orthogonality**: `Var_P(Sigma_p) = (k)_p^2/|C_p|`, so `Var(Sigma_3) = 3k(k-1)(k-2)` and
   `omega_3 = Sigma_3/3` gives `k(k-1)(k-2)/3`. VERIFIED here: all three agree exactly. An
   interpolant that fits is not a derivation; two of the three are.
2. "The route is the Kerov-CLT integral." `qou-ogrk` line 32, 2026-08-21.

**What my arc DID add, and the epic does not hold**: the Fulman edge decomposition `M_1 = P - N`
with both signs measured per edge; the eigenfunction-reach negative (`A`, `D` are not
eigenfunctions at any non-degenerate n, so the identity reaches `P`/`N` but not `V_A`/`V_D`); the
falsification of the 2026-08-21 audit's Fact B; the exact negative-edge criterion
`g(g + 2(d_u-d_v) - 2) < 0`; the reversal-closure proof; and the `Q < P` census. The epic's A2 leg
works in HOOK-VALUE coordinates (`nu_v`, `H_s`, the polynomial `R`); mine works in EDGE
coordinates. Those are genuinely different and the edge results are not duplicated anywhere.

**MY RECOMMENDED NEXT STEP WAS AIMED AT A ROUTE THE EPIC HAD ALREADY ELIMINATED -- partly.**
#6825 closed with "control of the joint distribution of (g, delta) under Plancherel ... the
Kerov-CLT-adjacent analysis, and it is where the next attempt should aim". `qou-ujil` (route 7,
2026-09-06) eliminates **concentration / limit-shape** arguments for the epic's object, because
`E_P[Sigma_3] = 0` exactly, so replacing lambda by the limit shape "discards exactly the term
being computed and proves 0 <= 0". **That objection transfers to `M_1` verbatim**: `E_P[omega_3] = 0`
is what makes `M_1 = E_P[Sum h * omega_3]` in the first place. So my recommendation was ambiguous
between an eliminated reading (limit-shape/concentration) and the one the epic endorses (a
CLT-SCALE CORRELATION computation, `qou-t5m1`'s Sniady genus expansion). Read it as the second only.

**THE UNEXPLORED ROUTE WITH THE BEST WARRANT, and I have not touched it.** `qou-ogrk` PROVED the
EVEN members of the moment tower `M_k = Cov(Sum h^k, omega_3)` positive for all n >= 3 (2026-07-25)
with manifest certificates -- `M_2 = n(n-1)(n-2)/3`, `M_4 = M_2 * 5(n - 8/3)`,
`M_6 = M_2 * 7(3n-8)^2` -- by: even hook-power moments are SHIFTED-SYMMETRIC, hence exact
polynomials in n by Ivanov-Olshanski Prop 5.1, hence provable by a finite positivity check.
`M_1` is the first ODD member; odd-k is empirical only, because `Sum h` is not shifted-symmetric.

**That is the SAME boundary my own arc kept hitting from two other directions**, which is why it
is worth stating as one fact rather than three: `V_W` has a closed form and `V_A` does not (#6627);
`W` is an eigenfunction of the up-down chain and `A`, `D` are not (#6651); and even-k moments are
shifted-symmetric while odd-k are not (`qou-ogrk`). Shifted-symmetric <=> closed form <=> reachable,
three times over. Cheap unasked question: is either piece of the split `Sum h = D + A` shifted-
symmetric on its own, or any combination that is not `Sum h` itself?

**Standing:** `qou-k5r5` stays OPEN and is NOT on `qou-x631`'s stated critical path -- the epic's
live phase-3 routes are `qou-t5m1` (Sniady genus expansion, todo) and `qou-0ml9` (RSK, todo, Lean
dependency landed in `qou-t181`). `M_1` sits under `qou-ogrk`. Before any further edge-coordinate
work here, grep `qou-ogrk` and `qou-v8t7`, not just `k5r5`.


---

## 2026-09-08 — the R_4 landing does NOT fall to my shifted-symmetry negative; and √2/24 came back

Two separate things, both about claims that landed on `main` while this branch was open.

**1. The cheap unasked question at the end of the previous entry is ANSWERED: no.** Neither
`Sum h`, nor `A = Sum|c|`, nor `D = Sum_u d_u^2` is shifted-symmetric — tested by exact Gaussian
elimination over Q against the span of monomials in the Kerov–Olshanski shifted power sums
`p_k^*`, pooled over every partition of every `n` in [1,12] (271 partitions), at degree bounds
6, 8 and 10 (30 / 67 / 139 monomials). Every verdict UNCHANGED as the bound rises, so the
negative is not a bound artifact. Controls `n`, `Sum c`, `Sum c^2`, `Sum h^2` all come back IN,
so a negative is a fact about the statistic, not about my elimination. PR #7126,
`wlambda_covariance_epic_M1_shifted_symmetry_membership.py`.

**What that forecloses, precisely.** `qou-ogrk`'s ONE proved positivity technique — shifted-
symmetric ⟹ exact polynomial in n (Ivanov–Olshanski Prop 5.1) ⟹ finite positivity check — applies
to *no part* of the split `Sum h = D + A`. Not to the sum, and not to either summand separately,
which was the remaining hope. Fourth sighting of the same wall.

**What it does NOT foreclose, and I nearly recorded it as if it did.** `106a6784c5f`
(2026-09-08, `resolve(qou-k5r5)`) establishes from characters, 6/6 PASS, that Biane/Kerov holds
here: `Sigma_3 = R_4 + R_2`, `R_2 = n`, and hence `R_4 = 3*omega_3 - n` — the Lean `r4Value`
form. The corpus's "naive `Sigma_3 = R_4 + R_2` ⟹ `R_4 = omega_3 - n`" wording was a
normalisation slip (`Sigma_3 = 3*omega_3`), not a failure of the identity. So the
**Kerov-polynomial / free-cumulant apparatus is live for `omega_3`**, and my negative says
nothing against it: `omega_3` IS shifted-symmetric (my own control confirms `Sum c^2` is IN).
The wall is on the `Sum h` side of the covariance only. An agent reading my negative as "the
Kerov machinery is out" would be reading it one factor too broadly.

**2. √2/24 is back on `main`, and it was retired on 2026-08-21.** The same commit closes with
*"kappa's gap is 0.3 % (~0.0591 vs sqrt(2)/24 = 0.058926)"*. Both halves are stale:

- `~0.0591` is `kappa_n` in its **peak region** (peak `kappa_32 = 0.0591961`, then descending),
  not `kappa`. The limit is DERIVED: `kappa = 128/(225 pi^2) = 0.0576404956` (PR #5428, VKLS
  Chebyshev-mode integral, quadrature-verified to 1e-42).
- `sqrt(2)/24` was **refuted on 2026-08-21** as a fit to n = 400..800 float64 data —
  `wlambda_covariance_epic_M1_kappa_structure.py:63` says "BOTH ARE WRONG" in as many words, and
  `..._kerov_clt_leading_kappa.py:212` prints "sqrt(2)/24 NOT confirmed".

It lives only in that commit *message*, not in any file, so this is a note for the next reader
rather than a sweep. But the two 2026-08-21 audits left one thing genuinely open and a committed
window now closes it, which is the only new content here:

**`kappa_n` CROSSES `sqrt(2)/24` between n = 68 and n = 69.** `kappa_68 = 0.0589313` (+0.0098 %),
`kappa_69 = 0.0589230` (−0.0044 %), falling monotonically to `kappa_78 = 0.0588572` (−0.116 %).
No new compute — the exact rationals are already in `b1-kappa-window-extension.json`; what is new
is the comparison. The exact-anchor audit had exact data only to n = 50 and correctly said
"sqrt(2)/24, 1/17 and neighbours are all within the still-moving window"; the window has since
moved past this one. And the IO-derivation audit's parenthetical *"the finite-n data never
reaches it because the corrections are large"* is **false** and is corrected in place.

**Two things the crossing does not establish**, stated because the class verdict differs by
constant: `1/17 = 0.0588235` is **NOT** crossed by n = 78 (`kappa_78` is still 0.057 % above it);
and a crossing is not a bound — nothing here constrains `kappa_n` for `n > 78`, which is exactly
what this gap needs. Probe (6/6 PASS, gated on recomputing every stored decimal from the stored
exact rational, worst disagreement 8.05e-26):
`computations/deltalambda/wlambda_covariance_epic_M1_kappa_sqrt2_24_crossing.py`.

**Standing unchanged.** `qou-k5r5` OPEN. The live reduction is the ONE-SIDED effective claim
`kappa_n >= kappa` for all `n >= 13` (verified exactly to n = 78, crossing at exactly n = 13,
non-monotone with a peak at n = 32 — so monotonicity is not available and an effective bound is
required). My edge-measure route (`Q < P ⟹ M_1 > 0`, PRs #6651/#6825) attacks the SIGN directly
and would bypass the effective bound entirely; it is not competing with it.

### 2026-09-07 — the even-moment route is SHUT: neither piece of `Sum h = D + A` is shifted-symmetric (PR #7126)

Probe `computations/deltalambda/wlambda_covariance_epic_M1_shifted_symmetry_membership.py`.
Executes the cheap question #7120 identified. The answer is negative and closes a route.

**Why it mattered.** `qou-ogrk` PROVED the EVEN moments `M_k = Cov(Sum h^k, omega_3) > 0` by
shifted-symmetric => exact polynomial in n (Ivanov-Olshanski Prop 5.1) => finite positivity check --
the epic's ONLY proved positivity technique. `M_1` is the first ODD member. If either summand of
`Sum h = D + A` were in `Lambda*`, that machinery would apply to it and reduce `M_1` to the other.

**The test.** `Lambda* = Q[p_1^*, p_2^*, ...]` with Kerov-Olshanski shifted power sums
`p_k^*(lam) = sum_i [(lam_i - i + 1/2)^k - (-i + 1/2)^k]` -- elementary, NO characters. So
membership is exact linear algebra over Q on monomials `prod p_{mu_j}^*`, `|mu| <= D`, with
n-INDEPENDENT coefficients, pooled over every partition of every n in [1,12] (271 partitions).

**MEASURED: `Sum h`, `A = Sum|c|`, `D = Sum d_u^2` are ALL OUT.** A rational linear functional
separates each from the whole subalgebra, so OUT is conclusive at the bound, not a failed search.
**Not a bound artifact:** the probe re-runs itself at `|mu| <= 8` and `<= 10` (30 -> 67 -> 139
monomials) and every verdict is UNCHANGED.

**Controls, all PASS, no verdict without them:** `n`, `Sum c`, `Sum c^2`, `Sum h^2` -- four
functions of KNOWN shifted-symmetric status -- must all land IN, and do. Plus `p_2^* == 2 Sum c`
and the split identity `Sum h == D + A`, both at every pooled partition.

**CONSEQUENCE.** The even-moment route to `M_1` is shut: ogrk's proved technique applies to no part
of the split.

**And it is the FOURTH independent sighting of ONE wall** -- worth carrying as one fact:
  1. `V_W` has a closed form, `V_A` does not (#6627)
  2. `W` is an eigenfunction of the up-down chain, `A` and `D` are not (#6651)
  3. even hook-power moments are shifted-symmetric, odd are not (`qou-ogrk`)
  4. neither summand of the odd one is either (this probe)
Shifted-symmetric <=> closed form <=> reachable, four times over. A fifth attempt that routes
around this wall rather than through it should expect the same answer.

**Scope.** OUT is exact at these bounds; it does NOT exclude higher-degree membership, and says
NOTHING about whether `M_1 > 0` -- only that this technique cannot reach it. scope-(a).

**What is left, after this.** Of the routes the epic names, `M_1` is reachable by none that are
proved. The live epic routes remain `qou-t5m1` (Sniady genus expansion on the `(f^lam)^3`-biased
measure, todo) and `qou-0ml9` (RSK, todo, Lean dependency landed in `qou-t181`), and `qou-ujil`
says a proof must operate at the CLT scale and produce a correlation coefficient. `M_1`'s own next
move, if any, is the integrated-covariance form `f668c434a97` introduced for the epic
(`E_Q[X] = integral_0^1 Cov_{Q_t}(log f^lam, X) dt`), which restores first order where the direct
tilt expansion is ~1/3 nonlinear. That is untested for `M_1` and is the one un-eliminated lead.


---

## 2026-09-11 — the tilt derivative is now PROVED in Lean, sorry-free (PR #7178)

Owner asked, of PRs #7120/#7126: *"all assertions proved in lean?"* **The answer was
NO** — both were Python probes whose controls are arithmetic self-checks, not theorems.
This entry records the promotion of the one assertion that warranted it.

**`folio/quantum-observable-universe/lean/QOU/MassTheory/TiltDerivativeCovariance.lean`**,
for an ARBITRARY finite family over an ARBITRARY field (not for `n <= 22`):

| declaration | statement | base ring |
|---|---|---|
| `tiltNum_derivative_eval_one` | `N'(1) = sum_i w_i f_i h_i` | `[CommRing R]` |
| `tiltNum_eval_one_eq_zero_iff` | `N(1) = 0 <-> wMean w f = 0` | `[Field R]` |
| `tilt_deriv_eq_wCov` | `N'(1)/D(1) = wCov w h f` | `[Field R]` |

So the probe's `n <= 22` check is now a fact about the CONSTRUCTION rather than about
the range sampled.

**The content is not the quotient rule.** It is that the derivative of the tilted mean
at `x = 1` is a COVARIANCE rather than a weighted moment, and that it is so PRECISELY
BECAUSE the tilted statistic has vanishing weighted mean. With `f = omega_3` that
hypothesis is exactly `E_Planch[omega_3] = 0` — the same fact `qou-ujil` uses to
ELIMINATE limit-shape arguments. The obstruction is re-used as the asset.

**Anti-vacuity.** `tilt_deriv_ne_wCov_of_mean_ne_zero` gives a concrete two-point family
with nonzero total weight and nonzero `wMean` where the conclusion is FALSE — so the
hypothesis is demonstrably load-bearing rather than inert.

**A hypothesis I wrote and then removed.** The first version carried
`(hw : sum_i w_i /= 0)`. The linter flagged it unused; checking rather than silencing,
the statement is TRUE without it (Lean's `x/0 = 0` makes both sides 0 in the degenerate
case), so dropping it STRENGTHENS the theorem. An unused hypothesis inside a theorem
about when a hypothesis is load-bearing would have been the wrong thing to ship.

**Verification as run:** `lean -DautoImplicit=false -s 65536` exit 0, ZERO warnings
(a bare `lean` is a weaker check — autoImplicit defaults true off-lakefile);
`#print axioms` on all four declarations gives `[propext, Classical.choice, Quot.sound]`,
no `sorryAx`; `grep -c sorry` = 0. Library file, no sidecar, so nothing but this covers it.

**Import note for the next agent:** `Mathlib.Algebra.BigOperators.Ring` is ABSENT from
the restored lake-cache olean set — a fresh instance of the documented cache-gap class.
Imports routed through `Algebra.Polynomial.Derivative` + `Order.Field.Basic` + `Tactic`.

**Scope, unchanged.** This proves the REFORMULATION, not the gap. Nothing bounds `R'(1)`
below; no claim is made about its sign. **`qou-k5r5` stays OPEN.**

## 2026-09-08 coordination: same kernel as qou-x631, qou-o6ov, qou-za3q, qou-omr7

Audit docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 1 / §7.3 C2: `k5r5` (99 commits, 08-21 → 09-08) and `o6ov` (99 commits, 08-30 → 09-05) both work the odd-moment / Magnus `tr(ρ_λ Ω₂)` kernel, and before this note there were **zero** cross-citations among k5r5 / o6ov / x631 / za3q / omr7 (measured 2026-09-08 by grepping each body for the other four ids). Shared ledger: epic `qou-x631`, now parent of the other four. Roles — x631: epic, Cov_Planch(f^λ, Σc²) ≤ 0 / T₃(k) kernel; k5r5: M₁ > 0 (first odd moment), all-n proof OPEN, identity Lean-proved; o6ov: does |tr(ρ_λ Ω₂)|/dim decay in b across the ≤2-row column (open mathematics, rescoped 2026-09-05, PR #6822); za3q: Magnus-Ω₂ probes use the Plancherel weight y_λ, 91 % of their work on shapes tr_M annihilates; omr7: Magnus probes' d_q was the hook product, weight inverted (4 files, PR #6442). Statuses are unchanged by this note; a result landing on any of the five should be cited in the other four.

---

## 2026-09-11 (cont.) — the tilt identity is now proved AT THE REAL OBJECTS (PR #7189)

PR #7178 proved the tilt identity for an arbitrary finite family over an arbitrary field.
That is a lemma about polynomials: on its own it says nothing about Plancherel measure,
`omega_3`, or `M_1`. #7189 discharges its hypothesis at the corpus's own Plancherel datum.

**The hypothesis is DERIVED, not assumed.** `tilt_deriv_eq_wCov` needs `wMean w f = 0` with
`w = dim^2`, `f = omega_3 = Sum_c c^2 - binom(n,2)`. From the two `PlancherelSnData` fields
already in the corpus — `sum_dim_sq : Sum dim^2 = n!` and `two_sum_dim_sq_content :
2 Sum dim^2 Sum c^2 = n(n-1) n!` — we get `Sum dim^2 omega_3 = 0` EXACTLY.

Four theorems in `QOU/MassTheory/PlancherelTiltDerivative.lean`, all with axioms
`[propext, Classical.choice, Quot.sound]`, no `sorryAx`:

| declaration | statement |
|---|---|
| `plancherel_weighted_omega3_sum_eq_zero` | `Sum dim^2 omega_3 = 0` |
| `plancherel_wMean_omega3_eq_zero` | `wMean = 0` |
| `plancherel_tilt_deriv_eq_wCov` | `R'(1) = Cov_Planch(hgt, omega_3)` |
| `plancherel_tiltNum_eval_one_eq_zero` | `R(1) = 0` |

**The fourth is the one worth citing.** It says the quantity a limit-shape evaluation
computes is IDENTICALLY ZERO at the point where such an evaluation happens — `qou-ujil`'s
objection as a theorem rather than a remark, and the reason the derivative is the
informative object.

**EPISTEMIC STATUS — do not over-read.** `[PlancherelSnData n]` is a CLASS HYPOTHESIS
(§3b-cond), so all four are CONDITIONAL. The class is not a hole (the corpus inhabits it at
every `n` from RSK + Okounkov-Vershik, and its unlabelled Wedderburn form is unconditional
and sorry-free), but **conditional-proved is not premise-established** — cite as "modulo
`PlancherelSnData`", never flatly.

`hgt` is left ARBITRARY deliberately: the identity does not need `hgt = Sum_h`, and pinning
it there would claim less while looking like more.

**What is still NOT Lean.** `M_1 > 0` (the gap). The `kappa_n` crossing of `sqrt(2)/24`
(a numerical comparison over a committed window). The shifted-symmetry negative (exact
Gaussian elimination in Python at degree bounds 6/8/10). `R(x) > 0` for `x > 1` and the
nonlinearity tail (measured to `n <= 22`). **The reformulation is formalised; the
measurements are not.**

**Build note for the next agent:** compile against a HARDLINKED MIRROR of the QOU olean
tree. A separate shadow root shadows `QOU` and does NOT fall through to the real tree —
that cost one failed attempt. Shadow removed afterwards; real olean tree untouched.

**`qou-k5r5` stays OPEN.**
## Cross-citation from qou-za3q (2026-09-11): the A=4 Magnus sign is measured

Per the 2026-09-08 coordination note on qou-za3q ("a result landing on any of the
five should be cited in the other four"), this is such a result.

`he4_magnus_omega2_sign_sparse_probe.py`, 77/77 partitions of H_12, max dim 7700,
28661s:

    P_total(A=4) = 34.1260272853576529271380692762741452981457684651471317452205
    sign = +1    control (rho = I) = 0.0 vanishes    33+/42-    sign_flip_vs_A3 = False

Sign map across the light nuclei: A2 = -1, A3 = +1, A4 = +1. There is exactly ONE
sign change in A = 2,3,4 and it sits between the deuteron and the triton, NOT at
the alpha particle.

Load-bearing for anyone reading the older framing: the he4 probe's docstring
asserted "A=3: P<0, NO flip vs A=2" and that premise had propagated into its
GENERATED VERDICT string. It is false — A=3 is +2.4701927, confirmed by the
committed witness and a fresh 30/30 re-run. Fixed under qou-rfhj. If any of the
five beans reasons from "negative through the deuteron and triton", that premise
is stale.

scope-(a): a dimensionless SIGN datum. NOT a MeV (the Delta_lambda magnitude gate
is open and untouched), NOT a physical binding-sign assertion (qou-v7ro / #6077,
cited not re-derived). The total is a weighted sum of mixed-sign terms (33+/42-).


## 2026-09-12 — the CS step is taken on the WRONG EDGE SET (free, but small); an exact identity; and a prediction of mine refuted

Probe `computations/deltalambda/wlambda_covariance_epic_M1_support_restricted_cs.py`, **7/7 PASS, exit 0**, exact `Fraction` throughout, mpmath only for √ and display. Reuses #6651/#6825's edge enumeration; no new chain code. Corpus-greped first (six paths): **all three items below are absent from the committed corpus** — the algebra is one line from `qou-k5r5:1165` and nobody had taken it.

### FINDING 1 — restrict Cauchy-Schwarz to `supp(g)`. It is free, and it is small.

At a `g = 0` edge (`|u| = |v|`, i.e. `v = −u`) **both** `M₁`'s integrand `g·k` and `P`'s integrand `g²` vanish identically, while `Q`'s `(2−2δ)²` does not. Those edges load `Q` and nothing else. CS only ever needed the support of `g`:

    M₁ = Σ_{g≠0} dμ g k = P + Σ_{g≠0} dμ g(2−2δ) ≥ P − √(P·Q'),   Q' := Σ_{g≠0} dμ (2−2δ)²

so the live sufficient condition is **`Q' < P`**, strictly weaker than `Q < P`, and `supp(g)` is the **optimal** restriction in this family (CS is insensitive to any `g = 0` edge; no other edge can be dropped without changing `M₁`).

**MEASURED at `n = 20`: `Q'/Q = 0.9943`**, raising `P/Q` `2.2615 → 2.2743` (**+0.57 %**) and the CS-certified share of the true margin `0.8615 → 0.8663` (+0.0048).

**Do NOT read #6825's 11.55 % as this number.** That entry says the `g = 0` edges *"carry 11.55 % of `P−Q`'s negative mass at `n = 20`"* — a different denominator. Both are right: 11.55 % of `P−Q`'s **negative** mass, 0.57 % of **`Q`**. So adopting `Q' < P` costs nothing and should be done, but it improves headroom by half a percent, **not by an order**, and does not change the difficulty. The open problem is still the joint law of `(g, δ)` under Plancherel.

### FINDING 2 — an exact identity, new to the corpus, and circular as a route

From #6825's recorded `g² − (2−2δ)² = k(2g−k)` together with `M₁ = Σ dμ g k`:

> **`2 M₁ = E_k + (P − Q)`,  `E_k := Σ dμ k² = Σ dμ (Δ Σh)²`**

Verified as CONTROL 1: exact `Fraction` equality at every `n` in 4..20, no tolerance. Two readings: `E_k ≥ 0` trivially gives **`M₁ ≥ (P−Q)/2` with no Cauchy-Schwarz at all** (weaker than CS's `P − √(PQ)` at the measured `P/Q ≈ 2.24` — `0.277P` against `0.332P`, reported so the weaker bound is not mistaken for a gain); and `E_k` is the exact slack, the Dirichlet energy of `Σh` under `dμ`.

**It yields no new sufficient condition by itself** — substituting `E_k = P + 2Σdμ(ΔA)(ΔD) + Q` turns `E_k > Q − P` back into `M₁ > 0`. Circular, and recorded as an identity rather than a route.

### FINDING 3 — 🛑 my own stated prediction was WRONG

`k = g + 2(d_u − d_v) − 2` is an **integer**, so `k² ≥ 1` off `{k = 0}` and `E_k ≥ μ({k ≠ 0})`. I wrote the prediction into the docstring *before* measuring, expecting the bound to be **cosmetic**: contents run to `O(√n)`, so `|k|` should too, and `E_k/μ` should grow like `n`.

**It does not.** `E_k/μ({k≠0})` runs `1.80` (n=5) → `4.10` (n=20), global log-log slope **0.594**. The dμ-weighted mean of `k²` stays near 4, i.e. `|k| ~ 2`: **`Δ(Σh)` does not inherit the `O(√n)` scale of the contents, because `ΔA` and `ΔD` largely cancel in `k = ΔA + ΔD`.** That is a structural fact about this edge set worth keeping independently of the bound.

**The exponent is NOT pinned** — the last six local slopes span `[0.315, 0.788]`, a factor 2.5, on a window ending at `n = 20`. Do not quote `√n`. And it still yields no route: the condition it buys (`Q − P < μ({k≠0})`) only helps where `Q > P`, which is not the measured regime.

### What the corpus-grep found that matters MORE than any of the above

**Nothing in the corpus relates `Σ dμ (Δf)²` to a spectral gap, a Poincaré inequality, or `Var_Planch(f)`** — measured zero across `docs/`, `computations/`, `.beans/`, `content/` (Lean included) for *Poincaré*, *log-Sobolev*, *conductance*. What exists is a Dirichlet-**form** identity for the **`qou-x631` kernel** (`f = dim`), **bilinear not energy**, on the **plain conductance without the `(|u|+|v|)` factor** (`..._phase5b_dirichlet_peredge.py`), plus exact chain eigenvalues `τ₁ = 2/n` (`Σc`) and `τ₃ = 3/n` (`ω₃`). Both routes now want the same missing thing, and the machinery for it is **held and uncited**: `library/arxiv-1804.03926v3` (*Weighted Poincaré inequalities … Stein kernels in dimension one*) and `library/arxiv-1704.00850v3` (*Estimating the spectral gap of a trace-class Markov operator*) — **0 citations each** across `docs/` + `.beans/` + `computations/`. Fulman's own held paper has zero hits for spectral gap / Poincaré / Dirichlet.

### 🛑 CORRECTION to a figure I was carrying, caught by the same grep

**`Var(Σh)/n² = 0.0099743` is the ANALYTIC ASYMPTOTIC LIMIT, not a measurement.** I had it as measured. The exact finite-`n` data is **`0.0191` (n=4) → `0.0140` (n=22)** — about **1.4× the limit** at the top of the window, still descending. Anyone using `0.00997` as a finite-`n` input is off by ~40 % at every `n` the exact table reaches. Source: `2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md:92` for the limit, `..._kappa_analytic_IO.py:110` for the data.

### Scope

Sufficient is never necessary. Window `n ≤ 20` against a requirement of `n ≥ 79`; **nothing here is a bound over all `n`** and none of the three findings closes the gap. Finding 1 improves the live route's headroom by 0.57 %; Findings 2 and 3 are recorded results that buy no route. Path 0 (`corpus_search`) was **down** (`paper-assistant` `ENOENT`), so `emptyRoots` is unchecked and a vocabulary blind spot is not ruled out. **`qou-k5r5` stays OPEN.**

### 2026-09-12 (cont.) — the DEPTH reading: the whole difficulty is depth-changing edges, and the free family is SHRINKING

Same probe, now **9/9 PASS**. In cell coordinates with `b = i+j` (anti-diagonal) and `c = j−i` (content), `Σh = Σ_cells b + n`, so **`k = Δb` exactly**, and

> **`b = |c| + 2m`, `m := min(i,j) ≥ 0`** — the cell's **depth** along its diagonal.

Hence `k = g + 2Δm` and **`M₁ = P + 2Σ dμ·g·Δm`**. Both halves of the decomposition are already in the corpus (`d = m+1` in `..._edge_ratio_monotonicity.py:158` and `..._kappa_large_n_sampler.py:100`; *"a cell on diagonal c at depth k is (k, k+c), so i+j+1 = 2k+c+1"* in `..._kappa_derivation.py:26`) — what is new is reading `k` through it.

**Two consequences.** If every cell sat at depth 0 (a hook), `k = g` and `M₁ = P > 0` **termwise** — so the entire obstruction *is* the depth. And on any edge with `Δm = 0` the integrand is `g·k = g² ≥ 0` with no inequality to solve:

    M₁ = [Σ_{Δm=0} dμ g²]  +  [Σ_{Δm≠0} dμ g k]

first bracket unconditionally non-negative, all negative edges confined to the second. `Δm = 0` is `δ = 1`, the value #6825 already singles out, and its recorded integer criterion independently implies no `δ = 1` edge is negative — so this derives a known fact **and prices it**.

**🛑 And the price kills it as a route.** The unconditional part is **12.33 % of `M₁` at n=20, with a DECLINING share**: `0.356` (n=8), `0.271` (n=10), `0.225` (n=12), `0.173` (n=15), `0.123` (n=20). The free family **shrinks as `n` grows** and cannot carry a large-`n` proof; `87.67 %` of `M₁` sits on depth-changing edges and is uncontrolled here. Quoting the 12.33 % without the trend would suggest a foothold that is not there.

**What the depth reading does buy** is a sharper statement of the open problem than `(g, δ)`: `m ≥ 0` is a *hard pointwise constraint* (`b ≥ |c|` for every cell), `m = 0` picks out the first row and column exactly, and the gap is now *"the `g`–`Δm` anti-correlation stays above `−1` uniformly"* — which is the bean's own opening `ratio → −0.62; need ratio > −1` in geometric rather than algebraic terms. CONTROL 6 checks the split is exact **and** that every `Δm = 0` edge is non-negative per edge, not in aggregate.

### 2026-09-12 (cont.) — 🛑 I RETRACT my own "held and uncited machinery" recommendation: both papers are the WRONG machinery

Two entries up I wrote that nothing in the corpus relates `Σ dμ (Δf)²` to a spectral gap or Poincaré inequality, and that *"the machinery for it is **held and uncited**"* — naming `library/arxiv-1804.03926v3` and `library/arxiv-1704.00850v3`. **I named them from their titles without opening them. Opened now, neither applies.**

| paper | what it actually does | verdict |
|---|---|---|
| `arxiv-1704.00850v3` *Estimating the spectral gap of a trace-class Markov operator* | a **Monte-Carlo estimator** for MCMC diagnostics — §5 "Classical Monte Carlo", examples are a Gaussian chain, Bayesian probit and linear regression; term counts: Monte Carlo 37, estimat* 110+ | **inapplicable** — estimates a gap statistically from simulation; supplies **no analytic lower bound** on a Dirichlet form |
| `arxiv-1804.03926v3` *Weighted Poincaré inequalities … Stein kernels in dimension one* | one-dimensional, **absolutely continuous** setting; the Stein kernel `τ` comes from a covariance identity for a real random variable **with a density**. Term counts: density 51, "dimension one" 28, absolutely continuous 9, **discrete 0, lattice 0, Markov chain 0** | **inapplicable** — the object here is a Dirichlet form on a **discrete** lattice, not a 1-d density |

The second was the more plausible (Fulman's method *is* a Stein exchangeable-pair method), and it is still the wrong setting: a weighted Poincaré inequality for a 1-d density says nothing about the joint law of `(g, Δm)` on the up-down chain, which is the whole difficulty. I am not proposing a projection-to-1-d rescue; that would need the Stein kernel of the relevant marginal, which is the same unknown.

**What survives and what does not.** The *measurement* stands: nothing in the corpus relates `Σ dμ (Δf)²` to a spectral gap, Poincaré inequality, or `Var_Planch(f)` — zero hits across `docs/`, `computations/`, `.beans/`, `content/`; and these two papers genuinely have **0 citations** each. What falls is my **inference** that an uncited on-topic *title* meant the missing tool was already in the building. **Title match is not applicability**, and I recommended a route on a title.

So the honest status is stronger than before, not weaker: the Poincaré/Dirichlet gap for this weighted form is real **and the corpus does not hold a source that fills it** — so it is an analytic build, not a citation, which is exactly the conclusion the 2026-09-03 entry reached for the Olver/Bessel route by a different road.

**Method disclosure, so this is re-checkable and not over-read:** I read section titles and term frequencies across each paper's `sections/`, not full proofs. That is enough to establish setting (1-d absolutely continuous / Monte-Carlo estimation) and therefore inapplicability to a discrete Dirichlet form; it is **not** a claim that the papers contain nothing else of use.


## 2026-09-12 — Poincare degeneracy worry REMOVED; gap still OPEN

`folio/quantum-observable-universe/lean/QOU/MassTheory/WeightedDirichletPoincare.lean`
(8 declarations, sorry-free, `lean -DautoImplicit=false -s 65536` exit 0, zero
warnings, `#print axioms` sorryAx 0).

**The claim.** `1 <= |u| + |v|` on every up-down edge of the Young lattice, so
the Fulman edge measure `dmu = pi(lam) J(lam,lam*) (|u|+|v|)` gives a weighted
Dirichlet form that **dominates** the unweighted one, and any unweighted
Poincare inequality transfers **at the same constant**.

**The evidence.** `|u| + |v| = 0` forces `u = v = 0`, i.e. one diagonal carrying
both a removable and an addable corner. `no_removable_addable_same_diagonal`
proves no partition does — three cases on the row indices, using only that row
lengths are antitone. Contents are carried in `Z`, so no `Nat` subtraction and
no Durfee square is needed.

**What it does NOT do, and this is the half that matters.** Poincare
lower-bounds a **quadratic** form. `M1 = E(A, Sum h)` is **bilinear**, and the
live sufficient condition `Q < P` needs an **UPPER** bound on `Q = E(D)`.
Poincare bounds `P` and `Q` both from **below**, so it cannot deliver `Q < P`.
The measured `P/Q ~ 2.24` is a structural fact about the joint law of
`(g, Delta m)`; a one-sided bound does not reach it.

It also does not supply the unweighted gap — `poincare_transfer` takes it as a
hypothesis, because the corpus does not have one (the recorded `tau_1 = 2/n`,
`tau_3 = 3/n` are eigenvalues of named eigenfunctions, not a spectral gap over
all of `L^2`).

**Status: OPEN.** This closes a *worry*, not the gap. The remaining routes are
unchanged: an upper bound on `Q = Sum dmu (2 - 2 delta)^2`, or a direct
termwise/support argument on `M1 = Sum dmu g k`.

## 2026-09-13 — rho is CONCAVE, so the site-density input is ONE MOMENT of kappa, not the distribution

`computations/deltalambda/wlambda_covariance_epic_M1_site_density_jensen_reduction.py`,
**7/7 PASS, exit 0, 22.5 s**, exact `Fraction` for kappa and all first moments, mpmath 40 dps
for `rho`. No float64. PR #7291.

Corpus-greped first (six paths). `..._M1_jensen_route.py` already applies Jensen **in this
arc**, but to a different object — the area functional `A_sigma`, for the opposite-sign
edges. Jensen on the SITE distribution is absent, and so is any use of `rho`'s concavity.

### The reduction

`..._M1_kappa_site_distribution.py` identifies `E_omega[density]` exactly as the kappa-mass on
drop sites and records its VKLS prediction (~0.36) as *"evidence, not proof"*, the open input
being the **whole distribution of kappa**. It need not be:

    rho(u)   = 1/2 - arcsin(u/2)/pi
    rho''(u) = -u / (pi (4 - u^2)^{3/2})   <  0   on (0,2)

so rho is **strictly concave**, and Jensen gives `E_kappa[rho(U)] <= rho(E_kappa[U])`. Since
`rho(m) < 1/2` for EVERY `m > 0`, the required `E_omega[density] < 1/2` follows from a LOWER
BOUND ON THE KAPPA-MEAN ALONE. The open input drops from a distribution to a first moment.

### The support caveat, which is load-bearing and is measured rather than waved

The producer's `rho` CLAMPS — `asin(min(u,2)/2)` — and that clamped `rho~` is **not** concave
across `u = 2`: `rho'(2^-) = -inf` and the extension is flat, so the slope *increases* there
and plain Jensen does not apply to it. Measured, not asserted:
`rho~(2.2) - (rho~(1.9) + rho~(2.5))/2 = -0.0505 < 0`.

Handled by conditioning, which is exact and needs no extra hypothesis, since `rho~` vanishes
off `{U <= 2}`:

    E_kappa[rho~(U)] = p * E_kappa[rho(U) | U <= 2]  <=  p * rho( E_kappa[U | U <= 2] )

and it costs nothing: `p = kappa({U <= 2}) >= 0.998 at every n measured`.

### What was checked

- **Concavity three independent ways**: sympy symbolic second derivative; the closed form at
  40 dps on a grid in (0,2); and midpoint concavity from `rho` ITSELF over all 741 grid pairs,
  using no derivative at all.
- **Jensen verified against the ACTUAL kappa at every n = 8..30** — the one measurement that
  could falsify the reduction. Min slack `+0.00287` (at n = 8), i.e. **nearly tight**, so the
  reduction loses almost nothing.
- **Bound < 1/2 at every n reached**, max `0.3976` at n = 8.
- **CONTROL**: `sum_t kappa(t) == sum_e w_e` exactly (Fraction) at every n — the Lean
  `kappa_sum`, and what makes this probe's kappa the sibling's kappa rather than a lookalike.
- Conditioned kappa-mean rises `0.632` (n=8) -> `0.807` (n=30). To certify
  `E_omega[density]_VKLS <= 1/2 - eps` needs cond mean `>= 2 sin(pi eps)`: 0.313 for eps=0.05,
  0.618 for 0.10, 0.908 for 0.15.

### Scope — what this is NOT

- **Same-sign edges only** (the producer's own restriction). `S_opp` saturates near 0.118,
  ~36% of `S`, and is untouched by this.
- It bounds the **VKLS-PREDICTED** density, not the finite-n empirical one. The sibling
  measured actual/prediction at ~0.5 over `n <= 48` and rising, so at every n reached here the
  empirical density sits well BELOW the bound and Jensen is not yet the binding constraint.
  Closing the route still needs the VKLS limit as an input, exactly as before.
- **It does not lower-bound the kappa-mean.** That is the reduced open problem and is not
  attempted. A reduction is not a proof.
- Range is small (n <= 30, against the sibling's 48); nothing here is an asymptotic claim.

### One wording mismatch in the sibling, recorded because it inverts an inequality

`..._M1_kappa_site_distribution.py`'s docstring describes its `vkls_ceiling` as *"the VKLS
local density at the measured position"*, i.e. `rho(E_kappa[U])`. Its CODE computes
`krho = sum_t kappa * rho(t/sqrt n)`, i.e. `E_kappa[rho(U)]`. By the concavity above those are
ordered `E_kappa[rho] <= rho(E_kappa[U])`, so the code computes the **sharper** of the two
while the prose names the weaker. The recorded number is correct; only the description names
a different object. Not fixed here (it is the sibling's file and the arc is live).

### What I looked for and did NOT find — four things already in the corpus

Recorded so the next agent does not re-derive them: `M_1 ~ Cov(Sum_cells c^2, Sum_cells(i+j))`
is the PR #5366 antidiagonal reformulation; `Sum_h = Sum_u d_u(d_u + |u|) = D + A` is already
the `D + A` identity; `P = E_w(A) = E(A,W)` because `Delta W = g (|u|+|v|)` exactly is the
Fulman identity; and `D` non-increasing away from the main diagonal (whence
`g > 0 => Delta_m <= -1` on same-sign edges) is `..._M1_telescoping_route.py`'s *"on the
positive axis D is non-increasing and 1-Lipschitz"*. All four were re-derived independently
here and all four were already held.

`qou-k5r5` stays OPEN.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-13 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Round 82 Execution Note (2026-11-17T10:13:44Z)

- **Status**: `in-progress` (PR awaiting merge; no unilateral closure).
- **PR**: [`litlfred/qou#8294`](https://github.com/litlfred/qou/pull/8294) (`feat/qou-b9cj-ck2w-k5r5-ndt5-x3iv-x631`, HEAD `22907bca8b5dd626221c15ea2658a1f14545c5be`).
- **Lean Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/PretzelSymmetryAdaptedGradingAndSubstrateBranchBrick.lean` (wired into `QOU.lean`, compiled with Lean 4.24.0, 0 findings across all 7 static Lean audits).
- **80-dps Probe & Witness**: `computations/probes/pretzel_symmetry_adapted_grading_and_substrate_branch_brick_probe.py` & `computations/probes/pretzel-symmetry-adapted-grading-and-substrate-branch-brick.witness.json` (`scriptCommitSha = caec3a2639d9338bfaf9aa9d455a0ab97b427071`, `scriptHash = 428700c5c7bd`, `outputHash = 27ee54e84b99cf035202cc1272490bd167d1f4ad8e861ae3bd043848cca760e3`).
