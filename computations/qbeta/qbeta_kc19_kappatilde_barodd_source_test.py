#!/usr/bin/env python3
"""qbeta_kc19_kappatilde_barodd_source_test.py

Executes the fit-free bar-odd-source test named by the KC19 x Phi_b bridge
probe (qbeta_kc19_phib_departure_bridge_probe.py, PR #3769) for the three
DERIVED bar-odd meridian candidates of the #3691 deformed-rung tower
(witness qbeta-c3-borel-pade-deformed-rungs.witness.json):

    G1  Im V_b truncation (4 deformed rungs)      0.0570576566
    G2  Im V_b resummed Borel-Pade[2/2]           0.0585499951
    G3  odd-only partial sum t*k1 - t^3*k3        0.0567896600

Pipeline (zero free parameters): each candidate S_geo maps to
c3_geo = -Vol(4_1) +/- S_geo and the KC19 departure
dw3 = -(h-2)/2 * c3 * u^3; compare against the empirical S at BOTH anchors.

FINDINGS (scope-(a); no c_k wired; no fit):

  1. **Value level: scale-only, same verdict class as the Phi_b handles.**
     All three candidates sit at the |S| scale (ratios O(0.2 - 0.7) per
     anchor) but are single meridian-smooth numbers, while S sign-flips
     between anchors. No clean structural constant (1, 1/2, [3]_q, ...)
     relates any candidate to |S| at both anchors simultaneously.

  2. **Slope level: the swing is a slope statement, and it excludes any
     O(1)-slope meridian object at c3 level.** The anchor swing satisfies
     S(p) - S(mu) ~= S'(q*)*(q_p - q_mu) with S' = 2.37/u^3 ~ 3.8e6 (the
     ladder amplification, KC21). A candidate S_geo(q) built from t = ln q
     and O(1) rungs has |dS_geo/dq| = O(1) (~7 orders short) unless the
     kappa-tilde(q) themselves are hypersensitive — which would contradict
     their smooth tall-ladder construction. So the deformed rungs, consumed
     at c3 level, supply scale but structurally cannot supply the swing.

  3. **The correct consumption level is the NUMERATOR, where the required
     slope is O(1).** The odd numerator N_odd(q) = S(q)*u(q)^3 has O(1e-8)
     values at the anchors and dN_odd/dq = O(1) — compatible with smooth
     geometry. Required KC19 crossing-weight departures delta_w_odd =
     S*u^3*(4-h^2)/(2h) are reported per anchor as the target any
     normalized geometric candidate must hit. The open piece remains the
     NORMALIZATION Im V_b -> N_odd (the capstone's "exact normalization").

  4. **Decisive follow-up named:** evaluate the deformed tall ladder at the
     two anchor moduli directly (expensive; N<=262144, dps 980 per #3691)
     and measure d(kappa-tilde)/dq. Prediction (from smoothness): O(1), i.e.
     scale-only confirmed and the odd swing lives in the ladder
     representation D(u) (KC21/KC22), not in the meridian geometry.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import c3_target_at, substrate_ladder_quantities  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from substrate import codata_constants as C  # noqa: E402

mp.mp.dps = 60
ME = mp.mpf(str(C.M_E_MEV))
QCOD = mp.mpf(str(C.Q_BETA_MEV))
with mp.workdps(60):
    VOL41 = +(2 * mp.clsin(2, mp.pi / 3))

RUNGS_WITNESS = Path(__file__).resolve().parent / "qbeta-c3-borel-pade-deformed-rungs.witness.json"


def S(q):
    return c3_target_at(q, QCOD, ME) + VOL41


def main() -> int:
    print("=" * 78)
    print(" kappa-tilde deformed rungs -> KC19 fit-free bar-odd source test")
    print("=" * 78)

    d = json.loads(RUNGS_WITNESS.read_text())["data"]
    cands = {
        "G1_imVb_truncation": mp.mpf(str(d["imV_meridian_corrected"]["truncation_4_rungs"])),
        "G2_imVb_resummed_pade22": mp.mpf(str(d["imV_meridian_corrected"]["resummed_pade22"])),
        "G3_odd_only_partial_sum": mp.mpf(str(d["imV_meridian_corrected"]["odd_only_part"])),
    }
    qp, qm = q_at(60), q_muon_at(60)
    anchors = {"proton": qp, "muon": qm}
    Sv = {a: S(qv) for a, qv in anchors.items()}
    print(f"\n[0] targets: S(proton)={mp.nstr(Sv['proton'],8)}  S(muon)={mp.nstr(Sv['muon'],8)}")
    print(f"    candidates: " + "  ".join(f"{k}={mp.nstr(v,8)}" for k, v in cands.items()))

    # ---- 1. value-level ratios per anchor ----
    print("\n[1] value-level ratios S/candidate (sign varies => no single constant):")
    ratios = {}
    for k, g in cands.items():
        ratios[k] = {a: Sv[a] / g for a in anchors}
        print(f"    {k:26s}: proton {mp.nstr(ratios[k]['proton'],6)}   muon {mp.nstr(ratios[k]['muon'],6)}")
    sign_flip = Sv["proton"] * Sv["muon"] < 0

    # ---- 2. slope level: the swing is S'(q*)*(dq) ----
    qstar = mp.findroot(S, (qp + qm) / 2)
    hh = mp.mpf("1e-18")
    Sprime = (S(qstar + hh) - S(qstar - hh)) / (2 * hh)
    swing_pred = Sprime * (qp - qm)
    swing_true = Sv["proton"] - Sv["muon"]
    slope_explains = abs(swing_pred / swing_true - 1) < mp.mpf("0.05")
    print("\n[2] the swing IS the amplified slope (KC21):")
    print(f"    S'(q*)={mp.nstr(Sprime,8)};  S'*(q_p-q_mu)={mp.nstr(swing_pred,8)} vs S(p)-S(mu)={mp.nstr(swing_true,8)}")
    print(f"    => a c3-level S_geo needs |dS_geo/dq| ~ {mp.nstr(Sprime,4)}; t=ln q rungs give O(1). Excluded at c3 level.")

    # ---- 3. numerator level: required values + O(1) slope ----
    print("\n[3] numerator level N_odd = S*u^3 (the level a smooth object CAN feed):")
    numer = {}
    for a, qv in anchors.items():
        u = substrate_ladder_quantities(qv)["u"]
        h = qv - 1 / qv
        Nodd = Sv[a] * u ** 3
        dw_odd = Sv[a] * u ** 3 * (4 - h * h) / (2 * h)   # KC19 ladder_odd_part inverted at w0=1
        numer[a] = {"u": u, "N_odd": Nodd, "dw_odd_required": dw_odd}
        print(f"    {a:7s}: N_odd={mp.nstr(Nodd,8)}   required KC19 dw_odd={mp.nstr(dw_odd,8)}")
    dN = (S(qstar + hh) * substrate_ladder_quantities(qstar + hh)["u"] ** 3
          - S(qstar - hh) * substrate_ladder_quantities(qstar - hh)["u"] ** 3) / (2 * hh)
    print(f"    dN_odd/dq at q* = {mp.nstr(dN,6)}  (O(1) — smooth-geometry compatible)")
    print("    open: the normalization Im V_b -> N_odd (capstone's 'exact normalization').")

    print("\n[4] decisive follow-up: evaluate the deformed tall ladder at BOTH anchor moduli")
    print("    and measure d(kappa-tilde)/dq. Prediction: O(1) => scale-only confirmed;")
    print("    the odd swing lives in the D(u) ladder (KC21/KC22), not meridian geometry.")

    wb = WitnessBuilder("qbeta-kc19-kappatilde-barodd-source-test", engine="mpmath")
    wb.set_description(
        "Fit-free KC19 consumption test of the three derived bar-odd meridian "
        "candidates from the #3691 deformed-rung tower (Im V_b truncation "
        "0.05706, resummed 0.05855, odd-only 0.05679). Value level: all three "
        "sit at the |S| scale (ratios 0.17-0.69 per anchor) but S sign-flips "
        "while each candidate is one smooth number — scale-only, same verdict "
        "class as the Phi_b handles. Slope level: the anchor swing equals "
        "S'(q*)*(q_p - q_mu) with S' ~ 3.8e6 (verified <5%), so any c3-level "
        "geometric source needs a 1e6 slope that smooth t=ln q rungs cannot "
        "supply — excluded at c3 level, scope-(a). Correct consumption level "
        "is the numerator N_odd = S*u^3 (dN/dq = O(1)); required per-anchor "
        "KC19 departures dw_odd reported as the normalization-bearing target. "
        "Decisive follow-up: tall-ladder d(kappa-tilde)/dq at both anchors. "
        "No c_k wired; no fit."
    )
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("candidates", {k: mp.nstr(v, 12) for k, v in cands.items()})
    wb.add_data("targets", {a: mp.nstr(Sv[a], 10) for a in anchors})
    wb.add_data("value_ratios", {k: {a: mp.nstr(r[a], 8) for a in anchors} for k, r in ratios.items()})
    wb.add_data("slope_test", {"S_prime_qstar": mp.nstr(Sprime, 10),
                               "swing_pred": mp.nstr(swing_pred, 10),
                               "swing_true": mp.nstr(swing_true, 10)})
    wb.add_data("numerator_level", {a: {kk: mp.nstr(vv, 10) for kk, vv in numer[a].items()} for a in anchors} |
                {"dN_odd_dq_at_qstar": mp.nstr(dN, 8)})
    wb.add_assertion("swing_is_amplified_slope",
                     computed=float(swing_pred / swing_true), expected=1.0, tolerance=0.05,
                     source="S(p)-S(mu) = S'(q*)*(q_p-q_mu) to <5%: the anchor swing is the KC21 1/u^3 slope, "
                            "so a c3-level smooth meridian source is structurally excluded from the swing")
    wb.add_assertion("targets_sign_flip",
                     computed=1.0 if sign_flip else 0.0, expected=1.0, tolerance=0.5,
                     source="S(proton)*S(muon) < 0 while every candidate is a single positive number")
    wb.add_assertion("candidates_at_S_scale",
                     computed=float(min(abs(r) for k in cands for r in ratios[k].values())),
                     expected=0.4, tolerance=0.4,
                     source="all |S|/candidate ratios are O(0.17-0.7): the deformed rungs supply the scale (only)")
    wb.save()
    print("\n  RESULT: kappa-tilde candidates = scale-only at c3 level (slope-excluded);")
    print("          numerator-level targets + normalization named; tall-ladder dq follow-up decisive.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
