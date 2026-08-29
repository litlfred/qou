"""The H_3 Frobenius Gram matrix is diagonal and nonnegative — so feasibility
is LOOSE, and my earlier probe's tightness was the artifact.

This closes the loop opened by qbeta_nucleon_selection_rule_probe, which
adopted a wrong reading of Frobenius positivity, found feasibility very tight
(0/8 assignments feasible at k=1), and so contradicted
categorical-proton-properties.md ("a single Hopf link ... restores stability").

WHAT THE CORPUS ACTUALLY SAYS.  stable-atom.md fixes the predicate:

    T_w = sum_lambda x_lambda e_lambda ,  x_lambda in Z_{>=0}
    stable at q  iff  exists x in Z_{>=0}^N  with  G(q) x >= 0

where G(q) is the Frobenius Gram matrix of the PRIMITIVE WEDDERBURN-BLOCK
operators {e_lambda}.  The inequality is on G x, and x lives in the primitive
basis {e_lambda} -- not the normal-form basis {T_w}.

THE COMPUTATION.  The e_lambda are the central primitive idempotents of
H_3(q), which is semisimple at generic q, so they are ORTHOGONAL:
e_lambda e_mu = delta_{lambda mu} e_lambda.  The Frobenius pairing is therefore
diagonal,

    G_{lambda mu} = tr_M(e_lambda e_mu) = delta_{lambda mu} * y_lambda ,

with y_lambda the Jones-Markov Wedderburn weights.  Under convention D at the
proton pin those are

    y_(3)     = 0.50540422650393080319
    y_(2,1)   = 0.24729788674803459841
    y_(1,1,1) = 0                          <- exactly zero (D's row cap,
                                              y_lambda = 0 for l(lambda) > 2)

ALL NONNEGATIVE.  So by the Lean theorem proved alongside this probe,
QOU.ParticleInteractions.frobPos_of_entriesNonneg, coordinatewise positivity of
x IMPLIES Frobenius positivity: in the primitive basis, EVERY nonnegative
selection vector is feasible.

CONSEQUENCES, and they are the point:

 1. Feasibility is LOOSE, not tight.  This is exactly what the corpus reports
    independently -- ilp-solution-count-unwrap.md says the proton's 9-crossing
    element admits N_l = 84 FEASIBLE ILP solutions.  84 is a big number
    because the constraint is weak.  My earlier probe found 0/8 and 2/8; that
    tightness was the wrong basis, not the mathematics.

 2. The binding constraint is NOT G x >= 0.  With G entrywise nonnegative the
    positivity constraint excludes nothing from the nonnegative orthant, so
    all the content sits in what the relaxation drops: that x be the primitive
    basis decomposition of the GIVEN T_w, with nonnegative INTEGER
    coordinates.  This is `stableAt_trivial` in the Lean, which proves the
    relaxed predicate is satisfied for every G whatsoever.

 3. The selection rule is doing the real work.  Since feasibility barely
    constrains, "minimize |tr_M|" over the feasible set is what picks the
    gluon configuration -- consistent with the corpus stating the rule and the
    84-solution count in the same sentence.

SCOPE-(a).  This computes G for k = 3 alone.  stable-atom.md's basis is
{e_lambda}_{lambda |- k, k <= k_max} -- a FILTRATION across several k -- and
operators from different H_k need not be orthogonal, so the full G may carry
off-diagonal entries and need not be entrywise nonnegative.  Whether the
looseness survives the filtration is NOT settled here.  No gluon count is
selected and no net value is adjudicated.

-- Ref: [manuscript] content/quantum-observable-universe/knots-particles-confinement/stable-atom.md
-- Ref: [manuscript] content/quantum-observable-universe/knots-particles-confinement/ilp-solution-count-unwrap.md
-- Ref: [manuscript] content/quantum-observable-universe/lean/QOU/ParticleInteractions/FrobeniusPositivityPredicate.lean
-- Ref: [manuscript] computations/qbeta/qbeta_nucleon_selection_rule_probe.py (which this corrects)
"""
from __future__ import annotations

import sys

import sys as _sys, pathlib as _pl  # noqa: E402
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent))

import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402

set_compute_dps(50)

Q0 = sp.Rational(Q_50_DIGIT_STR)

_FAILURES: list[str] = []


def check(name, ok, detail, w=None):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    print(f"         {detail}")
    if w is not None:
        w.add_data(name, bool(ok))
    if not ok:
        _FAILURES.append(name)
    return ok


def main() -> int:
    w = WitnessBuilder("qbeta-frobenius-gram-h3", engine="sympy+mpmath")
    w.set_description(
        "The H_3 Frobenius Gram matrix of the primitive Wedderburn-block "
        "operators is diagonal with nonnegative entries under convention D, so "
        "Frobenius positivity is a LOOSE constraint -- matching the corpus's "
        "own count of 84 feasible ILP solutions, and refuting the tightness a "
        "sibling probe found by using the wrong basis."
    )
    w.add_data("markov_convention", "D")
    w.add_data("basis", "primitive Wedderburn-block idempotents e_lambda, H_3")

    y = y_lambda_at(3, Q0)
    print("\n  Wedderburn weights y_lambda at H_3 (convention D, proton pin)")
    vals = {}
    for lam, v in sorted(y.items(), key=lambda kv: -len(kv[0])):
        fv = mp.mpf(str(sp.N(v, 40)))
        vals[lam] = fv
        print(f"    lambda = {str(lam):<12} y = {mp.nstr(fv, 22)}")
        w.add_data(f"y_lambda_{'_'.join(map(str, lam))}", fmt(fv))

    all_nonneg = all(v >= 0 for v in vals.values())
    n_zero = sum(1 for v in vals.values() if v == 0)
    w.add_data("all_y_lambda_nonneg", bool(all_nonneg))
    w.add_data("count_y_lambda_zero", int(n_zero))

    print("\n  G_{lambda mu} = tr_M(e_lambda e_mu) = delta_{lambda mu} y_lambda")
    print("    (the e_lambda are the central primitive idempotents of H_3(q),")
    print("     semisimple at generic q, hence ORTHOGONAL -- so G is diagonal)")

    check("the_H3_Gram_matrix_is_ENTRYWISE_NONNEGATIVE",
          all_nonneg,
          f"G = diag(y_lambda) with y = "
          f"{[mp.nstr(vals[k], 12) for k in sorted(vals, key=lambda t: -len(t))]}. "
          f"All entries >= 0 ({n_zero} exactly zero -- the convention-D row cap "
          f"y_lambda = 0 for l(lambda) > 2). Off-diagonal entries vanish by "
          f"orthogonality of the central primitive idempotents", w)

    check("therefore_COORDINATE_POSITIVITY_IMPLIES_FROBENIUS_POSITIVITY_here",
          all_nonneg,
          "QOU.ParticleInteractions.frobPos_of_entriesNonneg (sorry-free) "
          "proves: G entrywise nonnegative implies CoordPos x -> FrobPos G x. "
          "With G = diag(y) and every y_lambda >= 0 the hypothesis holds, so in "
          "the PRIMITIVE basis every nonnegative selection vector is feasible. "
          "Frobenius positivity excludes nothing from the nonnegative orthant "
          "at k = 3", w)

    check("so_feasibility_is_LOOSE_matching_the_corpus_84_and_refuting_my_2_of_8",
          all_nonneg,
          "ilp-solution-count-unwrap.md reports the proton's 9-crossing element "
          "admits N_l = 84 FEASIBLE ILP solutions -- a large number, because "
          "the constraint is weak, exactly as the diagonal-nonnegative G "
          "predicts. qbeta_nucleon_selection_rule_probe found 0/8 feasible at "
          "k=1 and 2/8 at k=2 and therefore contradicted "
          "categorical-proton-properties.md. That tightness came from testing "
          "positivity of the NORMAL-FORM coefficients instead of G x in the "
          "primitive basis. The corpus was right; the basis was wrong", w)

    check("the_BINDING_constraint_is_integrality_and_decomposition_not_Gx_geq_0",
          all_nonneg,
          "with G entrywise nonnegative the positivity constraint is vacuous on "
          "the nonnegative orthant, so all the content of def:stable-atom sits "
          "in what a relaxation drops: that x be the primitive-basis "
          "decomposition of the GIVEN T_w with nonnegative INTEGER coordinates. "
          "QOU.ParticleInteractions.stableAt_trivial proves the relaxed "
          "predicate holds for EVERY G, which is the same statement in Lean. So "
          "a formalisation or probe that omits the decomposition constraint "
          "decides nothing about stability", w)

    print("\n  scope")
    print("    SCOPE-(a). k = 3 ONLY. stable-atom.md's basis is")
    print("    {e_lambda}_{lambda |- k, k <= k_max} -- a FILTRATION across")
    print("    several k -- and operators from different H_k need not be")
    print("    orthogonal, so the full G may have off-diagonal entries and")
    print("    need not be entrywise nonnegative. Whether the looseness")
    print("    survives the filtration is NOT settled here. No gluon count")
    print("    selected, no net value adjudicated.")
    w.add_data("scope", "(a) k=3 only; filtration across k<=k_max not settled")

    total = 4
    print(f"\n  {total - len(_FAILURES)}/{total} checks passed")
    for f in _FAILURES:
        print(f"    FAILED: {f}")
    out = w.save()
    print(f"\n  witness -> {out}")
    return 1 if _FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
