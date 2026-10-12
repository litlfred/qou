---
# qou-slck
title: '#7705 dispatch B: GL_n vector rep K^n with the Hecke R-matrix as a nondegenerate OS(z,t) datum; go to the trace'
status: in-progress
type: task
priority: normal
created_at: 2026-10-12T18:13:10Z
updated_at: 2026-10-12T19:07:30Z
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
