#!/usr/bin/env python3
"""Which basis are the two crossing-energy channels written in?

Settles bean ``qou-yfro`` (relabel the two crossing-energy channels) by
identifying the basis structurally instead of by physical analogy.

The corrected split (PR #4764, ``observations/crossing-energy-decomposition``)
reads, for a composite carrying ``p`` positive and ``m`` negative crossings,

    E_cross = p*q - m/q
            = (1/2)(p - m)(q + 1/q)  +  (1/2)(p + m)(q - 1/q)
              ^ bar-even, coeff Q       ^ bar-odd, coeff c/2

``def:crossing-energy`` assigns the two *Hecke eigenvalues* of ``sigma_i`` --
``+q`` to a positive crossing and ``-1/q`` to a negative one -- so ``E_cross``
is a sum of eigenvalues, one per crossing.  Both the eigenvalue pair
``{q, -1/q}`` and the parity pair ``{cosh L, sinh L}`` are bases of the same
rank-2 free module.  This probe computes the change of basis between them.

The result decides the naming question:

  * If the change of basis were diagonal, one channel *would be* the
    antisymmetric Hecke eigen-channel ``e_-`` -- the object
    ``prop:em-coupling-projection`` uses to carry the electromagnetic
    content -- and the withdrawn "EM channel" label could simply be moved
    to whichever channel that is.
  * If every entry is nonzero, no channel is proportional to an eigenvalue,
    both channels weight ``-1/q`` with equal magnitude, and *neither* can
    be the EM channel by that route.

It is the second.  See ``docs/audits/`` for the write-up.

Conventions
-----------
q_0 is the **experimental (proton) pin** per the 2026-08-07 owner directive:
``qou_substrate.constants.Q``.  No muon-built cache is read.
"""

from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

_REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_REPO / "tools" / "qou-substrate" / "python"))

from qou_substrate import WitnessBuilder  # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

DPS = 50


def main() -> int:
    wb = WitnessBuilder("crossing-energy-channel-basis", engine="python")
    wb.set_description(
        "Change of basis between the Hecke eigenvalue pair {q, -1/q} and the "
        "bar-parity pair {cosh L, sinh L} spanning the crossing-energy "
        "channels; settles bean qou-yfro."
    )
    wb.set_content_block("obs:crossing-energy-decomposition")

    q, p, m = sp.symbols("q p m", positive=True)
    lam = sp.log(q)

    # --- The two Hecke eigenvalues of sigma_i, i.e. the crossing weights. ---
    ev_pos = q          # weight of a positive crossing
    ev_neg = -1 / q     # weight of a negative crossing

    # --- The two bar-parity basis vectors. ---
    cosh_L = (q + 1 / q) / 2          # bar-EVEN weight  = [2]_q / 2
    sinh_L = (q - 1 / q) / 2          # bar-ODD  weight  = h / 2

    checks: dict[str, bool] = {}

    # 1. cosh/sinh really are cosh(ln q) / sinh(ln q).
    checks["cosh_is_cosh_ln_q"] = sp.simplify(cosh_L - sp.cosh(lam)) == 0
    checks["sinh_is_sinh_ln_q"] = sp.simplify(sinh_L - sp.sinh(lam)) == 0

    # 2. The corrected split reconstructs E_cross exactly (residual 0).
    e_cross = p * ev_pos + m * ev_neg
    split = (p - m) * cosh_L + (p + m) * sinh_L
    residual_split = sp.simplify(sp.expand(e_cross - split))
    checks["split_residual_zero"] = residual_split == 0

    # 2b. The *old* (pre-#4764) pairing leaves the documented residual 2m/q.
    old_split = (p + m) * cosh_L + (p - m) * sinh_L
    residual_old = sp.simplify(sp.expand(old_split - e_cross))
    checks["old_pairing_residual_is_2m_over_q"] = (
        sp.simplify(residual_old - 2 * m / q) == 0
    )

    # 3. THE CENTRAL COMPUTATION: the change of basis.
    #    Express each parity vector in the eigenvalue basis {ev_pos, ev_neg}.
    #        cosh_L = a11*ev_pos + a12*ev_neg
    #        sinh_L = a21*ev_pos + a22*ev_neg
    a11, a12, a21, a22 = sp.symbols("a11 a12 a21 a22")
    sol_c = sp.solve(
        sp.Poly(sp.expand((a11 * ev_pos + a12 * ev_neg - cosh_L) * q), q).coeffs(),
        [a11, a12],
        dict=True,
    )[0]
    sol_s = sp.solve(
        sp.Poly(sp.expand((a21 * ev_pos + a22 * ev_neg - sinh_L) * q), q).coeffs(),
        [a21, a22],
        dict=True,
    )[0]
    M = sp.Matrix(
        [[sol_c[a11], sol_c[a12]], [sol_s[a21], sol_s[a22]]]
    )
    # Expect [[1/2, -1/2], [1/2, 1/2]]
    M_expected = sp.Matrix([[sp.Rational(1, 2), sp.Rational(-1, 2)],
                            [sp.Rational(1, 2), sp.Rational(1, 2)]])
    checks["change_of_basis_matches"] = sp.simplify(M - M_expected) == sp.zeros(2, 2)
    n_zero_entries = sum(1 for e in M if sp.simplify(e) == 0)
    checks["change_of_basis_has_no_zero_entry"] = n_zero_entries == 0
    checks["change_of_basis_invertible"] = sp.simplify(M.det()) != 0

    # 3b. Equal-magnitude weighting of the antisymmetric eigenvalue -1/q:
    #     |a12| == |a22|.  This is the sharp form of "neither channel
    #     isolates e_-".
    checks["equal_magnitude_on_antisym_eigenvalue"] = (
        sp.simplify(sp.Abs(M[0, 1]) - sp.Abs(M[1, 1])) == 0
    )

    # 4. Identify the two parity vectors as symmetric functions of sigma_i.
    #    Hecke relation: sigma^2 = h*sigma + 1, i.e. sigma^2 - h*sigma - 1 = 0.
    h = q - 1 / q
    tr_sigma = ev_pos + ev_neg          # = h
    det_sigma = ev_pos * ev_neg         # = -1
    disc = tr_sigma**2 - 4 * det_sigma  # = h^2 + 4
    bracket2 = q + 1 / q                # = [2]_q
    checks["trace_is_h"] = sp.simplify(tr_sigma - h) == 0
    checks["det_is_minus_one"] = sp.simplify(det_sigma + 1) == 0
    checks["disc_is_bracket2_squared"] = sp.simplify(disc - bracket2**2) == 0
    checks["bar_odd_weight_is_half_trace"] = sp.simplify(sinh_L - tr_sigma / 2) == 0
    checks["bar_even_weight_is_half_sqrt_disc"] = (
        sp.simplify(cosh_L - bracket2 / 2) == 0
    )

    # 5. Canonical form  E_cross = Q*[2]_q + (c/2)*h  with Q = w/2, c = p+m.
    Q_charge = (p - m) / 2
    c_total = p + m
    canonical = Q_charge * bracket2 + (c_total / 2) * h
    checks["canonical_form_residual_zero"] = (
        sp.simplify(sp.expand(canonical - e_cross)) == 0
    )

    # 6. The antisymmetric Hecke projector, for the record: its normaliser is
    #    the bar-even weight [2]_q, but it is not a channel.
    #        e_- = (q*1 - sigma) / [2]_q   (projects onto eigenvalue -1/q)
    #    Check on eigenvalues: e_- acts as 0 on q and as 1 on -1/q.
    e_minus_on_pos = sp.simplify((q - ev_pos) / bracket2)
    e_minus_on_neg = sp.simplify((q - ev_neg) / bracket2)
    checks["e_minus_kills_sym_eigenvalue"] = e_minus_on_pos == 0
    checks["e_minus_fixes_antisym_eigenvalue"] = sp.simplify(e_minus_on_neg - 1) == 0

    # --- Numerics at the experimental (proton) pin. ---
    def fmt(x, n=30):
        """Fixed-precision decimal string for a sympy expression."""
        return str(sp.N(x, n))

    q0 = sp.Float(Q_50_DIGIT_STR, DPS)
    subs0 = {q: q0}
    num = {
        "q_0": fmt(q0, 30),
        "cosh_lambda": fmt(cosh_L.subs(subs0), 30),
        "sinh_lambda": fmt(sinh_L.subs(subs0), 30),
        "bracket_2_q": fmt(bracket2.subs(subs0), 30),
        "h": fmt(h.subs(subs0), 30),
        "tanh_ln_q": fmt((sinh_L / cosh_L).subs(subs0), 30),
    }

    # 7. Worked multiplicity table (the per-crossing vs channel-total trap).
    table = []
    for pp, mm in [(1, 0), (3, 0), (2, 1), (5, 2), (3, 3)]:
        ratio_expr = (
            sp.nan
            if pp == mm
            else ((pp + mm) / sp.Integer(pp - mm)) * (sinh_L / cosh_L)
        )
        table.append(
            {
                "n_plus": pp,
                "n_minus": mm,
                # exact half-integer; float() threw away the exactness for
                # no gain — sympy prints it as "p/q" or an integer.
                "Q": str(sp.Rational(pp - mm, 2)),
                "crossings": pp + mm,
                "channel_total_ratio": (
                    "undefined (Q=0)"
                    if pp == mm
                    else fmt(ratio_expr.subs(subs0), 12)
                ),
                "per_crossing_ratio": fmt((sinh_L / cosh_L).subs(subs0), 12),
            }
        )

    all_pass = all(checks.values())

    wb.add_parameter("q_0_pin", "experimental/proton")
    wb.add_parameter("uses_muon_built_cache", False)
    wb.add_parameter("dps", DPS)
    wb.add_data("checks", {k: bool(v) for k, v in checks.items()})
    wb.add_data("change_of_basis_parity_from_eigenvalues", [
        [str(M[0, 0]), str(M[0, 1])],
        [str(M[1, 0]), str(M[1, 1])],
    ])
    wb.add_data("n_zero_entries_in_change_of_basis", n_zero_entries)
    wb.add_data("numerics_at_q0", num)
    wb.add_data("multiplicity_table", table)
    wb.add_data("canonical_form", "E_cross = Q*[2]_q + (c/2)*h")
    wb.add_data("basis_identification", {
        "bar_even_weight": "cosh(ln q) = [2]_q/2 = sqrt(disc(sigma))/2",
        "bar_odd_weight": "sinh(ln q) = h/2 = tr(sigma)/2",
        "bar_even_multiplicity": "n_+ - n_- = writhe w = 2Q",
        "bar_odd_multiplicity": "n_+ + n_- = crossing number c",
    })

    # Assertions compare a computed value against an expected one; the prose
    # for each lives in `interpretation` below.
    wb.add_assertion(
        "n_zero_entries_in_change_of_basis",
        n_zero_entries,
        0,
        source="sympy exact",
    )
    wb.add_assertion(
        "corrected_split_residual",
        str(residual_split),
        "0",
        source="sympy exact",
    )
    wb.add_assertion(
        "old_pairing_residual",
        str(sp.simplify(residual_old)),
        str(sp.simplify(2 * m / q)),
        source="sympy exact",
    )
    wb.add_assertion(
        "checks_failed",
        sum(1 for v in checks.values() if not v),
        0,
        source="sympy exact",
    )
    wb.add_data(
        "interpretation",
        {
            "channels_are_not_hecke_eigenchannels": (
                "Every entry of the change of basis from {q,-1/q} to "
                "{cosh,sinh} is +-1/2; no parity vector is proportional to a "
                "Hecke eigenvalue, and both weight -1/q with equal magnitude "
                "1/2. Structural exclusion (scope b) of the route "
                "'crossing-energy channel = e_- eigen-channel' -- the route "
                "prop:em-coupling-projection uses to carry EM."
            ),
            "corrected_split_residual_zero": (
                "PR #4764's corrected pairing reconstructs E_cross exactly; "
                "the old pairing leaves 2*n_-/q."
            ),
            "parity_weights_are_symmetric_functions_of_sigma": (
                "bar-odd weight = tr(sigma)/2 = h/2; bar-even weight = "
                "sqrt(disc(sigma))/2 = [2]_q/2, with disc = h^2+4 = [2]_q^2."
            ),
        },
    )

    wb.add_caveat(
        "This is a structural (scope-b) exclusion of the e_- route only. It "
        "does not exclude an electromagnetic reading of either channel "
        "reached by some other, stated route; no such route is currently in "
        "the corpus. Physical relabelling remains an author call."
    )
    wb.add_caveat(
        "notation-register-table3-data calls h = q - 1/q 'the Hecke-relation "
        "discriminant'. The discriminant of sigma^2 - h*sigma - 1 is h^2 + 4 "
        "= [2]_q^2, not h; h is the trace. Flagged, not edited here."
    )

    path = wb.save()

    print("=" * 68)
    print("crossing-energy channel basis probe   (proton pin, %d dps)" % DPS)
    print("=" * 68)
    for k, v in checks.items():
        print(f"  [{'PASS' if v else 'FAIL'}] {k}")
    print()
    print("  change of basis  parity <- eigenvalues:")
    print(f"    cosh L = {M[0,0]}*(q) + ({M[0,1]})*(-1/q)")
    print(f"    sinh L = {M[1,0]}*(q) + ({M[1,1]})*(-1/q)")
    print(f"    zero entries: {n_zero_entries}   det: {sp.simplify(M.det())}")
    print()
    print("  canonical form:  E_cross = Q*[2]_q + (c/2)*h")
    print(f"    at q_0: [2]_q = {num['bracket_2_q']}")
    print(f"            h     = {num['h']}")
    print()
    print(f"  ALL CHECKS {'PASS' if all_pass else 'FAIL'}")
    print(f"  witness -> {path}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
