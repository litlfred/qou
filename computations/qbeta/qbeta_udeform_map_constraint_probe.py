#!/usr/bin/env python3
"""
qbeta_udeform_map_constraint_probe.py — constraint characterization of the open
substrate→deformation map u(q₀) in the S-channel S = Im 𝔙(u(q₀)).

CORRECTION (2026-07-26) — WRONG NZ LEADING FORM FIXED.
========================================================================
This probe previously inverted the HEURISTIC figure-eight leading form
    Im 𝔙(u) ≈ (√3/2)|u|²·sin 2φ  =  √3·Re(u)·Im(u)         (WRONG)
which corresponds to a REAL a₂. The CCGLS A-polynomial cusp modulus of 4₁ is
τ = −i√3 (PURELY IMAGINARY, ℚ(√−3)), so the leading complex-volume coefficient
a₂ = 𝔙″(0)/2 = i·√3/4 is PURELY IMAGINARY, giving the CORRECT leading form
    Im 𝔙(u) = (√3/4)(Re²u − Im²u) = (√3/4)|u|²·cos 2φ       (RIGHT)
which vanishes on the DIAGONALS |Re u| = |Im u| (φ = ±π/4), NOT on the axes.
This is proved sorry-free in QOU/Knot/FigureEightComplexVolume.lean (`imV₄₁`,
lean-verify exit 0) and is the authoritative object; the corrected numerical
analysis lives in the T2 probe
    computations/probes/sdeformed_channel_signflip_probe.py
and the audit docs/audits/2026-07-26-sdeformed-channel-signflip.md.

Consequences of the fix for the family pruning below (all REFUTED now):
  * F1 (fixed-phase, Re²−Im² = a²cos2φ₀·d² ∝ d²) — STILL refuted (unchanged
    conclusion, now via the corrected even-quadratic form).
  * F2 (phase-crossing Re∝d, Im∝d²): Re²−Im² = d² − d⁴ ≈ d² (leading), so
    S ∝ d² (NOT the old S∝d³ — that cubic was an ARTEFACT of the wrong √3·Re·Im
    form). Being even in d, F2 gives the same sign at both anchors ⇒ REFUTED.
  * F3 (transverse-const Re∝d, Im≈c₀): Re²−Im² = (Re)²−c₀², EVEN in d and
    dominated by −c₀² (|Re| ≪ c₀ at both anchors) ⇒ same (negative) sign at
    both anchors ⇒ REFUTED. Its prior "survival" was the heuristic artefact.
  * NEW surviving constraint: S sign-flips only where Re²−Im² changes sign, so
    a viable u(q₀) MUST CROSS the diagonal |Re u| = |Im u| between the anchors
    ((Re²−Im²) = S/κ: +0.0224 at muon, −0.0911 at proton). u(q₀) stays OPEN.
========================================================================

The binding side of conj:binding-qbeta-complex-volume (Lean carrier
`QOU.QBeta.PhiBSArgumentIdentification.SDeformedVolumeChannel`, PR #3773) needs
the open map u(q₀) (log meridian holonomy). This probe INVERTS the CORRECTED 4₁
Neumann–Zagier leading form of the deformed complex volume,

    Im 𝔙(u) = (√3/4)·(Re²u − Im²u),      u = |u|e^{iφ}    (a₂ = i·√3/4)

against the two measured anchor S values and the root-found q*, and tests the
minimal structural families for u(q₀). It is a MEASUREMENT + scope-(a)/(b)
family pruning — no u-map is wired, no c_k proposed, no instance fabricated.

Findings encoded as assertions:
  [F1] fixed-phase u ∝ (q−q*)·e^{iφ₀} gives Re²−Im² = a²cos(2φ₀)·(q−q*)² ∝ d²
       — same sign on both sides of q*: REFUTED by the measured sign flip
       (scope-(a): this family, alone, at leading order).
  [F2] minimal phase-crossing (Re ∝ d, Im ∝ d², d = q−q*) gives Re²−Im² =
       d² − d⁴ ≈ d² (leading) ⇒ S ∝ d² (even) — same sign at both anchors, and
       the corrected predicted ratio (d_pr/d_mu)² is POSITIVE while the measured
       ratio is negative: REFUTED (scope-(a); corrects the old S∝d³ artefact).
  [F3] transverse-constant family (Re(u) ∝ d, Im(u) ≈ c₀) gives Re²−Im² =
       Re² − c₀², EVEN in d and dominated by −c₀² since |Re| ≪ c₀ near q*:
       same (negative) sign at both anchors ⇒ REFUTED. (Its #3773 survival was
       an artefact of the wrong √3·Re·Im form.)
  [NEW] channel not scope-(b) excluded: (Re²−Im²) = S/κ is +ve at muon, −ve at
       proton ⇒ any u(q₀) realizing the flip must CROSS the diagonal
       |Re u| = |Im u| between the anchors. Sharper open constraint; map OPEN.

Companion Lean: exists_cs_vanishing (Im 𝔙(u(q*)) = 0 — this probe's q* is the
numerical face of that derived theorem). NOTE (flagged for follow-up in the
audit): the laws in QOU.QBeta.UDeformFamilyPruning
(cubic_ratio_law, linear_family_eq, linear_family_sign_flip,
hasDerivAt_linear_family, and the `nzLeading x y = √3·x·y` definition) are built
on the WRONG √3·Re·Im leading form and are CONTRADICTED by this correction
(F2 is not cubic; F3 does not sign-flip). Only fixed_phase_family_excluded
reaches the right F1 conclusion, and even that is proved about the wrong form.
The Lean is NOT edited here — see docs/audits/2026-07-26-sdeformed-channel-signflip.md.
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
KAPPA = SQRT3 / 4  # = |a₂|; a₂ = i·κ purely imaginary, from τ = −i√3 (A-poly)


def S(q):
    return c3_target_at(q, QCOD, ME) + VOL41


def main() -> int:
    print("=" * 78)
    print(" u(q₀) constraint probe — CORRECTED NZ leading-form inversion + pruning")
    print(" (Im 𝔙 = (√3/4)(Re²u−Im²u); a₂ = i√3/4 from τ = −i√3, A-polynomial)")
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

    # [1] CORRECTED NZ leading-form inversion: required (Re²−Im²) at each anchor.
    #     Im 𝔙 = κ(Re²u−Im²u) = S  ⇒  (Re²u−Im²u) = S/κ = 4S/√3.
    need_mu, need_pr = Sm / KAPPA, Sp / KAPPA
    umin_mu = mp.sqrt(abs(need_mu))   # min |u| for a given Re²−Im² (on an axis)
    umin_pr = mp.sqrt(abs(need_pr))
    print("\n[1] inversion of Im 𝔙(u) = (√3/4)(Re²u − Im²u) at the anchors:")
    print(f"    required (Re²u−Im²u) = 4S/√3:  muon {mp.nstr(need_mu, 6)}  (>0 ⇒ |Re u|>|Im u|)")
    print(f"                                   proton {mp.nstr(need_pr, 6)}  (<0 ⇒ |Re u|<|Im u|)")
    print(f"    minimal |u| (on the near axis):  muon {mp.nstr(umin_mu, 6)}   proton {mp.nstr(umin_pr, 6)}")
    print(f"    (ladder lever u_sub(q*) = {mp.nstr(substrate_ladder_quantities(qstar)['u'], 6)} for scale)")

    # [2] family pruning against the CORRECTED form (all three refuted).
    ratio_meas = Sp / Sm
    ratio_F2_corrected = (d_pr / d_mu) ** 2   # S ∝ d² (leading), NOT d³
    print("\n[2] structural families for u(q₀) (leading order, scope-(a)/(b)):")
    print("    F1 fixed-phase u = a·e^{iφ₀}·d:  Re²−Im² = a²cos(2φ₀)·d² ∝ d²")
    print("       — even in d ⇒ NO sign flip across q* ⇒ REFUTED by the measured flip.")
    print(f"    F2 phase-crossing Re∝d, Im∝d²:  Re²−Im² = d² − d⁴ ≈ d² (leading), S ∝ d²")
    print(f"       corrected ratio (d_pr/d_mu)² = {mp.nstr(ratio_F2_corrected, 5)} (>0);"
          f" measured {mp.nstr(ratio_meas, 5)} (<0)")
    print(f"       ⇒ even in d ⇒ same sign ⇒ REFUTED (old 'S∝d³' was a wrong-form artefact).")

    # F3: take the #3773-surviving family (Re linear-thru-zero at q*, Im = const
    # c₀) and re-evaluate under the CORRECTED form. The #3773 OLD-form fit pins
    # ONLY the product k_r·c₀ = S_old/(√3·d) ≈ 2.216e6, leaving c₀ free (and
    # k_r = 2.216e6/c₀). So the faithful re-evaluation sets Re_i = S_i/(√3·c₀)
    # (invert the product slope) and computes S_corr = κ(Re² − c₀²). To reproduce
    # the MEASURED flip we need S_corr(muon) > 0 > S_corr(proton):
    #   S_corr(muon)  > 0  ⟺  |Re_mu| > c₀  ⟺  c₀ < c_mu* = (S_mu/√3)^½
    #   S_corr(proton)< 0  ⟺  |Re_pr| < c₀  ⟺  c₀ > c_pr* = (|S_pr|/√3)^½
    # Since |S_pr| > |S_mu| ⇒ c_pr* > c_mu*, these two conditions are INCOMPATIBLE:
    # no c₀ > 0 reproduces the measured muon>0>proton flip. F3 REFUTED.
    print("\n    F3 transverse-const Re∝d, Im≈c₀:  Re²−Im² = Re² − c₀²  (EVEN in d)")
    c_mu_star = mp.sqrt(Sm / SQRT3)          # c₀ threshold for S_corr(muon) sign
    c_pr_star = mp.sqrt(abs(Sp) / SQRT3)     # c₀ threshold for S_corr(proton) sign
    print(f"       measured flip needs c₀ < c_mu* = {mp.nstr(c_mu_star,6)} (for S(muon)>0)")
    print(f"                       AND c₀ > c_pr* = {mp.nstr(c_pr_star,6)} (for S(proton)<0)")
    print(f"       c_pr* > c_mu* ⇒ INCOMPATIBLE ⇒ no c₀ reproduces muon>0>proton.")
    f3_reproduces_measured = False
    for c0 in (mp.mpf("0.30"), mp.mpf("0.15"), mp.mpf("0.10"), mp.mpf("0.05")):
        re_mu = Sm / (SQRT3 * c0)     # invert OLD-form product slope: Re·c₀ = S/√3
        re_pr = Sp / (SQRT3 * c0)
        s_mu = KAPPA * (re_mu ** 2 - c0 ** 2)   # corrected S at muon
        s_pr = KAPPA * (re_pr ** 2 - c0 ** 2)   # corrected S at proton
        measured_flip = bool(s_mu > 0 > s_pr)
        f3_reproduces_measured = f3_reproduces_measured or measured_flip
        print(f"       c₀={mp.nstr(c0,3)}: S_corr(muon)={mp.nstr(s_mu,5)}, "
              f"S_corr(proton)={mp.nstr(s_pr,5)}  measured-flip(μ>0>p)={measured_flip}")
    f3_refuted = bool((c_pr_star > c_mu_star) and not f3_reproduces_measured)
    print("       ⇒ F3 CANNOT produce the measured muon>0>proton flip for ANY c₀ ⇒")
    print("         REFUTED (scope-(b), invariant a₂ purely imaginary ⇒ Re²−Im² even;")
    print("         refines the audit's 'same sign' claim — a WRONG-direction flip")
    print("         (μ<0<p) opens only in c_mu*<c₀<c_pr*, never the measured one).")

    f1_refuted = bool(sign_flip)  # even-in-d family vs measured flip
    # F2 refuted: even in d (positive corrected ratio) cannot match the negative
    # measured ratio.
    f2_refuted = bool(ratio_F2_corrected > 0 > ratio_meas)

    # [3] NEW surviving constraint: a diagonal crossing (channel not excluded).
    crosses = (need_mu > 0) != (need_pr > 0)
    print("\n[3] NEW surviving constraint (channel NOT scope-(b) excluded):")
    print("    Re²u−Im²u = S/κ opposite-signed at the anchors ⇒ u(q₀) MUST cross the")
    print(f"    diagonal |Re u|=|Im u| between muon ({mp.nstr(need_mu,6)}) and proton"
          f" ({mp.nstr(need_pr,6)}): {crosses}")
    print("    ⇒ sharper than the old 'F3: one-linear-one-const' — but u(q₀) stays OPEN.")
    print("      No u-map wired; identification open; nothing fabricated.")

    wb = WitnessBuilder("qbeta-udeform-map-constraint", engine="mpmath")
    wb.set_description(
        "Constraint characterization of the open substrate→deformation map "
        "u(q₀) in S = Im 𝔙(u(q₀)) (conj:binding-qbeta-complex-volume S-channel, "
        "Lean SDeformedVolumeChannel). CORRECTED (2026-07-26): the deformed "
        "complex volume's leading Im is Im 𝔙 = (√3/4)(Re²u−Im²u) (a₂ = i√3/4 "
        "from the A-polynomial cusp modulus τ=−i√3; proved in Lean "
        "FigureEightComplexVolume), NOT the prior heuristic √3·Re·Im. Inversion "
        "target is (Re²u−Im²u) = 4S/√3 at each anchor. Under the corrected form "
        "ALL three minimal families are refuted: F1 (fixed-phase, ∝d² even), F2 "
        "(phase-crossing, Re²−Im²≈d² so S∝d² even — corrects the old S∝d³ "
        "artefact), F3 (transverse-const, Re²−c₀² even, dominated by −c₀² ⇒ same "
        "sign both anchors). The surviving constraint is a diagonal crossing: "
        "(Re²u−Im²u)=S/κ is +0.0224 at muon, −0.0911 at proton, so a viable "
        "u(q₀) must cross |Re u|=|Im u| between the anchors. Measurement + "
        "pruning only — no u-map wired, no c_k proposed, no instance fabricated.")
    wb.set_content_block("conj:binding-qbeta-complex-volume")
    wb.add_data("inversion", {
        "leading_form": "Im V = (sqrt3/4)*(Re^2 u - Im^2 u); a2 = i*sqrt3/4 (tau=-i*sqrt3)",
        "q_star": mp.nstr(qstar, 25),
        "S_muon": mp.nstr(Sm, 12), "S_proton": mp.nstr(Sp, 12),
        "required_ReSq_minus_ImSq_muon": mp.nstr(need_mu, 10),
        "required_ReSq_minus_ImSq_proton": mp.nstr(need_pr, 10),
        "u_min_muon_near_axis": mp.nstr(umin_mu, 10),
        "u_min_proton_near_axis": mp.nstr(umin_pr, 10),
        "u_sub_qstar_for_scale": mp.nstr(substrate_ladder_quantities(qstar)["u"], 10)})
    wb.add_data("family_pruning", {
        "ratio_measured_Spr_over_Smu": mp.nstr(ratio_meas, 10),
        "ratio_F2_corrected_dsq_family": mp.nstr(ratio_F2_corrected, 10),
        "F1_verdict": "refuted (Re^2-Im^2 proportional to d^2, even => same sign)",
        "F2_verdict": ("refuted (Re^2-Im^2 = d^2-d^4 ~ d^2 leading => S ~ d^2 even; "
                       "corrected ratio (d_pr/d_mu)^2 > 0 vs measured < 0; old S~d^3 "
                       "was a wrong-form artefact)"),
        "F3_verdict": ("refuted (Re^2-Im^2 = Re^2 - c0^2, even in d; reproducing "
                       "measured mu>0>proton needs c0 < c_mu* AND c0 > c_pr* with "
                       "c_pr* > c_mu* => incompatible => no c0 works; prior #3773 "
                       "survival was a wrong-form artefact. Refines the audit's "
                       "'same sign' claim: a WRONG-direction flip mu<0<proton opens "
                       "only in c_mu*<c0<c_pr*, never the measured one)"),
        "F3_c_mu_star": mp.nstr(c_mu_star, 10),
        "F3_c_pr_star": mp.nstr(c_pr_star, 10)})
    wb.add_data("surviving_constraint", {
        "channel_status": ("NOT scope-(b) excluded; requires u(q0) crossing the "
                           "diagonal |Re u|=|Im u| between anchors"),
        "ReSq_minus_ImSq_muon": mp.nstr(need_mu, 10),
        "ReSq_minus_ImSq_proton": mp.nstr(need_pr, 10),
        "diagonal_crossing_required": bool(crosses),
        "verdict": ("u(q0) leading-order constraint (CORRECTED form): all minimal "
                    "families F1/F2/F3 refuted; the surviving admissible constraint "
                    "is that u(q0) crosses the diagonal |Re u|=|Im u| between the "
                    "anchors (Re^2-Im^2 = +0.0224 muon, -0.0911 proton). Numerical "
                    "face of the Lean exists_cs_vanishing (Im V(u(q*))=0). Map OPEN; "
                    "nothing wired.")})
    wb.add_data("correction_note", {
        "date": "2026-07-26",
        "wrong_form": "Im V ~ sqrt3*Re*Im = (sqrt3/2)|u|^2 sin2phi (implies real a2)",
        "right_form": "Im V = (sqrt3/4)(Re^2 u - Im^2 u) = (sqrt3/4)|u|^2 cos2phi",
        "reason": "A-polynomial cusp modulus tau = -i*sqrt3 (purely imaginary, Q(sqrt-3)) => a2 = i*sqrt3/4",
        "authoritative": ["folio/quantum-observable-universe/lean/QOU/Knot/FigureEightComplexVolume.lean (imV41)",
                          "computations/probes/sdeformed_channel_signflip_probe.py",
                          "docs/audits/2026-07-26-sdeformed-channel-signflip.md"],
        "lean_companion_contradicted": ("QOU.QBeta.UDeformFamilyPruning cubic_ratio_law / "
                                        "linear_family_eq / linear_family_sign_flip / "
                                        "hasDerivAt_linear_family + the nzLeading=sqrt3*x*y "
                                        "definition are built on the wrong form; flagged for "
                                        "follow-up (Lean not edited here)")})
    wb.add_assertion("anchors_reproduce", str(bool(repro)), "True")
    wb.add_assertion("sign_flip_hard_fact", str(bool(sign_flip)), "True")
    wb.add_assertion("F1_fixed_phase_refuted_by_sign_flip",
                     str(bool(f1_refuted)), "True",
                     source="Re^2-Im^2 = a^2 cos2phi0 d^2 (even) => same sign")
    wb.add_assertion("F2_phasecrossing_refuted_corrected",
                     str(bool(f2_refuted)), "True",
                     source="Re^2-Im^2 ~ d^2 (even); corrected ratio "
                            + mp.nstr(ratio_F2_corrected, 5) + " (>0) vs measured "
                            + mp.nstr(ratio_meas, 5) + " (<0)")
    wb.add_assertion("F3_transverse_const_refuted",
                     str(bool(f3_refuted)), "True",
                     source="measured mu>0>proton needs c0<c_mu*=" + mp.nstr(c_mu_star, 5)
                            + " AND c0>c_pr*=" + mp.nstr(c_pr_star, 5)
                            + " (incompatible) => no c0 reproduces the measured flip")
    wb.add_assertion("channel_requires_diagonal_crossing",
                     str(bool(crosses)), "True",
                     source="Re^2-Im^2 = S/kappa: +ve muon, -ve proton => u crosses "
                            "|Re u|=|Im u| between anchors (channel not scope-(b) excluded)")
    wb.save()
    print("\nwitness → qbeta-udeform-map-constraint.witness.json")
    ok = all([repro, sign_flip, f1_refuted, f2_refuted, f3_refuted, crosses])
    print("VERDICT: all F1/F2/F3 refuted (corrected form); surviving constraint = "
          "diagonal crossing, u(q₀) OPEN")
    print("ALL ASSERTIONS PASS" if ok else "ASSERTION FAILURE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
