---
# qou-slck
title: '#7705 dispatch B: GL_n vector rep K^n with the Hecke R-matrix as a nondegenerate OS(z,t) datum; go to the trace'
status: in-progress
type: task
priority: normal
created_at: 2026-10-12T18:13:10Z
updated_at: 2026-10-12T19:29:23Z
parent: qou-xhci
---

Owner picks on #7705.

2026-10-12 progress (branch claude/oriented-skein-category-2026-10-11, PR #7705). All sorry-free, lean -DautoImplicit=false -s 65536 exit 0 against a shadow rebuild of the import cone; #print axioms = propext, Classical.choice, Quot.sound.
- QOU/OrientedSkein/Model/GLnRMatrix.lean: GL_n Hecke R-matrix on X = R^n in ModuleCat R, every n, CommRing with q*qi=1: quad, braid (YBE), crossing : HeckeCrossing; S_ne_smul_id (n>=2).
- GLnTrace.lean (go to the trace): weighted partial trace w_i = q^(n-1-i) qi^i is a LeftTrace; loop d with d(q-qi) = q^n - qi^n; curl q^n; ptr2_conj by weight conservation. markovFamily : MarkovTraceFamily R q qi (q^n * [n]^-1); markov_eq (uniqueness).
- GLnCrossCheck.lean: n=2, closure trace = SeminormalRep.wtrace (convention D, z_D = q^3/(q^2+1)) at every level.
- GLnDatum.lean (dispatch B): ExactPairing on R^n, sideways crossing computed, T = swap + A^-1 on diagonal (A triangular, det q^n), dim relation t = q^n, delta = [n]_q. datum : OrientedSkeinDatum q qi (q^n) [n]_q (R^n) (R^n).
- GLnLift.lean: glnFunctor = OS.lift datum; OS_cross_ne_smul: in OS(q,qi,q^n,[n]_q), n>=2, the crossing is not a scalar.
OPEN: (1) that the GLnTrace weighted partial trace equals the closure in OS(z,t) via the datum's cups/caps (trace compatibility of the lift) is not proved; (2) faithfulness of OS(z,t) -> ModuleCat on Hecke parts for m <= n not proved; (3) no comparison with TensorMarkovModel (Pres presentation, no bridge to SchurWeyl.Hecke).

2026-10-12 (cont.) Open items 1 and 2 CLOSED, sorry-free, axioms clean.
- Item 1, trace compatibility: Model/GLnClosure.lean closeD (cup eta, leftward cap T;eps, no braiding); closeD_datum_eq: closeD datum = qi^n * ptr(wt) (colsum_eq: column sums of A^-1 = qi^n w_a, from curl_sum); closeLeftTrace. Model/GLnClosureLift.lean: map_closeL (any monoidal functor), glnFunctor_closeD and glnFunctor_closeD_eq_ptr: glnFunctor maps the OS closure of g to qi^n * ptr(wt)(glnFunctor.map g).
- Item 2, faithfulness: Model/GLnFaithful.lean heckeAction_injective: for m+1 <= n, H_{m+1}(q) -> End((R^n)^{tensor(m+1)}) injective over ANY CommRing with q*qi=1 (no genericity). Proof: T_w tvec(d) = tvec(d o w^-1) for strictly decreasing d (descents are pure swaps), spanning by T_w (span_cosetFam_eq_top), coordinate functionals.
STILL OPEN (not asked): injectivity of Brundan's iota_r into End_OS(E^r) as a corollary (needs lift o OS-heckeAction = conjugated crossing heckeAction); m+1 > n kernel (q-Schur/Temperley-Lieb quotient) not studied.

2026-10-12 (cont. 2) Faithfulness inside OS CLOSED: Model/GLnOSFaithful.lean OS_heckeAction_injective: for m+1 <= n, Brundan iota_{m+1}: H_{m+1}(q) -> End_OS(E^{tensor(m+1)}) in OS(q,qi,q^n,[n]_q) is injective, any CommRing with q*qi=1. Via map_gen (lift of OS crossing gen = Phi-conjugate of GL_n gen, coherence by monoidal) and lift_heckeAction (glnFunctor o iota = conj_Phi o rho as AlgHoms), then heckeAction_injective. Sorry-free, axioms clean. Open: m+1 > n kernel.
