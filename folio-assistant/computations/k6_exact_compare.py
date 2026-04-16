#!/usr/bin/env python3
"""
Compare k=5, k=6 (first-order formulas), and k=6 (exact characters)
on the AME2020 nuclei set. Reports MAE (percent) and RMS (MeV).

Exact character engine: for each partition λ⊢6, compute
    m_λ(Z,N) = w_λ · χ_λ(Z,N) / dim_λ · m_e
where χ_λ is the trace in irrep λ of the inter-nucleon crossing chain
    Π_{0≤i<j<A} (σ_g + d_ij · I), g = (i+j) mod 5, d_ij ∈ {0, -h, -h/2}.

Sum over all 11 partitions of 6 → total k=6 correction (replaces the
three first-order formulas at hecke_core.py:1040-1042).
"""
import math
import sys
from pathlib import Path
from functools import lru_cache

sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
from q_parameter import Q as q0, Q_INV as qi, HA
from experimental_constants import M_E_MEV
from level_k_binding import standard_young_tableaux, seminormal_matrix
from hoefsmit_witness import load_witness
from hecke_core import binding_energy_bw, atom_mass


AME2020 = [
    (1,0,'H',938.272),(2,2,'He',3727.379),(3,4,'Li',6533.833),
    (4,5,'Be',8392.751),(5,6,'B',10252.548),(6,6,'C',11174.863),
    (7,7,'N',13040.204),(8,8,'O',14895.081),(9,10,'F',17692.302),
    (10,10,'Ne',18617.730),(11,12,'Na',21409.214),(12,12,'Mg',22335.793),
    (13,14,'Al',25126.501),(14,14,'Si',26053.188),(15,16,'P',28844.211),
    (16,16,'S',29773.619),(17,18,'Cl',32564.593),(18,22,'Ar',37215.526),
    (19,20,'K',36284.754),(20,20,'Ca',37214.698),
    (21,24,'Sc',41862.228),(22,26,'Ti',44563.636),(23,28,'V',47449.459),
    (24,28,'Cr',48441.703),(25,30,'Mn',51147.752),(26,30,'Fe',52089.780),
    (27,32,'Co',54858.006),(28,30,'Ni',53950.826),(29,34,'Cu',58604.360),
    (30,34,'Zn',59544.152),
    (43,56,'Tc',92056.660),(50,70,'Sn',111662.639),
    (82,126,'Pb',193687.122),(92,146,'U',221695.893),
]


# ── Exact k=6 character engine ──────────────────────────────────

def _nuclear_ordering(Z, N):
    ordering = []
    pc = nc = 0
    for k in range(Z + N):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            ordering.append(1); pc += 1
        else:
            ordering.append(0); nc += 1
    return tuple(ordering)


@lru_cache(maxsize=2048)
def _k6_correction_mev(Z, N):
    """Sum of per-partition Markov contributions for k=6 (MeV).

    Replaces the three first-order formulas DELTA_W2, DELTA_411, DELTA_42
    with the exact symbolic-character evaluation at q₀.
    """
    A = Z + N
    if A < 2:
        return 0.0

    witness = load_witness()
    level = witness['levels'].get('6', [])
    n_gens = 5

    ordering = _nuclear_ordering(Z, N)
    total = 0.0

    for entry in level:
        shape = tuple(entry['shape'])
        dim = entry['dim']
        w = entry['w']
        if dim == 0:
            continue

        sigmas = [seminormal_matrix(shape, g) for g in range(n_gens)]
        I = np.eye(dim)
        M = np.eye(dim)

        for i in range(A - 1):
            for j in range(i + 1, A):
                ti, tj = ordering[i], ordering[j]
                if ti == 1 and tj == 1:
                    shift = 0.0
                elif ti == 0 and tj == 0:
                    shift = -HA
                else:
                    shift = -HA / 2
                g = (i + j) % n_gens
                M = M @ (sigmas[g] + shift * I)

        chi = float(np.trace(M))
        total += w * chi / dim

    return total * M_E_MEV


def binding_energy_bw_k6_exact(Z, N, is_fig8=False):
    """k=6 binding energy with exact character correction for k=6 terms."""
    # Start with k=5 binding (all terms up through H₅(q))
    B5 = binding_energy_bw(Z, N, k=5)
    # Add exact k=6 Markov trace (replaces DELTA_W2/411/42 first-order)
    if not is_fig8:
        B5 += _k6_correction_mev(Z, N)
    return B5


# ── Mass and error computation ──────────────────────────────────

def _atom_mass_with_k(Z, N, k=5, use_exact_k6=False):
    from hecke_core import M_P_MEV, M_N_MEV
    M_const = Z * M_P_MEV + N * M_N_MEV + Z * M_E_MEV
    if use_exact_k6:
        B = binding_energy_bw_k6_exact(Z, N)
    else:
        B = binding_energy_bw(Z, N, k=k)
    return M_const - B


def _evaluate(label, mass_fn):
    errs_pct = []
    errs_mev = []
    for Z, N, sym, obs in AME2020:
        M = mass_fn(Z, N)
        errs_pct.append((M - obs) / obs * 100)
        errs_mev.append(M - obs)
    mae = sum(abs(e) for e in errs_pct) / len(errs_pct)
    rms = math.sqrt(sum(e*e for e in errs_mev) / len(errs_mev))
    worst = max(AME2020, key=lambda row: abs(mass_fn(row[0], row[1]) - row[3]))
    worst_e = mass_fn(worst[0], worst[1]) - worst[3]
    print(f"{label:>28s}  MAE={mae:.5f}%  RMS={rms:.4f} MeV  "
          f"worst={worst[2]} ({worst_e:+.2f} MeV)")
    return mae, rms


def main():
    print(f"{'='*72}")
    print(f"k=6 RESIDUAL COMPARISON: first-order scalings vs exact characters")
    print(f"  {len(AME2020)} AME2020 nuclei, q₀={q0:.8f}")
    print(f"{'='*72}")

    _evaluate("k=5 baseline",
              lambda Z, N: _atom_mass_with_k(Z, N, k=5))
    _evaluate("k=6 current (first-order)",
              lambda Z, N: _atom_mass_with_k(Z, N, k=6))
    _evaluate("k=6 EXACT characters",
              lambda Z, N: _atom_mass_with_k(Z, N, use_exact_k6=True))

    # Per-nucleus breakdown on a subset
    print(f"\n{'='*72}")
    print("PER-NUCLEUS CORRECTION (MeV): current first-order vs exact characters")
    print(f"{'='*72}")
    print(f"{'atom':>6s} {'A':>3s}  {'Δ_current [MeV]':>18s} {'Δ_exact [MeV]':>16s} "
          f"{'diff [keV]':>13s}")
    print("-" * 72)
    for Z, N, sym, obs in AME2020[:15]:
        B5 = binding_energy_bw(Z, N, k=5)
        B6 = binding_energy_bw(Z, N, k=6)
        delta_current = B6 - B5
        delta_exact = _k6_correction_mev(Z, N)
        diff_kev = (delta_exact - delta_current) * 1000
        print(f"{sym:>6s} {Z+N:>3d}  {delta_current:>18.6f} "
              f"{delta_exact:>16.6f} {diff_kev:>+13.3f}")


if __name__ == "__main__":
    main()
