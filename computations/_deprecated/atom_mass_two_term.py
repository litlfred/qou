#!/usr/bin/env python3
"""
TWO-TERM MASS FORMULA: topological + algebraic.

  M(Z,N) = E₀ × [Z×𝔪_p + N×𝔪_n + α×Φ_q(Z,N)]

Term 1: Z×𝔪_p + N×𝔪_n — constituent mass
  𝔪_n = Vol(neutron braid)/ℏ_q² (archimedean, SnapPy)
  𝔪_p = calibrated from H (proton braid is non-hyperbolic)

Term 2: α×Φ_q — binding correction from quantum dilogarithm
  Φ_q = Σ ln|V̂_i| (exact in q, from transfer matrix chain)
  α = binding scale (calibrated from He and C)

3 calibration atoms (H, He, C) → 3 parameters (E₀, 𝔪_p, α).
7 atoms (Li, Be, B, N, O, F, Ne) are pure PREDICTIONS.

Usage:
    python3 computations/atom_mass_two_term.py
"""

import math, sys, time
from fractions import Fraction
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, HBAR_Q_SQ
from experimental_constants import M_P_MEV, M_N_MEV, M_E_MEV
from witness_base import WitnessBuilder

VOL_NEUTRON = 13.9484177283
hbar_q_sq = HBAR_Q_SQ
q_rat = Fraction(111, 100)
qi_rat = Fraction(100, 111)
ha_rat = q_rat - qi_rat
z_rat = Fraction(4993, 10000)

def crossing(ti, tj):
    if ti == 1 and tj == 1: return Fraction(1), Fraction(0)
    elif ti == 0 and tj == 0: return Fraction(1), -ha_rat
    else: return Fraction(1), -ha_rat / 2

def chain_reduce(gi, o):
    a, b = Fraction(0), Fraction(1)
    for j in range(gi + 1, len(o)):
        c, d = crossing(o[gi], o[j])
        a, b = a*c*ha_rat + a*d + b*c, a*c + b*d
    return a, b

def gs_ordering(p, n):
    A = p + n
    if math.comb(A, p) <= 5000:
        best_e, best_o = None, None
        for pos in combinations(range(A), p):
            o = [0]*A
            for pp in pos: o[pp] = 1
            e = sum(float(z_rat*chain_reduce(i,o)[0]+chain_reduce(i,o)[1]) for i in range(A-1))
            if best_e is None or e < best_e: best_e, best_o = e, o
        return best_o
    else:
        o, pi, ni = [], 0, 0
        for k in range(A):
            if pi < p and (ni >= n or k%2==0): o.append(1); pi += 1
            else: o.append(0); ni += 1
        return o

def phi_q(ordering):
    A = len(ordering)
    if A <= 1: return 0.0
    total = 0.0
    for i in range(A - 1):
        a, b = chain_reduce(i, ordering)
        v = float(z_rat * a + b)
        if abs(v) > 1e-30: total += math.log(abs(v))
    return total

def L1_norm(ordering):
    A = len(ordering)
    if A <= 1: return 0.0
    return sum(abs(float(z_rat * chain_reduce(i, ordering)[0] + chain_reduce(i, ordering)[1])) for i in range(A-1))

def n_nn_count(ordering):
    A = len(ordering)
    return sum(1 for i in range(A) for j in range(i+1,A) if ordering[i]==0 and ordering[j]==0)

def n_cross_asym(ordering):
    """n_nn - n_pp: crossing asymmetry."""
    A = len(ordering)
    nn = sum(1 for i in range(A) for j in range(i+1,A) if ordering[i]==0 and ordering[j]==0)
    pp = sum(1 for i in range(A) for j in range(i+1,A) if ordering[i]==1 and ordering[j]==1)
    return nn - pp

ELEMENTS = [
    ("H",  "¹H",  1, 0,  938.783),
    ("He", "⁴He", 2, 2,  3728.401),
    ("Li", "⁷Li", 3, 4,  6535.367),
    ("Be", "⁹Be", 4, 5,  8394.794),
    ("B",  "¹¹B", 5, 6,  10255.103),
    ("C",  "¹²C", 6, 6,  11177.930),
    ("N",  "¹⁴N", 7, 7,  13043.781),
    ("O",  "¹⁶O", 8, 8,  14899.169),
    ("F",  "¹⁹F", 9, 10, 17696.901),
    ("Ne", "²⁰Ne",10,10, 18622.835),
    ("Na", "²³Na",11,12, 21414.830),
    ("Mg", "²⁴Mg",12,12, 22341.908),
    ("Al", "²⁷Al",13,14, 25133.143),
    ("Si", "²⁸Si",14,14, 26060.344),
    ("P",  "³¹P", 15,16, 28851.873),
    ("S",  "³²S", 16,16, 29781.800),
    ("Cl", "³⁵Cl",17,18, 32573.283),
    ("Ar", "⁴⁰Ar",18,22, 37224.719),
    ("K",  "³⁹K", 19,20, 36294.464),
    ("Ca", "⁴⁰Ca",20,20, 37213.777),
    ("Sc", "⁴⁵Sc",21,24, 41875.569),
    ("Ti", "⁴⁸Ti",22,26, 44680.842),
    ("V",  "⁵¹V", 23,28, 47486.136),
    ("Cr", "⁵²Cr",24,28, 48383.826),
    ("Mn", "⁵⁵Mn",25,30, 51189.120),
    ("Fe", "⁵⁶Fe",26,30, 52089.806),
    ("Co", "⁵⁹Co",27,32, 54895.100),
    ("Ni", "⁵⁸Ni",28,30, 53966.267),
    ("Cu", "⁶³Cu",29,34, 58618.364),
    ("Zn", "⁶⁴Zn",30,34, 59549.474),
    ("Ga", "⁶⁹Ga",31,38, 64218.721),
    ("Ge", "⁷⁴Ge",32,42, 68862.540),
    ("As", "⁷⁵As",33,42, 69793.047),
    ("Se", "⁸⁰Se",34,46, 74436.856),
    ("Br", "⁷⁹Br",35,44, 73537.269),
    ("Kr", "⁸⁴Kr",36,48, 78181.105),
    ("Rb", "⁸⁵Rb",37,48, 79111.400),
    ("Sr", "⁸⁸Sr",38,50, 81886.301),
    ("Y",  "⁸⁹Y", 39,50, 82816.598),
    ("Zr", "⁹⁰Zr",40,50, 83746.895),
]

def main():
    m_n = VOL_NEUTRON / hbar_q_sq

    print("=" * 120)
    print("TWO-TERM MASS: M = E₀ × [Z×𝔪_p + N×𝔪_n + α×F(Z,N)]")
    print(f"𝔪_n = Vol(𝔫)/ℏ_q² = {m_n:.4f} Hecke units")
    print("=" * 120)

    # Compute binding functional for all atoms
    atoms = []
    for name, label, Z, N, M_obs in ELEMENTS:
        A = Z + N
        o = gs_ordering(Z, N) if A > 1 else [1]
        atoms.append({
            'label': label, 'Z': Z, 'N': N, 'A': A, 'M_obs': M_obs,
            'phi_q': phi_q(o), 'L1': L1_norm(o),
            'n_nn': n_nn_count(o), 'asym': n_cross_asym(o),
        })

    M_H = atoms[0]['M_obs']
    M_He = atoms[1]['M_obs']
    M_C = atoms[5]['M_obs']
    lhs1 = M_He - 2 * M_H
    lhs2 = M_C - 6 * M_H

    # Test each binding functional
    functionals = [
        ("Φ_q",        lambda a: a['phi_q']),
        ("L¹",         lambda a: a['L1']),
        ("n_nn",       lambda a: float(a['n_nn'])),
        ("n_nn−n_pp",  lambda a: float(a['asym'])),
    ]

    for func_name, func in functionals:
        f_he = func(atoms[1])
        f_c = func(atoms[5])
        denom = f_he * lhs2 - f_c * lhs1
        if abs(denom) < 1e-10:
            print(f"\n  {func_name}: DEGENERATE (cannot solve)")
            continue
        alpha = m_n * (6*lhs1 - 2*lhs2) / denom
        E0 = lhs1 / (2*m_n + alpha*f_he)
        mp = M_H / E0 if abs(E0) > 1e-10 else 0

        print(f"\n{'='*120}")
        print(f"  BINDING FUNCTIONAL: {func_name}")
        print(f"  α = {alpha:.6f},  E₀ = {E0:.6f} MeV,  𝔪_p = {mp:.4f}")
        print(f"  m_n(derived) = {E0*m_n:.3f} MeV (CODATA: {M_N_MEV+M_E_MEV:.3f})")
        print(f"{'='*120}")
        print(f"{'Atom':>5} | {'M_pred':>12} | {'M_obs':>12} | {'Δ MeV':>8} | {'Δ%':>7} | {'cal?':>4}")
        print("─" * 65)

        pred_errors = []
        for a in atoms:
            f_val = func(a)
            m_tot = a['Z'] * mp + a['N'] * m_n + alpha * f_val
            M_pred = E0 * m_tot
            delta = M_pred - a['M_obs']
            pct = delta / a['M_obs'] * 100
            cal = "*" if a['label'] in ['¹H', '⁴He', '¹²C'] else ""
            print(f"{a['label']:>5} | {M_pred:12.3f} | {a['M_obs']:12.3f} | {delta:+8.3f} | {pct:+6.2f}% | {cal:>4}")
            if not cal:
                pred_errors.append(abs(pct))

        mean_err = sum(pred_errors) / len(pred_errors) if pred_errors else 0
        max_err = max(pred_errors) if pred_errors else 0
        print(f"  Predictions (7 atoms): mean |Δ%| = {mean_err:.2f}%, max = {max_err:.2f}%")

    w = WitnessBuilder("atom-mass-two-term", engine="python")
    w.set_description("Two-term mass: topological constituent + algebraic binding.")
    w.add_parameter("q0", str(q0))
    w.add_parameter("vol_neutron", str(VOL_NEUTRON))
    w.save()

if __name__ == "__main__":
    main()
