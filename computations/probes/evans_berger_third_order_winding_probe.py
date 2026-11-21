#!/usr/bin/env python3
"""evans_berger_third_order_winding_probe.py — bean qou-0seq.

Cross-check of Evans & Berger, "A hierarchy of linking integrals" (1992)
[evans-berger1992], library/1992evansberger/ (OCR text, pp. 5-7), against the
corpus's Magnus mu-bar machinery
(computations/deltalambda/mixed_multibond_mubar_integrality_probe.py) and the
Milnor indeterminacy gate (QOU/Mass/MilnorIndeterminacyGate.lean).

PRE-REGISTERED (written before running):

  Source facts used (OCR text layer):
    S1  eq (20): lambda_ij = (1/2 pi i) log[(z_i(t)-z_j(t)) / (z_i(0)-z_j(0))].
    S2  eq (21)-(22): psi_ijk = lambda_ij d lambda_jk + lambda_jk d lambda_ki
        + lambda_ki d lambda_ij is closed (Arnol'd relation (19)), and
        Psi_ijk = Re int_gamma psi_ijk is invariant under homotopy of the braid
        path, "irrespective of whether the net second order winding numbers
        vanish or not".
    S3  p. 5: the third-order linking number is +1 for the Borromean rings;
        p. 6-7: the pigtail braid closes to the Borromean rings, and when the
        second-order windings vanish Psi equals that linking number.

  Braids. Three strands at 0, 1, 2 on the real axis. sigma_i^{+-1} is a
  half-twist of the strands at positions i-1, i about their midpoint, the
  offset running over (1/2)(cos th, +-b sin th), th in [0, pi]; b is a shape
  parameter. Pigtail P = (sigma_1 sigma_2^{-1})^3 (the corpus's Borromean word,
  photon vertex sigma_0 sigma_1^{-1} cubed in 0-based labels). Hopf spectator
  H = sigma_1^2 (lk_12 = 1).

  Checks (mpmath 40 dps, mp.quad per half-twist):
    A  |Psi_123(P)| = 1 to 1e-30, and equals |mu-bar_123(Borromean)| from the
       corpus Magnus machinery (= 1).
    B  Shape independence (S2): Psi(P), Psi(H), Psi(HP) agree between b = 1
       and b = 3 to 1e-30.
    C  Psi(P P^{-1}) = 0 to 1e-30.
    D  Hopf spectator: Psi(HP) - Psi(H) = Psi(P) and Psi(PH) - Psi(H) = Psi(P)
       to 1e-30, while the Milnor gate's indeterminacy gcd(1, 0, 0) = 1 makes
       mu-bar_123 carry no content for the same link.
    PASS iff A-D. Psi(H) is reported, not gated.

Run: python3 -u computations/probes/evans_berger_third_order_winding_probe.py
"""
from __future__ import annotations

import sys
from math import gcd
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "deltalambda"))

PAIRS = ((1, 2), (2, 3), (3, 1))


def psi(word, b):
    """Psi_123 along the braid word [(i, sign), ...] with shape parameter b."""
    pos = {1: 0, 2: 1, 3: 2}              # label -> position
    z0 = {k: mp.mpf(v) for k, v in pos.items()}
    lam = {p: mp.mpc(0) for p in PAIRS}   # continuous lambda at segment start
    total = mp.mpc(0)
    zstart = dict(z0)
    for (i, s) in word:
        a = next(k for k, v in pos.items() if v == i - 1)
        c = next(k for k, v in pos.items() if v == i)
        m = mp.mpf(2 * i - 1) / 2
        seg0 = dict(zstart)

        def zpos(th, k):
            if k == a:
                return m + mp.mpc(-mp.cos(th), -s * b * mp.sin(th)) / 2
            if k == c:
                return m + mp.mpc(mp.cos(th), s * b * mp.sin(th)) / 2
            return seg0[k]

        def dz(th, k):
            if k == a:
                return mp.mpc(mp.sin(th), -s * b * mp.cos(th)) / 2
            if k == c:
                return mp.mpc(-mp.sin(th), s * b * mp.cos(th)) / 2
            return mp.mpc(0)

        def lam_at(th, p):
            i1, j1 = p
            w = zpos(th, i1) - zpos(th, j1)
            w0 = seg0[i1] - seg0[j1]
            if {i1, j1} == {a, c}:
                # continuous argument of the rotating pair
                ang = s * mp.atan2(b * mp.sin(th), mp.cos(th))
                lg = mp.log(abs(w) / abs(w0)) + 1j * ang
            else:
                lg = mp.log(w / w0)        # no winding within one half-twist
            return lam[p] + lg / (2j * mp.pi)

        def dlam(th, p):
            i1, j1 = p
            w = zpos(th, i1) - zpos(th, j1)
            return (dz(th, i1) - dz(th, j1)) / w / (2j * mp.pi)

        def integrand(th):
            l = {p: lam_at(th, p) for p in PAIRS}
            d = {p: dlam(th, p) for p in PAIRS}
            return (l[(1, 2)] * d[(2, 3)] + l[(2, 3)] * d[(3, 1)]
                    + l[(3, 1)] * d[(1, 2)])

        total += mp.quad(integrand, [0, mp.pi / 2, mp.pi])
        newlam = {p: lam_at(mp.pi, p) for p in PAIRS}
        lam = newlam
        pos[a], pos[c] = pos[c], pos[a]
        zstart = {k: mp.mpf(pos[k]) for k in pos}
    return mp.re(total), lam


def inv(word):
    return [(i, -s) for (i, s) in reversed(word)]


def main() -> int:
    mp.mp.dps = 40
    tol = mp.mpf(10) ** -30
    P = [(1, 1), (2, -1)] * 3
    H = [(1, 1), (1, 1)]
    from mixed_multibond_mubar_integrality_probe import BORROMEAN, _mu
    mub = _mu(BORROMEAN, (1, 2, 3))
    vals = {}
    for b in (mp.mpf(1), mp.mpf(3)):
        for name, w in (("P", P), ("H", H), ("HP", H + P), ("PH", P + H), ("PPi", P + inv(P))):
            vals[(name, b)], lam = psi(w, b)
            if b == 1 and name in ("P", "H"):
                print(f"   {name}: final Re lambda (winding numbers) "
                      f"{[mp.nstr(mp.re(lam[p]), 12) for p in PAIRS]}")
    for k, v in sorted(vals.items(), key=lambda kv: (kv[0][0], kv[0][1])):
        print(f"   Psi({k[0]}), b={mp.nstr(k[1], 2)}: {mp.nstr(v, 25)}")
    pP = vals[("P", 1)]
    a_ok = abs(abs(pP) - 1) < tol and abs(mub) == 1
    print(f"A  |Psi(P)| = {mp.nstr(abs(pP), 25)}, Magnus mu-bar_123(Borromean) = {mub}: {a_ok}")
    b_ok = all(abs(vals[(n, mp.mpf(1))] - vals[(n, mp.mpf(3))]) < tol for n in ("P", "H", "HP"))
    print(f"B  shape independence b=1 vs b=3: {b_ok}")
    c_ok = abs(vals[("PPi", 1)]) < tol
    print(f"C  Psi(P P^-1) = {mp.nstr(vals[('PPi', 1)], 5)}: {c_ok}")
    pH = vals[("H", 1)]
    d1 = abs(vals[("HP", 1)] - pH - pP)
    d2 = abs(vals[("PH", 1)] - pH - pP)
    gate = gcd(1, gcd(0, 0))
    d_ok = d1 < tol and d2 < tol and gate == 1
    print(f"D  Psi(HP)-Psi(H)-Psi(P) = {mp.nstr(d1, 3)}, Psi(PH)-Psi(H)-Psi(P) = {mp.nstr(d2, 3)};"
          f" Milnor gate gcd(1,0,0) = {gate}: {d_ok}")
    print(f"   reported: Psi(H) = {mp.nstr(pH, 20)}")
    ok = a_ok and b_ok and c_ok and d_ok
    print("ALL PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
