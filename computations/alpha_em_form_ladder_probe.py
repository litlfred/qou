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
      Schwinger factor (1 - h^2 alpha) gives -0.365 ppb = 2.38 sigma_a (238x the
      100x criterion). See alpha_em_schwinger_ladder_probe.py. (Those read
      "0.313 ppb / ~2.1 sigma / ~209x" while both files scored against CODATA
      2018; the reference is now read from the registry and the residual's SIGN
      changed with the edition -- see #7069.)

Net: α_EM stays the highest-VALUE 1-ppq target (a fundamental constant, structural
integers, a derivation gap not a calibration wall). No c_k / no coefficient fitted
here; scope-(a).

CORRECTION (2026-07-12, #3625): this probe uses the QUADRATIC fixed-point form and
so reports proton +1.7 ppb / muon +80 ppb. Adding the RT-phase-3-DERIVED Schwinger
(1-h^2 alpha) cubic term brings the PROTON residual to -0.365 ppb = 2.38x sigma_a (the
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
from witness_base import WitnessBuilder, q0_comparison  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP, q_muon_at  # noqa: E402
from qou_substrate import codata as _codata  # noqa: E402

set_compute_dps()
# CODATA reference: READ FROM THE REGISTRY, never hand-typed.
#
# This file used to carry `CODATA_ALPHA_INV = mp.mpf("137.035999084")` (CODATA
# 2018) and `SIGMA_PPB = mp.mpf("0.15")`, with a witness note calling the 2018
# pin deliberate because "bumping it alone would desynchronise the recorded
# residuals". That is an argument for re-running, not for freezing, and the
# edition shift (0.6787 ppb) is 2.2x the SCHWINGER form's residual — large
# enough to flip that residual's sign. Reading the registry removes the choice:
# there is no edition to pick and the value tracks the table.
#
# `qou-rbdi` records that codata.py has "NO fine-structure entry". That is
# FALSE (corrected on the bean, PR #7069): it greps the module SOURCE, which
# cannot see entries parsed at runtime out of `data/allascii.txt`.
_ALPHA_INV = _codata.codata("inverse fine-structure constant")
CODATA_ALPHA_INV = mp.mpf(_ALPHA_INV.value_str)
# sigma derived from the table's own uncertainty; the old 0.15 was a 2%
# truncation of 0.15325.
SIGMA_PPB = mp.mpf(_ALPHA_INV.uncertainty_str) / CODATA_ALPHA_INV * mp.mpf(10) ** 9
# Both anchors are read BY NAME from the substrate (owner authorisation 2026-09-03,
# bean qou-4bef). Until then this file hardcoded the RETIRED muon pin A
# (1.10997859555733471, the self-certified value retired 2026-08-22/28) and a
# 19-figure truncation of the proton string; the muon residual it published
# (80.51 ppb) is therefore superseded by the value at the live CODATA-2022
# derivation (~81.04 ppb). The proton pin is the 2026-08-07 default; the muon
# leg is a DELIBERATE comparison (the mu-p substrate tension), stamped as such.
ANCHORS = {
    "muon": q_muon_at(50),               # ideal CAL-2 pin: live CODATA-2022 muon derivation
    "proton": Q_MP,   # experimental default (proton, 50-digit string)
}


def qb(n, q):
    return (q ** n - q ** (-n)) / (q - q ** (-1))


def ppb(v):
    """Residual against CODATA in parts per billion, carried as ``mpf``
    (no float64 anywhere on the value path; bean qou-4bef)."""
    return (v - CODATA_ALPHA_INV) / CODATA_ALPHA_INV * mp.mpf(10) ** 9


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
        "SUPERSEDED on the best number by the +Schwinger cubic at -0.365 ppb. Highest-value "
        "but long-horizon conjectural close, not near-term. No coefficient fitted; scope-(a)."
    )
    wb.set_content_block("prop:em-coupling-bring-zero-mode")

    print(f"\n  CODATA 1/α = {mp.nstr(CODATA_ALPHA_INV, 15)}   σ_α = {mp.nstr(SIGMA_PPB, 3)} ppb")
    print(f"  integers: g=4 (Bring genus); [9],[10] = cross# of T(2,9),T(3,5) [structural]\n")

    data = {}
    for name, q in ANCHORS.items():
        f = forms(q)
        print(f"  --- q0 = {name} ({mp.nstr(q, 14)}) ---")
        print(f"    tree q[9][10]          = {mp.nstr(f['tree'],13)}")
        print(f"    + zero-mode 2/(3π)     = {mp.nstr(f['additive'],13)}   resid = {mp.nstr(ppb(f['additive']), 5)} ppb")
        print(f"    + αH first order       = {mp.nstr(f['plus_oalpha'],13)}   resid = {mp.nstr(ppb(f['plus_oalpha']), 5)} ppb")
        print(f"    fixed-point (α²H+αT=1) = {mp.nstr(f['fixed_point'],13)}   resid = {mp.nstr(ppb(f['fixed_point']), 5)} ppb")
        print(f"      best form vs σ_α: {mp.nstr(abs(ppb(f['fixed_point'])) / SIGMA_PPB, 3)}× experimental σ\n")
        data[name] = {k: mp.nstr(v, 15) for k, v in f.items()}
        data[name]["fixed_point_resid_ppb"] = fmt(ppb(f["fixed_point"]), 20)
        data[name]["additive_resid_ppb"] = fmt(ppb(f["additive"]), 20)
        data[name]["q0"] = fmt(q, 50)

    fp_muon = ppb(forms(ANCHORS["muon"])["fixed_point"])
    fp_proton = ppb(forms(ANCHORS["proton"])["fixed_point"])

    print("  HONEST STATUS:")
    print("  (A) CONJECTURAL — conditional on 3 unproved classes (ArchimedeanLimit,")
    print("      BlochSuslinUniqueness, BringZeroModeBlochClass). Not a proved derivation.")
    print(f"  (B) ANCHOR-DEPENDENT — fixed-point resid {mp.nstr(fp_proton, 5)} ppb (proton) vs "
          f"{mp.nstr(fp_muon, 5)} ppb (muon, live CODATA-2022 derivation).")
    print(f"  (C) NOT AT TARGET — this probe's quadratic form at the PROTON default is "
          f"{mp.nstr(abs(fp_proton), 4)} ppb")
    print(f"      = {mp.nstr(abs(fp_proton) / SIGMA_PPB, 3)}× σ_α, and "
          f"{mp.nstr(abs(fp_proton) / (SIGMA_PPB / 100), 4)}× the L2 100× criterion "
          f"(σ_α/100 = {mp.nstr(SIGMA_PPB / 100, 3)} ppb).")
    print("      Those are DIFFERENT multiples — 'N σ' is not 'N × the 100× target' (qou-ydmy).")
    print("      SUPERSEDED on the best number: the +Schwinger cubic reaches -0.365 ppb")
    print("      (2.38 σ_α, 238× the criterion) — see alpha_em_schwinger_ladder_probe.py.")
    print("  => highest-VALUE 1-ppq target, but LONG-HORIZON conjectural, not near-term.")

    wb.add_data("ladder", data)
    # The reference the residuals below are scored against. It was NOT in the
    # witness (found 2026-09-04): the witness published `proton_ppb` /
    # `muon_ppb` while recording no value for them to be residuals FROM, so a
    # reader could not reproduce either number from the witness alone. Its own
    # consumer's docstring meanwhile claimed to "track the witness" for a value
    # the witness never held. Recording it here is what makes that claim true.
    wb.add_data("codata_reference", {
        "alpha_inv": _ALPHA_INV.value_str,
        "uncertainty": _ALPHA_INV.uncertainty_str,
        "sigma_ppb": fmt(SIGMA_PPB),
        "vintage": "CODATA-2022",
        "source": "qou_substrate.codata registry (data/allascii.txt) — derived, not chosen",
        "superseded": "137.035999084 (CODATA-2018 Cs recoil), sigma_ppb 0.15 "
                      "(a 2% rounding of 0.15325); the 0.6787 ppb edition shift "
                      "flips the Schwinger form's residual sign, see #7069",
    })
    wb.add_data("integers_provenance", {
        "g": "4 = genus of Bring's surface (structural)",
        "9_10": "crossing numbers of T(2,9),T(3,5) (prop:force-carrier-bring-uniqueness)",
        "zero_mode": "2g/(4pi(g-1)) = dim H^1/Area (Hodge/Gauss-Bonnet) = 2/(3pi)"})
    wb.add_data("honest_status", {
        "conjectural": "3 unproved classes; conditional-class != established",
        "anchor_dependent": {"proton_ppb": fmt(fp_proton, 20), "muon_ppb": fmt(fp_muon, 20)},
        "not_at_target": (f"proton (default) quadratic {mp.nstr(abs(fp_proton), 4)} ppb = "
                          f"~{mp.nstr(abs(fp_proton) / SIGMA_PPB, 3)}x sigma_a = "
                          f"~{mp.nstr(abs(fp_proton) / (SIGMA_PPB / 100), 4)}x the L2 100x criterion; "
                          f"muon (ideal CAL-2, live CODATA-2022 derivation) {mp.nstr(abs(fp_muon), 4)} ppb. "
                          f"Superseded on the best number by the +Schwinger cubic (-0.365 ppb, proton)."),
        "verdict": "highest-value but long-horizon conjectural close, not near-term"})
    # Scored at the PROTON pin: the 2026-08-07 owner directive makes the
    # experimental anchor the default for all compute.  The L2 100x criterion is
    # sigma_exp/100 = 0.0015 ppb -- NOT 10*sigma (1.5 ppb) and NOT 15 ppb, both
    # of which this assertion previously conflated (bean qou-ydmy).
    target_100x = SIGMA_PPB / 100
    wb.add_assertion("alpha_em_not_at_100x_target",
                     computed=("1" if abs(fp_proton) > target_100x else "0"), expected="1", tolerance="0.5",
                     source=(f"proton-anchored quadratic residual {mp.nstr(abs(fp_proton), 4)} ppb "
                             f"exceeds the L2 100x target sigma_a/100 = {mp.nstr(target_100x, 3)} ppb "
                             f"by ~{mp.nstr(abs(fp_proton) / target_100x, 4)}x. The cubic (+Schwinger) form "
                             f"reaches -0.365 ppb, still 238x short -- see "
                             f"alpha_em_schwinger_ladder_probe.py, which supersedes this probe's "
                             f"best number."))
    wb.add_assertion("alpha_em_anchor_dependent",
                     computed=("1" if abs(fp_muon - fp_proton) > 10.0 else "0"), expected="1", tolerance="0.5",
                     source=(f"quadratic fixed-point residual is {mp.nstr(abs(fp_proton), 4)} ppb at the "
                             f"proton (default) pin vs {mp.nstr(abs(fp_muon), 4)} ppb at the muon pin "
                             f"(live CODATA-2022 derivation; the retired pin A gave 80.51) -- "
                             f"the mu-p substrate tension, not an intrinsic scale"))
    wb.save(q0_comparison(
        muon=ANCHORS["muon"], proton=ANCHORS["proton"],
        reason=("anchor-dependence ladder: both pins are read on purpose and each is "
                "reported under its own key; the proton (default) leg is the scored one, "
                "the muon leg measures the mu-p substrate tension on 1/alpha")))

    print("\n  RESULT: ladder computed (standalone; no fitted coefficient)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
