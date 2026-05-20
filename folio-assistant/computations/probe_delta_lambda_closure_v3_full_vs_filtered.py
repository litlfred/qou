"""Δ_λ closure v3 — compare full vs filtered (crystal, combined) summations.

v1 (per-partition shift_NF) gave Δ_uniform = -41/-351/-162/-2148 for D/T/³He/⁴He
   (#leading = 7/22/22/63 — too coarse, all crystal-shift-max partitions).
v2 (combined crystal+Wenzl pole) gave Δ_uniform = -15/+2.5M/+2.4M/+3.1M
   (#leading = 2/2/2/12 — tighter, but Σ y·χ → 0 cancellation for heavier atoms).

v3 (this probe) ADDS the **no filter** column: Σ_(ALL λ ⊢ 3A) y_λ·χ^λ
to see whether the UNFILTERED constant-Δ ansatz gives a stable
binding-energy fit, and to quantify how much each filter "wastes"
or "improves" via inclusion of subdominant partitions.

For each atom:
  Δ_full = (binding/m_e) / Σ_(ALL λ) y_λ·χ^λ
  Δ_crystal = (binding/m_e) / Σ_(crystal-leading λ) y_λ·χ^λ
  Δ_combined = (binding/m_e) / Σ_(combined-leading λ) y_λ·χ^λ

Hypothesis: the full sum Σ_(ALL) is dominated by the
**numerically-dominant** partitions (often two-row, non-column),
which are NOT the pole-leading column-like partitions. The full
sum should give a more stable Δ_const than either filter.

CLASS-A acknowledged-anchor banner (per Workplan-0b/M_N):
This script imports M_*_MEV_VALIDATION constants from
`codata_constants.py` as production inputs (not just as
comparison targets).  M_N is currently a CLASS-A acknowledged-
stub anchor pending its own substrate derivation — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`
for the open spec.  Until that lands, the calibration-discipline
audit (`canonical-script-input-audit`) classifies this script
as "with-substrate-splitting" or "anchor-pending"; reviewers
should treat the M_*_MEV_VALIDATION usage as CAL-3-ish anchor,
NOT as an independent calibration input.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
from syt_prefix_cache import BlockCache

from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import (  # noqa: E402
    M_E_MEV,
    M_P_MEV_VALIDATION, M_N_MEV_VALIDATION,
    M_D_MEV_VALIDATION, M_T_MEV_VALIDATION,
    M_HE3_MEV_VALIDATION, M_HE4_MEV_VALIDATION,
)
from mass_at_3A_proper import atom_braid_word_3A, chi_lambda_of_word  # noqa: E402
from hecke_characters import build_seminormal_matrices  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q as Q_0_FLOAT  # noqa: E402
from crystal_shift_nf_atomic import crystal_shift_nf  # noqa: E402


M_CODATA = {
    "D": float(M_D_MEV_VALIDATION), "T": float(M_T_MEV_VALIDATION),
    "3He": float(M_HE3_MEV_VALIDATION), "4He": float(M_HE4_MEV_VALIDATION),
}


def main() -> int:
    mp.mp.dps = 50
    q_val = float(Q_0_FLOAT)
    m_e = float(M_E_MEV)
    m_p = float(M_P_MEV_VALIDATION)
    m_n = float(M_N_MEV_VALIDATION)

    pole_cache = json.loads(
        (HERE / "y-lambda-pole-order-cache.json").read_text()
    )

    print("=" * 100)
    print("  Δ_λ closure v3 — full vs crystal vs combined-pole filters")
    print("=" * 100)
    print()

    atoms = [
        ("D",   1, 1),
        ("T",   1, 2),
        ("3He", 2, 1),
        ("4He", 2, 2),
    ]

    rows = []
    for label, Z, N in atoms:
        A = Z + N
        n_strands = 3 * A
        n_gens = n_strands - 1
        word = atom_braid_word_3A(Z, N, include_inter=True)
        binding = M_CODATA[label] - (Z * m_p + N * m_n)
        target = binding / m_e

        sh = crystal_shift_nf(word, n_strands)
        crystal_per_lam = sh["shift_per_lam"]
        crystal_max = max(crystal_per_lam.values())

        n_key = str(n_strands)
        ord_y_cache = {}
        for entry in pole_cache.get("by_n", {}).get(n_key, {}).get("partitions", []):
            shape = tuple(entry["partition"])
            ord_y_cache[shape] = entry.get("ord_y_at_u_eq_0", 0)

        combined_per_lam = {}
        for lam, c_shift in crystal_per_lam.items():
            combined_per_lam[lam] = c_shift - 2 * ord_y_cache.get(lam, 0)
        combined_max = max(combined_per_lam.values())

        # Compute y·χ for EVERY partition of n_strands
        y_vals = y_lambda_at(n_strands, q_val=q_val)
        all_records = []
        for lam, y in y_vals.items():
            sigmas, dim, _ = build_seminormal_matrices(lam, q=q_val)
            chi_f = 0.0 if dim == 0 else float(
                chi_lambda_of_word(sigmas, dim, word, n_gens)
            )
            y_f = float(y)
            all_records.append({
                "lambda": list(lam),
                "crystal_shift": crystal_per_lam.get(lam, 0),
                "ord_y_u": ord_y_cache.get(lam, 0),
                "combined_pole": combined_per_lam.get(lam, 0),
                "y_at_q0": y_f, "chi_at_q0": chi_f,
                "y_times_chi": y_f * chi_f,
            })

        sum_all = sum(r["y_times_chi"] for r in all_records)
        sum_crystal = sum(
            r["y_times_chi"] for r in all_records
            if r["crystal_shift"] == crystal_max
        )
        sum_combined = sum(
            r["y_times_chi"] for r in all_records
            if r["combined_pole"] == combined_max
        )

        def safe_div(num, den, tol=1e-30):
            return num / den if abs(den) > tol else None

        delta_full = safe_div(target, sum_all)
        delta_crystal = safe_div(target, sum_crystal)
        delta_combined = safe_div(target, sum_combined)

        # Numerically dominant partitions (top-5 by |y·χ|)
        all_records.sort(key=lambda r: -abs(r["y_times_chi"]))
        top5 = all_records[:5]

        print(f"  ── {label} (Z={Z}, N={N}, A={A}, n={n_strands}, "
              f"#part={len(all_records)}) ──")
        print(f"  binding/m_e = {target:+.6f}")
        print(f"  crystal_max = {crystal_max}  combined_max = {combined_max}")
        print(f"  Σ_all          = {sum_all:+.6e}  → Δ_full     = "
              f"{delta_full:+.4f}" if delta_full is not None else
              f"  Σ_all          = {sum_all:+.6e}  → Δ_full     = (undef)")
        print(f"  Σ_crystal-max  = {sum_crystal:+.6e}  → Δ_crystal  = "
              f"{delta_crystal:+.4f}" if delta_crystal is not None else
              f"  Σ_crystal-max  = {sum_crystal:+.6e}  → Δ_crystal  = (undef)")
        print(f"  Σ_combined-max = {sum_combined:+.6e}  → Δ_combined = "
              f"{delta_combined:+.4f}" if delta_combined is not None else
              f"  Σ_combined-max = {sum_combined:+.6e}  → Δ_combined = (undef)")

        print(f"  Numerically-dominant partitions (top-5 by |y·χ|):")
        for r in top5:
            print(f"    λ={str(r['lambda']):<20}  c-shift={r['crystal_shift']:>3}  "
                  f"ord_y_u={r['ord_y_u']:>2}  combined={r['combined_pole']:>3}  "
                  f"y·χ={r['y_times_chi']:+.6e}")
        print()

        rows.append({
            "atom": label, "Z": Z, "N": N, "A": A, "n_strands": n_strands,
            "n_partitions": len(all_records),
            "binding_MeV": binding, "target": target,
            "crystal_max": crystal_max, "combined_max": combined_max,
            "sum_all": sum_all,
            "sum_crystal_max": sum_crystal,
            "sum_combined_max": sum_combined,
            "Delta_full": delta_full,
            "Delta_crystal": delta_crystal,
            "Delta_combined": delta_combined,
            "top5_by_abs_y_chi": top5,
        })

    # Summary
    print("=" * 100)
    print("  Δ closure v3 — summary")
    print("=" * 100)
    print(f"  {'atom':>5} {'binding/m_e':>13} "
          f"{'Δ_full':>10} {'Δ_crystal':>11} {'Δ_combined':>12}  "
          f"{'ratio cryst/full':>16}")
    print("  " + "-" * 80)
    for r in rows:
        df = f"{r['Delta_full']:+.4f}" if r['Delta_full'] is not None else "—"
        dc = f"{r['Delta_crystal']:+.4f}" if r['Delta_crystal'] is not None else "—"
        dcomb = f"{r['Delta_combined']:+.4f}" if r['Delta_combined'] is not None else "—"
        ratio = (r['Delta_crystal'] / r['Delta_full']
                 if r['Delta_full'] is not None and r['Delta_crystal'] is not None
                 and abs(r['Delta_full']) > 1e-30 else None)
        ratio_s = f"{ratio:+.4f}" if ratio is not None else "—"
        print(f"  {r['atom']:>5} {r['target']:>+13.6f} "
              f"{df:>10} {dc:>11} {dcomb:>12}  {ratio_s:>16}")
    print()

    builder = (
        WitnessBuilder("delta-lambda-closure-v3-full-vs-filtered",
                       engine="numpy+scipy")
        .set_description(
            "Δ_λ closure v3: compare unfiltered Σ_(ALL λ) y·χ vs "
            "crystal-shift-max filter vs combined-pole filter (v1/v2). "
            "Tests whether numerically-dominant partitions (often "
            "non-column-like, with O(1) y·χ) carry the binding-energy "
            "signal that the pole-order filters miss."
        )
        .set_content_block("prop:rho-k-h3a-refinement")
        .add_parameter("q_0", q_val)
        .add_data("rows", rows)
    )
    out = builder.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
