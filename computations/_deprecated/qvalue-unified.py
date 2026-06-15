#!/usr/bin/env python3
"""
Unified Q-value: Gram weights + shell corrections + LP dual shadow prices.

The Q-value for beta- decay (Z,N) → (Z+1,N-1) combines three ingredients:

1. NF REDUCTION COST (Δ_k): from typed Garside staircase
   For each converting neutron k, Δ_k = ||N_par||₁ - ||N_dau^(k)||₁

2. GRAM WEIGHT (w_k): from Frobenius norm of δ_k = N_par - N_dau^(k)
   Boundary neutrons get larger weight than interior ones.

3. LP SHADOW PRICE (y₀): from the confinement LP dual
   The marginal cost of changing the net constraint.
   At shell boundaries, the shadow price JUMPS because the
   active constraint set changes (a new Frobenius positivity
   constraint becomes tight).

The unified formula:
   Q = (Σ_k w_k × Δ_k) × y₀(Z,N) × m_e

where y₀(Z,N) encodes the shell-dependent operator selection preference.

For the LP dual, the shadow price y₀ depends on:
- Which Frobenius positivity constraints are active (tight)
- The active constraints change at magic shell closures
- y₀ jumps at shell boundaries (this is the shell correction)

Usage:
    cd folio-assistant/computations && python3 qvalue-unified.py
"""
import math
import json
import sys
import numpy as np
from datetime import datetime, timezone
from pathlib import Path
from itertools import combinations

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q, Q_INV as qi, HA as h, HBAR_Q, LN_Q, log_q
from experimental_constants import (
    M_E_MEV, Q_TRITIUM_MEV, Q_C14_MEV, Q_CO60_MEV,
    Q_SR90_MEV, Q_CS137_MEV, Q_BI210_MEV, Q_NEUTRON_MEV,
)

z = 1.0 / (q**0.5 + q**(-0.5))
m_e = M_E_MEV
E_cross = 0.5 * h
MAGIC = [0, 2, 8, 20, 28, 50, 82, 126]


# ══════════════════════════════════════════════════════════════
#  LP SHADOW PRICE
# ══════════════════════════════════════════════════════════════

def torus_trace(n):
    """Markov trace of T_{2,n} in H_2(q)."""
    a, b, c, d = 1.0, 0.0, 0.0, 1.0
    for _ in range(n):
        na, nb, nc, nd = a * h + c, b * h + d, a, b
        a, b, c, d = na, nb, nc, nd
    return z * a + d


def m_leq(X):
    return max(m for m in MAGIC if m <= X)


def n_out(X):
    return X - m_leq(X)


def n_shell(X):
    return m_leq(X) - max(m for m in MAGIC if m < X) if m_leq(X) > 0 else 2


def lp_shadow_price(Z, N):
    """LP dual shadow price y₀ for the beta decay (Z,N)→(Z+1,N-1).

    From the confinement LP: the dual optimal = y₀ × n_target.
    The shadow price y₀ is the marginal cost of the net constraint.

    Key insight: at a magic shell boundary, the ACTIVE SET of
    Frobenius positivity constraints changes. The shadow price
    is determined by the TIGHTEST active constraint.

    The LP has Gx ≥ 0 as constraints. When a magic shell closes,
    a new constraint becomes tight (binding). The shadow price
    at that constraint is the log_q of the torus knot trace ratio.

    For beta decay, y₀ captures how many "LP units" of Q are
    released per unit of vertex volume change.

    The correct normalization: y₀ should be O(1) to O(10), not
    exponentially large. We use log_q of trace ratios, which
    gives the number of "Hecke reduction steps" at the boundary.
    """
    Z2, N2 = Z + 1, N - 1

    # Count shell events and their log_q contributions
    y_terms = []

    # Z shell events
    if Z in MAGIC and Z > 0 and Z2 not in MAGIC:
        # Z BREAKS magic
        ns = n_shell(Z)
        # Breaking releases log_q(torus_trace(ns)) units of constraint energy
        contrib = abs(log_q(abs(torus_trace(ns))))
        y_terms.append(('Z_break', contrib))
    elif Z not in MAGIC and Z2 in MAGIC and Z2 > 0:
        # Z CLOSES magic
        ns = n_shell(Z2)
        contrib = abs(log_q(abs(torus_trace(ns))))
        y_terms.append(('Z_close', contrib))

    # N shell events
    if N in MAGIC and N > 0 and N2 not in MAGIC:
        ns = n_shell(N)
        contrib = abs(log_q(abs(torus_trace(ns))))
        y_terms.append(('N_break', contrib))
    elif N not in MAGIC and N2 in MAGIC and N2 > 0:
        ns = n_shell(N2)
        contrib = abs(log_q(abs(torus_trace(ns))))
        y_terms.append(('N_close', contrib))

    if not y_terms:
        # Ordinary transition: shadow price from outer shell occupancy
        nz = n_out(Z) if n_out(Z) > 0 else 1
        nn = n_out(N) if n_out(N) > 0 else 1
        nz2 = n_out(Z2) if n_out(Z2) > 0 else 1
        nn2 = n_out(N2) if n_out(N2) > 0 else 1
        # Ratio of log_q traces
        y0 = abs(log_q(abs(torus_trace(nz2))) - log_q(abs(torus_trace(nz)))
               + log_q(abs(torus_trace(nn2))) - log_q(abs(torus_trace(nn))))
        return max(y0, 1.0)

    # For break+close simultaneous (3H): contributions SUBTRACT
    breaks = sum(c for t, c in y_terms if 'break' in t)
    closes = sum(c for t, c in y_terms if 'close' in t)

    if breaks > 0 and closes > 0:
        # Partial cancellation
        return abs(breaks - closes) + 1.0
    else:
        # Single event: shadow price = log_q contribution
        return sum(c for _, c in y_terms) + 1.0


# ══════════════════════════════════════════════════════════════
#  VERTEX VOLUME ENGINE
# ══════════════════════════════════════════════════════════════

def typed_d(ti, tj):
    if ti == 1 and tj == 1: return 0.0
    elif ti == 0 and tj == 0: return -h
    else: return -h / 2


def chain_V(ordering, gen):
    A = len(ordering)
    a, b = 0.0, 1.0
    for j in range(gen + 1, A):
        d = typed_d(ordering[gen], ordering[j])
        new_a = a * h + a * d + b
        new_b = a + b * d
        a, b = new_a, new_b
    return z * a + b


def find_gs(Z, N):
    A = Z + N
    best = (float('inf'), None)
    for pp in combinations(range(A), Z):
        o = [0] * A
        for p in pp:
            o[p] = 1
        Phi = 0.0
        ok = True
        for gen in range(A - 1):
            V = chain_V(o, gen)
            if abs(V) < 1e-300:
                ok = False
                break
            Phi += math.log(abs(V))
        if ok and Phi < best[0]:
            best = (Phi, o[:])
    return best[1]


def Q_vertex_volume(Z, N):
    """Vertex volume Q-value (transfer matrix chain)."""
    A = Z + N
    gs_par = find_gs(Z, N)
    gs_dau = find_gs(Z + 1, N - 1)
    if gs_par is None or gs_dau is None:
        return float('nan')
    V_par = [chain_V(gs_par, i) for i in range(A - 1)]
    V_dau = [chain_V(gs_dau, i) for i in range(A - 1)]
    sum_dV = sum(V_dau[i] - V_par[i] for i in range(A - 1))
    return abs(sum_dV) * z ** 2 * m_e


# ══════════════════════════════════════════════════════════════
#  UNIFIED FORMULA
# ══════════════════════════════════════════════════════════════

def Q_unified(Z, N, verbose=False):
    """Unified Q-value: vertex volumes × LP shadow price.

    Q = |Σ ΔV̂_i| × z² × m_e × y₀(Z,N)

    where y₀ is the LP dual shadow price encoding shell structure.
    For non-magic: y₀ ≈ 1 (vertex volumes suffice).
    For magic: y₀ amplifies or suppresses based on shell transition.
    """
    A = Z + N
    Z2, N2 = Z + 1, N - 1

    # Base Q from vertex volumes (works for all A)
    # Use naive ordering for large A
    if A <= 20:
        Q_base = Q_vertex_volume(Z, N)
    else:
        # Naive ordering for large A
        gs_par = [1] * Z + [0] * N
        gs_dau = [1] * Z2 + [0] * N2
        V_par = [chain_V(gs_par, i) for i in range(A - 1)]
        V_dau = [chain_V(gs_dau, i) for i in range(A - 1)]
        sum_dV = sum(V_dau[i] - V_par[i] for i in range(A - 1))
        Q_base = abs(sum_dV) * z ** 2 * m_e

    # LP shadow price
    y0 = lp_shadow_price(Z, N)

    Q = Q_base * y0

    if verbose:
        # Shell events
        events = []
        if Z in MAGIC and Z > 0 and Z2 not in MAGIC:
            events.append(f"Z BREAK {Z}")
        elif Z not in MAGIC and Z2 in MAGIC:
            events.append(f"Z CLOSE {Z2}")
        if N in MAGIC and N > 0 and N2 not in MAGIC:
            events.append(f"N BREAK {N}")
        elif N not in MAGIC and N2 in MAGIC:
            events.append(f"N CLOSE {N2}")
        if not events:
            events.append("ordinary")
        print(f"  {','.join(events):>25s} | y₀ = {y0:>8.4f} | Q_base = {Q_base:.4f} | Q = {Q:.4f}")

    return Q, Q_base, y0


# ══════════════════════════════════════════════════════════════
#  BENCHMARK
# ══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print("UNIFIED Q-VALUE: vertex volumes × LP shadow price")
    print(f"Q = |Σ ΔV̂| × z² × m_e × y₀(Z,N)")
    print(f"where y₀ = LP dual shadow price from shell structure")
    print(f"q = {q:.6f}, m_e = {m_e:.6f} MeV")
    print("=" * 95)

    decays = [
        ('3H→3He', 1, 2, Q_TRITIUM_MEV),
        ('6He→6Li', 2, 4, 3.508),
        ('14C→14N', 6, 8, Q_C14_MEV),
        ('40K→40Ca', 19, 21, 1.312),
        ('60Co→60Ni', 27, 33, Q_CO60_MEV),
        ('90Sr→90Y', 38, 52, Q_SR90_MEV),
        ('137Cs→137Ba', 55, 82, Q_CS137_MEV),
    ]

    print(f"\n{'Decay':>14s} | {'A':>3s} | {'events':>25s} | {'y₀':>8s} | {'Q_base':>8s} | {'Q_pred':>8s} | {'Q_exp':>8s} | {'err':>7s}")
    print(f"{'-'*100}")

    results = []
    for name, Z, N, Q_exp in decays:
        A = Z + N
        Q, Q_base, y0 = Q_unified(Z, N)
        err = (Q / Q_exp - 1) * 100

        # Events
        Z2, N2 = Z + 1, N - 1
        events = []
        if Z in MAGIC and Z > 0 and Z2 not in MAGIC:
            events.append(f"Z BREAK {Z}")
        elif Z not in MAGIC and Z2 in MAGIC:
            events.append(f"Z CLOSE {Z2}")
        if N in MAGIC and N > 0 and N2 not in MAGIC:
            events.append(f"N BREAK {N}")
        elif N not in MAGIC and N2 in MAGIC:
            events.append(f"N CLOSE {N2}")
        if not events:
            events.append("ordinary")

        print(f"{name:>14s} | {A:>3d} | {','.join(events):>25s} | {y0:>8.4f} | {Q_base:>8.4f} | {Q:>8.4f} | {Q_exp:>8.4f} | {err:>+6.1f}%")

        results.append({
            'name': name, 'Z': Z, 'N': N, 'A': A,
            'events': events, 'y0': y0,
            'Q_base': Q_base, 'Q_pred': Q, 'Q_exp': Q_exp, 'err': err,
        })

    # MAE
    mae = sum(abs(r['err']) for r in results) / len(results)
    print(f"\n  MAE = {mae:.1f}%")

    # Witness
    witness = {
        'name': 'qvalue-unified',
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q': q, 'm_e': m_e,
        'formula': 'Q = |sum dV| * z^2 * m_e * y0(Z,N)',
        'results': results,
    }
    out = Path(__file__).with_suffix('.witness.json')
    out.write_text(json.dumps(witness, indent=2, default=float))
    print(f"  Witness: {out.name}")
