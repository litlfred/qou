#!/usr/bin/env python3
"""qbeta_odd_channel_saddle_crosslink_check.py

Structural cross-link between the odd-channel D-ladder divergence finding
(qbeta_odd_channel_stokes_borel_probe.py, #3810) and the landed Φ_b 2-loop
saddle data (main 360a1b22d9 A1 derivation; 57a0fcd02f k=21-gate analysis).

Verifies three exact/near facts about the figure-eight (4_1) state-integral
potential V(z)=Li₂(z)−Li₂(1/z) at the saddle z*=e^{iπ/3}=(1+i√3)/2:

  G2  −V''(z*) = −3/2 + i·√3/2,  |−V''(z*)| = √3   (adjoint Reidemeister torsion)
  G1  Im V(z*) = Vol(4_1) = 2.0298832…            (hyperbolic volume)
  BAND  Vol(4_1)/(4π) = 0.16153 ∈ [0.147, 0.168]  (odd-face Borel band, #3810)

Consequence (recorded, not a closure): the odd ladder is ℚ(√3)-valued because
the bar-odd (imaginary) part of the saddle Hessian is √3/2 — the same √3, same
6th-root-of-unity saddle; and the odd-face band candidate Vol(4_1)/(4π) is the
saddle's imaginary potential over the 4π two-channel loop measure, not an
arbitrary constant. Still not an identification (12% s-systematic on the band;
exact action needs the non-perturbative q-Borel/3d-index, #3805). scope-(a);
no c_k wired; no fit; comparison-only.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401
sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
# Vol(4_1) EXACT = 2*Cl_2(pi/3); the literal printed 37 digits, correct to 30 (qou-ckbv)
VOL_4_1 = 2 * mp.clsin(2, mp.pi / 3)


def main() -> int:
    zc = mp.e ** (1j * mp.pi / 3)
    V = lambda z: mp.polylog(2, z) - mp.polylog(2, 1 / z)
    Vpp = mp.diff(V, zc, 2)

    torsion_err = abs(-Vpp - (-mp.mpf(3) / 2 + 1j * mp.sqrt(3) / 2))
    torsion_mod_err = abs(abs(Vpp) - mp.sqrt(3))
    vol_err = abs(mp.im(V(zc)) - VOL_4_1)
    band_val = VOL_4_1 / (4 * mp.pi)
    in_band = mp.mpf("0.147") <= band_val <= mp.mpf("0.168")

    print("=" * 72)
    print(" odd-channel ↔ Φ_b saddle cross-link (4_1, z*=e^{iπ/3})")
    print("=" * 72)
    print(f"  z*            = {mp.nstr(zc, 12)}")
    print(f"  −V''(z*)      = {mp.nstr(-Vpp, 12)}   (target −3/2 + i√3/2)")
    print(f"  |−V''(z*)|    = {mp.nstr(abs(Vpp), 14)}   √3 = {mp.nstr(mp.sqrt(3), 14)}")
    print(f"  Im V(z*)      = {mp.nstr(mp.im(V(zc)), 14)}   Vol(4_1) = {mp.nstr(VOL_4_1, 14)}")
    print(f"  Vol(4_1)/(4π) = {mp.nstr(band_val, 10)}   in odd-face band [0.147,0.168]: {in_band}")
    print(f"\n  G2 torsion err = {mp.nstr(torsion_err, 4)}, |·| err = {mp.nstr(torsion_mod_err, 4)}")
    print(f"  G1 vol err     = {mp.nstr(vol_err, 4)}")

    wb = WitnessBuilder("qbeta-odd-channel-saddle-crosslink", engine="mpmath")
    wb.set_description(
        "Cross-link: the 4_1 saddle z*=e^{iπ/3} has −V''=−3/2+i√3/2 (|·|=√3, the "
        "adjoint torsion G2) and Im V=Vol(4_1) (G1). The odd D-ladder is ℚ(√3)-valued "
        "from the √3/2 bar-odd Hessian part; the odd-face Borel band [0.147,0.168] "
        "(#3810) contains Vol(4_1)/(4π)=0.16153 = saddle imaginary potential / 4π "
        "two-channel loop measure. Structural expectation, not identification (12% "
        "s-systematic; exact action needs 3d-index #3805). scope-(a); no fit.")
    wb.set_content_block("conj:faddeev-phi-b-quasiperiod")
    wb.add_data("saddle", "e^{i pi/3}")
    wb.add_data("neg_Vpp", [float(mp.re(-Vpp)), float(mp.im(-Vpp))])
    wb.add_data("torsion_modulus", float(abs(Vpp)))
    wb.add_data("im_V_saddle", float(mp.im(V(zc))))
    wb.add_data("vol_4_1_over_4pi", float(band_val))
    wb.add_assertion("hessian_is_sqrt3_torsion", computed=float(torsion_err), expected=0.0,
                     tolerance=1e-20, source="−V''(z*) = −3/2 + i√3/2, |−V''| = √3")
    wb.add_assertion("im_V_is_vol_4_1", computed=float(vol_err), expected=0.0,
                     tolerance=1e-20, source="Im V(z*) = Vol(4_1)")
    wb.add_assertion("vol_over_4pi_in_odd_band", computed=float(in_band), expected=1.0,
                     tolerance=0.5, source="Vol(4_1)/(4π)=0.16153 ∈ [0.147,0.168] (#3810)")
    wb.save()
    ok = torsion_err < 1e-20 and vol_err < 1e-20 and in_band
    print(f"\n  RESULT: {'ALL OK' if ok else 'CHECK'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
