#!/usr/bin/env python3
"""
LP DUAL: Crossing operator selection for atomic braids.

For the atomic braid H_{A+Z}(q) with strands [p, n, e], there are
C(n,2) crossings. Each crossing (i,k) has type (pp, nn, pn, pe, ne, ee)
and contributes to the final F_Pauli value.

This script computes the SENSITIVITY of F_Pauli to each crossing:
  δF_i = F_Pauli(all crossings) - F_Pauli(without crossing i)

Crossings with |δF_i| < ε can be dropped without significant loss.
The LP dual identifies the MINIMAL set of crossings needed.

Uses the Python transfer matrix (2×2 traced volume) for speed.
No NF expansion — just the scalar Markov trace.

Usage:
    python3 computations/atom_crossing_lp.py
"""

import math, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0

HA = q0 - 1.0 / q0
z = 1.0 / (q0**0.5 + q0**(-0.5))


def crossing_coeff(ti, tj):
    """Return (c, d) for strand types."""
    if ti == 'p' and tj == 'p': return 1.0, 0.0, 'pp'
    if ti == 'n' and tj == 'n': return 1.0, -HA, 'nn'
    if (ti == 'p' and tj == 'n') or (ti == 'n' and tj == 'p'):
        return 1.0, -HA/2, 'pn'
    if (ti == 'p' and tj == 'e') or (ti == 'e' and tj == 'p'):
        return 1.0, -HA, 'pe'
    if (ti == 'n' and tj == 'e') or (ti == 'e' and tj == 'n'):
        return 0.0, 1.0, 'ne'  # identity
    if ti == 'e' and tj == 'e': return 1.0, 0.0, 'ee'
    return 0.0, 1.0, '??'


def compute_Phi_selective(ordering, skip_crossings=set()):
    """Compute Φ_q with optional crossing omission.
    skip_crossings: set of (i,k) pairs to skip (treat as identity)."""
    n = len(ordering)
    if n <= 1: return 0.0, []
    Phi = 0.0
    crossing_details = []
    for gen in range(n - 1):
        a, b = 0.0, 1.0
        for j in range(gen + 1, n):
            c, d, ctype = crossing_coeff(ordering[gen], ordering[j])
            if (gen, j) in skip_crossings:
                c, d = 0.0, 1.0  # identity
            if c == 0.0 and d == 1.0:
                continue
            a, b = a * c * HA + a * d + b * c, a * c + b * d
        V = z * a + b
        if abs(V) < 1e-300:
            return float('inf'), crossing_details
        Phi += math.log(abs(V))
        crossing_details.append((gen, V))
    return Phi, crossing_details


def enumerate_crossings(ordering):
    """List all non-trivial crossings with their types."""
    n = len(ordering)
    crossings = []
    for i in range(n):
        for k in range(i + 1, n):
            c, d, ctype = crossing_coeff(ordering[i], ordering[k])
            if c == 0.0 and d == 1.0:
                continue  # skip identity crossings
            crossings.append((i, k, ctype, c, d))
    return crossings


def sensitivity_analysis(ordering):
    """Compute sensitivity of Φ to each crossing."""
    Phi_full, _ = compute_Phi_selective(ordering)
    crossings = enumerate_crossings(ordering)

    sensitivities = []
    for (i, k, ctype, c, d) in crossings:
        Phi_without, _ = compute_Phi_selective(ordering, skip_crossings={(i, k)})
        delta = Phi_full - Phi_without
        sensitivities.append({
            'i': i, 'k': k, 'type': ctype,
            'ti': ordering[i], 'tk': ordering[k],
            'Phi_full': Phi_full,
            'Phi_without': Phi_without,
            'delta_Phi': delta,
            'rel_delta': abs(delta / Phi_full) if abs(Phi_full) > 1e-30 else 0.0,
        })
    return Phi_full, sensitivities


def greedy_prune(ordering, tol=0.01):
    """Greedily remove crossings with smallest |δΦ| until F changes by > tol."""
    Phi_full, _ = compute_Phi_selective(ordering)
    crossings = enumerate_crossings(ordering)
    skip = set()
    removed = []

    for iteration in range(len(crossings)):
        best_to_remove = None
        best_delta = float('inf')

        for (i, k, ctype, c, d) in crossings:
            if (i, k) in skip:
                continue
            Phi_test, _ = compute_Phi_selective(ordering, skip | {(i, k)})
            delta = abs(Phi_full - Phi_test) / max(abs(Phi_full), 1e-30)
            if delta < best_delta:
                best_delta = delta
                best_to_remove = (i, k, ctype, delta)

        if best_to_remove is None:
            break

        i, k, ctype, delta = best_to_remove
        if delta > tol:
            break

        skip.add((i, k))
        removed.append(best_to_remove)

    return skip, removed, Phi_full


# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════

ATOMS = {
    'H':    ('pe',),
    'D':    ('pne',),
    'He-3': ('ppnee',),
    'He-4': ('ppnnee', 'eeppnn', 'penpnn'),
    'Li-7': ('pnpnpnneee', 'eeepnpnpnn', 'pppenenennn'),
    'Be-9': ('ppppnnnnneee', 'eeeeppppnnnnn'),
}

print("=" * 100)
print("LP DUAL: Crossing operator selection for atomic braids")
print(f"q₀ = {q0:.10f}   HA = {HA:.10f}")
print("=" * 100)

for name, orderings in ATOMS.items():
    print(f"\n{'─'*80}")
    print(f"  {name}")
    print(f"{'─'*80}")

    for ordering in orderings:
        n = len(ordering)
        crossings = enumerate_crossings(ordering)
        n_cross = len(crossings)
        n_ne = sum(1 for i in range(n) for k in range(i+1, n)
                   if crossing_coeff(ordering[i], ordering[k])[2] == 'ne')

        print(f"\n  Ordering: {ordering}  ({n} strands, {n_cross} non-trivial crossings, {n_ne} ne=identity)")

        Phi_full, sensitivities = sensitivity_analysis(ordering)
        print(f"  Φ_full = {Phi_full:+.6f}")

        # Sort by |δΦ| to find least important crossings
        sensitivities.sort(key=lambda s: abs(s['delta_Phi']))

        print(f"\n  {'Crossing':>12s} {'Type':>4s} {'δΦ':>12s} {'|δΦ/Φ|':>10s} {'Status':>8s}")
        print(f"  {'─'*50}")
        for s in sensitivities:
            status = "KEEP" if s['rel_delta'] > 0.01 else "drop?"
            print(f"  ({s['i']:2d},{s['k']:2d}) {s['ti']}{s['tk']:>3s} {s['delta_Phi']:>+12.6f} {s['rel_delta']:>10.4f} {status:>8s}")

        # Greedy pruning
        skip, removed, _ = greedy_prune(ordering, tol=0.01)
        if removed:
            Phi_pruned, _ = compute_Phi_selective(ordering, skip)
            print(f"\n  Greedy prune (1% tolerance): removed {len(removed)}/{n_cross} crossings")
            print(f"  Φ_pruned = {Phi_pruned:+.6f}  (error = {abs(Phi_full - Phi_pruned)/max(abs(Phi_full),1e-30):.4f})")
            for (i, k, ctype, delta) in removed:
                print(f"    dropped ({i},{k}) {ctype}: |δΦ/Φ| = {delta:.6f}")
        else:
            print(f"\n  No crossings removable at 1% tolerance")

print(f"\n{'='*100}")
print("RESULT: Crossings ranked by importance. Low |δΦ/Φ| → removable.")
print("For the Rust engine: skip these crossings to reduce NF word count.")
print(f"{'='*100}")
