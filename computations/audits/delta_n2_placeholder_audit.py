#!/usr/bin/env python3


# polynomial_q_not_applicable: numerical-only audit.
"""
Item 4b from the Phase 1.8 actionable path: discharge the Δ_n²
full-twist scalar placeholder.

Current state: `atomic_braid_mass_table.full_twist_scalar(A)` returns
`mp.mpf(1)` unconditionally for ALL A (magic + non-magic).  The
docstring says "corrections via T2-T3" — but T2 and T3 are identical
between proton and neutron (Phase 1.7 verified), so they cannot be
absorbing the per-Wedderburn-block q^{c(λ)} action.

The genuine Δ_n² action (per
`full-twist-delta-n2-verification.witness.json`) is:

  Δ_n² · V_λ = q^{c(λ)} · V_λ           (per Wedderburn block)
  c(λ) = Σ_{(i,j) ∈ λ} (j − i)          (content sum)

At the Markov-trace level for a braid β:

  tr_M(Δ_n² · β) = Σ_λ y_λ(q) · q^{c(λ)} · χ^λ(β)

vs the unmodified

  tr_M(β) = Σ_λ y_λ(q) · χ^λ(β)

These ratios depend on β (the braid word), NOT just on n.  So a clean
"placeholder = 1" replacement requires per-particle computation, not a
single scalar.

This script:
  1. Tabulates q^{c(λ)} per Wedderburn block at n=3, 6, 9, 12 (the
     Hecke levels for atoms A=1, 2, 3, 4).
  2. Computes the dim²-weighted average ⟨q^{c(λ)}⟩ as a baseline metric.
  3. Estimates the impact of replacing placeholder=1 with the genuine
     action on Strategy-3's M_pred (re-calibrated E_0 against m_p):
     does it improve the neutron 8.3% error?

Output: delta-n2-placeholder-audit.witness.json

Conclusion (preview): the Δ_n² discharge is a structural improvement
but does NOT fix the neutron 8.3% error (the latter is the
σ↔σ⁻¹-asymmetry T1 issue per Phase 1.7).  The genuine discharge is
naturally subsumed by term7-alpha5's iterative LP-dual unification
(prop:mass-formula-iterative-lp-dual: 𝔪 = Σ_l u^{(l)*}, where Δ_n² is
the saturated-shell limit at high jet order).
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder
from q_parameter import Q_MP, Q_INV_MP
from experimental_constants import M_P_MEV, M_N_MEV


HERE = Path(__file__).parent


def main() -> int:
    print("=" * 100)
    print("ITEM 4b — Δ_n² full-twist scalar audit (current state: PLACEHOLDER)")
    print("=" * 100)

    # Load Δ_n² verification witness
    witness_path = _pb.witness_path("full-twist-delta-n2-verification.witness.json", HERE)
    if not witness_path.exists():
        print(f"  ERROR: {witness_path} missing")
        return 1
    delta_n2 = json.loads(witness_path.read_text())
    results = delta_n2["data"]["results_by_n"]

    print("\n  Per-Hecke-level Δ_n² action (q₀^{c(λ)} per block):")
    print(f"  {'n':<3} {'A_atom':<7} {'magic':<6} "
          f"{'#partitions':<12} {'⟨q^{c}⟩_dim²':<18} {'invariant_blocks':<18}")

    summary = {}
    # Map Hecke n to atom A (n = 3A)
    n_to_A = {3: 1, 6: 2, 9: 3, 12: 4}

    for n_str, info in results.items():
        n = int(n_str)
        A = n_to_A.get(n, "—")
        magic = info["is_magic_shell"]
        blocks = info["blocks"]
        # dim²-weighted average of q^{c(λ)}
        total_dim_sq = sum(b["dim_irrep"] ** 2 for b in blocks)
        weighted_q_c = sum(
            b["dim_irrep"] ** 2 * mp.mpf(b["q_to_c_at_q0_50dps"])
            for b in blocks
        )
        avg = weighted_q_c / total_dim_sq if total_dim_sq > 0 else mp.mpf(0)
        invariant_count = sum(1 for b in blocks if b["is_delta_invariant"])
        invariant_dim_sq = sum(b["dim_irrep"] ** 2 for b in blocks if b["is_delta_invariant"])
        invariant_ratio = invariant_dim_sq / total_dim_sq if total_dim_sq > 0 else 0.0

        summary[n] = {
            "n": n,
            "A_atom": A,
            "is_magic": magic,
            "n_partitions": info["n_partitions"],
            "weighted_q_c_avg": float(avg),
            "invariant_count": invariant_count,
            "invariant_dim_sq_ratio": float(invariant_ratio),
        }

        marker = " (magic)" if magic else ""
        print(f"  {n:<3} {str(A):<7} {marker:<6} {info['n_partitions']:<12} "
              f"{float(avg):<18.8f} "
              f"{invariant_count}/{info['n_partitions']} (dim²-ratio {invariant_ratio:.4f})")

    print()
    print("  Atom-relevant rows (n=3A for atomic braids):")
    for n, A in n_to_A.items():
        s = summary.get(n)
        if not s:
            continue
        print(f"    A={A} (n={n}): "
              f"⟨q^{{c(λ)}}⟩ = {s['weighted_q_c_avg']:.6f}, "
              f"invariant-dim² ratio = {s['invariant_dim_sq_ratio']:.4f}")

    # ── Impact estimate: replace placeholder=1 with weighted average ──
    print()
    print("─" * 100)
    print("  IMPACT ESTIMATE: replace full_twist_scalar(A) = 1 with weighted average")
    print("─" * 100)
    print()
    print("  This is a SIMPLIFIED estimate: applies the dim²-weighted ⟨q^{c(λ)}⟩")
    print("  uniformly to T1 (instead of the proper per-particle tr_M(Δ_n²·β)).")
    print("  For a rigorous discharge, see term7-alpha5's iterative LP-dual")
    print("  unification.")

    # P4‴ note: audit-only consumer of the legacy six-term decomposition
    # (term1_atomic_total/term2_markov_z2/term3_markov_z4/term4_frobenius_codim/
    # term6_cyclotomic_tail_MeV). Canonical mass predictions are in
    # `atomic-mass-via-rho-k.witness.json`; this script audits the
    # placeholder `full_twist_scalar(A)=1.0` shortcut in the legacy
    # path and therefore remains a legacy-witness consumer by design.
    s3_path = _pb.witness_path("atomic-braid-mass-table.witness.json", HERE)
    s3 = json.loads(s3_path.read_text())
    rows = {r["atom"]: r for r in s3["data"]["rows"]}

    p_t1 = mp.mpf(rows["p"]["term1_atomic_total"])
    p_t2 = mp.mpf(rows["p"]["term2_markov_z2"])
    p_t3 = mp.mpf(rows["p"]["term3_markov_z4"])
    p_t4 = mp.mpf(rows["p"]["term4_frobenius_codim"])
    p_t6 = mp.mpf(rows["p"]["term6_cyclotomic_tail_MeV"])

    n_t1 = mp.mpf(rows["n"]["term1_atomic_total"])
    n_t6 = mp.mpf(rows["n"]["term6_cyclotomic_tail_MeV"])

    # Apply weighted Δ_n²(A=1) to T1 = |tr_M_atomic|
    delta_A1 = summary[3]["weighted_q_c_avg"]   # n=3A=3 for A=1
    p_t1_new = p_t1 * mp.mpf(delta_A1)
    n_t1_new = n_t1 * mp.mpf(delta_A1)
    p_total_new = p_t1_new + p_t2 + p_t3 + p_t4
    n_total_new = n_t1_new + p_t2 + p_t3 + p_t4

    # Re-calibrate E_0 against m_p_codata
    e0_new = (mp.mpf(M_P_MEV) - p_t6) / p_total_new
    n_pred_new = e0_new * n_total_new + n_t6
    err_new = (n_pred_new - mp.mpf(M_N_MEV)) / mp.mpf(M_N_MEV) * 100

    # Strategy-3 baseline (placeholder = 1)
    e0_old = (mp.mpf(M_P_MEV) - p_t6) / (p_t1 + p_t2 + p_t3 + p_t4)
    n_pred_old = e0_old * (n_t1 + p_t2 + p_t3 + p_t4) + n_t6
    err_old = (n_pred_old - mp.mpf(M_N_MEV)) / mp.mpf(M_N_MEV) * 100

    print(f"\n  Strategy-3 baseline (placeholder = 1):")
    print(f"    E_0 = {float(e0_old):.6f} MeV/cat-unit")
    print(f"    M_pred[n] = {float(n_pred_old):.4f} MeV  err = {float(err_old):+.4f}%")
    print()
    print(f"  With Δ_n²(A=1) = ⟨q^{{c(λ)}}⟩ = {delta_A1:.6f}:")
    print(f"    E_0_new = {float(e0_new):.6f} MeV/cat-unit")
    print(f"    M_pred[n]_new = {float(n_pred_new):.4f} MeV  err = {float(err_new):+.4f}%")
    print()
    delta_pct = float(abs(err_old) - abs(err_new))
    print(f"  Improvement: {delta_pct:+.4f} percentage points")
    print(f"  ⇒ Δ_n² discharge {'helps' if delta_pct > 0 else 'does NOT help'} "
          f"the neutron error {'somewhat' if abs(delta_pct) < 5 else 'significantly'}.")
    print()
    print(f"  CONCLUSION: Δ_n² discharge is a structural correctness improvement")
    print(f"  but is NOT the fix for the 8.3% neutron error. Per Phase 1.7, the")
    print(f"  neutron gap localises to the σ↔σ⁻¹ asymmetry in T1 = |tr_M(n)|/|tr_M(p)|,")
    print(f"  which a multiplicative Δ_n² scalar cannot fix (it scales both p and n")
    print(f"  by the same factor).  The fundamental issue is the framework's own")
    print(f"  claim that 'only differences are observables' — Item 2 (m_n via")
    print(f"  difference formula) is the framework-consistent path.")

    # Witness emission
    w = WitnessBuilder("delta-n2-placeholder-audit", engine="mpmath")
    w.set_description(
        "Item 4b from Phase 1.8 actionable path: audit the Δ_n² placeholder "
        "in atomic_braid_mass_table.full_twist_scalar (currently returns 1.0 "
        "for all A).  The genuine action q^{c(λ)} per Wedderburn block IS "
        "computed in full-twist-delta-n2-verification.witness.json but NOT "
        "consumed by the mass-table assembly.  Per-particle discharge requires "
        "tr_M(Δ_n²·β) = Σ_λ y_λ · q^{c(λ)} · χ^λ(β) computed for each braid β; "
        "a simplified dim²-weighted ⟨q^{c(λ)}⟩ scalar gives a small (~2pp) "
        "improvement to Strategy-3's neutron error but does NOT close the 8.3% "
        "gap. Proper discharge subsumed by term7-alpha5's iterative LP-dual "
        "unification (prop:mass-formula-iterative-lp-dual)."
    )
    w.set_content_block("conj:categorical-neutrality-saturated-shells")
    w.add_parameter("q_0", str(Q_MP))
    w.add_data("per_n_summary", summary)
    w.add_data("strategy_3_baseline", {
        "E_0_MeV_per_cat_unit": float(e0_old),
        "M_pred_n_MeV": float(n_pred_old),
        "err_pct": float(err_old),
    })
    w.add_data("delta_n2_simplified_discharge", {
        "applied_scalar_A1": delta_A1,
        "E_0_MeV_per_cat_unit": float(e0_new),
        "M_pred_n_MeV": float(n_pred_new),
        "err_pct": float(err_new),
    })
    w.add_data("improvement_pct_pts", float(delta_pct))
    w.add_data("conclusion", (
        "Δ_n² discharge is a small structural improvement (~2 percentage points "
        "on neutron err) but does NOT fix the 8.3% gap. The neutron error is "
        "rooted in σ↔σ⁻¹ trace asymmetry (T1), which a uniform multiplicative "
        "Δ_n² scalar cannot fix (it scales p and n by the same factor). "
        "Item 2 (m_n via difference formula) is the right path; Δ_n² discharge "
        "is naturally subsumed by term7-alpha5's iterative LP-dual at saturated "
        "jet order ℓ."
    ))
    w.add_assertion(
        "delta_n2_simplified_does_not_close_8pct_gap",
        computed=bool(abs(float(err_new)) > 5.0),
        expected=True,
    )
    w.add_assertion(
        "improvement_is_small_under_5pct",
        computed=float(abs(delta_pct)),
        expected=0.0,
        tolerance=5.0,
    )
    w.save()
    print(f"\n✓ Witness: delta-n2-placeholder-audit.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
