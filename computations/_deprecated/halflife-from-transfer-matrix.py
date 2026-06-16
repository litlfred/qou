#!/usr/bin/env python3
"""
Half-lives from transfer matrix Skein polynomial ratios.

The transfer matrix P_dau/P_par encodes the Q-value:
  ln(P_dau/P_par) ≈ -Q/(E_× μ₀)

Verified for tritium: ln = -0.102, -Q/(E_× μ₀) = -0.109.

The decay rate formula (exact phase space integral, not Sargent Q⁵):
  Γ = (G_F² m_e⁵ / 2π³) × |M_q|² × f(Z, Q)

where:
  |M_q|² = ∏ |V̂_par/V̂_dau|²  (product of generator volume ratios)
  f(Z, Q) = ∫₁^{W₀} F(Z,W) √(W²-1) W (W₀-W)² dW  (exact phase space)
  F(Z, W) = 2πη / (1 - e^{-2πη})  (Coulomb enhancement)
  Q = -ln(P_dau/P_par) × E_× × μ₀  (from transfer matrix)

All from q + μ₀ + G_F (G_F open: to be derived from T_{3,5}).

Usage:
    cd computations
    python3 halflife-from-transfer-matrix.py
"""

import json
import math
from datetime import datetime, timezone
from pathlib import Path

from q_parameter import (Q as q, Q_INV as qi, S_SKEIN as s,
                         E_CROSS, TWO_Q, HBAR_Q, HBAR_Q_SQ)
from hecke_engine import HeckeEngine

# ── Constants ────────────────────────────────────────────────────
m_e = 0.51100  # MeV
mu_0 = m_e / (3 * E_CROSS)
G_F = 1.1664e-11  # MeV⁻²
hbar = 6.582119569e-22  # MeV·s
sec_per_yr = 3.15576e7

def q_int(n):
    return (q**n - qi**n) / (q - qi)
from hecke_core import alpha_em

print(f"Half-lives from transfer matrix Skein polynomial ratios")
print(f"q = {q:.10f}, α_EM = {alpha_em:.6f} (1/α = {1/alpha_em:.2f})")
print(f"E_× = {E_CROSS:.6f}, μ₀ = {mu_0:.6f} MeV, E_×μ₀ = {E_CROSS*mu_0:.6f} MeV")
print()

# ── Phase space integral (exact) ─────────────────────────────────

from phase_space import fermi_phase_space

def phase_space(Z, Q_MeV, n_steps=50000):
    """Vectorized Fermi phase-space integral (delegated to phase_space.py)."""
    return fermi_phase_space(Z, Q_MeV, alpha_em=alpha_em, m_e_MeV=m_e, n_steps=n_steps)

# ── HeckeEngine for all nuclei ───────────────────────────────────

engine = HeckeEngine()

nuclei = [
    (1,   2,   "³H",    12.32,  "yr", sec_per_yr,  2),
    (6,   8,   "¹⁴C",   5730.0, "yr", sec_per_yr,  7),
    (27,  33,  "⁶⁰Co",  5.2714, "yr", sec_per_yr, 28),
    (38,  52,  "⁹⁰Sr",  28.79,  "yr", sec_per_yr, 39),
    (55,  82,  "¹³⁷Cs", 30.17,  "yr", sec_per_yr, 56),
    (83,  127, "²¹⁰Bi", 5.012,  "d",  86400.0,    84),
]

rate_base = G_F**2 * m_e**5 / (2 * math.pi**3 * hbar)  # s⁻¹

print(f"Rate base = {rate_base:.6e} s⁻¹")
print()

print(f"{'Nuc':>6} {'A':>4} {'ln(Pd/Pp)':>10} {'Q_pred':>8} {'Q_exp':>8} "
      f"{'|M|²':>10} {'f(Z,Q)':>10} {'t_pred':>12} {'t_obs':>10} {'ratio':>8}")
print("-" * 110)

# Experimental Q-values for comparison
Q_exp = {"³H": 0.01861, "¹⁴C": 0.15648, "⁶⁰Co": 0.31817,
         "⁹⁰Sr": 0.54590, "¹³⁷Cs": 0.51400, "²¹⁰Bi": 1.16270}

results = []
for p, n, name, t_obs, unit, conv, Z_d in nuclei:
    A = p + n
    r = engine.compute(p, n)

    # Generator volume product = |M_q|²
    # For A ≤ 20: use exact rational traces
    if A <= 20:
        log_M_sq = 0.0
        for i in range(A - 1):
            Vp = float(engine.qr.traced_volume(i, r.ordering_par))
            Vd = float(engine.qr.traced_volume(i, r.ordering_dau))
            if Vp != 0 and Vd != 0:
                log_M_sq += 2 * math.log(abs(Vp / Vd))
        M_sq = math.exp(log_M_sq) if abs(log_M_sq) < 500 else float('inf')

        # Skein polynomial ratio
        ln_ratio = math.log(abs(r.trace_dau_float / r.trace_par_float))
    else:
        # Log traces for large A
        log_M_sq = 0.0
        for i in range(A - 1):
            Vp = float(engine.qr.traced_volume(i, r.ordering_par))
            Vd = float(engine.qr.traced_volume(i, r.ordering_dau))
            if Vp != 0 and Vd != 0:
                log_M_sq += 2 * math.log(abs(Vp / Vd))
        M_sq = math.exp(log_M_sq) if abs(log_M_sq) < 500 else float('inf')
        ln_ratio = r.trace_dau_float - r.trace_par_float  # log traces

    # Q-value from Skein polynomial ratio
    Q_pred = abs(ln_ratio) * E_CROSS * mu_0

    # Use predicted Q for phase space
    f_val = phase_space(Z_d, Q_pred)

    # Self-deformation correction
    delta_q = (A - 1) / A**2 * HBAR_Q_SQ
    q_corr = 1 - 48 * delta_q / q  # shortens half-life

    # Rate and half-life
    Gamma = rate_base * M_sq * f_val * q_corr
    if Gamma > 0 and M_sq < 1e100:
        t_half = math.log(2) / Gamma / conv
    else:
        t_half = float('inf')

    ratio = t_half / t_obs if t_obs > 0 and t_half < 1e15 else float('nan')
    Qe = Q_exp[name]

    print(f"{name:>6} {A:>4} {ln_ratio:>10.6f} {Q_pred:>8.5f} {Qe:>8.5f} "
          f"{M_sq:>10.4e} {f_val:>10.4e} {t_half:>10.4f} {unit:2s} {t_obs:>8.3f} {unit:2s} {ratio:>8.4f}")

    results.append({
        "name": name, "A": A, "p": p, "n": n,
        "ln_ratio": ln_ratio, "Q_pred": Q_pred, "Q_exp": Qe,
        "M_sq": M_sq, "f_ZQ": f_val,
        "t_pred": t_half, "t_obs": t_obs, "unit": unit,
        "ratio": ratio,
    })

# ── Also compute with experimental Q-values ─────────────────────

print()
print("With EXPERIMENTAL Q-values (to isolate |M|² accuracy):")
print(f"{'Nuc':>6} {'|M|²':>10} {'f(Z,Q_exp)':>12} {'t_pred':>12} {'t_obs':>10} {'ratio':>8}")
print("-" * 70)

for r_data, (p, n, name, t_obs, unit, conv, Z_d) in zip(results, nuclei):
    M_sq = r_data["M_sq"]
    Qe = r_data["Q_exp"]
    f_val = phase_space(Z_d, Qe)

    A = p + n
    delta_q = (A - 1) / A**2 * HBAR_Q_SQ
    q_corr = 1 - 48 * delta_q / q

    Gamma = rate_base * M_sq * f_val * q_corr
    if Gamma > 0 and M_sq < 1e100:
        t_half = math.log(2) / Gamma / conv
    else:
        t_half = float('inf')
    ratio = t_half / t_obs if t_obs > 0 and t_half < 1e15 else float('nan')

    print(f"{name:>6} {M_sq:>10.4e} {f_val:>12.4e} {t_half:>10.4f} {unit:2s} {t_obs:>8.3f} {unit:2s} {ratio:>8.4f}")

# ── Witness ─────────────────────────────────────────────────────

witness = {
    "computation": "halflife-from-transfer-matrix",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "parameters": {"q": q, "alpha_em": alpha_em, "mu_0": mu_0,
                    "G_F": G_F, "rate_base": rate_base},
    "results": results,
}
out = Path(__file__).parent / "halflife-from-transfer-matrix.witness.json"
with open(out, "w") as f:
    json.dump(witness, f, indent=2)
print(f"\nWitness: {out}")
