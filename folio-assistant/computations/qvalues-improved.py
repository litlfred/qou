"""
Improved Q-value predictions: systematic exploration of correction strategies.

The base formula (MAE 4.9%) has two known issues:
1. Odd-odd pairing deficit (⁶⁰Co, ²¹⁰Bi)
2. Spectator overcounting for heavy nuclei (A > 28)

This script tests multiple approaches to find the right formula.
"""

import math
import sys
sys.path.insert(0, '.')
from q_parameter import Q, Q_INV, Q_ERR, HA, LN_Q
from experimental_constants import M_E_MEV

KAPPA = M_E_MEV / 3.0   # bare kappa (without ln(q))
KAPPA_Q = LN_Q * KAPPA   # kappa_q = ln(q) × m_e/3
Z_MARKOV = 1.0 / (math.sqrt(Q) + 1.0/math.sqrt(Q))
S_SKEIN = math.sqrt(Q) - 1.0/math.sqrt(Q)
F_DEG2 = 0.5949
F_PAULI = 0.6382
MAGIC = [2, 8, 20, 28, 50, 82, 126]

def shell_degree(n):
    for i, m in enumerate(MAGIC):
        if n <= m: return 2 if i+1 >= 5 else 1
    return 2

def crossing_coeffs(ti, tj):
    pair = ti + tj
    if pair == 'pp': return (1.0, 0.0)
    elif pair == 'nn': return (Q**2, -Q * S_SKEIN)
    else: return ((1.0 + Q**2)/2.0, -Q * S_SKEIN / 2.0)

def generator_volumes(z, n):
    a = z + n
    types = ['p']*z + ['n']*n
    vols = []
    for i in range(a-1):
        m = [[1.0, 0.0], [0.0, 1.0]]
        for j in range(i+1, a):
            c, d = crossing_coeffs(types[i], types[j])
            t = [[c*HA+d, c], [c, d]]
            m = [[m[0][0]*t[0][0]+m[0][1]*t[1][0], m[0][0]*t[0][1]+m[0][1]*t[1][1]],
                 [m[1][0]*t[0][0]+m[1][1]*t[1][0], m[1][0]*t[0][1]+m[1][1]*t[1][1]]]
        vols.append(Z_MARKOV * m[0][0] + m[1][0])
    return vols

def parity(z, n):
    if z%2==0 and n%2==0: return "ee"
    elif z%2==1 and n%2==1: return "oo"
    else: return "oA"


BENCHMARKS = [
    (1,  2,  "³H",       0.01861),
    (6,  8,  "¹⁴C",      0.15648),
    (27, 33, "⁶⁰Co",     0.31817),
    (38, 52, "⁹⁰Sr",     0.54590),
    (55, 82, "¹³⁷Cs",    0.51400),
    (83, 127,"²¹⁰Bi",    1.16270),
]


def base_qvalue(z, n):
    """Current formula (MAE 4.9%)."""
    a = z + n
    types_p = ['p']*z + ['n']*n
    types_d = ['p']*(z+1) + ['n']*(n-1)
    vp = generator_volumes(z, n)
    vd = generator_volumes(z+1, n-1)

    lu, lr, luc = 0.0, 0.0, 0.0
    for i in range(a-1):
        if abs(vp[i]) < 1e-30 or abs(vd[i]) < 1e-30: continue
        lratio = (math.log(abs(vd[i])) - math.log(abs(vp[i]))) / LN_Q
        changed = [j for j in range(i+1, a)
                   if types_p[i]+types_p[j] != types_d[i]+types_d[j]]
        if not changed:
            luc += lratio
        else:
            nu = sum(1 for j in changed if types_p[i]=='n' and types_p[j]=='n')
            nr = sum(1 for j in changed if types_d[i]=='p' and types_d[j]=='p')
            t = nu + nr
            if nr==0: lu += lratio
            elif nu==0: lr += lratio
            else:
                lu += lratio*nu/t; lr += lratio*nr/t

    q_qwt = abs(Q*lu + Q_INV*lr + luc) * KAPPA_Q
    deg = shell_degree(n)
    f = F_DEG2 if deg >= 2 else 1.0
    if n in MAGIC and deg >= 2: f *= F_PAULI
    return q_qwt * f


def approach_skein_ratio(z, n):
    """Q = |ln(P_dau/P_par)| × κ  (pure Skein polynomial ratio).

    The Skein polynomial P(q) = ∏_i V̂_i(q). The Q-value is the
    energy difference, which should be proportional to the log of
    the amplitude ratio.
    """
    vp = generator_volumes(z, n)
    vd = generator_volumes(z+1, n-1)

    # ln(P_dau/P_par) = Σ_i ln(V̂_i^dau / V̂_i^par)
    log_ratio = 0.0
    for i in range(z+n-1):
        if abs(vp[i]) < 1e-30 or abs(vd[i]) < 1e-30: continue
        log_ratio += math.log(abs(vd[i])) - math.log(abs(vp[i]))

    # Q = |ln ratio| × κ  (not κ_q — the ln(q) is already in the log ratio)
    q_pred = abs(log_ratio) * KAPPA

    deg = shell_degree(n)
    f = F_DEG2 if deg >= 2 else 1.0
    if n in MAGIC and deg >= 2: f *= F_PAULI
    return q_pred * f


def approach_converting_chain(z, n):
    """Q from the converting generator's chain only.

    In β⁻ decay, the converting nucleon is at position Z.
    Generator σ_{Z-1} connects nucleon Z-1 to Z (pn→pp).
    Generator σ_Z connects nucleon Z to Z+1 (nn→pn).

    Use only these two generators' volume ratios.
    """
    a = z + n
    vp = generator_volumes(z, n)
    vd = generator_volumes(z+1, n-1)

    log_sum = 0.0
    # Converting generators: Z-1 and Z (if they exist)
    for i in [z-1, z]:
        if i < 0 or i >= a-1: continue
        if abs(vp[i]) < 1e-30 or abs(vd[i]) < 1e-30: continue
        log_sum += math.log(abs(vd[i])) - math.log(abs(vp[i]))

    q_pred = abs(log_sum) * KAPPA
    deg = shell_degree(n)
    f = F_DEG2 if deg >= 2 else 1.0
    if n in MAGIC and deg >= 2: f *= F_PAULI
    return q_pred * f


def approach_per_nucleon(z, n):
    """Q = |ln(P_dau/P_par)| / A × κ_A.

    Divide by A to get per-nucleon energy, then scale.
    This counters the overcounting by normalizing by nucleus size.
    """
    vp = generator_volumes(z, n)
    vd = generator_volumes(z+1, n-1)
    a = z + n

    log_ratio = 0.0
    for i in range(a-1):
        if abs(vp[i]) < 1e-30 or abs(vd[i]) < 1e-30: continue
        log_ratio += math.log(abs(vd[i])) - math.log(abs(vp[i]))

    # Per-nucleon normalization: heavy nuclei have more generators
    q_pred = abs(log_ratio) / (a - 1) * KAPPA * (a - 1)  # this cancels...

    # Better: normalize by the number of CHANGED generators
    n_changed = 0
    types_p = ['p']*z + ['n']*n
    types_d = ['p']*(z+1) + ['n']*(n-1)
    for i in range(a-1):
        for j in range(i+1, a):
            if types_p[i]+types_p[j] != types_d[i]+types_d[j]:
                n_changed += 1
                break

    if n_changed == 0: n_changed = 1
    q_pred = abs(log_ratio) / n_changed * KAPPA

    deg = shell_degree(n)
    f = F_DEG2 if deg >= 2 else 1.0
    if n in MAGIC and deg >= 2: f *= F_PAULI
    return q_pred * f


def approach_log_skein_qweighted(z, n):
    """Q from q-weighted log of Skein polynomial ratio.

    Like the base formula but using ln (not log_q) and κ (not κ_q).
    Since log_q × κ_q = ln × κ, this should be identical.
    Sanity check.
    """
    a = z + n
    types_p = ['p']*z + ['n']*n
    types_d = ['p']*(z+1) + ['n']*(n-1)
    vp = generator_volumes(z, n)
    vd = generator_volumes(z+1, n-1)

    lu, lr, luc = 0.0, 0.0, 0.0
    for i in range(a-1):
        if abs(vp[i]) < 1e-30 or abs(vd[i]) < 1e-30: continue
        lratio = math.log(abs(vd[i])) - math.log(abs(vp[i]))  # ln, not log_q
        changed = [j for j in range(i+1, a)
                   if types_p[i]+types_p[j] != types_d[i]+types_d[j]]
        if not changed:
            luc += lratio
        else:
            nu = sum(1 for j in changed if types_p[i]=='n' and types_p[j]=='n')
            nr = sum(1 for j in changed if types_d[i]=='p' and types_d[j]=='p')
            t = nu + nr
            if nr==0: lu += lratio
            elif nu==0: lr += lratio
            else:
                lu += lratio*nu/t; lr += lratio*nr/t

    q_qwt = abs(Q*lu + Q_INV*lr + luc) * KAPPA  # κ, not κ_q
    deg = shell_degree(n)
    f = F_DEG2 if deg >= 2 else 1.0
    if n in MAGIC and deg >= 2: f *= F_PAULI
    return q_qwt * f


def approach_sqrt_product(z, n):
    """Q from geometric mean of base and converting-chain approaches.

    The base formula overcounts (includes spectators).
    The converting-chain undercounts (misses cascading effects).
    The geometric mean may balance these.
    """
    q_base = base_qvalue(z, n)
    q_conv = approach_converting_chain(z, n)
    return math.sqrt(q_base * q_conv) if q_base > 0 and q_conv > 0 else q_base


def approach_changed_generators_only(z, n):
    """Sum log_q ratios only for generators with changed crossings.

    Unlike converting-chain (which uses only σ_{Z-1}, σ_Z),
    this includes ALL generators that have at least one changed crossing.
    For light nuclei: all generators. For heavy: only ~Z generators.
    No q-weighting (all are equally physical).
    """
    a = z + n
    types_p = ['p']*z + ['n']*n
    types_d = ['p']*(z+1) + ['n']*(n-1)
    vp = generator_volumes(z, n)
    vd = generator_volumes(z+1, n-1)

    log_sum = 0.0
    for i in range(a-1):
        if abs(vp[i]) < 1e-30 or abs(vd[i]) < 1e-30: continue
        # Check if this generator has ANY changed crossing
        has_changed = any(types_p[i]+types_p[j] != types_d[i]+types_d[j]
                         for j in range(i+1, a))
        if not has_changed:
            continue  # skip spectator
        log_sum += math.log(abs(vd[i])) - math.log(abs(vp[i]))

    q_pred = abs(log_sum) * KAPPA
    deg = shell_degree(n)
    f = F_DEG2 if deg >= 2 else 1.0
    if n in MAGIC and deg >= 2: f *= F_PAULI
    return q_pred * f


def approach_changed_qweighted(z, n):
    """q-weighted sum over changed generators only (drop spectators)."""
    a = z + n
    types_p = ['p']*z + ['n']*n
    types_d = ['p']*(z+1) + ['n']*(n-1)
    vp = generator_volumes(z, n)
    vd = generator_volumes(z+1, n-1)

    lu, lr = 0.0, 0.0
    for i in range(a-1):
        if abs(vp[i]) < 1e-30 or abs(vd[i]) < 1e-30: continue
        lratio = (math.log(abs(vd[i])) - math.log(abs(vp[i]))) / LN_Q
        changed = [j for j in range(i+1, a)
                   if types_p[i]+types_p[j] != types_d[i]+types_d[j]]
        if not changed:
            continue  # skip spectator
        nu = sum(1 for j in changed if types_p[i]=='n' and types_p[j]=='n')
        nr = sum(1 for j in changed if types_d[i]=='p' and types_d[j]=='p')
        t = nu + nr
        if nr==0: lu += lratio
        elif nu==0: lr += lratio
        else:
            lu += lratio*nu/t; lr += lratio*nr/t

    q_pred = abs(Q*lu + Q_INV*lr) * KAPPA_Q
    deg = shell_degree(n)
    f = F_DEG2 if deg >= 2 else 1.0
    if n in MAGIC and deg >= 2: f *= F_PAULI
    return q_pred * f


# ══════════════════════════════════════════════════════════════════
# RUN ALL APPROACHES
# ══════════════════════════════════════════════════════════════════

APPROACHES = [
    ("Base (MAE 4.9%)", base_qvalue),
    ("Skein ratio",     approach_skein_ratio),
    ("Conv chain",      approach_converting_chain),
    ("Changed only",    approach_changed_generators_only),
    ("Changed q-wt",    approach_changed_qweighted),
    ("√(base×conv)",    approach_sqrt_product),
    ("Per-n_changed",   approach_per_nucleon),
    ("ln sanity",       approach_log_skein_qweighted),
]

if __name__ == "__main__":
    print("=" * 110)
    print("Q-VALUE FORMULA COMPARISON")
    print("=" * 110)

    # Print per-nucleus errors for each approach
    for name, func in APPROACHES:
        errs = []
        print(f"\n── {name} ──")
        for z, n, nuc, q_exp in BENCHMARKS:
            q_pred = func(z, n)
            err = (q_pred - q_exp) / q_exp * 100
            errs.append(abs(err))
            par = parity(z, n)
            mark = "◀" if abs(err) < 5 else " "
            print(f"  {nuc:>6} ({par}) {q_pred:>8.5f} vs {q_exp:>8.5f}  {err:>+6.1f}%{mark}")
        mae = sum(errs) / len(errs)
        rms = math.sqrt(sum(e**2 for e in errs) / len(errs))
        print(f"  → MAE = {mae:.1f}%,  RMS = {rms:.1f}%")

    # Summary table
    print(f"\n{'='*70}")
    print(f"SUMMARY")
    print(f"{'='*70}")
    print(f"{'Approach':>20}", end="")
    for _, _, nuc, _ in BENCHMARKS:
        print(f" {nuc:>7}", end="")
    print(f"  {'MAE':>5}")
    print("-" * 70)

    for name, func in APPROACHES:
        print(f"{name:>20}", end="")
        errs = []
        for z, n, _, q_exp in BENCHMARKS:
            q_pred = func(z, n)
            err = (q_pred - q_exp) / q_exp * 100
            errs.append(abs(err))
            print(f" {err:>+6.1f}%", end="")
        mae = sum(errs) / len(errs)
        print(f"  {mae:>5.1f}%")
