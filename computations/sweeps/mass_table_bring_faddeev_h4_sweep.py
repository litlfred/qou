#!/usr/bin/env python3
"""Sweep — Bring color-tube + Faddeev h⁴ candidate vs Family A production
across the full 65-isotope mass table.

Per the user-picked next step (audit `2026-05-25-m-p-m-n-full-chain-audit.md`
+ `m_p_bring_plus_faddeev_h4_probe.py`'s +108 ppm m_p result): test
whether the candidate
  linking_weight(q) = 1/(1 − h·q^{10}) + 1/(1 − h⁴) − 1
preserves the +0.03% Δm/M_N flavor-split match AND closes the +2.89%
gap uniformly across the isotope table.

Strategy: load `mass-table-comprehensive.witness.json` (existing Family
A production output), recompute the m_pred column with the candidate
linking_weight, report per-isotope improvement. Does NOT touch the
binding-energy column (binding is computed separately via Kashaev
`ρ_F · Vol_hyp` in `mass_table_ppb.py`, independent of linking_weight).

The mass shift propagates linearly per nucleon:
  Δm_p = m_p_Bring+Faddeev − m_p_FamilyA  ≈ −27.0 MeV per proton
  Δm_n ≈ −27.0 MeV per neutron
  Δm_atom ≈ Z·Δm_p + N·Δm_n  (linear, since B is unchanged)

Output: `mass-table-bring-faddeev-h4-sweep.witness.json` — per-isotope
column of m_pred (Family A) vs m_pred (Bring + Faddeev h⁴) + delta + rel
err vs CODATA.

This is PROBE/EXPLORATORY (per Rule 14): the categorical proof of the
additive composition is pending; do not promote to production until
the H_4 direct-sum vs tensor-product proof lands.
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

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from _li_2_q_util import (  # noqa: E402
    linking_weight_family_a,
    flavor_split_subleading,
)

mp.mp.dps = 80


def linking_weight_bring_plus_faddeev_h4(q: mp.mpf, q_inv: mp.mpf | None = None) -> mp.mpf:
    """Candidate: Bring color-tube + Faddeev h⁴ additive composition.

      linking_weight(q) = 1/(1 − h_q · q^{10}) + 1/(1 − h_q⁴) − 1

    Both factors are Φ_q functional-equation ratios at substrate-natural
    z values (z_1 = h·q^{10} for Bring; z_2 = h⁴ for Faddeev recursion
    at the even-substrate KLR-canonical-basis vector).
    Rule-14 compliant (driver (i) + driver (xiii) of the 13-driver menu).
    """
    qi = mp.mpf(1) / q if q_inv is None else q_inv
    h = q - qi
    z1 = h * q ** 10
    z2 = h ** 4
    return 1 / (1 - z1) + 1 / (1 - z2) - 1


def main() -> int:
    Q0 = mp.mpf(Q_50_DIGIT_STR)
    Q_INV = mp.mpf(1) / Q0
    HBAR_Q = (Q0 - 1) / Q0
    M_E = M_E_MEV
    VOL_B3 = 8 * mp.catalan
    INV_HBAR2 = 1 / (HBAR_Q ** 2)
    scale_const = M_E * VOL_B3 * INV_HBAR2

    # ── Both candidates' m_p, m_n ────────────────────────────────
    lam_A = linking_weight_family_a(Q0, Q_INV)
    lam_BF = linking_weight_bring_plus_faddeev_h4(Q0, Q_INV)
    dm_over_Mn = flavor_split_subleading(Q0, Q_INV)

    m_avg_A = scale_const * lam_A
    m_avg_BF = scale_const * lam_BF

    m_p_A = m_avg_A * (1 - dm_over_Mn / 2)
    m_n_A = m_avg_A * (1 + dm_over_Mn / 2)
    m_p_BF = m_avg_BF * (1 - dm_over_Mn / 2)
    m_n_BF = m_avg_BF * (1 + dm_over_Mn / 2)

    print("=" * 80)
    print("Mass-table sweep — Bring + Faddeev h⁴ vs Family A production")
    print("=" * 80)
    print()
    print(f"linking_weight Family A      = {mp.nstr(lam_A, 15)}")
    print(f"linking_weight Bring + Fad h⁴ = {mp.nstr(lam_BF, 15)}")
    print()
    print(f"m_p Family A                  = {float(m_p_A):.6f} MeV")
    print(f"m_p Bring + Fad h⁴            = {float(m_p_BF):.6f} MeV")
    print(f"m_p shift per proton          = {float(m_p_BF - m_p_A):+.6f} MeV")
    print()
    print(f"m_n Family A                  = {float(m_n_A):.6f} MeV")
    print(f"m_n Bring + Fad h⁴            = {float(m_n_BF):.6f} MeV")
    print(f"m_n shift per neutron         = {float(m_n_BF - m_n_A):+.6f} MeV")
    print()

    # ── Load production mass-table-comprehensive witness ────────
    witness_path = _pb.witness_path("mass-table-comprehensive.witness.json", HERE)
    if not witness_path.exists():
        print(f"ERROR: {witness_path} not found")
        return 1
    with witness_path.open() as f:
        prod = json.load(f)
    rows = prod["data"]["rows"]
    print(f"Loaded {len(rows)} isotope rows from production witness")
    print()

    # CODATA m_p, m_n for nucleon-by-nucleon shift
    from codata_constants import M_P_MEV_VALIDATION, M_N_MEV_VALIDATION
    M_P_CODATA = M_P_MEV_VALIDATION
    M_N_CODATA = M_N_MEV_VALIDATION

    # ── Sweep ────────────────────────────────────────────────────
    out_rows = []
    print(f"{'atom':<6} {'Z':>3} {'N':>3} {'A':>4} {'m_FamilyA':>14} {'m_Bring+Fad':>14} "
          f"{'CODATA':>14} {'errFamA %':>10} {'errBF %':>10} {'improve':>8}")
    print("-" * 100)
    for row in rows:
        Z = row["Z"]
        N = row["N"]
        A = row["A"]
        atom = row["atom"]
        m_pred_A = row.get("m_pred_MeV")
        m_codata = row.get("m_codata_MeV")

        if m_pred_A is None or m_codata is None:
            continue

        # Bring + Faddeev shift: each nucleon's mass is scaled, but the
        # binding energy B is unchanged. So:
        #   m_pred_BF_atom = Z * m_p_BF + N * m_n_BF − B_pred
        # Substituting m_pred_A_atom = Z * m_p_A + N * m_n_A − B_pred:
        #   m_pred_BF_atom = m_pred_A_atom + Z*(m_p_BF − m_p_A) + N*(m_n_BF − m_n_A)
        # This is exact, no approximation, since B is unchanged.
        m_pred_A_mp = mp.mpf(str(m_pred_A))
        m_pred_BF_mp = (
            m_pred_A_mp + Z * (m_p_BF - m_p_A) + N * (m_n_BF - m_n_A)
        )
        m_codata_mp = mp.mpf(str(m_codata))
        err_A = (m_pred_A_mp - m_codata_mp) / m_codata_mp
        err_BF = (m_pred_BF_mp - m_codata_mp) / m_codata_mp

        # Improvement factor (FamilyA error / Bring+Faddeev error)
        if abs(err_BF) > 1e-15:
            improve_factor = abs(err_A) / abs(err_BF)
        else:
            improve_factor = float('inf')

        print(f"{atom:<6} {Z:>3} {N:>3} {A:>4} "
              f"{float(m_pred_A_mp):>14.6f} {float(m_pred_BF_mp):>14.6f} "
              f"{float(m_codata_mp):>14.6f} "
              f"{float(err_A) * 100:>9.4f}% {float(err_BF) * 100:>9.4f}% "
              f"{float(improve_factor) if improve_factor != float('inf') else 999999.9:>7.1f}×")
        out_rows.append({
            "atom": atom, "Z": Z, "N": N, "A": A,
            "m_FamilyA_MeV": mp.nstr(m_pred_A_mp, 18),
            "m_Bring_Faddeev_h4_MeV": mp.nstr(m_pred_BF_mp, 18),
            "m_codata_MeV": mp.nstr(m_codata_mp, 12),
            "err_FamilyA_pct": mp.nstr(err_A * 100, 10),
            "err_Bring_Faddeev_h4_pct": mp.nstr(err_BF * 100, 10),
            "improvement_factor": str(improve_factor),
        })

    # Summary
    if out_rows:
        avg_improve = sum(
            float(r["improvement_factor"]) for r in out_rows
            if r["improvement_factor"] not in ("inf", "nan")
        ) / len(out_rows)
        max_improve = max(
            float(r["improvement_factor"]) for r in out_rows
            if r["improvement_factor"] not in ("inf", "nan")
        )
        max_err_BF = max(
            abs(float(r["err_Bring_Faddeev_h4_pct"])) for r in out_rows
        )
        max_err_A = max(
            abs(float(r["err_FamilyA_pct"])) for r in out_rows
        )
        print()
        print("=" * 80)
        print(f"SUMMARY across {len(out_rows)} isotopes:")
        print(f"  max |err_FamilyA|       = {max_err_A:.4f} %  ({max_err_A * 1e4:.1f} ppm)")
        print(f"  max |err_Bring+Fad h⁴|  = {max_err_BF:.4f} %  ({max_err_BF * 1e4:.1f} ppm)")
        print(f"  avg improvement factor  = {avg_improve:.1f}×")
        print(f"  max improvement factor  = {max_improve:.1f}×")
        print("=" * 80)

    # ── Witness ──────────────────────────────────────────────────
    w = WitnessBuilder("mass-table-bring-faddeev-h4-sweep", engine="mpmath")
    w.set_description(
        "Sweep of the Bring color-tube + Faddeev h⁴ candidate "
        "linking_weight `1/(1 − h·q^{10}) + 1/(1 − h⁴) − 1` against "
        "the Family A production output across the full isotope mass "
        "table (mass-table-comprehensive.witness.json). The candidate "
        "shifts m_p, m_n each by ~−27 MeV (closing the +2.89 % gap to "
        "+108 ppm); the shift propagates linearly to atomic masses as "
        "Z·Δm_p + N·Δm_n (binding unchanged). RULE 14 compliance: both "
        "factors are Φ_q functional-equation ratios at substrate-natural "
        "z values (driver i Faddeev iterated + driver xiii KLR positivity). "
        "Open load-bearing step: additive-vs-multiplicative composition "
        "categorical proof at H_4."
    )
    w.set_content_block("conj:borromean-baryon-mass-formula")
    w.add_parameter("dps", 80)
    w.add_parameter("linking_weight_FamilyA", mp.nstr(lam_A, 25))
    w.add_parameter("linking_weight_Bring_Faddeev_h4", mp.nstr(lam_BF, 25))
    w.add_parameter("m_p_FamilyA_MeV", mp.nstr(m_p_A, 15))
    w.add_parameter("m_p_Bring_Faddeev_h4_MeV", mp.nstr(m_p_BF, 15))
    w.add_parameter("m_n_FamilyA_MeV", mp.nstr(m_n_A, 15))
    w.add_parameter("m_n_Bring_Faddeev_h4_MeV", mp.nstr(m_n_BF, 15))
    w.add_data("isotope_rows", out_rows)
    if out_rows:
        w.add_data("summary", {
            "n_isotopes": len(out_rows),
            "max_err_FamilyA_pct": f"{max_err_A:.10f}",
            "max_err_Bring_Faddeev_h4_pct": f"{max_err_BF:.10f}",
            "avg_improvement_factor": f"{avg_improve:.4f}",
            "max_improvement_factor": f"{max_improve:.4f}",
        })

        w.add_assertion(
            "candidate_improves_uniformly",
            computed=int(max_err_BF < max_err_A),
            expected=1,
            tolerance=None,
            source=(
                "Bring + Faddeev h⁴ candidate strictly tightens the "
                "worst-case atomic mass error vs Family A across all "
                "isotopes (both reductions are linear shifts; binding "
                "energy column unchanged)."
            ),
        )

    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
