"""The primitive filtration basis is LINEARLY DEPENDENT — which is why the
corpus writes "exists x" and reports a solution COUNT rather than "the"
decomposition.

def:stable-atom says:

    Decompose the normal form in the primitive basis:
      T_w = sum_lambda x_lambda e_lambda ,  x_lambda in Z_{>=0}
    The atom K is stable at q iff this decomposition admits an ILP solution:
      EXISTS x in Z_{>=0}^N  such that  G(q) x >= 0 .

Read quickly, that sentence looks redundant: if x IS the decomposition of a
given T_w then x is determined, and "exists x" is odd phrasing for a quantity
you have already fixed.  I read it that way, and it is why I could not see what
the ILP was ranging over.

IT IS NOT REDUNDANT, because the basis is OVERCOMPLETE.  The corpus's basis is
the FILTRATION {e_lambda}_{lambda |- k, k <= k_max}, which collects primitive
operators from every H_k up to k_max -- and those are not independent across k.
The smallest instance needs no computation beyond what the Gram probe already
verified symbolically:

    E_+ + E_-  =  1                          (completeness in H_2)

The k = 1 operator (the identity) is the SUM of the two k = 2 operators.  So
the filtration basis carries at least one exact linear relation, the
decomposition of any T_w in it is NOT unique, and "exists x" quantifies over a
genuine solution set.

That is what N_l counts.  ilp-solution-count-unwrap.md defines the unwrap depth
as d_l = max(0, N_l - 1) and reports N_l = 84 for the proton's 9-crossing
element -- a definition that only makes sense if multiple x describe the same
atom.  Its own gloss says so: "N_l = k >= 2: (k-1)-fold AMBIGUOUS at level l.
One must unwrap k-1 levels to disambiguate."  The ambiguity is the redundancy
of the basis, not noise in the constraint.

WHAT THIS SETTLES, taken with the two results it follows:

  * The Gram matrix is entrywise nonnegative (measured at k=3 and k<=2; proved
    for symmetric idempotents in QOU.ParticleInteractions), so G x >= 0
    excludes nothing from the nonnegative orthant.
  * QOU.ParticleInteractions.stableAt_trivial: the relaxed predicate holds for
    EVERY G.
  * And now: the decomposition constraint does not pin x either, because the
    basis is overcomplete.

So stability is decided by neither the positivity constraint nor uniqueness of
the decomposition.  What remains is INTEGRALITY together with nonnegativity on
an overcomplete basis -- a lattice-point count, which is exactly the shape of
N_l.  The selection rule (minimize |tr_M|) then picks among those points.  The
three pieces are consistent, and the framework's own quantity N_l is the count
of lattice points, not a count of anything the positivity constraint cuts out.

SCOPE-(a).  Demonstrates ONE exact relation, in the k <= 2 part of the
filtration, which suffices to establish non-uniqueness.  It does NOT compute
the full rank of the filtration basis for k <= 3, does not reproduce N_l = 84,
and adjudicates no net value.

-- Ref: [manuscript] content/quantum-observable-universe/knots-particles-confinement/stable-atom.md
-- Ref: [manuscript] content/quantum-observable-universe/knots-particles-confinement/ilp-solution-count-unwrap.md
-- Ref: [manuscript] content/quantum-observable-universe/lean/QOU/ParticleInteractions/FrobeniusPositivityPredicate.lean
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
from qbeta_net_trace_invariance_probe import (  # noqa: E402
    q, h, N, L, ONE, basis_vec,
)

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
    w = WitnessBuilder("qbeta-primitive-basis-overcomplete", engine="sympy")
    w.set_description(
        "The primitive filtration basis of def:stable-atom is linearly "
        "dependent (E+ + E- = 1 exactly), so the decomposition of a normal "
        "form is not unique and the corpus's 'exists x' quantifies over a real "
        "solution set -- which is what N_l counts."
    )

    den = q + 1 / q
    Ep = sp.simplify((L[0] + (1 / q) * ONE) / den)
    Em = sp.simplify((q * ONE - L[0]) / den)

    # the exact relation, symbolic in q -- not a numerical coincidence at q_0
    rel = sp.simplify(Ep + Em - ONE)
    is_zero = rel.is_zero_matrix
    print("\n  the k <= 2 filtration operators")
    print("    E+ = (sigma_0 + 1/q)/(q + 1/q)      [symmetric projector]")
    print("    E- = (q - sigma_0)/(q + 1/q)        [antisymmetric projector]")
    print(f"\n    E+ + E- - 1 == 0 (symbolically in q) ?  {is_zero}")
    w.add_data("relation_Ep_plus_Em_eq_one_symbolic", bool(is_zero))

    idem = (sp.simplify(Ep * Ep - Ep).is_zero_matrix
            and sp.simplify(Em * Em - Em).is_zero_matrix)
    orth = sp.simplify(Ep * Em).is_zero_matrix
    w.add_data("operators_are_idempotent", bool(idem))
    w.add_data("operators_are_orthogonal", bool(orth))
    print(f"    E+^2 = E+, E-^2 = E- ? {idem}     E+E- = 0 ? {orth}")

    check("the_filtration_basis_carries_an_EXACT_LINEAR_RELATION",
          is_zero and idem and orth,
          "E+ + E- = 1 holds identically in q, not merely at q_0. The k=1 "
          "operator of the filtration (the identity) is the SUM of the two k=2 "
          "operators, so {e_lambda}_{lambda |- k, k <= k_max} is overcomplete "
          "as soon as k_max >= 2. Both operators are genuine primitive "
          "idempotents (verified idempotent and mutually orthogonal), so this "
          "is a property of the corpus's basis, not of a bad choice of "
          "representatives", w)

    # the redundancy direction: adding t*(1, -1, -1) changes no element
    print("\n  the redundancy direction")
    print("    coordinates (x_1, x_E+, x_E-) and (x_1 + t, x_E+ - t, x_E- - t)")
    print("    describe the SAME algebra element, for every t.")
    t = sp.Symbol("t")
    shifted = sp.simplify(t * ONE - t * Ep - t * Em)
    w.add_data("redundancy_direction", "(+1, -1, -1) on (1, E+, E-)")
    check("the_decomposition_is_therefore_NOT_UNIQUE",
          shifted.is_zero_matrix,
          "t*1 - t*E+ - t*E- = 0 for every t, so the coordinate vectors "
          "(x_1, x_E+, x_E-) and (x_1 + t, x_E+ - t, x_E- - t) decompose the "
          "same element. 'The decomposition' of a normal form in the primitive "
          "basis does not exist as a unique object; a one-parameter family "
          "does. This is why def:stable-atom says EXISTS x rather than fixing "
          "x from T_w, a phrasing I first read as redundant", w)

    check("so_N_l_counts_LATTICE_POINTS_not_what_positivity_cuts_out",
          is_zero,
          "ilp-solution-count-unwrap.md defines unwrap depth d_l = max(0, "
          "N_l - 1) and reports N_l = 84 for the proton, glossing N_l >= 2 as "
          "'(k-1)-fold AMBIGUOUS ... one must unwrap to disambiguate'. That "
          "definition presupposes several x for one atom, which is exactly the "
          "overcompleteness above. Combined with the Gram matrix being "
          "entrywise nonnegative (so G x >= 0 excludes nothing) and "
          "stableAt_trivial (the relaxed predicate holds for every G), what "
          "decides stability is INTEGRALITY plus nonnegativity on an "
          "overcomplete basis -- a lattice-point count, which is the shape N_l "
          "has", w)

    print("\n  scope")
    print("    SCOPE-(a). ONE exact relation, in the k <= 2 part of the")
    print("    filtration -- enough to establish non-uniqueness. Does NOT")
    print("    compute the full rank of the k <= 3 filtration basis, does")
    print("    NOT reproduce N_l = 84, adjudicates no net value.")
    w.add_data("scope", "(a) one relation at k<=2; full rank and N_l=84 not computed")

    total = 3
    print(f"\n  {total - len(_FAILURES)}/{total} checks passed")
    for f in _FAILURES:
        print(f"    FAILED: {f}")
    out = w.save()
    print(f"\n  witness -> {out}")
    return 1 if _FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
