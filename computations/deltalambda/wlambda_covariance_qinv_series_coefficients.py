#!/usr/bin/env python3
"""Covariance kernel: the coefficients a_m = [sigma](e - Q)^m of the Q^{-1} series, quantified.

Setting (audit 2026-11-27-covariance-kernel-square-law-inverse.md): Q = (1/n!) sum_x x^2 acts on
V^lambda by 1/f^lambda, kernel <=> [sigma]Q^{-1} <= 0, and Q^{-1} = sum_{m>=0} (e - Q)^m.
Up to a positive constant, a_m = (1/n!) sum_lambda f^2 omega_3 (1 - 1/f)^m, a_0 = 0, and the tail
sum_{m>=M} a_m = R(M) = (1/n!) sum_lambda f^3 omega_3 (1 - 1/f)^M is closed form.

Checks:
  A (exact, Fraction-free integers): sum_lambda f*omega_3 = n(n-1)(n-2)/3 * I(n-3), I = number of
    involutions. This is Frobenius-Schur: [sigma]Q = #{x : x^2 = sigma}/n!, and x^2 = (123) forces
    x = (132)*tau with tau an involution of the other n-3 points. So a_1 = -[sigma]Q < 0.
  B (mpmath, 50 digits; no float): the real zeros of t -> a(t) on a log grid t in [1, 1e7 f_max],
    refined by root finding, and the positive and negative masses P+ = sum_{a_m>0} a_m,
    N- = -sum_{a_m<0} a_m, from R at the integer cuts.
Result for n = 3..26: a_m < 0 for every m >= 1 except n = 18 and n = 26, where a(t) changes sign
once, at m ~ s* f_max (s* the large-tilt crossing), and P+/N- is ~1e-161 and ~1e-66.
No fit; nothing wired. This measures; it proves nothing about the kernel for other n.
"""
import sys
import mpmath as mp
from math import factorial, comb

mp.mp.dps = 50


def parts(n, m=None):
    m = n if m is None else m
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for p in parts(n - k, k):
            yield (k,) + p


def f_omega(l, n):
    lc = [sum(1 for r in l if r > j) for j in range(l[0])]
    hp = 1
    for i, r in enumerate(l):
        for j in range(r):
            hp *= (r - j - 1) + (lc[j] - i - 1) + 1
    w = sum((j - i) ** 2 for i, r in enumerate(l) for j in range(r)) - comb(n, 2)
    return factorial(n) // hp, w


def involutions(k):
    a, b = 1, 1
    for i in range(1, k):
        a, b = b, b + i * a
    return b


def analyse(n, pts=8000, span=10**7):
    groups, S = {}, 0
    for l in parts(n):
        f, w = f_omega(l, n)
        S += f * w
        groups[f] = groups.get(f, 0) + f * f * w
    check_a = 3 * S == n * (n - 1) * (n - 2) * involutions(n - 3)
    g = {f: c for f, c in groups.items() if c != 0 and f > 1}  # f = 1 terms vanish for m >= 1
    N = mp.mpf(factorial(n))
    L = {f: mp.log1p(-mp.mpf(1) / f) for f in g}
    a = lambda t: sum(c * mp.exp(t * L[f]) for f, c in g.items()) / N
    R = lambda M: sum(c * f * mp.exp(M * L[f]) for f, c in g.items()) / N
    fmax = max(g)
    top = mp.log10(span * fmax)
    T = [mp.mpf(10) ** (mp.mpf(k) / pts * top) for k in range(pts + 1)]
    vals = [a(t) for t in T]
    zeros = [mp.findroot(a, (T[i], T[i + 1]), solver="anderson")
             for i in range(pts) if vals[i] != 0 and mp.sign(vals[i]) != mp.sign(vals[i + 1])]
    cuts = [1] + [int(mp.ceil(z)) for z in zeros]
    pos = neg = mp.mpf(0)
    for i, M in enumerate(cuts):
        mass = R(M) - (R(cuts[i + 1]) if i + 1 < len(cuts) else 0)
        if mass > 0:
            pos += mass
        else:
            neg -= mass
    return {"n": n, "check_A_sqrt_count": check_a, "f_max": str(fmax),
            "a1_sign": int(mp.sign(a(1))), "zeros": [mp.nstr(z, 3) for z in zeros],
            "zero_over_fmax": [mp.nstr(z / fmax, 4) for z in zeros],
            "P_plus": mp.nstr(pos, 5), "N_minus": mp.nstr(neg, 12),
            "ratio": mp.nstr(pos / neg, 3) if neg else "0",
            "kernel_eq_minus_N_plus_P": bool(abs(R(1) - (pos - neg)) <= abs(R(1)) * mp.mpf(10) ** -40)}


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 26
    rows, ok = [], True
    for n in range(3, nmax + 1):
        r = analyse(n)
        rows.append(r)
        ok = ok and r["check_A_sqrt_count"] and r["a1_sign"] < 0 and r["kernel_eq_minus_N_plus_P"]
        print(r, flush=True)
    try:
        sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[1] / "substrate"))
        from witness_base import WitnessBuilder
        w = WitnessBuilder("wlambda-covariance-qinv-series-coefficients", engine="python-mpmath-50dps")
        w.set_description(
            "a_m = [sigma](e-Q)^m for the Q^{-1} series of the covariance kernel. a_1 = -[sigma]Q < 0 "
            "with [sigma]Q = I(n-3)/n! (Frobenius-Schur square-root count; exact check). Measured for "
            "n = 3..26: a_m < 0 for all m >= 1 except n = 18, 26 (one sign change at m ~ s* f_max); "
            "positive mass / negative mass ~1e-161 (n=18), ~1e-66 (n=26). Measurement only; no fit.")
        w.add_data("rows", rows)
        w.add_assertion("qinv_series_coefficients", computed=str(int(ok)), expected="1", tolerance=0,
                        source=f"exact sqrt-count identity and mpmath 50-dps scan, n=3..{nmax}")
        print(f"Witness: {w.save()}")
    except ImportError as e:
        print(f"(witness skipped: {e})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
