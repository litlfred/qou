#!/usr/bin/env python3
"""qbeta_c3_geometric_channel_q0star_probe.py — direction 2: does the leading geometric
channel identity S = Im 𝔙₄₁(u(q₀)) reproduce the smooth target? Honest null + a
direction-4 confirmation.

The well-posed target (after the #4509 reframe): reproduce the SMOOTH object
S = c₃ + Vol(4₁) = Im 𝔙₄₁(u(q₀)) geometrically, rather than the 1/u³-amplified
|S_p/S_m| ratio. The leading geometric prediction (Re u = ln q₀ boost, Im u = 0) is
`geom(q) = (√3/4)(ln q₀)²`. Test it against the ladder S(q) at/near the canonical
anchors.

Findings (honest):
  - `geom(q)` is essentially FLAT across the muon/proton anchor gap: it changes by
    ~1e-9 while the ladder S(q) sweeps ~0.049 (the 1/u³ amplification, #4509). This is
    a clean CONFIRMATION of the direction-4 picture: the geometric object is smooth; the
    apparent S hypersensitivity is the extraction artifact.
  - The leading identity is NOT satisfied at EITHER canonical pin: geom ≈ 0.004714 is
    ~2.05× below S(muon)=0.009683 (the known A≈2.05 boost-enhancement / spin-part gap)
    and has the wrong sign vs S(proton)=−0.039459. So the smooth target is NOT
    reproduced by the leading form + pure ln q₀ boost; the 2.05× gap persists.
  - There IS a q₀* in the gap where S(q*)=geom(q*) — but this is IVT-TRIVIAL: the steep
    amplified S curve must cross the flat geometric line once. It is NOT independent
    evidence for the identity; we record q₀* only as a datum (it sits ~90% of the way
    from the proton to the muon pin).

Net: the well-posed geometric target still faces the A≈2.05 boost-enhancement / spin-
part gap at the canonical anchor (open, qou-iyj5). The q* crossing confirms the
amplification picture, not a closure. No fit; nothing wired.
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
VOL41 = +(2 * mp.clsin(2, mp.pi / 3))
K = mp.sqrt(3) / 4


def S(q):
    return c3_target_at(q, QCOD, ME) + VOL41


def geom(q):
    return K * mp.log(q) ** 2          # leading Im 𝔙₄₁ at Re u=ln q, Im u=0


def main() -> int:
    print("=" * 78)
    print(" dir2: leading geometric channel identity S = Im 𝔙₄₁(ln q₀) vs the smooth target")
    print("=" * 78)
    q_pr, q_mu = q_at(50), q_muon_at(50)
    lo, hi = (q_pr, q_mu) if q_pr < q_mu else (q_mu, q_pr)

    S_mu, S_pr = S(q_mu), S(q_pr)
    g_mu, g_pr = geom(q_mu), geom(q_pr)
    print(f"\n muon  : S={mp.nstr(S_mu,8)}  geom={mp.nstr(g_mu,10)}  S/geom={mp.nstr(S_mu/g_mu,5)}")
    print(f" proton: S={mp.nstr(S_pr,8)}  geom={mp.nstr(g_pr,10)}  (opposite sign)")

    # geom flat vs S steep across the gap
    dgeom = abs(g_mu - g_pr)
    dS = abs(S_mu - S_pr)
    print(f"\n across the anchor gap: Δgeom = {mp.nstr(dgeom,4)} (FLAT)   ΔS = {mp.nstr(dS,4)} "
          f"(STEEP, 1/u³-amplified)   ratio ΔS/Δgeom = {mp.nstr(dS/dgeom,5)}")
    geom_flat = dgeom < mp.mpf("1e-8")
    S_steep = dS > mp.mpf("1e-2")

    # leading identity fails at canonical pins: 2.05x undershoot at muon, wrong sign at proton
    muon_undershoot = S_mu / g_mu       # ≈ 2.05
    identity_fails_at_pins = bool(muon_undershoot > mp.mpf("1.5") and S_pr < 0 < g_pr)
    print(f"\n leading identity at canonical pins: S(muon)/geom = {mp.nstr(muon_undershoot,5)} "
          f"(≈2.05, the boost-enhancement gap); S(proton)<0<geom (wrong sign).")
    print("   ⇒ NOT satisfied at either pin — the A≈2.05 spin/boost gap persists (open).")

    # IVT-trivial crossing q*
    qstar = mp.findroot(lambda q: S(q) - geom(q), (lo + hi) / 2)
    frac = (qstar - lo) / (hi - lo)
    print(f"\n q₀* (S=geom, IVT crossing in the gap) = {mp.nstr(qstar,16)}")
    print(f"   = {mp.nstr(frac,5)} of the way proton→muon;  S(q*)=geom(q*)={mp.nstr(geom(qstar),8)}")
    print("   NOTE: existence is IVT-trivial (steep S must cross flat geom once); NOT evidence.")

    ok = bool(geom_flat and S_steep and identity_fails_at_pins)

    wb = WitnessBuilder("qbeta-c3-geometric-channel-q0star", engine="mpmath")
    wb.set_description(
        "Direction 2 (reproduce the smooth target geometrically). Honest null + direction-4 "
        "confirmation. The leading geometric channel identity geom(q)=(√3/4)(ln q₀)² is FLAT "
        "across the muon/proton gap (Δgeom~1e-9) while the ladder S sweeps ~0.049 (1/u³-"
        "amplified) — confirming the #4509 picture (smooth geometry, extraction-artifact S "
        "hypersensitivity). The identity is NOT satisfied at either canonical pin: geom≈0.00471 "
        "is ~2.05× below S(muon)=0.00968 (the boost-enhancement/spin gap) and wrong-sign vs "
        "S(proton)=−0.03946. A q₀* with S=geom exists in the gap but is IVT-trivial (steep S "
        "crosses flat geom once), recorded only as a datum (~90% proton→muon), NOT evidence. "
        "The A≈2.05 gap persists (open, qou-iyj5). No fit; nothing wired.")
    wb.set_content_block("conj:binding-qbeta-complex-volume")
    wb.add_data("channel_identity_readout", {
        "geom_leading_0470": mp.nstr(g_mu, 10),
        "S_muon": mp.nstr(S_mu, 10),
        "S_proton": mp.nstr(S_pr, 10),
        "muon_S_over_geom": mp.nstr(muon_undershoot, 8),
        "delta_geom_across_gap": mp.nstr(dgeom, 6),
        "delta_S_across_gap": mp.nstr(dS, 6),
        "geom_flat_S_steep": bool(geom_flat and S_steep),
        "identity_fails_at_both_canonical_pins": identity_fails_at_pins,
        "q0star_ivt_crossing": mp.nstr(qstar, 16),
        "q0star_is_ivt_trivial_not_evidence": True,
        "verdict": ("leading geometric identity fails at both canonical pins (2.05× gap "
                    "persists); geom flat vs S steep confirms the 1/u³ extraction picture; "
                    "q0* crossing is IVT-trivial, not evidence")})
    wb.add_assertion("geom_flat_S_steep_confirms_extraction_picture",
                     str(bool(geom_flat and S_steep)), "True")
    wb.add_assertion("leading_identity_fails_at_canonical_pins", str(identity_fails_at_pins), "True")
    wb.save()
    print("\nwitness → qbeta-c3-geometric-channel-q0star.witness.json")
    print("ALL ASSERTIONS PASS (honest null + direction-4 confirmation)" if ok
          else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
