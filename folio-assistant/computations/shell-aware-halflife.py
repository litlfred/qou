#!/usr/bin/env python3
"""
Shell-aware half-lives: transfer matrix with sequential filling order.

The sequential builder (Hopf link + reduce) revealed that filling
order matters: alternating p-n with shell closures gives different
Skein polynomials than naive [p...n...] ordering.

This script uses the TRANSFER MATRIX (2×2 chain, O(A²)) with
the shell-aware ordering from the sequential builder. Scalable
to any A.

For each nucleus AND its daughter, compute P(q) = ∏ V̂_i,
then Q_pred = |ln(P_dau/P_par)| × E_× × μ₀.

Usage:
    python3 shell-aware-halflife.py
"""

import json
import math
import time
from datetime import datetime, timezone
from pathlib import Path

from q_parameter import Q as q, Q_INV as qi, E_CROSS
from experimental_constants import (
    M_E_MEV, G_F_MEV, G_F_MEV_ERR, HBAR_MEV_S, ALPHA_EM_INV,
    Q_TRITIUM_MEV, Q_TRITIUM_MEV_ERR, HALFLIFE_TRITIUM_YR, HALFLIFE_TRITIUM_YR_ERR,
    Q_C14_MEV, Q_C14_MEV_ERR, HALFLIFE_C14_YR, HALFLIFE_C14_YR_ERR,
    Q_CO60_MEV, Q_CO60_MEV_ERR, HALFLIFE_CO60_YR, HALFLIFE_CO60_YR_ERR,
    Q_SR90_MEV, Q_SR90_MEV_ERR, HALFLIFE_SR90_YR, HALFLIFE_SR90_YR_ERR,
    Q_CS137_MEV, Q_CS137_MEV_ERR, HALFLIFE_CS137_YR, HALFLIFE_CS137_YR_ERR,
    Q_BI210_MEV, Q_BI210_MEV_ERR, HALFLIFE_BI210_D, HALFLIFE_BI210_D_ERR,
    SEC_PER_YR, SEC_PER_DAY,
    G_A_PDG, G_A_PDG_ERR,
)

# ── Parameters ──────────────────────────────────────────────────
HA = q - qi
Z_m = 1.0 / (q**0.5 + q**(-0.5))
mu_0 = M_E_MEV / (3 * E_CROSS)

def q_int(n):
    return (q**n - qi**n) / HA

from hecke_core import alpha_em
two_q = q_int(2)

print(f"Shell-aware half-lives")
print(f"q = {q:.10f}, [2]_q = {two_q:.6f}, 1/α = {1/alpha_em:.2f}")
print()

# ── 2×2 transfer matrix ────────────────────────────────────────

def T_mat(c, d):
    return [[c*HA+d, c], [c, d]]

def mat_mul(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]

def traced_vol(M):
    return Z_m * M[0][0] + M[1][0]

def crossing_coeffs(ti, tj):
    if ti == 'p' and tj == 'p': return 1.0, 0.0
    elif ti == 'n' and tj == 'n': return 1.0, -HA
    else: return 1.0, -HA/2

# ── Shell-aware ordering ───────────────────────────────────────

def shell_filling_order(p, n):
    """Generate nucleon ordering by alternating p-n filling.

    This is the ordering used by the sequential builder that
    revealed the shell structure. Matches the interleaved
    Hopf-link construction.
    """
    A = p + n
    seq = []
    pi, ni = 0, 0
    for k in range(A):
        if pi < p and (ni >= n or k % 2 == 0):
            seq.append('p')
            pi += 1
        else:
            seq.append('n')
            ni += 1
    return seq

def naive_ordering(p, n):
    """Naive ordering: all protons first, then all neutrons."""
    return ['p'] * p + ['n'] * n

# ── Skein polynomial from ordering ─────────────────────────────

def log_skein_poly(ordering):
    """Compute log|P| = Σ log|V̂_i| from the ordering.

    Each generator σ_i has crossings with all j > i.
    Transfer matrix chain gives V̂_i = z·M₁₁ + M₂₁.
    """
    A = len(ordering)
    log_P = 0.0
    sign = 1

    for i in range(A - 1):
        M = [[1,0],[0,1]]
        for j in range(i + 1, A):
            c, d = crossing_coeffs(ordering[i], ordering[j])
            T = T_mat(c, d)
            M = mat_mul(M, T)
        V = traced_vol(M)
        if V < 0:
            sign *= -1
        if abs(V) > 0:
            log_P += math.log(abs(V))
        else:
            return float('-inf'), 0

    return log_P, sign

# ── Phase space integral ───────────────────────────────────────

def phase_space(Z_d, Q_MeV, n_steps=50000):
    W0 = 1.0 + Q_MeV / M_E_MEV
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

# ── All 6 nuclei ────────────────────────────────────────────────

nuclei = [
    (1,   2,   "³H",    HALFLIFE_TRITIUM_YR, HALFLIFE_TRITIUM_YR_ERR, "yr", SEC_PER_YR,  2, Q_TRITIUM_MEV, Q_TRITIUM_MEV_ERR, "mirror"),
    (6,   8,   "¹⁴C",   HALFLIFE_C14_YR, HALFLIFE_C14_YR_ERR, "yr", SEC_PER_YR,  7, Q_C14_MEV, Q_C14_MEV_ERR, "GT"),
    (27,  33,  "⁶⁰Co",  HALFLIFE_CO60_YR, HALFLIFE_CO60_YR_ERR, "yr", SEC_PER_YR, 28, Q_CO60_MEV, Q_CO60_MEV_ERR, "GT"),
    (38,  52,  "⁹⁰Sr",  HALFLIFE_SR90_YR, HALFLIFE_SR90_YR_ERR, "yr", SEC_PER_YR, 39, Q_SR90_MEV, Q_SR90_MEV_ERR, "GT"),
    (55,  82,  "¹³⁷Cs", HALFLIFE_CS137_YR, HALFLIFE_CS137_YR_ERR, "yr", SEC_PER_YR, 56, Q_CS137_MEV, Q_CS137_MEV_ERR, "GT"),
    (83,  127, "²¹⁰Bi", HALFLIFE_BI210_D, HALFLIFE_BI210_D_ERR, "d", SEC_PER_DAY, 84, Q_BI210_MEV, Q_BI210_MEV_ERR, "GT"),
]

rate_base = G_F_MEV**2 * M_E_MEV**5 / (2 * math.pi**3 * HBAR_MEV_S)

# ── Compare naive vs shell-aware orderings ──────────────────────

print("=" * 90)
print("Q-VALUES: NAIVE vs SHELL-AWARE ORDERING")
print("=" * 90)

print(f"\n  {'Nuc':>6} {'Q_naive':>10} {'Q_shell':>10} {'Q_exp±δ':>14} {'err_naive':>10} {'err_shell':>10}")
print("  " + "-" * 68)

results = []
for p, n, name, t_obs, t_err, unit, conv, Z_d, Q_exp, Q_err, tr_type in nuclei:
    t0 = time.time()

    # Naive ordering
    ord_naive = naive_ordering(p, n)
    ord_naive_dau = naive_ordering(p + 1, n - 1)
    lp_par_n, sp_n = log_skein_poly(ord_naive)
    lp_dau_n, sd_n = log_skein_poly(ord_naive_dau)
    ln_ratio_naive = lp_dau_n - lp_par_n
    Q_naive = abs(ln_ratio_naive) * E_CROSS * mu_0

    # Shell-aware ordering
    ord_shell = shell_filling_order(p, n)
    ord_shell_dau = shell_filling_order(p + 1, n - 1)
    lp_par_s, sp_s = log_skein_poly(ord_shell)
    lp_dau_s, sd_s = log_skein_poly(ord_shell_dau)
    ln_ratio_shell = lp_dau_s - lp_par_s
    Q_shell = abs(ln_ratio_shell) * E_CROSS * mu_0

    elapsed = time.time() - t0

    err_naive = (Q_naive - Q_exp) / Q_exp * 100
    err_shell = (Q_shell - Q_exp) / Q_exp * 100

    print(f"  {name:>6} {Q_naive:>10.5f} {Q_shell:>10.5f} "
          f"{Q_exp:>8.5f}±{Q_err:.0e} {err_naive:>+9.1f}% {err_shell:>+9.1f}% "
          f"({elapsed:.2f}s)")

    results.append({
        "name": name, "p": p, "n": n, "A": p + n,
        "Q_naive": Q_naive, "Q_shell": Q_shell,
        "Q_exp": Q_exp, "Q_err": Q_err,
        "err_naive_pct": err_naive, "err_shell_pct": err_shell,
        "ln_ratio_naive": ln_ratio_naive, "ln_ratio_shell": ln_ratio_shell,
        "t_obs": t_obs, "t_err": t_err, "unit": unit, "conv": conv,
        "Z_d": Z_d, "tr_type": tr_type,
    })

# ── Half-lives from shell-aware Q ───────────────────────────────

print(f"\n{'='*90}")
print(f"HALF-LIVES: shell-aware Q + experimental g_A + exact phase space")
print(f"{'='*90}")

print(f"\n  rate_base = {rate_base:.6e} s⁻¹")
print(f"  g_A = {G_A_PDG} ± {G_A_PDG_ERR} (PDG 2024)")

print(f"\n  {'Nuc':>6} {'Q_shell':>8} {'f(Z,Q)':>10} {'|M|²':>8} {'t_pred':>12} {'t_obs±δ':>16} {'ratio':>8}")
print("  " + "-" * 78)

for r in results:
    Q = r["Q_shell"]
    Z_d = r["Z_d"]
    f_val = phase_space(Z_d, Q)

    # Matrix element: mirror → |M|² = 1 + 3g_A², GT → use logft
    if r["tr_type"] == "mirror":
        M_sq = 1.0 + 3 * G_A_PDG**2
    else:
        # For GT transitions, use logft from NNDC to get |M|²
        # ft = K / (g_A² |M_GT|²), K = 6147 s
        K_fermi = 2 * math.pi**3 * math.log(2) * HBAR_MEV_S / (G_F_MEV**2 * M_E_MEV**5)
        # Use experimental ft to extract |M_GT|² (not from q — open computation)
        f_exp = phase_space(Z_d, r["Q_exp"])
        ft_exp = r["t_obs"] * r["conv"] * f_exp
        M_sq = K_fermi / ft_exp if ft_exp > 0 else 1.0

    # Self-deformation
    A = r["A"]
    from q_parameter import HBAR_Q_SQ
    dq = (A-1)/A**2 * HBAR_Q_SQ
    q_corr = 1 - 48*dq/q

    Gamma = rate_base * M_sq * f_val * q_corr
    t_half = math.log(2) / Gamma / r["conv"] if Gamma > 0 else float('inf')
    ratio = t_half / r["t_obs"]

    r["M_sq"] = M_sq
    r["f_val"] = f_val
    r["t_pred"] = t_half
    r["ratio"] = ratio

    print(f"  {r['name']:>6} {Q:>8.5f} {f_val:>10.4e} {M_sq:>8.4f} "
          f"{t_half:>10.4f} {r['unit']:2s} "
          f"{r['t_obs']:>8.3f}±{r['t_err']:.0e} {r['unit']:2s} {ratio:>8.4f}")

# ── Also with experimental Q ────────────────────────────────────

print(f"\n  With EXPERIMENTAL Q (isolate ordering effect on Q only):")
print(f"  {'Nuc':>6} {'Q_exp':>8} {'t_pred':>12} {'t_obs±δ':>16} {'ratio':>8}")
print("  " + "-" * 56)

for r in results:
    Q = r["Q_exp"]
    Z_d = r["Z_d"]
    f_val = phase_space(Z_d, Q)
    M_sq = r["M_sq"]

    A = r["A"]
    dq = (A-1)/A**2 * HBAR_Q_SQ
    q_corr = 1 - 48*dq/q

    Gamma = rate_base * M_sq * f_val * q_corr
    t_half = math.log(2) / Gamma / r["conv"] if Gamma > 0 else float('inf')
    ratio = t_half / r["t_obs"]

    r["t_pred_Qexp"] = t_half
    r["ratio_Qexp"] = ratio

    print(f"  {r['name']:>6} {Q:>8.5f} {t_half:>10.4f} {r['unit']:2s} "
          f"{r['t_obs']:>8.3f}±{r['t_err']:.0e} {r['unit']:2s} {ratio:>8.4f}")

# ── Witness ─────────────────────────────────────────────────────

witness = {
    "computation": "shell-aware-halflife",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "parameters": {"q": q, "alpha_em": alpha_em, "mu_0": mu_0,
                    "G_F": G_F_MEV, "g_A": G_A_PDG},
    "results": results,
}
out = Path(__file__).parent / "shell-aware-halflife.witness.json"
with open(out, "w") as f:
    json.dump(witness, f, indent=2)
print(f"\nWitness: {out}")
