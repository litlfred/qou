---
# qou-s9au
title: 'The rank-N Ocneanu family: z_N = q^(2N-1)(q^2-1)/(q^(2N)-1); D is N=2'
status: completed
type: task
priority: high
created_at: 2026-09-04T02:45:39Z
updated_at: 2026-09-04T02:46:13Z
parent: qou-8lxd
---

PROVED + MEASURED 2026-09-04, commit be970862cf.

**z_N = (q - 1/q) q^(2N)/(q^(2N)-1)**, exact in q, verified in sympy N=1..8 against
computations/y_lambda_su_n.py (the corpus's own hook-content producer).

  z_1 = q                    gl(1)
  z_2 = q^3/(q^2+1)          CONVENTION D, on the nose; z_2(q0) matches REG_ZD
  z_3 = q^5/(q^4+q^2+1)      = 0.44930480909020786056 at q0 -- the flavour value
  z_N -> q - 1/q             the Hecke coefficient; uncapped limit, never attained

Carriers: QOU/Eightfold/OcneanuRankFamily.lean (16 decls, sorry-free) +
computations/ocneanu_rank_family_closed_form_probe.py (symbolic, no float64).

TWO CONSEQUENCES.
(1) Rank is recoverable from z: strictly antitone in N for q>1, hence injective
    (conventionD_forces_rank_two). Convention D is a RANK COMMITMENT, not a
    normalisation choice. Lean form of ocneanu_N_lockin_probe.py.
(2) The row cap IS the volume form. Cell (N+1,1) has content -N, so the numerator
    picks up [0]_q = 0. Last block surviving at rank N is the column (1^N) =
    Lambda^N of the fundamental = the determinant; first to die is (1^(N+1)).
    So the N of VolumeFormDegree.rank_eq_of_volumeForm and the N of the trace are
    ONE number: condition 5 (Lambda^2 V = 1) and convention D are the same
    commitment stated twice.

NOT proved: that markovParam N IS the SU(N) Markov parameter (hook-content
principal specialisation -- no Mathlib API, verified in the probe and cited); that
a rank-3 trace EXISTS compatible with axioms 1-4 (z_3 is a specification, not a
construction). Which rank the axioms supply is qou-j3w6, still the author's.
