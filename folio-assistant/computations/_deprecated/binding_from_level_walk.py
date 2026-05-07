#!/usr/bin/env python3
"""
Compute nuclear binding energies using cached level-3 ILP ground states
from confinement-level-walk.witness.json.

The level-3 ILP gives (m_pp, m_pn, m_nn) for each atom — the integer
inter-nucleon crossing multiplicities that minimize |tr_M(W_atom)| at
the nucleon-shorthand level.  Use these to construct the actual atom
braid in the quark-level Hecke algebra and compute tower mass.

Binding energy:
    B = E_0_tower · (𝔪(W_free) - 𝔪(W_atom))
with E_0_tower calibrated from CODATA m_p.
"""
import sys
import json
import math
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from mass_endomorphism import (
    q0, qi0 as qi, z_mark, HA as h, mass_from_tower,
    additive_wedderburn_volumes, proton_cross, neutron_cross,
)
from pyhecke.gram import atom_per_generator_volumes

_proton_vols = additive_wedderburn_volumes(3, proton_cross)
_, _, _, M_PROTON = mass_from_tower(_proton_vols)
E_0 = 938.272 / M_PROTON

WITNESS = Path(__file__).parent / "confinement-level-walk.witness.json"


def atom_tower_from_ilp(Z, N, m_pp, m_pn, m_nn):
    """Compute atom tower mass using ILP-determined multiplicities.

    The Z-before-N ordering puts pp pairs first, then pn boundary,
    then nn pairs. We use the average multiplicity as the effective
    inter-nucleon crossings_per_pair (since the current per-generator
    code uses a single multiplicity).
    """
    A = Z + N
    if A < 2:
        return None
    # Weighted average of multiplicities by pair count
    n_pp = max(0, Z - 1)
    n_pn = 1 if Z > 0 and N > 0 else 0
    n_nn = max(0, N - 1)
    total_pairs = n_pp + n_pn + n_nn
    if total_pairs == 0:
        return None
    total_crossings = n_pp * m_pp + n_pn * m_pn + n_nn * m_nn

    vols_atom = atom_per_generator_volumes(Z, N, include_inter=True,
                                           m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)
    vols_free = atom_per_generator_volumes(Z, N, include_inter=False)
    if not vols_atom or not vols_free:
        return None
    _, _, _, m_atom = mass_from_tower(vols_atom)
    _, _, _, m_free = mass_from_tower(vols_free)
    return {
        "m_pp": m_pp, "m_pn": m_pn, "m_nn": m_nn,
        "total_crossings": total_crossings,
        "total_pairs": total_pairs,
        "m_atom": m_atom, "m_free": m_free,
        "B_MeV": E_0 * (m_free - m_atom),
    }


if __name__ == "__main__":
    print("NUCLEAR BINDING via cached ILP ground states")
    print("=" * 80)
    print(f"E_0_tower = {E_0:.4e} MeV/cat.unit")
    print()

    if not WITNESS.exists():
        print(f"ERROR: cache {WITNESS} not found. Run confinement_level_walk.py first.")
        sys.exit(1)

    w = json.loads(WITNESS.read_text())
    level3 = w["levels"].get("3", {}).get("atoms", {})

    ATOMS_AME = {
        "D": 2.22, "T": 8.48, "3He": 7.72, "4He": 28.30,
        "6Li": 32.00, "7Li": 39.24, "12C": 92.16, "14C": 105.66,
        "16O": 127.62, "20Ne": 160.65,
    }

    print(f"  {'Atom':>6} {'A':>3} {'ILP (pp,pn,nn)':<18} "
          f"{'B_pred':>10} {'B_AME':>8} {'|Δ/B|':>8}")
    print("  " + "-" * 70)
    results = []
    for atom_key, data in level3.items():
        if data.get("unstable"):
            continue
        Z, N = data["Z"], data["N"]
        gs = data["ground_state"]
        r = atom_tower_from_ilp(Z, N, gs["m_pp"], gs["m_pn"], gs["m_nn"])
        if r is None:
            continue
        B_AME = ATOMS_AME.get(atom_key, None)
        ratio = abs(r["B_MeV"] - B_AME) / B_AME if B_AME else None
        ilp_str = f"({gs['m_pp']},{gs['m_pn']},{gs['m_nn']})"
        ratio_str = f"{ratio:.4f}" if ratio is not None else "N/A"
        print(f"  {atom_key:>6} {Z+N:>3d} {ilp_str:<18} "
              f"{r['B_MeV']:>10.4f} {B_AME or 0:>8.2f} "
              f"{ratio_str:>8}")
        results.append({
            "atom": atom_key, "Z": Z, "N": N, "A": Z + N,
            "ilp_ground_state": gs,
            **r,
            "B_AME_MeV": B_AME, "ratio_off_AME": ratio,
        })

    witness = {
        "computation": "binding-from-level-walk",
        "description": (
            "Nuclear binding via level-3 ILP ground states from "
            "confinement-level-walk. For each atom, use the ILP-determined "
            "(m_pp, m_pn, m_nn) as effective inter-nucleon multiplicities, "
            "compute quark-level tower mass, report binding."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q": q0, "E_0_tower_MeV": E_0},
        "results": results,
    }
    out = Path(__file__).parent / "binding-from-level-walk.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
