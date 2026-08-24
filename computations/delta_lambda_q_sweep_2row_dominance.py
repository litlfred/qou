#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical mpmath consumer; symbolic chi
# polynomials live upstream in chi-deuteron-h6.witness.json.
"""Test the SU(2) restriction hypothesis: do > 2-row Wedderburn block
contributions vanish at q → 1?

The 2-row stratum analysis (delta_lambda_2row_stratum_analysis) found
that the 2-row sector carries 83-95% of |tr_M(β_K)| at q = q_0.  The
remaining 5-17% comes from > 2-row partitions.

Schur-Weyl duality at q = 1: the irreducible H_n(1) = ℂ[S_n]
components in V^⊗n with V = ℂ^2 are exactly the partitions with
≤ 2 rows.  If the atomic braid β_K lives effectively in V^⊗n
with V = ℂ^2, the > 2-row contributions should VANISH at q = 1
(modulo deformation that picks up > 2-row content for q ≠ 1).

This script sweeps q ∈ {1.001, 1.01, 1.05, q_0} for the deuteron
β_D ∈ H_6 (the smallest case where this is fast) and reports:
  - the > 2-row sector fraction at each q,
  - whether the fraction → 0 as q → 1.

If the fraction → 0, that's structural confirmation that the
2-row stratum is the natural categorical home for atomic-braid
Markov traces.

Output: `delta-lambda-q-sweep-2row.witness.json`.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from q_parameter import Q_MP  # noqa: E402

Q0_FLOAT = float(Q_MP)


def split_2row_vs_gt(rows: list[dict]) -> tuple[float, float, list[dict]]:
    """Split per-partition contributions by row count, return
    (mass_2row, mass_gt_2row, full_table)."""
    m2 = 0.0
    mgt = 0.0
    for r in rows:
        c = abs(float(r["chi_q_at_q0"]) * float(r["y_at_q0"]))
        n_rows = len(r["partition"])
        if n_rows <= 2:
            m2 += c
        else:
            mgt += c
    return m2, mgt, rows


def main() -> int:
    # Construct WitnessBuilder up front to capture full durationMs
    # (Copilot PR #619 review). Engine "python": the q-sweep uses
    # global_wedderburn_sum_q_hecke_seminormal (float64 Hoefsmit numpy).
    from witness_base import WitnessBuilder
    w = (WitnessBuilder("delta-lambda-q-sweep-2row", engine="python")
         .set_description(
            "q-sweep for deuteron (n=6) testing whether the > 2-row "
            "Wedderburn sector contribution vanishes as q → 1.  If yes, "
            "the 2-row stratum dominance found in the Δ_λ tabulation is "
            "the q-deformation of the Schur-Weyl restriction to V = ℂ² "
            "(SU(2) fundamental), with the > 2-row content being a "
            "deformation-induced correction that vanishes at q = 1.  "
            "Numeric path: float64 (numpy/Hoefsmit)."
         )
         .set_content_block("prop:rho-k-h3a-refinement"))

    print("=" * 96)
    print("  Δ_λ q-sweep: does > 2-row sector vanish at q → 1?")
    print("=" * 96)

    from wedderburn_jones_markov import global_wedderburn_sum_q_hecke_seminormal

    # Test points: small q-1 values approaching 1 + the substrate q_0
    q_values = [1.001, 1.01, 1.05, 1.10, Q0_FLOAT]

    # Deuteron only (n=6, fast).
    Z, N = 1, 1
    print(f"\n  Atom: deuteron (Z={Z}, N={N}, n=6); 11 partitions of 6")

    sweep_results = []
    print(f"\n  {'q':>10}{'q-1':>12}{'|tr_M|':>14}{'2-row mass':>14}"
          f"{'>2-row mass':>14}{'>2-row %':>12}")
    print("  " + "-" * 80)
    for q in q_values:
        t0 = time.time()
        try:
            tr_M_total, terms = global_wedderburn_sum_q_hecke_seminormal(
                Z=Z, N=N, q_val=q
            )
        except Exception as exc:
            print(f"  q={q}: ERROR {type(exc).__name__}: {exc}")
            continue
        elapsed = time.time() - t0
        abs_tr_M = abs(float(tr_M_total))
        m2, mgt, _ = split_2row_vs_gt(terms)
        mass_total = m2 + mgt
        frac_gt = mgt / mass_total if mass_total > 0 else 0
        print(f"  {q:>10.6f}{q-1:>12.6f}{abs_tr_M:>14.10f}{m2:>14.10f}"
              f"{mgt:>14.10f}{frac_gt*100:>11.4f}%")
        sweep_results.append({
            "q": q,
            "q_minus_1": q - 1,
            "abs_tr_M": abs_tr_M,
            "mass_2row": m2,
            "mass_gt_2row": mgt,
            "frac_gt_2row": frac_gt,
            "elapsed_sec": elapsed,
            "per_partition": [
                {"partition": r["partition"],
                 "y": float(r["y_at_q0"]),
                 "chi": float(r["chi_q_at_q0"]),
                 "n_rows": len(r["partition"])}
                for r in terms
            ],
        })

    # Verdict
    print(f"\n  Limit analysis:")
    if len(sweep_results) >= 2:
        smallest_q_minus_1 = min(s["q_minus_1"] for s in sweep_results)
        smallest_entry = next(s for s in sweep_results
                              if s["q_minus_1"] == smallest_q_minus_1)
        largest_entry = max(sweep_results, key=lambda s: s["q_minus_1"])
        print(f"    smallest q-1 tested: {smallest_q_minus_1}")
        print(f"      > 2-row mass at q={smallest_entry['q']}: "
              f"{smallest_entry['mass_gt_2row']:.6e} "
              f"({smallest_entry['frac_gt_2row']*100:.4f}%)")
        print(f"    largest q-1 tested: {largest_entry['q_minus_1']}")
        print(f"      > 2-row mass at q={largest_entry['q']}: "
              f"{largest_entry['mass_gt_2row']:.6e} "
              f"({largest_entry['frac_gt_2row']*100:.4f}%)")

        # Compute scaling exponent: log(mass_gt) / log(q-1)
        if smallest_entry["mass_gt_2row"] > 1e-30 and smallest_entry["q_minus_1"] > 0:
            from math import log
            ratio_mass = log(largest_entry["mass_gt_2row"] /
                             smallest_entry["mass_gt_2row"])
            ratio_qm1 = log(largest_entry["q_minus_1"] /
                            smallest_entry["q_minus_1"])
            if abs(ratio_qm1) > 1e-9:
                scaling_exp = ratio_mass / ratio_qm1
                print(f"\n    Empirical scaling: > 2-row mass ∝ (q-1)^{scaling_exp:.3f}")
                print(f"      (positive exponent ⇒ vanishes at q=1; ")
                print(f"       negative ⇒ stays finite or grows)")
                if scaling_exp > 0.5:
                    print(f"\n    ✅ HYPOTHESIS CONFIRMED: > 2-row mass scales like "
                          f"(q-1)^{scaling_exp:.2f} → 0 as q → 1.")
                    print(f"       The 2-row stratum is the q→1 limit's natural "
                          f"categorical home (consistent with SU(2) Schur-Weyl).")
                    verdict = "confirmed"
                elif scaling_exp > 0:
                    print(f"\n    ✓ HYPOTHESIS WEAKLY SUPPORTED: > 2-row mass "
                          f"vanishes slowly (∝ (q-1)^{scaling_exp:.2f}).")
                    verdict = "weakly_supported"
                else:
                    print(f"\n    ✗ HYPOTHESIS REFUTED: > 2-row mass does NOT vanish at q=1.")
                    verdict = "refuted"
            else:
                verdict = "indeterminate"
        else:
            verdict = "indeterminate"
    else:
        verdict = "insufficient_data"

    # WitnessBuilder constructed at start of main(); now populate.
    w.parameters.update({
        "atom": "deuteron",
        "Z": 1, "N": 1, "n": 6,
        "q_values_swept": q_values,
        "n_partitions": 11,
    })
    w.add_data("sweep", sweep_results)
    w.add_data("verdict", verdict)
    w.add_data("reference_blocks", [
        "prop:rho-k-h3a-refinement",
        "prop:categorical-mass-markov",
    ])
    out = w.save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
