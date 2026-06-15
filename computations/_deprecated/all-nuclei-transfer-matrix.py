#!/usr/bin/env python3
"""
All 6 nuclei: Skein polynomial from 2×2 transfer matrix chain.

Uses the CORRECT approach (beta-decay-matrix convention):
- Each nucleon pair (i,j) contributes a 2×2 transfer matrix T(c,d)
- Crossings at the SAME generator multiply as matrices
- V̂_i = z·M₁₁ + M₂₁ (Markov-traced volume per generator)
- P = ∏ V̂_i (Skein polynomial)
- Ratio P_dau/P_par gives the transition
- ln(P_dau/P_par) ≈ -Q/(E_× μ₀)

For the T_{3,5} weak vertex: append (σ_k σ_{k+1})⁵ positive crossings
at the converting generator, multiplied into the chain.

Usage:
    cd folio-assistant/computations
    python3 all-nuclei-transfer-matrix.py
"""

import json
import math
from datetime import datetime, timezone
from pathlib import Path

from q_parameter import (Q as q, Q_INV as qi, S_SKEIN as s_amp,
                         E_CROSS, TWO_Q, HBAR_Q_SQ)

# ── Parameters (Skein convention) ────────────────────────────────
HA = q - qi                        # Hecke amplitude q - q⁻¹
Z = 1.0 / (q**0.5 + q**(-0.5))

# Crossing coefficients (from Skein relation: σ⁻¹ = q²σ - qs)
def crossing_coeffs(ti, tj):
    """Returns (c, d) for a crossing between nucleon types ti, tj.
    ti, tj: 'p' or 'n'. Returns coefficients for T(c,d)."""
    if ti == 'p' and tj == 'p':
        return 1.0, 0.0
    elif ti == 'n' and tj == 'n':
        return 1.0, -HA
    else:  # mixed
        return 1.0, -HA / 2

# 2×2 matrix ops
def mat_mul(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]

def T_mat(c, d):
    return [[c*HA+d, c], [c, d]]

def traced_vol(M):
    return Z * M[0][0] + M[1][0]

def identity():
    return [[1,0],[0,1]]

# ── Compute Skein polynomial for N(p,n) ─────────────────────────

def skein_polynomial(p, n, ordering=None):
    """Compute P = ∏ V̂_i for nucleus N(p,n).

    ordering: list of 'p'/'n' for each nucleon position.
    If None, uses [p protons, then n neutrons].

    Returns (P, generator_volumes, log_P).
    """
    A = p + n
    if ordering is None:
        ordering = ['p'] * p + ['n'] * n

    volumes = []
    log_P = 0.0

    for i in range(A - 1):
        # Chain at generator σ_i: multiply T matrices for all crossings
        # Nucleon i with nucleons j > i
        M = identity()
        for j in range(i + 1, A):
            c, d = crossing_coeffs(ordering[i], ordering[j])
            T = T_mat(c, d)
            M = mat_mul(M, T)

        V = traced_vol(M)
        volumes.append(V)
        if V != 0:
            log_P += math.log(abs(V))

    P = math.exp(log_P) if abs(log_P) < 500 else float('inf')
    # Fix sign
    sign = 1
    for v in volumes:
        if v < 0:
            sign *= -1
    P *= sign

    return P, volumes, log_P


# ── All 6 nuclei ────────────────────────────────────────────────

print(f"All 6 nuclei: Skein polynomial from transfer matrix chain")
print(f"q = {q:.10f}, ha = {HA:.10f}, z = {Z:.10f}")
print(f"E_× = {E_CROSS:.6f}, μ₀ = {0.511/(3*E_CROSS):.6f} MeV")
print()

nuclei = [
    (1,   2,   "³H",    12.32,  "yr", 3.15576e7,  2,  0.01861),
    (6,   8,   "¹⁴C",   5730.0, "yr", 3.15576e7,  7,  0.15648),
    (27,  33,  "⁶⁰Co",  5.2714, "yr", 3.15576e7, 28,  0.31817),
    (38,  52,  "⁹⁰Sr",  28.79,  "yr", 3.15576e7, 39,  0.54590),
    (55,  82,  "¹³⁷Cs", 30.17,  "yr", 3.15576e7, 56,  0.51400),
    (83,  127, "²¹⁰Bi", 5.012,  "d",  86400.0,   84,  1.16270),
]

mu_0 = 0.51100 / (3 * E_CROSS)
m_e = 0.51100
G_F = 1.1664e-11
hbar = 6.582119569e-22

def q_int(n):
    return (q**n - qi**n) / (q - qi)
from hecke_core import alpha_em
from phase_space import fermi_phase_space

def phase_space(Z_d, Q_MeV, n_steps=50000):
    return fermi_phase_space(Z_d, Q_MeV, alpha_em=alpha_em, m_e_MeV=m_e, n_steps=n_steps)

print(f"{'Nuc':>6} {'A':>4} {'log P_par':>10} {'log P_dau':>10} {'ln(Pd/Pp)':>10} "
      f"{'Q_pred':>8} {'Q_exp':>8}")
print("-" * 70)

results = []
for p, n, name, t_obs, unit, conv, Z_d, Q_exp in nuclei:
    A = p + n

    P_par, vols_par, log_par = skein_polynomial(p, n)
    P_dau, vols_dau, log_dau = skein_polynomial(p + 1, n - 1)

    ln_ratio = log_dau - log_par
    Q_pred = abs(ln_ratio) * E_CROSS * mu_0

    print(f"{name:>6} {A:>4} {log_par:>10.4f} {log_dau:>10.4f} {ln_ratio:>10.6f} "
          f"{Q_pred:>8.5f} {Q_exp:>8.5f}")

    results.append({
        "name": name, "p": p, "n": n, "A": A,
        "log_P_par": log_par, "log_P_dau": log_dau,
        "ln_ratio": ln_ratio, "Q_pred": Q_pred, "Q_exp": Q_exp,
        "t_obs": t_obs, "unit": unit, "conv": conv, "Z_d": Z_d,
        "n_gen_par": len(vols_par), "n_gen_dau": len(vols_dau),
    })

# ── Half-life from Q_pred (fully from q) ────────────────────────

print()
print(f"{'='*70}")
print(f"HALF-LIVES from predicted Q-values (transfer matrix ratio)")
print(f"{'='*70}")

rate_base = G_F**2 * m_e**5 / (2 * math.pi**3 * hbar)

# The half-life formula:
# Γ = rate_base × f(Z, Q) × [2]_q × (sensitivity correction)
# |M|² is ALREADY ENCODED in the Skein polynomial ratio —
# the transfer matrix product captures the full nuclear structure.
# The ratio P_dau/P_par = exp(ln_ratio) gives BOTH |M|² and Q.
#
# Specifically: Γ ∝ |P_dau/P_par - 1|² × Q⁵ ← WRONG (|M|² approach)
# Correct: Γ ∝ f(Z, Q_pred) where Q_pred = |ln(P_dau/P_par)| × E_× × μ₀
# and the matrix element is implicitly in the Q-value prediction.
#
# The Sargent rule says Γ ∝ Q⁵ at fixed |M|².
# The transfer matrix ratio gives the COMBINED effect.
#
# For the half-life, we use:
# t_{1/2} = ln(2) / (rate_base × f(Z, Q_pred) × [2]_q)

print(f"\n  rate_base = {rate_base:.4e} s⁻¹")
print(f"  [2]_q = {TWO_Q:.6f}")
print(f"  α = {alpha_em:.6f}, 1/α = {1/alpha_em:.2f}")

print(f"\n  {'Nuc':>6} {'Q_pred':>8} {'f(Z,Q)':>10} {'t_pred':>12} {'t_obs':>10} {'ratio':>8}")
print("  " + "-" * 62)

for r in results:
    Q = r["Q_pred"]
    Z_d = r["Z_d"]
    f_val = phase_space(Z_d, Q)

    # Self-deformation
    A = r["A"]
    dq = (A-1)/A**2 * HBAR_Q_SQ
    q_corr = 1 - 48 * dq / q

    Gamma = rate_base * f_val * TWO_Q * q_corr
    if Gamma > 0:
        t_half = math.log(2) / Gamma / r["conv"]
    else:
        t_half = float('inf')

    ratio = t_half / r["t_obs"]
    r["f_val"] = f_val
    r["t_pred"] = t_half
    r["ratio"] = ratio

    print(f"  {r['name']:>6} {Q:>8.5f} {f_val:>10.4e} {t_half:>10.4f} {r['unit']:2s} "
          f"{r['t_obs']:>8.3f} {r['unit']:2s} {ratio:>8.4f}")

# ── Also with experimental Q ────────────────────────────────────

print(f"\n  With EXPERIMENTAL Q-values:")
print(f"  {'Nuc':>6} {'Q_exp':>8} {'f(Z,Q)':>10} {'t_pred':>12} {'t_obs':>10} {'ratio':>8}")
print("  " + "-" * 62)

for r in results:
    Q = r["Q_exp"]
    Z_d = r["Z_d"]
    f_val = phase_space(Z_d, Q)

    A = r["A"]
    dq = (A-1)/A**2 * HBAR_Q_SQ
    q_corr = 1 - 48 * dq / q

    Gamma = rate_base * f_val * TWO_Q * q_corr
    if Gamma > 0:
        t_half = math.log(2) / Gamma / r["conv"]
    else:
        t_half = float('inf')

    ratio = t_half / r["t_obs"]
    r["t_pred_Qexp"] = t_half
    r["ratio_Qexp"] = ratio

    print(f"  {r['name']:>6} {Q:>8.5f} {f_val:>10.4e} {t_half:>10.4f} {r['unit']:2s} "
          f"{r['t_obs']:>8.3f} {r['unit']:2s} {ratio:>8.4f}")

# ── Tritium detail: per-generator volumes ────────────────────────

print(f"\n{'='*70}")
print(f"TRITIUM DETAIL")
print(f"{'='*70}")

_, vp, _ = skein_polynomial(1, 2)
_, vd, _ = skein_polynomial(2, 1)

print(f"\n  Generator volumes:")
for i in range(2):
    r = vp[i] / vd[i] if vd[i] != 0 else float('inf')
    print(f"    σ_{i}: V̂_par = {vp[i]:.10f}, V̂_dau = {vd[i]:.10f}, "
          f"ratio = {r:.10f}, ln = {math.log(abs(r)):.10f}")

P_par = vp[0] * vp[1]
P_dau = vd[0] * vd[1]
print(f"\n  P_par = {P_par:.10f}")
print(f"  P_dau = {P_dau:.10f}")
print(f"  P_dau/P_par = {P_dau/P_par:.10f}")
print(f"  ln(P_dau/P_par) = {math.log(P_dau/P_par):.10f}")

# ── Witness ─────────────────────────────────────────────────────

witness = {
    "computation": "all-nuclei-transfer-matrix",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "description": "Skein polynomial from 2×2 transfer matrix chain for all 6 nuclei",
    "parameters": {"q": q, "HA": HA, "Z": Z, "E_cross": E_CROSS,
                    "mu_0": mu_0, "alpha_em": alpha_em},
    "results": results,
}
out = Path(__file__).parent / "all-nuclei-transfer-matrix.witness.json"
with open(out, "w") as f:
    json.dump(witness, f, indent=2)
print(f"\nWitness: {out}")
