---
# qou-k5r5
title: 'GAP: M_1>0 (first odd moment) — rigorous all-n proof OPEN; identity Lean-proved, Kerov-CLT gives asymptotic only'
status: todo
type: task
priority: normal
created_at: 2026-08-21T16:10:21Z
updated_at: 2026-08-23T08:31:54Z
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
