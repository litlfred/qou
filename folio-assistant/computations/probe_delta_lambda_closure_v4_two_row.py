"""Δ_λ closure v4 — restrict to 2-row partitions (HasTwoRowProjection stratum).

v3 showed the numerically-dominant partitions in Σ_λ y·χ are 2-row
([n−k, k]). The crystal-pole filter captures ~45% of the full sum
(ratio ~2.2), with the missing ~55% from non-crystal-leading 2-row
partitions.

This probe tests whether RESTRICTING to 2-row partitions only
yields a stable Δ_const closure, motivated by the
HasTwoRowProjection theorem (PR #657): the categorical density
ρ_K is a finite linear combination of |χ^λ|² over 2-row
λ = [n−k, k] for 0 ≤ k ≤ ⌊n/2⌋.

For each atom K, compute:
  Σ_2row = Σ_(λ=[n−k, k], 0 ≤ k ≤ ⌊n/2⌋) y_λ · χ^λ(β_K)
  Δ_2row = (binding/m_e) / Σ_2row

Compare with Δ_full from v3.

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

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

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


M_CODATA = {
    "D": float(M_D_MEV_VALIDATION), "T": float(M_T_MEV_VALIDATION),
    "3He": float(M_HE3_MEV_VALIDATION), "4He": float(M_HE4_MEV_VALIDATION),
}


def is_two_row(lam: tuple[int, ...]) -> bool:
    """λ = [n−k, k] with 1 ≤ k ≤ ⌊n/2⌋, or single-row [n]."""
    if len(lam) == 1:
        return True
    if len(lam) == 2:
        return True
    return False


def main() -> int:
    mp.mp.dps = 50
    q_val = float(Q_0_FLOAT)
    m_e = float(M_E_MEV)
    m_p = float(M_P_MEV_VALIDATION)
    m_n = float(M_N_MEV_VALIDATION)

    print("=" * 100)
    print("  Δ_λ closure v4 — restrict to 2-row stratum (HasTwoRowProjection)")
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

        y_vals = y_lambda_at(n_strands, q_val=q_val)

        two_row_records = []
        all_sum = 0.0
        two_row_sum = 0.0

        for lam, y in y_vals.items():
            sigmas, dim, _ = build_seminormal_matrices(lam, q=q_val)
            chi_f = 0.0 if dim == 0 else float(
                chi_lambda_of_word(sigmas, dim, word, n_gens)
            )
            y_f = float(y)
            y_chi = y_f * chi_f
            all_sum += y_chi
            if is_two_row(lam):
                two_row_sum += y_chi
                two_row_records.append({
                    "lambda": list(lam),
                    "y_at_q0": y_f,
                    "chi_at_q0": chi_f,
                    "y_times_chi": y_chi,
                })

        two_row_records.sort(key=lambda r: -abs(r["y_times_chi"]))

        if abs(two_row_sum) > 1e-30:
            delta_2row = target / two_row_sum
        else:
            delta_2row = None
        if abs(all_sum) > 1e-30:
            delta_full = target / all_sum
        else:
            delta_full = None
        two_row_pct = (two_row_sum / all_sum * 100
                       if abs(all_sum) > 1e-30 else None)

        print(f"  ── {label} (Z={Z}, N={N}, A={A}, n={n_strands}, "
              f"#2-row={len(two_row_records)}) ──")
        print(f"  binding/m_e = {target:+.6f}")
        print(f"  Σ_all   = {all_sum:+.6e}   Δ_full  = "
              f"{delta_full:+.4f}" if delta_full is not None else
              f"  Σ_all   = {all_sum:+.6e}   Δ_full  = (undef)")
        print(f"  Σ_2row  = {two_row_sum:+.6e}   Δ_2row  = "
              f"{delta_2row:+.4f}" if delta_2row is not None else
              f"  Σ_2row  = {two_row_sum:+.6e}   Δ_2row  = (undef)")
        if two_row_pct is not None:
            print(f"  2-row captures {two_row_pct:.2f}% of full sum")
        print()
        print(f"  2-row partitions ranked by |y·χ|:")
        for r in two_row_records:
            print(f"    λ={str(r['lambda']):<20}  y·χ={r['y_times_chi']:+.6e}")
        print()

        rows.append({
            "atom": label, "Z": Z, "N": N, "A": A, "n_strands": n_strands,
            "n_two_row": len(two_row_records),
            "binding_MeV": binding, "target": target,
            "sum_all": all_sum, "sum_two_row": two_row_sum,
            "two_row_pct_of_full": two_row_pct,
            "Delta_full": delta_full, "Delta_two_row": delta_2row,
            "two_row_records": two_row_records,
        })

    # Summary — look for stability across atoms
    print("=" * 100)
    print("  Δ closure v4 — does Δ_2row stabilize across atoms?")
    print("=" * 100)
    print(f"  {'atom':>5} {'binding/m_e':>13} {'Δ_2row':>10} "
          f"{'Δ_full':>10} {'2row %':>9} {'Δ_2row/A²':>11}")
    print("  " + "-" * 80)
    for r in rows:
        d2 = f"{r['Delta_two_row']:+.4f}" if r['Delta_two_row'] is not None else "—"
        df = f"{r['Delta_full']:+.4f}" if r['Delta_full'] is not None else "—"
        pct = f"{r['two_row_pct_of_full']:.2f}" if r['two_row_pct_of_full'] is not None else "—"
        a2 = (r['Delta_two_row'] / (r['A'] ** 2)
              if r['Delta_two_row'] is not None else None)
        a2s = f"{a2:+.4f}" if a2 is not None else "—"
        print(f"  {r['atom']:>5} {r['target']:>+13.6f} {d2:>10} "
              f"{df:>10} {pct:>9} {a2s:>11}")
    print()

    builder = (
        WitnessBuilder("delta-lambda-closure-v4-two-row",
                       engine="numpy+scipy")
        .set_description(
            "Δ_λ closure v4: restrict the leading-order Σ_λ y_λ·χ^λ·Δ "
            "to 2-row partitions only (λ = [n−k, k]), motivated by "
            "HasTwoRowProjection (PR #657's two-row projection theorem). "
            "Tests stability of Δ_const across atoms when the categorical "
            "density ρ_K is restricted to its 2-row stratum."
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
