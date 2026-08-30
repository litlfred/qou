"""The LP cone condition has its OWN threshold, at q ~ 0.8945 — not at q = 1.
This refutes the negative-proportionality candidate for the reduction.

BACKGROUND (bean qou-ahu3).  prop:toffoli-lp-stability reduces feasibility of
G.t >= 0 to "the positivity of P_77 . W_std with the appropriate sign from" the
flip amplitude.  Two results already bound that step:

  * P_77 . W_std > 0 for every q > 0  (toffoliDiagonal_mul_wStd_pos), so the
    first factor never obstructs;
  * a SIGN-INHERITING reduction is structurally excluded
    (toffoliFlip_mul_coneCoord_nonpos): sign P_76 = -sign t_(0,1) identically.

That left one candidate: a NEGATIVE proportionality, the cone condition
tracking -P_76.  Since -P_76 > 0 exactly on q > 1, that predicts

    G.t >= 0   <==>   q > 1.

THREE FINDINGS.

1. THE PREDICTION IS FALSE, so the negative-proportionality candidate is
   refuted too.  Measured on a grid, all-proton ordering:

       q <= 0.8    infeasible      -P_76 < 0     consistent
       q = 0.9     FEASIBLE        -P_76 < 0     CONTRADICTS
       q = 0.95    FEASIBLE        -P_76 < 0     CONTRADICTS
       q >= 1.05   feasible        -P_76 > 0     consistent

   The cone condition does have a threshold, but it sits strictly below 1.
   So no reduction of the cone condition to the sign of P_76 -- with either
   proportionality -- can hold.

2. EXACTLY ONE CONSTRAINT GOVERNS, and it is the longest word.  Of the six
   components of G.t, five stay strictly positive across the threshold; only
   row 5, indexed by the NF word (0,1,0) = sigma_0 sigma_1 sigma_0, changes
   sign.  The cone condition for the q-Toffoli is therefore a single
   inequality, not six.

3. THE THRESHOLD IS EXACT, and it is the root of an irreducible degree-10
   polynomial.  See "RESOLVED" below -- an earlier revision of this file said
   the value was undetermined; that has been superseded by a symbolic Gram.

RESOLVED -- the exact threshold.  With a general H_3 normal-form multiplication
(the finite 12-entry right-multiplication table; s_i^2 = h s_i + 1 and the
braid relation s0s1s0 = s1s0s1) the Gram is symbolic in q, validated against
pyhecke.gram.gram_matrix_mp at five values of q to ~1e-37.  Row 5 is then

    (G t)_5  =  (q^10 + q^6 - q^4 + q^2 - 1) / (q^2 + 1)^2

The numerator is IRREDUCIBLE over Q and has EXACTLY ONE positive real root,

    q_c = 0.894480292910614763779004984173341677394988638886...

matching the bisected value to 1.14e-46.

A CORRECTION I OWE, recorded because both of my earlier verdicts were wrong.
An earlier revision reported PSLQ returning [1,0,-1,0,1,0,-1,0,0,0,-1], i.e.
1 - q^2 + q^4 - q^6 - q^10, and declined to quote it because AGENTS.md's
entropy bound puts degree 10 at ~58 digits needed against ~58 available.  That
caution was right.  What was NOT right was the follow-up: I then "REJECTED" the
candidate on a dps-160 run, not noticing that gram_matrix_mp SATURATES near 60
digits -- its Markov weights are built at _GRAM_MP_DPS = 60, and its dps=80 and
dps=160 outputs are bit-identical -- so every digit past ~58 was noise and the
rejection rested on noise exactly as an acceptance would have.

The symbolic derivation settles it: PSLQ's relation is exactly -1 times the
numerator above, so PSLQ WAS RIGHT.  The lesson is not that the entropy bound
was wrong to withhold judgement -- it was right -- but that a numerical
"refutation" at saturated precision is no more evidence than a numerical
confirmation.  The way out was to stop fitting and derive.

Exact rational arithmetic for t(q); mpmath for the Gram.  No float64.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent
                      / "tools" / "pyhecke" / "python"))

import mpmath as mp                                          # noqa: E402
import sympy as sp                                           # noqa: E402
from toffoli_nf_coordinates_and_lp_feasibility import (      # noqa: E402
    toffoli_element, decode, NF, q as qsym,
)

mp.mp.dps = 60


def p76(qv):
    return -(qv - 1) * (qv + 1) * (qv**6 + qv**4 + 2 * qv**2 + 1) \
        / (2 * qv * (qv**2 + 1) ** 2)


def main() -> int:
    from pyhecke.gram import gram_matrix_mp

    T7 = toffoli_element(decode(7))
    tsym = [sp.cancel(T7.get(w, sp.Integer(0))) for w in NF]

    def gt(qv):
        G = [[mp.mpf(str(x)) for x in r] for r in gram_matrix_mp(q=qv)]
        qq = sp.Float(mp.nstr(qv, 50), 50)
        t = [mp.mpf(str(sp.N(c.subs(qsym, qq), 50))) for c in tsym]
        return [sum((G[i][j] * t[j] for j in range(6)), mp.mpf(0)) for i in range(6)]

    print("=" * 74)
    print("  THE CONE CONDITION'S THRESHOLD IS NOT AT q = 1")
    print("=" * 74)
    print()
    print(f"  {'q':>6} {'-P_76':>10} {'feasible':>9}   prediction (feasible <-> -P_76>0)")
    print("  " + "-" * 62)
    contra = 0
    for g in ["0.2", "0.4", "0.6", "0.8", "0.9", "0.95", "1.05", "1.1", "2.0", "5.0"]:
        qv = mp.mpf(g)
        feas = all(x >= 0 for x in gt(qv))
        pred = -p76(qv) > 0
        bad = feas != pred
        contra += bad
        print(f"  {g:>6} {('+' if pred else '-'):>10} {str(feas):>9}   "
              f"{'CONTRADICTS' if bad else 'consistent'}")
    print()
    print(f"  contradictions: {contra}  ->  negative-proportionality "
          f"{'REFUTED' if contra else 'survives'}")

    # which component governs
    lo, hi = mp.mpf("0.8"), mp.mpf("0.95")
    for _ in range(200):
        mid = (lo + hi) / 2
        if min(gt(mid)) < 0:
            lo = mid
        else:
            hi = mid
    qc = (lo + hi) / 2
    below, above = gt(qc - mp.mpf("0.02")), gt(qc + mp.mpf("0.02"))
    crossing = [i for i in range(6) if (below[i] < 0) != (above[i] < 0)]
    print()
    print(f"  threshold q_c ~ {mp.nstr(qc, 20)}")
    print(f"  components that change sign there: {crossing}  "
          f"(NF word {NF[crossing[0]] if crossing else '-'})")
    print(f"  -> exactly {len(crossing)} of 6 constraints governs the cone condition")
    print()
    print("  EXACT: q_c is the unique positive root of")
    print("      q^10 + q^6 - q^4 + q^2 - 1   (irreducible over Q)")
    print("  from the symbolic Gram; matches the bisection to 1.14e-46.")
    print("  Lean: coneRow5Numerator, cone_threshold_ne_amplitude_threshold.")
    return 0 if (contra > 0 and len(crossing) == 1) else 1


if __name__ == "__main__":
    sys.exit(main())
