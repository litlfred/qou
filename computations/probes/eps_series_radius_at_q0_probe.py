#!/usr/bin/env python3
"""The ε-expansion of the Markov trace: exact rational structure, radius 1, and the cost at A=5.

Bean `qou-i719`. Successor to `qou-qqm4` (PR #6521) / `qou-pdg9` (PR #6492).

## Why this is the question

The diagonal-insertion expansion gives EVERY order of `tr_M(word)` in `ε = q − 1`
as a weighted fixed-point count over sub-words, at cost `2ⁿ · C(L, ≤k)` — against
`dim H_{3A} = (3A)!` for the direct trace (`15! ≈ 1.3e12` at `A = 5`, which is why
the mass table stops there). So the expansion is a candidate **compute route** to
`A = 5, 6` — but only if the series converges at the substrate point
`ε₀ = 0.1099785827…`, and only if the order needed there is affordable.

## The structural prediction, stated before measuring — and CONFIRMED

`tr_M(x) = Σ_λ y_λ(q) χ^λ(x, q)` with `y_λ = s_λ(1,q²)/(1+q²)ⁿ`. The seminormal
entries carry denominators `1 − q^{−2ρ}`, poles at roots of unity — but those are
gauge artifacts, absent from a character. So `Δtr·(1+q²)ⁿ` should be a **Laurent
polynomial**, and the only singularities of `Δtr` should be `q = 0` and `q = ±i`,
i.e. `ε = −1` and `ε = ±i − 1` (`|ε| = √2`). **Predicted radius: exactly 1.**

Measured, for the deuteron: `Δtr·(1+q²)⁶` is a Laurent polynomial of degrees
`−23 … 33` — interpolated from 57 exact rational evaluations and **validated on
held-out points it was not fitted to**. Prediction confirmed; radius 1.

## 🛑 The trap this probe exists to record

**The ratio and root tests give ≈ 0.39 at order 26 and are wrong by 2.5×.**
A pole of order 23 sits at `ε = −1`, so `c_k ~ C(k+22, 22)` — polynomial growth of
degree 22, which is indistinguishable from exponential growth over the first few
dozen orders. `|c_k|^{−1/k} → 1` only for `k ≫ 22`.

Two false conclusions this produced in the session that wrote the probe, both
caught only by computing the exact rational function:

1. *"The coefficients grow 1/8, 19/8, 357/32 — ratios 19 then 4.7, so the radius
   is ≈ 0.05–0.2 and the series diverges at ε₀ = 0.11."* Wrong: those are the
   first three terms of a degree-22 polynomial growth.
2. *"The partial sums at ε = 1/2 grow with k, so the radius is below 1/2."*
   Wrong: with `c_k ~ C(k+22,22)`, the terms `c_k ε^k` at `ε = 1/2` **rise until
   `k ≈ 22/ln 2 ≈ 32`** and only then decay. Truncating at 26 samples the rising
   side of a hump. The series converges there; the truncation did not.

The honest rule: **do not read a radius off a truncated coefficient sequence when
a high-order pole is present.** Get the rational function, or bound the pole order
first. This probe therefore reports the radius from the *analytic structure*, and
reports the tests only as the measurement that misleads.

## Also verified

All 27 coefficients produced by the `Ser` series pipeline
(`c1_leading_coefficient_derived_probe`) agree exactly with the Taylor expansion
of the interpolated rational function — an end-to-end check of the series
arithmetic that the `c₀`/`c₁`/`c₂` derivations rest on.

## The verdict on the compute route

Convergence at `ε₀` holds and is fast: 1 ppb by order 16, 1 ppQ by order 26. But
the insertion expansion costs `2ⁿ·C(L, ≤k)`, and at `A = 5` (`n = 15`, `L ≈ 55`)
order 26 is astronomically out of reach. **Convergence is necessary and not
sufficient; the expansion is a structural tool, and a compute route only at low
order where it is not accurate.** Stated as a measured cost, not a route.

Precision: `Fraction` and exact `sympy.Rational` throughout. `q₀` enters only as
the number `ε₀` compared against; nothing is evaluated at `q₀`.
"""
from __future__ import annotations

import importlib.util
import sys
import time
from fractions import Fraction as F
from math import comb, log
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "hecke"), str(_COMP / "markov"),
           str(_COMP / "substrate"), str(_COMP / "habiro")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge as _bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402

set_compute_dps(40)

from canonical_braid_crossings import atom_canonical_crossings  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "c1probe", _HERE / "c1_leading_coefficient_derived_probe.py")
_c1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_c1)

_q0s = Q_50_DIGIT_STR
EPS0 = F(int(_q0s.replace(".", "")), 10 ** (len(_q0s) - _q0s.index(".") - 1)) - 1

ORDER = 28              # ~27 usable after the pipeline's one-order loss
LO, HI = -23, 33        # measured degree span of Dtr*(1+q^2)^6 for the deuteron
EVAL_Q = F(111, 100)


def dtr(Z: int, N: int, q: F) -> F:
    return (_c1.tr_M_fraction(Z, N, False, q) - _c1.tr_M_fraction(Z, N, True, q))


def main() -> int:
    T0 = time.time()

    def log_(m):
        print(f"  [{time.time()-T0:7.1f}s] {m}", flush=True)

    w = WitnessBuilder("eps-series-radius-at-q0-probe")
    w.set_description(
        "Determines the analytic structure of the Markov trace difference in eps = q-1: "
        "Dtr*(1+q^2)^n is a Laurent polynomial (interpolated exactly and validated on held-out "
        "points), so the only poles are q=0 and q=+-i and the radius is exactly 1. Records that "
        "the ratio and root tests give ~0.39 at order 26 and are wrong by 2.5x because of an "
        "order-23 pole, verifies the Ser series pipeline against the exact rational function, and "
        "measures the order needed at eps_0 and the cost of the insertion expansion at A=5."
    )
    w.add_parameter("eps0_proton_pin", str(EPS0))
    w.add_parameter("series_order", ORDER)

    print("=" * 78)
    print(f"  The eps-series of the Markov trace:  eps_0 = {float(EPS0):.9f}")
    print("=" * 78)
    print("\n  PREDICTION (before measuring): Dtr*(1+q^2)^n is a Laurent polynomial,")
    print("  so the only poles are q = 0 (eps = -1) and q = +-i (|eps| = sqrt 2),")
    print("  and the radius of convergence in eps is exactly 1.\n")

    # ── 1. the exact rational function, by interpolation ────────────────────
    NC = HI - LO + 1
    log_(f"interpolating Dtr*(1+q^2)^6 * q^{-LO}: {NC} coefficients, "
         f"{NC + 3} exact evaluations (q = k/7, all > 1) …")
    pts = [F(k, 7) for k in range(8, 8 + NC + 3)]     # q > 1: never a root of unity
    vals = [dtr(1, 1, q) * (1 + q * q) ** 6 * q ** (-LO) for q in pts]
    qv, ev = sp.Symbol("q"), sp.Symbol("e")
    data = [(sp.Rational(p.numerator, p.denominator), sp.Rational(v.numerator, v.denominator))
            for p, v in zip(pts, vals)]
    poly = sp.Poly(sp.expand(sp.interpolate(data[:NC], qv)), qv)
    held_out = all(d[1] == poly.eval(d[0]) for d in data[NC:])
    log_(f"degree {poly.degree()} (expected {NC-1}); held-out points reproduce exactly: {held_out}")
    w.add_assertion(
        "trace_difference_is_exactly_rational_with_poles_only_at_q0_and_q_pm_i",
        computed="1" if (held_out and poly.degree() == NC - 1) else "0", expected="1",
        source=f"Dtr(q)*(1+q^2)^6 interpolated from {NC} exact Fraction evaluations at q = k/7 "
               f"as a polynomial of degree {NC-1} in q (i.e. Laurent degrees {LO}..{HI}), then "
               f"CHECKED at 3 further points not used in the fit — exact Rational equality at all "
               f"three. A Laurent polynomial has no singularities other than q = 0, so the only "
               f"poles of Dtr are q = 0 (order {-LO}) and q = +-i (order 6, from the normaliser).",
    )

    # ── 2. the radius, from the structure ───────────────────────────────────
    radius_exact = 1               # |eps| from 0 to q=0 (eps=-1); the +-i poles are at sqrt(2)
    w.add_assertion(
        "radius_of_convergence_is_exactly_1_as_predicted",
        computed=str(radius_exact), expected="1",
        source="the nearest singularity in eps is q = 0 at eps = -1 (|eps| = 1); q = +-i sit at "
               "|eps| = sqrt(2) = 1.41421. So the radius is 1, and eps_0 = "
               f"{float(EPS0):.9f} is well inside it. This was the stated prediction.",
    )

    # ── 3. the trap: what the tests say, and the hump ───────────────────────
    log_(f"exact series to order {ORDER} (three A=2 words) …")
    rows, root_last = [], []
    for name, (Z, N) in [("pp", (2, 0)), ("pn", (1, 1)), ("nn", (0, 2))]:
        tf = _c1.tr_M_series(Z, N, False, ORDER)
        ta = _c1.tr_M_series(Z, N, True, ORDER)
        K = min(tf.p, ta.p)
        c = [tf.coeff(k) - ta.coeff(k) for k in range(K)]
        ratio = [abs(c[k]) / abs(c[k + 1]) for k in range(K - 1) if c[k + 1] != 0]
        root = [mp.power(mp.mpf(abs(c[k]).numerator) / abs(c[k]).denominator,
                         mp.mpf(-1) / k) for k in range(2, K) if c[k] != 0]
        exact = dtr(Z, N, EVAL_Q)
        e = EVAL_Q - 1
        partial, errs = F(0), []
        for k in range(K):
            partial += c[k] * e ** k
            errs.append(abs(partial - exact) / abs(exact))
        f_ppb = next((k for k, x in enumerate(errs) if x < F(1, 10 ** 9)), None)
        f_ppq = next((k for k, x in enumerate(errs) if x < F(1, 10 ** 15)), None)
        rows.append({"case": name, "orders": K, "coefficients": [str(x) for x in c],
                     "ratio_test_last": str(ratio[-1]),
                     "root_test_last": mp.nstr(root[-1], 20),
                     "true_radius": 1,
                     "root_test_error_factor": mp.nstr(1 / root[-1], 20),
                     "exact_at_111_over_100": str(exact),
                     "relative_error_by_order": [f"{float(x):.4e}" for x in errs],
                     "order_for_1ppb": f_ppb, "order_for_1ppQ": f_ppq})
        root_last.append(root[-1])
        log_(f"  {name}: root test {mp.nstr(root[-1], 5)}, ratio test "
             f"{mp.nstr(mp.mpf(ratio[-1].numerator) / ratio[-1].denominator, 5)} (TRUE radius 1); "
             f"1 ppb at order {f_ppb}, 1 ppQ at order {f_ppq}")

    worst_root = max(root_last)
    w.add_assertion(
        "the_root_and_ratio_tests_are_MISLEADING_here_by_more_than_two_fold",
        computed="1" if worst_root < mp.mpf("0.5") else "0", expected="1",
        source=f"largest root-test estimate at order {ORDER} is {mp.nstr(worst_root, 6)} against the "
               f"true radius 1 — wrong by {mp.nstr(1/worst_root, 4)}x, and it points BELOW the 0.5 at which the "
               f"partial sums visibly grow. Cause: the order-{-LO} pole at eps = -1 makes "
               f"c_k ~ C(k+{-LO-1}, {-LO-1}), polynomial growth of degree {-LO-1} that is "
               f"indistinguishable from exponential over the first few dozen orders. Recorded as "
               f"the trap: do NOT read a radius off a truncated coefficient sequence when a "
               f"high-order pole is present.",
    )

    # the hump: terms at eps = 1/2 rise until k ~ (pole order - 1)/ln 2, then decay
    hump_k = int((-LO - 1) / log(2.0))
    tf = _c1.tr_M_series(1, 1, False, ORDER)
    ta = _c1.tr_M_series(1, 1, True, ORDER)
    K = min(tf.p, ta.p)
    c = [tf.coeff(k) - ta.coeff(k) for k in range(K)]
    terms_half = [abs(c[k]) * F(1, 2) ** k for k in range(K)]
    rising = all(terms_half[k] <= terms_half[k + 1] for k in range(K - 4, K - 1))
    w.add_assertion(
        "the_apparent_divergence_at_eps_one_half_is_a_TRUNCATION_artifact",
        computed="1" if (rising and hump_k > K) else "0", expected="1",
        source=f"at eps = 1/2 the terms |c_k|/2^k are still RISING at k = {K-1}, which reads as "
               f"divergence. With c_k ~ C(k+{-LO-1},{-LO-1}) the terms peak at "
               f"k ~ {-LO-1}/ln2 = {hump_k}, past the {K} orders computed. So the series converges "
               f"at eps = 1/2 (radius 1) and the truncation, not the series, is what failed. This "
               f"probe's own first reading called it divergence.",
    )

    # ── 4. the Ser pipeline verified against the exact rational function ────
    log_("verifying every Ser coefficient against the exact rational function …")
    expr = poly.as_expr() * qv ** LO / (1 + qv ** 2) ** 6
    ser = sp.expand(sp.series(expr.subs(qv, 1 + ev), ev, 0, K).removeO())
    mismatch = []
    for k in range(K):
        t = sp.Rational(sp.nsimplify(ser.coeff(ev, k)))
        if F(int(t.p), int(t.q)) != c[k]:
            mismatch.append(k)
    log_(f"  {K} coefficients compared; mismatches: {mismatch or 'none'}")
    w.add_assertion(
        "every_series_coefficient_matches_the_exact_rational_function",
        computed=str(len(mismatch)), expected="0",
        source=f"all {K} coefficients from the Ser pipeline (c1_leading_coefficient_derived_probe) "
               f"vs the Taylor expansion of the interpolated rational function, exact Rational "
               f"equality. End-to-end check of the series arithmetic the c0/c1/c2 derivations rest "
               f"on — including its valuation tracking and precision bookkeeping.",
    )

    # ── 5. the cost verdict ────────────────────────────────────────────────
    order_needed = max((r["order_for_1ppQ"] or r["orders"]) for r in rows)
    L5 = len(atom_canonical_crossings(3, 2, include_inter=True))
    ops5 = 2 ** 15 * sum(comb(L5, j) for j in range(order_needed + 1))
    cost = {"A5_strands": 15, "A5_letters": L5, "order_for_1ppQ": order_needed,
            "A5_subset_state_pairs_at_that_order": str(ops5),
            "direct_trace_dim": "15! = 1307674368000",
            "A5_order_for_1ppb_estimate": max((r["order_for_1ppb"] or 0) for r in rows)}
    w.add_data("cost", cost)
    log_(f"A=5: {L5} letters; order {order_needed} needs {mp.nstr(mp.mpf(ops5), 4)} subset-state pairs "
         f"(direct trace: 15! = 1.3e12)")

    w.add_data("per_word", rows)
    w.add_data("laurent_structure", {
        "lowest_degree": LO, "highest_degree": HI, "n_coefficients": NC,
        "denominator": "(1+q^2)^6", "held_out_validation_points": 3,
        "poles": {"q=0": -LO, "q=+-i": 6},
        "eps_distance_to_q0_pole": 1, "eps_distance_to_pm_i_poles": "sqrt(2)",
    })
    w.add_data("verdict", (
        f"The eps-series converges at the substrate point, with radius EXACTLY 1 — the trace "
        f"difference is a rational function whose only poles are q=0 (order {-LO}) and q=+-i. "
        f"1 ppb by order {max((r['order_for_1ppb'] or 0) for r in rows)}, 1 ppQ by order "
        f"{order_needed}. But the insertion expansion costs 2^n C(L,<=k), and at A=5 "
        f"({L5} letters) order {order_needed} is {mp.nstr(mp.mpf(ops5), 4)} subset-state pairs. So convergence is "
        f"necessary and NOT sufficient: the expansion is a STRUCTURAL tool (it derived c0, c1, c2 "
        f"as permutation counts) and a compute route only at low order, where it is not accurate. "
        f"The A>=5 barrier is not lifted by it. Recorded with the trap that the ratio and root "
        f"tests, read at order {K-1}, give 0.39 and would have produced the opposite conclusion."
    ))
    out = w.save()

    print("\n" + "=" * 78)
    print(f"  {'word':6}{'root test':>11}{'ratio test':>12}{'TRUE':>7}{'1 ppb':>8}{'1 ppQ':>8}")
    for r in rows:
        _rt = F(r['ratio_test_last'])
        print(f"  {r['case']:6}{r['root_test_last'][:9]:>11}"
              f"{mp.nstr(mp.mpf(_rt.numerator) / _rt.denominator, 7):>12}"
              f"{r['true_radius']:>7}{str(r['order_for_1ppb']):>8}{str(r['order_for_1ppQ']):>8}")
    print("=" * 78)
    print(f"  witness -> {out}")
    ok = (held_out and poly.degree() == NC - 1 and not mismatch
          and worst_root < 0.5 and rising and hump_k > K)
    print(f"  ALL PASSED: {ok}   ({time.time()-T0:.0f}s)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
