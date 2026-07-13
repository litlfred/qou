#!/usr/bin/env python3
"""qbeta_kc19_phib_departure_bridge_probe.py

Bridge probe: KC19 (affine crossing-weight evaluation) × Φ_b state-integral
geometry (#3654). KC19 proves the archimedean evaluation is AFFINE in the
crossing weight w with an anchor-rigid kernel, and the exact inversion
(Lean `ladder_departure`, sorry-free) gives the departure

    w(u) − 1 = −(h−2)/2 · Σ_{k≥2} c_k u^k,   (h−2)/2 = (q² − 2q − 1)/(2q),

so the entire c₃ odd channel S = c₃ + Vol(4₁) enters w LINEARLY through the
fixed prefactor. The Φ_b saddle witness (#3654) supplies two geometric
handles at the |S| scale — the volume deficit (≈0.0094) and the finite-b
correction t·κ₁ (≈0.0578) — both smooth and ANCHOR-BLIND. This probe pushes
each handle through the exact KC19 bridge and asks, anchor-by-anchor with
zero free parameters: can either handle source the required departure?

FINDINGS (scope-(a); no c_k wired; no fit; registry §8 respected):

  1. **The bridge is exact and parameter-free.** The Lean identity
     `(h−2)/2 = (q²−2q−1)/(2q)` (`departure_factor_eq`) reproduces to
     working precision at both anchors; the required u³-order departure
     `δw₃ = −(h−2)/2·c₃·u³` and its S-part are computed exactly from the
     extractor chain. Once ANY bar-odd geometric object is computed at the
     substrate meridian, it maps to a c₃ candidate with NO free parameter:
     `c₃_geo = −Vol(4₁) + S_geo`, `δw₃_geo = −(h−2)/2·c₃_geo·u³`.

  2. **Scale matches, parity does not: the even handles cannot source the
     swing.** |S|/handle is O(1) for both handles at both anchors (the
     capstone's "right scale, no fit" — quantified here per anchor). But the
     handles are anchor-blind to ~2×10⁻⁷ relative, while S sign-flips
     between anchors (+0.0097 μ / −0.0395 p). Under KC19 anchor-rigidity
     (the kernel K(q) carries no anchor dependence) an anchor-blind bar-even
     handle pushed through the affine bridge yields an anchor-blind
     departure — it can supply the |S| SCALE but structurally cannot supply
     the SWING or the sign. This composes three proved/witnessed facts
     (affine bridge + anchor-rigid kernel + witnessed anchor-blindness);
     scope-(a): these two handles, alone, as evaluated at the real meridian,
     do not close S.

  3. **What closes it (named target).** The missing object is a BAR-ODD
     geometric quantity at the meridian — per the saddle witness's own
     `scope.open`: the ℚ(√−3) odd channel / κ₁(u) at meridian u = 2·log q₀,
     and the deformed rungs κ̃₁, κ̃₃ (#3691) are the available candidates.
     The bridge here means any such computation is IMMEDIATELY testable:
     evaluate it at both anchors, map through step 1, compare to S — a
     falsifiable, fit-free pipeline.

Consumes the committed saddle witness
`qbeta-c3-phib-saddle-state-integral.witness.json` (canonical producer
`qbeta_c3_phib_saddle_state_integral_probe.py`) rather than re-running the
state integral.
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

SADDLE_WITNESS = Path(__file__).resolve().parent / "qbeta-c3-phib-saddle-state-integral.witness.json"


def S(q):
    return c3_target_at(q, QCOD, ME) + VOL41


def departure_prefactor(q):
    """−(h−2)/2 with h = q − 1/q (Lean `ladder_departure` prefactor, sign in)."""
    h = q - 1 / q
    return -(h - 2) / 2


def main() -> int:
    print("=" * 78)
    print(" KC19 × Φ_b bridge: push the geometric handles through the affine departure")
    print("=" * 78)

    qp, qm = q_at(60), q_muon_at(60)
    anchors = {"proton": qp, "muon": qm}

    # ---- 0. anchors + saddle witness handles ----
    saddle = {row["anchor"]: row for row in json.loads(SADDLE_WITNESS.read_text())["data"]["saddle"]}
    repro = all(
        abs(S(q) - mp.mpf(saddle[name]["S_target"])) < mp.mpf("1e-6")
        for name, q in anchors.items()
    )
    print(f"\n[0] anchors reproduced vs saddle witness: {repro}")

    # ---- 1. Lean identity check + exact required departure ----
    print("\n[1] exact KC19 departure (w₀=1 counit; Lean ladder_departure):")
    ident_ok = True
    rows = {}
    for name, q in anchors.items():
        h = q - 1 / q
        lhs = (h - 2) / 2
        rhs = (q * q - 2 * q - 1) / (2 * q)
        ident_ok = ident_ok and abs(lhs - rhs) < mp.mpf("1e-55")
        u = substrate_ladder_quantities(q)["u"]
        c3 = c3_target_at(q, QCOD, ME)
        pref = departure_prefactor(q)
        dw3 = pref * c3 * u ** 3          # full u^3-order departure
        dw3_S = pref * S(q) * u ** 3      # its S-carrying (odd-channel) part
        rows[name] = {"q": q, "h": h, "u": u, "c3": c3, "S": S(q), "pref": pref,
                      "dw3": dw3, "dw3_S": dw3_S}
        print(f"    {name:7s}: (h−2)/2 = (q²−2q−1)/(2q) ✓   δw₃ = {mp.nstr(dw3, 8)}   δw₃(S-part) = {mp.nstr(dw3_S, 8)}")

    # ---- 2. handles: scale O(1), anchor-blind; S swings ----
    print("\n[2] geometric handles vs required S (per anchor, zero fit):")
    handle_stats = {}
    for hkey in ("vol_deficit", "finite_b_im"):
        vp, vm = (mp.mpf(saddle[a][hkey]) for a in ("proton", "muon"))
        spread = abs(vp - vm) / vp
        ratios = {a: rows[a]["S"] / mp.mpf(saddle[a][hkey]) for a in anchors}
        handle_stats[hkey] = {"proton": vp, "muon": vm, "rel_spread": spread, "ratios": ratios}
        print(f"    {hkey:12s}: value≈{mp.nstr(vp,6)}  rel spread(p,μ)={mp.nstr(spread,3)}")
        for a in anchors:
            print(f"        S/{hkey}({a}) = {mp.nstr(ratios[a], 6)}   (O(1) scale, sign varies)")
    s_flip = rows["proton"]["S"] * rows["muon"]["S"] < 0
    print(f"    S sign-flips between anchors: {s_flip}; handles anchor-blind to ~{mp.nstr(handle_stats['vol_deficit']['rel_spread'],3)}")
    print("    ⇒ under KC19 anchor-rigidity an anchor-blind bar-even handle yields an")
    print("      anchor-blind departure: right SCALE, structurally cannot supply the SWING.")

    # ---- 3. the named fit-free pipeline for any future bar-odd geometric object ----
    print("\n[3] fit-free test pipeline for a future bar-odd geometric S_geo(q₀):")
    print("      c₃_geo = −Vol(4₁) + S_geo;  δw₃_geo = −(h−2)/2·c₃_geo·u³;  compare to [1].")
    print("      candidates (witness scope.open / #3691): ℚ(√−3) odd channel, κ₁(u) at")
    print("      meridian u = 2·log q₀, deformed rungs κ̃₁/κ̃₃.")

    wb = WitnessBuilder("qbeta-kc19-phib-departure-bridge", engine="mpmath")
    wb.set_description(
        "Bridge probe KC19 x Phi_b: push the two anchor-blind geometric handles of the "
        "saddle witness (vol_deficit ~0.0094, finite_b t*kappa1 ~0.0578) through the exact "
        "affine crossing-weight departure w(u)-1 = -(h-2)/2 * sum c_k u^k (Lean "
        "ladder_departure; prefactor identity (h-2)/2=(q^2-2q-1)/(2q) verified to 1e-55). "
        "RESULT: |S|/handle is O(1) at both anchors (scale match, quantified per anchor) "
        "but the handles are anchor-blind (~2e-7 rel) while S sign-flips — under KC19 "
        "anchor-rigidity a bar-even anchor-blind handle cannot source the swing (scope-(a): "
        "these two handles alone, at real meridian, do not close S). Named fit-free "
        "pipeline for any future bar-odd geometric S_geo: c3_geo = -Vol(4_1)+S_geo, "
        "dw3_geo = -(h-2)/2*c3_geo*u^3, compare per anchor. Candidates: Q(sqrt-3) odd "
        "channel, kappa1(u) at meridian, deformed rungs (#3691). No c_k wired; no fit."
    )
    wb.set_content_block("conj:im-q-physical-role")
    for name in anchors:
        r = rows[name]
        wb.add_data(f"required_departure_{name}", {
            "c3": mp.nstr(r["c3"], 12), "S": mp.nstr(r["S"], 10),
            "prefactor_neg_h_minus_2_over_2": mp.nstr(r["pref"], 12),
            "u": mp.nstr(r["u"], 12), "dw3": mp.nstr(r["dw3"], 10), "dw3_S_part": mp.nstr(r["dw3_S"], 10)})
    for hkey, st in handle_stats.items():
        wb.add_data(f"handle_{hkey}", {
            "proton": mp.nstr(st["proton"], 12), "muon": mp.nstr(st["muon"], 12),
            "rel_spread": mp.nstr(st["rel_spread"], 6),
            "S_over_handle_proton": mp.nstr(st["ratios"]["proton"], 8),
            "S_over_handle_muon": mp.nstr(st["ratios"]["muon"], 8)})
    wb.add_data("verdict", {
        "scale": "both handles O(1) vs |S| at both anchors (capstone scale-match, quantified)",
        "swing": "handles anchor-blind + KC19 kernel anchor-rigid => cannot source the S "
                 "sign-flip; scope-(a) — a bar-odd geometric source at the meridian is required",
        "pipeline": "any bar-odd S_geo(q0) maps to c3_geo=-Vol(4_1)+S_geo and "
                    "dw3_geo=-(h-2)/2*c3_geo*u^3 with zero free parameters"})
    wb.add_assertion("ladder_departure_prefactor_identity",
                     computed=1.0 if ident_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="(h-2)/2 == (q^2-2q-1)/(2q) at both anchors to 1e-55 (Lean departure_factor_eq)")
    wb.add_assertion("anchors_reproduced_vs_saddle_witness",
                     computed=1.0 if repro else 0.0, expected=1.0, tolerance=0.5,
                     source="S(anchor) from c3_target_at matches the committed saddle witness S_target to 1e-6")
    wb.add_assertion("handles_anchor_blind_S_sign_flips",
                     computed=1.0 if (s_flip and float(handle_stats["vol_deficit"]["rel_spread"]) < 1e-5) else 0.0,
                     expected=1.0, tolerance=0.5,
                     source="vol_deficit rel spread < 1e-5 across anchors while S(p)*S(mu) < 0: "
                            "even anchor-blind handles cannot source the swing through the anchor-rigid affine bridge")
    wb.save()
    print("\n  RESULT: bridge exact; handles = scale only; swing needs a bar-odd meridian object.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
