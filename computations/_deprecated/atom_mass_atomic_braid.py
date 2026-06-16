#!/usr/bin/env python3
"""
ATOMIC BRAID MASS: Compare nuclear vs atomic braid mass predictions.

For each atom Z=1-20:
1. Nuclear braid H_A(q): ordering [p]^Z [n]^N → Φ_nuc
2. Atomic braid H_{A+Z}(q): ep-pair ordering → Φ_atom
3. Mass prediction from both, compared with AME2020

The atomic braid uses iterative electron insertion (ep pairs).

Usage:
    python3 computations/atom_mass_atomic_braid.py
"""

import math, sys, subprocess, json, time
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, HBAR_Q_SQ
from experimental_constants import M_P_MEV, M_N_MEV, M_E_MEV
from witness_base import WitnessBuilder

HA = q0 - 1.0 / q0
z_markov = 1.0 / (q0**0.5 + q0**(-0.5))

# Calibration from hecke_engine
VOL_NEUTRON = 13.9484177283
m_n_derived = VOL_NEUTRON / HBAR_Q_SQ


def crossing_coeff(ti, tj):
    """Return (c, d) for strand types p, n, e."""
    if ti == 'p' and tj == 'p': return 1.0, 0.0
    if ti == 'n' and tj == 'n': return 1.0, -HA
    if (ti, tj) in [('p','n'),('n','p')]: return 1.0, -HA/2
    if (ti, tj) in [('p','e'),('e','p')]: return 1.0, -HA
    if (ti, tj) in [('n','e'),('e','n')]: return 0.0, 1.0
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
        V = z_markov * a + b
        if abs(V) < 1e-300: return float('inf')
        Phi += math.log(abs(V))
    return Phi


def find_nuclear_gs(Z, N):
    """Find nuclear GS ordering via exact search or steepest descent."""
    A = Z + N
    if A <= 1: return list('p' * Z + 'n' * N)
    total = math.comb(A, Z)
    if total <= 50000:
        best_Phi, best_o = float('inf'), None
        for pos in combinations(range(A), Z):
            o = ['n'] * A
            for p in pos: o[p] = 'p'
            Phi = compute_Phi(o)
            if Phi < best_Phi: best_Phi, best_o = Phi, list(o)
        return best_o
    # Steepest descent
    o = list('p' * Z + 'n' * N)
    Phi = compute_Phi(o)
    improved = True
    while improved:
        improved = False
        for pi in [i for i in range(A) if o[i] == 'p']:
            for ni in [i for i in range(A) if o[i] == 'n']:
                o[pi], o[ni] = 'n', 'p'
                new_Phi = compute_Phi(o)
                if new_Phi < Phi - 1e-12:
                    Phi = new_Phi; improved = True; break
                o[pi], o[ni] = 'p', 'n'
            if improved: break
    return o


def insert_electrons(nuclear_ordering, Z):
    """Iteratively insert Z electrons into nuclear ordering.
    Returns atomic ordering."""
    current = list(nuclear_ordering)
    for _ in range(Z):
        best_pos, best_Phi = 0, float('inf')
        for pos in range(len(current) + 1):
            candidate = list(current)
            candidate.insert(pos, 'e')
            Phi = compute_Phi(candidate)
            if Phi < best_Phi:
                best_Phi = Phi
                best_pos = pos
        current.insert(best_pos, 'e')
    return current


def load_nuclear_cert(Z, N):
    """Load Rust certificate for nuclear F_Pauli."""
    cert_dir = Path(__file__).parent.parent.parent / "tools" / "hecke-engine"
    names = {1:'h',2:'he',3:'li',4:'be',5:'b',6:'c',7:'n',8:'o',
             9:'f',10:'ne',11:'na',12:'mg'}
    sym = names.get(Z, f'z{Z}')
    A = Z + N
    for pat in [f"certificate-{A}{sym}.json", f"certificate-{A}{sym.lower()}.json"]:
        fpath = cert_dir / pat
        if fpath.exists():
            try:
                d = json.load(open(fpath))
                return d.get('f_pauli_f64', None)
            except:
                pass
    return None


# ══════════════════════════════════════════════════════════════
# ATOMS
# ══════════════════════════════════════════════════════════════

ATOMS = [
    (1, 0, "H",  938.783),
    (2, 2, "He", 3728.401),
    (3, 4, "Li", 6535.367),
    (4, 5, "Be", 8394.794),
    (5, 6, "B",  10255.103),
    (6, 6, "C",  11177.930),
    (7, 7, "N",  13043.781),
    (8, 8, "O",  14899.169),
    (9, 10,"F",  17696.901),
    (10,10,"Ne", 18622.835),
    (11,12,"Na", 21414.830),
    (12,12,"Mg", 22341.908),
    (13,14,"Al", 25133.143),
    (14,14,"Si", 26060.344),
    (15,16,"P",  28851.873),
    (16,16,"S",  29781.800),
    (17,18,"Cl", 32573.283),
    (18,22,"Ar", 37224.719),
    (19,20,"K",  36294.464),
    (20,20,"Ca", 37213.777),
]

print("=" * 120)
print("ATOMIC BRAID MASS: nuclear vs atomic braid comparison")
print(f"q₀ = {q0:.10f}   HA = {HA:.10f}")
print("Atomic braid: iterative ep-pair electron insertion, no stripping")
print("=" * 120)

# Phase 1: Compute Φ for all atoms (nuclear and atomic)
results = []
for Z, N, sym, M_obs in ATOMS:
    A = Z + N
    t0 = time.time()

    # Nuclear GS ordering
    nuc_ord = find_nuclear_gs(Z, N)
    Phi_nuc = compute_Phi(nuc_ord)

    # Atomic ordering (with electrons)
    atom_ord = insert_electrons(nuc_ord, Z)
    Phi_atom = compute_Phi(atom_ord)

    elapsed = time.time() - t0
    nuc_str = ''.join(nuc_ord)
    atom_str = ''.join(atom_ord)

    # Load nuclear certificate F_Pauli
    F_nuc = load_nuclear_cert(Z, N)

    results.append({
        'Z': Z, 'N': N, 'A': A, 'sym': sym, 'M_obs': M_obs,
        'nuc_ord': nuc_str, 'atom_ord': atom_str,
        'Phi_nuc': Phi_nuc, 'Phi_atom': Phi_atom,
        'F_nuc': F_nuc,
        'elapsed': elapsed,
    })

    print(f"  {A:>2d}{sym:>3s}  nuc={nuc_str:<20s} Φ_nuc={Phi_nuc:>+10.4f}  "
          f"atom={atom_str:<30s} Φ_atom={Phi_atom:>+10.4f}  "
          f"ΔΦ={Phi_atom-Phi_nuc:>+8.4f}  [{elapsed:.1f}s]")

# Phase 2: Mass predictions
# Calibrate: M = Z·m_p + N·m_n + Z·m_e + α·Φ
# Use H and C as calibration points

print("\n" + "=" * 120)
print("MASS PREDICTIONS")
print("=" * 120)

# Method 1: Nuclear Φ only (existing approach)
# Method 2: Atomic Φ
# Method 3: Atomic Φ + nuclear F_Pauli correction

for method_name, phi_key in [("Nuclear Φ", 'Phi_nuc'), ("Atomic Φ", 'Phi_atom')]:
    # Calibrate α from H (trivial) and C-12
    r_H = [r for r in results if r['sym'] == 'H'][0]
    r_C = [r for r in results if r['sym'] == 'C'][0]

    M_free_H = r_H['Z'] * M_P_MEV + r_H['N'] * M_N_MEV + r_H['Z'] * M_E_MEV
    M_free_C = r_C['Z'] * M_P_MEV + r_C['N'] * M_N_MEV + r_C['Z'] * M_E_MEV

    Phi_H = r_H[phi_key]
    Phi_C = r_C[phi_key]

    # M = M_free + alpha * Phi
    # For H: M_obs_H = M_free_H + alpha * Phi_H → alpha = (M_obs_H - M_free_H) / Phi_H
    # But Phi_H might be 0 for nuclear (H is single nucleon)
    # Use C as calibration: alpha = (M_obs_C - M_free_C) / Phi_C
    if abs(Phi_C) < 1e-30:
        print(f"\n  {method_name}: Φ_C ≈ 0, cannot calibrate")
        continue

    alpha = (r_C['M_obs'] - M_free_C) / Phi_C

    print(f"\n  {method_name}: α = {alpha:.4f}")
    print(f"  {'Atom':>6s} | {'M_pred':>12s} | {'M_obs':>12s} | {'Δ%':>8s} | {'Φ':>10s}")
    print(f"  {'─'*60}")

    errors = []
    for r in results:
        M_free = r['Z'] * M_P_MEV + r['N'] * M_N_MEV + r['Z'] * M_E_MEV
        Phi = r[phi_key]
        M_pred = M_free + alpha * Phi
        delta_pct = (M_pred - r['M_obs']) / r['M_obs'] * 100
        is_cal = " CAL" if r['sym'] in ['H', 'C'] else ""
        print(f"  {r['A']:>2d}{r['sym']:>4s} | {M_pred:>12.3f} | {r['M_obs']:>12.3f} | {delta_pct:>+7.3f}% | {Phi:>+10.4f}{is_cal}")
        if r['sym'] not in ['H', 'C']:
            errors.append(abs(delta_pct))

    if errors:
        print(f"  {len(errors)} predictions: mean = {sum(errors)/len(errors):.4f}%, max = {max(errors):.4f}%")

# Method 3: Atomic Φ + ln(F_nuc) correction
print(f"\n  Atomic Φ + ln(F_nuc):")
# Three calibration: H, He, C
cal_atoms = ['H', 'He']
r_He = [r for r in results if r['sym'] == 'He'][0]
r_H = [r for r in results if r['sym'] == 'H'][0]
r_C = [r for r in results if r['sym'] == 'C'][0]

# M = M_free + α·Φ_atom + β·ln(F_nuc)
# Calibrate with H and C (H has Φ_atom ≠ 0 unlike nuclear)
# Use He as third calibration for β
# Simple: fit α from C, then fit β from He
M_free_C = r_C['Z'] * M_P_MEV + r_C['N'] * M_N_MEV + r_C['Z'] * M_E_MEV
Phi_C_atom = r_C['Phi_atom']
F_C = r_C.get('F_nuc', 1.0) or 1.0
ln_F_C = math.log(F_C) if F_C > 0 else 0.0

M_free_He = r_He['Z'] * M_P_MEV + r_He['N'] * M_N_MEV + r_He['Z'] * M_E_MEV
Phi_He_atom = r_He['Phi_atom']
F_He = r_He.get('F_nuc', 1.0) or 1.0
ln_F_He = math.log(F_He) if F_He > 0 else 0.0

# Two-parameter fit: α, β from C and He
# C: M_obs_C = M_free_C + α·Φ_C + β·ln(F_C)
# He: M_obs_He = M_free_He + α·Φ_He + β·ln(F_He)
import numpy as np
A_mat = np.array([[Phi_C_atom, ln_F_C], [Phi_He_atom, ln_F_He]])
b_vec = np.array([r_C['M_obs'] - M_free_C, r_He['M_obs'] - M_free_He])
try:
    params = np.linalg.solve(A_mat, b_vec)
    alpha, beta = params
    print(f"  α = {alpha:.4f}, β = {beta:.4f}")
    print(f"  {'Atom':>6s} | {'M_pred':>12s} | {'M_obs':>12s} | {'Δ%':>8s} | {'Φ_atom':>10s} | {'ln(F)':>8s}")
    print(f"  {'─'*75}")

    errors = []
    for r in results:
        M_free = r['Z'] * M_P_MEV + r['N'] * M_N_MEV + r['Z'] * M_E_MEV
        Phi = r['Phi_atom']
        F = r.get('F_nuc', 1.0) or 1.0
        ln_F = math.log(F) if F > 0 else 0.0
        M_pred = M_free + alpha * Phi + beta * ln_F
        delta_pct = (M_pred - r['M_obs']) / r['M_obs'] * 100
        is_cal = " CAL" if r['sym'] in ['He', 'C'] else ""
        print(f"  {r['A']:>2d}{r['sym']:>4s} | {M_pred:>12.3f} | {r['M_obs']:>12.3f} | {delta_pct:>+7.3f}% | {Phi:>+10.4f} | {ln_F:>+8.4f}{is_cal}")
        if r['sym'] not in ['H', 'He', 'C']:
            errors.append(abs(delta_pct))

    if errors:
        print(f"  {len(errors)} predictions: mean = {sum(errors)/len(errors):.4f}%, max = {max(errors):.4f}%")
except np.linalg.LinAlgError:
    print("  Cannot solve 2-parameter fit")

# Witness
w = WitnessBuilder("atom-mass-atomic-braid", engine="v12-atomic")
w.set_description("Atomic braid mass: ep-pair electron insertion into nuclear braid")
for r in results:
    w.add_parameter(f"{r['sym']}_Phi_nuc", str(r['Phi_nuc']))
    w.add_parameter(f"{r['sym']}_Phi_atom", str(r['Phi_atom']))
    w.add_parameter(f"{r['sym']}_atom_ord", r['atom_ord'])
w.save()
