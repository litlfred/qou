#!/usr/bin/env python3
"""The Laplace sum -> Laplace integral step is EXPONENTIALLY exact, not O(1/N).

Bean `qou-mlgp` (B).  Formalised in
`folio/quantum-observable-universe/lean/QOU/MathlibExt/GaussianThetaSum.lean`
(`hasSum_gaussian_theta`, sorry-free).

WHAT IS AT STAKE.  `one_loop_c_sigma_tetrahedral_probe.py` derives
`c_sigma(4_1) = 3^{-1/4}` by Laplace's method on Kashaev's sum, and the one
place the derivation could leak is the replacement of a DISCRETE sum over `k`
by a CONTINUUM Gaussian integral at the saddle:

    sum_k e^{phi(k)}  ->  e^{phi(k*)} sqrt(2 pi / |phi''(k*)|).

Naive Euler-Maclaurin bounds that step's error by `O(h)` with `h = 1`, i.e. by
`O(1/N)` relative — the SAME order as the one-loop term being extracted.  If
that were the true size, the constant would not survive the step and
`3^{-1/4}` would be an artifact.

THE POINT.  It is not the true size.  Poisson summation gives the shifted
discrete Gaussian in closed form,

    sum_{n in Z} e^{-a(n-c)^2}  =  sqrt(pi/a) . theta_2(-c, i pi / a)
                                =  sqrt(pi/a) . (1 + 2 sum_{n>=1} e^{-pi^2 n^2/a} cos(2 pi n c))

with `sqrt(pi/a) = int_R e^{-a(x-c)^2} dx` the continuum integral exactly.  So

    sum / integral  =  1 + O(e^{-pi^2/a})     uniformly in the shift `c`,

EXPONENTIALLY small, with no polynomial correction at any order.  The offset
`c` — where the saddle sits relative to the integer lattice, which is the thing
one might fear — enters only inside a `cos` multiplying an already
exponentially small factor.  That is why it was never the obstacle.

AT THE 4_1 SADDLE, CONCRETELY.  The tetrahedral probe computes
`|phi''(k*)| = 2 pi sqrt3 / N`, so `a = |phi''|/2 = pi sqrt3 / N` and

    sqrt(pi/a) = sqrt(N / sqrt3)        <- exactly the Laplace factor it uses
    e^{-pi^2/a} = e^{-pi N / sqrt3}     <- the entire discretisation error

At `N = 100` that is `10^{-79}`.  The `O(1/N)` fear is off by an exponential.

WHAT THIS PROBE CHECKS.  (1) the identity itself, to full working precision, at
assorted `(a, c)` including the irrational offsets that make lattice-alignment
arguments fail; (2) that the relative deviation from the continuum integral is
bounded by `2 e^{-pi^2/a} / (1 - 2 e^{-pi^2/a})` and DECAYS EXPONENTIALLY in
`N` along `a = pi sqrt3 / N`, not polynomially; (3) that `sqrt(pi/a)` at that
`a` reproduces the tetrahedral probe's `sqrt(N/sqrt3)`.

PRIOR ART, STATED PLAINLY.  This is Poisson summation for the Gaussian and is
classical.  Mathlib already proves the same transformation in un-theta'd form
(`Complex.tsum_exp_neg_quadratic`).  Nothing here is new mathematics; what is
new in this repo is that the step is now formalised in the theta normalisation
with a `HasSum`, so the Lean statement of `c_sigma(4_1)` no longer has to
assume it.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent
                       / "substrate"))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from mpmath import mp, mpf, mpc, exp, sqrt, pi, cos, fabs, nstr  # noqa: E402


def gauss_sum(a, c, terms: int = 400):
    """sum_{n in Z} e^{-a(n-c)^2}, summed until the terms underflow."""
    total = mpf(0)
    n0 = int(mp.floor(c))
    for k in range(-terms, terms + 1):
        n = n0 + k
        total += exp(-a * (mpf(n) - c) ** 2)
    return total


def theta2(z, tau, terms: int = 400):
    """jacobiTheta2 in Mathlib's two-variable convention:

        theta_2(z, tau) = sum_{n in Z} exp(2 pi i n z + pi i n^2 tau).
    """
    total = mpc(0)
    for n in range(-terms, terms + 1):
        total += exp(2 * pi * mpc(0, 1) * n * z + pi * mpc(0, 1) * n ** 2 * tau)
    return total


def theta_side(a, c):
    """sqrt(pi/a) . theta_2(-c, i pi / a) — the closed form."""
    return sqrt(pi / a) * theta2(-mpf(c), mpc(0, 1) * pi / a)


def main() -> int:
    set_compute_dps()

    print("=" * 74)
    print(" Laplace sum -> integral: exponentially exact, uniformly in the offset")
    print("=" * 74)

    # ---- (1) the identity, at assorted (a, c) ---------------------------
    # `a` large enough that the theta series is not the trivial `1`, and
    # offsets that are irrational / half-integer / at the 4_1 value 5/6.
    cases = [
        (mpf(1), mpf(0)),
        (mpf(1), mpf(1) / 2),
        (mpf(1), mpf(5) / 6),
        (mpf(3), mpf(5) / 6),
        (mpf(3) / 10, pi / 7),
        (mpf(20), sqrt(2) - 1),
    ]
    print("\n  (1) sum_{n in Z} e^{-a(n-c)^2}  vs  sqrt(pi/a) theta_2(-c, i pi/a)")
    print(f"\n  {'a':>10}  {'c':>14}  {'sum':>26}  {'rel err':>10}")
    identity_worst = mpf(0)
    identity_rows = []
    for a, c in cases:
        lhs = gauss_sum(a, c)
        rhs = theta_side(a, c)
        # the theta value is real (pair n <-> -n); check that too
        imag = fabs(mp.im(rhs))
        rel = fabs(lhs - mp.re(rhs)) / fabs(lhs)
        identity_worst = max(identity_worst, rel, imag)
        identity_rows.append({
            "a": nstr(a, 12), "c": nstr(c, 12),
            "sum": nstr(lhs, 22), "rel_err": nstr(rel, 6),
            "theta_imag_part": nstr(imag, 6),
        })
        print(f"  {nstr(a, 6):>10}  {nstr(c, 10):>14}  {nstr(lhs, 20):>26}"
              f"  {nstr(rel, 4):>10}")
    identity_ok = identity_worst < mpf(10) ** (-mp.dps + 8)
    print(f"\n  worst relative error (and worst spurious imaginary part): "
          f"{nstr(identity_worst, 6)}")

    # ---- (2) exponential, not polynomial, decay along a = pi sqrt3 / N --
    # This is the 4_1 saddle scaling: |phi''| = 2 pi sqrt3 / N, a = |phi''|/2.
    print("\n  (2) along the 4_1 saddle scaling a = pi sqrt3 / N:")
    print("      relative deviation of the SUM from the continuum INTEGRAL")
    print(f"\n  {'N':>6}  {'sum/integral - 1':>24}  {'bound 2e^{-pi^2/a}':>22}"
          f"  {'O(1/N) would be':>16}")
    decay_rows = []
    decay_ok = True
    for N in [4, 8, 16, 32, 64]:
        a = pi * sqrt(3) / N
        c = mpf(5) / 6          # a generic, non-lattice offset
        integral = sqrt(pi / a)
        lhs = gauss_sum(a, c)
        dev = fabs(lhs / integral - 1)
        bound = 2 * exp(-pi ** 2 / a)
        # the honest two-sided bound including the |cos| <= 1 slack
        bound_full = bound / (1 - bound) if bound < 1 else mpf("inf")
        if not (dev <= bound_full):
            decay_ok = False
        decay_rows.append({
            "N": N, "a": nstr(a, 12), "deviation": nstr(dev, 8),
            "bound_2exp": nstr(bound_full, 8), "one_over_N": nstr(mpf(1) / N, 8),
        })
        print(f"  {N:>6}  {nstr(dev, 8):>24}  {nstr(bound_full, 8):>22}"
              f"  {nstr(mpf(1) / N, 6):>16}")

    # the decay is exponential: log(dev) should be linear in N with slope
    # -pi/sqrt3, not logarithmic in N.
    N1, N2 = 16, 64
    d1 = fabs(gauss_sum(pi * sqrt(3) / N1, mpf(5) / 6)
              / sqrt(N1 / sqrt(3)) - 1)
    d2 = fabs(gauss_sum(pi * sqrt(3) / N2, mpf(5) / 6)
              / sqrt(N2 / sqrt(3)) - 1)
    slope = (mp.log(d2) - mp.log(d1)) / (N2 - N1)
    slope_pred = -pi / sqrt(3)
    slope_ok = fabs(slope - slope_pred) / fabs(slope_pred) < mpf("1e-12")
    print(f"\n  d log(deviation) / dN  measured = {nstr(slope, 18)}")
    print(f"                        predicted = -pi/sqrt3 = "
          f"{nstr(slope_pred, 18)}")
    print(f"  exponential (NOT polynomial) decay confirmed: {slope_ok}")

    # ---- (3) sqrt(pi/a) is the tetrahedral probe's Laplace factor -------
    print("\n  (3) the continuum factor at the 4_1 saddle")
    lap_ok = True
    for N in [10, 100, 1000]:
        a = pi * sqrt(3) / N
        lhs = sqrt(pi / a)
        rhs = sqrt(mpf(N) / sqrt(3))
        if fabs(lhs - rhs) / rhs > mpf(10) ** (-mp.dps + 8):
            lap_ok = False
        print(f"    N = {N:>5}:  sqrt(pi/a) = {nstr(lhs, 20):>24}"
              f"   sqrt(N/sqrt3) = {nstr(rhs, 20):>24}")

    all_ok = identity_ok and decay_ok and slope_ok and lap_ok
    print("\n" + "=" * 74)
    print(f"  ALL CHECKS {'PASS' if all_ok else 'FAIL'}")
    print("=" * 74)

    wb = WitnessBuilder("laplace-sum-theta-exactness", engine="mpmath")
    wb.add_data("identity", {
        "statement": ("sum_{n in Z} e^{-a(n-c)^2} = sqrt(pi/a) . "
                      "theta_2(-c, i pi/a), exactly, for every a > 0 and "
                      "every real offset c"),
        "lean": ("QOU.MathlibExt.hasSum_gaussian_theta (and _real), sorry-free "
                 "on [propext, Classical.choice, Quot.sound]"),
        "prior_art": ("Poisson summation for the Gaussian; Mathlib has the "
                      "same transformation un-theta'd as "
                      "Complex.tsum_exp_neg_quadratic. Nothing here is new "
                      "mathematics"),
        "rows": identity_rows,
        "worst_rel_err": nstr(identity_worst, 8),
    })
    wb.add_data("the_discretisation_error_is_exponential", {
        "expansion": ("sum / integral = 1 + 2 sum_{n>=1} e^{-pi^2 n^2/a} "
                      "cos(2 pi n c)"),
        "consequence": ("the offset c enters only inside a cos multiplying an "
                        "already exponentially small factor, so it is "
                        "uniformly harmless — it was never the obstacle"),
        "at_the_4_1_saddle": {
            "phi_second_derivative": "2 pi sqrt3 / N",
            "a": "pi sqrt3 / N",
            "continuum_factor": "sqrt(pi/a) = sqrt(N/sqrt3)",
            "error": "e^{-pi^2/a} = e^{-pi N/sqrt3}",
            "at_N_100": "about 1e-79",
        },
        "rows": decay_rows,
        "log_slope_measured": nstr(slope, 20),
        "log_slope_predicted": nstr(slope_pred, 20),
    })
    wb.add_data("what_this_closes_and_what_it_does_not", {
        "closes": ("qou-mlgp (B): the sum -> integral step in the Laplace "
                   "derivation of c_sigma(4_1) = 3^{-1/4} costs only "
                   "O(e^{-pi N/sqrt3}), so the one-loop constant survives it"),
        "does_not_close": ("qou-mlgp (A): the Euler-Maclaurin expansion of "
                           "s_k = -sum_{j<=k} log(2 sin(j pi/N)) WITH its "
                           "constant. That sum has a SINGULAR integrand at the "
                           "j = 0 endpoint, Poisson summation does not apply, "
                           "and its corrections really are polynomial "
                           "(O(log N)). See QOU/Knot/KashaevProdEndpoint.lean "
                           "for the exact endpoint any refinement must hit"),
        "still_assumed_in_lean": ("the Gaussian APPROXIMATION of phi near the "
                                  "saddle — this probe and the Lean file "
                                  "handle the sum of an EXACT Gaussian, not "
                                  "the cubic-and-higher remainder of phi"),
    })
    wb.add_assertion(
        "gaussian_sum_equals_theta_closed_form",
        computed="1" if identity_ok else "0", expected="1", tolerance="0.5",
        source="six (a, c) pairs including irrational offsets, to working dps")
    wb.add_assertion(
        "deviation_within_exponential_bound",
        computed="1" if decay_ok else "0", expected="1", tolerance="0.5",
        source="|sum/integral - 1| <= 2e^{-pi^2/a}/(1-2e^{-pi^2/a}), N = 4..64")
    wb.add_assertion(
        "decay_is_exponential_with_slope_minus_pi_over_sqrt3",
        computed="1" if slope_ok else "0", expected="1", tolerance="0.5",
        source="d log(deviation)/dN between N = 16 and N = 64 against -pi/sqrt3")
    wb.add_assertion(
        "continuum_factor_is_the_tetrahedral_probes_laplace_factor",
        computed="1" if lap_ok else "0", expected="1", tolerance="0.5",
        source="sqrt(pi/a) at a = pi sqrt3/N against sqrt(N/sqrt3)")
    out = wb.save()
    print(f"\n  witness -> {out.name}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
