#!/usr/bin/env python3
"""
Atom mass via branching rule + PHYSICAL (positive-chirality) filter
+ JOINT H_{3A}(q) inter-nucleon coupling.

Fixes:
1. Filter to physical (positive) partitions — negative χ terms are
   vacuum/CPT-conjugate states, not observable mass.
2. Replace per-pair Markov-trace heuristic with joint H_{3A}(q) YSN
   action via hecke_core.atom_character_raw (which IS correct).

The "vacuum" partitions are those with χ_free(λ) ≤ 0 — these are
mirror/CPT images that don't contribute to observable matter mass.
Observable mass = sum over partitions with χ > 0 only.
"""
import sys
import math
import json
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from mass_endomorphism import (
    q0, qi0 as qi, z_mark, HA as h,
    proton_cross, neutron_cross, Phi_q,
    mass_from_tower, additive_wedderburn_volumes,
)
from hecke_core import (
    atom_character_raw, _PARTITION_TABLE, K_PARTITION_MAX,
)


def q_int(k):
    return (q0 ** k - qi ** k) / (q0 - qi) if k != 0 else 0.0

def q_fact(n):
    r = 1.0
    for kk in range(1, n + 1):
        r *= q_int(kk)
    return r


def tower_mass_filtered(Z, N, include_inter=True, observable_only=True,
                         k_cap=4):
    """Atom tower mass via partition sum with OBSERVABLE filter.

    For each partition λ ⊢ k (k ≤ k_cap), use hecke_core's joint
    H_{3A}(q) character χ_λ(W_atom) directly.  Filter to observable
    partitions (χ > 0) when observable_only=True.

    k_cap: limit partition size for speed. For heavy atoms, use
    k_cap=4 or 5; for light atoms, up to 8.
    """
    A = Z + N
    if A < 1:
        return {"tower": 0.0, "n_partitions_observable": 0,
                "n_partitions_vacuum": 0}

    active = [e for e in _PARTITION_TABLE
              if e.get('has_ysn', False) and e.get('k', 0) <= k_cap]
    if not active:
        return {"tower": 0.0, "n_partitions_observable": 0,
                "n_partitions_vacuum": 0}

    max_ln = 0.0
    chi_per_lambda = {}
    for entry in active:
        chi_q, ln, dim = atom_character_raw(Z, N, entry,
                                             include_inter=include_inter)
        chi_per_lambda[tuple(entry['partition'])] = {
            'chi': chi_q, 'ln': ln, 'dim': dim, 'entry': entry,
        }
        if ln > max_ln:
            max_ln = ln

    n_obs, n_vac = 0, 0
    total = 0.0
    by_partition = {}
    for lam, data in chi_per_lambda.items():
        chi = data['chi'] * math.exp(data['ln'] - max_ln)
        dim = data['dim']
        w = data['entry'].get('wedderburn_weight', 0)
        contribution = w * chi / dim if dim > 0 else 0.0
        is_observable = chi > 0  # physical filter
        if is_observable:
            n_obs += 1
            if observable_only:
                total += contribution
        else:
            n_vac += 1
            if not observable_only:
                total += contribution
        by_partition[str(lam)] = {
            'chi_rescaled': chi, 'dim': dim, 'weight': w,
            'contribution': contribution, 'observable': is_observable,
        }

    return {
        "tower": total, "n_partitions_observable": n_obs,
        "n_partitions_vacuum": n_vac,
        "by_partition": by_partition,
        "max_ln": max_ln,
    }


# Calibrate E_0 from CODATA m_p (use one-nucleon tower)
_p_vols = additive_wedderburn_volumes(3, proton_cross)
_, _, _, M_PROTON_TOWER = mass_from_tower(_p_vols)
E_0 = 938.272 / M_PROTON_TOWER  # MeV per categorical unit


def binding_filtered(Z, N):
    """Binding with observable-only filter applied.

    B = E_0 · (m_free - m_atom) where both use observable-only
    tower mass sums (CPT-conjugate states filtered out).
    """
    # Per-nucleon shorthand tower masses (from mass_endomorphism)
    A = Z + N
    # Free baseline: sum of per-nucleon towers (each positive, well-defined)
    m_free_tower = 0.0
    p_vols = additive_wedderburn_volumes(3, proton_cross)
    n_vols = additive_wedderburn_volumes(3, neutron_cross)
    _, _, _, m_p = mass_from_tower(p_vols)
    _, _, _, m_n = mass_from_tower(n_vols)
    m_free_tower = Z * m_p + N * m_n

    # Atom: use joint H_{3A}(q) character with observable filter
    atom_data = tower_mass_filtered(Z, N, include_inter=True,
                                    observable_only=True)
    free_data_joint = tower_mass_filtered(Z, N, include_inter=False,
                                           observable_only=True)

    # Normalize: the joint characters are in different units than the
    # per-nucleon tower. We compute the RATIO of observable parts and
    # apply to the free_tower baseline.
    if abs(free_data_joint["tower"]) > 1e-30:
        atom_ratio = atom_data["tower"] / free_data_joint["tower"]
    else:
        atom_ratio = 1.0

    m_atom_tower = m_free_tower * atom_ratio
    B = E_0 * (m_free_tower - m_atom_tower)

    return {
        "Z": Z, "N": N, "A": A,
        "m_free_tower": m_free_tower,
        "m_atom_tower": m_atom_tower,
        "atom_joint_chi_sum": atom_data["tower"],
        "free_joint_chi_sum": free_data_joint["tower"],
        "atom_ratio": atom_ratio,
        "n_observable": atom_data["n_partitions_observable"],
        "n_vacuum": atom_data["n_partitions_vacuum"],
        "B_MeV": B,
    }


if __name__ == "__main__":
    print("ATOM MASS with PHYSICAL FILTER + JOINT H_{3A}(q)")
    print("=" * 92)
    print(f"q₀ = {q0}")
    print(f"E_0 = {E_0:.4e} MeV/cat.unit (from m_p tower)")
    print()
    print(f"Negative-χ partitions = vacuum (CPT-conjugate), filtered out.")
    print(f"Observable mass = Σ_{{χ(λ)>0}} w_λ · χ_λ / d_λ")
    print()

    ATOMS = [
        ("D",    1,  1,   2.22),
        ("T",    1,  2,   8.48),
        ("3He",  2,  1,   7.72),
        ("4He",  2,  2,  28.30),
        ("6Li",  3,  3,  32.00),
    ]  # Limited to A ≤ 6 for now — heavier needs partition truncation (see opts doc)

    print(f"  {'Atom':>6} {'A':>3} {'n_obs':>6} {'n_vac':>6} "
          f"{'m_free (MeV)':>14} {'m_atom (MeV)':>14} "
          f"{'B_pred':>10} {'B_AME':>8} {'|Δm/m|%':>9}")
    print("  " + "-" * 96)
    results = []
    for atom, Z, N, B_AME in ATOMS:
        try:
            r = binding_filtered(Z, N)
            m_free_MeV = E_0 * r["m_free_tower"]
            m_atom_MeV = E_0 * r["m_atom_tower"]
            M_total = A * 938.272 if (A := Z + N) > 0 else 1.0
            dm_m = abs(r["B_MeV"] - B_AME) / M_total * 100 if B_AME != 0 else 0
            print(f"  {atom:>6} {Z+N:>3d} {r['n_observable']:>6d} "
                  f"{r['n_vacuum']:>6d} {m_free_MeV:>14.2f} "
                  f"{m_atom_MeV:>14.2f} {r['B_MeV']:>10.4f} "
                  f"{B_AME:>8.2f} {dm_m:>8.4f}%")
            results.append({**r, "atom": atom, "B_AME_MeV": B_AME,
                            "m_free_MeV": m_free_MeV,
                            "m_atom_MeV": m_atom_MeV,
                            "delta_m_over_m_pct": dm_m})
        except Exception as e:
            print(f"  {atom:>6} ERROR: {e}")

    witness = {
        "computation": "atom-mass-physical-filter",
        "description": (
            "Atom tower mass with PHYSICAL (observable) filter: only "
            "χ_λ(W_atom) > 0 partitions contribute. Negative-χ partitions "
            "are CPT-conjugate vacuum states, filtered out. Uses joint "
            "H_{3A}(q) YSN from hecke_core.atom_character_raw (correct), "
            "not per-pair Markov heuristic. Binding = E_0 · (m_free - m_atom)."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q": q0, "E_0_tower_MeV": E_0, "M_proton_tower": M_PROTON_TOWER,
        },
        "results": results,
    }
    out = Path(__file__).parent / "atom-mass-physical-filter.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
