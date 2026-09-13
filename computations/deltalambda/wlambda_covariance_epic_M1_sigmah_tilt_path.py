#!/usr/bin/env python3
"""M_1 as a tilt derivative: the ONE reformulation that escapes the qou-ujil obstruction.

Bean qou-k5r5 (gap), epic qou-x631.  The epic's tilt path (qou-x631, f668c434a97,
qbeta_covariance_kernel_tilt_path_probe.py) turns a MEAN under a tilted measure into an
integral of covariances, because its quantity E_Q[Sigma_3] is a mean.  M_1 is already a
covariance, so the same construction runs BACKWARDS here -- and the backwards direction is
the useful one.

THE CONSTRUCTION.  Tilt Plancherel by Sum_h rather than by log f^lam.  Keep the tilt
variable as x = e^s so every weight stays an INTEGER power and nothing here needs a float:

    P_x(lam)  =  (f^lam)^2 * x^{Sum_h(lam)} / D(x),     D(x) = sum_lam (f^lam)^2 x^{Sum_h}

    R(x)  :=  E_{P_x}[omega_3]  =  N(x)/D(x),           N(x) = sum_lam (f^lam)^2 x^{Sum_h} omega_3

N and D are integer polynomials in x, so R is an exact rational function and every number
below is a Fraction.  Two facts make it the right object:

    R(1) = 0          because E_Planch[omega_3] = 0 EXACTLY (qou-cze8 fact B)
    R'(1) = M_1       because N(1) = 0, so R'(1) = N'(1)/D(1)
                      = sum (f^lam)^2 h omega_3 / n! = Cov_P(Sum_h, omega_3)

So M_1 is the SLOPE AT x = 1 of a function that vanishes there, and

    R(x)  =  integral_1^x  Cov_{P_u}(Sum_h, omega_3) * du/u        (the integrated form)

WHY THIS MATTERS -- it is not a restatement.  qou-ujil (route 7, eliminated 2026-09-06)
kills concentration / limit-shape arguments for this family precisely BECAUSE
E_Planch[omega_3] = 0 exactly: replacing lam by the VKLS shape "discards exactly the term
being computed and proves 0 <= 0".  That objection is an objection to evaluating at x = 1.
At x != 1 the Sum_h-tilt DEFORMS the limit shape, and omega_3 on the deformed shape is a
first-order limit-shape quantity that does NOT vanish.  M_1 is then recovered as a
derivative at the point where the obstruction sits, rather than being computed there.

WHAT THIS PROBE DOES AND DOES NOT DO.  It MEASURES R(x): its sign, its shape, and whether
the covariance integrand keeps one sign along the path.  It does NOT derive R(x) from a
tilted limit shape -- that is the actual work this reformulation would license, and it is
not attempted here.  A measured R is not a proof of anything about n > n_max.  Gap stays
OPEN.

CONTROLS (the verdict is not printed unless all pass):
  1. D(1) == n!                        -- the Plancherel normalisation
  2. R(1) == 0 exactly                 -- the fact the whole construction turns on
  3. R'(1) == M_1 computed directly    -- as Cov_P(Sum_h, omega_3) from its own definition,
                                          NOT reusing N'(1); a coincidence of two spellings
                                          of the same sum would prove nothing
  4. Sum_h == D + A at every partition -- the split identity this arc runs on

NO float64 anywhere: Fraction and int end to end.  float() appears only inside f-strings.
"""
import sys
from fractions import Fraction as F
from math import factorial


def partitions(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def conjugate(lam):
    if not lam:
        return []
    return [sum(1 for p in lam if p > j) for j in range(lam[0])]


def f_lambda(lam):
    """Hook-length formula, exact integer."""
    n = sum(lam)
    c = conjugate(lam)
    den = 1
    for i, li in enumerate(lam):
        for j in range(li):
            den *= (li - j) + (c[j] - i) - 1
    return factorial(n) // den


def stats(lam):
    """(Sum_h, Sum c^2, A = Sum|c|, D = Sum_u d_u^2) -- all exact integers."""
    c = conjugate(lam)
    h = c2 = a = 0
    diag = {}
    for i, li in enumerate(lam):
        for j in range(li):
            h += (li - j) + (c[j] - i) - 1
            cc = j - i
            c2 += cc * cc
            a += abs(cc)
            diag[cc] = diag.get(cc, 0) + 1
    d = sum(v * v for v in diag.values())
    return h, c2, a, d


def tilt_data(n):
    """Coefficients of N(x) and D(x) as dicts {power of x: integer coefficient}."""
    binom = n * (n - 1) // 2
    Nc, Dc = {}, {}
    m1_direct = 0            # sum (f^lam)^2 * h * omega_3, computed from its own definition
    split_ok = True
    for lam in partitions(n):
        f = f_lambda(lam)
        w = f * f
        h, c2, a, d = stats(lam)
        if h != d + a:
            split_ok = False
        w3 = c2 - binom
        Dc[h] = Dc.get(h, 0) + w
        Nc[h] = Nc.get(h, 0) + w * w3
        m1_direct += w * h * w3
    return Nc, Dc, F(m1_direct, factorial(n)), split_ok


def poly_at(coeffs, x):
    return sum(F(c) * x ** k for k, c in coeffs.items())


def dpoly_at(coeffs, x):
    return sum(F(c) * k * x ** (k - 1) for k, c in coeffs.items() if k)


def main():
    nmin, nmax = 3, int(sys.argv[1]) if len(sys.argv) > 1 else 26
    # Tilt points as EXACT rationals, straddling x = 1 so both directions are visible.
    xs = [F(9, 10), F(19, 20), F(1), F(21, 20), F(11, 10), F(6, 5), F(3, 2)]

    checks = []
    ctrl_norm = ctrl_zero = ctrl_slope = ctrl_split = True
    rows = []

    for n in range(nmin, nmax + 1):
        Nc, Dc, m1_direct, split_ok = tilt_data(n)
        if not split_ok:
            ctrl_split = False
        if poly_at(Dc, F(1)) != factorial(n):
            ctrl_norm = False
        if poly_at(Nc, F(1)) != 0:
            ctrl_zero = False
        # R'(1) = N'(1)/D(1) since N(1) = 0.  Compare to M_1 built from its own definition.
        slope = dpoly_at(Nc, F(1)) / poly_at(Dc, F(1))
        if slope != m1_direct:
            ctrl_slope = False
        vals = []
        for x in xs:
            D = poly_at(Dc, x)
            vals.append(poly_at(Nc, x) / D)
        rows.append((n, m1_direct, vals))

    checks.append(("CONTROL 1: D(1) == n! at every n", ctrl_norm, "Plancherel normalisation"))
    checks.append(("CONTROL 2: R(1) == 0 EXACTLY at every n", ctrl_zero,
                   "E_Planch[omega_3] = 0 -- the fact the construction turns on, and the "
                   "fact qou-ujil uses to kill limit-shape arguments AT x = 1"))
    checks.append(("CONTROL 3: R'(1) == M_1 from its own definition", ctrl_slope,
                   "N'(1)/D(1) reproduces Cov_P(Sum_h, omega_3) computed independently"))
    checks.append(("CONTROL 4: Sum_h == D + A at every partition", ctrl_split,
                   "the split identity this arc runs on"))

    if not all(ok for _, ok, _ in checks):
        for name, ok, detail in checks:
            print(f"[{'PASS' if ok else 'FAIL'}] {name}\n        {detail}")
        return 1

    # -- FINDING 1: sign of R on each side of x = 1 ----------------------------------------
    pos_above = all(v > 0 for _, _, vals in rows for x, v in zip(xs, vals) if x > 1)
    neg_below = all(v < 0 for _, _, vals in rows for x, v in zip(xs, vals) if x < 1)
    checks.append(("FINDING 1: R(x) > 0 for x > 1 and R(x) < 0 for x < 1, at every n",
                   pos_above and neg_below,
                   "R vanishes at x = 1 and changes sign there -- consistent with, and "
                   "implied by, M_1 = R'(1) > 0; recorded because it is what a tilted "
                   "limit-shape derivation would have to reproduce"))

    # -- FINDING 2: is the path LINEAR, as the epic's was not? -----------------------------
    # Compare R(x) against its own tangent at x = 1.  The epic measured ~1/3 of its answer
    # nonlinear over t in [0,1]; the analogous number here says how far a first-order
    # tilted-shape computation would get.
    #
    # A FIXED x IS NOT A FIXED TILT STRENGTH, and reading the n-drift below as a property of
    # the path would be wrong.  The tilt enters as x^{Sum_h} and E_P[Sum_h] grows like
    # n^{3/2}, so holding x = 1.1 while n grows STRENGTHENS the tilt without limit: at n = 20
    # the exponent is already ~n^{3/2} = 89 and 1.1^89 ~ 5e3.  The scale-consistent
    # comparison holds x^{n^{3/2}} fixed instead, i.e. x_n = 1 + 1/round(n^{3/2}), which
    # stays an exact rational.  Both are reported; only the second is a statement about the
    # path rather than about the parameterisation.
    lin_rows = []
    for n, m1, vals in rows:
        x = F(11, 10)
        actual = vals[xs.index(x)]
        tangent = m1 * (x - 1)
        xs_n = F(1) + F(1, round(n ** 1.5))
        Nc, Dc, _, _ = tilt_data(n)
        actual_s = poly_at(Nc, xs_n) / poly_at(Dc, xs_n)
        tangent_s = m1 * (xs_n - 1)
        lin_rows.append((n, actual, tangent, actual / tangent,
                         xs_n, actual_s, tangent_s, actual_s / tangent_s))
    ratios = [r for _, _, _, r, _, _, _, _ in lin_rows]
    ratios_s = [r for _, _, _, _, _, _, _, r in lin_rows]
    fixed_drift = abs(ratios[-1] - ratios[0])
    scaled_drift = abs(ratios_s[-1] - ratios_s[0])
    checks.append(("FINDING 2: the n-drift in nonlinearity is the PARAMETERISATION, not the path",
                   scaled_drift < fixed_drift,
                   f"fixed x = 1.1: ratio {float(ratios[0]):.4f} -> {float(ratios[-1]):.4f} "
                   f"(drift {float(fixed_drift):.4f}); scale-consistent x_n = 1 + n^-3/2: "
                   f"{float(ratios_s[0]):.4f} -> {float(ratios_s[-1]):.4f} "
                   f"(drift {float(scaled_drift):.4f}). 1.0 = first order exact"))

    # -- FINDING 3: and the sign of the drift REVERSES, which is the headline ---------------
    # Under the fixed-x reading the path looks like it is becoming MORE nonlinear with n.
    # Under the scale-consistent one it peaks early and then approaches 1 monotonically --
    # first order becomes asymptotically exact.  Those are opposite conclusions about the
    # viability of a first-order tilted-limit-shape derivation, from the same data.
    # The start of the monotone tail is MEASURED, not chosen: picking the threshold that
    # makes a monotonicity claim true is selection against the target, which is the thing
    # this repo's anti-fit directive forbids.  So find the longest strictly-decreasing
    # SUFFIX and report where it begins, including the small-n wobble that precedes it.
    seq = [(n, r) for n, _, _, _, _, _, _, r in lin_rows]
    start = len(seq) - 1
    while start > 0 and seq[start - 1][1] > seq[start][1]:
        start -= 1
    tail = seq[start:]
    end_to_end = seq[-1][1] < seq[min(2, len(seq) - 1)][1]
    all_above_one = all(r > 1 for _, r in tail)
    checks.append(("FINDING 3: first order becomes MORE exact with n over a measured tail",
                   end_to_end and all_above_one and len(tail) >= 3,
                   f"scale-consistent ratio is strictly decreasing from n = {tail[0][0]} to "
                   f"n = {tail[-1][0]} ({float(tail[0][1]):.5f} -> {float(tail[-1][1]):.5f}), "
                   f"{len(tail)} of {len(seq)} points, staying above 1. It is NOT monotone "
                   f"before that: it wobbles up at n=6->7 and n=7->8, so the tail start is "
                   f"read off the data rather than assumed. Contrast the epic's own tilt "
                   f"path, which is ~1/3 nonlinear and DEGRADES further out (f668c434a97: "
                   f"linear predicts g(3) = -0.74 against -0.374 at k=40). Measured to "
                   f"n = {seq[-1][0]} only; a monotone tail is not a limit."))

    print("M_1 as the slope at x = 1 of the Sum_h-tilted mean of omega_3")
    print("  P_x(lam) ~ (f^lam)^2 x^{Sum_h};  R(x) = E_{P_x}[omega_3];  R(1) = 0;  R'(1) = M_1")
    print()
    slope_label = "M_1 = R'(1)"
    hdr = "  " + f"{'n':>3} {slope_label:>16}"
    for x in xs:
        hdr += f"{'R(' + str(x) + ')':>16}"
    print(hdr)
    for n, m1, vals in rows:
        line = f"  {n:>3} {float(m1):>16.8f}"
        for v in vals:
            line += f"{float(v):>16.8f}"
        print(line)
    print()
    print("  nonlinearity: R(x) against its tangent M_1*(x-1), two parameterisations")
    print(f"  {'n':>3} | {'R(1.1)':>14} {'tangent':>14} {'ratio':>9} | "
          f"{'x_n':>10} {'R(x_n)':>14} {'tangent':>14} {'ratio':>9}")
    for n, a, t, r, xn, a_s, t_s, r_s in lin_rows:
        print(f"  {n:>3} | {float(a):>14.8f} {float(t):>14.8f} {float(r):>9.5f} | "
              f"{float(xn):>10.6f} {float(a_s):>14.8f} {float(t_s):>14.8f} {float(r_s):>9.5f}")
    print()

    for name, ok, detail in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
        print(f"        {detail}")
    npass = sum(1 for _, ok, _ in checks if ok)
    print(f"\n{npass}/{len(checks)} checks pass")

    print("""
WHAT THIS IS AND IS NOT.  This is a REFORMULATION with its controls verified, not a proof
and not a bound.  It relocates M_1 from a covariance at the one point where the limit-shape
argument is obstructed (E_Planch[omega_3] = 0) to the derivative of a tilted mean that is
nonzero away from that point.  The work it licenses -- deriving R(x) from the Sum_h-tilted
limit shape and differentiating at x = 1 -- is NOT done here.  Gap qou-k5r5 stays OPEN.""")
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
