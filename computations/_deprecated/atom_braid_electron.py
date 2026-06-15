#!/usr/bin/env python3
"""
ATOMIC BRAID: electrons included in the H_{A+Z}(q) braid.

The nuclear braid H_A(q) uses A nucleon strands. This script
adds Z electron strands, creating H_{A+Z}(q) with crossing
coefficients:

  pp → σ:          c = 1,   d = 0             (strong repulsion)
  nn → σ⁻¹:        c = 1,   d = -HA           (strong inverse)
  pn → ½(σ+σ⁻¹):  c = 1,   d = -HA/2         (strong mixed)
  pe → α_EM mixed: c = α,   d = -α·HA/2       (EM attraction)
  ne →  trivial:   c = 0,   d = 0             (neutral)
  ee → α_EM rep:   c = α,   d = 0             (EM repulsion)

where α = α_EM ≈ 0.00729... derived from q₀.

Usage:
    python3 folio-assistant/computations/atom_braid_electron.py
"""

import math, sys, time
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, HBAR_Q_SQ, LN_Q
from experimental_constants import M_P_MEV, M_N_MEV, M_E_MEV

HA = q0 - 1.0/q0
z = 1.0 / (q0**0.5 + q0**(-0.5))

# α_EM from q₀ (CS-corrected, physical value)
from hecke_core import alpha_em as _alpha_em
ALPHA_EM = _alpha_em
print(f"α_EM = {ALPHA_EM:.6f}  (CODATA: 0.007297)")


def crossing_coeff(ti, tj):
    """Return (c, d) for strand types ti, tj.
    Types: 1=proton, 0=neutron, 2=electron."""
    a = ALPHA_EM
    if ti == 1 and tj == 1: return 1.0, 0.0             # pp: strong
    if ti == 0 and tj == 0: return 1.0, -HA              # nn: strong
    if (ti == 1 and tj == 0) or (ti == 0 and tj == 1):
        return 1.0, -HA / 2                               # pn: strong mixed
    if (ti == 1 and tj == 2) or (ti == 2 and tj == 1):
        return a, -a * HA / 2                              # pe: EM attraction
    if (ti == 0 and tj == 2) or (ti == 2 and tj == 0):
        return 0.0, 0.0                                   # ne: trivial
    if ti == 2 and tj == 2:
        return a, 0.0                                      # ee: EM repulsion
    return 0.0, 0.0


def compute_Phi(ordering):
    """Quantum dilogarithm volume Φ_q = Σ ln|V̂_i|."""
    A = len(ordering)
    if A <= 1: return 0.0
    Phi = 0.0
    for gen in range(A - 1):
        a_val, b_val = 0.0, 1.0
        for j in range(gen + 1, A):
            c, d = crossing_coeff(ordering[gen], ordering[j])
            if c == 0.0 and d == 0.0:
                continue  # trivial crossing (ne)
            a_val, b_val = a_val * c * HA + a_val * d + b_val * c, a_val * c + b_val * d
        V = z * a_val + b_val
        if abs(V) < 1e-300: return float('inf')
        Phi += math.log(abs(V))
    return Phi


def compute_Phi_nuclear_only(ordering):
    """Φ_q for ONLY the nucleon part (ignore electron strands)."""
    nuc = [t for t in ordering if t != 2]
    return compute_Phi(nuc)


def find_gs_atomic(Z, N):
    """Find ground-state ordering for the atomic braid [p,n,e].
    Try several orderings: nucleons first, interleaved, etc."""
    A = Z + N
    n_strands = A + Z  # total strands including electrons

    # Strategy: use nuclear GS ordering + append electrons
    # (or interleave electrons among nucleons)
    best = (float('inf'), None)

    # 1. Nuclear GS + electrons at end
    nuc_gs = find_gs_nuclear(Z, N)
    o1 = nuc_gs + [2] * Z
    Phi1 = compute_Phi(o1)
    if Phi1 < best[0]: best = (Phi1, o1)

    # 2. Electrons at beginning
    o2 = [2] * Z + nuc_gs
    Phi2 = compute_Phi(o2)
    if Phi2 < best[0]: best = (Phi2, o2)

    # 3. Interleaved: [p, e, p, e, ..., n, n, ...]
    o3 = []
    e_placed = 0
    for t in nuc_gs:
        o3.append(t)
        if t == 1 and e_placed < Z:
            o3.append(2)
            e_placed += 1
    while e_placed < Z:
        o3.append(2)
        e_placed += 1
    Phi3 = compute_Phi(o3)
    if Phi3 < best[0]: best = (Phi3, o3)

    # 4. [e, p, n, e, p, n, ...]  round-robin
    elems = [1] * Z + [0] * N + [2] * Z
    o4 = sorted(elems, key=lambda x: (x == 0, x == 1, x == 2))  # e, p, n
    Phi4 = compute_Phi(o4)
    if Phi4 < best[0]: best = (Phi4, o4)

    return best[1], best[0]


def find_gs_nuclear(Z, N):
    """Find nuclear GS ordering (p=1, n=0 only)."""
    A = Z + N
    if A <= 1: return [1] if Z > 0 else [0]
    total = math.comb(A, Z)
    if total <= 50000:
        best_Phi, best_o = float('inf'), None
        for pos in combinations(range(A), Z):
            o = [0]*A
            for p in pos: o[p] = 1
            Phi = compute_Phi(o)
            if Phi < best_Phi: best_Phi, best_o = Phi, list(o)
        return best_o
    # Steepest descent for large A
    o = [1]*Z + [0]*N
    Phi = compute_Phi(o)
    improved = True
    while improved:
        improved = False
        for pi in [i for i in range(A) if o[i]==1]:
            for ni in [i for i in range(A) if o[i]==0]:
                o[pi], o[ni] = 0, 1
                new_Phi = compute_Phi(o)
                if new_Phi < Phi - 1e-12:
                    Phi = new_Phi; improved = True; break
                o[pi], o[ni] = 1, 0
            if improved: break
    return o


# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════

ELEMENTS = {
    1:  ("H",   1, 0),
    2:  ("He",  2, 2),
    3:  ("Li",  3, 4),
    4:  ("Be",  4, 5),
    5:  ("B",   5, 6),
    6:  ("C",   6, 6),
    7:  ("N",   7, 7),
    8:  ("O",   8, 8),
    9:  ("F",   9, 10),
    10: ("Ne",  10, 10),
}

print("=" * 100)
print("ATOMIC BRAID: electrons in the H_{A+Z}(q) braid")
print(f"q₀ = {q0:.10f}   HA = {HA:.10f}   α_EM = {ALPHA_EM:.6f}")
print(f"Strand types: p (proton), n (neutron), e (electron)")
print("=" * 100)

print(f"\n{'Atom':>6s} | {'A':>3s} | {'A+Z':>3s} | {'Φ_nuc':>10s} | {'Φ_atom':>10s} | {'ΔΦ':>10s} | {'Ordering'}")
print("-" * 100)

results = []
for Zval in range(1, 11):
    sym, Z, N = ELEMENTS[Zval]
    A = Z + N
    n_total = A + Z

    t0 = time.time()

    # Nuclear-only Φ
    nuc_gs = find_gs_nuclear(Z, N)
    Phi_nuc = compute_Phi(nuc_gs)

    # Atomic (with electrons) Φ
    atom_gs, Phi_atom = find_gs_atomic(Z, N)
    elapsed = time.time() - t0

    delta = Phi_atom - Phi_nuc

    ordering_str = ''.join(['p' if t==1 else 'n' if t==0 else 'e' for t in atom_gs])
    if len(ordering_str) > 30: ordering_str = ordering_str[:30] + "..."

    print(f"{A:>2d}{sym:>4s} | {A:>3d} | {n_total:>3d} | {Phi_nuc:>+10.4f} | {Phi_atom:>+10.4f} | {delta:>+10.6f} | {ordering_str}  [{elapsed:.1f}s]")

    results.append({
        'sym': sym, 'Z': Z, 'N': N, 'A': A, 'n_total': n_total,
        'Phi_nuc': Phi_nuc, 'Phi_atom': Phi_atom, 'delta': delta,
    })

print()
print("KEY QUESTION: Does the electron ΔΦ correlate with mass prediction error?")
print("If yes → electrons in the braid capture binding corrections we're missing.")
print("If no → electrons are perturbative noise and don't help.")
