#!/usr/bin/env python3
"""
NF transition lifting: track how the NF changes at each nucleon
addition and decompose into Wedderburn channels.

At each step k, adding nucleon k introduces:
  1. Intra-nucleon crossings (B₃ + quarks + gluon) — fixed per type
  2. Inter-nucleon crossings with all previous nucleons — topology

The transition's std channel V_std decomposes the confinement:
  - Proton additions: V_new > 1 (pp crossings add chirality)
  - Neutron additions: V_new < 1 (nn crossings reduce chirality)

Key finding: the neutron-step V_new decays geometrically with
ratio → W_STD (the standard Wedderburn weight). This is the
same convergence as the jet-filtered per-level invariant.

The R_std = V_std(full)/V_std(free) tracks the cumulative
confinement across all steps. Its relationship to the BW knot
factor is mediated by the BW polynomial structure.

Usage:
    python3 nf_transition_lifting.py
"""
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import math
import numpy as np
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from hecke_core import h, z, q0, qi, W_SYM, W_STD, W_ALT, hm
from witness_base import WitnessBuilder

h_val = h


def vstd_chain(chain):
    a, b = 0.0, 1.0
    for c, d in chain:
        a, b = a * c * h_val + a * d + b * c, a * c + b * d
    return z * a + b


def build_transitions(Z, N):
    A = Z + N
    ordering = []
    pc, nc = 0, 0
    for k in range(A):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            ordering.append('p')
            pc += 1
        else:
            ordering.append('n')
            nc += 1

    g0_full, g0_free = [], []
    steps = []

    for k in range(A):
        nuc = ordering[k]
        if nuc == 'p':
            intra = [(1, 0)] * 3 + [(1, 0)] + [(1, -h_val / 2)] + [(1, 0)] * 2
        else:
            intra = [(1, 0)] * 3 + [(1, -h_val / 2)] * 2 + [(1, 0)] * 2
        g0_full.extend(intra)
        g0_free.extend(intra)

        new_inter = []
        for prev in range(k):
            ti, tj = ordering[prev], ordering[k]
            if ti == 'p' and tj == 'p':
                new_inter.append((1, 0))
            elif ti == 'n' and tj == 'n':
                new_inter.append((1, -h_val))
            else:
                new_inter.append((1, -h_val / 2))
        g0_full.extend(new_inter)

        V_full = vstd_chain(g0_full)
        V_free = vstd_chain(g0_free)
        V_new = vstd_chain(new_inter) if new_inter else 1.0
        R_std = V_full / V_free if abs(V_free) > 1e-300 else 0

        Z_k = sum(1 for x in ordering[:k + 1] if x == 'p')
        N_k = k + 1 - Z_k
        n_pp = sum(1 for _, d in new_inter if d == 0)
        n_nn = sum(1 for _, d in new_inter if abs(d + h_val) < 1e-10)
        n_pn = len(new_inter) - n_pp - n_nn

        steps.append({
            'A': k + 1, 'Z': Z_k, 'N': N_k, 'nuc': nuc,
            'n_pp': n_pp, 'n_nn': n_nn, 'n_pn': n_pn,
            'V_new': round(V_new, 8),
            'R_std': round(R_std, 8),
        })

    return steps


ATOMS = [
    ("²H", 1, 1), ("³H", 1, 2), ("⁴He", 2, 2),
    ("⁶Li", 3, 3), ("⁷Li", 3, 4),
    ("¹²C", 6, 6), ("¹⁶O", 8, 8),
]

all_data = {}
for name, Z, N in ATOMS:
    steps = build_transitions(Z, N)
    all_data[name] = steps

    print(f"=== {name} (Z={Z}, N={N}) ===")
    for s in steps:
        print(
            f"  A={s['A']} {s['nuc']} "
            f"pp={s['n_pp']} nn={s['n_nn']} pn={s['n_pn']} "
            f"V_new={s['V_new']:+.4f} R_std={s['R_std']:.6f}"
        )

    # Neutron-step V_new decay ratios
    n_steps = [s for s in steps if s['nuc'] == 'n' and s['A'] > 1]
    if len(n_steps) >= 2:
        ratios = []
        for i in range(1, len(n_steps)):
            if abs(n_steps[i - 1]['V_new']) > 1e-10:
                ratios.append(n_steps[i]['V_new'] / n_steps[i - 1]['V_new'])
        if ratios:
            print(f"  Neutron V_new decay ratios: {[round(r, 4) for r in ratios]}")
            print(f"  W_STD = {W_STD:.4f} (expected convergence target)")
    print()

# Witness
w = WitnessBuilder("nf-transition-lifting", engine="python")
w.set_description(
    "NF transition lifting: per-step Wedderburn channel decomposition "
    "during atom construction. Proton steps increase R_std (pp chirality), "
    "neutron steps decrease (nn cancellation). Neutron-step V_new decays "
    "geometrically with ratio → W_STD. R_std = V_std(full)/V_std(free) "
    "tracks cumulative confinement."
)
w.set_content_block("conj:jet-filtered-knot-factor")
w.add_parameter("q", q0)
w.add_parameter("W_STD", W_STD)
for name, Z, N in ATOMS:
    w.add_data(name, all_data[name])
w.save()
