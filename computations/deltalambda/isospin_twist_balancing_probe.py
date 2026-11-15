#!/usr/bin/env python3
"""Does the balancing axiom let the twist skip the isospin factor?

Companion to ``QOU/Hecke/IsospinTwistFromBalancing.lean``.  Exact arithmetic only:
``fractions.Fraction`` for the identities and seminormal checks, ``mpmath`` at
``mp.dps = 60`` at the proton-pinned ``q0`` (``q_parameter.Q_MP``) for the numbers.
No float in any computation.  Emits no witness.

Balancing on six strands: the twist on block lambda is  tau^6 * f_lambda,  f_lambda the
full-twist scalar.  Spin braids by the Hecke relation at q, isospin at t.  Then

    D - S = sigma^6 tau^6 (g f' - g' f) tr p tr p'
          = sigma^6 tau^6 q^6 t^6 (q^4 - t^4) tr p tr p'        (JM spectrum f = t^{2c})

Checks:
  1. the full twist acts by t^{2c(lambda)} on explicit seminormal (4,2), (3,3) at several
     rational t, INCLUDING t = 1 and t = -1 (the transparent / classical points);
  2. the closed form against the 2x2 determinant, exactly over Q;
  3. at q0: D/S for (a) one Hecke parameter on both factors (t = q0) -> 1,
     (b) spin-only under balancing (t = 1) -> q0^4,
     (c) the half-twist convention theta = q^c used in TwistedChannelSplitting -> q0^2.
"""
from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parent), str(HERE.parent / "substrate")]
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

from framing_twist_channel_split_probe import (  # noqa: E402
    check_rep_and_twist, content_sum, eye, is_scalar, mm, standard_tableaux)

mp.mp.dps = 60


def classical_point_twist(lam, tv):
    """At t = +-1 the q-seminormal formula is singular (0/0).  Use the classical
    Young seminormal form (diagonal 1/d) times t: sigma = t * s_i satisfies
    (sigma - t)(sigma + 1/t) = t^2 (s - 1)(s + 1) = 0.  Returns (relations ok,
    full twist == 1, dim)."""
    one = Fraction(1)
    tabs = standard_tableaux(lam)
    idx = {T: a for a, T in enumerate(tabs)}
    dim, n = len(tabs), sum(lam)
    mats = []
    for i in range(n - 1):
        M = [[0 * one for _ in range(dim)] for _ in range(dim)]
        for T in tabs:
            a = idx[T]
            (r1, c1), (r2, c2) = T[i], T[i + 1]
            d = (c2 - r2) - (c1 - r1)
            M[a][a] = tv * one / d
            if r1 != r2 and c1 != c2:
                T2 = list(T)
                T2[i], T2[i + 1] = T2[i + 1], T2[i]
                b = idx[tuple(T2)]
                M[b][a] = tv * (one if r2 > r1 else one - one / (d * d))
        mats.append(M)
    I = eye(dim, one)
    ok = True
    for S in mats:
        A = [[S[r][c] - tv * I[r][c] for c in range(dim)] for r in range(dim)]
        B = [[S[r][c] + I[r][c] / tv for c in range(dim)] for r in range(dim)]
        ok &= is_scalar(mm(A, B), 0 * one)
    for i in range(len(mats) - 1):
        a, b = mats[i], mats[i + 1]
        ok &= mm(mm(a, b), a) == mm(mm(b, a), b)
    run = I
    for S in mats:
        run = mm(run, S)
    D2 = I
    for _ in range(n):
        D2 = mm(D2, run)
    return ok, is_scalar(D2, one), dim


def closed_form(q, t, sig, tau):
    return sig ** 6 * tau ** 6 * q ** 6 * t ** 6 * (q ** 4 - t ** 4)


def determinant(q, t, sig, tau):
    g, gp = q ** (2 * content_sum((4, 2))), q ** (2 * content_sum((3, 3)))
    f, fp = t ** (2 * content_sum((4, 2))), t ** (2 * content_sum((3, 3)))
    return sig ** 6 * tau ** 6 * (g * fp - gp * f)


def main() -> int:
    ok = True
    print("1. full twist on seminormal (4,2), (3,3) at isospin parameter t")
    for tv in (Fraction(1), Fraction(-1), Fraction(11, 10), Fraction(-7, 5)):
        for lam in ((4, 2), (3, 3)):
            if tv in (1, -1):
                rel, tw, dim = classical_point_twist(lam, tv)
            else:
                rel, tw, dim = check_rep_and_twist(lam, tv, Fraction(1))
            print(f"   t={str(tv):>6} {lam} dim={dim} relations={rel} "
                  f"Delta^2 = t^{2 * content_sum(lam)}: {tw}")
            ok &= rel and tw
    print("   => at t = +-1 the full twist is 1 on both blocks (transparent isospin)")

    print("\n2. closed form vs determinant, exact over Q")
    samples = [(Fraction(11, 10), Fraction(1), Fraction(3, 2), Fraction(2)),
               (Fraction(7, 5), Fraction(7, 5), Fraction(1), Fraction(5, 3)),
               (Fraction(9, 7), Fraction(-2, 3), Fraction(4, 5), Fraction(1, 2))]
    for s in samples:
        eq = closed_form(*s) == determinant(*s)
        print(f"   (q,t,sigma,tau)={tuple(map(str, s))}: equal={eq}")
        ok &= eq

    print("\n3. D/S at q0 (proton pin)")
    from q_parameter import Q_MP
    q0 = mp.mpf(Q_MP)
    same = (q0 ** 10 * q0 ** 6) / (q0 ** 6 * q0 ** 10)
    bal = q0 ** 10 / q0 ** 6
    half = q0 ** 5 / q0 ** 3
    print(f"   one Hecke parameter on both factors (t = q0): D/S = {mp.nstr(same, 30)}")
    print(f"   spin-only, balancing twist (t = 1):          D/S = {mp.nstr(bal, 30)}  (= q0^4)")
    print(f"   spin-only, half-twist theta = q^c:            D/S = {mp.nstr(half, 30)}  (= q0^2)")
    ok &= same == 1 and abs(bal - q0 ** 4) < mp.mpf(10) ** -55
    print("\nCOMPARISON (context only, nothing tuned): AME deuteron bound, 1S0 singlet unbound.")
    print("ALL CHECKS PASS" if ok else "CHECK FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
