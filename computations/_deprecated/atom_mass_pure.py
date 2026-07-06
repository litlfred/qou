#!/usr/bin/env python3
"""
PURE DERIVED MASS — shell-aware GS ordering, no fitting.

Improvements over atom_mass_exact.py:
1. Shell-aware GS search: orderings respect magic number structure
2. More restarts with shell-structured starting points
3. Exact enumeration threshold raised to C(A,Z) ≤ 100,000
4. NO pairing, NO surface, NO Coulomb — only Φ_q

The shell structure IS derived (magic numbers from torus knot
hierarchy on Bring's surface), so encoding it in the ordering
search is purely mathematical — not a parameter.

Usage:
    python3 computations/atom_mass_pure.py
"""

import math, sys, time
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, HBAR_Q_SQ
from witness_base import WitnessBuilder

VOL_NEUTRON = 13.9484177283
HA = q0 - 1.0/q0
z = 1.0 / (q0**0.5 + q0**(-0.5))
m_n_hecke = VOL_NEUTRON / HBAR_Q_SQ

# Magic numbers (DERIVED from torus knot hierarchy)
SHELL_CAPACITIES = [2, 6, 12, 8, 22, 32, 44]  # cumulative: 2,8,20,28,50,82,126


# ══════════════════════════════════════════════════════════════
# §1  FAST Φ_q COMPUTATION
# ══════════════════════════════════════════════════════════════

def compute_Phi(ordering):
    """Φ_q = Σ ln|V̂_i|. O(A²)."""
    A = len(ordering)
    if A <= 1:
        return 0.0
    Phi = 0.0
    for gen in range(A - 1):
        a, b = 0.0, 1.0
        for j in range(gen + 1, A):
            ti, tj = ordering[gen], ordering[j]
            if ti == 1 and tj == 1:
                d = 0.0
            elif ti == 0 and tj == 0:
                d = -HA
            else:
                d = -HA / 2
            a, b = a * HA + a * d + b, a + b * d
        V = z * a + b
        if abs(V) < 1e-300:
            return float('inf')
        Phi += math.log(abs(V))
    return Phi


# ══════════════════════════════════════════════════════════════
# §2  SHELL-AWARE STARTING ORDERINGS
# ══════════════════════════════════════════════════════════════

def shell_assignment(A):
    """Assign each position to a shell. Returns list of shell indices."""
    shells = []
    pos = 0
    for shell_idx, cap in enumerate(SHELL_CAPACITIES):
        for k in range(cap):
            if pos >= A:
                return shells
            shells.append(shell_idx)
            pos += 1
    # Beyond known shells
    while pos < A:
        shells.append(len(SHELL_CAPACITIES))
        pos += 1
    return shells


def shell_interleaved(Z, N):
    """Build ordering that interleaves p/n WITHIN each shell.

    Each shell gets its share of protons and neutrons,
    distributed as evenly as possible within the shell.
    This respects the shell structure derived from magic numbers.
    """
    A = Z + N
    shells = shell_assignment(A)
    max_shell = max(shells) if shells else 0

    # Count positions per shell
    shell_positions = {}
    for i, s in enumerate(shells):
        shell_positions.setdefault(s, []).append(i)

    # Distribute Z protons across shells proportionally
    ordering = [0] * A
    protons_remaining = Z

    for s in range(max_shell + 1):
        positions = shell_positions.get(s, [])
        n_pos = len(positions)
        # Proportional share of protons for this shell
        if A > 0:
            share = round(Z * n_pos / A)
        else:
            share = 0
        share = min(share, protons_remaining, n_pos)

        # Interleave within shell: put protons at even positions
        placed = 0
        for k, pos in enumerate(positions):
            if placed < share and k % 2 == 0:
                ordering[pos] = 1
                placed += 1
        # Fill remaining protons at odd positions
        for k, pos in enumerate(positions):
            if placed >= share:
                break
            if ordering[pos] == 0:
                ordering[pos] = 1
                placed += 1
        protons_remaining -= placed

    # Fix up: ensure exactly Z protons
    current_Z = sum(ordering)
    if current_Z < Z:
        for i in range(A):
            if ordering[i] == 0 and current_Z < Z:
                ordering[i] = 1
                current_Z += 1
    elif current_Z > Z:
        for i in range(A - 1, -1, -1):
            if ordering[i] == 1 and current_Z > Z:
                ordering[i] = 0
                current_Z -= 1

    return ordering


def shell_blocked(Z, N):
    """Protons fill inner shells first, neutrons fill outer."""
    A = Z + N
    shells = shell_assignment(A)
    ordering = [0] * A
    # Fill protons from inside out
    for i in range(min(Z, A)):
        ordering[i] = 1
    return ordering


def alternating_block(Z, N, block_size=2):
    """Blocks of protons and neutrons of given size."""
    A = Z + N
    ordering = []
    pz, nn = 0, 0
    block_type = 1  # start with protons
    while len(ordering) < A:
        for _ in range(block_size):
            if len(ordering) >= A:
                break
            if block_type == 1 and pz < Z:
                ordering.append(1)
                pz += 1
            elif block_type == 0 and nn < N:
                ordering.append(0)
                nn += 1
            elif pz < Z:
                ordering.append(1)
                pz += 1
            else:
                ordering.append(0)
                nn += 1
        block_type = 1 - block_type
    return ordering[:A]


# ══════════════════════════════════════════════════════════════
# §3  EXHAUSTIVE + STEEPEST DESCENT GS SEARCH
# ══════════════════════════════════════════════════════════════

def find_gs(Z, N):
    """Find ground-state ordering.

    Exact for C(A,Z) ≤ 100,000.
    Otherwise: steepest descent to convergence from many starting points.
    """
    A = Z + N
    if A <= 1:
        return [1] if Z > 0 else [0], "trivial"

    total = math.comb(A, Z)

    # Exact exhaustive search
    if total <= 100000:
        best_Phi = float('inf')
        best_ordering = None
        for positions in combinations(range(A), Z):
            o = [0] * A
            for p in positions:
                o[p] = 1
            Phi = compute_Phi(o)
            if Phi < best_Phi:
                best_Phi = Phi
                best_ordering = list(o)
        return best_ordering, "exact"

    # Steepest descent from multiple shell-aware starting points
    def steepest_descent(ordering):
        """Run steepest descent to convergence. Returns (ordering, Phi)."""
        o = list(ordering)
        Phi = compute_Phi(o)
        improved = True
        while improved:
            improved = False
            best_swap = None
            best_delta = 0.0
            p_pos = [i for i in range(A) if o[i] == 1]
            n_pos = [i for i in range(A) if o[i] == 0]
            for pi in p_pos:
                for ni in n_pos:
                    o[pi], o[ni] = 0, 1
                    new_Phi = compute_Phi(o)
                    delta = new_Phi - Phi
                    o[pi], o[ni] = 1, 0
                    if delta < best_delta - 1e-12:
                        best_delta = delta
                        best_swap = (pi, ni)
            if best_swap:
                pi, ni = best_swap
                o[pi], o[ni] = 0, 1
                Phi += best_delta
                improved = True
        return o, Phi

    # Generate many starting points
    starts = [
        shell_interleaved(Z, N),
        list(reversed(shell_interleaved(Z, N))),
        shell_blocked(Z, N),
        list(reversed(shell_blocked(Z, N))),
        alternating_block(Z, N, 1),  # pnpnpn...
        alternating_block(Z, N, 2),  # ppnnppnn...
        alternating_block(Z, N, 3),  # pppnnnpppnnn...
        [1]*Z + [0]*N,
        [0]*N + [1]*Z,
    ]

    # Add shifted variants
    base = shell_interleaved(Z, N)
    for shift in [1, 2, 3, A//4, A//3, A//2]:
        shifted = base[shift:] + base[:shift]
        if sum(shifted) == Z:
            starts.append(shifted)

    best_global_Phi = float('inf')
    best_global_ord = None

    for start in starts:
        if sum(start) != Z or len(start) != A:
            continue
        o, Phi = steepest_descent(start)
        if Phi < best_global_Phi:
            best_global_Phi = Phi
            best_global_ord = list(o)

    return best_global_ord, "steepest_converged"


# ══════════════════════════════════════════════════════════════
# §4  MAIN
# ══════════════════════════════════════════════════════════════

ELEMENTS = [
    ("H",  "¹H",  1, 0,  938.783),  ("He", "⁴He", 2, 2,  3728.401),
    ("Li", "⁷Li", 3, 4,  6535.367), ("Be", "⁹Be", 4, 5,  8394.794),
    ("B",  "¹¹B", 5, 6,  10255.103),("C",  "¹²C", 6, 6,  11177.930),
    ("N",  "¹⁴N", 7, 7,  13043.781),("O",  "¹⁶O", 8, 8,  14899.169),
    ("F",  "¹⁹F", 9, 10, 17696.901),("Ne", "²⁰Ne",10,10, 18622.835),
    ("Na", "²³Na",11,12, 21414.830),("Mg", "²⁴Mg",12,12, 22341.908),
    ("Al", "²⁷Al",13,14, 25133.143),("Si", "²⁸Si",14,14, 26060.344),
    ("P",  "³¹P", 15,16, 28851.873),("S",  "³²S", 16,16, 29781.800),
    ("Cl", "³⁵Cl",17,18, 32573.283),("Ar", "⁴⁰Ar",18,22, 37224.719),
    ("K",  "³⁹K", 19,20, 36294.464),("Ca", "⁴⁰Ca",20,20, 37213.777),
]


def main():
    print("=" * 110)
    print("PURE DERIVED MASS — shell-aware GS, no fitting")
    print(f"q₀ = {q0:.10f}  HA = {HA:.10f}  z = {z:.10f}")
    print("M(Z,N) = E₀ × [Z×𝔪_p + N×𝔪_n + α×Φ_q(Z,N)]")
    print("NO pairing. NO surface. NO Coulomb. ONLY Φ_q.")
    print("=" * 110)
    print()

    # Phase 1: GS search
    atoms = []
    for name, label, Z, N, M_obs in ELEMENTS:
        A = Z + N
        t0 = time.time()
        ordering, method = find_gs(Z, N)
        gs_time = time.time() - t0
        phi = compute_Phi(ordering)
        atoms.append({
            'label': label, 'Z': Z, 'N': N, 'A': A, 'M_obs': M_obs,
            'phi': phi, 'method': method, 'gs_time': gs_time,
            'ordering': ordering,
        })
        ord_str = ''.join('●' if x else '○' for x in ordering)
        print(f"  {label:>5} A={A:2d}: Φ={phi:+.6f}  [{method}, {gs_time:.1f}s]  {ord_str[:40]}{'...' if A>40 else ''}")

    # Phase 2: Calibrate from H, He, C
    M_H = atoms[0]['M_obs']
    M_He = atoms[1]['M_obs']
    M_C = atoms[5]['M_obs']
    phi_He = atoms[1]['phi']
    phi_C = atoms[5]['phi']
    lhs1 = M_He - 2 * M_H
    lhs2 = M_C - 6 * M_H
    denom = phi_He * lhs2 - phi_C * lhs1
    alpha = m_n_hecke * (6*lhs1 - 2*lhs2) / denom
    E0 = lhs1 / (2*m_n_hecke + alpha*phi_He)
    mp = M_H / E0

    print()
    print(f"  Calibrated: E₀={E0:.6f}  𝔪_p={mp:.4f}  α={alpha:.6f}")
    print()

    # Phase 3: Predict
    print("=" * 110)
    print(f"{'Atom':>5} | {'A':>3} | {'Φ_q':>10} | {'M_pred':>12} | {'M_obs':>12} | {'Δ MeV':>8} | {'Δ%':>8} | {'':>4}")
    print("─" * 110)

    pred_errors = []
    for a in atoms:
        m_tot = a['Z'] * mp + a['N'] * m_n_hecke + alpha * a['phi']
        M_pred = E0 * m_tot
        delta = M_pred - a['M_obs']
        pct = delta / a['M_obs'] * 100
        cal = "CAL" if a['label'] in ['¹H', '⁴He', '¹²C'] else "PRED"
        print(f"{a['label']:>5} | {a['A']:3d} | {a['phi']:+10.4f} | {M_pred:12.3f} | {a['M_obs']:12.3f} | {delta:+8.3f} | {pct:+7.3f}% | {cal}")
        if cal == "PRED":
            pred_errors.append(abs(pct))

    print("─" * 110)
    mean_e = sum(pred_errors)/len(pred_errors)
    max_e = max(pred_errors)
    print(f"  {len(pred_errors)} predictions: mean |Δ%| = {mean_e:.4f}%, max = {max_e:.4f}%")

    # Witness
    w = WitnessBuilder("atom-mass-pure", engine="python")
    w.set_description(
        "Pure derived mass: shell-aware GS, no fitting. "
        "Only Phi_q from Hecke algebra. 3 calibration inputs."
    )
    w.add_parameter("q0", str(q0))
    w.add_parameter("E0", str(E0))
    w.add_parameter("mp_hecke", str(mp))
    w.add_parameter("alpha", str(alpha))
    w.add_data("predictions", [
        {'atom': a['label'], 'Z': a['Z'], 'N': a['N'], 'phi': a['phi'],
         'method': a['method']} for a in atoms
    ])
    w.save()


if __name__ == "__main__":
    main()
