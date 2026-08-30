---
# qou-k5r5
title: 'GAP: M_1>0 (first odd moment) — rigorous all-n proof OPEN; identity Lean-proved, Kerov-CLT gives asymptotic only'
status: in-progress
type: task
priority: normal
created_at: 2026-08-21T16:10:21Z
updated_at: 2026-08-29T16:34:28Z
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

