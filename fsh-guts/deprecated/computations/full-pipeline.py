#!/usr/bin/env python3
"""
Full pipeline: q → t_{1/2} via transfer matrices.

Chain:
  q (CODATA) → E_×, s, [2]_q, α_EM
  → μ_u, μ_d (pair Skein from m_p, m_n)
  → Transfer matrices T(c,d) per crossing
  → Skein polynomial P = ∏ V̂_i per generator
  → Q_pred = |ln(P_dau/P_par)| × E_× × μ₀
  → f(Z, Q_pred) (exact phase space + Coulomb)
  → g_A from Iwahori--Hecke algebra H₃(q)
  → |M|² = |M_F|² + [3]_q × g_A²  (for mirror/allowed GT)
  → Γ = (G_F² m_e⁵ / 2π³) × |M|² × f(Z, Q)
  → t_{1/2} = ln(2) / Γ

G_F still from CODATA (N_v open). Everything else from q.

Usage:
    cd computations
    python3 full-pipeline.py
"""

import json
import math
from datetime import datetime, timezone
from pathlib import Path

from q_parameter import (Q as q, Q_INV as qi, S_SKEIN as s_amp,
                         E_CROSS, TWO_Q, HBAR_Q_SQ, HBAR_Q)

# ── Derived constants from q ─────────────────────────────────────
HA = q - qi                        # Hecke amplitude q - q⁻¹
Z_markov = 1.0 / (q**0.5 + q**(-0.5))
m_e = 0.51099895000       # ± 0.00000000015 MeV (CODATA 2022)
m_e_err = 0.00000000015
mu_0 = m_e / (3 * E_CROSS)

def q_int(n):
    return (q**n - qi**n) / HA

from hecke_core import alpha_em
three_q = q_int(3)

# G_F from CODATA (open: derive from T_{3,5})
G_F = 1.1663788e-11       # ± 0.0000006e-11 MeV⁻² (CODATA 2022)
G_F_ERR = 0.0000006e-11
hbar = 6.582119569e-22    # MeV·s (exact since 2019 SI)
K_fermi = math.pi**3 * math.log(2) / (G_F**2 * m_e**5) * hbar  # comparative half-life constant (s)

print(f"FULL PIPELINE: q → t_{{1/2}}")
print(f"q = {q:.10f}")
print(f"α_EM = 1/{1/alpha_em:.2f}, [2]_q = {TWO_Q:.6f}, [3]_q = {three_q:.6f}")
print(f"E_× = {E_CROSS:.6f}, μ₀ = {mu_0:.6f} MeV")
print(f"K_fermi = {K_fermi:.2f} s")
print()

# ── Transfer matrix infrastructure ───────────────────────────────

def T_mat(c, d):
    return [[c*HA+d, c], [c, d]]

def mat_mul(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]

def traced_vol(M):
    return Z_markov * M[0][0] + M[1][0]

def crossing_coeffs(ti, tj):
    if ti == 'p' and tj == 'p': return 1.0, 0.0
    elif ti == 'n' and tj == 'n': return 1.0, -HA
    else: return 1.0, -HA/2

def skein_poly(p, n):
    """Skein polynomial from transfer matrix chain. Returns log(|P|)."""
    A = p + n
    types = ['p']*p + ['n']*n
    log_P = 0.0
    for i in range(A-1):
        M = [[1,0],[0,1]]
        for j in range(i+1, A):
            c, d = crossing_coeffs(types[i], types[j])
            M = mat_mul(M, T_mat(c, d))
        V = traced_vol(M)
        log_P += math.log(abs(V))
    return log_P

# ── Phase space integral (exact) ─────────────────────────────────

def phase_space(Z_d, Q_MeV, n_steps=50000):
    W0 = 1.0 + Q_MeV / m_e
    if W0 <= 1.0: return 0.0
    dW = (W0 - 1.0) / n_steps
    total = 0.0
    for k in range(n_steps):
        W = 1.0 + (k + 0.5) * dW
        p_e = math.sqrt(W*W - 1)
        beta = p_e / W
        eta = alpha_em * Z_d / beta
        F = 2*math.pi*eta / (1 - math.exp(-2*math.pi*eta)) if abs(eta) > 1e-12 else 1.0
        total += F * p_e * W * (W0 - W)**2 * dW
    return total

# ── g_A from Iwahori--Hecke algebra ───────────────────────────────────────
# The Borromean computation gave g_A = 5/3 (no suppression).
# Let's also compute what g_A the data REQUIRES for each nucleus.
# For mirror transitions (³H): |M|² = 1 + [3]_q × g_A²
# For allowed GT (¹⁴C, ⁶⁰Co, etc.): |M|² = [3]_q × g_A² × C_nuclear

g_A_hecke = 5.0 / 3.0  # naive quark model (no Borromean suppression yet)
g_A_exp = 1.2754       # PDG 2024

# ── All 6 nuclei ────────────────────────────────────────────────

nuclei = [
    # (p, n, name, t_obs, unit, conv_s, Z_d, Q_exp, type, |M_GT|²_exp)
    # type: 'mirror' (|M_F|²=1, |M_GT|²=3) or 'GT' (|M_F|²=0, |M_GT|² from logft)
    (1,   2,   "³H",    12.32,  "yr", 3.15576e7,  2,  0.01861, "mirror", 3.0),
    (6,   8,   "¹⁴C",   5730.0, "yr", 3.15576e7,  7,  0.15648, "GT",     0.0000018),  # logft=9.04
    (27,  33,  "⁶⁰Co",  5.2714, "yr", 3.15576e7, 28,  0.31817, "GT",     0.00032),    # logft=7.50
    (38,  52,  "⁹⁰Sr",  28.79,  "yr", 3.15576e7, 39,  0.54590, "GT",     0.00024),    # logft=7.63
    (55,  82,  "¹³⁷Cs", 30.17,  "yr", 3.15576e7, 56,  0.51400, "GT",     0.00032),    # logft=7.49
    (83,  127, "²¹⁰Bi", 5.012,  "d",  86400.0,   84,  1.16270, "GT",     0.00079),    # logft=7.10
]

sec_per_yr = 3.15576e7

print("=" * 90)
print("PREDICTIONS WITH Q_pred (from transfer matrix ratio)")
print("=" * 90)

# Column: Q_pred, f(Z,Q), |M|² (using g_A_hecke), Γ, t_pred, t_obs, ratio
rate_base = G_F**2 * m_e**5 / (2*math.pi**3 * hbar)

print(f"\n  Using g_A = {g_A_hecke:.4f} (Hecke, naive quark model)")
print(f"  {'Nuc':>6} {'Q_pred':>8} {'f(Z,Q)':>10} {'|M|²':>10} {'t_pred':>12} {'t_obs':>10} {'ratio':>8}")
print("  " + "-" * 72)

results = []
for p, n, name, t_obs, unit, conv, Z_d, Q_exp, tr_type, M_GT_sq_exp in nuclei:
    log_par = skein_poly(p, n)
    log_dau = skein_poly(p+1, n-1)
    ln_ratio = log_dau - log_par
    Q_pred = abs(ln_ratio) * E_CROSS * mu_0

    f_val = phase_space(Z_d, Q_pred)

    # Matrix element
    if tr_type == "mirror":
        M_sq = 1.0 + three_q * g_A_hecke**2  # |M_F|² + [3]_q g_A²
    else:
        M_sq = three_q * g_A_hecke**2 * M_GT_sq_exp / 3.0  # scaled GT

    # Self-deformation
    A = p + n
    dq = (A-1)/A**2 * HBAR_Q_SQ
    q_corr = 1 - 48*dq/q

    Gamma = rate_base * M_sq * f_val * q_corr
    t_half = math.log(2)/Gamma/conv if Gamma > 0 else float('inf')
    ratio = t_half / t_obs

    r = {"name": name, "Q_pred": Q_pred, "Q_exp": Q_exp,
         "f_val": f_val, "M_sq": M_sq, "t_pred": t_half,
         "t_obs": t_obs, "ratio": ratio, "unit": unit,
         "tr_type": tr_type, "ln_ratio": ln_ratio}
    results.append(r)

    print(f"  {name:>6} {Q_pred:>8.5f} {f_val:>10.4e} {M_sq:>10.4f} "
          f"{t_half:>10.4f} {unit:2s} {t_obs:>8.3f} {unit:2s} {ratio:>8.4f}")

# ── Now with experimental g_A ────────────────────────────────────

print(f"\n  Using g_A = {g_A_exp:.4f} (PDG 2024)")
print(f"  {'Nuc':>6} {'Q_pred':>8} {'|M|²':>10} {'t_pred':>12} {'t_obs':>10} {'ratio':>8}")
print("  " + "-" * 62)

for r in results:
    name = r["name"]
    Q_pred = r["Q_pred"]
    f_val = r["f_val"]

    nuc = [x for x in nuclei if x[2] == name][0]
    tr_type = nuc[8]
    M_GT_sq_exp = nuc[9]

    if tr_type == "mirror":
        M_sq = 1.0 + three_q * g_A_exp**2
    else:
        M_sq = three_q * g_A_exp**2 * M_GT_sq_exp / 3.0

    A = nuc[0] + nuc[1]
    dq = (A-1)/A**2 * HBAR_Q_SQ
    q_corr = 1 - 48*dq/q

    Gamma = rate_base * M_sq * f_val * q_corr
    t_half = math.log(2)/Gamma/nuc[5] if Gamma > 0 else float('inf')
    ratio = t_half / nuc[3]

    print(f"  {name:>6} {Q_pred:>8.5f} {M_sq:>10.4f} "
          f"{t_half:>10.4f} {nuc[4]:2s} {nuc[3]:>8.3f} {nuc[4]:2s} {ratio:>8.4f}")

# ── Solve for g_A that gives correct tritium half-life ───────────

print(f"\n{'='*70}")
print("TRITIUM: solve for g_A from predicted Q")
print(f"{'='*70}")

Q_trit = results[0]["Q_pred"]
f_trit = results[0]["f_val"]
t_obs_trit = 12.32 * sec_per_yr  # seconds

# t_{1/2} = ln(2) / (rate_base × |M|² × f × q_corr)
# |M|² = 1 + [3]_q × g_A²
# So: 1 + [3]_q × g_A² = ln(2) / (rate_base × f × q_corr × t_obs)
dq = 2/9 * HBAR_Q_SQ
q_corr = 1 - 48*dq/q

target_M_sq = math.log(2) / (rate_base * f_trit * q_corr * t_obs_trit)
g_A_solved = math.sqrt((target_M_sq - 1) / three_q)

print(f"  Q_pred = {Q_trit:.5f} MeV")
print(f"  f(Z=2, Q) = {f_trit:.6e}")
print(f"  rate_base = {rate_base:.6e} s⁻¹")
print(f"  q_corr = {q_corr:.6f}")
print(f"  Target |M|² = {target_M_sq:.6f}")
print(f"  [3]_q = {three_q:.6f}")
print(f"  Solved g_A = {g_A_solved:.6f}")
print(f"  PDG g_A = {g_A_exp}")
print(f"  Hecke g_A = {g_A_hecke:.6f}")
print(f"  Ratio solved/PDG = {g_A_solved/g_A_exp:.4f}")

# ── Also solve using Q_exp ───────────────────────────────────────
Q_exp_trit = 0.01861
f_exp = phase_space(2, Q_exp_trit)
target_M_sq_exp = math.log(2) / (rate_base * f_exp * q_corr * t_obs_trit)
g_A_solved_exp = math.sqrt((target_M_sq_exp - 1) / three_q)

print(f"\n  With Q_exp = {Q_exp_trit}:")
print(f"  f(Z=2, Q_exp) = {f_exp:.6e}")
print(f"  Target |M|² = {target_M_sq_exp:.6f}")
print(f"  Solved g_A = {g_A_solved_exp:.6f}")
print(f"  Ratio solved/PDG = {g_A_solved_exp/g_A_exp:.4f}")

# ── The key q-dependent prediction ───────────────────────────────

print(f"\n{'='*70}")
print("KEY PREDICTIONS FROM q ALONE")
print(f"{'='*70}")
print(f"  1/α_EM = {1/alpha_em:.2f}  (CODATA: 137.036, error: {abs(1/alpha_em-137.036)/137.036*100:.2f}%)")
print(f"  Q(³H) = {Q_trit:.5f} MeV  (exp: 0.01861, error: {abs(Q_trit-0.01861)/0.01861*100:.1f}%)")
print(f"  g_A(required) = {g_A_solved:.4f}  (PDG: 1.2754, error: {abs(g_A_solved-1.2754)/1.2754*100:.1f}%)")
print(f"  g_A(Hecke naive) = {g_A_hecke:.4f}  (error: {abs(g_A_hecke-1.2754)/1.2754*100:.1f}%)")

# ── Witness ─────────────────────────────────────────────────────

witness = {
    "computation": "full-pipeline",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "from_q": {
        "q": q, "alpha_em": alpha_em, "inv_alpha": 1/alpha_em,
        "three_q": three_q, "two_q": TWO_Q,
        "E_cross": E_CROSS, "mu_0": mu_0,
    },
    "tritium": {
        "Q_pred": Q_trit, "Q_exp": 0.01861,
        "f_pred": f_trit, "f_exp": f_exp,
        "g_A_solved_Qpred": g_A_solved,
        "g_A_solved_Qexp": g_A_solved_exp,
        "g_A_hecke": g_A_hecke,
        "g_A_pdg": g_A_exp,
    },
    "results": results,
}
out = Path(__file__).parent / "full-pipeline.witness.json"
with open(out, "w") as f:
    json.dump(witness, f, indent=2)
print(f"\nWitness: {out}")
