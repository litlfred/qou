#!/usr/bin/env python3
"""mmu_categorical_correction_first_probe.py — m_μ categorical-correction probe.

Production m_μ wiring uses the Kashaev volume identity at proton-pinned q₀:

    m_μ_pred = m_e × Vol(4_1) / ℏ_q²

This bare prediction misses CODATA by ~209.8 ppb (963.6× off the 100×
σ_exp target = 0.2177 ppb), per the L2 dashboard
[`per-observable-100x-status.witness.json`](per-observable-100x-status.witness.json).

The bare prediction is HIGHER than CODATA by ~210 ppb, so a categorical
correction factor δ(q) is needed such that:

    m_μ_pred_corrected = m_e × (Vol(4_1) / ℏ_q²) × (1 − δ(q₀))
    with δ(q₀) ≈ 2.1e-7

This probe tests 8 natural categorical correction terms at proton-
pinned q₀ to see whether ANY natural δ-structure lands within the 10
ppb gate (= 100× σ_exp; closer than the current 209.8 ppb).

8 candidate δ(q) formulas (closed-form, no fits):

  D1. ℏ_q⁶ / 4
  D2. ℏ_q⁶ × b / 4
  D3. (1 − b)² × ℏ_q⁴
  D4. h² × ℏ_q⁴ (h = q − q⁻¹)
  D5. ℏ_q⁴ × (q − 1) × Vol(4_1)
  D6. ℏ_q^8 / Vol(4_1)
  D7. (q − q⁻¹)³ × ℏ_q²
  D8. b²·ℏ_q⁶ × (q − 1) / 2

These are first-pass natural categorical corrections at the ℏ_q^6-ish
scale needed to land 2.1e-7. None has a deep structural derivation; the
probe is a falsification reference.

Verdict: NEGATIVE expected (the 8 candidates are guesses, not derived
forms). If any lands within 10 ppm of the needed correction (2.1e-7),
that's a residue-A-style candidate for m_μ. Otherwise the search space
narrows.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401

from mpmath import mp, mpf, sqrt  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from knot_volumes import vol_at  # noqa: E402 — canonical volume registry

# Vol(4_1) is EXCISED, not corrected (bean qou-ckbv, 2026-08-30).
# This file carried VOL_4_1_STR = "2.0298832128193072500115970029" -- 29
# digits printed, 19 correct, the same 20-digit carrier bean qou-f8lit
# tracks. Vol(4_1) has a closed form, 2*Cl_2(pi/3); a literal for it can
# only ever be a truncation of something the machine can compute exactly,
# so the fix is deletion rather than re-transcription.


def hoefsmit_b(q: mpf) -> mpf:
    h = q - 1 / q
    return sqrt((h ** 2 + 3) / (h ** 2 + 4))


# ── Candidate δ(q) formulas — return correction factor ──

def delta_1_hbar_6_over_4(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return hbar ** 6 / 4


def delta_2_hbar_6_b_over_4(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return hbar ** 6 * hoefsmit_b(q) / 4


def delta_3_one_minus_b_sq_hbar_4(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return (1 - hoefsmit_b(q)) ** 2 * hbar ** 4


def delta_4_h_sq_hbar_4(q: mpf) -> mpf:
    h = q - 1 / q
    hbar = (q - 1) / q
    return h ** 2 * hbar ** 4


def delta_5_hbar_4_q_minus_1_vol(q: mpf) -> mpf:
    hbar = (q - 1) / q
    vol = vol_at("4_1")
    return hbar ** 4 * (q - 1) * vol


def delta_6_hbar_8_over_vol(q: mpf) -> mpf:
    hbar = (q - 1) / q
    vol = vol_at("4_1")
    return hbar ** 8 / vol


def delta_7_h_cubed_hbar_sq(q: mpf) -> mpf:
    h = q - 1 / q
    hbar = (q - 1) / q
    return h ** 3 * hbar ** 2


def delta_8_b_sq_hbar_6_q_minus_1_over_2(q: mpf) -> mpf:
    hbar = (q - 1) / q
    b = hoefsmit_b(q)
    return b ** 2 * hbar ** 6 * (q - 1) / 2


def main() -> int:
    set_compute_dps()
    wb = WitnessBuilder("mmu-categorical-correction-first-probe", engine="mpmath")

    q_mp = Q_MP
    # Target δ ≈ 2.1e-7 (positive — bare m_μ_pred is HIGHER than CODATA;
    # subtracting δ reduces the prediction)
    target_delta = mpf("2.098e-7")  # bare miss / CODATA; from per-obs witness

    candidates = {
        "D1. hbar_q^6 / 4": delta_1_hbar_6_over_4,
        "D2. hbar_q^6 * b / 4": delta_2_hbar_6_b_over_4,
        "D3. (1 - b)^2 * hbar_q^4": delta_3_one_minus_b_sq_hbar_4,
        "D4. h^2 * hbar_q^4 (h=q-1/q)": delta_4_h_sq_hbar_4,
        "D5. hbar_q^4 * (q-1) * Vol(4_1)": delta_5_hbar_4_q_minus_1_vol,
        "D6. hbar_q^8 / Vol(4_1)": delta_6_hbar_8_over_vol,
        "D7. h^3 * hbar_q^2": delta_7_h_cubed_hbar_sq,
        "D8. b^2 * hbar_q^6 * (q-1) / 2": delta_8_b_sq_hbar_6_q_minus_1_over_2,
    }

    print("=" * 76)
    print(" m_μ categorical-correction first-probe — 8 δ(q₀) candidates")
    print("=" * 76)
    print(f"  q₀ = {mp.nstr(q_mp, 14)}")
    print(f"  Target δ ≈ {mp.nstr(target_delta, 8)}  (2.1e-7; closes 209.8 ppb miss)")
    print(f"  Tolerance: 10 ppm of target (2.1e-12 absolute) → m_μ at ≤10 ppb miss")
    print()

    results = {}
    any_pass = False
    best_err_rel = mpf("inf")
    best_name = None

    for name, formula in candidates.items():
        try:
            value = formula(q_mp)
            err_rel = float(abs(value - target_delta) / target_delta)
            err_ppm = err_rel * 1e6
            ok = err_ppm <= 10.0
            status = "PASS" if ok else "FAIL"
        except Exception as e:
            value = mpf("nan")
            err_rel = float("inf")
            err_ppm = float("inf")
            ok = False
            status = f"ERROR: {e}"

        print(f"  {name}")
        print(f"     δ_pred = {mp.nstr(value, 12):>22}  miss: {err_ppm:>12.2f} ppm  {status}")

        results[name] = {
            "computed_delta": mp.nstr(value, 30) if not mp.isnan(value) else "nan",
            "err_ppm_vs_target": err_ppm,
            "passed": ok,
        }
        if ok:
            any_pass = True
        if mpf(err_rel) < best_err_rel:
            best_err_rel = mpf(err_rel)
            best_name = name

    best_err_ppm = float(best_err_rel) * 1e6

    print()
    print("=" * 76)
    print(" VERDICT")
    print("=" * 76)
    print(f"  Best candidate: {best_name}  ({best_err_ppm:.2f} ppm)")
    print()
    if any_pass:
        print("  POSITIVE — at least one categorical correction matches the target δ")
        print("  within 10 ppm. This is a m_μ residue-correction candidate worth")
        print("  scaffolding into the Vol(4_1)/ℏ_q² production wiring.")
    else:
        print("  NEGATIVE — no natural categorical correction term lands within")
        print("  10 ppm of the target δ ≈ 2.1e-7. The 8 candidates were first-pass")
        print("  guesses spanning the ℏ_q^k × {h, b, q-1, Vol} natural combinations.")
        print()
        print("  Implication: the m_μ residue at proton-pinned q₀ is NOT well-")
        print("  captured by a simple closed-form categorical correction. Like")
        print("  Q_β residue A, m_μ closure may also require upstream-infra-gated")
        print("  search (different knot tower / Demazure crystal at lepton level)")
        print("  or formal acceptance as inherently bare-categorical-anchored.")

    wb.add_assertion(
        "mmu_categorical_correction_at_least_one_passes_10_ppm",
        computed=any_pass,
        expected=False,
        source="8 natural categorical corrections δ(q) tested at proton-pinned q₀ "
               "against the target δ ≈ 2.1e-7 (the residual to close the 209.8 ppb "
               "m_μ miss). PASS would identify a closed-form m_μ correction.",
    )

    wb.add_data("target_delta", mp.nstr(target_delta, 30))
    wb.add_data("q_substrate", mp.nstr(q_mp, 30))
    wb.add_data("vol_4_1", mp.nstr(vol_at("4_1"), 30))
    wb.add_data("candidates_tested", list(candidates.keys()))
    wb.add_data("per_candidate_results", results)
    wb.add_data("best_candidate_name", best_name)
    wb.add_data("best_candidate_err_ppm", best_err_ppm)
    wb.add_data("any_candidate_passes_10_ppm", any_pass)
    wb.add_data("interpretation", (
        f"m_μ categorical-correction first-probe: 8 closed-form δ(q) candidates "
        f"tested at proton-pinned q₀ against target δ ≈ 2.1e-7. Best: "
        f"'{best_name}' at {best_err_ppm:.2f} ppm. "
        + ("POSITIVE — closed-form m_μ correction candidate identified."
           if any_pass else
           "NEGATIVE — no simple categorical correction matches. m_μ residue "
           "likely requires upstream-infra-gated search or formal bare-anchored "
           "acceptance, paralleling Q_β residue A.")
    ))

    out = wb.save()
    print()
    print(f"✓ Witness: {out.name}  ({len(wb.assertions)} assertions, "
          f"all {'passed' if all(a.passed for a in wb.assertions) else 'FAILED'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
