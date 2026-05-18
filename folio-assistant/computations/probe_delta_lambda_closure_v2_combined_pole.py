"""Δ_λ closure v2 — combined per-λ pole order (crystal-shift + y_λ Wenzl pole).

Refines `probe_delta_lambda_per_partition_shift_nf_closure.py` by using
the COMBINED per-λ pole order at q=0:

  combined_pole_λ = crystal_shift_λ + ord_y_λ (in q units)

where:
  crystal_shift_λ — from crystal_shift_nf.shift_per_lam (per λ, SYT-max)
  ord_y_λ         — from y-lambda-pole-order-cache.json (Wenzl-bridge)

Note: cache stores ord_y_at_u_eq_0 in u=q² coordinates. The q-power
pole is 2 × ord_u, but y_λ tends to be a *zero* (positive power) at
q=0, so contributes -ord_y_λ to the leading pole order (in absolute
terms, larger ord_y → less leading-pole-y_λ contribution).

## Filter

The full Habiro shift per atom is shift_NF(Z, N) = 18Z + 21N + 1.
The contributing partitions for the LEADING order are those whose
combined pole order at q=0 matches the maximum.

This probe:
1. For each atom, compute crystal_shift_λ (= crystal_shift_nf.shift_per_lam[λ])
2. Look up ord_y_λ from cache for each λ
3. Compute per-λ combined-leading-pole = crystal_shift_λ - ord_y_λ
   (subtraction because y_λ is a zero at q=0, suppresses pole)
4. Filter to partitions achieving the max combined-leading-pole
5. Solve Δ_uniform = binding / (m_e · Σ_(filtered) y · χ)

## Status

The empirical 18Z + 21N + 1 closed form for shift_NF is verified at
A = 2..4 by SYT enumeration in `crystal_shift_nf`. Beyond, it's
extrapolated. For ⁴He (A=4): shift_NF = 79 = 2·(47 − 7.5) — but
7.5 is half-integer, so the cancellation goes to a fractional pole
order. The combined-leading-pole filter is therefore approximate.

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
    "p": float(M_P_MEV_VALIDATION), "n": float(M_N_MEV_VALIDATION),
    "D": float(M_D_MEV_VALIDATION), "T": float(M_T_MEV_VALIDATION),
    "3He": float(M_HE3_MEV_VALIDATION), "4He": float(M_HE4_MEV_VALIDATION),
}


def main() -> int:
    mp.mp.dps = 50
    q_val = float(Q_0_FLOAT)
    m_e = float(M_E_MEV)
    m_p = float(M_P_MEV_VALIDATION)
    m_n = float(M_N_MEV_VALIDATION)

    # Load y_λ pole-order cache
    pole_cache = json.loads(
        (HERE / "y-lambda-pole-order-cache.json").read_text()
    )

    print("=" * 90)
    print("  Δ_λ closure v2 — combined per-λ pole (crystal-shift + y-Wenzl)")
    print("=" * 90)
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
        full_shift_nf = 18 * Z + 21 * N + 1

        sh = crystal_shift_nf(word, n_strands)
        crystal_per_lam = sh["shift_per_lam"]  # {λ tuple: int}

        # y_λ pole orders from cache (in u = q² coords; convert to q)
        n_key = str(n_strands)
        ord_y_cache = {}
        for entry in pole_cache.get("by_n", {}).get(n_key, {}).get("partitions", []):
            shape = tuple(entry["partition"])
            ord_y_cache[shape] = entry.get("ord_y_at_u_eq_0", 0)

        # Combined per-λ leading pole at q=0:
        #   combined_λ = crystal_shift_λ − ord_y_λ_at_q (=2·ord_y_at_u)
        # (subtraction because y_λ zero suppresses the pole)
        combined_per_lam = {}
        for lam, c_shift in crystal_per_lam.items():
            ord_y_u = ord_y_cache.get(lam, 0)
            ord_y_q = 2 * ord_y_u  # u = q² ⇒ q-power = 2·u-power
            combined_per_lam[lam] = c_shift - ord_y_q

        max_combined = max(combined_per_lam.values())
        leading_combined = [
            lam for lam, v in combined_per_lam.items() if v == max_combined
        ]

        # ALSO: filter for partitions matching full_shift_nf if possible
        # (the script's crystal_shift max should be related to the per-A
        # closed-form 12A-1, and combined_per_lam max may match
        # shift_NF − cancellation_offset.)

        print(f"  ── {label} (Z={Z}, N={N}, A={A}, n={n_strands}) ──")
        print(f"  full shift_NF = 18Z + 21N + 1 = {full_shift_nf}")
        print(f"  crystal-shift max = {max(crystal_per_lam.values())}")
        print(f"  combined-pole max = {max_combined}")
        print(f"  # leading (crystal alone) = "
              f"{sum(1 for v in crystal_per_lam.values() if v == max(crystal_per_lam.values()))}")
        print(f"  # leading (combined)      = {len(leading_combined)}")
        print(f"  binding(K) = {binding:+.6f} MeV")
        print()

        y_vals = y_lambda_at(n_strands, q_val=q_val)
        print(f"  Top-5 leading-combined partitions:")
        print(f"  {'λ':>15} {'c-shift':>8} {'ord_y':>6} {'combined':>9} "
              f"{'y_λ(q_0)':>14} {'χ^λ(β_K)':>14} {'y·χ':>14}")
        print("  " + "-" * 90)

        # Sort leading partitions by |y·χ| to highlight dominant
        leading_records = []
        for lam in leading_combined:
            y = y_vals.get(lam, mp.mpf(0))
            sigmas, dim, _ = build_seminormal_matrices(lam, q=q_val)
            chi_f = 0.0 if dim == 0 else float(
                chi_lambda_of_word(sigmas, dim, word, n_gens)
            )
            y_f = float(y)
            y_chi = y_f * chi_f
            leading_records.append({
                "lambda": list(lam),
                "crystal_shift": crystal_per_lam[lam],
                "ord_y_u": ord_y_cache.get(lam, 0),
                "combined_pole": combined_per_lam[lam],
                "y_at_q0": y_f, "chi_at_q0": chi_f,
                "y_times_chi": y_chi,
            })
        leading_records.sort(key=lambda r: -abs(r["y_times_chi"]))
        for r in leading_records[:5]:
            print(f"  {str(r['lambda']):>15} {r['crystal_shift']:>8} "
                  f"{r['ord_y_u']:>6} {r['combined_pole']:>9} "
                  f"{r['y_at_q0']:>+14.6e} {r['chi_at_q0']:>+14.4f} "
                  f"{r['y_times_chi']:>+14.6e}")

        sum_y_chi = sum(mp.mpf(repr(r["y_times_chi"])) for r in leading_records)
        if abs(float(sum_y_chi)) > 1e-50:
            delta_uniform = binding / m_e / float(sum_y_chi)
        else:
            delta_uniform = None

        print()
        print(f"  Σ_(combined-leading) y·χ = {float(sum_y_chi):+.6e}")
        print(f"  binding/m_e              = {binding / m_e:+.6f}")
        if delta_uniform is not None:
            print(f"  Δ_uniform                = {delta_uniform:+.6f}")
        print()

        rows.append({
            "atom": label, "Z": Z, "N": N, "A": A,
            "full_shift_NF": full_shift_nf,
            "crystal_max": max(crystal_per_lam.values()),
            "combined_max": max_combined,
            "n_leading_crystal": sum(1 for v in crystal_per_lam.values()
                                      if v == max(crystal_per_lam.values())),
            "n_leading_combined": len(leading_combined),
            "binding_MeV": binding,
            "sum_y_chi_combined": float(sum_y_chi),
            "Delta_uniform": delta_uniform,
            "leading_top5": leading_records[:5],
        })

    # ── Summary ──
    print("=" * 90)
    print("  Δ closure v2 — combined-pole filter comparison")
    print("=" * 90)
    print()
    print(f"  {'atom':>5} {'full_NF':>8} {'crystal_max':>11} "
          f"{'combined_max':>12} {'#cryst':>8} {'#comb':>7} "
          f"{'Δ_uniform':>12}")
    print("  " + "-" * 80)
    for r in rows:
        d = r["Delta_uniform"]
        d_str = f"{d:+.4f}" if d is not None else "—"
        print(f"  {r['atom']:>5} {r['full_shift_NF']:>8} "
              f"{r['crystal_max']:>11} {r['combined_max']:>12} "
              f"{r['n_leading_crystal']:>8} {r['n_leading_combined']:>7} "
              f"{d_str:>12}")
    print()

    builder = (
        WitnessBuilder("delta-lambda-closure-v2-combined-pole", engine="numpy+scipy")
        .set_description(
            "Δ_λ closure v2: tighter leading-partition filter using "
            "combined per-λ pole order (crystal_shift_λ + ord_y_λ_q) "
            "rather than crystal-shift alone. y_λ's q-zero suppresses "
            "the pole, so combined_λ = crystal_shift_λ - 2·ord_y_λ_u. "
            "Aims to reduce the #leading set from 7/22/22/63 (crystal-"
            "only) to the partitions where the FULL canonical pole "
            "concentrates."
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
