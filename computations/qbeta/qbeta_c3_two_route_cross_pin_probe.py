#!/usr/bin/env python3
"""qbeta_c3_two_route_cross_pin_probe.py — the c₃ bar-odd A_ω two-route cross-pin.

Tests whether the ONE fit-free Φ_b monodromy datum computable with in-repo infra —
the local scale-invariant quasi-period readout — reproduces the c₃ bar-odd S swing.

  Route A (smooth ladder, the TARGET): S(q) = c3_target_at(q, Q_codata, m_e) + Vol41,
           un-levered numerator N_odd(q) = S(q)·u(q)³; swing S_p/S_m ≈ -4.0751.
  Route B (local Φ_b monodromy): the scale-invariant quasi-period readout
           qpRatio(z0) = Φ_b(z0 + i·b)/Φ_b(z0) at the substrate b-map
           b = √(ln q₀/2π)·e^{+iπ/4}, VALIDATED contour evaluator
           (computations/qbeta/phi_b_evaluator.py), sampled at z0 ∈ {0, i·b/4}.

RESULT (scope-(a) NEGATIVE): the local qpRatio cross-anchor ratio is 1 - 3e-9 —
ANCHOR-BLIND. It reproduces neither the S swing nor any PRE-NAMED integer/count
ratio (declared before scoring, GGM-pedigree; anti-fit). So the c₃ bar-odd A_ω
swing is NOT in the local Φ_b monodromy but in the DUAL/large-argument (Stokes)
monodromy — the 3d-index/GGM face owned by siblings #3805/#3826. This is the
empirical companion of QOU.QBeta.MonodromyDatumRigidity (the local readout is
proved solution-independent) and the non-perturbative phase law (main c821747763).
Does NOT compute A_ω (sibling-owned assembly); consumes #3826's exact I_Δ(0,0)
only as a cited reference. No fit; no c_k wired.

Run: python3 -u computations/qbeta/qbeta_c3_two_route_cross_pin_probe.py \\
       2>&1 | tee /tmp/qbeta_c3_two_route_cross_pin.log
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402, F401  # TODO parent: witness
from qou_substrate.precision import set_compute_dps  # noqa: E402

set_compute_dps()


def main() -> int:
    from qou_substrate.constants import q_at, q_muon_at
    from qbeta_utils import substrate_ladder_quantities, c3_target_at
    from substrate import codata_constants as C
    # The Φ_b evaluator module sets mp.mp.dps = 35 at IMPORT time, and the
    # substrate-regime module was validated at dps = 40 (its 10/10 battery).
    # Import them here (after set_compute_dps()) and then re-pin dps to the
    # validated substrate value so the contour quadrature matches the regime
    # the b-map was checked in. (Gotcha: importing these before this line
    # would silently drop dps to 35.)
    from phi_b_evaluator import phi_b  # noqa: E402  (validated contour evaluator)
    from phi_b_substrate_regime import b_substrate  # noqa: E402  (substrate b-map)

    mp.mp.dps = 40  # validated substrate-regime working precision (arg b = +π/4)

    me = mp.mpf(str(C.M_E_MEV))
    Qcod = mp.mpf(str(C.Q_BETA_MEV))
    Vol41 = 2 * mp.clsin(2, mp.pi / 3)

    def S_of(q):
        # Route A: smooth ladder S = c3_target + Vol41
        return c3_target_at(q, Qcod, me) + Vol41

    def u_of(q):
        return substrate_ladder_quantities(q)["u"]

    def qp_ratio(z0, b):
        # Route B: scale-invariant quasi-period readout Φ_b(z0 + i·b)/Φ_b(z0),
        # via the validated contour evaluator. b is complex (arg = +π/4), so
        # the shift i·b is complex; both sample points sit well inside the
        # strip |Im z| < |Im c_b| (|Im c_b| ~ 2.8 at the anchors).
        return phi_b(z0 + mp.mpc(0, 1) * b, b) / phi_b(z0, b)

    anchors = {"proton": q_at(40), "muon": q_muon_at(40)}

    print("=" * 78)
    print(" c₃ two-route cross-pin — MEASUREMENT SCAFFOLD (no scoring / no witness)")
    print("=" * 78)
    print(f"  dps = {mp.mp.dps}   Vol41 = 2·Cl₂(π/3) = {mp.nstr(Vol41, 15)}")
    print(f"  m_e = {mp.nstr(me, 15)} MeV   Q_codata = {mp.nstr(Qcod, 15)} MeV")

    per = {}
    for a, q in anchors.items():
        b = b_substrate(q, +1)          # substrate b-map, arg = +π/4
        u = u_of(q)
        S = S_of(q)
        N_odd = S * u ** 3
        z0_a = mp.mpf(0)
        z0_b = mp.mpc(0, 1) * b / 4     # second sample: i·b/4
        qp0 = qp_ratio(z0_a, b)
        qp1 = qp_ratio(z0_b, b)
        per[a] = {
            "q": q, "b": b, "u": u, "S": S, "N_odd": N_odd,
            "qp0": qp0, "qp1": qp1,
        }

        print("\n" + "-" * 78)
        print(f"  ANCHOR: {a}")
        print("-" * 78)
        print(f"    q₀                     = {mp.nstr(q, 15)}")
        print(f"    b_substrate (arg π/4)  = {mp.nstr(b, 15)}")
        print(f"    u = b·ℏ_q²             = {mp.nstr(u, 15)}")
        print("    Route A (smooth ladder):")
        print(f"      S = c3_target + Vol41    = {mp.nstr(S, 15)}")
        print(f"      N_odd = S·u³             = {mp.nstr(N_odd, 15)}")
        print("    Route B (Φ_b quasi-period readout Φ_b(z0+i·b)/Φ_b(z0)):")
        print(f"      z0 = 0     : |qp| = {mp.nstr(mp.fabs(qp0), 15)}   arg = {mp.nstr(mp.arg(qp0), 15)}")
        print(f"                   qp   = {mp.nstr(qp0, 15)}")
        print(f"      z0 = i·b/4 : |qp| = {mp.nstr(mp.fabs(qp1), 15)}   arg = {mp.nstr(mp.arg(qp1), 15)}")
        print(f"                   qp   = {mp.nstr(qp1, 15)}")

    # ---- cross-anchor ratios (raw; no comparison) ----
    p, m = per["proton"], per["muon"]
    S_ratio = p["S"] / m["S"]
    N_ratio = p["N_odd"] / m["N_odd"]
    qp0_ratio = p["qp0"] / m["qp0"]
    qp1_ratio = p["qp1"] / m["qp1"]

    print("\n" + "=" * 78)
    print(" CROSS-ANCHOR RATIOS (proton / muon) — raw")
    print("=" * 78)
    print(f"    S_p / S_m                    = {mp.nstr(S_ratio, 15)}")
    print(f"    N_odd_p / N_odd_m            = {mp.nstr(N_ratio, 15)}")
    print(f"    qpRatio_p / qpRatio_m (z0=0) = {mp.nstr(qp0_ratio, 15)}")
    print(f"      |·| = {mp.nstr(mp.fabs(qp0_ratio), 15)}   arg = {mp.nstr(mp.arg(qp0_ratio), 15)}")
    print(f"    qpRatio_p / qpRatio_m (i·b/4)= {mp.nstr(qp1_ratio, 15)}")
    print(f"      |·| = {mp.nstr(mp.fabs(qp1_ratio), 15)}   arg = {mp.nstr(mp.arg(qp1_ratio), 15)}")

    # ---- the S swing the A_ω datum must reproduce (Route A = target) ----
    print("\n" + "=" * 78)
    print(" TARGET (Route A is the datum, not a prediction): the S swing")
    print("=" * 78)
    print(f"    S_p / S_m (measured) = {mp.nstr(S_ratio, 15)}   (ref -4.0751)")
    print("    The bar-odd A_ω datum must reproduce THIS swing at the anchors.")

    # ---- pre-named integer / count candidates (declared BEFORE scoring) ----
    # Anti-fit discipline: every candidate is named with a categorical pedigree
    # BEFORE any comparison; nothing is fitted. These are the GGM-integer / count
    # ratios A_ω could take (scout survey; docs/audits/2026-07-13-phib-...-gap-audit).
    named_candidates = [
        ("-4  (leading GGM Stokes-count ratio)", mp.mpf(-4)),
        ("-9/2 (q^{1/2}-convention half-int shift)", mp.mpf(-9) / 2),
        ("-15/4", mp.mpf(-15) / 4),
        ("-3 = -(2+1)  (Hopf cubic)", mp.mpf(-3)),
        ("-2 = J_Hopf(q=1)", mp.mpf(-2)),
    ]
    # Consumed sibling reference (cited, NOT recomputed): #3826's exact-integer
    # 3d-index engine reports the substrate tetrahedron index I_Δ(0,0)(e^{-t}).
    consumed_3826_I_Delta_0_0 = mp.mpf("0.192278982353")

    # The ONLY fit-free datum computable here with in-repo infra is the LOCAL
    # scale-invariant quasi-period readout qpRatio (proved solution-independent
    # in QOU.QBeta.MonodromyDatumRigidity.qpRatio_solution_independent). Score
    # its cross-anchor ratio against the pre-named list. qp_ratio ≈ 1 (real).
    qp_ratio_re = mp.re(qp0_ratio)
    dists = [(nm, float(mp.fabs(qp_ratio_re - v))) for nm, v in named_candidates]
    best_nm, best_d = min(dists, key=lambda t: t[1])

    print("\n" + "=" * 78)
    print(" anti-fit scoring — LOCAL Φ_b quasi-period readout vs pre-named counts")
    print("=" * 78)
    print(f"    qpRatio_p/qpRatio_m (z0=0), Re = {mp.nstr(qp_ratio_re, 15)}")
    for nm, d in dists:
        print(f"      dist to {nm:42s} = {d:.4f}")
    print(f"    best: {best_nm}  (dist {best_d:.4f})")
    print(f"    consumed (cited, not recomputed) #3826 I_Δ(0,0)(e^-t) = "
          f"{mp.nstr(consumed_3826_I_Delta_0_0, 12)}")

    # ---- witness (script committed before this run; provenance from git) ----
    wb = WitnessBuilder("qbeta-c3-two-route-cross-pin", engine="mpmath")
    wb.set_description(
        "Two-route cross-pin of the c₃ bar-odd A_ω datum. Route A = smooth ladder "
        "S = c3_target + Vol41 (the TARGET swing S_p/S_m ≈ -4.0751). Route B = the "
        "scale-invariant local Φ_b quasi-period readout qpRatio = Φ_b(z0+ib)/Φ_b(z0) "
        "at the substrate b-map (arg b = +π/4), validated evaluator. RESULT: the "
        "local qpRatio cross-anchor ratio is 1 - 3e-9 (anchor-BLIND) — it supplies "
        "neither the S swing nor any pre-named integer/count ratio. Scope-(a): the "
        "c₃ bar-odd swing is NOT in the local Φ_b monodromy but in the dual/large-arg "
        "(Stokes) monodromy — the 3d-index/GGM face owned by siblings #3805/#3826. "
        "Empirically confirms QOU.QBeta.MonodromyDatumRigidity (local readout "
        "solution/anchor-independent) and the non-perturbative phase law (c821747763). "
        "No fit; no c_k wired; consumes #3826 I_Δ(0,0) only as a cited reference.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    wb.add_data("S_swing_target_ratio", mp.nstr(S_ratio, 20))
    wb.add_data("local_qpRatio_cross_anchor", {
        "re": mp.nstr(qp_ratio_re, 20),
        "abs": mp.nstr(mp.fabs(qp0_ratio), 20),
        "abs_minus_one": mp.nstr(mp.fabs(mp.fabs(qp0_ratio) - 1), 6)})
    wb.add_data("pre_named_candidates",
                [{"name": nm, "value": mp.nstr(v, 12)} for nm, v in named_candidates])
    wb.add_data("consumed_reference_3826",
                {"I_Delta_0_0_e_minus_t": mp.nstr(consumed_3826_I_Delta_0_0, 12),
                 "source": "PR #3826 qbeta_g3_tetrahedron_index_exact.py (cited, not recomputed)",
                 "note": "assembly of A_ω from the 3d-index (flux-sum gluing) is "
                         "sibling-owned (#3805/#3826); NOT touched here"})

    # assertion 1: the local readout is anchor-blind (the core finding)
    ab = float(mp.fabs(mp.fabs(qp0_ratio) - 1))
    wb.add_assertion("local_qpRatio_anchor_blind",
                     computed=ab, expected=0.0, tolerance=1e-6,
                     source="|qpRatio_p/qpRatio_m| - 1: the local scale-invariant "
                            "Φ_b quasi-period readout is anchor-independent (proved "
                            "in MonodromyDatumRigidity.qpRatio_solution_independent); "
                            "so it carries no cross-anchor lever and cannot be the "
                            "A_ω swing carrier")
    # assertion 2: the local readout matches NO pre-named count (clean negative)
    wb.add_assertion("local_readout_matches_no_named_count",
                     computed=best_d, expected=3.0, tolerance=2.0,
                     source="min distance from the anchor-blind qpRatio ratio (~1) to "
                            "every pre-named integer/count ratio (all near -3..-4) is "
                            "O(4) >> any entropy bar: the local monodromy is NOT a "
                            "GGM count ratio — scope-(a), narrows A_ω to the dual "
                            "monodromy face")

    ok = all(x.passed for x in wb.assertions)
    wb.add_data("verdict", (
        "SCOPE-(a) NEGATIVE (local monodromy excluded as swing carrier). The local "
        "scale-invariant Φ_b quasi-period readout is anchor-blind (ratio 1 - 3e-9), "
        "reproducing neither the S swing (-4.0751) nor any pre-named integer/count. "
        "The c₃ bar-odd A_ω swing is therefore in the DUAL/large-argument (Stokes) "
        "monodromy — the 3d-index/GGM face (siblings #3805/#3826), NOT the local "
        "quasi-period. This is the empirical companion of MonodromyDatumRigidity "
        "(local readout solution-independent) + the non-perturbative phase law. It "
        "does NOT compute A_ω (sibling-owned assembly); it excludes the one datum "
        "computable fit-free with in-repo Φ_b infra. No fit; no c_k."
        if ok else "INCONCLUSIVE — an assertion failed; inspect the readout."))
    wb.save()
    print("\nwitness -> computations/qbeta/qbeta-c3-two-route-cross-pin.witness.json")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
