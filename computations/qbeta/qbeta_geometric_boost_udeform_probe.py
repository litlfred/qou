#!/usr/bin/env python3
"""qbeta_geometric_boost_udeform_probe.py — the GEOMETRIC substrate meridian
holonomy u(q₀) = ln q₀ (real boost) tested against the S-channel, under the
CORRECTED harmonic Im form.

Context: the open `u(q₀)` input of the `conj:binding-qbeta-complex-volume`
S-channel (Lean `SDeformedVolumeChannel`; `docs/coordination/
keystone-sdeformedvolume-channel-attack.md`). This is a DERIVE-then-CHECK (no
fit): the meridian log-holonomy is *derived* geometrically, then its `Im 𝔙₄₁`
readout is *checked* against the two measured anchors.

DERIVE (not fitted).
  `content/quantum-observable-universe/braids-and-knots/meridian-holonomy-boost.md`
  (proved sorry-free): the cusp-torus meridian holonomy IS multiplication by the
  substrate parameter q₀ — a hyperbolic BOOST of rapidity `ln q₀` at real q₀>1,
  becoming a compact U(1) SPIN only at |q|=1. So the geometric log meridian
  holonomy is `u = ln q₀` (REAL), plus a spin part that switches on toward |q|=1.

CORRECTED readout (the #4372 fix — this supersedes the WRONG `√3·Re·Im` form used
by `qbeta_c3_geometry_derived_argument_probe.py`, which is a THIRD probe carrying
that error). The figure-eight NZ leading complex volume has a PURELY IMAGINARY
`a₂ = i√3/4` (cusp modulus τ=−i√3, A-polynomial, ℚ(√−3)), so
  Im 𝔙₄₁(u) = (√3/4)(Re²u − Im²u)   (QOU.Knot.FigureEightComplexVolume.imV₄₁)
— vanishing on the DIAGONALS |Re u|=|Im u|, NOT the axes. Under the OLD wrong
form (Im ∝ Re·Im) a real u gave Im 𝔙 = 0 ("silent"); under the CORRECT form a
real boost u=ln q₀ gives Im 𝔙 = (√3/4)(ln q₀)² > 0 — NONZERO.

CHECK / findings (assertions):
  [G1] real boost is muon-sign-correct + right ballpark: Im 𝔙₄₁(ln q₀) > 0 and
       within a small factor of S(muon) > 0.
  [G2] real boost is REFUTED as the FULL map (scope-(a)): the two anchor q₀'s
       differ by ~1e-6, so Im 𝔙₄₁(ln q₀) is NEARLY CONSTANT across anchors and
       cannot produce S(proton) < 0 nor the S(muon)/S(proton) gap.
  [G3] the sign-flip therefore requires the meridian holonomy's BOOST→SPIN
       transition — a complex/spin part pushing u across the diagonal
       (Im²u > Re²u) at the proton side. That hypersensitive spin part is the
       OPEN u(q₀); it is NOT fitted here.

No u-map is wired; no c_k proposed; no SDeformedVolumeChannel instance fabricated.
This is a geometry-side scope-(a) data point sharpening the open constraint.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import c3_target_at  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
with mp.workdps(50):
    VOL41 = +(2 * mp.clsin(2, mp.pi / 3))
KAPPA = mp.sqrt(3) / 4  # |a₂|, the (purely imaginary) NZ leading coeff magnitude


def S(q):
    return c3_target_at(q, QCOD, ME) + VOL41


def imV41(u: mp.mpc) -> mp.mpf:
    """Corrected leading Im 𝔙₄₁ = (√3/4)(Re²u − Im²u)  (imV₄₁, #4372)."""
    return KAPPA * (mp.re(u) ** 2 - mp.im(u) ** 2)


def main() -> int:
    print("=" * 78)
    print(" geometric meridian-boost u(q₀)=ln q₀ vs S-channel (corrected harmonic form)")
    print("=" * 78)

    q_pr, q_mu = q_at(50), q_muon_at(50)
    S_mu, S_pr = S(q_mu), S(q_pr)
    print(f"\n[0] anchors: S(muon)={mp.nstr(S_mu,8)} (tgt +0.00968298)  "
          f"S(proton)={mp.nstr(S_pr,8)} (tgt −0.03945936)")

    # [G1]/[G2] real boost u = ln q₀ (Im u = 0), corrected readout
    u_mu, u_pr = mp.mpc(mp.log(q_mu), 0), mp.mpc(mp.log(q_pr), 0)
    imV_mu, imV_pr = imV41(u_mu), imV41(u_pr)
    print("\n[1] REAL geometric boost u = ln q₀ (meridian-holonomy-boost.md), "
          "corrected Im 𝔙₄₁ = (√3/4)(ln q₀)²:")
    print(f"    muon:   u=ln q₀={mp.nstr(mp.re(u_mu),7)}  Im 𝔙₄₁=+{mp.nstr(imV_mu,7)}  "
          f"S={mp.nstr(S_mu,7)}  ratio Im/S={mp.nstr(imV_mu/S_mu,5)}")
    print(f"    proton: u=ln q₀={mp.nstr(mp.re(u_pr),7)}  Im 𝔙₄₁=+{mp.nstr(imV_pr,7)}  "
          f"S={mp.nstr(S_pr,7)}  sign-match={imV_pr*S_pr>0}")
    d_lnq = mp.re(u_pr) - mp.re(u_mu)
    print(f"    Δ(ln q₀) muon→proton = {mp.nstr(d_lnq,4)}  ⇒ Im 𝔙₄₁ nearly CONSTANT "
          f"across anchors (Δ Im 𝔙₄₁ = {mp.nstr(imV_pr-imV_mu,4)})")

    # findings
    g1_muon_sign = imV_mu > 0 and S_mu > 0
    g1_ballpark = mp.mpf("0.2") < imV_mu / S_mu < mp.mpf("5")   # within a small factor
    g2_proton_wrong_sign = not (imV_pr * S_pr > 0)              # real boost can't give S_pr<0
    g2_nearly_const = abs(imV_pr - imV_mu) < abs(S_mu - S_pr) / 100  # can't span the S gap
    # [G3] diagonal-crossing requirement: proton needs Im²u > Re²u (Im 𝔙 < 0)
    print("\n[2] ⇒ real boost matches muon SIGN + ballpark, but is REFUTED as the full")
    print("    map (scope-(a)): nearly-constant across anchors, cannot give S(proton)<0.")
    print("    The sign-flip needs the BOOST→SPIN transition — a complex/spin part")
    print("    pushing u across the diagonal |Re u|=|Im u| (Im²u>Re²u) at proton. OPEN.")

    wb = WitnessBuilder("qbeta-geometric-boost-udeform", engine="mpmath")
    wb.set_description(
        "Geometric meridian-boost u(q₀)=ln q₀ (meridian-holonomy-boost.md) tested "
        "against the S-channel under the CORRECTED harmonic Im 𝔙₄₁=(√3/4)(Re²u−Im²u) "
        "(#4372). Real boost is muon-sign-correct + right ballpark (Im 𝔙₄₁>0, ~0.5×S_mu) "
        "but REFUTED as the full map (scope-(a)): nearly constant across the ~1e-6-apart "
        "anchor q₀'s, cannot produce S(proton)<0 or the S gap. Sign-flip requires the "
        "boost→spin transition (complex/spin part crossing the diagonal); that part is "
        "the OPEN u(q₀). Corrects the third wrong-form probe "
        "(qbeta_c3_geometry_derived_argument_probe.py). No fit, no c_k, no instance.")
    wb.set_content_block("conj:binding-qbeta-complex-volume")
    wb.add_data("real_boost_readout", {
        "u_muon_ln_q0": mp.nstr(mp.re(u_mu), 12),
        "imV41_muon": mp.nstr(imV_mu, 12), "S_muon": mp.nstr(S_mu, 12),
        "imV41_over_S_muon": mp.nstr(imV_mu / S_mu, 8),
        "u_proton_ln_q0": mp.nstr(mp.re(u_pr), 12),
        "imV41_proton": mp.nstr(imV_pr, 12), "S_proton": mp.nstr(S_pr, 12),
        "delta_ln_q0": mp.nstr(d_lnq, 8),
        "delta_imV41_across_anchors": mp.nstr(imV_pr - imV_mu, 8),
        "verdict": ("real boost u=ln q₀ is muon-sign+ballpark but scope-(a) refuted as "
                    "the full map (nearly constant across anchors); sign-flip needs the "
                    "boost→spin complex part crossing the diagonal — OPEN u(q₀).")})
    wb.add_assertion("real_boost_muon_sign_correct", str(bool(g1_muon_sign)), "True")
    wb.add_assertion("real_boost_muon_ballpark", str(bool(g1_ballpark)), "True",
                     source="Im 𝔙₄₁/S(muon) = " + mp.nstr(imV_mu / S_mu, 5))
    wb.add_assertion("real_boost_wrong_sign_at_proton", str(bool(g2_proton_wrong_sign)), "True")
    wb.add_assertion("real_boost_nearly_constant_refuted_as_full_map",
                     str(bool(g2_nearly_const)), "True",
                     source="Δ Im 𝔙₄₁ = " + mp.nstr(imV_pr - imV_mu, 4)
                            + " ≪ |S gap| = " + mp.nstr(abs(S_mu - S_pr), 4))
    wb.save()
    print("\nwitness → qbeta-geometric-boost-udeform.witness.json")
    ok = all([g1_muon_sign, g1_ballpark, g2_proton_wrong_sign, g2_nearly_const])
    print("ALL ASSERTIONS PASS" if ok else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
