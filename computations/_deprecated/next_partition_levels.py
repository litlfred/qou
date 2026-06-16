#!/usr/bin/env python3
"""
NEXT PARTITION LEVELS — k=4 and k=5 mass formula corrections.

Extends the 3-channel Wedderburn mass formula with the k=4 hook
partition [2,2] and k=5 Wigner partitions ([3,2], [3,1,1], [2,2,1]).

The existing 3-channel formula:
  M = M_free + α × (Φ₁ + β₂Φ₂ + β₃Φ₃)

where:
  Φ₁ = Φ_std       (standard channel traced volume)
  Φ₂ = Φ_sym + Φ_alt  (sum = pairing channel)
  Φ₃ = Φ_sym - Φ_alt  (difference = asymmetry channel)
  α  = m_e × Vol(B₃)  (binding scale, no fit)
  β₂ = -6.087415      (from Wedderburn weights)
  β₃ = 0.0499         (from Wedderburn weights)

This computation adds:
  Φ₄ = hook partition [2,2] → shell correction
  Φ₅ = Wigner partition channels → isospin/form corrections

Usage:
    python3 computations/next_partition_levels.py
"""

import math
import json
import sys
import numpy as np
from itertools import combinations
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0, HA as h0
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

z_markov = 1.0 / (q0**0.5 + qi0**0.5)


# ══════════════════════════════════════════════════════════════
# §1. PARTITIONS AND YOUNG TABLEAUX
# ══════════════════════════════════════════════════════════════

def partitions(n):
    """Generate all partitions of n as tuples in decreasing order."""
    if n == 0:
        yield ()
        return
    def gen(n, mx):
        if n == 0:
            yield ()
            return
        for k in range(min(n, mx), 0, -1):
            for r in gen(n - k, k):
                yield (k,) + r
    yield from gen(n, n)


def standard_tableaux(partition):
    """Generate all standard Young tableaux of given shape."""
    n = sum(partition)
    shape = list(partition)

    def fill(tableau, val, shape_remaining):
        if val > n:
            yield [list(row) for row in tableau]
            return
        for r in range(len(shape_remaining)):
            if shape_remaining[r] == 0:
                continue
            col = len(tableau[r])
            if r > 0 and col >= len(tableau[r - 1]):
                continue
            tableau[r].append(val)
            shape_remaining[r] -= 1
            yield from fill(tableau, val + 1, shape_remaining)
            tableau[r].pop()
            shape_remaining[r] += 1

    init_tableau = [[] for _ in range(len(shape))]
    yield from fill(init_tableau, 1, list(shape))


def content(tableau, val):
    """Content c(val) = column - row (0-indexed)."""
    for r, row in enumerate(tableau):
        for c, v in enumerate(row):
            if v == val:
                return c - r
    return None


def swap_values(tableau, a, b):
    """Return new tableau with values a and b swapped, or None if invalid."""
    new_tab = [list(row) for row in tableau]
    pos_a = pos_b = None
    for r, row in enumerate(new_tab):
        for c, v in enumerate(row):
            if v == a:
                pos_a = (r, c)
            if v == b:
                pos_b = (r, c)
    if pos_a is None or pos_b is None:
        return None
    new_tab[pos_a[0]][pos_a[1]] = b
    new_tab[pos_b[0]][pos_b[1]] = a
    for row in new_tab:
        if row != sorted(row):
            return None
    for c_idx in range(max(len(row) for row in new_tab)):
        col = [new_tab[r][c_idx] for r in range(len(new_tab))
               if c_idx < len(new_tab[r])]
        if col != sorted(col):
            return None
    return new_tab


# ══════════════════════════════════════════════════════════════
# §2. YOUNG SEMINORMAL FORM FOR H_n(q)
# ══════════════════════════════════════════════════════════════

def q_number(rho):
    """[ρ]_q = (q^ρ - q^{-ρ})/(q - q^{-1})."""
    if abs(rho) < 1e-10:
        return 0.0
    return (q0**rho - qi0**rho) / h0


def hecke_generator_matrix(tableaux, k):
    """Matrix of σ_k in Young seminormal form.

    k: generator index (swaps positions k+1 and k+2).
    Returns d×d matrix where d = len(tableaux).
    """
    d = len(tableaux)
    M = np.zeros((d, d))
    tab_index = {}
    for i, T in enumerate(tableaux):
        key = tuple(tuple(row) for row in T)
        tab_index[key] = i

    processed = set()
    for i, T in enumerate(tableaux):
        if i in processed:
            continue
        a, b = k + 1, k + 2
        rho = content(T, b) - content(T, a)
        if rho == 0:
            continue

        same_row = any(a in row and b in row for row in T)
        same_col = False
        for c_idx in range(max(len(row) for row in T)):
            col_vals = [T[r][c_idx] for r in range(len(T))
                        if c_idx < len(T[r])]
            if a in col_vals and b in col_vals:
                same_col = True

        if same_row:
            M[i, i] = q0
            processed.add(i)
        elif same_col:
            M[i, i] = -qi0
            processed.add(i)
        else:
            T_swapped = swap_values(T, a, b)
            if T_swapped is None:
                M[i, i] = q0 if rho > 0 else -qi0
                processed.add(i)
            else:
                key_swapped = tuple(tuple(row) for row in T_swapped)
                j = tab_index.get(key_swapped)
                if j is None:
                    M[i, i] = q0 if rho > 0 else -qi0
                    processed.add(i)
                else:
                    diag_i = h0 / q_number(rho)
                    diag_j = h0 - diag_i
                    bc = diag_i * diag_j + 1
                    off = math.sqrt(abs(bc))
                    if bc < 0:
                        off = -off
                    M[i, i] = diag_i
                    M[j, j] = diag_j
                    M[i, j] = off
                    M[j, i] = off
                    processed.add(i)
                    processed.add(j)
    return M


def verify_hecke_relation(M):
    """Check σ² = h·σ + I."""
    M2 = M @ M
    RHS = h0 * M + np.eye(M.shape[0])
    return np.allclose(M2, RHS, atol=1e-8)


# ══════════════════════════════════════════════════════════════
# §3. PARTITION PROPERTIES
# ══════════════════════════════════════════════════════════════

def hook_lengths(partition):
    """Compute all hook lengths of a partition."""
    hooks = []
    lam = list(partition)
    conj = []
    for j in range(lam[0] if lam else 0):
        conj.append(sum(1 for p in lam if p > j))
    for i, li in enumerate(lam):
        for j in range(li):
            arm = li - j - 1
            leg = conj[j] - i - 1
            hooks.append(arm + leg + 1)
    return hooks


def q_dim(partition):
    """Quantum dimension dim_q(λ) = [n]_q! / prod [h]_q."""
    n = sum(partition)
    num = 1.0
    for k in range(1, n + 1):
        num *= q_number(k)
    hooks = hook_lengths(partition)
    den = 1.0
    for hk in hooks:
        den *= q_number(hk)
    return num / den


def q_factorial(n):
    """[n]_q! = [1]_q [2]_q ... [n]_q."""
    result = 1.0
    for k in range(1, n + 1):
        result *= q_number(k)
    return result


def wedderburn_weight(partition):
    """w_λ = dim_q(λ)² / [n]_q!."""
    n = sum(partition)
    return q_dim(partition)**2 / q_factorial(n)


# ══════════════════════════════════════════════════════════════
# §4. CROSSING COEFFICIENTS (matching existing formula)
# ══════════════════════════════════════════════════════════════

def crossing_coeff(ti, tj):
    """Crossing coefficients for strand types p, n, e.
    Returns (c, d) such that crossing operator = c·σ + d·I.
    """
    if ti == 'p' and tj == 'p':
        return 1.0, 0.0
    if ti == 'n' and tj == 'n':
        return 1.0, -h0
    if (ti, tj) in [('p', 'n'), ('n', 'p')]:
        return 1.0, -h0 / 2
    if (ti, tj) in [('p', 'e'), ('e', 'p')]:
        return 1.0, -h0
    if (ti, tj) in [('n', 'e'), ('e', 'n')]:
        return 0.0, 1.0
    if ti == 'e' and tj == 'e':
        return 1.0, 0.0
    return 0.0, 1.0


# ══════════════════════════════════════════════════════════════
# §5. THREE EXISTING CHANNELS (reproduce baseline)
# ══════════════════════════════════════════════════════════════

def compute_3ch(ordering):
    """Compute the 3 existing channels: Φ_sym, Φ_std, Φ_alt.

    Returns (Phi_sym, Phi_std, Phi_alt).
    """
    A = len(ordering)
    sym_total = 0.0
    std_total = 0.0
    alt_total = 0.0

    for i in range(A - 1):
        sym_prod = 1.0
        alt_prod = 1.0
        a, b = 0.0, 1.0
        for j in range(i + 1, A):
            c, d = crossing_coeff(ordering[i], ordering[j])
            if c == 0 and d == 1:
                continue
            sym_prod *= (c * q0 + d)
            alt_prod *= (-c * qi0 + d)
            na = a * c * h0 + a * d + b * c
            nb = a * c + b * d
            a, b = na, nb
        V = z_markov * a + b
        if abs(V) > 1e-300:
            std_total += math.log(abs(V))
        if abs(sym_prod) > 1e-300:
            sym_total += math.log(abs(sym_prod))
        if abs(alt_prod) > 1e-300:
            alt_total += math.log(abs(alt_prod))

    return sym_total, std_total, alt_total


# ══════════════════════════════════════════════════════════════
# §6. NEW PARTITION CHANNELS (hook + Wigner)
# ══════════════════════════════════════════════════════════════

def compute_partition_channel(ordering, target_partition):
    """Compute Φ_λ for a partition λ in H_n(q) via YSN.

    If target_partition has fewer boxes than n=len(ordering),
    stabilize by adding boxes to the first row.

    Returns Φ_λ = Σ_gen ln|tr(M_gen^λ)|.
    """
    n = len(ordering)
    k = sum(target_partition)

    if n < 2:
        return 0.0

    # Stabilize if needed
    if k < n:
        tail = list(target_partition[1:])
        first_row = n - sum(tail)
        if first_row <= 0 or first_row < target_partition[0]:
            return 0.0
        partition = tuple([first_row] + tail)
        # Verify valid partition (decreasing rows)
        for i in range(len(partition) - 1):
            if partition[i] < partition[i + 1]:
                return 0.0
        if len(partition) > n:
            return 0.0
    elif k == n:
        partition = target_partition
    else:
        return 0.0  # partition too large

    tabs = list(standard_tableaux(partition))
    d = len(tabs)
    if d <= 1:
        return 0.0  # 1D reps (sym/alt) are already captured by 3ch

    gen_matrices = {}
    for gk in range(n - 1):
        M = hecke_generator_matrix(tabs, gk)
        if not verify_hecke_relation(M):
            return 0.0
        gen_matrices[gk] = M

    Phi = 0.0
    for gen in range(n - 1):
        M_chain = np.eye(d)
        for j in range(gen + 1, n):
            c, dc = crossing_coeff(ordering[gen], ordering[j])
            if c == 0.0 and dc == 1.0:
                continue
            C = c * gen_matrices[gen] + dc * np.eye(d)
            M_chain = M_chain @ C

        tr_val = np.trace(M_chain).real
        if abs(tr_val) < 1e-300:
            return float('inf')
        Phi += math.log(abs(tr_val))

    return Phi


# ══════════════════════════════════════════════════════════════
# §7. GROUND-STATE ORDERING
# ══════════════════════════════════════════════════════════════

# Cache from the existing witness
WITNESS_ORDERINGS = {}


def load_witness_orderings():
    """Load ground-state orderings from existing witness."""
    global WITNESS_ORDERINGS
    witness_path = Path(__file__).parent / \
        'atom-mass-complete-wedderburn.witness.json'
    if witness_path.exists():
        with open(witness_path) as f:
            data = json.load(f)
        for r in data['results']:
            key = (r['Z'], r['N'])
            WITNESS_ORDERINGS[key] = list(r['ordering'])


def get_ordering(Z, N):
    """Get ground-state ordering (from witness cache or computed)."""
    if not WITNESS_ORDERINGS:
        load_witness_orderings()

    key = (Z, N)
    if key in WITNESS_ORDERINGS:
        return WITNESS_ORDERINGS[key]

    # Compute if not in witness
    A = Z + N
    # Simple alternating: e p n p n ... with electrons interleaved
    ordering = []
    pi, ni, ei = 0, 0, 0
    for k in range(A + Z):
        if ei < Z and k % 3 == 0:
            ordering.append('e')
            ei += 1
        elif pi < Z and (ni >= N or k % 2 == 0):
            ordering.append('p')
            pi += 1
        elif ni < N:
            ordering.append('n')
            ni += 1
        elif pi < Z:
            ordering.append('p')
            pi += 1
        elif ei < Z:
            ordering.append('e')
            ei += 1
    return ordering


# ══════════════════════════════════════════════════════════════
# §8. MASS FORMULA
# ══════════════════════════════════════════════════════════════

# Existing calibration (from witness, no fitting)
VOL_B3 = 7.327724753417752
m_p = 938.230457    # derived nucleon masses
m_n = 939.532005
ALPHA = M_E_MEV * VOL_B3   # ≈ 3.74446
BETA2 = -6.087415
BETA3 = 0.0499

# Hook coefficient: -½ × w_{[2,2]}(4)
w_hook_22 = wedderburn_weight((2, 2))
BETA4 = -0.5 * w_hook_22

# Wigner coefficients: from k=5 Wedderburn weights
w_32 = wedderburn_weight((3, 2))
w_311 = wedderburn_weight((3, 1, 1))
w_221 = wedderburn_weight((2, 2, 1))
# Total Wigner weight (combined k=5 correction)
BETA5 = -0.5 * (w_32 + w_311 + w_221)


# Experimental masses (AME2020)
AME2020 = {
    (1, 0): ('1H', 938.78313),
    (2, 2): ('4He', 3728.4013),
    (3, 4): ('7Li', 6535.367),
    (4, 5): ('9Be', 8394.7937),
    (5, 6): ('11B', 10255.103),
    (6, 6): ('12C', 11177.929),
    (7, 7): ('14N', 13043.780),
    (8, 8): ('16O', 14899.169),
    (9, 10): ('19F', 17696.929),
    (10, 10): ('20Ne', 18622.838),
    (11, 12): ('23Na', 21414.835),
    (12, 12): ('24Mg', 22341.921),
    (13, 14): ('27Al', 25133.142),
    (14, 14): ('28Si', 26060.339),
    (15, 16): ('31P', 28851.879),
    (16, 16): ('32S', 29781.801),
    (17, 18): ('35Cl', 32573.337),
    (18, 22): ('40Ar', 37224.706),
    (19, 20): ('39K', 36294.456),
    (20, 20): ('40Ca', 37213.757),
}


def mass_prediction(Z, N, compute_k5=True):
    """Predict atomic mass at each partition level.

    Returns dict with Phi channels and predictions at each level.
    """
    ordering = get_ordering(Z, N)

    # 3-channel baseline (reproduces existing witness)
    Phi_sym, Phi_std, Phi_alt = compute_3ch(ordering)
    Phi1 = Phi_std
    Phi2 = Phi_sym + Phi_alt
    Phi3 = Phi_sym - Phi_alt

    M_free = Z * m_p + N * m_n + Z * M_E_MEV

    # Baseline 3ch prediction
    bind_3ch = ALPHA * (Phi1 + BETA2 * Phi2 + BETA3 * Phi3)
    M_3ch = M_free + bind_3ch

    # k=4: Hook partition [2,2]
    n = len(ordering)
    Phi_hook = 0.0
    if n >= 4:
        Phi_hook = compute_partition_channel(ordering, (2, 2))

    bind_4ch = bind_3ch + ALPHA * BETA4 * Phi_hook
    M_4ch = M_free + bind_4ch

    # k=5: Wigner partitions
    Phi_32 = 0.0
    Phi_311 = 0.0
    Phi_221 = 0.0
    if compute_k5 and n >= 5:
        Phi_32 = compute_partition_channel(ordering, (3, 2))
        Phi_311 = compute_partition_channel(ordering, (3, 1, 1))
        Phi_221 = compute_partition_channel(ordering, (2, 2, 1))

    # Combined Wigner channel
    Phi_wigner = Phi_32 + Phi_311 + Phi_221
    bind_5ch = bind_4ch + ALPHA * BETA5 * Phi_wigner
    M_5ch = M_free + bind_5ch

    return {
        'ordering': ''.join(ordering),
        'Phi1': Phi1, 'Phi2': Phi2, 'Phi3': Phi3,
        'Phi_hook': Phi_hook,
        'Phi_32': Phi_32, 'Phi_311': Phi_311, 'Phi_221': Phi_221,
        'Phi_wigner': Phi_wigner,
        'M_free': M_free,
        'M_3ch': M_3ch, 'M_4ch': M_4ch, 'M_5ch': M_5ch,
    }


# ══════════════════════════════════════════════════════════════
# §9. MAIN
# ══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import time

    print("=" * 90)
    print("NEXT PARTITION LEVELS: k=4 Hook + k=5 Wigner Corrections")
    print("=" * 90)

    # Coefficients
    print(f"\nCALIBRATION (no fitted parameters)")
    print(f"  α = m_e × Vol(B₃) = {M_E_MEV:.6f} × {VOL_B3:.6f} = {ALPHA:.6f}")
    print(f"  β₂ = {BETA2:.6f}")
    print(f"  β₃ = {BETA3:.6f}")
    print(f"  β₄ (hook [2,2])  = -½ × w_{{[2,2]}}(4) = "
          f"-½ × {w_hook_22:.6f} = {BETA4:.6f}")
    print(f"  β₅ (Wigner k=5)  = -½ × (w_32+w_311+w_221) = "
          f"-½ × ({w_32:.6f}+{w_311:.6f}+{w_221:.6f}) = {BETA5:.6f}")

    # Partition tower properties
    print(f"\nPARTITION TOWER")
    print(f"  k=3: [3]     dim_q=1.000  w={wedderburn_weight((3,)):.6f}  (sym)")
    print(f"  k=3: [2,1]   dim_q={q_dim((2,1)):.3f}  "
          f"w={wedderburn_weight((2,1)):.6f}  (std)")
    print(f"  k=3: [1,1,1] dim_q=1.000  w={wedderburn_weight((1,1,1)):.6f}  (alt)")
    print(f"  k=4: [2,2]   dim_q={q_dim((2,2)):.3f}  "
          f"w={w_hook_22:.6f}  (hook)")
    print(f"  k=5: [3,2]   dim_q={q_dim((3,2)):.3f}  w={w_32:.6f}")
    print(f"  k=5: [3,1,1] dim_q={q_dim((3,1,1)):.3f}  w={w_311:.6f}")
    print(f"  k=5: [2,2,1] dim_q={q_dim((2,2,1)):.3f}  w={w_221:.6f}")

    # Wedderburn trace identity verification
    print(f"\n  Wedderburn identity Σ dim_q(λ)² = [n]_q!:")
    for n in range(3, 7):
        total = sum(q_dim(lam)**2 for lam in partitions(n))
        qfact = q_factorial(n)
        print(f"    n={n}: {total:.4f} vs {qfact:.4f} "
              f"(ratio {total/qfact:.8f})")

    # Mass predictions
    print(f"\n{'='*90}")
    print(f"MASS PREDICTIONS")
    print(f"{'='*90}")

    hdr = (f"{'Atom':>5s} {'Z':>2s} {'N':>2s} {'A':>2s}  "
           f"{'M_obs':>10s}  "
           f"{'3ch δ%':>8s} {'4ch δ%':>8s} {'5ch δ%':>8s}  "
           f"{'Φ_hook':>8s} {'Φ_wig':>8s}")
    print(hdr)
    print("-" * len(hdr))

    results_list = []
    t0 = time.time()

    for (Z, N), (name, M_obs) in sorted(AME2020.items()):
        # Limit k=5 to atoms with ≤ 20 strands for speed
        A = Z + N
        n_strands = A + Z  # includes electrons
        compute_k5 = n_strands <= 25

        result = mass_prediction(Z, N, compute_k5=compute_k5)

        d3 = (result['M_3ch'] - M_obs) / M_obs * 100
        d4 = (result['M_4ch'] - M_obs) / M_obs * 100
        d5 = (result['M_5ch'] - M_obs) / M_obs * 100

        print(f"{name:>5s} {Z:>2d} {N:>2d} {A:>2d}  "
              f"{M_obs:>10.1f}  "
              f"{d3:>+8.4f} {d4:>+8.4f} {d5:>+8.4f}  "
              f"{result['Phi_hook']:>+8.3f} "
              f"{result['Phi_wigner']:>+8.3f}"
              f"{'*' if not compute_k5 else ''}")

        results_list.append({
            'atom': name, 'Z': Z, 'N': N, 'A': A,
            'M_obs': M_obs,
            'M_pred_3ch': round(result['M_3ch'], 3),
            'M_pred_4ch': round(result['M_4ch'], 3),
            'M_pred_5ch': round(result['M_5ch'], 3),
            'delta_pct_3ch': round(d3, 6),
            'delta_pct_4ch': round(d4, 6),
            'delta_pct_5ch': round(d5, 6),
            'Phi1': round(result['Phi1'], 6),
            'Phi2': round(result['Phi2'], 6),
            'Phi3': round(result['Phi3'], 6),
            'Phi_hook': round(result['Phi_hook'], 6),
            'Phi_32': round(result['Phi_32'], 6),
            'Phi_311': round(result['Phi_311'], 6),
            'Phi_221': round(result['Phi_221'], 6),
            'ordering': result['ordering'],
        })

    elapsed = time.time() - t0

    # Summary
    pcts_3 = [abs(r['delta_pct_3ch']) for r in results_list]
    pcts_4 = [abs(r['delta_pct_4ch']) for r in results_list]
    pcts_5 = [abs(r['delta_pct_5ch']) for r in results_list]

    print("-" * len(hdr))
    print(f"\nSUMMARY ({len(results_list)} atoms, {elapsed:.1f}s)")
    print(f"  3-channel (baseline):    "
          f"mean |δ| = {sum(pcts_3)/len(pcts_3):.4f}%  "
          f"max |δ| = {max(pcts_3):.4f}%")
    print(f"  4-channel (+hook [2,2]): "
          f"mean |δ| = {sum(pcts_4)/len(pcts_4):.4f}%  "
          f"max |δ| = {max(pcts_4):.4f}%")
    print(f"  5-channel (+Wigner k=5): "
          f"mean |δ| = {sum(pcts_5)/len(pcts_5):.4f}%  "
          f"max |δ| = {max(pcts_5):.4f}%")

    # Per-atom improvements
    print(f"\nPER-ATOM IMPROVEMENTS:")
    for r in results_list:
        d3 = abs(r['delta_pct_3ch'])
        d4 = abs(r['delta_pct_4ch'])
        d5 = abs(r['delta_pct_5ch'])
        imp4 = (d3 - d4) / d3 * 100 if d3 > 1e-6 else 0
        imp5 = (d3 - d5) / d3 * 100 if d3 > 1e-6 else 0
        marker = '✓' if d4 < d3 else '✗'
        print(f"  {r['atom']:>5s}: 3ch={d3:.4f}%  "
              f"4ch={d4:.4f}%  5ch={d5:.4f}%  "
              f"(4ch {imp4:+.1f}%) {marker}")

    # Write witness
    witness = {
        'name': 'next-partition-levels',
        'engine': 'Python 3ch + YSN partition tower',
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'parameters': {
            'q0': q0,
            'm_e': M_E_MEV,
            'm_p': m_p,
            'm_n': m_n,
            'Vol_B3': VOL_B3,
            'alpha': ALPHA,
            'beta2': BETA2,
            'beta3': BETA3,
            'beta4_hook': BETA4,
            'beta5_wigner': BETA5,
            'w_22': w_hook_22,
            'w_32': w_32,
            'w_311': w_311,
            'w_221': w_221,
            'fitted': 0,
        },
        'partition_tower': {
            'k3_sym': '(3,)',
            'k3_std': '(2, 1)',
            'k3_alt': '(1, 1, 1)',
            'k4_hook': '(2, 2)',
            'k5_wigner_a': '(3, 2)',
            'k5_wigner_b': '(3, 1, 1)',
            'k5_wigner_c': '(2, 2, 1)',
        },
        'results': results_list,
        'summary': {
            'n_atoms': len(results_list),
            'mean_pct_3ch': round(sum(pcts_3)/len(pcts_3), 4),
            'mean_pct_4ch': round(sum(pcts_4)/len(pcts_4), 4),
            'mean_pct_5ch': round(sum(pcts_5)/len(pcts_5), 4),
            'max_pct_3ch': round(max(pcts_3), 4),
            'max_pct_4ch': round(max(pcts_4), 4),
            'max_pct_5ch': round(max(pcts_5), 4),
        },
    }

    witness_path = Path(__file__).parent / \
        'next-partition-levels.witness.json'
    with open(witness_path, 'w') as f:
        json.dump(witness, f, indent=2)
    print(f"\nWitness → {witness_path}")
