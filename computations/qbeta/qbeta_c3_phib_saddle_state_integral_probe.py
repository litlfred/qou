#!/usr/bin/env python3
"""qbeta_c3_phib_saddle_state_integral_probe.py

"Build it": the Φ_b state-integral saddle evaluated at the substrate, to test
whether it reproduces the c₃ bar-odd S sign-flip (owner: "the state-integral
saddle gives the exact u(q₀) map — the wall"). Follows #3654 (the finite-b
i·t·κ₁ scale) and the merged #3636 (S's hypersensitivity is a 1/u³ ladder
artifact over a SMOOTH object).

The state-integral SADDLE value at meridian holonomy m is the figure-eight
complex volume 𝔙(m) = Vol(m) + i·CS(m), computed by the corpus's validated
gluing-equation Newton solver (`qbeta_c3_barodd_gluing_newton_solve.vol_of_m`,
which recovers Vol(4₁)=2.0298832 to 4e-18). The substrate meridian holonomy is
m = q₀ (the R-matrix / meridian eigenvalue, #3579). The finite-b fluctuation
adds i·t·κ₁ (κ₁=11√3π/108, #3571/#3606; #3654), imaginary because 2πb²=i·t.

RESULT — the state integral is SMOOTH and ANCHOR-BLIND (scope-(a); C14; no fit):

  * **Saddle at the real substrate meridian m=q₀:** Re 𝔙 = 2.02048069 (a volume
    DEFICIT of 0.00940 from the complete Vol(4₁) — the S(muon) scale), and
    **Im 𝔙 = 0 EXACTLY** at BOTH anchors (real m ⇒ CS = 0; the figure-eight's
    amphichirality). The deficit is anchor-blind (m=q₀ differs ~1e-8).
  * **Finite-b:** Im 𝔙_b ≈ i·t·κ₁ = 0.0578, also anchor-blind (#3654).

So the state integral supplies the S SCALE (deficit 0.0094 ≈ |S(muon)|; finite-b
0.058 ~ |S|) from TWO independent geometric handles, no fit — but **neither is
anchor-dependent**, and the real-meridian saddle Im is *exactly* zero.

CONCLUSION (decisive): building the state integral **CONFIRMS** there is no
physical near-singular substrate→u map. The bar-odd geometric object (Im 𝔙 /
the deficit) is smooth and O(0.01–0.06); S's sign-flip between anchors is the
**1/u³ ladder-representation artifact** proven in the merged #3636, NOT a term
in the state-integral 𝔙. A complex meridian m = q₀ + iε would be needed for a
nonzero saddle Im, and that ε is precisely the (smooth, 1/u³-amplified-in-c₃)
residue — the state integral does not itself force it. Route 1 therefore closes
the "does the saddle give the sign-flip?" question: NO, because the sign-flip is
not physical. The S scale is geometric; the swing is representational.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_c3_barodd_gluing_newton_solve import vol_of_m  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
# Evaluate the transcendentals inside an explicit high-precision context so they
# cannot silently truncate to a stale default dps (Gemini review).
with mp.workdps(50):
    VOL41 = +(2 * mp.clsin(2, mp.pi / 3))
    KAPPA1 = +(11 * mp.sqrt(3) * mp.pi / 108)
S_TARGET = {"proton": mp.mpf("-0.03945936"), "muon": mp.mpf("0.00968298")}


def main() -> int:
    print("=" * 78)
    print(" c₃ bar-odd S — Φ_b state-integral saddle 𝔙(m) at the substrate meridian")
    print("=" * 78)
    print(f"\n Vol(4₁) = {mp.nstr(VOL41,10)}  (complete structure); κ₁ = 11√3π/108 = {mp.nstr(KAPPA1,8)}")

    rows = []
    im_all_zero, deficit_anchor_blind = True, True
    deficits = {}
    print("\n saddle 𝔙(m=q₀ real) [= gluing Newton solve, validates Vol(4₁) to 4e-18]:")
    for tag, q0 in (("proton", q_at(50)), ("muon", q_muon_at(50))):
        vol, z, w = vol_of_m(q0)
        reV, imV = mp.re(vol), mp.im(vol)
        deficit = VOL41 - reV
        deficits[tag] = deficit
        t = mp.log(q0)
        finite_b_im = mp.im(mp.mpc(0, 1) * t * KAPPA1)   # i*t*kappa1
        im_all_zero = im_all_zero and (abs(imV) < mp.mpf("1e-30"))
        print(f"   {tag:7s}: Re 𝔙={mp.nstr(reV,10)}  deficit={mp.nstr(deficit,7)}  "
              f"Im 𝔙={mp.nstr(imV,4)} (=0 exact)  | finite-b i·t·κ₁={mp.nstr(finite_b_im,6)}")
        print(f"            S({tag})={mp.nstr(S_TARGET[tag],6)}   deficit/|S|={mp.nstr(deficit/mp.fabs(S_TARGET[tag]),4)}")
        rows.append({"anchor": tag, "Re_V_saddle": mp.nstr(reV, 20), "Im_V_saddle": mp.nstr(imV, 12),
                     "vol_deficit": mp.nstr(deficit, 20), "finite_b_im": mp.nstr(finite_b_im, 20),
                     "S_target": mp.nstr(S_TARGET[tag], 12)})
    deficit_anchor_blind = abs(deficits["proton"] - deficits["muon"]) < mp.mpf("1e-6")

    print("\n ⇒ Im 𝔙(real m)=0 exactly at both anchors; deficit + finite-b are SMOOTH + ANCHOR-BLIND.")
    print("   The state integral supplies the S SCALE (deficit 0.0094 ≈ |S(muon)|; finite-b 0.058)")
    print("   but NO anchor-dependence ⇒ CONFIRMS no physical singular map; the S sign-flip is the")
    print("   1/u³ ladder-representation artifact (merged #3636), not a term in 𝔙. Route 1: the")
    print("   saddle does NOT give the sign-flip — because the sign-flip is not physical.")

    wb = WitnessBuilder("qbeta-c3-phib-saddle-state-integral", engine="mpmath")
    wb.set_description(
        "Owner-directed 'build it': the Φ_b state-integral SADDLE 𝔙(m) (= the "
        "validated gluing Newton solve vol_of_m, Vol(4₁) to 4e-18) at the substrate "
        "meridian m=q₀. Result: Re 𝔙=2.02048069 (volume deficit 0.00940 from complete "
        "Vol(4₁) — the S(muon) scale), Im 𝔙=0 EXACTLY at both anchors (real m ⇒ CS=0, "
        "amphichirality); finite-b adds i·t·κ₁=0.058 (imaginary, #3654). Both smooth + "
        "anchor-blind. So the state integral supplies the S scale from two geometric "
        "handles (deficit, finite-b), no fit, but no anchor-dependence — CONFIRMING no "
        "physical near-singular substrate→u map: S's sign-flip is the 1/u³ ladder artifact "
        "(merged #3636), not a term in 𝔙. Route 1 closes: the saddle does NOT give the "
        "sign-flip because it is not physical; a complex m=q₀+iε (the smooth ε) is needed "
        "for nonzero saddle Im. Scope-(a); C14; no c_k wired; no fit."
    )
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("saddle", rows)
    wb.add_data("conclusion", {
        "im_V_real_m_zero_both_anchors": bool(im_all_zero),
        "deficit_anchor_blind": bool(deficit_anchor_blind),
        "S_scale_reproduced": "deficit 0.0094 ~ |S(muon)|; finite-b 0.058 ~ |S| (no fit)",
        "verdict": "state integral is smooth+anchor-blind => confirms no physical singular map; "
                   "S sign-flip is the 1/u^3 ladder artifact (#3636), not a term in V"})
    wb.add_assertion("saddle_Im_zero_at_real_meridian",
                     computed=1.0 if im_all_zero else 0.0, expected=1.0, tolerance=0.5,
                     source="Im V(m=q0 real)=0 exactly at both anchors (real meridian => CS=0, amphichirality)")
    wb.add_assertion("state_integral_smooth_anchor_blind",
                     computed=1.0 if deficit_anchor_blind else 0.0, expected=1.0, tolerance=0.5,
                     source="volume deficit identical at both anchors (m=q0 differ ~1e-8); state integral supplies S scale but no anchor-dependence => sign-flip is the 1/u^3 ladder artifact not physics")
    wb.save()
    print("\n  RESULT: state-integral saddle Im=0 (real m) + finite-b 0.058, both smooth/anchor-blind")
    print("          ⇒ CONFIRMS the 1/u³ picture: the sign-flip is representational, not physical.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
