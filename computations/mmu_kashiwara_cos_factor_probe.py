#!/usr/bin/env python3
"""mmu_kashiwara_cos_factor_probe.py — m_μ Kashiwara cos factor probe.

Pivot from the closed-form δ family (30 candidates, all NEGATIVE, see
PRs #1781 + commits) to a Kashiwara cos-factor structure paralleling
the Q_β N1_factor `cos(α - bℏ²/2)`:

    m_μ_pred = m_e × Vol(4_1) / ℏ_q² × cos(η_μ(q))

The needed correction `1 - cos(η_μ) = 2.1e-7` requires η_μ ≈ 6.5e-4 rad
at proton-pinned q₀.

Natural Kashiwara/categorical angle candidates at the right scale:

  H1.  α × ℏ_q (Kashiwara α scaled)
  H2.  α × ℏ_q²
  H3.  α × ℏ_q³
  H4.  (α - bℏ²/2) × ℏ_q  (Q_β N1 angle scaled)
  H5.  (α - bℏ²/2) × ℏ_q²
  H6.  ℏ_q^3 × b  (pure dimensionless)
  H7.  ℏ_q^4 × √(b² + 1)
  H8.  α × b · ℏ_q²
  H9.  h × ℏ_q² (h = q - q⁻¹)
  H10. h × ℏ_q³

For each, compute `1 - cos(η)` and compare to target δ = 2.098e-7.

Kashiwara form precedent: Q_β N1_factor = cos(α - bℏ²/2) is canonical
in `QBetaCategoricalPrecisionLadder.lean:67-68`. If a parallel
m_μ N1-like factor lands within 10 ppm, this is a STRUCTURAL HIT.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401

from mpmath import mp, mpf, sqrt, cos  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402


def hoefsmit_b(q: mpf) -> mpf:
    h = q - 1 / q
    return sqrt((h ** 2 + 3) / (h ** 2 + 4))


def alpha_kashiwara(q: mpf) -> mpf:
    """α = (z - 1) * h / 2 per QBetaCategoricalPrecisionLadder."""
    z = q**3 / (q**2 + 1)
    h = q - 1 / q
    return (z - 1) * h / 2


def angle_h1(q: mpf) -> mpf:
    return alpha_kashiwara(q) * ((q - 1) / q)


def angle_h2(q: mpf) -> mpf:
    return alpha_kashiwara(q) * ((q - 1) / q) ** 2


def angle_h3(q: mpf) -> mpf:
    return alpha_kashiwara(q) * ((q - 1) / q) ** 3


def angle_h4(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return (alpha_kashiwara(q) - hoefsmit_b(q) * hbar ** 2 / 2) * hbar


def angle_h5(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return (alpha_kashiwara(q) - hoefsmit_b(q) * hbar ** 2 / 2) * hbar ** 2


def angle_h6(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return hbar ** 3 * hoefsmit_b(q)


def angle_h7(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return hbar ** 4 * sqrt(hoefsmit_b(q) ** 2 + 1)


def angle_h8(q: mpf) -> mpf:
    hbar = (q - 1) / q
    return alpha_kashiwara(q) * hoefsmit_b(q) * hbar ** 2


def angle_h9(q: mpf) -> mpf:
    hbar = (q - 1) / q
    h = q - 1 / q
    return h * hbar ** 2


def angle_h10(q: mpf) -> mpf:
    hbar = (q - 1) / q
    h = q - 1 / q
    return h * hbar ** 3


def main() -> int:
    set_compute_dps()
    wb = WitnessBuilder("mmu-kashiwara-cos-factor-probe", engine="mpmath")

    q_mp = Q_MP
    target_delta = mpf("2.098e-7")

    candidates = {
        "H1.  alpha * hbar_q": angle_h1,
        "H2.  alpha * hbar_q^2": angle_h2,
        "H3.  alpha * hbar_q^3": angle_h3,
        "H4.  (alpha - b*hbar^2/2) * hbar_q  (Q_β-N1 scaled)": angle_h4,
        "H5.  (alpha - b*hbar^2/2) * hbar_q^2": angle_h5,
        "H6.  hbar_q^3 * b": angle_h6,
        "H7.  hbar_q^4 * sqrt(b^2 + 1)": angle_h7,
        "H8.  alpha * b * hbar_q^2": angle_h8,
        "H9.  h * hbar_q^2  (h = q - q^-1)": angle_h9,
        "H10. h * hbar_q^3": angle_h10,
    }

    print("=" * 76)
    print(" m_μ Kashiwara cos-factor probe — 10 candidate angles η_μ(q)")
    print("=" * 76)
    print(f"  q₀ = {mp.nstr(q_mp, 14)}")
    print(f"  Target δ = 1 - cos(η_μ) = {mp.nstr(target_delta, 8)}")
    print(f"  Required η_μ ≈ 6.48e-4 rad")
    print()

    results = {}
    any_pass = False
    best_err_rel = mpf("inf")
    best_name = None

    for name, formula in candidates.items():
        try:
            eta = formula(q_mp)
            value = 1 - cos(eta)  # the actual δ from the cos factor
            err_rel = abs(value - target_delta) / target_delta
            err_ppm = float(err_rel) * 1e6
            ok = err_ppm <= 10.0
            status = "PASS" if ok else "FAIL"
        except Exception as e:
            value = mpf("nan")
            eta = mpf("nan")
            err_rel = mpf("inf")
            err_ppm = float("inf")
            ok = False
            status = f"ERROR: {e}"

        print(f"  {name}")
        print(f"     eta = {mp.nstr(eta, 12):>18}  delta = 1-cos = {mp.nstr(value, 12):>22}  miss: {err_ppm:>14.2f} ppm  {status}")

        results[name] = {
            "computed_eta": mp.nstr(eta, 30) if not mp.isnan(eta) else "nan",
            "computed_delta_from_cos": mp.nstr(value, 30) if not mp.isnan(value) else "nan",
            "err_ppm_vs_target_delta": err_ppm,
            "passed": ok,
        }
        if ok:
            any_pass = True
        if err_rel < best_err_rel:
            best_err_rel = err_rel
            best_name = name

    best_err_ppm = float(best_err_rel) * 1e6

    print()
    print("=" * 76)
    print(" VERDICT")
    print("=" * 76)
    print(f"  Best candidate: {best_name}  ({best_err_ppm:.2f} ppm)")
    print()
    if any_pass:
        print("  POSITIVE — Kashiwara cos-factor candidate matches within 10 ppm.")
        print("  This is a STRUCTURAL HIT paralleling Q_β's N1_factor.")
    else:
        print("  NEGATIVE — no Kashiwara cos-factor angle reproduces target δ.")
        print()
        print(f"  Cumulative m_μ NEGATIVE bracket: 30 + 10 = 40 candidates.")
        print("  Best so far: R9 hbar_q^6 * q / 5 at 1,152 ppm (closed-form family)")

    wb.add_assertion(
        "kashiwara_cos_at_least_one_passes_10_ppm",
        computed=any_pass,
        expected=False,
        source="10 Kashiwara cos-factor angles η_μ(q) tested at proton-pinned q₀ "
               "against the target δ = 1 - cos(η_μ) = 2.098e-7. PASS would identify "
               "an m_μ N1-like factor paralleling Q_β.",
    )

    wb.add_data("target_delta", mp.nstr(target_delta, 30))
    wb.add_data("q_substrate", mp.nstr(q_mp, 30))
    wb.add_data("candidates_tested", list(candidates.keys()))
    wb.add_data("per_candidate_results", results)
    wb.add_data("best_candidate_name", best_name)
    wb.add_data("best_candidate_err_ppm", best_err_ppm)
    wb.add_data("any_candidate_passes_10_ppm", any_pass)

    out = wb.save()
    print()
    print(f"✓ Witness: {out.name}  ({len(wb.assertions)} assertions, "
          f"all {'passed' if all(a.passed for a in wb.assertions) else 'FAILED'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
