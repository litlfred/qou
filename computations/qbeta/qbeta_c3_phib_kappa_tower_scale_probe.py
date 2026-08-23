#!/usr/bin/env python3
"""qbeta_c3_phib_kappa_tower_scale_probe.py

Joint tightening (coordination with #3628): extend the merged #3654 finite-b
state-integral correction to the c₃ bar-odd S using the exact Ohtsuki tower
κ₁..κ₄ derived on #3628 (branch `z-c-k-f-map-keystone-ub5yix`):

    κ₁ = (11/108)√3π   κ₂ = (2/27)π²   κ₃ = (1081/21870)√3π³   κ₄ = (98/729)π⁴
    (odd rungs carry √3, even rungs pure-rational — the ℚ(√−3) trace-field
     signature; κ_n^Oht ∈ ℚ(√−3), √3 emerges via ℏ=2πi/N.)

The figure-eight finite-b complex volume at the substrate is
    𝔙_b = 𝔙_0 + Σ_n (2πb²)ⁿ κ_n,   2πb² = i·t,  t = ln q₀   (#3654: imaginary substrate).
Because (i·t)ⁿ alternates real/imaginary and κ_n are real:

  * **Im 𝔙_b (the bar-ODD S) is fed ONLY by the ODD rungs:** Im 𝔙_b = t·κ₁ − t³·κ₃ + …
  * **Re 𝔙_b (the bar-EVEN Vol) is fed ONLY by the EVEN rungs:** Re-corr = −t²·κ₂ + t⁴·κ₄ + …

This is the state-integral realization of #3628's **√3-parity alternation**: the
√3-carrying odd Ohtsuki rungs land on the bar-odd S, the pure-rational even rungs
on the bar-even Vol. Bar-parity is exact and structural.

RESULT (scope-(a); C14; no fit; no c_k wired):

  * Summing κ₁..κ₄ **tightens the S scale** from the leading `t·κ₁ ≈ 0.05783` to
    `t·κ₁ − t³·κ₃ ≈ 0.05481` (a −5.21 % correction), still `~0.055`.
  * It stays **SMOOTH + ANCHOR-BLIND** (both anchors identical to ~1e-8) — as it
    must: the exact anchor-dependent S is the `1/u³` ladder *representation* of
    this smooth object (merged #3636), NOT `Im 𝔙_b` itself. So the tower refines
    the smooth *scale*, and (correctly) does not reproduce the ±sign-flip.

CONCLUSION: #3628's κ-tower + the #3654 finite-b picture give the bar-odd S scale
to higher order (0.0548) AND the exact bar-parity mechanism (odd rungs → Im,
√3-carrying). The anchor-dependence remains representational per the merged
capstone; nothing here is a fit or a wiring.

Ohtsuki κ₁..κ₄ values cited from #3628 (`qbeta_ohtsuki_higher_rungs.py`).

Superseded-mechanism note (merged #3692): the bar-parity mechanism demonstrated
numerically here (odd rungs → Im 𝔙, even rungs → Re 𝔙) is now **Lean-proved
sorry-free** in `OhtsukiTowerBarParity.lean` (`even_rung_real`,
`odd_rung_imaginary`), and the full divergent tower is **Borel–Padé resummed** to
the exact smooth Im 𝔙 = 0.05545 in `qbeta_c3_borel_pade_resummation_probe.py`
(which cites this probe's κ₁..κ₄ truncation value 0.05481 as its baseline). This
probe stands as the finite-truncation-order scale computation and the #3628
coordination point; #3692 carries the proof + resummation.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
with mp.workdps(50):
    PI = +mp.pi
    S3 = +mp.sqrt(3)
    # exact Ohtsuki tower (#3628); odd rungs carry sqrt3, even rungs rational
    K1 = +(mp.mpf(11) / 108 * S3 * PI)
    K2 = +(mp.mpf(2) / 27 * PI ** 2)
    K3 = +(mp.mpf(1081) / 21870 * S3 * PI ** 3)
    K4 = +(mp.mpf(98) / 729 * PI ** 4)


def main() -> int:
    print("=" * 78)
    print(" c₃ bar-odd S — Im 𝔙_b with the exact Ohtsuki tower κ₁..κ₄ (#3628, joint)")
    print("=" * 78)
    print(f"\n κ₁={mp.nstr(K1,8)} κ₂={mp.nstr(K2,8)} κ₃={mp.nstr(K3,8)} κ₄={mp.nstr(K4,8)}")
    print(" (odd κ₁,κ₃ carry √3 → feed Im 𝔙 = bar-odd S; even κ₂,κ₄ rational → feed Re 𝔙 = Vol)")

    rows = []
    lead_all, full_all = {}, {}
    for tag, q0 in (("proton", q_at(50)), ("muon", q_muon_at(50))):
        t = mp.log(q0)
        it = mp.mpc(0, 1) * t
        terms = [it * K1, it ** 2 * K2, it ** 3 * K3, it ** 4 * K4]
        im_lead = mp.im(terms[0])                       # t*kappa1
        im_full = sum(mp.im(x) for x in terms)          # t*k1 - t^3*k3
        re_corr = sum(mp.re(x) for x in terms)          # -t^2*k2 + t^4*k4
        lead_all[tag], full_all[tag] = im_lead, im_full
        shift = (im_full / im_lead - 1) * 100
        print(f"\n {tag:7s}: t={mp.nstr(t,8)}")
        print(f"   Im 𝔙_b: lead(κ₁)={mp.nstr(im_lead,8)}  full(κ₁..κ₄)={mp.nstr(im_full,8)}  ({mp.nstr(shift,3)}%)")
        print(f"   Re-corr(κ₂,κ₄)={mp.nstr(re_corr,8)}")
        rows.append({"anchor": tag, "t": mp.nstr(t, 20),
                     "Im_V_lead_kappa1": mp.nstr(im_lead, 20),
                     "Im_V_full_kappa1_4": mp.nstr(im_full, 20),
                     "shift_pct": mp.nstr(shift, 6),
                     "Re_corr_even": mp.nstr(re_corr, 20)})

    anchor_blind = abs(full_all["proton"] - full_all["muon"]) < mp.mpf("1e-6")
    tightened = abs(full_all["muon"] - lead_all["muon"]) > mp.mpf("1e-4")
    print(f"\n ⇒ κ-tower tightens Im 𝔙_b scale 0.0578→0.0548 (−5.2%); anchor-blind? {anchor_blind}")
    print("   Bar-parity exact: odd rungs (√3) → Im 𝔙 (bar-odd S); even rungs (ℚ) → Re 𝔙 (Vol).")
    print("   Still smooth/anchor-blind ⇒ exact S = 1/u³ ladder representation of this (merged #3636),")
    print("   not Im 𝔙_b itself. The tower refines the smooth SCALE, not the ±sign-flip.")

    wb = WitnessBuilder("qbeta-c3-phib-kappa-tower-scale", engine="mpmath")
    wb.set_description(
        "Joint tightening (coordination with #3628): extend the merged #3654 finite-b "
        "state-integral S-scale using #3628's exact Ohtsuki tower κ₁..κ₄ "
        "(κ₁=11√3π/108, κ₂=2π²/27, κ₃=1081√3π³/21870, κ₄=98π⁴/729). At the substrate "
        "2πb²=i·t, so Im 𝔙_b (bar-odd S) is fed ONLY by odd rungs (t·κ₁−t³·κ₃) and "
        "Re 𝔙_b by even rungs — the state-integral realization of #3628's √3-parity "
        "alternation (odd→√3→Im, even→rational→Re). The κ-tower tightens the S scale "
        "0.0578→0.0548 (−5.21%), still smooth + anchor-blind. Exact anchor-dependent S "
        "is the 1/u³ ladder representation of this smooth object (merged #3636), not "
        "Im 𝔙_b; the tower refines the scale, not the sign-flip. κ values cited from "
        "#3628. Scope-(a); C14; no c_k wired; no fit."
    )
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("kappa_tower", {"k1": "11*sqrt3*pi/108", "k2": "2*pi^2/27",
                                "k3": "1081*sqrt3*pi^3/21870", "k4": "98*pi^4/729",
                                "source": "#3628 qbeta_ohtsuki_higher_rungs.py",
                                "parity": "odd rungs sqrt3 -> Im (bar-odd S); even rungs rational -> Re (Vol)"})
    wb.add_data("scale_tightening", rows)
    wb.add_data("conclusion", {
        "im_V_b_lead": "0.05783 (t*kappa1)", "im_V_b_full": "0.05481 (t*k1 - t^3*k3)",
        "shift_pct": "-5.21", "anchor_blind": bool(anchor_blind),
        "note": "tightens smooth scale; exact S = 1/u^3 ladder representation (#3636), not Im V_b"})
    wb.add_assertion("kappa_tower_tightens_scale_stays_anchor_blind",
                     computed=1.0 if (tightened and anchor_blind) else 0.0, expected=1.0, tolerance=0.5,
                     source="summing kappa1..kappa4 shifts Im V_b 0.0578->0.0548 (odd rungs only) and stays anchor-blind at both anchors")
    wb.save()
    print("\n  RESULT: κ₁..κ₄ tightens Im 𝔙_b to 0.0548; odd rungs→Im (bar-odd), even→Re; anchor-blind")
    print("          (exact S sign-flip stays the 1/u³ representation, merged #3636).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
