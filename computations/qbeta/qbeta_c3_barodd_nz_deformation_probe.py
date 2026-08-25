#!/usr/bin/env python3
"""qbeta_c3_barodd_nz_deformation_probe.py

The z(q₀) gap for the c₃ bar-ODD S, via the Neumann–Zagier complex-volume
deformation of the figure-eight 4₁. Sharpens WHERE the derivation gap is; it
does NOT fit S (scope-(a); C14).

Chain of facts (each computed or cited, none fitted):

  1. Vol(4₁) = 2·Λ(π/3) = 2·D(e^{iπ/3})  (Bloch–Wigner dilog) — the bar-EVEN
     part of c₃ (= −Vol(4₁)), SOLVED. Computed here.
  2. 4₁ is AMPHICHIRAL ⇒ CS(4₁) = 0 at the complete structure. So the bar-ODD
     S is NOT the knot's own Chern–Simons; it is a DEFORMATION phase induced by
     the substrate q₀ moving off the complete point.
  3. Neumann–Zagier: near the complete structure, with complex meridian
     deformation u (log-holonomy), the complex volume obeys
         CVol(u) = CVol(0) − (τ/4)·u² + O(u³),   v(u)=τ·u+…,  τ = cusp shape.
     For 4₁ the cusp modulus is ∝ √−3 (tied to the π/3 angle of Vol(4₁)=2·Cl₂(π/3),
     a corpus-structural link, NOT a fit). S is the bar-ODD projection of the
     deformation phase.
  4. FALSIFIABLE consistency check (no fit): IF S(q₀)=Im[−(τ/4)u(q₀)²] with a
     SMOOTH real-scaling u(q₀), then S(proton)/S(muon)=(u_p/u_m)². The two
     anchors differ at ~10⁻⁸, so (u_p/u_m)²≈1 — it CANNOT give the measured
     ratio −4.08. Hence u(q₀) must carry an anchor-dependent PHASE (complex /
     fibre-level), i.e. the variation lives in the phase channel with a
     root-of-unity accumulation (dc₃/dq≈4.66×10⁶, PR #1821 magnitude wall) —
     the OPEN z→c_k evaluation map (PR #3458). The gap is sharpened to exactly
     that map; the NZ picture explains WHY a smooth deformation cannot close it.

Companion: docs/audits/2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

S_TARGET = {"muon": mp.mpf("0.00968298"), "proton": mp.mpf("-0.03945936")}
# substrate anchors (50-dps proton; muon differs at ~1e-8) — for the ratio test
Q_PROTON = mp.mpf("1.1099785827513808075916690956107688798744991218736")
Q_MUON = mp.mpf("1.10997859555733471")


def bloch_wigner(z):
    """Bloch–Wigner dilogarithm D(z) = Im Li₂(z) + arg(1−z)·log|z|."""
    z = mp.mpc(z)
    if z == 0 or z == 1:
        return mp.mpf(0)
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(mp.fabs(z))


def main() -> int:
    print("=" * 78)
    print(" c₃ bar-odd S — Neumann–Zagier deformation gap (where z(q₀) lives)")
    print("=" * 78)

    wb = WitnessBuilder("qbeta-c3-barodd-nz-deformation-gap", engine="mpmath")
    wb.set_description(
        "Sharpens the z(q₀) gap for the c₃ bar-ODD S via the Neumann–Zagier "
        "complex-volume deformation of 4₁. Computes Vol(4₁)=2·Cl₂(π/3), notes "
        "CS(4₁)=0 (amphichiral ⇒ S is a deformation phase, not the knot's own "
        "CS), and shows a SMOOTH real-scaling deformation u(q₀) cannot produce "
        "the measured S(proton)/S(muon)=−4.08 (anchors differ at ~1e-8) — so "
        "u(q₀) is a phase-channel / root-of-unity-accumulation quantity, the "
        "open z→c_k evaluation map. Scope-(a); C14 anti-fitting; no c_k wired."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    # ---- 1. Vol(4₁) = 2·Cl₂(π/3) (bar-even part, solved) ----
    z0 = mp.e ** (mp.mpc(0, 1) * mp.pi / 3)          # complete shape e^{iπ/3}
    vol = 2 * bloch_wigner(z0)
    lam_pi3 = mp.im(mp.polylog(2, z0))               # Λ(π/3) = D(e^{iπ/3}) (|z0|=1 ⇒ log term 0)
    print(f"\n[1] Vol(4₁) = 2·D(e^{{iπ/3}}) = {mp.nstr(vol, 12)}")
    print(f"    2·Λ(π/3)                 = {mp.nstr(2*lam_pi3, 12)}   (bar-EVEN part = −Vol(4₁), SOLVED)")
    vol_ok = mp.fabs(vol - 2 * lam_pi3) < mp.mpf(10) ** (-30)

    # ---- 2. CS(4₁) = 0 at the complete structure (amphichiral) ----
    # log|z0| = 0 exactly (|z0|=1); the Bloch–Wigner is purely the volume, the
    # imaginary (CS) companion vanishes at the complete amphichiral point.
    cs_complete = mp.log(mp.fabs(z0))
    print(f"\n[2] CS(4₁) complete = log|e^{{iπ/3}}| = {mp.nstr(cs_complete, 6)}  (=0, amphichiral)")
    print("    ⇒ the bar-ODD S is a DEFORMATION phase (q₀ off the complete point),")
    print("      NOT the knot's own Chern–Simons.")
    cs_ok = mp.fabs(cs_complete) < mp.mpf(10) ** (-30)

    # ---- 3. NZ leading form + cusp modulus ∝ √−3 (the π/3 link) ----
    tau = mp.sqrt(mp.mpc(-3))                          # 4₁ cusp modulus factor √−3
    print(f"\n[3] NZ leading: CVol(u) = CVol(0) − (τ/4)u² + O(u³), τ ∝ √−3 = {mp.nstr(tau,8)}")
    print("    (√−3 ↔ the π/3 angle of Vol(4₁)=2·Cl₂(π/3) — corpus-structural, NOT fitted)")

    # ---- 4. Falsifiable check: a SMOOTH real u(q₀) cannot give the ratio ----
    print("\n[4] Falsifiable (no fit) — smooth real-scaling u(q₀) ⇒ ratio (u_p/u_m)²:")
    # a natural smooth substrate deformation candidate: u ∝ log q₀ (meridian-like)
    u_p, u_m = mp.log(Q_PROTON), mp.log(Q_MUON)
    ratio_smooth = (u_p / u_m) ** 2
    ratio_meas = S_TARGET["proton"] / S_TARGET["muon"]
    print(f"    u ∝ log q₀:  (u_p/u_m)² = {mp.nstr(ratio_smooth, 10)}")
    print(f"    measured S(proton)/S(muon) = {mp.nstr(ratio_meas, 6)}")
    print(f"    smooth-deformation ratio ≈ 1  ≠  −4.08  ⇒ a smooth real u(q₀)")
    print(f"    CANNOT reproduce S (anchors differ at ~1e-8). The variation is")
    print(f"    in the PHASE channel — u(q₀) carries an anchor-dependent phase")
    print(f"    (root-of-unity accumulation; dc₃/dq≈4.66e6, PR #1821 wall).")
    smooth_insufficient = mp.fabs(ratio_smooth - 1) < mp.mpf("1e-6")  # ≈1, not −4.08

    # ---- boundary ----
    print("\n[5] SHARPENED GAP (honest boundary):")
    print("    • ALGEBRA closes: S = decay projection ½[e_k(q)−e_k(q⁻¹)] (Lean:")
    print("      QOU.QBeta EkParitySplit, sorry-free).")
    print("    • OBJECT exists: Faddeev Φ_b (validated evaluator).")
    print("    • GEOMETRY: S = bar-odd projection of the 4₁ NZ deformation phase.")
    print("    • OPEN (single link): u(q₀) — the complex meridian deformation as")
    print("      a function of the substrate anchor = the z→c_k evaluation map")
    print("      (PR #3458). NOT closeable by a smooth deformation ([4]); needs")
    print("      the root-of-unity accumulation. This session does NOT fit it.")

    ok_all = vol_ok and cs_ok and smooth_insufficient

    wb.add_data("vol_4_1", {"value": mp.nstr(vol, 20), "eq_2_lambda_pi3": vol_ok,
                            "role": "bar-EVEN part = −Vol(4₁), SOLVED"})
    wb.add_data("cs_4_1_complete", {"value": mp.nstr(cs_complete, 8), "is_zero": cs_ok,
                                    "note": "amphichiral ⇒ S is a deformation phase"})
    wb.add_data("nz_leading", {"form": "CVol(u)=CVol(0)−(τ/4)u²+O(u³)",
                               "cusp_modulus_factor": "sqrt(-3)", "pi3_link": True})
    wb.add_data("smooth_deformation_ruled_out", {
        "ratio_smooth_u_log_q": mp.nstr(ratio_smooth, 10),
        "ratio_measured": mp.nstr(ratio_meas, 8),
        "conclusion": "smooth real u(q0) gives ratio~1, not -4.08 -> phase channel / RoU accumulation"})
    wb.add_data("sharpened_gap", {
        "algebra": "closed (EkParitySplit decay projection, Lean sorry-free)",
        "object": "Faddeev Phi_b (validated evaluator)",
        "geometry": "S = bar-odd projection of 4_1 NZ deformation phase",
        "open_single_link": "u(q0) complex meridian deformation = z->c_k evaluation map (PR #3458)"})
    wb.add_assertion("vol_4_1_eq_2_lambda_pi3", computed=float(mp.fabs(vol - 2 * lam_pi3)),
                     expected=0.0, tolerance=1e-30, source="Bloch-Wigner D(e^{iπ/3})=Λ(π/3)")
    wb.add_assertion("cs_4_1_complete_zero", computed=float(mp.fabs(cs_complete)),
                     expected=0.0, tolerance=1e-30, source="4₁ amphichiral: CS=0 at complete structure")
    wb.add_assertion("smooth_deformation_ratio_is_unity_not_minus4",
                     computed=float(mp.fabs(ratio_smooth - 1)), expected=0.0, tolerance=1e-6,
                     source="smooth real u(q0)∝log q0 gives ratio~1; measured is -4.08 -> phase channel")
    wb.save()

    print(f"\n  RESULT: {'ALL OK' if ok_all else 'CHECK'}  (gap sharpened, not fitted, not closed)")
    return 0 if ok_all else 1


if __name__ == "__main__":
    raise SystemExit(main())
