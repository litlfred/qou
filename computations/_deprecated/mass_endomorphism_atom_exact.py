#!/usr/bin/env python3
"""
EXACT per-generator atom tower mass.

Uses hecke_core.atom_per_generator_volumes(Z, N) to compute the
true per-generator V̂_i^full for the atom braid (no interpolation,
no calibration beyond E_0_tower from CODATA m_p).

Tower formula (prop:mass-endomorphism-tower):
    𝔪(W) = |Π V̂_i| + Σ Φ_q(|V̂_i|)
          + z² Σ_{|i-j|=1} Φ_q(|V̂_i V̂_j|)

Free baseline: per-nucleon disjoint computation (intra only).
Atom: full joint braid with pp/nn/pn inter-nucleon crossings.

Binding: B = E_0_tower · (𝔪(W_free) - 𝔪(W_atom))

E_0_tower calibrated from CODATA m_p = 938.272 MeV.
"""
import sys
import math
import json
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from pyhecke.gram import atom_per_generator_volumes
from mass_endomorphism import (
    q0, qi0, z_mark, Phi_q, mass_from_tower,
    additive_wedderburn_volumes, proton_cross,
)


# Calibrate E_0_tower from CODATA m_p
_proton_vols = additive_wedderburn_volumes(3, proton_cross)
_, _, _, M_PROTON_TOWER = mass_from_tower(_proton_vols)
E_0_TOWER_MEV = 938.272 / M_PROTON_TOWER


def atom_tower_mass_exact(Z, N, include_inter=True):
    """Tower mass via exact per-generator V̂_i."""
    vols = atom_per_generator_volumes(Z, N, include_inter=include_inter)
    if not vols:
        return {"desc": 0.0, "single": 0.0, "cross": 0.0, "total": 0.0,
                "n_gens": 0}
    desc, single, cross, total = mass_from_tower(vols)
    return {
        "desc": desc, "single": single, "cross": cross, "total": total,
        "n_gens": len(vols),
    }


def binding_exact(Z, N):
    A = Z + N
    m_atom = atom_tower_mass_exact(Z, N, include_inter=True)
    m_free = atom_tower_mass_exact(Z, N, include_inter=False)
    B = E_0_TOWER_MEV * (m_free["total"] - m_atom["total"])
    return {
        "Z": Z, "N": N, "A": A,
        "m_atom_total": m_atom["total"],
        "m_atom_n_gens": m_atom["n_gens"],
        "m_free_total": m_free["total"],
        "m_free_n_gens": m_free["n_gens"],
        "B_MeV": B,
    }


if __name__ == "__main__":
    print("EXACT PER-GENERATOR TOWER MASS (no interpolation)")
    print("=" * 72)
    print(f"q₀ = {q0}")
    print(f"E_0_tower = {E_0_TOWER_MEV:.4e} MeV/cat.unit (from CODATA m_p)")
    print()
    print(f"  {'Atom':>6} {'A':>3} {'B_AME':>8} "
          f"{'n_gen':>6} {'𝔪_atom':>12} {'𝔪_free':>12} "
          f"{'B_pred':>10} {'|Δ/B|':>8}")
    print("  " + "-" * 70)

    ATOMS = [
        ("D",    1,  1,   2.22),
        ("T",    1,  2,   8.48),
        ("3He",  2,  1,   7.72),
        ("4He",  2,  2,  28.30),
        ("6Li",  3,  3,  32.00),
        ("7Li",  3,  4,  39.24),
        ("9Be",  4,  5,  58.17),
        ("11B",  5,  6,  76.20),
        ("12C",  6,  6,  92.16),
        ("14N",  7,  7, 104.66),
        ("16O",  8,  8, 127.62),
        ("20Ne", 10, 10, 160.65),
    ]

    results = []
    for atom, Z, N, B_AME in ATOMS:
        try:
            r = binding_exact(Z, N)
            ratio = abs(r["B_MeV"] - B_AME) / B_AME if B_AME > 0 else 0
            print(f"  {atom:>6} {Z+N:>3d} {B_AME:>8.2f} "
                  f"{r['m_atom_n_gens']:>6d} "
                  f"{r['m_atom_total']:>12.4e} {r['m_free_total']:>12.4e} "
                  f"{r['B_MeV']:>10.4f} {ratio:>8.4f}")
            results.append({**r, "atom": atom, "B_AME_MeV": B_AME,
                            "ratio_off_AME": ratio})
        except Exception as e:
            print(f"  {atom:>6} ERROR: {e}")

    witness = {
        "computation": "mass-endomorphism-atom-exact-per-generator",
        "description": (
            "Exact per-generator V̂_i^full for atom braid via "
            "hecke_core.atom_per_generator_volumes. Tower formula "
            "𝔪 = |ΠV̂| + ΣΦ_q(|V̂|) + z²ΣΦ_q(|V̂V̂|). "
            "Single archimedean calibration E_0 from CODATA m_p. "
            "No interpolation, no per-atom calibration."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q": q0, "M_proton_tower": M_PROTON_TOWER,
            "E_0_tower_MeV": E_0_TOWER_MEV,
            "z_mark": z_mark, "z_squared": z_mark**2,
        },
        "results": results,
    }
    out = Path(__file__).parent / "mass-endomorphism-atom-exact.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
