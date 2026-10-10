"""
Benzene ring resonance stabilization via cyclic braid at level k.

Computes the energy difference between the ring-closed (cyclic)
and open-chain (linear) Kekulé structures of benzene C₆H₆.

The resonance stabilization arises from the cyclic closure of the
braid: the last bond (C₆-C₁) creates crossing paths that don't
exist in the open chain, redistributing the Wedderburn-weighted
traced volumes across all partitions.

Zero fitted parameters. All from q₀ + Hoefsmit seminormal form.

Results:
  k=5: resonance = 2.13 eV (exp ~1.5 eV, 42% over)
  k=7: resonance = 2.20 eV (47% over)

Usage:
    python3 benzene_resonance.py
"""

import math
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
from level_k_binding import (
    seminormal_matrix, standard_young_tableaux, E_MOL, HA
)
from hoefsmit_witness import load_witness
from witness_base import WitnessBuilder


def _cm(shape, gen, ct):
    M = seminormal_matrix(shape, gen)
    d = M.shape[0]
    if ct == 'pp': return M
    elif ct in ('nn', 'pe', 'bond'): return M - HA * np.eye(d)
    elif ct == 'pn': return M - (HA / 2) * np.eye(d)
    return np.eye(d)


def _carbon_chain(gen):
    """Crossing chain for one carbon atom (Z=6, N=6)."""
    c = []
    for nt in ['p'] * 6 + ['n'] * 6:
        if gen == 0:
            c.extend(['pp'] * 3)
            c.extend(['pp', 'pp'] if nt == 'p' else ['pn', 'pn'])
        else:
            c.extend(['nn'] * 3)
            c.append('pn' if nt == 'p' else 'nn')
    if gen == 0:
        o = ['p'] * 6 + ['n'] * 6
        for i in range(12):
            for j in range(i + 1, 12):
                ti, tj = o[i], o[j]
                c.append('pp' if ti == 'p' and tj == 'p'
                         else ('nn' if ti == 'n' and tj == 'n' else 'pn'))
    if gen == 1:
        c.extend(['pe'] * 6)
    return c


def _bond_chain(gen, order):
    return ['bond'] * (2 * order) if gen == 0 else ['bond'] * order


def benzene_resonance(k=7, max_dim=35):
    """Compute benzene ring resonance at Hecke level k.

    Returns (E_open, E_ring, resonance, details).
    """
    witness = load_witness()
    level = witness['levels'].get(str(k), [])
    if not level:
        return 0.0, 0.0, 0.0, []

    kekule = [2, 1, 2, 1, 2, 1]
    total_ring = 0.0
    total_open = 0.0
    details = []

    for entry in level:
        shape = tuple(entry['shape'])
        w, dim = entry['w'], entry['dim']
        if dim > max_dim:
            continue

        tabs = standard_young_tableaux(shape)
        d = len(tabs)
        if d == 0:
            continue

        part_ring, part_open = 0.0, 0.0
        for gen in [0, 1]:
            C = _carbon_chain(gen)

            M_free = np.eye(d)
            for i in range(6):
                for ct in C:
                    M_free = M_free @ _cm(shape, gen, ct)

            M_open = np.eye(d)
            for i in range(6):
                for ct in C:
                    M_open = M_open @ _cm(shape, gen, ct)
                if i < 5:
                    for ct in _bond_chain(gen, kekule[i]):
                        M_open = M_open @ _cm(shape, gen, ct)

            M_ring = np.eye(d)
            for i in range(6):
                for ct in C:
                    M_ring = M_ring @ _cm(shape, gen, ct)
                for ct in _bond_chain(gen, kekule[i]):
                    M_ring = M_ring @ _cm(shape, gen, ct)

            tf = abs(float(np.trace(M_free)))
            to = abs(float(np.trace(M_open)))
            tr = abs(float(np.trace(M_ring)))

            if tf > 1e-300 and to > 1e-300 and tr > 1e-300:
                part_open += abs(math.log(tf) - math.log(to))
                part_ring += abs(math.log(tf) - math.log(tr))

        total_open += w * part_open
        total_ring += w * part_ring
        details.append({
            'shape': shape, 'w': w, 'dim': dim,
            'open': part_open, 'ring': part_ring,
        })

    E_open = total_open * E_MOL
    E_ring = total_ring * E_MOL
    resonance = E_ring - E_open

    return E_open, E_ring, resonance, details


if __name__ == "__main__":
    print("Benzene ring resonance stabilization")
    print(f"E_MOL = {E_MOL:.4f} eV, zero fitted parameters")
    print()

    for k in [3, 5, 7]:
        t0 = time.monotonic()
        E_open, E_ring, resonance, details = benzene_resonance(k=k)
        elapsed = time.monotonic() - t0
        n = len(details)
        print(f"k={k:>2d}: {n:>3d} partitions, open={E_open:.2f}, "
              f"ring={E_ring:.2f}, resonance={resonance:+.2f} eV "
              f"(exp ~1.5) [{elapsed:.1f}s]")

    print()
    print("Experimental benzene resonance: ~1.5 eV (36 kcal/mol)")

    # Save witness
    w = WitnessBuilder("benzene-resonance", engine="python")
    w.set_description(
        "Benzene ring resonance stabilization from cyclic braid "
        "at Hecke levels k=3,5,7. The resonance energy is the "
        "difference between ring-closed and open-chain Kekulé "
        "structures. Zero fitted parameters."
    )

    for k in [3, 5, 7]:
        E_o, E_r, res, _ = benzene_resonance(k=k)
        w.add_data(f"k{k}", {
            "E_open_eV": round(E_o, 4),
            "E_ring_eV": round(E_r, 4),
            "resonance_eV": round(res, 4),
        })

    w.add_assertion(
        "Benzene resonance at k=5",
        computed=round(benzene_resonance(k=5)[2], 2),
        expected=1.5,
        tolerance=1.0,
        unit="eV",
        source="Experimental resonance energy ~36 kcal/mol",
    )
    w.save()
