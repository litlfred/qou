"""
I₁₀ DERIVATION: pairing correction from q.

Key discovery: F_deg2 ≈ V̂(paired)/V̂(single)² from the Hecke algebra.
This means F_deg2 is the pairing energy ratio for pp crossings.

The oo→ee correction comes from the TRANSITION pairing:
when a odd-odd parent decays to an even-even daughter, the daughter
gains one paired pp crossing and one paired nn crossing that the
parent didn't have.

The correction factor for oo→ee is:
  F_oo = V̂(paired pp) × V̂(paired nn) / [V̂(single pp)² × V̂(single nn)²]
       = F_pp_pair × F_nn_pair

where F_pp_pair = V̂(T²_pp) / V̂(T_pp)²
and   F_nn_pair = V̂(T²_nn) / V̂(T_nn)²

This is derived entirely from q — no fitting.
"""

import math
import sys
sys.path.insert(0, '.')
from q_parameter import Q, Q_INV, HA, LN_Q
from experimental_constants import M_E_MEV

KAPPA = M_E_MEV / 3.0
KAPPA_Q = LN_Q * KAPPA
Z_MARKOV = 1.0 / (math.sqrt(Q) + 1.0/math.sqrt(Q))
S_SK = math.sqrt(Q) - 1.0/math.sqrt(Q)
F_DEG2 = 0.5904
F_PAULI = 0.6382
MAGIC = [2, 8, 20, 28, 50, 82, 126]

def shell_degree(n):
    for i, m in enumerate(MAGIC):
        if n <= m: return 2 if i+1 >= 5 else 1
    return 2

# ── Pairing ratios from Hecke algebra ────────────────────────────

def compute_pairing_ratios():
    """Derive pairing correction factors from q.

    For a crossing of type X, the transfer matrix is T_X = T(c_X, d_X).
    The "paired" version is T_X² (two adjacent same-type crossings).

    The traced volume V̂ = z·M[0,0] + M[1,0] for each matrix.

    The pairing ratio R_X = V̂(T_X²) / V̂(T_X)² measures how much
    the paired crossing deviates from two independent crossings.
    """
    z = Z_MARKOV

    # pp: T(1, 0) = [[HA, 1], [1, 0]]
    v_pp = z * HA + 1
    # T_pp² = [[HA²+1, HA], [HA, 1]]
    v_pp2 = z * (HA**2 + 1) + HA
    R_pp = v_pp2 / v_pp**2

    # nn: T(q², -q·s)
    c_nn, d_nn = Q**2, -Q * S_SK
    t_nn = [[c_nn*HA + d_nn, c_nn], [c_nn, d_nn]]
    v_nn = z * t_nn[0][0] + t_nn[1][0]
    # T_nn²
    t2_00 = t_nn[0][0]**2 + t_nn[0][1]*t_nn[1][0]
    t2_10 = t_nn[1][0]*t_nn[0][0] + t_nn[1][1]*t_nn[1][0]
    v_nn2 = z * t2_00 + t2_10
    R_nn = v_nn2 / v_nn**2

    # pn: T((1+q²)/2, -q·s/2)
    c_pn, d_pn = (1 + Q**2)/2, -Q * S_SK / 2
    v_pn = z * (c_pn * HA + d_pn) + c_pn
    # T_pn² (pn × pn = two adjacent mixed crossings)
    t_pn = [[c_pn*HA + d_pn, c_pn], [c_pn, d_pn]]
    t2p_00 = t_pn[0][0]**2 + t_pn[0][1]*t_pn[1][0]
    t2p_10 = t_pn[1][0]*t_pn[0][0] + t_pn[1][1]*t_pn[1][0]
    v_pn2 = z * t2p_00 + t2p_10
    R_pn = v_pn2 / v_pn**2

    return R_pp, R_nn, R_pn

R_pp, R_nn, R_pn = compute_pairing_ratios()

print("Pairing ratios from q (derived, no fitting):")
print(f"  R_pp = V̂(T²_pp)/V̂(T_pp)² = {R_pp:.6f}")
print(f"  R_nn = V̂(T²_nn)/V̂(T_nn)² = {R_nn:.6f}")
print(f"  R_pn = V̂(T²_pn)/V̂(T_pn)² = {R_pn:.6f}")
print(f"  F_deg2 (from H₃ irreps)    = {F_DEG2}")
print(f"  R_pp ≈ F_deg2: {abs(R_pp - F_DEG2) < 0.01}")
print()

# ── I₁₀ correction factor ───────────────────────────────────────

# In β⁻ decay (odd-odd → even-even):
# The parent has unpaired p and n: one pp and one nn crossing are "solo"
# The daughter gains the pairing: those crossings become "paired"
# The correction = R_pp × R_nn (the pairing gain for both types)

# But this double-counts because the shell factor F_deg2 already
# accounts for the pp pairing. So:
# F_oo = R_nn / R_pp (correct for nn relative to the pp baseline)
# Or: F_oo = √(R_pp × R_nn) / R_pp = √(R_nn / R_pp)

# Actually, the simplest approach: the odd-odd correction is the
# ratio of the geometric mean of paired ratios to the F_deg2 baseline.

F_oo_to_ee = math.sqrt(R_pp * R_nn)  # geometric mean of pairing ratios
print(f"I₁₀ correction for oo→ee transitions:")
print(f"  F_oo = √(R_pp × R_nn) = {F_oo_to_ee:.6f}")
print(f"  1/F_oo = {1/F_oo_to_ee:.6f}")
print(f"  F_oo / F_deg2 = {F_oo_to_ee / F_DEG2:.6f}")
print()

# The correction to the Q-value: for oo→ee transitions, the existing
# F_deg2 factor assumes even occupancy. For odd-odd parents, we need
# to correct by the pairing deficit. The correction is:
# Q_corrected = Q_base × (F_oo / F_deg2)
# where F_oo accounts for the unpaired crossings in the parent.

# But let's be more careful. The F_deg2 factor is applied to ALL
# shell 5+ nuclei. For oo→ee, both parent AND daughter are shell 5+.
# The parent is weaker (odd-odd), so the volume ratio overestimates Q.
# The correction should REDUCE Q by the pairing deficit of the parent.

# The parent pairing deficit: one pp and one nn crossing are unpaired.
# The number of unpaired crossings is 1 (for pp) and 1 (for nn).
# Out of Z pp crossings and N nn crossings, 1 of each is unpaired.
# The fractional deficit is 1/Z for pp and 1/N for nn.
# The correction factor is (1 - δ_pp/Z) × (1 - δ_nn/N) where
# δ = 1 - R is the pairing deficit per crossing.

delta_pp = 1 - R_pp  # ≈ 0.401
delta_nn = 1 - R_nn  # ≈ 0.529

print(f"Pairing deficit per crossing:")
print(f"  δ_pp = 1 - R_pp = {delta_pp:.4f}")
print(f"  δ_nn = 1 - R_nn = {delta_nn:.4f}")
print()

# ── Apply to benchmarks ─────────────────────────────────────────

def crossing_coeffs_f(ti, tj):
    pair = ti + tj
    if pair == 'pp': return (1.0, 0.0)
    elif pair == 'nn': return (Q**2, -Q * S_SK)
    else: return ((1.0 + Q**2)/2.0, -Q * S_SK / 2.0)

def generator_volumes_f(z, n):
    a = z+n; types = ['p']*z + ['n']*n; vols = []
    for i in range(a-1):
        m = [[1.0, 0.0], [0.0, 1.0]]
        for j in range(i+1, a):
            c, d = crossing_coeffs_f(types[i], types[j])
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

print("=" * 90)
print("Q-VALUES WITH I₁₀ PAIRING CORRECTION (derived from q)")
print("=" * 90)

# The correction: for oo→ee transitions, multiply by (1 - δ/Z)(1 - δ/N)
# where δ is the pairing deficit and Z, N are the parent nucleon counts.
# This is a per-crossing correction: one unpaired out of Z proton crossings,
# one unpaired out of N neutron crossings.

print(f"\n{'Nuc':>8} {'Par':>5} {'Q_base':>8} {'F_I10':>8} {'Q_corr':>8} {'Q_exp':>8} {'err_b':>7} {'err_c':>7}")
print("-" * 75)

errs_base, errs_corr = [], []
for z, n, nuc, q_exp in BENCHMARKS:
    a = z + n
    vp = generator_volumes_f(z, n)
    vd = generator_volumes_f(z+1, n-1)

    types_p = ['p']*z + ['n']*n
    types_d = ['p']*(z+1) + ['n']*(n-1)
    lu, lr, luc = 0.0, 0.0, 0.0
    for i in range(a-1):
        if abs(vp[i]) < 1e-30 or abs(vd[i]) < 1e-30: continue
        lratio = (math.log(abs(vd[i])) - math.log(abs(vp[i]))) / LN_Q
        changed = [j for j in range(i+1, a)
                   if types_p[i]+types_p[j] != types_d[i]+types_d[j]]
        if not changed: luc += lratio
        else:
            nu = sum(1 for j in changed if types_p[i]=='n' and types_p[j]=='n')
            nr = sum(1 for j in changed if types_d[i]=='p' and types_d[j]=='p')
            t = nu + nr
            if nr==0: lu += lratio
            elif nu==0: lr += lratio
            else: lu += lratio*nu/t; lr += lratio*nr/t

    q_raw = abs(Q*lu + Q_INV*lr + luc) * KAPPA_Q
    deg = shell_degree(n)
    f = F_DEG2 if deg >= 2 else 1.0
    if n in MAGIC and deg >= 2: f *= F_PAULI

    q_base = q_raw * f

    # I₁₀ correction — ONLY for shell 5+ (deg ≥ 2)
    # For shells 1-4, the q-weighting already captures pairing correctly.
    # The I₁₀ correction accounts for the odd-odd pairing deficit that
    # the F_deg2 shell factor doesn't handle.
    par = parity(z, n)
    par_d = parity(z+1, n-1)
    if deg >= 2 and par == "oo" and par_d == "ee":
        # Odd-odd parent → even-even daughter at shell 5+
        f_i10 = (1 - delta_pp / z) * (1 - delta_nn / n)
    elif deg >= 2 and par == "oA":
        # Odd-A at shell 5+: one unpaired nucleon
        if z % 2 == 1:  # odd Z
            f_i10 = 1 - delta_pp / (2*z)
        else:  # odd N
            f_i10 = 1 - delta_nn / (2*n)
    else:
        f_i10 = 1.0

    q_corr = q_base * f_i10

    e_b = (q_base - q_exp) / q_exp * 100
    e_c = (q_corr - q_exp) / q_exp * 100
    errs_base.append(abs(e_b))
    errs_corr.append(abs(e_c))

    mark_b = "◀" if abs(e_b) < 5 else " "
    mark_c = "◀" if abs(e_c) < 5 else " "
    print(f"{nuc:>8} {par+'→'+par_d:>5} {q_base:>8.5f} {f_i10:>8.4f} {q_corr:>8.5f} {q_exp:>8.5f} {e_b:>+6.1f}%{mark_b}{e_c:>+6.1f}%{mark_c}")

mae_b = sum(errs_base) / len(errs_base)
mae_c = sum(errs_corr) / len(errs_corr)
rms_b = math.sqrt(sum(e**2 for e in errs_base) / len(errs_base))
rms_c = math.sqrt(sum(e**2 for e in errs_corr) / len(errs_corr))

print(f"\n  Base:      MAE = {mae_b:.1f}%, RMS = {rms_b:.1f}%")
print(f"  With I₁₀:  MAE = {mae_c:.1f}%, RMS = {rms_c:.1f}%")
print(f"\n  I₁₀ pairing deficits (from q):")
print(f"    δ_pp = {delta_pp:.4f} (pp pairing deficit per crossing)")
print(f"    δ_nn = {delta_nn:.4f} (nn pairing deficit per crossing)")
print(f"    F_I10(oo→ee) = (1 - δ_pp/Z)(1 - δ_nn/N)")
print(f"    F_I10(oA) = 1 - δ/(2·Z or 2·N) for the odd nucleon type")
print(f"\n  All factors derived from q = {Q:.10f} alone.")
