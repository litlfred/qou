#!/usr/bin/env python3
"""
ADAPTIVE confinement-level unwrap driven by ILP solution count.

Per rem:ilp-solution-count-unwrap:
  unwrap_depth(K, q) = max(0, N_ℓ(K, q) - 1)
where N_ℓ is the number of integer LP solutions at the current
confinement level.

  N_ℓ = 0 → unstable (decay)
  N_ℓ = 1 → uniquely determined, use shorthand (no unwrap)
  N_ℓ = k ≥ 2 → unwrap k-1 levels

For nuclear atoms:
  * Non-magic → N = 1 at nucleon level → use nucleon shorthand
  * Single-magic (Z XOR N magic) → N = 2 → unwrap to quark level on 1 side
  * Double-magic (Z AND N magic) → N ≥ 3 → unwrap to quark level on both

This keeps the Hecke algebra H_n(q) small:
  * Non-magic: n = A (nucleons as single words)
  * Single-magic: n = A + 3·(magic_count) (partial quark unwrap)
  * Double-magic: n = 3A (full quark unwrap)
"""
import sys
import math
import json
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from mass_endomorphism import (
    q0, qi0, z_mark, Phi_q, mass_from_tower,
    additive_wedderburn_volumes, proton_cross, neutron_cross,
    HA as h,
)


MAGIC_NUMBERS = {2, 8, 20, 28, 50, 82, 126}


def ilp_solution_count_nucleon_level(Z, N):
    """Count ILP solutions at the nucleon-shorthand level.

    Heuristic (proxy for Lenstra ILP enumeration):
      * Z magic + N magic → 3 solutions (double magic degeneracy)
      * Z magic XOR N magic → 2 solutions (single magic)
      * Neither magic → 1 solution (unique)
      * A < 2 → 0 solutions (unstable or trivial)

    This is a categorical proxy; the full ILP enumeration per
    Lenstra's algorithm would be strictly correct but expensive.
    """
    A = Z + N
    if A < 2:
        return 0
    z_magic = Z in MAGIC_NUMBERS
    n_magic = N in MAGIC_NUMBERS
    if z_magic and n_magic:
        return 3
    elif z_magic or n_magic:
        return 2
    else:
        return 1


def unwrap_depth(Z, N):
    """Adaptive unwrap depth = max(0, N_ℓ - 1)."""
    n_sol = ilp_solution_count_nucleon_level(Z, N)
    return max(0, n_sol - 1)


def nucleon_tower_mass(nucleon_type):
    """Precomputed tower mass for one proton or neutron (shorthand word)."""
    src = proton_cross if nucleon_type == 'p' else neutron_cross
    vols = additive_wedderburn_volumes(3, src)
    _, _, _, total = mass_from_tower(vols)
    return total, vols


# Precompute per-nucleon tower masses (shorthand)
M_PROTON,  VOLS_PROTON  = nucleon_tower_mass('p')
M_NEUTRON, VOLS_NEUTRON = nucleon_tower_mass('n')

# Calibrate E_0 from CODATA m_p
E_0_TOWER_MEV = 938.272 / M_PROTON


def atom_mass_adaptive(Z, N):
    """Compute atom tower mass using adaptive unwrap depth.

    Returns a dict with mass, unwrap depth, ILP solution count,
    and per-level contributions.
    """
    A = Z + N
    n_sol = ilp_solution_count_nucleon_level(Z, N)
    depth = unwrap_depth(Z, N)

    # Base: sum of per-nucleon shorthand masses (free baseline)
    m_free = Z * M_PROTON + N * M_NEUTRON

    # Nucleon-level contribution: always present
    # Inter-nucleon coupling: A-1 adjacent pairs
    z_sq = z_mark ** 2

    # At depth 0 (non-magic): atom ≈ free − 1 coupling per pair at nucleon level
    # This is a soft coupling: Φ_q(|V_pair|) for each pair.
    # Pair V estimated from product of adjacent nucleon Vs.
    nucleon_types = ['p'] * Z + ['n'] * N

    # Effective per-pair V (geometric mean of nucleon full volumes)
    def pair_V(i):
        nt_i = nucleon_types[i]
        nt_j = nucleon_types[i + 1]
        # Use the "full" V_hat from each nucleon's last generator
        v_i = VOLS_PROTON[1]["full"] if nt_i == 'p' else VOLS_NEUTRON[1]["full"]
        v_j = VOLS_PROTON[0]["full"] if nt_j == 'p' else VOLS_NEUTRON[0]["full"]
        return (v_i * v_j) ** 0.5

    # Level-3 (pair) contribution: adjacent Φ_q cross-term
    level3_contrib = 0.0
    for i in range(A - 1):
        V_pair = pair_V(i)
        if abs(V_pair) < q0:
            level3_contrib += z_sq * Phi_q(abs(V_pair))

    # Level-4 (shell-magic) contribution: only for magic configurations
    # When depth >= 1, the shell-closure operator adds extra structure
    level4_contrib = 0.0
    if depth >= 1:
        # Magic shell closure: effective V at the shell level
        # Approximation: shell V = geometric mean of all pair Vs
        shell_V = sum(pair_V(i) for i in range(A - 1)) / max(A - 1, 1)
        if abs(shell_V) < q0:
            # Shell has A-1 pair couplings with additional Φ_q^2 term
            level4_contrib = (A - 1) * Phi_q(abs(shell_V)) ** 0.5

    # Level-5 (cross-shell) contribution: only for double-magic
    level5_contrib = 0.0
    if depth >= 2:
        # Double magic: both Z and N magic → additional cross-shell coupling
        cross_V = (M_PROTON * M_NEUTRON) ** 0.5 / max(M_PROTON, M_NEUTRON)
        if abs(cross_V) < q0:
            level5_contrib = 2 * Phi_q(abs(cross_V))

    # Atom mass = free - binding contribution
    # (contributions reduce mass, hence subtraction)
    m_atom = m_free - (level3_contrib + level4_contrib + level5_contrib)

    return {
        "Z": Z, "N": N, "A": A,
        "ilp_solutions": n_sol,
        "unwrap_depth": depth,
        "m_free": m_free,
        "m_atom": m_atom,
        "level3_contrib": level3_contrib,
        "level4_contrib": level4_contrib,
        "level5_contrib": level5_contrib,
        "B_MeV": E_0_TOWER_MEV * (m_free - m_atom),
    }


if __name__ == "__main__":
    print("ADAPTIVE CONFINEMENT-LEVEL UNWRAP")
    print("=" * 84)
    print(f"E_0_tower = {E_0_TOWER_MEV:.4e} MeV/cat.unit")
    print(f"Magic numbers: {sorted(MAGIC_NUMBERS)}")
    print()
    print(f"  {'Atom':>6} {'Z':>3} {'N':>3} {'N_ℓ':>4} {'depth':>6} "
          f"{'B_pred':>10} {'B_AME':>8} {'|Δ/B|':>8}")
    print("  " + "-" * 74)

    ATOMS = [
        ("D",    1,  1,   2.22),
        ("T",    1,  2,   8.48),   # N magic (N=2)
        ("3He",  2,  1,   7.72),   # Z magic (Z=2)
        ("4He",  2,  2,  28.30),   # double magic
        ("6Li",  3,  3,  32.00),
        ("7Li",  3,  4,  39.24),
        ("9Be",  4,  5,  58.17),
        ("11B",  5,  6,  76.20),
        ("12C",  6,  6,  92.16),
        ("14C",  6,  8, 105.66),   # N magic
        ("14N",  7,  7, 104.66),
        ("16O",  8,  8, 127.62),   # double magic
        ("20Ne", 10, 10, 160.65),
        ("28Si", 14, 14, 236.54),
        ("40Ca", 20, 20, 342.05),  # double magic
    ]

    results = []
    for atom, Z, N, B_AME in ATOMS:
        r = atom_mass_adaptive(Z, N)
        ratio = abs(r["B_MeV"] - B_AME) / B_AME if B_AME > 0 else 0
        print(f"  {atom:>6} {Z:>3d} {N:>3d} {r['ilp_solutions']:>4d} "
              f"{r['unwrap_depth']:>6d} {r['B_MeV']:>10.4f} "
              f"{B_AME:>8.2f} {ratio:>8.4f}")
        results.append({**r, "atom": atom, "B_AME_MeV": B_AME,
                        "ratio_off_AME": ratio})

    witness = {
        "computation": "confinement-adaptive-unwrap",
        "description": (
            "Adaptive confinement-level unwrap per rem:ilp-solution-count-unwrap. "
            "Unwrap depth = max(0, N_ℓ - 1) where N_ℓ is the ILP solution "
            "count at the current level. Uses Z/N magic-ness as proxy for "
            "ILP solution count (1 non-magic, 2 single-magic, 3 double-magic). "
            "Levels 3 (pair), 4 (shell-magic), 5 (cross-shell) added "
            "adaptively based on depth."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q": q0, "E_0_tower_MeV": E_0_TOWER_MEV,
            "M_proton": M_PROTON, "M_neutron": M_NEUTRON,
            "magic_numbers": sorted(MAGIC_NUMBERS),
        },
        "results": results,
    }
    out = Path(__file__).parent / "confinement-adaptive.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
