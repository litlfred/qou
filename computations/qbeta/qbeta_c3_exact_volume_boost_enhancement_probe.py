#!/usr/bin/env python3
"""qbeta_c3_exact_volume_boost_enhancement_probe.py — direction 1: the EXACT figure-8
Im 𝔙₄₁ does NOT close the A≈2.05 muon gap; the survivor is a boost-rapidity
enhancement Re u = √A·ln q₀ (not a spin part, not higher volume terms).

Direct assault on the sole open target (bean qou-iyj5), now slip-safe: the A-polynomial
branch L(M) is validated (#4508 reproduced the proved √3/4 leading coefficient). Here we
integrate the EXACT complex volume and test whether its higher-order terms reach the muon
anchor under the pinned meridian boost Re u = ln q₀.

Exact CS integral (convention fixed empirically against the proved leading √3/4):
At a real boost M = √q₀, the geometric longitude branch L(M) lies on the unit circle
(|L|=1; disc B²−4M⁸ < 0), rotating from −1 by angle θ = arg(−L), with θ ≈ √3·u near u=0.
The exact deformation CS / bar-odd face is

    Im 𝔙₄₁(u) = ½ ∫₀^u arg(−L(M(u'))) du' ,   M(u') = e^{u'/2} ,

which reproduces the leading (√3/4)u² (validated to 0.18% at u = ln q₀; ratio → 1 as u→0).

Findings:
  - Im 𝔙₄₁(real boost u = ln q₀) = 0.0047229 — only 0.18% above the leading 0.0047143.
    A(real boost, exact) = 1.0018 ≈ 1. The exact potential's higher terms are NEGLIGIBLE
    at the anchor (radius R = 2·log φ ≈ 0.96 ≫ u = 0.104, #4508). The exact 𝔙₄₁ does NOT
    reach S(muon) = 0.009683 (A = 2.054).
  - Reaching A ≈ 2.05 requires Re u = c·ln q₀ with c ≈ 1.4305 — the boost rapidity
    enhanced ~43%. Since Im 𝔙₄₁ = (√3/4)(Re²u − Im²u), a spin part Im u ≠ 0 only DECREASES
    Im 𝔙₄₁; it cannot raise A above 1. So the gap is UNAMBIGUOUSLY a Re u boost-enhancement,
    NOT a spin part and NOT higher volume terms.
  - c ≈ 1.4305 = √A (since exact ≈ leading quadratic at the anchor); it is NOT √2 = 1.4142
    and has no clean geometric origin. Deriving it is the irreducible open content.

Verdict: the exact figure-8 volume CONFIRMS the A ≈ 2.05 gap is a genuine boost-rapidity
enhancement — the survivor sharpens to "why is the effective boost √A·ln q₀, not the
meridian rapidity ln q₀?". No fit; nothing wired.
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
from qou_substrate.constants import q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
VOL41 = +(2 * mp.clsin(2, mp.pi / 3))
K = mp.sqrt(3) / 4


def L_geom(M):
    B = M**8 - M**6 - 2 * M**4 - M**2 + 1
    d = mp.sqrt(B**2 - 4 * M**8)
    r1 = (B + d) / (2 * M**4)
    r2 = (B - d) / (2 * M**4)
    return r1 if abs(r1 + 1) < abs(r2 + 1) else r2


def theta(u):
    return mp.arg(-L_geom(mp.e ** (u / 2)))


def ImV(u):
    return mp.quad(theta, [0, u]) / 2       # convention fixed by leading √3/4


def main() -> int:
    print("=" * 78)
    print(" dir1: EXACT Im 𝔙₄₁ vs the A≈2.05 muon gap — boost-rapidity enhancement")
    print("=" * 78)
    q0 = q_muon_at(50)
    lnq = mp.log(q0)
    S_muon = c3_target_at(q0, QCOD, ME) + VOL41

    # validate exact integral against leading √3/4
    val_small = ImV(mp.mpf("0.01")) / (K * mp.mpf("0.01") ** 2)
    val_anchor = ImV(lnq) / (K * lnq ** 2)
    print(f"\n validation: ImV_exact/leading → 1: u=0.01 ratio={mp.nstr(val_small,7)}, "
          f"u=ln q₀ ratio={mp.nstr(val_anchor,7)}")
    validated = abs(val_small - 1) < mp.mpf("1e-3")

    imv_anchor = ImV(lnq)
    lead = K * lnq ** 2
    A_real_boost = imv_anchor / lead
    print(f"\n Im 𝔙₄₁(real boost u=ln q₀) exact = {mp.nstr(imv_anchor,8)}")
    print(f"   leading (√3/4)(ln q₀)²        = {mp.nstr(lead,8)}   A(real boost) = {mp.nstr(A_real_boost,6)}")
    print(f"   S(muon) target (A=2.054)      = {mp.nstr(S_muon,8)}")
    exact_does_not_close = imv_anchor < mp.mpf("0.9") * S_muon   # does not reach S(muon) (here ~0.49×)

    # boost enhancement c needed: ImV(c·ln q₀) = S(muon)
    c = mp.findroot(lambda cc: ImV(cc * lnq) - S_muon, mp.mpf("1.43"))
    A = S_muon / lead
    print(f"\n boost enhancement for A=2.05: Re u = c·ln q₀, c = {mp.nstr(c,7)}")
    print(f"   √A = {mp.nstr(mp.sqrt(A),7)}  (c≈√A since exact≈leading);  √2 = {mp.nstr(mp.sqrt(2),6)}")
    print(f"   c is NOT √2 (differs {mp.nstr(100*(c-mp.sqrt(2))/mp.sqrt(2),3)}%); no clean origin.")
    print("\n ⇒ spin part Im u≠0 only DECREASES Im 𝔙₄₁=(√3/4)(Re²−Im²), so the gap is")
    print("   UNAMBIGUOUSLY a Re u boost-rapidity enhancement (√A·ln q₀), not a spin part,")
    print("   not higher volume terms. Deriving c (≈1.43; leading proxy √A≈1.4332) is the "
          "irreducible open content (qou-iyj5).")

    ok = bool(validated and exact_does_not_close)

    wb = WitnessBuilder("qbeta-c3-exact-volume-boost-enhancement", engine="mpmath")
    wb.set_description(
        "Direction 1 (direct assault on qou-iyj5). Integrates the EXACT figure-8 complex "
        "volume Im 𝔙₄₁(u)=½∫₀^u arg(−L(M)) du' (L = validated A-polynomial branch; convention "
        "fixed by the proved √3/4 leading, reproduced to 0.18% at u=ln q₀). Result: "
        "Im 𝔙₄₁(real boost u=ln q₀)=0.0047229, A(real boost)=1.002 — the exact potential's "
        "higher terms are negligible (radius 0.96≫u), so it does NOT reach S(muon)=0.009683 "
        "(A=2.054). Reaching A=2.05 needs Re u=c·ln q₀, c=1.4305 (exact solve; leading-quadratic "
        "proxy √A=1.4332), NOT √2. Since a spin part "
        "Im u≠0 only decreases Im 𝔙₄₁=(√3/4)(Re²−Im²), the gap is UNAMBIGUOUSLY a boost-rapidity "
        "enhancement, not a spin part or higher volume terms. Deriving c is the open content. "
        "No fit; nothing wired; no instance.")
    wb.set_content_block("conj:binding-qbeta-complex-volume")
    wb.add_data("boost_enhancement_readout", {
        "ImV_exact_real_boost": mp.nstr(imv_anchor, 10),
        "leading_sqrt3_4_u2": mp.nstr(lead, 10),
        "A_real_boost_exact": mp.nstr(A_real_boost, 8),
        "S_muon_target": mp.nstr(S_muon, 10),
        "A_target": mp.nstr(A, 8),
        "boost_enhancement_c": mp.nstr(c, 10),
        "sqrt_A": mp.nstr(mp.sqrt(A), 10),
        "sqrt_2": mp.nstr(mp.sqrt(2), 10),
        "c_is_not_sqrt2": bool(abs(c - mp.sqrt(2)) > mp.mpf("0.01")),
        "exact_potential_does_not_close_gap": bool(exact_does_not_close),
        "leading_validated": bool(validated),
        "verdict": ("exact Im 𝔙₄₁ does NOT close the A≈2.05 muon gap (A_real_boost=1.002); the "
                    "gap is a boost-rapidity enhancement Re u=√A·ln q₀ (c≈1.43, not √2), not a "
                    "spin part or higher volume terms — deriving c (exact≈1.4305, leading proxy "
                    "√A≈1.4332) is the open content")})
    wb.add_assertion("leading_coefficient_validated", str(bool(validated)), "True")
    wb.add_assertion("exact_potential_does_not_close_A205_gap", str(bool(exact_does_not_close)), "True")
    wb.save()
    print("\nwitness → qbeta-c3-exact-volume-boost-enhancement.witness.json")
    print("ALL ASSERTIONS PASS (exact volume confirms boost-enhancement gap)" if ok
          else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
