#!/usr/bin/env python3
"""
qbeta_udeform_map_constraint_probe.py — constraint characterization of the open
substrate→deformation map u(q₀) in the S-channel S = Im 𝔙(u(q₀)).

The binding side of conj:binding-qbeta-complex-volume (Lean carrier
`QOU.QBeta.PhiBSArgumentIdentification.SDeformedVolumeChannel`, PR #3773) needs
the open map u(q₀) (log meridian holonomy). This probe INVERTS the 4₁
Neumann–Zagier leading form of the deformed complex volume,

    Im 𝔙(u) ≈ (√3/2)·|u|²·sin 2φ  =  √3 · Re(u) · Im(u),      u = |u|e^{iφ}

(the leading form of the gluing-variety expansion,
qbeta_c3_barodd_gluing_newton_solve.py; docs/audits/
2026-07-11-complex-volume-conditional-mass-binding.md), against the two
measured anchor S values and the root-found q*, and tests the minimal
structural families for u(q₀). It is a MEASUREMENT + scope-(a) family
pruning — no u-map is wired, no c_k proposed, no instance fabricated.

Findings encoded as assertions:
  [F1] fixed-phase u ∝ (q−q*)·e^{iφ₀} gives S ∝ (q−q*)² — same sign on both
       sides of q*: REFUTED by the measured sign flip alone (scope-(a):
       this family, alone, at leading order).
  [F2] minimal phase-crossing (Re ∝ d, Im ∝ d², d = q−q*) gives S ∝ d³ —
       predicted anchor ratio (d_pr/d_mu)³ is off the measured
       S_pr/S_mu ≈ −4.08 by an order of magnitude: REFUTED (scope-(a)).
  [F3] transverse-constant family (Re(u) ∝ d, Im(u) ≈ const, or the
       mirror) gives S linear in d — anchor-consistent, and its single
       product-slope k = Re'·Im = S'(q*)/√3 matches the committed
       hypersensitivity witness. SURVIVES: the leading-order constraint is
       that ONE component of u(q₀) crosses zero linearly at q* while the
       OTHER is anchor-constant and nonzero.

Companion Lean: exists_cs_vanishing (Im 𝔙(u(q*)) = 0 — this probe's q* is
the numerical face of that derived theorem), and the family kill-test LAWS
are formalized sorry-free in QOU.QBeta.UDeformFamilyPruning
(fixed_phase_family_excluded, cubic_ratio_law, linear_family_sign_flip,
hasDerivAt_linear_family) — this probe supplies the measured violations,
the Lean supplies the laws they kill.
"""
from __future__ import annotations

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
SQRT3 = mp.sqrt(3)


def S(q):
    return c3_target_at(q, QCOD, ME) + VOL41


def main() -> int:
    print("=" * 78)
    print(" u(q₀) constraint probe — NZ leading-form inversion + family pruning")
    print("=" * 78)

    qp, qm = q_at(60), q_muon_at(60)
    Sp, Sm = S(qp), S(qm)
    print("\n[0] anchors (c3_target_at deterministic):")
    print(f"    S(muon)  = {mp.nstr(Sm, 8)}   (tgt +0.00968298)")
    print(f"    S(proton)= {mp.nstr(Sp, 8)}   (tgt −0.03945936)")
    repro = (abs(Sp - mp.mpf("-0.03945936")) < mp.mpf("1e-6")
             and abs(Sm - mp.mpf("0.00968298")) < mp.mpf("1e-6"))
    sign_flip = Sm > 0 > Sp

    qstar = mp.findroot(S, (qp + qm) / 2)
    d_mu, d_pr = qm - qstar, qp - qstar
    print(f"    q* = {mp.nstr(qstar, 25)}   d_mu = {mp.nstr(d_mu, 6)}, d_pr = {mp.nstr(d_pr, 6)}")

    # [1] NZ leading-form inversion: required Re(u)·Im(u) at each anchor.
    Pi_mu, Pi_pr = Sm / SQRT3, Sp / SQRT3
    umin_mu = mp.sqrt(2 * abs(Sm) / SQRT3)
    umin_pr = mp.sqrt(2 * abs(Sp) / SQRT3)
    print("\n[1] inversion of Im 𝔙(u) ≈ √3·Re(u)·Im(u) at the anchors:")
    print(f"    required Re·Im:  muon {mp.nstr(Pi_mu, 6)}   proton {mp.nstr(Pi_pr, 6)}")
    print(f"    minimal |u| (φ=±π/4):  muon {mp.nstr(umin_mu, 6)}   proton {mp.nstr(umin_pr, 6)}")
    print(f"    (ladder lever u_sub(q*) = {mp.nstr(substrate_ladder_quantities(qstar)['u'], 6)} for scale)")

    # [2] family pruning against the measured anchor ratio.
    ratio_meas = Sp / Sm
    ratio_F2 = (d_pr / d_mu) ** 3
    ratio_F3 = d_pr / d_mu
    print("\n[2] structural families for u(q₀) (leading order, scope-(a)):")
    print("    F1 fixed-phase u = a·e^{iφ₀}·d:  S ∝ d² — NO sign flip across q*.")
    print(f"       measured sign flip ⇒ REFUTED (alone, leading order).")
    print(f"    F2 phase-crossing Re∝d, Im∝d²:  S ∝ d³ — predicted S_pr/S_mu = {mp.nstr(ratio_F2, 5)}")
    print(f"       measured {mp.nstr(ratio_meas, 5)} ⇒ off by {mp.nstr(ratio_F2 / ratio_meas, 4)}× — REFUTED.")
    print(f"    F3 transverse-const Re∝d, Im≈c₀:  S ∝ d — predicted {mp.nstr(ratio_F3, 5)}")
    print(f"       measured {mp.nstr(ratio_meas, 5)} ⇒ agreement {mp.nstr(ratio_F3 / ratio_meas, 6)}")
    f1_refuted = bool(sign_flip)  # same-sign family vs measured flip
    f2_off = abs(ratio_F2 / ratio_meas)
    f2_refuted = f2_off > 10 or f2_off < mp.mpf("0.1")
    f3_agree = abs(ratio_F3 / ratio_meas - 1)

    # [3] F3 consistency: per-anchor product slope k_i = S_i/(√3·d_i) and the
    # hypersensitivity cross-check k = S'(q*)/√3.
    k_mu, k_pr = Sm / (SQRT3 * d_mu), Sp / (SQRT3 * d_pr)
    hh = mp.mpf("1e-18")
    dS = (S(qstar + hh) - S(qstar - hh)) / (2 * hh)
    k_star = dS / SQRT3
    mism = abs(k_mu / k_pr - 1)
    mism_star = max(abs(k_mu / k_star - 1), abs(k_pr / k_star - 1))
    print("\n[3] F3 (surviving family) consistency:")
    print(f"    k_mu = {mp.nstr(k_mu, 8)}   k_pr = {mp.nstr(k_pr, 8)}   anchor mismatch {mp.nstr(mism * 100, 3)}%")
    print(f"    k(q*) = S'(q*)/√3 = {mp.nstr(k_star, 8)}   max dev {mp.nstr(mism_star * 100, 3)}%")
    print("    ⇒ leading-order constraint on the open u(q₀): one component crosses")
    print("      zero linearly at q* (slope×transverse-const = k), the other is")
    print("      anchor-constant and nonzero. No u-map wired; identification open.")

    f3_consistent = mism < mp.mpf("0.10") and mism_star < mp.mpf("0.10")

    wb = WitnessBuilder("qbeta-udeform-map-constraint", engine="mpmath")
    wb.set_description(
        "Constraint characterization of the open substrate→deformation map "
        "u(q₀) in S = Im 𝔙(u(q₀)) (conj:binding-qbeta-complex-volume S-channel, "
        "Lean SDeformedVolumeChannel): NZ leading-form inversion at both anchors "
        "+ q*, and scope-(a) pruning of the minimal structural families. F1 "
        "(fixed-phase, S∝d²) refuted by the sign flip; F2 (phase-crossing, "
        "S∝d³) refuted by the anchor ratio; F3 (one component linear through "
        "zero at q*, the other anchor-constant) survives with product-slope "
        "k = S'(q*)/√3. Measurement + pruning only — no u-map wired, no c_k "
        "proposed, no instance fabricated.")
    wb.set_content_block("conj:binding-qbeta-complex-volume")
    wb.add_data("inversion", {
        "q_star": mp.nstr(qstar, 25),
        "S_muon": mp.nstr(Sm, 12), "S_proton": mp.nstr(Sp, 12),
        "required_ReIm_muon": mp.nstr(Pi_mu, 10),
        "required_ReIm_proton": mp.nstr(Pi_pr, 10),
        "u_min_muon_phi_pi4": mp.nstr(umin_mu, 10),
        "u_min_proton_phi_pi4": mp.nstr(umin_pr, 10),
        "u_sub_qstar_for_scale": mp.nstr(substrate_ladder_quantities(qstar)["u"], 10)})
    wb.add_data("family_pruning", {
        "ratio_measured_Spr_over_Smu": mp.nstr(ratio_meas, 10),
        "ratio_F2_cubic_family": mp.nstr(ratio_F2, 10),
        "ratio_F3_linear_family": mp.nstr(ratio_F3, 10),
        "F2_off_by_factor": mp.nstr(f2_off, 6)})
    wb.add_data("F3_consistency", {
        "k_product_slope_muon": mp.nstr(k_mu, 10),
        "k_product_slope_proton": mp.nstr(k_pr, 10),
        "k_product_slope_qstar_from_Sprime": mp.nstr(k_star, 10),
        "anchor_mismatch_pct": mp.nstr(mism * 100, 6),
        "max_dev_vs_qstar_pct": mp.nstr(mism_star * 100, 6),
        "verdict": ("u(q0) leading-order constraint: one component crosses zero "
                    "linearly at q* while the other is anchor-constant and nonzero "
                    "(F3); fixed-phase (F1) and minimal phase-crossing (F2) "
                    "families refuted scope-(a). Numerical face of the Lean "
                    "exists_cs_vanishing (Im V(u(q*)) = 0).")})
    wb.add_assertion("anchors_reproduce", str(bool(repro)), "True")
    wb.add_assertion("sign_flip_hard_fact", str(bool(sign_flip)), "True")
    wb.add_assertion("F1_fixed_phase_refuted_by_sign_flip",
                     str(bool(f1_refuted)), "True")
    wb.add_assertion("F2_cubic_family_refuted_by_anchor_ratio",
                     str(bool(f2_refuted)), "True",
                     source="F2/measured ratio = " + mp.nstr(f2_off, 5) + "x")
    wb.add_assertion("F3_linear_family_anchor_consistent",
                     str(bool(f3_consistent)), "True",
                     source="anchor mismatch " + mp.nstr(mism * 100, 4)
                            + "%; vs S'(q*)/sqrt3 " + mp.nstr(mism_star * 100, 4) + "%")
    wb.add_assertion("F3_ratio_agreement", float(f3_agree), 0.0, tolerance=1e-3)
    wb.save()
    print("\nwitness → qbeta-udeform-map-constraint.witness.json")
    ok = all([repro, sign_flip, f1_refuted, f2_refuted, f3_consistent])
    print("ALL ASSERTIONS PASS" if ok else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
