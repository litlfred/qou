#!/usr/bin/env python3
"""
ITERATIVE ELECTRON INSERTION into the nuclear braid.

Start with the nuclear braid H_A(q). For each electron to add:
1. Try inserting 'e' at every position in the current ordering
2. Compute Φ_q for each candidate
3. Choose the position that minimizes |Φ_q| (ground state)

This builds the atom one electron at a time, finding where
each electron "wants" to sit in the braid.

Uses Python transfer matrix (fast, scalar), not Rust NF.
Then for small atoms, also compute exact NF via Rust engine.

Usage:
    python3 folio-assistant/computations/atom_electron_insert.py
"""

import math, sys, subprocess, json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0

HA = q0 - 1.0 / q0
z = 1.0 / (q0**0.5 + q0**(-0.5))

RUST_BIN = Path(__file__).parent.parent.parent / "tools" / "hecke-engine" / "target" / "release" / "hecke-atomic"


def crossing_coeff(ti, tj):
    """Return (c, d) for strand types."""
    if ti == 'p' and tj == 'p': return 1.0, 0.0
    if ti == 'n' and tj == 'n': return 1.0, -HA
    if (ti, tj) in [('p','n'),('n','p')]: return 1.0, -HA/2
    if (ti, tj) in [('p','e'),('e','p')]: return 1.0, -HA
    if (ti, tj) in [('n','e'),('e','n')]: return 0.0, 1.0  # identity
    if ti == 'e' and tj == 'e': return 1.0, 0.0
    return 0.0, 1.0


def compute_Phi(ordering):
    """Φ_q via transfer matrix chain."""
    n = len(ordering)
    if n <= 1: return 0.0
    Phi = 0.0
    for gen in range(n - 1):
        a, b = 0.0, 1.0
        for j in range(gen + 1, n):
            c, d = crossing_coeff(ordering[gen], ordering[j])
            if c == 0.0 and d == 1.0: continue
            a, b = a * c * HA + a * d + b * c, a * c + b * d
        V = z * a + b
        if abs(V) < 1e-300: return float('inf')
        Phi += math.log(abs(V))
    return Phi


def find_best_insertion(ordering, char='e'):
    """Find best position to insert char into ordering.
    Returns (best_position, best_Phi, all_candidates)."""
    candidates = []
    for pos in range(len(ordering) + 1):
        new_ord = list(ordering)
        new_ord.insert(pos, char)
        Phi = compute_Phi(new_ord)
        candidates.append((pos, ''.join(new_ord), Phi))
    candidates.sort(key=lambda x: x[2])  # sort by Φ (most negative = lowest energy)
    return candidates[0], candidates


def run_rust_nf(ordering, timeout=30):
    """Run Rust engine for exact NF computation."""
    if not RUST_BIN.exists():
        return None
    z_count = ordering.count('p')
    n_count = ordering.count('n')
    try:
        result = subprocess.run(
            [str(RUST_BIN), str(z_count), str(n_count), ordering],
            capture_output=True, text=True, timeout=timeout
        )
        lines = result.stdout.strip().split('\n')
        for line in lines:
            if 'NF words' in line:
                # Extract word count
                parts = line.split()
                for i, p in enumerate(parts):
                    if p == 'NF':
                        return int(parts[i-1])
            if 'f_pauli' in line:
                pass
        # Try to get word count from the output
        for line in lines:
            if 'NF words' in line:
                return int(line.split()[0])
        return None
    except (subprocess.TimeoutExpired, Exception):
        return None


# ══════════════════════════════════════════════════════════════
# MAIN: Iterative construction
# ══════════════════════════════════════════════════════════════

NUCLEAR_GS = {
    'H':   ('p',     1, 0),
    'D':   ('pn',    1, 1),
    'He-3':('ppn',   2, 1),
    'He-4':('ppnn',  2, 2),
    'Li-6':('pnpnpn',3, 3),
    'Li-7':('pnpnpnn',3, 4),
    'Be-9':('ppppnnnnn', 4, 5),
}

print("=" * 100)
print("ITERATIVE ELECTRON INSERTION")
print(f"q₀ = {q0:.10f}   HA = {HA:.10f}")
print("For each atom: start with nuclear GS, insert electrons one at a time")
print("=" * 100)

for name, (nuc_ord, Z, N) in NUCLEAR_GS.items():
    print(f"\n{'━'*80}")
    print(f"  {name} (Z={Z}, N={N}): nuclear ordering = {nuc_ord}")
    print(f"{'━'*80}")

    Phi_nuc = compute_Phi(list(nuc_ord))
    print(f"  Nuclear Φ = {Phi_nuc:+.6f}  ({len(nuc_ord)} strands)")

    # Iteratively insert Z electrons
    current = list(nuc_ord)
    for e_idx in range(1, Z + 1):
        best, candidates = find_best_insertion(current, 'e')
        best_pos, best_ord, best_Phi = best

        # Show top 3 and worst
        print(f"\n  Insert electron #{e_idx}:")
        print(f"    {'Pos':>4s} {'Ordering':>30s} {'Φ':>12s} {'ΔΦ':>12s}")
        shown = set()
        for rank, (pos, ord_str, Phi) in enumerate(candidates[:3]):
            marker = " ← BEST" if rank == 0 else ""
            print(f"    {pos:>4d} {ord_str:>30s} {Phi:>+12.6f} {Phi - Phi_nuc:>+12.6f}{marker}")
            shown.add(pos)
        # Show worst
        worst = candidates[-1]
        if worst[0] not in shown:
            print(f"    {worst[0]:>4d} {worst[1]:>30s} {worst[2]:>+12.6f} {worst[2] - Phi_nuc:>+12.6f}  (worst)")

        current = list(best_ord)
        current_str = ''.join(current)

        # Run Rust NF for small atoms
        nf_words = None
        if len(current) <= 10:
            nf_words = run_rust_nf(current_str, timeout=30)

        nf_str = f", NF={nf_words} words" if nf_words is not None else ""
        print(f"    → {current_str}  (Φ={best_Phi:+.6f}{nf_str})")

    print(f"\n  FINAL ATOMIC ORDERING: {current_str}")
    print(f"  Φ_nuclear = {Phi_nuc:+.6f}")
    print(f"  Φ_atomic  = {best_Phi:+.6f}")
    print(f"  ΔΦ_electron = {best_Phi - Phi_nuc:+.6f}")
