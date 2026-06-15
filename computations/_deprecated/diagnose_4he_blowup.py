#!/usr/bin/env python3
"""
34a: Diagnose ⁴He +354% blowup in strict 3-cal Markov-invariant prediction.

Per-partition table at H_12 showing each (λ, χ_λ, w_λ, log|χ_λ|, w_λ·log|χ_λ|).
Identify which partition(s) drive the divergence.
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
import numpy as np
mp.mp.dps = 30

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from hecke_characters import (
    build_seminormal_matrices, nuclear_braid_character,
    partitions_of, dim_q, qfac
)

Q0 = Q_MP  # was f64 roundtrip

# ⁴He: Z=2, N=2, A=4, n=12
Z, N = 2, 2
n = 12
n_gens = n - 1

print(f"⁴He at H_{n}: Z={Z}, N={N}, n_gens={n_gens}")
print()
print(f"  {'partition':<28} {'depth':>5} {'dim_q':>10} {'chi':>15} {'w_lambda':>14} {'log|chi|':>12} {'w·log':>14}")
print("-" * 120)

contribs = []
for shape in partitions_of(n):
    try:
        sigmas, dim_lam, _ = build_seminormal_matrices(shape)
        if dim_lam == 0: continue
        chi = float(nuclear_braid_character(Z, N, sigmas, dim_lam, n_gens))
        d = float(dim_q(shape))
        w = d*d / float(qfac(n))
        log_chi = float(np.log(abs(chi))) if abs(chi) > 1e-30 else float('-inf')
        contrib = w * log_chi if abs(chi) > 1e-30 else 0
        contribs.append((shape, len(shape)-1, d, chi, w, log_chi, contrib))
    except Exception as e:
        contribs.append((shape, len(shape)-1, None, None, None, None, None))

# Sort by absolute contribution
contribs.sort(key=lambda c: abs(c[6]) if c[6] is not None else 0, reverse=True)

for shape, depth, d, chi, w, log_chi, contrib in contribs[:25]:
    if contrib is None:
        print(f"  {str(shape):<28} {depth:>5} (build failed)")
        continue
    print(f"  {str(shape):<28} {depth:>5} {d:>10.4e} {chi:>+15.6e} {w:>14.4e} {log_chi:>+12.4f} {contrib:>+14.4f}")

# Total
total = sum(c[6] for c in contribs if c[6] is not None)
print()
print(f"  Σ w_λ · log|χ_λ| (= total structural sum at depth-mixed) = {total:+.6f}")
print(f"  Σ w_λ                                                     = {sum(c[4] for c in contribs if c[4] is not None):+.6f}")
print()

# Bin by depth
print(f"{'depth':>6} {'n_part':>7} {'Σ w_λ':>14} {'Σ w_λ·log|χ_λ|':>18}")
print("-" * 60)
by_depth = {}
for shape, depth, d, chi, w, log_chi, contrib in contribs:
    if contrib is None: continue
    by_depth.setdefault(depth, []).append((w, contrib))
for depth in sorted(by_depth):
    parts = by_depth[depth]
    sum_w = sum(p[0] for p in parts)
    sum_contrib = sum(p[1] for p in parts)
    print(f"{depth:>6} {len(parts):>7} {sum_w:>14.6e} {sum_contrib:>+18.6f}")

out_path = Path(__file__).parent / "diagnose-4he-blowup.witness.json"
contribs_serializable = [
    {"shape": list(c[0]), "depth": c[1],
     "dim_q": c[2], "chi": c[3], "w_lambda": c[4],
     "log_chi": c[5] if c[5] != float('-inf') else None,
     "contribution": c[6]}
    for c in contribs
]
with open(out_path, "w") as fp:
    json.dump({
        "computation": "diagnose-4he-blowup",
        "description": "Per-partition Hoefsmit χ_λ(β_⁴He) at H_12 to identify which partition drives the +354% structural blowup.",
        "isotope": "⁴He", "Z": Z, "N": N, "A": 4, "n": n,
        "contributions_sorted_by_abs": contribs_serializable
    }, fp, indent=2)
print(f"\nWitness: {out_path}")
