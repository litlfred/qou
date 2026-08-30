#!/usr/bin/env python3
"""The higher remainder never enters: sum and integral share the SAME expansion.

Bean `qou-mlgp`, the follow-on to (B).

WHAT (B) LEFT OPEN.  `laplace_sum_theta_exactness_probe.py` and
`QOU/MathlibExt/GaussianThetaSum.lean` show that summing an EXACT Gaussian over
the integers costs only `O(e^{-pi^2/a})` relative to integrating it.  But the
Kashaev potential is not exactly Gaussian: near the saddle

    phi(k) = phi(k*) - a (k-k*)^2 + R(k),     R(k) = sum_{q>=3} phi^(q)(k*) (k-k*)^q / q!

and the file's own header says the cubic-and-higher remainder `R` "is a separate
estimate and is still assumed".  This probe removes that caveat for the ONE
question it actually bears on — whether DISCRETISATION and the REMAINDER can
interact to produce a `1/N` term the continuum calculation would miss.

THE MECHANISM.  They cannot, and the reason is that every term of the expansion
of `e^R` against the Gaussian is a Gaussian MOMENT, and every discrete Gaussian
moment equals its continuum value up to an exponentially small error.
Differentiating the (B) identity in the shift `c`,

    sum_k e^{-a(k-c)^2} = sqrt(pi/a) . Theta(c),   Theta(c) = 1 + 2 sum_{n>=1} e^{-pi^2 n^2/a} cos(2 pi n c)

and using `d/dc e^{-a(k-c)^2} = 2a(k-c) e^{-a(k-c)^2}`, each `c`-derivative
brings down one factor of `(k-c)` and acts on `Theta` — whose every non-constant
term already carries `e^{-pi^2 n^2/a}`.  Hence for every `m`

    sum_k (k-c)^m e^{-a(k-c)^2}  =  int_R x^m e^{-a x^2} dx  +  O(e^{-pi^2/a})

(the continuum value being `0` for odd `m` and `(2p-1)!!/(2a)^p . sqrt(pi/a)`
for `m = 2p`).  Expanding `e^R` term by term therefore produces, for the SUM,
exactly the series the INTEGRAL produces, with a discrepancy that is
exponentially small at every order.  So the asymptotic expansions agree to ALL
orders in `1/N` — not merely at leading order — and `c_sigma` (and any
higher-loop coefficient one might later want) can be read off the continuum
Laplace integral.

Note what this does and does NOT say.  It says the SUM-vs-INTEGRAL discrepancy
contributes at no order.  It does not evaluate the integral's own `1/N`
corrections, and it is a statement about the expansions rather than a bound on
the actual sums (that still needs the usual window + tail control).  It closes
the specific worry, not Laplace's method in general.

WHAT THIS PROBE CHECKS.
  (1) the moment identity above, `m = 0..6`, against the exponential bound;
  (2) a MODEL with the exact `4_1` cubic and quartic coefficients, isolating the
      remainder from endpoint effects: `sum` vs `integral` decays exponentially
      in `N`, not like `1/N`;
  (3) the REAL `4_1` potential over its real range, where the residual is
      dominated by the ENDPOINT and is still exponentially small.

The `4_1` derivatives, at `theta* = 5 pi/6` where `sin = 1/2`, `csc^2 = 4`,
`cot = -sqrt3`, from `phi(k) = -(2N/pi) Lambda(k pi/N) + log(2 N sin(k pi/N))`:

    phi''   = 2 cot(theta) pi/N          = -2 sqrt3 pi/N      -> a = sqrt3 pi/N
    phi'''  = -2 (pi/N)^2 csc^2(theta)   = -8 (pi/N)^2
    phi'''' = 4 (pi/N)^3 csc^2 cot       = -16 sqrt3 (pi/N)^3

so `b3 = phi'''/6 = -(4/3)(pi/N)^2` and `b4 = phi''''/24 = -(2 sqrt3/3)(pi/N)^3`.
At the Gaussian width `sigma = (2a)^{-1/2} ~ N^{1/2}` these give
`b3 sigma^3 ~ N^{-1/2}` and `b4 sigma^4 ~ N^{-1}` — the remainder is NOT
negligible pointwise, which is why (2) is a real test and not a tautology.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent
                       / "substrate"))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from mpmath import (mp, mpf, mpc, exp, sqrt, pi, log, sin, fabs,  # noqa: E402
                    nstr, gamma, quad, inf, clsin)


def lobachevsky(theta):
    """Lambda(theta) = -int_0^theta log|2 sin t| dt = Cl_2(2 theta)/2."""
    return clsin(2, 2 * theta) / 2


# ---------------------------------------------------------------------------
# (1) discrete Gaussian moments vs continuum moments
# ---------------------------------------------------------------------------

def discrete_moment(a, c, m, reach=None):
    """sum_{k in Z} (k-c)^m e^{-a(k-c)^2}, summed well past the Gaussian tail."""
    if reach is None:
        reach = int(20 / sqrt(a)) + 40
    k0 = int(mp.floor(c))
    total = mpf(0)
    for k in range(k0 - reach, k0 + reach + 1):
        x = mpf(k) - c
        total += x ** m * exp(-a * x ** 2)
    return total


def theta2(z, tau, terms: int = 300):
    """theta_2(z, tau) = sum_{n in Z} exp(2 pi i n z + pi i n^2 tau)."""
    total = mpc(0)
    for n in range(-terms, terms + 1):
        total += exp(2 * pi * mpc(0, 1) * n * z + pi * mpc(0, 1) * n ** 2 * tau)
    return total


def check_tilt():
    """The identity Lean now proves as `hasSum_gaussian_theta_tilt`:

        sum_k e^{-a(k-c)^2 + t(k-c)}
          = e^{t^2/4a} . sqrt(pi/a) . theta_2(-(c + t/2a), i pi/a)

    The prefactor `e^{t^2/4a} sqrt(pi/a)` is exactly the CONTINUUM generating
    function `int_R e^{-ax^2+tx} dx`, so the whole discrete-vs-continuum
    discrepancy — at every moment simultaneously — is the single theta factor.
    """
    print("\n  (1b) the tilted sum (moment generating function)")
    print("       discrete MGF  vs  continuum MGF x theta_2")
    print(f"\n  {'a':>7}  {'c':>10}  {'t':>7}  {'discrete MGF':>22}"
          f"  {'rel err':>11}  {'theta_2 - 1':>12}")
    rows = []
    ok = True
    for a, c, t in [(mpf(1), mpf(5) / 6, mpf(1)), (mpf(1), mpf(5) / 6, -mpf(2)),
                    (mpf(1) / 2, pi / 7, mpf(3) / 2),
                    (mpf(3) / 10, sqrt(2) - 1, -mpf(1) / 3)]:
        reach = int(20 / sqrt(a)) + int(fabs(t) / a) + 60
        k0 = int(mp.floor(c))
        lhs = mpf(0)
        for k in range(k0 - reach, k0 + reach + 1):
            x = mpf(k) - c
            lhs += exp(-a * x ** 2 + t * x)
        cshift = c + t / (2 * a)
        th = theta2(-cshift, mpc(0, 1) * pi / a)
        rhs = exp(t ** 2 / (4 * a)) * sqrt(pi / a) * th
        rel = fabs(lhs - mp.re(rhs)) / fabs(lhs)
        if not (rel < mpf(10) ** (-mp.dps + 10)):
            ok = False
        rows.append({"a": nstr(a, 10), "c": nstr(c, 10), "t": nstr(t, 10),
                     "discrete_mgf": nstr(lhs, 18), "rel_err": nstr(rel, 6),
                     "theta_minus_one": nstr(fabs(th - 1), 6)})
        print(f"  {nstr(a, 5):>7}  {nstr(c, 8):>10}  {nstr(t, 5):>7}"
              f"  {nstr(lhs, 16):>22}  {nstr(rel, 4):>11}"
              f"  {nstr(fabs(th - 1), 4):>12}")
    return ok, rows


def continuum_moment(a, m):
    """int_R x^m e^{-a x^2} dx: 0 for odd m, Gamma((m+1)/2)/a^{(m+1)/2} else."""
    if m % 2 == 1:
        return mpf(0)
    return gamma(mpf(m + 1) / 2) / a ** (mpf(m + 1) / 2)


def check_moments():
    print("\n  (1) discrete Gaussian moments vs continuum, m = 0..6")
    print("      claim: difference is O(e^{-pi^2/a}), for EVERY m")
    rows = []
    ok = True
    for a, c in [(mpf(1), mpf(5) / 6), (mpf(1) / 2, pi / 7),
                 (mpf(3) / 10, sqrt(2) - 1)]:
        env = exp(-pi ** 2 / a)
        print(f"\n    a = {nstr(a, 8)}   c = {nstr(c, 10)}   "
              f"e^(-pi^2/a) = {nstr(env, 6)}")
        print(f"      {'m':>3}  {'discrete':>24}  {'continuum':>24}  {'|diff|':>12}")
        for m in range(7):
            d = discrete_moment(a, c, m)
            k = continuum_moment(a, m)
            diff = fabs(d - k)
            # the bound carries a polynomial-in-1/a prefactor from the m
            # derivatives; allow a generous but FIXED polynomial factor.
            bound = env * (1 + 1 / a) ** (m + 2) * 100
            if not (diff <= bound):
                ok = False
            rows.append({"a": nstr(a, 10), "c": nstr(c, 10), "m": m,
                         "discrete": nstr(d, 18), "continuum": nstr(k, 18),
                         "abs_diff": nstr(diff, 8), "bound": nstr(bound, 8)})
            print(f"      {m:>3}  {nstr(d, 18):>24}  {nstr(k, 18):>24}"
                  f"  {nstr(diff, 6):>12}")
    return ok, rows


# ---------------------------------------------------------------------------
# (2) the model with the real 4_1 cubic and quartic
# ---------------------------------------------------------------------------

def model_phi(x, N):
    """-a x^2 + b3 x^3 + b4 x^4 with the 4_1 coefficients at scale N."""
    h = pi / N
    a = sqrt(3) * pi / N
    b3 = -(mpf(4) / 3) * h ** 2
    b4 = -(2 * sqrt(3) / 3) * h ** 3
    return -a * x ** 2 + b3 * x ** 3 + b4 * x ** 4


def check_model():
    print("\n  (2) model with the exact 4_1 cubic + quartic, offset c = 5N/6 mod 1")
    print("      sum over Z vs integral over R, both of e^{phi}")
    print(f"\n  {'N':>6}  {'b3 sigma^3':>12}  {'b4 sigma^4':>12}"
          f"  {'|sum/int - 1|':>16}  {'1/N':>10}")
    rows = []
    ok = True
    prev = None
    devs = {}
    for N in [12, 24, 48, 96]:
        a = sqrt(3) * pi / N
        sigma = 1 / sqrt(2 * a)
        h = pi / N
        b3s = fabs(-(mpf(4) / 3) * h ** 2) * sigma ** 3
        b4s = fabs(-(2 * sqrt(3) / 3) * h ** 3) * sigma ** 4
        # the saddle sits at k* = 5N/6; its fractional offset is what the
        # lattice sees.  Sum over k - k* for integer k.
        kstar = mpf(5) * N / 6
        frac = kstar - mp.floor(kstar)
        reach = int(30 * sigma) + 60
        s = mpf(0)
        for j in range(-reach, reach + 1):
            s += exp(model_phi(mpf(j) - frac, N))
        integral = quad(lambda x: exp(model_phi(x, N)), [-inf, inf])
        dev = fabs(s / integral - 1)
        rows.append({"N": N, "b3_sigma3": nstr(b3s, 8), "b4_sigma4": nstr(b4s, 8),
                     "deviation": nstr(dev, 8), "one_over_N": nstr(mpf(1) / N, 8)})
        print(f"  {N:>6}  {nstr(b3s, 6):>12}  {nstr(b4s, 6):>12}"
              f"  {nstr(dev, 8):>16}  {nstr(mpf(1)/N, 6):>10}")
        devs[N] = dev
        if prev is not None:
            # doubling N must shrink the deviation by far more than 2x
            # (polynomial) — demand at least 100x, exponential decay gives >>.
            if not (dev * 100 < prev):
                ok = False
        prev = dev
    # measured exponential rate, and how the remainder degrades it
    rate = (log(devs[48]) - log(devs[96])) / (96 - 48)
    gauss_rate = pi / sqrt(3)
    print(f"\n    measured  d(-log dev)/dN = {nstr(rate, 10)}")
    print(f"    pure Gaussian would give   = pi/sqrt3 = {nstr(gauss_rate, 10)}")
    print("    => the cubic/quartic remainder ROUGHLY HALVES the exponential")
    print("       rate. It does NOT make the decay polynomial, which is the")
    print("       only thing the one-loop constant depends on.")
    # the honest claim: still exponential (rate bounded away from 0), and
    # strictly slower than the pure-Gaussian rate.
    rate_ok = bool(mpf("0.5") < rate < gauss_rate)
    return ok and rate_ok, rows, rate, gauss_rate


# ---------------------------------------------------------------------------
# (3) the real 4_1 potential
# ---------------------------------------------------------------------------

def real_phi(x, N):
    """phi(x) = -(2N/pi) Lambda(x pi/N) + log(2 N sin(x pi/N)), normalised."""
    th = x * pi / N
    return -(2 * N / pi) * lobachevsky(th) + log(2 * N * sin(th))


def check_real():
    print("\n  (3) the real 4_1 potential, sum_{k=1}^{N-1} vs int_1^{N-1}")
    print("      (normalised at the saddle so the numbers stay finite)")
    print(f"\n  {'N':>6}  {'|sum/int - 1|':>18}  {'1/N':>10}"
          f"  {'e^{-Vol N/2pi}':>16}")
    rows = []
    ok = True
    prev = None
    ratios = []
    vol41 = 4 * lobachevsky(pi / 6)
    for N in [24, 48, 96, 192]:
        kstar = mpf(5) * N / 6
        peak = real_phi(kstar, N)
        s = mpf(0)
        for k in range(1, N):
            s += exp(real_phi(mpf(k), N) - peak)
        integral = quad(lambda x: exp(real_phi(x, N) - peak), [1, N - 1])
        dev = fabs(s / integral - 1)
        endpoint = exp(-vol41 * N / (2 * pi))
        ratio = dev / endpoint
        ratios.append(ratio)
        rows.append({"N": N, "deviation": nstr(dev, 8),
                     "one_over_N": nstr(mpf(1) / N, 8),
                     "endpoint_scale": nstr(endpoint, 8),
                     "dev_over_endpoint": nstr(ratio, 8)})
        print(f"  {N:>6}  {nstr(dev, 8):>18}  {nstr(mpf(1)/N, 6):>10}"
              f"  {nstr(endpoint, 6):>16}   ratio {nstr(ratio, 6)}")
        if prev is not None and not (dev * 10 < prev):
            ok = False
        prev = dev
    # the residual IS the endpoint half-term: the ratio stays O(1), drifting
    # only by the polynomial prefactor, over four doublings of N.
    ratio_ok = all(mpf(1) < r < mpf(10) for r in ratios)
    print("\n    deviation / e^{-Vol N/2pi} stays O(1) across four doublings —")
    print("    the residual IS the endpoint half-term, not a saddle effect.")
    return ok and ratio_ok, rows, vol41, ratios


def main() -> int:
    set_compute_dps()

    print("=" * 78)
    print(" The higher remainder never enters: sum and integral share one expansion")
    print("=" * 78)

    mom_ok, mom_rows = check_moments()
    tilt_ok, tilt_rows = check_tilt()
    mod_ok, mod_rows, rate, gauss_rate = check_model()
    real_ok, real_rows, vol41, ratios = check_real()

    all_ok = mom_ok and tilt_ok and mod_ok and real_ok
    print("\n" + "=" * 78)
    print(f"  ALL CHECKS {'PASS' if all_ok else 'FAIL'}")
    print("=" * 78)

    wb = WitnessBuilder("laplace-higher-remainder", engine="mpmath")
    wb.add_data("the_moment_identity", {
        "statement": ("sum_k (k-c)^m e^{-a(k-c)^2} = int_R x^m e^{-ax^2} dx + "
                      "O(e^{-pi^2/a}), for every m >= 0"),
        "derivation": ("differentiate the (B) identity in the shift c: each "
                       "d/dc brings down 2a(k-c) on the left and acts on "
                       "Theta(c) = 1 + 2 sum_{n>=1} e^{-pi^2 n^2/a} cos(2 pi n c) "
                       "on the right, whose every non-constant term already "
                       "carries e^{-pi^2 n^2/a}"),
        "consequence": ("expanding e^R term by term gives the SUM exactly the "
                        "series the INTEGRAL gives, with an exponentially small "
                        "discrepancy at every order — the asymptotic expansions "
                        "agree to ALL orders in 1/N"),
        "rows": mom_rows,
    })
    wb.add_data("the_tilted_sum_every_moment_at_once", {
        "statement": ("sum_k e^{-a(k-c)^2 + t(k-c)} = e^{t^2/4a} . sqrt(pi/a) "
                      ". theta_2(-(c + t/2a), i pi/a), exactly"),
        "lean": "QOU.MathlibExt.hasSum_gaussian_theta_tilt, sorry-free",
        "why_it_matters": ("e^{t^2/4a} sqrt(pi/a) IS the continuum generating "
                           "function int_R e^{-ax^2+tx} dx, so the entire "
                           "discrete-vs-continuum discrepancy at EVERY moment "
                           "is the one theta factor, uniformly in c and t. "
                           "Completing the square is a shift of c, so this "
                           "needs no analytic input beyond (B)"),
        "rows": tilt_rows,
    })
    wb.add_data("model_with_the_real_4_1_cubic_and_quartic", {
        "coefficients": {
            "phi_2": "2 cot(5pi/6) pi/N = -2 sqrt3 pi/N,  a = sqrt3 pi/N",
            "phi_3": "-2 (pi/N)^2 csc^2 = -8 (pi/N)^2,  b3 = -(4/3)(pi/N)^2",
            "phi_4": "4 (pi/N)^3 csc^2 cot = -16 sqrt3 (pi/N)^3, "
                     "b4 = -(2 sqrt3/3)(pi/N)^3",
        },
        "why_this_is_a_real_test": ("at the Gaussian width sigma ~ N^{1/2} the "
                                    "remainder is b3 sigma^3 ~ N^{-1/2} and "
                                    "b4 sigma^4 ~ N^{-1} — NOT negligible "
                                    "pointwise, so a sum-vs-integral difference "
                                    "of order 1/N was entirely possible a priori"),
        "rows": mod_rows,
        "measured_exponential_rate": nstr(rate, 12),
        "pure_gaussian_rate": nstr(gauss_rate, 12),
        "the_remainder_does_degrade_the_rate": (
            "measured d(-log dev)/dN is about 0.81, roughly HALF the "
            "pure-Gaussian pi/sqrt3 = 1.814. The cubic and quartic terms move "
            "the relevant complex saddle and slow the Poisson tail. They do "
            "NOT make the decay polynomial, and only that distinction matters "
            "for the one-loop constant — but the e^{-pi^2/a} rate of the (B) "
            "identity must not be quoted for the FULL potential"),
    })
    wb.add_data("the_real_4_1_potential", {
        "potential": "phi(x) = -(2N/pi) Lambda(x pi/N) + log(2 N sin(x pi/N))",
        "vol_4_1_recomputed": nstr(vol41, 25),
        "note": ("over the real range the residual is dominated by the ENDPOINT "
                 "half-terms, not by the saddle: the peak is e^{Vol N/2pi} above "
                 "the endpoints, so the endpoint contributes at relative scale "
                 "e^{-Vol N/2pi} ~ e^{-0.323 N}, larger than the saddle's "
                 "e^{-pi N/sqrt3} ~ e^{-1.814 N}. Both are exponential; neither "
                 "is polynomial"),
        "rows": real_rows,
    })
    wb.add_data("scope", {
        "closes": ("the specific worry that DISCRETISATION and the "
                   "cubic-and-higher REMAINDER could interact to produce a 1/N "
                   "term the continuum calculation misses. They cannot, at any "
                   "order"),
        "does_not_close": [
            "the integral's OWN 1/N corrections (a different question)",
            ("a rigorous bound on the actual sums rather than on their "
             "expansions — that still needs window + tail control"),
            "Laplace's method in general",
            ("(A): s_k's Euler-Maclaurin constant, where the integrand is "
             "singular at the endpoint and corrections really are polynomial"),
        ],
    })
    wb.add_assertion(
        "discrete_moments_match_continuum_to_exponential_order",
        computed="1" if mom_ok else "0", expected="1", tolerance="0.5",
        source="m = 0..6 at three (a,c), against e^{-pi^2/a}(1+1/a)^{m+2}")
    wb.add_assertion(
        "tilted_sum_matches_continuum_mgf_times_theta",
        computed="1" if tilt_ok else "0", expected="1", tolerance="0.5",
        source="four (a, c, t) including negative tilts, to working dps")
    wb.add_assertion(
        "model_with_real_cubic_quartic_decays_faster_than_polynomially",
        computed="1" if mod_ok else "0", expected="1", tolerance="0.5",
        source=("doubling N shrinks |sum/int - 1| by >100x, N = 12..96; and "
                "the measured rate sits strictly between 0.5 and pi/sqrt3, "
                "i.e. still exponential but slower than the pure Gaussian"))
    wb.add_assertion(
        "real_4_1_residual_is_the_endpoint_half_term",
        computed="1" if real_ok else "0", expected="1", tolerance="0.5",
        source=("doubling N shrinks |sum/int - 1| by >10x, N = 24..192, and "
                "deviation / e^{-Vol N/2pi} stays in (1, 10) throughout"))
    out = wb.save()
    print(f"\n  witness -> {out.name}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
