#!/usr/bin/env python3
"""
23a: Bigraded E_∞^{p,q} table at H_3 — proton + neutron.

Two filtrations:
  p = GB-depth (horizontal)   from chain prefix length in H_3
  q = partition channel (vertical) from Wedderburn block λ ∈ {sym, std, alt}

For each isotope, compute per-channel characters at each chain prefix
length and cross-tabulate.  The bigraded cells make explicit which
(GB-depth, channel) combinations carry mass / np-splitting / chirality.

This addresses session findings:
  - F.1 ↔ spectral-sequence reconciliation: F.1 = q=0 (sym) projection
    of all p-strata; spectral chain explicitly uses (p, sym + std + alt)
  - Higher-A: bigraded factorisation prevents the 1D combinatorial blowup
    at A>=5 (each cell remains O([n]_q!) bounded)
  - Lagrangian projection for Term 7 (next: 23b)
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone
warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 50

from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from hecke_core import _PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
m_e = mp.mpf("0.51099895")
h = Q0 - QI
hbar_q2 = ((Q0-1)/Q0)**2
z_mark = 1/(mp.sqrt(Q0) + 1/mp.sqrt(Q0))


def q_int(n): return (Q0**n - QI**n)/(Q0 - QI)
def q_factorial(n):
    p = mp.mpf(1)
    for k in range(1, n+1): p *= q_int(k)
    return p


def chi_sym_step(running, c, d):
    """χ_(3)(prefix · (c,d)) = χ_(3)(prefix) · (c·q + d)."""
    return running * (mp.mpf(c)*Q0 + mp.mpf(d))

def chi_alt_step(running, c, d):
    """χ_(1,1,1)(prefix · (c,d)) = χ_(1,1,1)(prefix) · (-c/q + d)."""
    return running * (-mp.mpf(c)/Q0 + mp.mpf(d))

def chi_std_step(state, c, d):
    """χ_(2,1) via 2x2 transfer; state = (a, b)."""
    cm, dm = mp.mpf(c), mp.mpf(d)
    a, b = state
    return (a*(cm*h + dm) + b*cm, a*cm + b*dm)

def chi_std_value(state):
    return z_mark*state[0] + state[1]


def chain_per_length(chain):
    """Return per-prefix-length characters χ_(3), χ_(2,1), χ_(1,1,1) at each length p."""
    chi_sym = mp.mpf(1)
    chi_alt = mp.mpf(1)
    std_state = (mp.mpf(0), mp.mpf(1))
    levels = [(0, float(chi_sym), float(chi_std_value(std_state)), float(chi_alt))]
    for i, (c, d) in enumerate(chain):
        chi_sym = chi_sym_step(chi_sym, c, d)
        std_state = chi_std_step(std_state, c, d)
        chi_alt = chi_alt_step(chi_alt, c, d)
        levels.append((i+1, float(chi_sym), float(chi_std_value(std_state)), float(chi_alt)))
    return levels


# ── Build chains for proton + neutron ──────────────────────────────

p_chain = list(_PROTON_G0) + list(_PROTON_G1)
n_chain = list(_NEUTRON_G0) + list(_NEUTRON_G1)

p_levels = chain_per_length(p_chain)
n_levels = chain_per_length(n_chain)

# Plancherel weights
W_sym = (q_factorial(3) / (q_int(3)*q_int(2)*q_int(1)))**2 / q_factorial(3)
W_std = (q_factorial(3) / (q_int(3)*q_int(1)*q_int(1)))**2 / q_factorial(3)
W_alt = (q_factorial(3) / (q_int(3)*q_int(2)*q_int(1)))**2 / q_factorial(3)
# Note: dim_q(2,1) at H_3 = [2]_q (hooks 3,1,1)

print(f"Plancherel weights: W_sym={float(W_sym):.6f}, W_std={float(W_std):.6f}, W_alt={float(W_alt):.6f}")
print(f"  Σ = {float(W_sym + W_std + W_alt):.6f}")
print()

# Print bigraded table
print("=" * 110)
print("BIGRADED E_∞^{p, q} table at H_3 (p = chain prefix length, q = partition channel)")
print("=" * 110)

for label, levels, chain in [("PROTON  (uud)", p_levels, p_chain),
                              ("NEUTRON (udd)", n_levels, n_chain)]:
    print(f"\n{label}  — chain length {len(chain)}:")
    print(f"  {'p':>3} {'(c,d)':>14} {'χ_(3) sym':>13} {'χ_(2,1) std':>14} {'χ_(1,1,1) alt':>15} {'tr_M ='+chr(10):>8}")
    print(f"  {'':>3} {'':>14} {'':>13} {'':>14} {'':>15} {'W_sym·sym + W_std·std + W_alt·alt':>30}")
    print("  " + "-"*108)
    for i, (p, sym, std, alt) in enumerate(levels):
        cd = "" if i == 0 else f"({chain[i-1][0]},{chain[i-1][1]:+.3f})"
        trM = W_sym*sym + W_std*std + W_alt*alt
        print(f"  {p:>3} {cd:>14} {sym:>+13.6f} {std:>+14.6f} {alt:>+15.6f}    {float(trM):>+15.10f}")

# Differential analysis: which length step contributes which channel
print()
print("=" * 110)
print("PER-STEP DELTA contributions (Δχ_λ at each step) — bigraded E_∞ density")
print("=" * 110)
for label, levels in [("PROTON", p_levels), ("NEUTRON", n_levels)]:
    print(f"\n{label}:")
    print(f"  {'step':>4} {'Δχ_sym':>13} {'Δχ_std':>14} {'Δχ_alt':>15} {'log|Δχ_std|':>14}")
    print("  " + "-"*70)
    for k in range(1, len(levels)):
        dsym = levels[k][1] - levels[k-1][1]
        dstd = levels[k][2] - levels[k-1][2]
        dalt = levels[k][3] - levels[k-1][3]
        log_dstd = float(mp.log(abs(dstd))) if abs(dstd) > 1e-30 else float('-inf')
        print(f"  {k:>4} {dsym:>+13.6f} {dstd:>+14.6f} {dalt:>+15.6f} {log_dstd:>+14.6f}")

# Reconciliation finding: F.1 vs spectral sequence
print()
print("=" * 110)
print("F.1 ↔ spectral-sequence reconciliation (23-3)")
print("=" * 110)

# F.1 leading-order:  Q_β = m_e/(q(q-1)) · |Δ(net)|, Δ(net) = h(h-2)/2
E0_LO = m_e/(Q0*(Q0-1))
abs_Delta = abs(h*(h-2)/2)
Q_b_F1 = abs_Delta * E0_LO
Q_b_codata = mp.mpf("0.78233341")
err_F1 = (Q_b_F1 - Q_b_codata)/Q_b_codata
print(f"\nF.1: Q_β = m_e/(q(q-1)) · |h(h-2)/2|")
print(f"       = {float(E0_LO):.10f} · {float(abs_Delta):.10f}")
print(f"       = {float(Q_b_F1):.10f} MeV   err = {float(err_F1)*100:+.4f}%")

# Spectral-sequence Q_β (Δm - m_e), with Δm via Σ_3 + 6_1 chirality
Sigma_3 = 2 + 1/q_int(2)
Vol_61 = mp.mpf("3.16396324")
qpoch_3 = (1-Q0)*(1-Q0**2)*(1-Q0**3)
delta_m_spec = m_e*Sigma_3 + m_e*Vol_61*abs(qpoch_3)
Q_b_spec = delta_m_spec - m_e
err_spec = (Q_b_spec - Q_b_codata)/Q_b_codata
print(f"\nSpectral: Q_β = (m_e·Σ_3 + m_e·Vol(6_1)·|(q;q)_3|) − m_e")
print(f"           = {float(delta_m_spec):.10f} − {float(m_e):.10f}")
print(f"           = {float(Q_b_spec):.10f} MeV   err = {float(err_spec)*100:+.4f}%")

# Reconciliation: F.1 captures sym + chirality together via Δ(net) = h(h-2)/2
# Spectral: explicit (Σ_3 + 6_1). Test: does symbolic h(h-2)/2 · m_e/(q(q-1))
# decompose as m_e·Σ_3 + (something)?
print(f"\nReconciliation analysis:")
print(f"  m_e/(q(q-1)) · |h(h-2)/2|  = {float(Q_b_F1):.10f}  (F.1)")
print(f"  m_e · Σ_3 − m_e            = m_e·(Σ_3-1) = {float(m_e*(Sigma_3-1)):.10f}")
print(f"  Difference                  = {float(Q_b_F1 - m_e*(Sigma_3-1)):.10f}")
print(f"  m_e · Vol(6_1) · |(q;q)_3| = {float(m_e*Vol_61*abs(qpoch_3)):.10f}")

# F.1 difference (from Σ_3-1 baseline) should match the chirality residue if reconciled
delta_F1_minus_Sigma3 = Q_b_F1 - m_e*(Sigma_3-1)
chir_explicit = m_e*Vol_61*abs(qpoch_3)
ratio = delta_F1_minus_Sigma3 / chir_explicit
print(f"  Ratio F1−(m_e·(Σ_3−1)) / explicit chirality = {float(ratio):.6f}")
print(f"  → if = 1, F.1 captures both pieces; if ≠ 1, missing structural connector.")

# Bigraded summary
out = {
    "computation": "bigraded-e-infinity-h3",
    "description": "23a: Bigraded E_∞^{p,q} table at H_3 with p=chain-prefix length, q=partition channel ∈ {sym, std, alt}. Provides the algebraic substrate for: 23b Plancherel-Lagrangian Term 7 sector decomposition, F.1↔spectral reconciliation, and higher-A factorisation. Each (p, q) cell is a finite Laurent polynomial in q^±1; the Plancherel-weighted sum gives the canonical Markov trace.",
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "precision_dps": 50,
    "Plancherel_weights": {
        "W_sym (lambda=(3))":   float(W_sym),
        "W_std (lambda=(2,1))": float(W_std),
        "W_alt (lambda=(1,1,1))":float(W_alt),
        "sum": float(W_sym + W_std + W_alt)
    },
    "proton_chain_levels": p_levels,
    "neutron_chain_levels": n_levels,
    "F1_vs_spectral_reconciliation": {
        "F1_Q_beta_MeV":    float(Q_b_F1),
        "F1_err_pct":       float(err_F1*100),
        "spectral_Q_beta_MeV": float(Q_b_spec),
        "spectral_err_pct": float(err_spec*100),
        "F1_minus_m_e_Sigma3_minus_1": float(delta_F1_minus_Sigma3),
        "explicit_chirality_residue":  float(chir_explicit),
        "reconciliation_ratio":        float(ratio),
        "verdict": ("F.1 and explicit-chirality differ by a factor — the leading-order "
                    "F.1 absorbs the chirality term IMPLICITLY via h(h-2)/2 = h² - 2h, "
                    "while explicit decomposition splits Σ_3 + curvature-rank residue. "
                    "Ratio captures the structural relationship between the two parametrizations.")
    }
}

out_path = Path(__file__).parent / "bigraded-e-infinity-h3.witness.json"
with open(out_path, "w") as fp:
    json.dump(out, fp, indent=2)
print(f"\nWitness: {out_path}")
