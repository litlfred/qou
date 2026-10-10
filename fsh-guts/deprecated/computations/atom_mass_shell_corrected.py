#!/usr/bin/env python3
"""
TWO-TERM MASS WITH GARSIDE NF SHELL CORRECTIONS.

At shell boundaries (magic numbers 2, 8, 20, 28, 50, 82, 126),
the inter-nucleon crossing coefficient changes from bare (c=1, d=...)
to the Chebyshev torus knot coefficient (c_n, d_n) of T_{2,n_s}.

This modifies Φ_q at the shell boundary generators, providing
the missing shell correction that reduces the systematic +0.3%
drift at high Z.

The shell construction:
  1. Within a shell: bare crossings (c=1, d from pair type)
  2. At shell boundary: crossing mediated by T_{2,n_s}
     with c_{n_s}, d_{n_s} from Chebyshev recurrence

Chebyshev recurrence:
  c₁ = 1, d₁ = 0
  c_{n+1} = c_n(q-q⁻¹) + c_n + d_n
  d_{n+1} = c_n

Usage:
    python3 computations/atom_mass_shell_corrected.py
"""

import math, sys
from fractions import Fraction
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, HBAR_Q_SQ
from experimental_constants import M_P_MEV, M_N_MEV, M_E_MEV
from witness_base import WitnessBuilder

VOL_NEUTRON = 13.9484177283
q_rat = Fraction(111, 100)
qi_rat = Fraction(100, 111)
ha_rat = q_rat - qi_rat
z_rat = Fraction(4993, 10000)

# ══════════════════════════════════════════════════════════════
# §1  CHEBYSHEV TORUS KNOT COEFFICIENTS
# ══════════════════════════════════════════════════════════════

def chebyshev_coefficients(n_shell, q_r=q_rat):
    """Compute (c_n, d_n) for torus knot T_{2,n} via Chebyshev recurrence.
    c₁=1, d₁=0; c_{n+1} = c_n·HA + c_n + d_n; d_{n+1} = c_n."""
    ha = q_r - Fraction(1, 1) / q_r
    c, d = Fraction(1), Fraction(0)
    for _ in range(n_shell - 1):
        c, d = c * ha + c + d, c
    return c, d


# Magic numbers and their shell sizes
MAGIC_NUMBERS = [2, 8, 20, 28, 50, 82, 126]
SHELL_SIZES = [2, 6, 12, 8, 22, 32, 44]  # occupancy of each shell


def get_shell_info(A):
    """For a nucleus of mass number A, determine which shells are closed
    and the current shell occupancy.
    Returns list of (shell_size, is_closed) pairs."""
    remaining = A
    shells = []
    for ss in SHELL_SIZES:
        if remaining >= ss:
            shells.append((ss, True))
            remaining -= ss
        elif remaining > 0:
            shells.append((remaining, False))
            remaining = 0
        else:
            break
    return shells


# ══════════════════════════════════════════════════════════════
# §2  SHELL-CORRECTED CROSSING COEFFICIENTS
# ══════════════════════════════════════════════════════════════

def crossing_with_shell(ti, tj, is_shell_boundary, shell_size):
    """Crossing coefficient, modified at shell boundaries.

    Within a shell: bare crossing (c=1, d from pair type).
    At shell boundary: Chebyshev coefficient (c_n, d_n) modulates
    the pair-type coefficient.
    """
    # Base crossing
    if ti == 1 and tj == 1:
        c_base, d_base = Fraction(1), Fraction(0)
    elif ti == 0 and tj == 0:
        c_base, d_base = Fraction(1), -ha_rat
    else:
        c_base, d_base = Fraction(1), -ha_rat / 2

    if is_shell_boundary and shell_size > 1:
        c_shell, d_shell = chebyshev_coefficients(shell_size)
        # The shell crossing modulates: effective c = c_base × c_shell,
        # effective d = c_base × d_shell + d_base × c_shell
        # This is the composition of two transfer matrices
        c_eff = c_base * c_shell
        d_eff = c_base * d_shell + d_base
        return c_eff, d_eff
    else:
        return c_base, d_base


def chain_reduce_shell(gi, ordering, shell_boundary_gens):
    """Chain reduction with shell corrections at boundary generators."""
    a, b = Fraction(0), Fraction(1)
    A = len(ordering)
    for j in range(gi + 1, A):
        is_boundary = gi in shell_boundary_gens or j in shell_boundary_gens
        shell_size = shell_boundary_gens.get(gi, 1) if gi in shell_boundary_gens else shell_boundary_gens.get(j, 1)

        # Base crossing
        if ordering[gi] == 1 and ordering[j] == 1:
            c, d = Fraction(1), Fraction(0)
        elif ordering[gi] == 0 and ordering[j] == 0:
            c, d = Fraction(1), -ha_rat
        else:
            c, d = Fraction(1), -ha_rat / 2

        # Shell correction: at boundary, multiply c by Chebyshev factor
        if is_boundary and shell_size > 1:
            c_cheb, d_cheb = chebyshev_coefficients(shell_size)
            # Scale the crossing: c → c × correction_factor
            # The correction is small: ln(c_cheb) adds to Φ_q
            correction = Fraction(1) + (c_cheb - 1) / Fraction(A)
            c = c * correction

        new_a = a * c * ha_rat + a * d + b * c
        new_b = a * c + b * d
        a, b = new_a, new_b
    return a, b


# ══════════════════════════════════════════════════════════════
# §3  PHI_Q WITH SHELL CORRECTIONS
# ══════════════════════════════════════════════════════════════

def gs_ordering(p, n):
    A = p + n
    if math.comb(A, p) <= 5000:
        best_e, best_o = None, None
        for pos in combinations(range(A), p):
            o = [0]*A
            for pp in pos: o[pp] = 1
            e = sum(float(z_rat * chain_reduce_bare(i, o)[0] + chain_reduce_bare(i, o)[1]) for i in range(A-1))
            if best_e is None or e < best_e: best_e, best_o = e, o
        return best_o
    else:
        o, pi, ni = [], 0, 0
        for k in range(A):
            if pi < p and (ni >= n or k%2==0): o.append(1); pi += 1
            else: o.append(0); ni += 1
        return o


def chain_reduce_bare(gi, ordering):
    a, b = Fraction(0), Fraction(1)
    for j in range(gi + 1, len(ordering)):
        if ordering[gi] == 1 and ordering[j] == 1:
            c, d = Fraction(1), Fraction(0)
        elif ordering[gi] == 0 and ordering[j] == 0:
            c, d = Fraction(1), -ha_rat
        else:
            c, d = Fraction(1), -ha_rat / 2
        a, b = a*c*ha_rat + a*d + b*c, a*c + b*d
    return a, b


def phi_q_bare(ordering):
    A = len(ordering)
    if A <= 1: return 0.0
    return sum(math.log(abs(float(z_rat*chain_reduce_bare(i,ordering)[0]+chain_reduce_bare(i,ordering)[1])))
               for i in range(A-1)
               if abs(float(z_rat*chain_reduce_bare(i,ordering)[0]+chain_reduce_bare(i,ordering)[1])) > 1e-30)


def phi_q_shell_corrected(ordering, Z, N):
    """Φ_q with shell corrections at magic number boundaries.

    The correction: at each closed shell boundary, the crossing
    coefficient gets a Chebyshev enhancement factor ln(c_{n_s}).
    This adds a NEGATIVE contribution to Φ_q (more binding at
    shell closures).
    """
    A = Z + N
    phi_bare = phi_q_bare(ordering)

    # Shell correction: for each closed shell, add the torus knot
    # contribution. The Chebyshev coefficient c_{n_s} > 1 for n_s > 1,
    # so ln(c_{n_s}) > 0. The shell correction REDUCES the mass
    # (increases binding).
    shells = get_shell_info(A)
    shell_correction = 0.0
    cumulative = 0
    for shell_size, is_closed in shells:
        if is_closed and shell_size >= 2:
            c_cheb, d_cheb = chebyshev_coefficients(shell_size)
            c_f = float(c_cheb)
            # The shell boundary adds ln(c_{n_s}) per crossing at boundary
            # Number of boundary crossings ~ shell_size
            # But the correction should be intensive (per nucleon)
            correction = math.log(c_f) * shell_size / A
            shell_correction += correction
        cumulative += shell_size

    return phi_bare - shell_correction  # subtract to increase binding


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
    ("Sc", "⁴⁵Sc",21,24, 41875.569),("Ti", "⁴⁸Ti",22,26, 44680.842),
    ("V",  "⁵¹V", 23,28, 47486.136),("Cr", "⁵²Cr",24,28, 48383.826),
    ("Mn", "⁵⁵Mn",25,30, 51189.120),("Fe", "⁵⁶Fe",26,30, 52089.806),
    ("Co", "⁵⁹Co",27,32, 54895.100),("Ni", "⁵⁸Ni",28,30, 53966.267),
    ("Cu", "⁶³Cu",29,34, 58618.364),("Zn", "⁶⁴Zn",30,34, 59549.474),
    ("Ga", "⁶⁹Ga",31,38, 64218.721),("Ge", "⁷⁴Ge",32,42, 68862.540),
    ("As", "⁷⁵As",33,42, 69793.047),("Se", "⁸⁰Se",34,46, 74436.856),
    ("Br", "⁷⁹Br",35,44, 73537.269),("Kr", "⁸⁴Kr",36,48, 78181.105),
    ("Rb", "⁸⁵Rb",37,48, 79111.400),("Sr", "⁸⁸Sr",38,50, 81886.301),
    ("Y",  "⁸⁹Y", 39,50, 82816.598),("Zr", "⁹⁰Zr",40,50, 83746.895),
]


def main():
    m_n = VOL_NEUTRON / HBAR_Q_SQ

    # Show Chebyshev coefficients
    print("=" * 100)
    print("GARSIDE NF SHELL CORRECTIONS — Chebyshev torus knot coefficients")
    print("=" * 100)
    print()
    print(f"{'n_s':>4} | {'c_n':>12} | {'d_n':>12} | {'ln(c_n)':>10} | Shell")
    print("─" * 60)
    for ns in [1, 2, 3, 6, 8, 12, 22]:
        c, d = chebyshev_coefficients(ns)
        print(f"{ns:4d} | {float(c):12.4f} | {float(d):12.4f} | {math.log(float(c)):10.4f} | "
              f"{'1s' if ns==2 else '1p' if ns==6 else '1d' if ns==12 else '2s-2d' if ns==22 else ''}")
    print()

    # Compute Φ_q with and without shell corrections for all atoms
    atoms = []
    for name, label, Z, N, M_obs in ELEMENTS:
        A = Z + N
        o = gs_ordering(Z, N) if A > 1 else [1]
        phi_bare = phi_q_bare(o)
        phi_shell = phi_q_shell_corrected(o, Z, N)
        shells = get_shell_info(A)
        atoms.append({
            'label': label, 'Z': Z, 'N': N, 'A': A, 'M_obs': M_obs,
            'phi_bare': phi_bare, 'phi_shell': phi_shell,
            'shells': shells,
        })

    # Calibrate from H, He, C — same as before, but with shell-corrected Φ
    M_H = atoms[0]['M_obs']
    M_He = atoms[1]['M_obs']
    M_C = atoms[5]['M_obs']
    lhs1 = M_He - 2 * M_H
    lhs2 = M_C - 6 * M_H

    for func_name, phi_key in [("Φ_bare (no shell)", 'phi_bare'),
                                ("Φ_shell (with shell correction)", 'phi_shell')]:
        f_he = atoms[1][phi_key]
        f_c = atoms[5][phi_key]
        denom = f_he * lhs2 - f_c * lhs1
        if abs(denom) < 1e-10:
            continue
        alpha = m_n * (6*lhs1 - 2*lhs2) / denom
        E0 = lhs1 / (2*m_n + alpha*f_he)
        mp = M_H / E0 if abs(E0) > 1e-10 else 0

        print(f"{'='*100}")
        print(f"  {func_name}")
        print(f"  α = {alpha:.6f},  E₀ = {E0:.6f} MeV,  𝔪_p = {mp:.4f}")
        print(f"{'='*100}")
        print(f"{'Atom':>5} | {'M_pred':>12} | {'M_obs':>12} | {'Δ MeV':>8} | {'Δ%':>7} | {'cal?':>4} | {'shells':>15}")
        print("─" * 85)

        pred_errors = []
        for a in atoms:
            f_val = a[phi_key]
            m_tot = a['Z'] * mp + a['N'] * m_n + alpha * f_val
            M_pred = E0 * m_tot
            delta = M_pred - a['M_obs']
            pct = delta / a['M_obs'] * 100
            cal = "*" if a['label'] in ['¹H', '⁴He', '¹²C'] else ""
            shell_str = ','.join(f"{s}{'✓' if c else ''}" for s, c in a['shells'])
            print(f"{a['label']:>5} | {M_pred:12.3f} | {a['M_obs']:12.3f} | {delta:+8.3f} | {pct:+6.2f}% | {cal:>4} | {shell_str:>15}")
            if not cal:
                pred_errors.append(abs(pct))

        mean_err = sum(pred_errors) / len(pred_errors) if pred_errors else 0
        max_err = max(pred_errors) if pred_errors else 0
        print(f"  Predictions ({len(pred_errors)} atoms): mean |Δ%| = {mean_err:.3f}%, max = {max_err:.3f}%")

    w = WitnessBuilder("atom-mass-shell-corrected", engine="python")
    w.set_description("Shell-corrected two-term mass with Chebyshev torus knot coefficients at magic numbers.")
    w.add_parameter("q", "111/100")
    w.save()


if __name__ == "__main__":
    main()
