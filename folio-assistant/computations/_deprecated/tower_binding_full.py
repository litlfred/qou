#!/usr/bin/env python3
"""
Full tower binding: use prop:mass-endomorphism-tower for BOTH atom and free.

For each atom:
  1. Get ILP ground state (m_pp, m_pn, m_nn) from level-walk cache.
  2. Build per-generator V̂_i via atom_per_generator_volumes.
  3. Apply tower formula: 𝔪 = |Π V̂| + Σ Φ_q(|V̂|) + z² Σ_{adj} Φ_q(|V̂V̂|)
     (via mass_from_tower in mass_endomorphism).
  4. B = E_0 · (𝔪_free - 𝔪_atom) with E_0 from m_p tower calibration.

Binding comes from the Φ_q cross-terms that shell-structure generators
contribute — this is what level 4+ provides.

The tower formula is ADDITIVE (sum terms grow linearly in A), unlike the
single-level |tr_M| which is multiplicative and underflows.
"""
import sys
import math
import json
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from mass_endomorphism import (
    q0, mass_from_tower, additive_wedderburn_volumes, proton_cross,
)
from pyhecke.gram import atom_per_generator_volumes

_p_vols = additive_wedderburn_volumes(3, proton_cross)
_, _, _, M_PROTON_TOWER = mass_from_tower(_p_vols)
E_0 = 938.272 / M_PROTON_TOWER

WALK_CACHE = Path(__file__).parent / "confinement-level-walk.witness.json"


def get_ilp_ground(Z, N):
    """Get (m_pp, m_pn, m_nn) from level-walk cache, default (1,1,1)."""
    if not WALK_CACHE.exists():
        return {"m_pp": 1, "m_pn": 1, "m_nn": 1}
    w = json.loads(WALK_CACHE.read_text())
    atoms = w.get("levels", {}).get("3", {}).get("atoms", {})
    # Find by (Z, N)
    for atom_key, data in atoms.items():
        if data.get("Z") == Z and data.get("N") == N and not data.get("unstable"):
            return data["ground_state"]
    return {"m_pp": 1, "m_pn": 1, "m_nn": 1}


def tower_binding(Z, N, m_pp, m_pn, m_nn):
    """Full tower binding with ILP-determined multiplicities."""
    vols_atom = atom_per_generator_volumes(
        Z, N, include_inter=True,
        m_pp=m_pp, m_pn=m_pn, m_nn=m_nn)
    vols_free = atom_per_generator_volumes(Z, N, include_inter=False)
    if not vols_atom or not vols_free:
        return None
    desc_a, sgl_a, cross_a, total_a = mass_from_tower(vols_atom)
    desc_f, sgl_f, cross_f, total_f = mass_from_tower(vols_free)
    return {
        "Z": Z, "N": N, "A": Z + N,
        "m_pp": m_pp, "m_pn": m_pn, "m_nn": m_nn,
        "m_free_tower": total_f,
        "m_atom_tower": total_a,
        "m_free_breakdown": {"desc": desc_f, "single": sgl_f, "cross": cross_f},
        "m_atom_breakdown": {"desc": desc_a, "single": sgl_a, "cross": cross_a},
        "B_MeV": E_0 * (total_f - total_a),
    }


if __name__ == "__main__":
    print("FULL TOWER BINDING (prop:mass-endomorphism-tower for both atom/free)")
    print("=" * 116)
    print(f"q₀ = {q0}")
    print(f"E_0 = {E_0:.4e} MeV/cat.unit (from m_p tower → 938.272 MeV)")
    print()

    ATOMS = [
        ("D",    1,  1,    2.22),
        ("T",    1,  2,    8.48),
        ("3He",  2,  1,    7.72),
        ("4He",  2,  2,   28.30),
        ("6Li",  3,  3,   32.00),
        ("7Li",  3,  4,   39.24),
        ("9Be",  4,  5,   58.17),
        ("10B",  5,  5,   64.75),
        ("11B",  5,  6,   76.20),
        ("12C",  6,  6,   92.16),
        ("13C",  6,  7,   97.11),
        ("14C",  6,  8,  105.66),
        ("14N",  7,  7,  104.66),
        ("15N",  7,  8,  115.49),
        ("16O",  8,  8,  127.62),
        ("17O",  8,  9,  131.76),
        ("18O",  8, 10,  139.81),
        ("19F",  9, 10,  147.80),
        ("20Ne", 10, 10, 160.65),
        ("22Ne", 10, 12, 177.77),
        ("23Na", 11, 12, 186.56),
        ("24Mg", 12, 12, 198.26),
        ("27Al", 13, 14, 224.95),
        ("28Si", 14, 14, 236.54),
        ("32S",  16, 16, 271.78),
        ("40Ca", 20, 20, 342.05),
        ("48Ca", 20, 28, 416.00),
        ("56Fe", 26, 30, 492.25),
    ]

    print(f"  {'Atom':>6} {'Z':>3} {'N':>3} {'A':>3} "
          f"{'(pp,pn,nn)':>12} {'m_free':>11} {'m_atom':>11} "
          f"{'B_pred':>10} {'B_AME':>8} {'B_err':>8} {'|Δm/m|%':>9} "
          f"{'B/A_pred':>9} {'B/A_AME':>9}")
    print("  " + "-" * 114)

    results = []
    for atom, Z, N, B_AME in ATOMS:
        gs = get_ilp_ground(Z, N)
        r = tower_binding(Z, N, gs["m_pp"], gs["m_pn"], gs["m_nn"])
        if r is None:
            continue
        A = Z + N
        M_total = A * 938.272
        dm_m = abs(r["B_MeV"] - B_AME) / M_total * 100
        B_err = r["B_MeV"] - B_AME
        Bpa = r["B_MeV"] / A
        B_AME_pa = B_AME / A
        ilp_str = f"({gs['m_pp']},{gs['m_pn']},{gs['m_nn']})"
        print(f"  {atom:>6} {Z:>3d} {N:>3d} {A:>3d} {ilp_str:>12} "
              f"{r['m_free_tower']:>11.3e} {r['m_atom_tower']:>11.3e} "
              f"{r['B_MeV']:>10.3f} {B_AME:>8.2f} {B_err:>+8.3f} "
              f"{dm_m:>8.4f}% {Bpa:>9.3f} {B_AME_pa:>9.3f}")
        results.append({
            **r, "atom": atom, "B_AME_MeV": B_AME, "M_atom_MeV": M_total,
            "B_err_MeV": B_err, "delta_m_over_m_pct": dm_m,
            "B_per_A_pred": Bpa, "B_per_A_AME": B_AME_pa,
        })

    dms = [r["delta_m_over_m_pct"] for r in results]
    print()
    print(f"|Δm/m|% summary:  min={min(dms):.4f}%, max={max(dms):.4f}%, "
          f"mean={sum(dms)/len(dms):.4f}%")

    # Trend analysis
    print()
    print("Trend by A-bucket:")
    buckets = {"A≤10": [], "A∈[11,20]": [], "A∈[21,40]": [], "A>40": []}
    for r in results:
        A = r["A"]
        if A <= 10:
            buckets["A≤10"].append(r["delta_m_over_m_pct"])
        elif A <= 20:
            buckets["A∈[11,20]"].append(r["delta_m_over_m_pct"])
        elif A <= 40:
            buckets["A∈[21,40]"].append(r["delta_m_over_m_pct"])
        else:
            buckets["A>40"].append(r["delta_m_over_m_pct"])
    for b, v in buckets.items():
        if v:
            print(f"  {b:>12}: n={len(v)}, mean={sum(v)/len(v):.4f}%, "
                  f"max={max(v):.4f}%")

    witness = {
        "computation": "tower-binding-full",
        "description": (
            "Full tower binding per prop:mass-endomorphism-tower for both "
            "atom and free. Uses level-walk ILP (m_pp, m_pn, m_nn) ground "
            "states + atom_per_generator_volumes + mass_from_tower. "
            "B = E_0 · (𝔪_free - 𝔪_atom)."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {"q": q0, "E_0_tower_MeV": E_0},
        "results": results,
        "summary": {
            "min_dm_m_pct": min(dms), "max_dm_m_pct": max(dms),
            "mean_dm_m_pct": sum(dms) / len(dms),
        },
    }
    out = Path(__file__).parent / "tower-binding-full.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
