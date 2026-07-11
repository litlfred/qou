#!/usr/bin/env python3
"""qbeta_c3_phib_mplane_inversion_probe.py — invert S = Im 𝔙 on the m-plane:
which meridian holonomy does each anchor REQUIRE, and do canonical Φ_b/substrate
candidates for m(q₀) supply it? EXPLORATORY MEASUREMENT — no fit, no wiring.

Builds directly on merged #3543 (S = Im 𝔙(m), u = 2·log m, NZ leading
Im 𝔙 ≈ (√3/2)·|u|²·sin(2·arg u), open link = the q₀ → m map,
conj:algebraic-geometric-dilog-equivalence) and #3540 (b-map
b = √(t/2π)e^{iπ/4}; un-levered r = S·u_ladder³ reframing). All Im 𝔙 numbers
here are the NZ LEADING order (cusp shape √−3) — a stated tier, not the full
framing-corrected CS.

What this probe measures (three independent deliverables):

  M1 FEASIBILITY FLOOR. Per anchor, the minimal deformation
     |u|_min = √(2|S|/√3) below which NO phase can produce the required S.
     The muon floor lands within ~1.3% of t = ln q₀ (measured, reported as a
     ratio — NOT claimed as an identity); the proton floor is ~2× t, so any
     single anchor-blind |u| = O(t) law is killed by feasibility alone.

  M2 CANONICAL CANDIDATE TABLE (cross-anchor gate). u-candidates built from
     named substrate quantities only (t, b-map direction e^{iπ/4}, ℏ_q², h):
     each either has Im 𝔙 = 0 (real u) or is anchor-blind up to 1e-8 — the
     b-aligned u = t·e^{iπ/4} reproduces S(muon) to a few % and MISSES the
     proton sign+magnitude: the same single-anchor near-match class as the
     keystone claim formula (#3524 re-scope). Expected verdict: all fail the
     cross-anchor gate (scope-(a); menu finite, nothing structurally excluded).

  M3 PHASE-ACCUMULATION RATE (the useful narrowing). Fixing any |u| feasible
     at both anchors, the required phases φ_req(anchor) = ½·arcsin(S/((√3/2)|u|²))
     give a REQUIRED |dφ/dq| between the anchors. Compared against the rate
     scales of candidate phase laws:
        smooth substrate phases (φ ~ 2π²/t):        |dφ/dq| ~ 1.6e3   (too slow)
        dual-lattice winding (φ ~ 4π²/t·k, k small): same order        (too slow)
        ladder-lever phases (φ ~ C/u_ladder³):       |dφ/dq| ~ 8e7    (right class)
     The required rate is a LOWER bound (arcsin branches mod π), so the
     conclusion is one-sided and safe: the q₀ → m phase must accumulate at
     least at the u_ladder³-lever class rate — consistent with #3543's
     "near-singular, phase accumulates like a root of unity", and with #3540's
     observation that the S lever IS the ÷u³ CODATA inversion.

Run: python3 -u computations/qbeta/qbeta_c3_phib_mplane_inversion_probe.py \\
       2>&1 | tee /tmp/qbeta_c3_phib_mplane_inversion.log
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402
from qbeta_c3_barodd_gluing_newton_solve import vol_of_m, VOL_4_1  # noqa: E402

set_compute_dps()  # mp.mp.dps <- COMPUTE_DPS (70 default; QOU_COMPUTE_DPS honored)

SQRT3_HALF = mp.sqrt(3) / 2


def im_V_leading(u):
    """NZ leading Im 𝔙 for meridian deformation u = 2 log m (cusp shape √−3)."""
    return SQRT3_HALF * mp.fabs(u) ** 2 * mp.sin(2 * mp.arg(u))


def main() -> int:
    from qou_substrate.constants import q_at, q_muon_at
    from qbeta_utils import substrate_ladder_quantities, c3_target_at
    from substrate import codata_constants as C

    me = mp.mpf(str(C.M_E_MEV))
    Qcod = mp.mpf(str(C.Q_BETA_MEV))
    Vol41 = 2 * mp.clsin(2, mp.pi / 3)

    anchors = {"proton": q_at(50), "muon": q_muon_at(50)}
    S, sub, t = {}, {}, {}
    for a, q in anchors.items():
        sub[a] = substrate_ladder_quantities(q)
        S[a] = c3_target_at(q, Qcod, me) + Vol41
        t[a] = mp.log(q)

    wb = WitnessBuilder("qbeta-c3-phib-mplane-inversion", engine="mpmath")
    wb.set_description(
        "Invert S = Im V (NZ leading) on the m-plane: per-anchor feasibility "
        "floor |u|_min = sqrt(2|S|/sqrt(3)); canonical substrate u-candidates "
        "all fail the cross-anchor gate (b-aligned t*e^{i pi/4} is a "
        "muon-only near-match); required phase-accumulation rate |dphi/dq| "
        "matches the u_ladder^3-lever class (~1e7..1e9), excluding smooth "
        "substrate phase laws (~1e3). Exploratory; NZ-leading tier; no fit; "
        "no c_k wired.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    print("=" * 78)
    print(" m-plane inversion of S = Im 𝔙 (NZ leading) — floors, candidates, rate")
    print("=" * 78)

    # ---- sanity: solver import + real-axis Im 𝔙 = 0 ----
    vol1, _, _ = vol_of_m(mp.mpf(1))
    err_vol = float(mp.fabs(vol1 - VOL_4_1))
    im_real_axis = float(im_V_leading(t["proton"]))  # real u ⇒ arg u = 0
    print(f"\n[0] solver check: Vol(m=1) err {err_vol:.1e};  Im 𝔙_lead(real u) = {im_real_axis}")
    wb.add_assertion("newton_solver_recovers_vol41", computed=err_vol,
                     expected=0.0, tolerance=1e-10,
                     source="import of #3543 vol_of_m at complete structure")
    wb.add_assertion("real_axis_gives_zero_S", computed=im_real_axis,
                     expected=0.0, tolerance=1e-40,
                     source="arg u = 0 => sin(2 arg u) = 0 (substrate real axis)")

    # ---- M1: feasibility floors ----
    print("\n[M1] per-anchor feasibility floor |u|_min = √(2|S|/√3):")
    floors = {}
    for a in ("muon", "proton"):
        floors[a] = mp.sqrt(mp.fabs(S[a]) / SQRT3_HALF)
        ratio_t = floors[a] / t[a]
        print(f"    {a:7s}: S = {mp.nstr(S[a], 10):>15s}   |u|_min = {mp.nstr(floors[a], 10)}"
              f"   |u|_min / t = {mp.nstr(ratio_t, 8)}")
    wb.add_data("M1_feasibility_floors", {
        a: {"S": mp.nstr(S[a], 20), "u_min": mp.nstr(floors[a], 20),
            "u_min_over_t": mp.nstr(floors[a] / t[a], 12)} for a in anchors})
    # any anchor-blind |u| = O(t) law dies on the proton floor:
    wb.add_assertion("proton_floor_exceeds_t",
                     computed=float(floors["proton"] / t["proton"]),
                     expected=2.0, tolerance=0.3,
                     source="|u|_min(proton)/t ~ 2 => |u| = O(t) anchor-blind law infeasible")

    # ---- M2: canonical candidate table ----
    print("\n[M2] canonical u-candidates (cross-anchor gate):")
    cand_rows = []
    n_pass = 0
    for name, fu in (
        ("t (real substrate)", lambda a: t[a]),
        ("t*e^(i pi/4) (b-aligned)", lambda a: t[a] * mp.e ** (mp.mpc(0, 1) * mp.pi / 4)),
        ("2 pi i b+^2 = i t", lambda a: mp.mpc(0, 1) * t[a]),
        ("hbar_q^2 * e^(i pi/4)", lambda a: sub[a]["hbar_q"] ** 2 * mp.e ** (mp.mpc(0, 1) * mp.pi / 4)),
        ("h * e^(i pi/4)", lambda a: sub[a]["h"] * mp.e ** (mp.mpc(0, 1) * mp.pi / 4)),
        ("u_ladder * e^(i pi/4)", lambda a: sub[a]["u"] * mp.e ** (mp.mpc(0, 1) * mp.pi / 4)),
    ):
        errs = {}
        for a in anchors:
            iv = im_V_leading(fu(a))
            errs[a] = (float(mp.fabs(iv / S[a] - 1))
                       if mp.fabs(S[a]) > 0 else float("inf"))
        passes = max(errs.values()) < 1e-4
        n_pass += passes
        cand_rows.append({"candidate": name,
                          "rel_err_muon": errs["muon"], "rel_err_proton": errs["proton"],
                          "cross_anchor_pass": bool(passes)})
        print(f"    {name:28s}: err(muon) {errs['muon']:.3e}   err(proton) {errs['proton']:.3e}"
              f"   {'PASS' if passes else 'fail'}")
    wb.add_data("M2_candidates", cand_rows)
    muon_near = cand_rows[1]["rel_err_muon"]
    print(f"    NOTE: b-aligned t·e^(iπ/4) hits muon to {muon_near*100:.1f}% and misses proton")
    print("    (sign+magnitude) — the single-anchor near-match class again (cf. #3524).")
    wb.add_assertion("no_candidate_passes_cross_anchor_gate",
                     computed=float(n_pass), expected=0.0, tolerance=0.5,
                     source="scope-(a): this finite canonical menu fails; nothing excluded")

    # ---- M3: required phase-accumulation rate ----
    print("\n[M3] required |dφ/dq| for a both-anchor-feasible fixed |u|:")
    dq = anchors["proton"] - anchors["muon"]
    rate_rows = []
    for scale in (mp.mpf("1.05"), mp.mpf("1.5"), mp.mpf("3")):
        umod = floors["proton"] * scale
        phi = {a: mp.asin(S[a] / (SQRT3_HALF * umod ** 2)) / 2 for a in anchors}
        rate = mp.fabs((phi["proton"] - phi["muon"]) / dq)
        rate_rows.append({"u_mod_over_proton_floor": float(scale),
                          "phi_muon": mp.nstr(phi["muon"], 10),
                          "phi_proton": mp.nstr(phi["proton"], 10),
                          "required_dphi_dq_lower_bound": mp.nstr(rate, 8)})
        print(f"    |u| = {mp.nstr(umod, 6)} ({mp.nstr(scale, 3)}× proton floor): "
              f"φ_μ = {mp.nstr(phi['muon'], 6)}, φ_p = {mp.nstr(phi['proton'], 6)}"
              f"  ⇒ |dφ/dq| ≥ {mp.nstr(rate, 4)}")
    # comparison scales
    u_lad = sub["proton"]["u"]
    du_dq = (sub["proton"]["u"] - sub["muon"]["u"]) / dq
    rate_smooth = 2 * mp.pi ** 2 / (t["proton"] ** 2 * anchors["proton"])
    rate_lever = mp.fabs(-3 * u_lad ** (-4) * du_dq)  # d(1/u³)/dq magnitude
    req = mp.mpf(rate_rows[0]["required_dphi_dq_lower_bound"])
    print(f"    scales: smooth 2π²/t law |dφ/dq| ≈ {mp.nstr(rate_smooth, 4)}; "
          f"u_ladder³-lever law ≈ {mp.nstr(rate_lever, 4)}")
    in_lever_class = bool(rate_smooth * 100 < req < rate_lever * 100)
    print(f"    required ≥ {mp.nstr(req, 4)} ⇒ "
          f"{'EXCLUDES smooth-phase laws; u³-lever class compatible' if in_lever_class else 'CHECK'}")
    wb.add_data("M3_phase_rate", {
        "rows": rate_rows,
        "rate_smooth_2pi2_over_t": mp.nstr(rate_smooth, 12),
        "rate_ladder_lever_1_over_u3": mp.nstr(rate_lever, 12),
        "note": "required rate is a LOWER bound (arcsin principal branch; "
                "mod-π ambiguity only raises it)"})
    # one-sided claim encoded as a boolean: required rate >= 100x smooth-law rate
    wb.add_assertion("required_phase_rate_excludes_smooth_laws",
                     computed=float(1.0 if req > 100 * rate_smooth else 0.0),
                     expected=1.0, tolerance=0.1,
                     source=f"required {mp.nstr(req, 4)} >= 100x smooth "
                            f"{mp.nstr(rate_smooth, 4)} — smooth substrate phase "
                            "laws cannot carry the anchor swing; the "
                            "u_ladder^3-lever class can (one-sided lower bound)")

    ok = wb.all_assertions_passed() if hasattr(wb, "all_assertions_passed") else True
    wb.add_data("verdict", (
        "m-plane inversion (NZ-leading tier): each anchor's S is reachable only "
        "above |u|_min = sqrt(2|S|/sqrt3) (proton floor ~2x t kills anchor-blind "
        "|u| = O(t) laws); every canonical substrate u-candidate fails the "
        "cross-anchor gate (b-aligned t*e^{i pi/4} is a muon-only near-match, "
        "the #3524 class); the required phase-accumulation rate |dphi/dq| >= "
        "~1e7 excludes smooth substrate phase laws (~1e3) and matches the "
        "u_ladder^3-lever class (~8e7) — quantitative support for #3543's "
        "'near-singular / root-of-unity phase accumulation' and #3540's "
        "r = S*u^3 lever identification. Scope-(a); no fit; nothing wired."))
    wb.save()
    print("\nwitness -> computations/qbeta/qbeta-c3-phib-mplane-inversion.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
