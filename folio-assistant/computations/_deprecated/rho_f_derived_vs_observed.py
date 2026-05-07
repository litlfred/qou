#!/usr/bin/env python3
"""
Derived ρ_F vs observed ρ_F^eff — NO FITTING.

Derivation (from the paper):
    B(Z, N) = -α · Φ_1(β)                     α = m_e · 8G
    Φ_1(β) = Σ_i ln|V̂_i^full(q_0)|           (`def:algebraic-quantum-volume-specialization`)
    V̂_i^full = w_sym·λ_i^sym + w_std·V_i^std + w_alt·λ_i^alt
               (`thm:wedderburn-mass-formula`)

Density:
    ρ_F_derived(K) = B_derived(K) / V_hyp(K) = -α · Φ_1 / V_hyp

Compare to:
    ρ_F_observed(K) = B_AME(K) / V_hyp(K)

If ρ_F_derived(K) ≈ ρ_F_observed(K) (per atom), the paper formula
holds.  If NOT, the discrepancy tells us what the formula is missing.
"""
from __future__ import annotations

import sys
import json
import math
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))

from mass_endomorphism import (additive_wedderburn_volumes, w_sym, w_std,
                                  w_alt, HA)
from hecke_core import atom_per_generator_volumes
from q_parameter import Q as q0

CATALAN_G = 0.915965594177219015054603514932
VOL_BORROMEAN_8G = 8.0 * CATALAN_G
M_E_MEV = 0.51099895
ALPHA_MEV = M_E_MEV * VOL_BORROMEAN_8G   # paper's binding scale

# Empirical inputs (no fits)
ATOMS = [
    ("D",   1, 1, 2.22456612,  4.4008325161,  M_E_MEV),         # knot 6_2, ρ_nominal = m_e
    ("T",   1, 2, 8.4817984,   8.28632,       2 * M_E_MEV),     # knot 8_11
    ("3He", 2, 1, 7.7180375,   VOL_BORROMEAN_8G, 2 * M_E_MEV),   # Borromean
    ("4He", 2, 2, 28.295674,   4 * VOL_BORROMEAN_8G, 2 * M_E_MEV),
]


def phi_1(Z: int, N: int) -> float:
    """Φ_1(β_atom) = Σ_i ln|V̂_i^full| using paper's algebraic quantum volume.

    Computed on atom - free (bond only).
    """
    v_atom = atom_per_generator_volumes(Z, N, include_inter=True)
    v_free = atom_per_generator_volumes(Z, N, include_inter=False)

    def _sum_ln(vols):
        total = 0.0
        for v in vols:
            f = v["full"]
            if abs(f) < 1e-30:
                return float("-inf")
            total += math.log(abs(f))
        return total

    return _sum_ln(v_atom) - _sum_ln(v_free)


if __name__ == "__main__":
    print("=" * 110)
    print("DERIVED vs OBSERVED ρ_F — no fitting")
    print(f"  α = m_e · 8G = {ALPHA_MEV:.6f} MeV  (paper binding scale)")
    print("=" * 110)

    print(f"\n  {'atom':>4} {'B_AME':>10} {'Φ_1':>10} "
          f"{'B_derived':>12} {'ratio':>10} {'err_pct':>10}")
    results = []
    for (name, Z, N, B_ame, V_hyp, rho_nominal) in ATOMS:
        P1 = phi_1(Z, N)
        B_derived = -ALPHA_MEV * P1
        ratio = B_derived / B_ame if B_ame else float("nan")
        err = (B_derived - B_ame) / B_ame * 100
        print(f"  {name:>4} {B_ame:>10.4f} {P1:>+10.4f} "
              f"{B_derived:>+12.4f} {ratio:>10.4f} {err:>+9.3f}%")
        results.append({
            "atom": name, "Z": Z, "N": N, "A": Z + N,
            "B_AME": B_ame, "V_hyp": V_hyp,
            "phi_1": P1,
            "B_derived": B_derived,
            "ratio_derived_over_AME": ratio,
            "err_pct": err,
            "rho_F_observed": B_ame / V_hyp,
            "rho_F_derived":  B_derived / V_hyp,
            "rho_F_nominal":  rho_nominal,
        })

    # Density comparison
    print(f"\n{'=' * 100}")
    print("DENSITY comparison: ρ_F_obs vs ρ_F_derived (both = B/V_hyp)")
    print("=" * 100)
    print(f"  {'atom':>4} {'ρ_F_obs':>10} {'ρ_F_der':>10} "
          f"{'ρ_F_nom':>10} {'obs/nom':>10} {'der/nom':>10}")
    for r in results:
        obs = r["rho_F_observed"]
        der = r["rho_F_derived"]
        nom = r["rho_F_nominal"]
        print(f"  {r['atom']:>4} {obs:>10.5f} {der:>10.5f} {nom:>10.5f} "
              f"{obs/nom:>10.5f} {der/nom:>10.5f}")

    # Ratio-of-ratios — how does the derived deviation compare to observed?
    print(f"\n{'=' * 100}")
    print("HOW does derived error compare to observed deviation?")
    print("=" * 100)
    print(f"  {'atom':>4} {'(obs/nom-1)%':>14} {'(der/nom-1)%':>14} "
          f"{'der/obs':>10}")
    for r in results:
        obs_dev = (r["rho_F_observed"] / r["rho_F_nominal"] - 1) * 100
        der_dev = (r["rho_F_derived"]  / r["rho_F_nominal"] - 1) * 100
        ratio_der_obs = r["rho_F_derived"] / r["rho_F_observed"]
        print(f"  {r['atom']:>4} {obs_dev:>+13.3f}% {der_dev:>+13.3f}% "
              f"{ratio_der_obs:>10.5f}")

    witness = {
        "computation": "rho-f-derived-vs-observed",
        "description": (
            "No-fitting check: does the paper's derivation "
            "B = -α·Φ_1 with α = m_e·8G and Φ_1 = Σ ln|V̂_i^full| "
            "reproduce B_AME?  If yes, ρ_F_derived = B_derived/V_hyp "
            "would match ρ_F_observed and the density dichotomy is "
            "automatic from the algebraic volume formula.  If no, the "
            "discrepancy shows where the formula is incomplete."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "q_0": q0, "alpha_MeV": ALPHA_MEV,
        "w_sym": w_sym, "w_std": w_std, "w_alt": w_alt,
        "atoms": results,
    }
    out = Path(__file__).parent / "rho-f-derived-vs-observed.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
