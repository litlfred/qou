#!/usr/bin/env python3
# polynomial_q_not_applicable: evaluates at q = q_0, numeric output.
"""Per-block reading of `m(K) = m_e · VolDensity(K, q₀)` for the 6 atoms
that have Vol(K) data (p, n, D, T, ³He, ⁴He).

## What this script answers

User asked 2026-06-03: "wire up ALL isotopes/nucleotides properly".
The cheat-sheet drift (PR #1749 / #1751) was correctly identified —
production uses uniform `Vol(𝓑₃)` for all atoms; the canonical formula
is `m(K) = m_e · VolDensity(K, q₀)` with K knot-dependent.

This script does the per-knot wire-up for the 6 atoms with `Vol(K)`
data in `per-atom-hyperbolic-volume.witness.json`, using:

    VolDensity(K, q₀) = [Vol(K) / ℏ_q²] · tr_M(K, q₀)
                     = `_li_2_q_util.vol_density_per_block(vol_K, tr_M_K, q)`

where `tr_M(K, q₀)` is the canonical Markov trace over the partitions
of K's strand count (H_3 for the 3-strand baryons; H_6 for D; etc.),
loaded via `canonical_tr_m_via_chi_cache.canonical_tr_m`.

## Discipline + honest framing

This wire-up is **TRUTH-TRACKING**, not a closure attempt. The
existing testbed `vol_density_per_block_wiring.py` already documented a
RED verdict for the proton: per-block `tr_M(p) ≈ 1.065` and production
`H_4 Family-A linking_weight ≈ 2.53` are DIFFERENT scalars (off by
~2.4×), so this wire-up makes the proton prediction go from
+2.89% to **−56.7%**, not the other way.

Per CLAUDE.md production-vs-exploratory discipline, this script
DOES NOT propose the per-block reading as a closure. It MAKES the
discrepancy visible across the 6 atoms with data, so the structural
question — "what is the per-knot generalization of H_4 Family-A
linking_weight that closes the gap?" — has a quantitative scoreboard
for future research.

## Output

`per-knot-mass-table-demonstration.witness.json` — per-atom rows
with:

- atom, Z, N, A
- vol_K (Vol of the canonical knot for this atom)
- tr_M_K (canonical Markov trace at q_0)
- vol_density_per_block (m_e × VolDensity(K, q₀))
- m_pred_per_block_MeV (per-knot reading prediction)
- m_observed_MeV (CODATA / AME)
- err_per_block_pct (vs CODATA)
- m_pred_production_MeV (uniform-Vol reading from `mass-table-comprehensive`)
- err_production_pct
- delta_per_block_vs_production_pct (does per-block move us closer?)
- summary["per_block_recovers_production_gap_pct"] — analogous to
  the testbed's `recovered_fraction_pct`

EXPLORATORY assertions only; CI-safe.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import json
import sys
import time
from pathlib import Path

import mpmath as mp

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from _li_2_q_util import (  # noqa: E402
    vol_density_borromean,
    vol_density_per_block,
    geom_leading,
)
from q_parameter import Q as q_0  # noqa: E402
from codata_constants import (  # noqa: E402 — registry (no inline CODATA literals)
    M_E_MEV,
    M_P_MEV_VALIDATION, M_N_MEV_VALIDATION, M_D_MEV_VALIDATION,
    M_T_MEV_VALIDATION, M_HE3_MEV_VALIDATION, M_HE4_MEV_VALIDATION,
)
from closed_form_tau_M import (  # noqa: E402
    compute_tau_M_nucleon_H3,
    closed_form_tau_M,
)
from witness_base import WitnessBuilder  # noqa: E402


# CODATA / AME observed masses — codata_constants registry (no inline literals)
CODATA = {
    "p":    M_P_MEV_VALIDATION,
    "n":    M_N_MEV_VALIDATION,
    "D":    M_D_MEV_VALIDATION,     # AME 2020
    "T":    M_T_MEV_VALIDATION,
    "3He":  M_HE3_MEV_VALIDATION,
    "4He":  M_HE4_MEV_VALIDATION,
}


def main() -> int:
    start = time.time()
    w = WitnessBuilder(
        "per-knot-mass-table-demonstration",
        engine="mpmath",
    )
    w.set_description(
        "Per-block reading of m(K) = m_e · VolDensity(K, q₀) for the "
        "6 atoms with Vol(K) data, using vol_density_per_block(vol_K, "
        "tr_M_K, q). EXPLORATORY truth-tracking, NOT a closure — "
        "validates the vol_density_per_block_wiring.py RED verdict "
        "across the atomic table."
    )

    q = mp.mpf(str(q_0))
    m_e = mp.mpf(str(M_E_MEV))

    # Load per-atom Vol(K) witness
    vol_witness = HERE / "per-atom-hyperbolic-volume.witness.json"
    vol_data = json.loads(vol_witness.read_text())["data"]

    atoms = [
        ("p",   1, 0, 1, vol_data["Vol_p"],   vol_data["knot_p"]),
        ("n",   0, 1, 1, vol_data["Vol_n"],   vol_data["knot_n"]),
        ("D",   1, 1, 2, vol_data["Vol_D"],   vol_data["knot_D"]),
        ("T",   1, 2, 3, vol_data["Vol_T"],   vol_data["knot_T"]),
        ("3He", 2, 1, 3, vol_data["Vol_3He"], vol_data["knot_3He"]),
        ("4He", 2, 2, 4, vol_data["Vol_4He"], vol_data["knot_4He"]),
    ]

    # Production uniform-Vol baseline (same for every atom)
    vol_density_uniform = vol_density_borromean(q)
    m_avg_production = m_e * vol_density_uniform

    # H_3 building blocks for the Phase 5q closed form (sub-second compute)
    print("Computing H_3 building blocks tr_M^3(𝓑_p), tr_M^3(𝓑_n)...")
    tau_p_H3 = compute_tau_M_nucleon_H3("p", q)
    tau_n_H3 = compute_tau_M_nucleon_H3("n", q)
    print(f"  tr_M^3(𝓑_p, q₀) = {float(tau_p_H3):.6f}")
    print(f"  tr_M^3(𝓑_n, q₀) = {float(tau_n_H3):.6f}")

    rows = []
    for atom, Z, N, A, vol_K_raw, knot_label in atoms:
        vol_K = mp.mpf(str(vol_K_raw))

        # Per-knot tr_M(K, q₀) via Phase 5q closed form
        # tr_M(𝓑_K) = tr_M^3(𝓑_p)^Z · tr_M^3(𝓑_n)^N · ∏ f_i(q)
        try:
            tr_M_K = closed_form_tau_M(Z, N, q, tau_p_H3, tau_n_H3)
        except Exception as e:
            rows.append({
                "atom": atom, "Z": Z, "N": N, "A": A,
                "knot": knot_label, "vol_K": float(vol_K),
                "tr_M_K_status": f"closed_form_tau_M failed: {e!s}",
                "m_pred_per_block_MeV": None,
                "m_observed_MeV": float(CODATA[atom]),
            })
            continue

        # Paper-faithful per-block: vol_density_per_block already folds
        # in tr_M(K, q₀) — i.e. this returns m_e × VolDensity(K, q₀) when
        # multiplied by m_e below; do NOT re-multiply by tr_M_K here.
        vol_density_pb = vol_density_per_block(vol_K, tr_M_K, q)
        m_pred_pb = m_e * vol_density_pb

        codata = CODATA[atom]
        err_pb = (m_pred_pb - codata) / codata * 100
        err_prod = (m_avg_production - codata) / codata * 100
        delta = err_pb - err_prod   # signed delta (kept for reproducibility)
        # delta_abs measures actual distance to CODATA — negative means
        # per-block reading is CLOSER, positive means FURTHER. This is
        # the quantity the row's "did per-block move us closer?" claim
        # actually asserts.
        delta_abs = abs(err_pb) - abs(err_prod)

        rows.append({
            "atom": atom, "Z": Z, "N": N, "A": A,
            "knot": knot_label,
            "vol_K": float(vol_K),
            "tr_M_K": float(tr_M_K),
            "vol_density_per_block": float(vol_density_pb),
            "vol_density_uniform_production": float(vol_density_uniform),
            "m_pred_per_block_MeV": float(m_pred_pb),
            "m_pred_production_MeV": float(m_avg_production),
            "m_observed_MeV": float(codata),
            "err_per_block_pct": float(err_pb),
            "err_production_pct": float(err_prod),
            "delta_per_block_vs_production_pct": float(delta),
            "delta_abs_per_block_vs_production_pct": float(delta_abs),
        })

    # Summary stats
    valid = [r for r in rows if r.get("m_pred_per_block_MeV") is not None]
    if valid:
        # Recovered fraction (mirroring testbed convention)
        worst_pb = max(abs(r["err_per_block_pct"]) for r in valid)
        worst_prod = max(abs(r["err_production_pct"]) for r in valid)
        mean_pb = sum(abs(r["err_per_block_pct"]) for r in valid) / len(valid)
        mean_prod = sum(abs(r["err_production_pct"]) for r in valid) / len(valid)
    else:
        worst_pb = worst_prod = mean_pb = mean_prod = None

    w.add_data("rows", rows)
    verdict = (
        "Per-block reading makes predictions worse on average — "
        "consistent with the vol_density_per_block_wiring.py "
        "RED verdict that H_3 tr_M(K) is NOT the H_4 Family-A "
        "linking_weight scalar. To 'wire up properly' for closure "
        "requires a per-knot generalization of linking_weight(K), "
        "not just per-knot Vol(K). Open research."
        if (mean_pb is not None and mean_prod is not None and mean_pb > mean_prod)
        else "Per-block reading is at least as good on average; revisit assumption."
    )
    w.add_data("summary", {
        "n_atoms_evaluated": len(valid),
        "n_atoms_total": len(rows),
        "mean_abs_err_per_block_pct": mean_pb,
        "mean_abs_err_production_pct": mean_prod,
        "worst_abs_err_per_block_pct": worst_pb,
        "worst_abs_err_production_pct": worst_prod,
        "verdict": verdict,
    })
    w.add_data("parameters", {
        "q_0": str(q),
        "m_e_MeV": str(m_e),
    })
    w.add_assertion(
        "n_atoms_with_per_block_prediction",
        len(valid),
        expected=6,
        source="all 6 atoms with Vol(K) witness data should have chi cache",
    )

    w.save()

    # Brief human-readable report
    print()
    print("=== per-knot reading (vol_density_per_block) vs production ===")
    print(f"{'atom':<5}{'Vol(K)':>10}{'tr_M(K)':>10}{'m_pb (MeV)':>14}{'m_prod (MeV)':>15}{'observed':>14}{'err_pb %':>10}{'err_prod %':>12}")
    for r in rows:
        if r.get("m_pred_per_block_MeV") is None:
            print(f"  {r['atom']}: SKIP — {r.get('tr_M_K_status', 'unknown')}")
            continue
        print(f"{r['atom']:<5}{r['vol_K']:>10.4f}{r['tr_M_K']:>10.4f}{r['m_pred_per_block_MeV']:>14.4f}{r['m_pred_production_MeV']:>15.4f}{r['m_observed_MeV']:>14.4f}{r['err_per_block_pct']:>10.4f}{r['err_production_pct']:>12.4f}")
    print()
    print(f"VERDICT: {verdict}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
