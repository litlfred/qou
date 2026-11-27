#!/usr/bin/env python3
"""mu-p residual, open worldline: do projector insertions on 4_1 force the w^2 dressing?

Bean qou-6gf9.  Open-worldline companion of
``mu_p_projector_insertion_w_order_probe.py`` (PR #9445, closed normalisation).
Companion Lean:
``folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/MuPOpenWorldlineWOrder.lean``.

The worldline is left open: the (1,1)-tangle reduction normalises by the unknot,
tr_M(1) = y_3 + 2 y_21 = 1, instead of by tr_M(4_1).  The observables are the
un-normalised traces tr_M(X . 4_1); the knot trace tr_M(4_1) is itself a member
of the class.  The closed class of #9445 is this class divided by tr_M(4_1).

Question
--------
PR #9362 left ``-(3 alpha/(4 pi)) w^2`` (``w = q + q^-1 - 2``) as an UNWIRED
working assumption for the correction to ``m_mu/m_e = Vol(4_1)/hbar_q^2``.
It would be *derived* only if a natural observable of the muon carrier
``4_1 = (s1 s2^-1)^2`` had vanishing ``O(w^0)`` and ``O(w^1)`` terms and a
forced ``w^2`` coefficient.  This probe tests the Hecke projector-insertion
class: the photon projector ``e_i = (q - s_i)/[2]_q`` inserted once or twice
into the 4_1 word, SU(2) Markov trace (weights y_3, y_21, y_111 = 0),
normalised by tr_M(4_1).

Everything is EXACT: sympy over Q(q), then eliminated to Q(w) using the
bar-evenness of the bar-symmetric sums.  No float anywhere in the algebra.
The only numerics are 80-dps mpmath evaluations at the proton pin, used for
the comparison section (where the empirical claim lives), never in the
algebra.

Findings asserted
-----------------
1. Each single insertion is slot-independent; e1 and e2 insertions are bar
   images of each other, so the bar-symmetric sum is a rational function of w.
2. The covariant open observables (knot trace tr_M(4_1), singles S1, doubles D,
   connected C) are exact rational functions of w with NONZERO O(w^0) and O(w^1)
   terms.
3. Every denominator is a power of (w + 2) = [2]_q: the only pole is w = -2, so
   the radius of convergence is 2.  The closed class of #9445 had radius
   |2cos(pi/10) - 2| = 0.098; the difference is exactly the 1/tr_M(4_1)
   normalisation (closed pair = open pair / tr_M(4_1), checked exactly).
4. Non-forcing: the coefficient matrix (rows O(1), O(w), O(w^2); columns
   1, tr_M(4_1), S1, D, C) has rank 3, so the combinations killing O(1) and O(w)
   form a 3-dim space on which the w^2 coefficient takes EVERY value.
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import _path_bridge  # noqa: E402, F401
from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps(80)
mp.mp.dps = 80

from qou_substrate import codata as _codata  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from witness_base import WitnessBuilder, q0_comparison  # noqa: E402

q = sp.symbols("q", positive=True)
w = sp.symbols("w")
s = sp.symbols("s")
r = sp.symbols("r")

I3 = sp.eye(3)
A1 = sp.Matrix([[q, 0, 0], [0, 0, 1], [0, 1, q - 1 / q]])
A2 = sp.Matrix([[0, 1, 0], [1, q - 1 / q, 0], [0, 0, q]])
A2I = A2.inv()
TWO_Q = q + 1 / q
E1 = (q * I3 - A1) / TWO_Q
E2 = (q * I3 - A2) / TWO_Q
Y3 = (q**4 + 1) / (q**2 + 1) ** 2
Y21 = q**2 / (q**2 + 1) ** 2
WORD = [A1, A2I, A1, A2I]  # 4_1 = (s1 s2^-1)^2, exponent sum 0 -> chi_triv = 1
Z = sp.factor(sp.simplify(Y3 + Y21 * ((A1 * A2I * A1 * A2I).trace() - 1)))
PROJ = {"e1": E1, "e2": E2}


def corr(ins: dict[int, list]) -> sp.Expr:
    """Open-worldline Markov trace tr_M(X . 4_1); e_i kills the trivial rep, so only y_21 survives."""
    m = sp.eye(3)
    for j, letter in enumerate(WORD):
        for e in ins.get(j, []):
            m = m * e
        m = m * letter
    return sp.simplify(Y21 * m.trace())  # open worldline: no 1/tr_M(4_1)


def to_w(expr: sp.Expr) -> sp.Expr:
    """Exact elimination q -> w for a bar-even rational function (resultant in s = q + 1/q)."""
    num, den = sp.fraction(sp.together(sp.simplify(expr)))
    res = sp.resultant(sp.expand(num - r * den), q**2 - s * q + 1, q)
    sols = sp.solve(sp.factor(res), r)
    if len(sols) != 1:
        raise RuntimeError(f"elimination not unique: {sols}")
    return sp.factor(sols[0].subs(s, w + 2))


def taylor(expr: sp.Expr, n: int = 3) -> list[sp.Rational]:
    ser = sp.series(expr, w, 0, n).removeO()
    return [sp.nsimplify(ser.coeff(w, k)) for k in range(n)]


def main() -> int:
    # ---- exact algebra -------------------------------------------------
    singles = {}
    for k in range(4):
        for name, e in PROJ.items():
            singles[(name, k)] = corr({k: [e]})
    slot_independent = all(
        sp.simplify(singles[(n, k)] - singles[(n, 0)]) == 0 for n in PROJ for k in range(4)
    )
    bar_image = sp.simplify(singles[("e1", 0)].subs(q, 1 / q) - singles[("e2", 0)]) == 0

    s1 = sp.simplify(sum(singles.values()))
    d_full = 0
    c_conn = 0
    keys = list(singles.keys())
    for a in keys:
        for b in keys:
            if a[1] > b[1]:
                continue
            ins: dict[int, list] = {}
            ins.setdefault(a[1], []).append(PROJ[a[0]])
            ins.setdefault(b[1], []).append(PROJ[b[0]])
            c = corr(ins)
            d_full += c
            c_conn += c - singles[a] * singles[b]

    pair_q = singles[("e1", 0)] + singles[("e2", 0)]
    obs = {
        "knot_trace_trM_41": to_w(Z),
        "pair_single_e1_plus_e2": to_w(pair_q),
        "S1_all_singles": to_w(s1),
        "D_all_doubles": to_w(d_full),
        "C_connected_doubles": to_w(c_conn),
    }
    coeffs = {k: taylor(v, 3) for k, v in obs.items()}

    # closed class (#9445) = open class / tr_M(4_1): exact check on the pair
    closed_pair_9445 = (s**4 - 6 * s**2 + 7) / (s**4 - 5 * s**2 + 5)
    closed_is_open_over_knot = sp.simplify(
        obs["pair_single_e1_plus_e2"] / obs["knot_trace_trM_41"] - closed_pair_9445.subs(s, w + 2)
    ) == 0

    # radius: every denominator is a power of (w + 2)
    den_powers = {}
    for k, v in obs.items():
        den = sp.factor(sp.fraction(sp.together(v))[1])
        rest = sp.simplify(den / (w + 2) ** sp.degree(den, w))
        den_powers[k] = (int(sp.degree(den, w)), str(rest))
    only_pole_w_minus_2 = all(sp.simplify(sp.sympify(r_)).is_number for _, r_ in den_powers.values())

    # non-forcing rank test on columns (1, knot, S1, D, C)
    cols = [[1, 0, 0]] + [coeffs[k] for k in ("knot_trace_trM_41", "S1_all_singles",
                                              "D_all_doubles", "C_connected_doubles")]
    mat = sp.Matrix(cols).T  # rows: O(1), O(w), O(w^2)
    rank3 = mat.rank()
    kernel = mat[:2, :].nullspace()
    w2_values = [sp.simplify((mat[2, :] * v)[0]) for v in kernel]
    w2_free = rank3 == 3 and len(kernel) == 3 and any(x != 0 for x in w2_values)
    # the Lean witness (MuPOpenWorldlineWOrder.open_w2_not_forced): (5/8, -9/8, 11/8) on (1, knot, pair)
    kp = sp.Matrix([[1, 0, 0], coeffs["knot_trace_trM_41"], coeffs["pair_single_e1_plus_e2"]]).T
    lean_witness = list(kp * sp.Matrix([sp.Rational(5, 8), sp.Rational(-9, 8), sp.Rational(11, 8)]))

    # ---- comparison section (empirical inputs live ONLY here) ----------
    q_p = q_at(80)
    q_mu = q_muon_at(80)
    w_p = q_p + 1 / q_p - 2
    alpha = 1 / mp.mpf(_codata.codata("inverse fine-structure constant").value_str)
    cand_coeff = 3 * alpha / (4 * mp.pi)
    radius_open = mp.mpf(2)
    radius_closed = 2 - 2 * mp.cos(mp.pi / 10)
    min_class_w2 = min(mp.fabs(mp.mpf(sp.Rational(c[2]).p) / sp.Rational(c[2]).q) for c in coeffs.values())

    print("=" * 78)
    print(" mu-p: open-worldline projector insertions on 4_1, exact w-order structure")
    print("=" * 78)
    print(f"  single insertions slot-independent: {slot_independent}; e1 <-> e2 bar images: {bar_image}")
    for k, v in obs.items():
        print(f"  {k:26s} = {v}")
        print(f"  {'':26s}   O(1), O(w), O(w^2) = {coeffs[k]}")
    print(f"  closed (#9445) pair = open pair / tr_M(4_1): {closed_is_open_over_knot}")
    print(f"  denominators (power of w+2, remaining factor): {den_powers}")
    print(f"  radius open = 2, closed = {mp.nstr(radius_closed, 20)}; pin w = {mp.nstr(w_p, 15)}, "
          f"w/2 = {mp.nstr(w_p / radius_open, 12)}")
    print(f"  rank (1,knot,S1,D,C) on (O1,Ow,Ow2) = {rank3}; w^2 values on O1=Ow=0 kernel: {w2_values}")
    print(f"  Lean witness (5/8,-9/8,11/8) on (1,knot,pair) -> {lean_witness} (expect [0,0,1])")
    print(f"  candidate w^2 coefficient 3 alpha/(4 pi) = {mp.nstr(cand_coeff, 15)}; "
          f"smallest |class w^2 coeff| = {mp.nstr(min_class_w2, 10)}")

    wb = WitnessBuilder("mu-p-open-worldline-w-order", engine="sympy+mpmath")
    wb.set_description(
        "Exact Q(w) structure of open-worldline (unknot-normalised) Hecke photon-projector insertions on "
        "the muon carrier 4_1 = (s1 s2^-1)^2 (qou-6gf9): nonzero O(1) and O(w) terms, only pole w = -2 "
        "(radius 2), and rank-3 non-forcing of the w^2 coefficient. Companion of the closed-normalisation "
        "probe of PR #9445."
    )
    wb.add_data(
        "exact_observables_in_w",
        {k: {"rational_function": str(v), "taylor_O1_Ow_Ow2": [str(c) for c in coeffs[k]]}
         for k, v in obs.items()},
    )
    wb.add_data(
        "structure",
        {
            "trM_41_in_q": str(Z),
            "slot_independent_singles": slot_independent,
            "e1_e2_bar_images": bar_image,
            "closed_pair_equals_open_pair_over_trM_41": closed_is_open_over_knot,
            "denominator_powers_of_w_plus_2": {k: v[0] for k, v in den_powers.items()},
            "radius_open": "2",
            "radius_closed_9445": "2 - 2*cos(pi/10)",
            "coefficient_matrix_rank": int(rank3),
            "w2_values_on_O1_Ow_kernel": [str(x) for x in w2_values],
            "lean_witness_5_8_m9_8_11_8_on_1_knot_pair": [str(x) for x in lean_witness],
        },
    )
    wb.add_data(
        "comparison_at_proton_pin",
        {
            "q_p": fmt(q_p),
            "w_p": fmt(w_p),
            "w_p_over_open_radius": fmt(w_p / radius_open),
            "w_p_over_closed_radius": fmt(w_p / radius_closed),
            "candidate_w2_coeff_3alpha_over_4pi": fmt(cand_coeff),
            "smallest_class_w2_coeff_abs": fmt(min_class_w2),
            "note": "alpha is CODATA-2022 here; comparison only, never an input to the algebra or the Lean.",
        },
    )
    wb.add_assertion(
        name="single_insertions_slot_independent_and_bar_paired",
        computed=str(slot_independent and bar_image),
        expected="True",
        source="exact sympy over Q(q)",
    )
    wb.add_assertion(
        name="every_covariant_observable_has_nonzero_O1_and_Ow",
        computed=str(all(c[0] != 0 and c[1] != 0 for c in coeffs.values())),
        expected="True",
        source="exact Taylor coefficients in w",
    )
    wb.add_assertion(
        name="only_pole_is_w_minus_2_and_closed_is_open_over_knot",
        computed=str(only_pole_w_minus_2 and closed_is_open_over_knot),
        expected="True",
        source="denominators factor as (w+2)^k; closed pair of #9445 = open pair / tr_M(4_1)",
    )
    wb.add_assertion(
        name="w2_coefficient_not_forced_rank3",
        computed=str(w2_free and lean_witness == [0, 0, 1]),
        expected="True",
        source="rank of 3x5 coefficient matrix; nullspace of the O(1),O(w) rows; Lean open_w2_not_forced",
    )
    out_path = wb.save(
        q0_comparison(
            muon=fmt(q_mu),
            proton=fmt(q_p),
            reason="algebra is pin-free; the comparison section evaluates at the proton pin only",
            dps=80,
        )
    )
    ok = all(a.passed for a in wb.assertions)
    print(f"\n  Witness written -> {out_path} (assertions={len(wb.assertions)}, allPassed={ok})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
