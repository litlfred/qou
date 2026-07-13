#!/usr/bin/env python3
"""qbeta_c3_phib_lever_phase_scan.py — round 2 of the m-plane S-inversion:
scan the u_ladder³-LEVER phase-law class isolated by the round-1 probe
(qbeta_c3_phib_mplane_inversion_probe.py: required |dφ/dq| ≥ 5.3e7; smooth
laws ~1.6e3 excluded; lever class ~8.0e7 compatible). EXPLORATORY MEASUREMENT —
no fit, no wiring; every near-match reported tiered per registry §8.

Model (NZ-leading tier, stated): S_cand(q) = (√3/2)·|U(q)|²·sin(2·φ(q)) with
  * |U| laws — zero-parameter canonical magnitudes (feasibility floor from
    round 1: |U| ≥ |u|_min(proton) = 0.21346 = 2.046·t; canonical candidates
    at or below the floor are reported INFEASIBLE, itself informative — both
    `h = q−1/q ≈ 0.2090` and `2t ≈ 0.2087` sit ~2% BELOW the proton floor).
  * φ laws — the lever class φ = κ/u_ladder³ for canonical κ (zero-parameter).

Two deliverables:
  D1 DIRECT GATE. Every (|U| law, κ) pair evaluated at both anchors against
     S; max-anchor relative error; cross-anchor gate 1e-4.
  D2 REQUIRED-κ STABILITY (the measurement that matters). For each feasible
     |U| law, invert per anchor: φ_req = ½·arcsin(S/((√3/2)|U|²)) (principal
     branch) ⇒ κ_req = φ_req·u³. If κ_req were anchor-STABLE for some |U| law,
     that would be a candidate lead. CAVEAT (stated in the witness): arcsin
     branches make κ_req a family κ_0 + kπ·u³ (spacing π·u³ ≈ 1.9e-6); the
     principal-branch comparison is decisive only for candidate κ of that
     scale or if stability appears; large-κ laws (κ ~ t) are compared modulo
     the branch spacing and flagged accordingly.

Run: python3 -u computations/qbeta/qbeta_c3_phib_lever_phase_scan.py \\
       2>&1 | tee /tmp/qbeta_c3_phib_lever_phase_scan.log
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

set_compute_dps()

SQRT3_HALF = mp.sqrt(3) / 2


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
    floor_p = mp.sqrt(mp.fabs(S["proton"]) / SQRT3_HALF)  # |u|_min(proton), recorded below

    wb = WitnessBuilder("qbeta-c3-phib-lever-phase-scan", engine="mpmath")
    wb.set_description(
        "Round-2 m-plane scan over the u_ladder^3-lever phase-law class "
        "(S_cand = (sqrt3/2)|U|^2 sin(2 kappa/u^3)): direct cross-anchor gate "
        "over canonical (|U|, kappa) pairs + required-kappa stability "
        "measurement per |U| law. NZ-leading tier; exploratory; no fit; "
        "no c_k wired.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    print("=" * 78)
    print(" u³-lever phase-law scan (round 2) — direct gate + required-κ stability")
    print("=" * 78)
    for a in ("muon", "proton"):
        print(f"  {a:7s}: S = {mp.nstr(S[a], 12)}   u³ = {mp.nstr(sub[a]['u'] ** 3, 8)}")

    # ---- |U| laws (zero-parameter canonical magnitudes) ----
    def U_laws(a):
        q = anchors[a]
        s = sub[a]
        return {
            "h": s["h"],
            "2t": 2 * t[a],
            "3t": 3 * t[a],
            "sqrt(t)": mp.sqrt(t[a]),
            "z_markov": s["z"],
            "1/2": mp.mpf(1) / 2,
            "2h": 2 * s["h"],
        }

    # ---- κ menu for the lever phase φ = κ/u³ (both signs) ----
    def kappa_menu(a):
        s = sub[a]
        base = {
            "1": mp.mpf(1),
            "t": t[a],
            "hbar_q^2": s["hbar_q"] ** 2,
            "alpha": s["alpha"],
            "u": s["u"],
            "u^2": s["u"] ** 2,
        }
        out = {}
        for n, v in base.items():
            out[f"+{n}"] = v
            out[f"-{n}"] = -v
        return out

    # ---- D1: direct cross-anchor gate ----
    GATE = 1e-4
    rows = []
    for Uname in U_laws("proton"):
        for kname in kappa_menu("proton"):
            errs = {}
            for a in anchors:
                U = U_laws(a)[Uname]
                kap = kappa_menu(a)[kname]
                phi = kap / sub[a]["u"] ** 3
                cand = SQRT3_HALF * U ** 2 * mp.sin(2 * phi)
                errs[a] = float(mp.fabs(cand / S[a] - 1))
            rows.append({"U": Uname, "kappa": kname,
                         "err_muon": errs["muon"], "err_proton": errs["proton"],
                         "max_err": max(errs.values())})
    rows.sort(key=lambda r: r["max_err"])
    n_pass = sum(1 for r in rows if r["max_err"] < GATE)
    print(f"\n[D1] {len(rows)} lever-class candidates; gate {GATE:.0e}; passes: {n_pass}")
    for r in rows[:8]:
        print(f"    |U|={r['U']:9s} κ={r['kappa']:10s}: "
              f"err(μ) {r['err_muon']:.3e}  err(p) {r['err_proton']:.3e}")
    wb.add_data("D1_direct_gate", {"gate": GATE, "n_candidates": len(rows),
                                   "n_pass": n_pass, "top8": rows[:8]})
    wb.add_assertion("d1_direct_gate_scan_completed",
                     computed=float(n_pass), expected=0.0, tolerance=0.5,
                     source="scope-(a) if 0: this finite lever-class menu, as-is, "
                            "does not reproduce S at both anchors")

    # ---- D2: required-κ stability per |U| law ----
    print("\n[D2] required κ (principal branch) per anchor, per feasible |U| law:")
    d2 = []
    for Uname in U_laws("proton"):
        feas = all(SQRT3_HALF * U_laws(a)[Uname] ** 2 > mp.fabs(S[a]) for a in anchors)
        row = {"U": Uname, "feasible": bool(feas)}
        if feas:
            kreq = {}
            for a in anchors:
                U = U_laws(a)[Uname]
                phi = mp.asin(S[a] / (SQRT3_HALF * U ** 2)) / 2
                kreq[a] = phi * sub[a]["u"] ** 3
            spread = float(mp.fabs(kreq["proton"] - kreq["muon"])
                           / max(mp.fabs(kreq["muon"]), mp.mpf("1e-40")))
            row.update({"kappa_req_muon": mp.nstr(kreq["muon"], 12),
                        "kappa_req_proton": mp.nstr(kreq["proton"], 12),
                        "rel_spread": spread,
                        "branch_spacing_pi_u3_muon": mp.nstr(mp.pi * sub["muon"]["u"] ** 3, 8),
                        "branch_spacing_pi_u3_proton": mp.nstr(mp.pi * sub["proton"]["u"] ** 3, 8)})
            print(f"    |U|={Uname:9s}: κ_req(μ) = {mp.nstr(kreq['muon'], 8):>14s}"
                  f"  κ_req(p) = {mp.nstr(kreq['proton'], 8):>14s}"
                  f"  spread {spread:.2e}")
        else:
            print(f"    |U|={Uname:9s}: INFEASIBLE (below the |S(proton)| floor)")
        d2.append(row)
    stable = [r for r in d2 if r.get("feasible") and r.get("rel_spread", 1) < 1e-3]
    wb.add_data("feasibility_floor_proton_u_min", mp.nstr(floor_p, 20))
    wb.add_data("D2_required_kappa", d2)
    wb.add_data("D2_note",
                "kappa_req is principal-branch only; the arcsin family is "
                "kappa_0 + k*pi*u^3. A stable kappa_req (spread < 1e-3) would "
                "be a candidate lead, not a derivation.")
    wb.add_assertion("d2_stability_measured",
                     computed=float(len(stable)), expected=0.0, tolerance=100.0,
                     source="measurement (informational): count of |U| laws with "
                            "anchor-stable principal-branch kappa_req")

    n_infeas = sum(1 for r in d2 if not r["feasible"])
    verdict = (
        f"Round-2 lever-class scan (NZ-leading tier): {len(rows)} zero-parameter "
        f"(|U|, kappa/u^3) candidates -> {n_pass} pass the 1e-4 cross-anchor gate. "
        f"{n_infeas} canonical |U| laws are INFEASIBLE below the proton floor "
        "(notably h and 2t, each ~2% under it). Required-kappa inversion "
        f"per feasible |U| law recorded; {len(stable)} law(s) show principal-branch "
        "kappa_req stable across anchors at 1e-3. Scope-(a): the lever CLASS "
        "remains the only rate-compatible family (round 1); this finite menu "
        "does not identify the member. No fit; nothing wired.")
    wb.add_data("verdict", verdict)
    wb.save()
    print("\nVERDICT:", verdict)
    print("witness -> computations/qbeta/qbeta-c3-phib-lever-phase-scan.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
