#!/usr/bin/env python3
"""How many admissible functionals are there REALLY? The answer depends on the
class, and "closed at two" is closed in only one of them.

Bean `qou-99qc`. Owner asked, on the statement that the admissible options are
the augmentation (+12.470 %) and the Markov trace at z_D (-43.157 %):
*"what are options for admissible? others?"*

`qou-99qc` records the admissible set as "closed at two elements", from solving
`y_(1^3)(z) = 0` -- quadratic, roots `z = q` and `z_D = q^3/(q^2+1)`. That is
true and is CLOSED WITHIN THE ONE-PARAMETER MARKOV FAMILY `tr_M^z`. It is not
a statement about every functional that descends to the convention-D quotient,
and this probe measures the three nested classes so the scope is explicit.

  admissibility  ==  annihilates the (1^3) block, which convention D quotients
                     away (the GNS embedding H_inf/rad = TL_inf places the
                     theory in the two-row quotient)

  CLASS                                   admissible subspace
  ------------------------------------    -------------------
  all linear functionals on H_3(q)        measured below
  trace functionals (phi(ab) = phi(ba))   measured below
  Markov traces tr_M^z                    two POINTS: z = q, z = z_D

WHAT THIS SETTLES, and it is not a widening of the options:

Every dimension is computed here, not asserted. The load-bearing result is
whether the admissible TRACE space is exactly `span{aug, tr_M(z_D)}` -- if it
is, then relaxing "Markov trace" to "trace" adds no new DIRECTION, only the
line through the two already named, which is precisely the one-parameter fit
`qou-99qc` refuses. Relaxing further to "all linear functionals" does add
directions, but at the cost of the trace property, which is what connects the
functional to knot invariants at all.

AND THE WEIGHT IS NOT MYSTERIOUS. `qou-99qc` records that a unique weight
`w* = -q^2 + q + 1/q` reproduces `Delta`. Because `Delta` is supported on
`{gamma, sigma_0, sigma_1}`, `tr_M^z(Delta) = h^2/2 - h*z` is AFFINE in z, so
matching any target is interpolation of the PARAMETER:

    w* = (1 - z_D) / (q - z_D)

i.e. `w*` is the barycentric coordinate of the inadmissible point `z = 1`
between the two admissible ones. That is a restatement of "one equation, one
unknown", not an independent justification -- so it is the fit in closed form,
not a derivation of it. Verified symbolically below rather than asserted.

SCOPE. Scope-(a) throughout: nothing is refuted, nothing wired, no c_k
proposed, no content block edited. Exact sympy over Q(q); the pin appears only
in a display print. Writes a witness recording the measured dimensions.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

from qbeta_net_trace_invariance_probe import (  # noqa: E402
    BASIS, N, LEFT, basis_vec, length, q, h, reg_char,
)


def main() -> int:
    checks: list[dict] = []

    def chk(name, ok, detail):
        checks.append({"name": name, "passed": bool(ok), "detail": detail})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
        return bool(ok)

    print(__doc__.splitlines()[0])
    print()
    ok = True
    Z = sp.Symbol("z")
    Z_D = q**3 / (q**2 + 1)

    # ---- the (1^3) ideal: the q-antisymmetrizer ---------------------------
    # The sign rep sends every generator to -1/q, so the (1^3)-isotypic ideal
    # is the common eigenspace  sigma_i . x = (-1/q) x.  Computed, not quoted.
    S0, S1 = LEFT[1], LEFT[2]
    M = sp.Matrix.vstack(S0 + sp.eye(N) / q, S1 + sp.eye(N) / q)
    ns = M.nullspace()
    ok &= chk("the_1cubed_ideal_is_one_dimensional", len(ns) == 1,
              f"common (-1/q)-eigenspace of both generators has dim {len(ns)}")
    e_sign = sp.simplify(ns[0]) if ns else None

    # ---- CLASS 1: all linear functionals ---------------------------------
    # phi annihilates a 1-dim ideal  <=>  one linear condition on 6 unknowns.
    A = sp.Matrix([[sp.simplify(e_sign[i]) for i in range(N)]])
    dim_all_adm = N - A.rank()
    ok &= chk("class1_all_linear_functionals_admissible_dim", dim_all_adm == 5,
              f"dim = {dim_all_adm} of {N} (one condition: kill the ideal)")

    # ---- CLASS 2: trace functionals --------------------------------------
    # the irreducible characters, as covectors. chi_(3) IS the augmentation.
    chi_3 = sp.Matrix([[q ** length(BASIS[i]) for i in range(N)]])
    chi_111 = sp.Matrix([[(-1 / q) ** length(BASIS[i]) for i in range(N)]])
    reg = sp.Matrix([[sp.simplify(reg_char(basis_vec(i))) for i in range(N)]])
    # regular character = sum_lambda dim(lambda) * chi_lambda = chi_3 + 2*chi_21 + chi_111
    chi_21 = sp.simplify((reg - chi_3 - chi_111) / 2)

    trace_space = sp.Matrix.vstack(chi_3, chi_21, chi_111)
    ok &= chk("class2_trace_space_is_three_dimensional", trace_space.rank() == 3,
              f"rank{{chi_(3), chi_(2,1), chi_(1^3)}} = {trace_space.rank()} "
              "= the number of partitions of 3")

    adm_traces = sp.Matrix.vstack(chi_3, chi_21)
    ok &= chk("class2_admissible_trace_space_is_TWO_dimensional",
              adm_traces.rank() == 2,
              f"rank{{chi_(3), chi_(2,1)}} = {adm_traces.rank()} "
              "(the (1^3) character is the one direction removed)")
    for nm, cv in (("chi_3", chi_3), ("chi_21", chi_21)):
        r = sp.simplify((cv * e_sign)[0])
        ok &= chk(f"class2_{nm}_annihilates_the_ideal", r == 0,
                  f"{nm}(e_sign) = {r}")
    ok &= chk("class2_chi_1cubed_does_NOT_annihilate_it",
              sp.simplify((chi_111 * e_sign)[0]) != 0,
              f"chi_(1^3)(e_sign) = {sp.simplify((chi_111 * e_sign)[0])} "
              "-- the control: the removed direction is genuinely removed")

    # ---- CLASS 3: the Markov family, and whether it SPANS class 2 ---------
    TR = [sp.Integer(1), Z, Z, Z**2, Z**2, Z * (h * Z + 1)]
    co_aug = sp.Matrix([[sp.simplify(t.subs(Z, q)) for t in TR]])
    co_trD = sp.Matrix([[sp.simplify(t.subs(Z, Z_D)) for t in TR]])
    co_net = sp.Matrix([[sp.simplify(t.subs(Z, 1)) for t in TR]])

    ok &= chk("class3_trM_at_z_equals_q_IS_the_augmentation",
              sp.simplify(co_aug - chi_3) == sp.zeros(1, N),
              "tr_M^{z=q} == chi_(3) on all six basis elements "
              "(so the second root adds no third option)")

    # THE LOAD-BEARING ONE: does {aug, tr_M(z_D)} span the whole admissible
    # trace space, or is it a proper subspace of it?
    both = sp.Matrix.vstack(co_aug, co_trD)
    joined = sp.Matrix.vstack(co_aug, co_trD, chi_3, chi_21)
    ok &= chk("class3_the_two_Markov_points_SPAN_the_admissible_trace_space",
              both.rank() == 2 and joined.rank() == 2,
              f"rank{{aug, tr_D}} = {both.rank()}, "
              f"rank{{aug, tr_D, chi_(3), chi_(2,1)}} = {joined.rank()} "
              "-- equal, so relaxing 'Markov trace' to 'trace' adds NO new "
              "direction, only the line through the two already named")

    ok &= chk("control_net_is_outside_the_admissible_trace_space",
              sp.Matrix.vstack(both, co_net).rank() == 3,
              "rank{aug, tr_D, net} = 3 > 2 (reproduces qou-99qc's rank-3 "
              "exclusion from a different construction)")

    # ---- the weight is interpolation of the PARAMETER, not a derivation ---
    # Delta is supported on {gamma, sigma_0, sigma_1}, so tr_M^z(Delta) is
    # affine in z and any target is hit by exactly one weight.
    Delta = sp.Matrix([h**2 / 2, -h / 2, -h / 2, 0, 0, 0])
    trM_Delta = sp.simplify((sp.Matrix([TR]) * Delta)[0])
    ok &= chk("trM_of_Delta_is_AFFINE_in_z",
              sp.degree(sp.Poly(sp.expand(trM_Delta), Z), Z) == 1,
              f"tr_M^z(Delta) = {sp.simplify(trM_Delta)} -- degree 1 in z, "
              "which is WHY one weight always exists")
    w_bary = sp.simplify((1 - Z_D) / (q - Z_D))
    w_bean = -q**2 + q + 1 / q
    ok &= chk("w_star_is_the_barycentric_coordinate_of_z_equals_1",
              sp.simplify(w_bary - w_bean) == 0,
              f"(1 - z_D)/(q - z_D) = {sp.factor(w_bary)} = qou-99qc's w*. "
              "So w* is where z=1 sits between the two admissible roots -- "
              "a restatement of one-equation-one-unknown, not a derivation")
    ok &= chk("w_star_carries_the_supergolden_polynomial",
              sp.simplify(w_bary + (q**3 - q**2 - 1) / q) == 0,
              f"w* = -(q^3 - q^2 - 1)/q. The same factor appears in "
              f"N(q,1) = {sp.factor((1 - q) * ((q**2 + 1) - q**3))}, because "
              "both measure how far z=1 is from being a root -- shared cause, "
              "not independent evidence")

    q0 = Q_MP
    w0 = (1 - q0**3 / (q0**2 + 1)) / (q0 - q0**3 / (q0**2 + 1))
    print(f"\n      w*(q0) = {mp.nstr(w0, 20)}")

    print()
    print(f"  {sum(c['passed'] for c in checks)}/{len(checks)} checks passed")

    witness = {
        "name": "qbeta-admissible-functional-hierarchy",
        "description": (
            "Measures how many functionals are admissible under convention D "
            "(annihilating the (1^3) block) in three nested classes. All "
            "linear: 5 of 6 dimensions. Traces: 2 of 3. Markov traces: two "
            "points, z = q (which IS the augmentation) and z_D. The two "
            "Markov points SPAN the admissible trace space, so relaxing "
            "'Markov trace' to 'trace' adds no new direction -- only the line "
            "through them, which is qou-99qc's one-parameter fit. The weight "
            "w* that hits Q_beta is the barycentric coordinate (1-z_D)/(q-z_D) "
            "of the inadmissible z=1 between the two roots, because Delta's "
            "support makes tr_M^z(Delta) affine in z -- the fit in closed "
            "form, not a derivation of it. Scope-(a); nothing wired."),
        "assertions": checks,
        "admissible_dimensions": {
            "all_linear_functionals": f"{dim_all_adm} of {N}",
            "trace_functionals": f"{adm_traces.rank()} of {trace_space.rank()}",
            "markov_traces": "2 points (z = q, z_D); z = q IS the augmentation",
        },
        "w_star": {
            "closed_form": "(1 - z_D)/(q - z_D) = -(q^3 - q^2 - 1)/q",
            "at_proton_pin": mp.nstr(w0, 25),
            "status": "the fit in closed form; NOT derived",
        },
        "caveats": [
            "Does NOT widen the honest options. The extra admissible traces "
            "are exactly the line through the two already named.",
            "Dropping the trace condition does add directions (5 of 6), but a "
            "non-trace functional is not a Markov trace and loses the link to "
            "knot invariants that motivates the construction.",
            "Says nothing about which functional SHOULD be used -- qou-99qc's "
            "owner call is untouched.",
            "Delta_S only; qou-avt5's finding that Delta_S is not the "
            "exhibited nucleon-word difference is unaffected.",
        ],
        "related": [
            "QOU.QBeta.ConventionDAdmissibleRoots",
            "computations/qbeta/qbeta_admissible_span_prune_probe.py",
            "computations/qbeta/qbeta_published_form_is_the_inadmissible_z1_probe.py",
        ],
        "source": "bean qou-99qc",
        "scriptFile": Path(__file__).name,
    }
    WitnessBuilder.stamp_staleness_metadata(
        witness, script_path=__file__, engine="python+sympy",
        q0_anchor="proton",
        q0_anchor_reason=(
            "Display only. Every dimension and every identity is exact over "
            "Q(q) and pin-free; q0 enters solely to print w*(q0)."),
        q0_value=Q_50_DIGIT_STR)
    out = Path(__file__).resolve().parent / "qbeta-admissible-functional-hierarchy.witness.json"
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"  witness -> {out.name}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
