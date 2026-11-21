#!/usr/bin/env python3
"""ohtsuki_5_2_asymptotic_crosscheck_probe.py — bean qou-o4k6.

Cross-check of Ohtsuki, "On the asymptotic expansion of the Kashaev invariant
of the 5_2 knot" [ohtsuki2016], held at library/ki52/, by computing the
Kashaev invariant of 5_2 independently from Takata's 2-bridge formula
(computations/probes/takata_twist_knot_colored_jones_probe.py, bean qou-tiwv)
and SnapPy.

PRE-REGISTERED (written before running):

  Source facts used (PDF text layer, Theorem 1.1 and the tables after it):
    S1  <5_2>_N = e^{N varsigma} N^{3/2} omega (1 + sum_i kappa_i (2 pi i/N)^i
        + O(N^{-d-1})), with
          varsigma = 0.4501096100 + 0.4813049796 i,
          omega    = 0.0901905774 - 0.6499757866 i,
          kappa_1  = 1.0537470859 - 0.1055728779 i.
    S2  Table: (<5_2>_N (e^{N varsigma} N^{3/2} omega)^{-1} - 1) N/(2 pi i)
          N = 200: 1.0567234007 - 0.0885918466 i.

  Checks (mpmath 60 dps):
    A  2 pi Re varsigma = Vol(5_2) (SnapPy, high precision), rel < 1e-9.
    B  2 pi |Im varsigma| = |CS(5_2)| mod pi^2 (SnapPy complex_volume), abs < 1e-8.
    C  With K_N the Takata value, or its complex conjugate (Takata's S(7,3) is
       the mirror of Rolfsen's 5_2, check A of the tiwv probe), one fixed
       choice for all N: R(N) = K_N / (e^{N varsigma} N^{3/2} omega) for
       N = 64..120 step 8. Neville extrapolation in 1/N (last 6 points) of
       (R(N) - 1) N/(2 pi i) equals kappa_1, abs < 1e-5.
    D  The N = 200 table entry of S2 is reproduced, abs < 1e-6.
    PASS iff A-D. The bean's named target, the Lean file
    QOU.QBeta.Stokes3LargeOrderAmplitude, is about 4_1 only; it carries no
    5_2 object to compare, which is recorded as a premise finding.

Run: python3 -u computations/probes/ohtsuki_5_2_asymptotic_crosscheck_probe.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from takata_twist_knot_colored_jones_probe import kashaev_52, neville0  # noqa: E402

VS = mp.mpc("0.4501096100", "0.4813049796")
OM = mp.mpc("0.0901905774", "-0.6499757866")
K1 = mp.mpc("1.0537470859", "-0.1055728779")
T200 = mp.mpc("1.0567234007", "-0.0885918466")


def main() -> int:
    import snappy
    mp.mp.dps = 60
    M = snappy.Manifold("5_2").high_precision()
    vol = mp.mpf(str(M.volume()))
    cv = M.complex_volume()
    cs = mp.mpf(str(cv.imag()))
    VS_ = mp.mpc("0.4501096100", "0.4813049796")
    a_rel = abs(2 * mp.pi * VS_.real / vol - 1)
    a_ok = a_rel < mp.mpf("1e-9")
    print(f"A  2 pi Re varsigma = {mp.nstr(2 * mp.pi * VS_.real, 15)}, Vol = {mp.nstr(vol, 15)}, rel {mp.nstr(a_rel, 3)}: {a_ok}")
    p2 = mp.pi ** 2
    d = abs(2 * mp.pi * VS_.imag) - abs(cs)
    d = d - p2 * mp.nint(d / p2)
    b_ok = abs(d) < mp.mpf("1e-8")
    print(f"B  2 pi Im varsigma = {mp.nstr(2 * mp.pi * VS_.imag, 15)}, SnapPy CS = {mp.nstr(cs, 15)}, diff mod pi^2 {mp.nstr(d, 3)}: {b_ok}")

    def table(N, conj):
        mp.mp.dps = 60
        Kn = kashaev_52(N, 60)
        if conj:
            Kn = mp.conj(Kn)
        R = Kn / (mp.e ** (N * VS_) * mp.mpf(N) ** (mp.mpf(3) / 2) * OM)
        return (R - 1) * N / (2j * mp.pi)

    Ns = list(range(64, 121, 8))
    best = None
    for conj in (False, True):
        vals = [table(N, conj) for N in Ns[-6:]]
        lim = neville0([1 / mp.mpf(N) for N in Ns[-6:]], vals)
        err = abs(lim - K1)
        print(f"C  conj={conj}: extrapolated kappa_1 = {mp.nstr(lim, 12)}, |diff| {mp.nstr(err, 3)}", flush=True)
        if best is None or err < best[1]:
            best = (conj, err)
    conj, err = best
    c_ok = err < mp.mpf("1e-5")
    t = table(200, conj)
    d_err = abs(t - T200)
    d_ok = d_err < mp.mpf("1e-6")
    print(f"D  N=200 table value {mp.nstr(t, 12)} vs printed {mp.nstr(T200, 12)}, |diff| {mp.nstr(d_err, 3)}: {d_ok}")
    ok = a_ok and b_ok and c_ok and d_ok
    print("ALL PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
