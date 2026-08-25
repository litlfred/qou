#!/usr/bin/env python3
"""alpha_em_form_ladder_probe.py

Honest residual ladder for the α_EM Bring-zero-mode form (prop:em-coupling-bring-
zero-mode), reconstructed standalone (the committed alpha_em_4pi_fixed_point_solve.py
has a stale `_precision` import after the miga path reorg). Follows up the
path-to-1ppq audit's α_EM section with three honest caveats.

THE FORM (content block em-coupling-bring-zero-mode.md):
  1/α = q·[9]_q·[10]_q  +  2g/(4π(g-1))  +  αH(1−h²α)  +  Δ₂,   g = 4 (Bring genus),
  H = [2]_q/(8π); h = q−q⁻¹ (Hecke structure constant, NOT ℏ_q = 1−q⁻¹);
  Δ₂ = uncomputed archimedean two-loop (weight-3), NOT the −h²Hα² carried above.
  α is on both sides — the relation is solved as a FIXED POINT, not a series.
  [n]_q = (q^n − q^{-n})/(q − q^{-1}).
The integers ARE structurally derived (not free fits):
  g=4 = genus of Bring's surface; [9],[10] = crossing numbers of the two genus-4
  torus knots T_{2,9}, T_{3,5} (prop:force-carrier-bring-uniqueness); 2g/(4π(g-1))
  = dim H¹/Area (Hodge/Gauss-Bonnet) = 2/(3π).

THREE HONEST CAVEATS (this probe quantifies each):
  (A) CONJECTURAL: the block is conditional on THREE unproved classes
      (ArchimedeanLimit, BlochSuslinUniqueness, BringZeroModeBlochClass) — not a
      proved derivation (anti-laundering: conditional-class ≠ established).
  (B) ANCHOR-DEPENDENT: the quadratic fixed-point residual is ~1.7 ppb at the
      PROTON pin (the 2026-08-07 default for all compute) but ~80 ppb at the MUON
      pin. Any "80 ppb" headline is anchor-specific, not intrinsic. The witness
      reports BOTH anchors and scores against the proton one.
  (C) NOT YET AT TARGET: at the proton pin this probe's quadratic form is ~1.7 ppb
      = ~11x sigma_a (0.15 ppb), and ~1115x the L2 100x criterion sigma_a/100 =
      0.0015 ppb. NOTE the two are different multiples and have been conflated
      before (qou-ydmy): "N sigma" is not "N x the 100x target".
      This probe is also SUPERSEDED on the best number: adding the derived
      Schwinger factor (1 - h^2 alpha) gives 0.313 ppb = ~2.1 sigma_a (~209x the
      100x criterion). See alpha_em_schwinger_ladder_probe.py.

Net: α_EM stays the highest-VALUE 1-ppq target (a fundamental constant, structural
integers, a derivation gap not a calibration wall). No c_k / no coefficient fitted
here; scope-(a).

CORRECTION (2026-07-12, #3625): this probe uses the QUADRATIC fixed-point form and
so reports proton +1.7 ppb / muon +80 ppb. Adding the RT-phase-3-DERIVED Schwinger
(1-h^2 alpha) cubic term brings the PROTON residual to +0.313 ppb = ~2x sigma_a (the
closest not-yet-met observable to 1 ppq). See alpha_em_schwinger_ladder_probe.py +
alpha_em_anchor_preference_probe.py (#3625) for the corrected best number.

Companion: docs/audits/2026-07-11-path-to-1ppq-alpha-em-opportunity.md.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401, E402
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
CODATA_ALPHA_INV = mp.mpf("137.035999084")
SIGMA_PPB = mp.mpf("0.15")
ANCHORS = {
    "muon": mp.mpf("1.10997859555733471"),
    "proton": mp.mpf("1.109978582751380808"),
}


def qb(n, q):
    return (q ** n - q ** (-n)) / (q - q ** (-1))


def ppb(v):
    return float((v - CODATA_ALPHA_INV) / CODATA_ALPHA_INV * 1e9)


def forms(q):
    g = 4
    tree = q * qb(9, q) * qb(10, q)
    zero_mode = mp.mpf(2 * g) / (4 * mp.pi * (g - 1))          # = 2/(3π)
    additive = tree + zero_mode
    alpha_approx = 1 / additive
    plus_oalpha = additive + alpha_approx / (4 * mp.pi)         # first-order aH term
    # fixed-point cubic (quadratic truncation): α²H + αT − 1 = 0, T=additive, H=[2]_q/(8π)
    H = qb(2, q) / (8 * mp.pi)
    T = additive
    alpha_fp = (-T + mp.sqrt(T * T + 4 * H)) / (2 * H)
    fixed_point = 1 / alpha_fp
    return {"tree": tree, "zero_mode": zero_mode, "additive": additive,
            "plus_oalpha": plus_oalpha, "fixed_point": fixed_point}


def main() -> int:
    print("=" * 78)
    print(" α_EM Bring-zero-mode form — honest residual ladder (prop:em-coupling-bring)")
    print("=" * 78)

    wb = WitnessBuilder("alpha-em-form-ladder", engine="mpmath")
    wb.set_description(
        "Standalone residual ladder for the alpha_EM Bring-zero-mode form "
        "(1/a=q[9]_q[10]_q+2g/(4pi(g-1))+a*H*(1-h^2 a)+D2, g=4; H=[2]_q/(8pi), "
        "h=q-1/q Hecke structure constant; D2=uncomputed archimedean 2-loop). "
        "Integers structurally derived "
        "(Bring genus 4; crossing numbers of T_{2,9},T_{3,5}). Honest caveats: "
        "(A) conjectural (3 unproved classes), (B) anchor-dependent (~1.7 ppb proton "
        "vs ~80 ppb muon; scored at the proton default), (C) proton quadratic ~1.7 ppb "
        "= ~11x sigma_a = ~1115x the L2 100x criterion (sigma_a/100 = 0.0015 ppb); "
        "SUPERSEDED on the best number by the +Schwinger cubic at 0.313 ppb. Highest-value "
        "but long-horizon conjectural close, not near-term. No coefficient fitted; scope-(a)."
    )
    wb.set_content_block("prop:em-coupling-bring-zero-mode")

    print(f"\n  CODATA 1/α = {mp.nstr(CODATA_ALPHA_INV, 15)}   σ_α = {float(SIGMA_PPB)} ppb")
    print(f"  integers: g=4 (Bring genus); [9],[10] = cross# of T(2,9),T(3,5) [structural]\n")

    data = {}
    for name, q in ANCHORS.items():
        f = forms(q)
        print(f"  --- q0 = {name} ({float(q):.12f}) ---")
        print(f"    tree q[9][10]          = {mp.nstr(f['tree'],13)}")
        print(f"    + zero-mode 2/(3π)     = {mp.nstr(f['additive'],13)}   resid = {ppb(f['additive']):+.1f} ppb")
        print(f"    + αH first order       = {mp.nstr(f['plus_oalpha'],13)}   resid = {ppb(f['plus_oalpha']):+.1f} ppb")
        print(f"    fixed-point (α²H+αT=1) = {mp.nstr(f['fixed_point'],13)}   resid = {ppb(f['fixed_point']):+.1f} ppb")
        print(f"      best form vs σ_α: {abs(ppb(f['fixed_point']))/float(SIGMA_PPB):.0f}× experimental σ\n")
        data[name] = {k: mp.nstr(v, 15) for k, v in f.items()}
        data[name]["fixed_point_resid_ppb"] = ppb(f["fixed_point"])
        data[name]["additive_resid_ppb"] = ppb(f["additive"])

    fp_muon = ppb(forms(ANCHORS["muon"])["fixed_point"])
    fp_proton = ppb(forms(ANCHORS["proton"])["fixed_point"])

    print("  HONEST STATUS:")
    print("  (A) CONJECTURAL — conditional on 3 unproved classes (ArchimedeanLimit,")
    print("      BlochSuslinUniqueness, BringZeroModeBlochClass). Not a proved derivation.")
    print(f"  (B) ANCHOR-DEPENDENT — fixed-point resid {fp_proton:+.1f} ppb (proton) vs "
          f"{fp_muon:+.1f} ppb (muon).")
    print(f"  (C) NOT AT TARGET — this probe's quadratic form at the PROTON default is "
          f"{abs(fp_proton):.2f} ppb")
    print(f"      = {abs(fp_proton)/float(SIGMA_PPB):.0f}× σ_α, and "
          f"{abs(fp_proton)/(float(SIGMA_PPB)/100):.0f}× the L2 100× criterion "
          f"(σ_α/100 = {float(SIGMA_PPB)/100:.4f} ppb).")
    print("      Those are DIFFERENT multiples — 'N σ' is not 'N × the 100× target' (qou-ydmy).")
    print("      SUPERSEDED on the best number: the +Schwinger cubic reaches 0.313 ppb")
    print("      (~2.1 σ_α, ~209× the criterion) — see alpha_em_schwinger_ladder_probe.py.")
    print("  => highest-VALUE 1-ppq target, but LONG-HORIZON conjectural, not near-term.")

    wb.add_data("ladder", data)
    wb.add_data("integers_provenance", {
        "g": "4 = genus of Bring's surface (structural)",
        "9_10": "crossing numbers of T(2,9),T(3,5) (prop:force-carrier-bring-uniqueness)",
        "zero_mode": "2g/(4pi(g-1)) = dim H^1/Area (Hodge/Gauss-Bonnet) = 2/(3pi)"})
    wb.add_data("honest_status", {
        "conjectural": "3 unproved classes; conditional-class != established",
        "anchor_dependent": {"proton_ppb": fp_proton, "muon_ppb": fp_muon},
        "not_at_target": f"best ~{abs(fp_muon):.0f} ppb muon = ~{abs(fp_muon)/float(SIGMA_PPB):.0f}x sigma_a",
        "verdict": "highest-value but long-horizon conjectural close, not near-term"})
    # Scored at the PROTON pin: the 2026-08-07 owner directive makes the
    # experimental anchor the default for all compute.  The L2 100x criterion is
    # sigma_exp/100 = 0.0015 ppb -- NOT 10*sigma (1.5 ppb) and NOT 15 ppb, both
    # of which this assertion previously conflated (bean qou-ydmy).
    target_100x = float(SIGMA_PPB) / 100.0
    wb.add_assertion("alpha_em_not_at_100x_target",
                     computed=float(abs(fp_proton) > target_100x), expected=1.0, tolerance=0.5,
                     source=(f"proton-anchored quadratic residual {abs(fp_proton):.2f} ppb "
                             f"exceeds the L2 100x target sigma_a/100 = {target_100x:.4f} ppb "
                             f"by ~{abs(fp_proton)/target_100x:.0f}x. The cubic (+Schwinger) form "
                             f"reaches 0.313 ppb, still ~209x short -- see "
                             f"alpha_em_schwinger_ladder_probe.py, which supersedes this probe's "
                             f"best number."))
    wb.add_assertion("alpha_em_anchor_dependent",
                     computed=float(abs(fp_muon - fp_proton) > 10.0), expected=1.0, tolerance=0.5,
                     source=(f"quadratic fixed-point residual is {abs(fp_proton):.2f} ppb at the "
                             f"proton (default) pin vs {abs(fp_muon):.1f} ppb at the muon pin -- "
                             f"the mu-p substrate tension, not an intrinsic scale"))
    wb.save()

    print("\n  RESULT: ladder computed (standalone; no fitted coefficient)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
