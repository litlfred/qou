#!/usr/bin/env python3
"""Slot sensitivity of the electroweak vev fixed point N_v = v/m_p.

Companion to `QOU/StandardModel/ElectroweakVevFixedPointDecomposition.lean` and
`docs/audits/2026-11-20-ew-vev-fixed-point-derivation.md`.

The formula held by `ElectroweakVevFixedPointClass` is

    N_v = 1/a = T - s*a*H*(1 - c*a),
    T = q([2]/2)[4][6][8] + Z,  Z = 1/pi,  H = [2]/(8 pi),  s = -1,  c = hbar_q^2.

This probe recomputes N_v at the proton-pinned q0 and then changes ONE discrete
slot at a time to the alternative that a uniform rule across the EM and EW
sectors would give. It does not choose among them; it reports how far each
slot moves N_v, in ppb and in units of the experimental sigma on v/m_p
(sigma from G_F only, 0.514 ppm on G_F -> 0.257 ppm on v).

All arithmetic is mpmath at 60 dps. No witness is written.
"""
from __future__ import annotations

import sys
from pathlib import Path

THIS = Path(__file__).resolve()
COMPUTE_DIR = THIS.parent.parent
sys.path.insert(0, str(COMPUTE_DIR))
sys.path.insert(0, str(COMPUTE_DIR / "substrate"))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402
from mpmath import mpf  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_P_MEV_VALIDATION  # noqa: E402

mp.mp.dps = 60


def main() -> int:
    q = mpf(Q_50_DIGIT_STR)  # proton pin
    qi = 1 / q
    h = q - qi
    hbar = 1 - qi
    pi = mp.pi

    def b(k: int) -> mpf:
        return (q ** k - qi ** k) / h

    G_F = mpf("1.1663787e-5")
    G_F_sig = mpf("0.0000006e-5")
    m_p = M_P_MEV_VALIDATION / mpf(1000)
    v = 1 / mp.sqrt(mp.sqrt(mpf(2)) * G_F)
    N_exp = v / m_p
    sig = N_exp * G_F_sig / (2 * G_F)
    H = b(2) / (8 * pi)

    def solve(T: mpf, s: int, c: mpf) -> mpf:
        f = lambda a: 1 / a - (T + s * a * H * (1 - c * a))  # noqa: E731
        return 1 / mp.findroot(f, 1 / T)

    bare = q * b(4) * b(6) * b(8)
    tree = bare * b(2) / 2
    rows = [
        ("as published: tree q([2]/2)[4][6][8], Z=1/pi, s=-1, c=hbar^2",
         solve(tree + 1 / pi, -1, hbar ** 2)),
        ("c = h^2 (corpus skein contraction hecke_skein_bar_contraction)",
         solve(tree + 1 / pi, -1, h ** 2)),
        ("s = +1 (EM loop sign), c = hbar^2", solve(tree + 1 / pi, +1, hbar ** 2)),
        ("s = +1, c = h^2 (EM relation transcribed)", solve(tree + 1 / pi, +1, h ** 2)),
        ("no loop term (tree + Z only)", tree + 1 / pi),
        ("Z = 2/(3 pi) (surface-genus rule, as in EM)", solve(tree + 2 / (3 * pi), -1, hbar ** 2)),
        ("no zero mode", solve(tree, -1, hbar ** 2)),
        ("bare tree q[4][6][8] (no [2]/2, as in EM)", solve(bare + 1 / pi, -1, hbar ** 2)),
        ("([2]/2)^3, one dressing per 2-strand carrier", solve(bare * (b(2) / 2) ** 3 + 1 / pi, -1, hbar ** 2)),
    ]
    print(f"q0 (proton)         = {mp.nstr(q, 30)}")
    print(f"v/m_p (G_F, CODATA) = {mp.nstr(N_exp, 15)}   sigma = {mp.nstr(sig / N_exp * mpf(10) ** 9, 6)} ppb")
    print(f"bare q[4][6][8]     = {mp.nstr(bare, 15)}")
    print(f"tree q([2]/2)[4][6][8] = {mp.nstr(tree, 15)}")
    for name, N in rows:
        ppb = (N - N_exp) / N_exp * mpf(10) ** 9
        print(f"{name:66s} N_v = {mp.nstr(N, 15):>18s}  miss {mp.nstr(ppb, 6):>12s} ppb  {mp.nstr((N - N_exp) / sig, 4):>9s} sigma")

    # EM side: does the same 2-strand dressing applied to T(2,9) keep the EM tree?
    em_bare = q * b(9) * b(10)
    print(f"EM bare q[9][10]       = {mp.nstr(em_bare, 15)}")
    print(f"EM dressed q([2]/2)[9][10] = {mp.nstr(em_bare * b(2) / 2, 15)} (vs 137.035999177)")

    # Carrier coefficient identity a4 a6 a8 [2]^3 = h^3 [4][6][8], with a_n from the recursion.
    a, bb = mpf(0), mpf(1)
    coeffs = {}
    for n in range(1, 9):
        a, bb = h * a + bb, a
        coeffs[n] = a
    lhs = coeffs[4] * coeffs[6] * coeffs[8] * b(2) ** 3
    rhs = h ** 3 * b(4) * b(6) * b(8)
    print(f"carrier identity residual a4a6a8[2]^3 - h^3[4][6][8] = {mp.nstr(lhs - rhs, 5)}")
    print(f"a4a6a8 = {mp.nstr(coeffs[4] * coeffs[6] * coeffs[8], 15)}  (h/[2])^3 = {mp.nstr((h / b(2)) ** 3, 15)}")
    assert abs(lhs - rhs) < mpf(10) ** -50
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
