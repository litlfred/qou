#!/usr/bin/env python3
"""
Q-values from Rust engine GB NF certificates.

Uses the exact Gröbner-Shirshov normal forms computed by the Rust
Hecke engine (tools/hecke-engine) to compute Q-values.

The certificates contain:
  - f_pauli: the Pauli function F = Σ w_k tr_k (Wedderburn-weighted trace)
  - net: the net function (L1-like norm)
  - tr_alt: the alternating trace
  - total_words: number of NF terms
  - Symbolic Laurent polynomials in t = q^{1/2}

Q-value formula:
  Q = |F_parent - F_daughter| × E₀
where F is the Pauli function and E₀ is the energy scale.

Usage:
    cd folio-assistant/computations && python3 qvalue-from-certificates.py
"""
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0, HA as h, HBAR_Q, LN_Q
from experimental_constants import (
    M_E_MEV, M_P_MEV, M_N_MEV,
    Q_TRITIUM_MEV, Q_C14_MEV, Q_CO60_MEV,
    Q_SR90_MEV, Q_CS137_MEV,
)

z = 1.0 / (q0**0.5 + q0**(-0.5))
CERT_DIR = Path(__file__).parent.parent.parent / "tools" / "hecke-engine"


def load_cert(name):
    """Load a certificate JSON file."""
    path = CERT_DIR / f"certificate-{name}.json"
    if not path.exists():
        return None
    return json.load(open(path))


def eval_lpoly(terms, q_val):
    """Evaluate a Laurent polynomial at q = q_val.
    terms = [[power, coeff_str], ...] where power is in t = q^{1/2}."""
    t = math.sqrt(q_val)
    result = 0.0
    for power, coeff_str in terms:
        result += int(coeff_str) * t ** power
    return result


print(f"Q-VALUES FROM RUST ENGINE GB NF CERTIFICATES")
print(f"q₀ = {q0:.10f}, m_e = {M_E_MEV:.6f} MeV")
print(f"="*90)

# Load all relevant certificates
decays = [
    ('3H→3He',    '3h',  '3he',  Q_TRITIUM_MEV),
    ('6He→6Li',   '6he', '6li',  3.508),
    ('14C→14N',   '14c', '14n',  Q_C14_MEV),
    ('40K→40Ca',  None,  '40ca', 1.312),  # No 40K cert, but 40Ca exists
]

print(f"\nCERTIFICATE DATA:")
print(f"{'Isotope':>8s} | {'Z':>3s} {'N':>3s} {'A':>3s} | {'words':>5s} | {'f_pauli':>10s} | {'net':>12s} | {'tr_alt':>12s}")
print(f"{'-'*70}")

all_certs = {}
for iso_name in ['3h', '3he', '6he', '6li', '14c', '14n', '40ca', '60co']:
    c = load_cert(iso_name)
    if c is None:
        print(f"{iso_name:>8s} | MISSING")
        continue
    all_certs[iso_name] = c
    iso = c['isotope']
    fp = c.get('f_pauli_f64', 0)
    net = c.get('net_f64', 0)
    tr_alt = c.get('tr_alt_f64', 0)
    words = c.get('total_words', 0)
    print(f"{iso_name:>8s} | {iso['z']:>3d} {iso['n']:>3d} {iso['a']:>3d} | {words:>5d} | {fp:>10.6f} | {net:>12.6f} | {tr_alt:>12.4e}")

# Evaluate symbolic polynomials at q₀
print(f"\nSYMBOLIC EVALUATION AT q₀:")
print(f"{'Isotope':>8s} | {'f_pauli(q₀)':>12s} | {'net(q₀)':>12s} | {'tr_alt(q₀)':>12s} | {'observable(q₀)':>14s}")
print(f"{'-'*70}")

for iso_name, c in all_certs.items():
    fp = c.get('f_pauli_f64', 0)
    # Also try evaluating the symbolic polynomials
    net_sym = eval_lpoly(c['net']['terms'], q0) if 'net' in c else 0
    tr_alt_sym = eval_lpoly(c['tr_alt']['terms'], q0) if 'tr_alt' in c else 0
    obs_sym = eval_lpoly(c['observable']['terms'], q0) if 'observable' in c else 0

    print(f"{iso_name:>8s} | {fp:>12.6f} | {net_sym:>12.6f} | {tr_alt_sym:>12.6f} | {obs_sym:>14.6f}")

# ══════════════════════════════════════════════════════════════
#  Q-VALUE FORMULAS
# ══════════════════════════════════════════════════════════════

print(f"\n{'='*90}")
print(f"Q-VALUE COMPUTATION")
print(f"{'='*90}")

# Energy scale: E₀ = m_p / f_pauli(proton)
# The proton cert is embedded in the nuclear certs.
# From the atom mass engine: E₀ calibrated so that M(proton) = m_p
# For now use E₀ = m_p (since proton f_pauli ≈ 1 for our formula)

# Actually, the f_pauli IS the binding energy functional.
# Q = |f_pauli(parent) - f_pauli(daughter)| × energy_scale
# What energy scale? The atom mass engine uses M = f(tr_M, net, ...) × E₀
# where E₀ = m_p / tr_M(proton).

# Let's try multiple Q formulas using the certificate data:

print(f"\n{'Decay':>12s} | {'Δf_pauli':>10s} | {'Δnet':>10s} | {'Δwords':>6s} | {'Q_exp':>8s}")
print(f"{'-'*60}")

results = []
for name, par_iso, dau_iso, Q_exp in decays:
    if par_iso is None or par_iso not in all_certs:
        print(f"{name:>12s} | {'no cert':>10s}")
        continue
    if dau_iso not in all_certs:
        print(f"{name:>12s} | {'no dau cert':>10s}")
        continue

    cp = all_certs[par_iso]
    cd = all_certs[dau_iso]

    fp_p = cp.get('f_pauli_f64', 0)
    fp_d = cd.get('f_pauli_f64', 0)
    net_p = cp.get('net_f64', 0)
    net_d = cd.get('net_f64', 0)
    words_p = cp.get('total_words', 0)
    words_d = cd.get('total_words', 0)

    d_fp = fp_p - fp_d
    d_net = net_p - net_d
    d_words = words_p - words_d

    print(f"{name:>12s} | {d_fp:>+10.6f} | {d_net:>+10.6f} | {d_words:>+6d} | {Q_exp:>8.4f}")

    results.append({
        'name': name, 'Q_exp': Q_exp,
        'd_fp': d_fp, 'd_net': d_net, 'd_words': d_words,
        'fp_p': fp_p, 'fp_d': fp_d,
        'net_p': net_p, 'net_d': net_d,
    })

# Try different Q formulas
print(f"\n{'='*90}")
print(f"Q-VALUE FORMULAS")
print(f"{'='*90}")

if results:
    # Use 14C as calibration: Q_14C = 0.1565 MeV
    r_14c = next((r for r in results if '14C' in r['name']), None)

    if r_14c:
        # Scale from 14C: energy_per_dfp = Q_14C / |d_fp_14C|
        if abs(r_14c['d_fp']) > 1e-15:
            E_fp = Q_C14_MEV / abs(r_14c['d_fp'])
        else:
            E_fp = 1.0

        if abs(r_14c['d_net']) > 1e-15:
            E_net = Q_C14_MEV / abs(r_14c['d_net'])
        else:
            E_net = 1.0

        print(f"\n  Calibration from ¹⁴C:")
        print(f"  E_fp  = Q(14C) / |Δf_pauli(14C)| = {E_fp:.4f} MeV")
        print(f"  E_net = Q(14C) / |Δnet(14C)| = {E_net:.6f} MeV")

        print(f"\n  {'Decay':>12s} | {'Q_fp':>8s} | {'Q_net':>8s} | {'Q_exp':>8s} | {'err_fp':>7s} | {'err_net':>7s}")
        print(f"  {'-'*65}")

        for r in results:
            Q_fp = abs(r['d_fp']) * E_fp
            Q_net = abs(r['d_net']) * E_net
            err_fp = (Q_fp / r['Q_exp'] - 1) * 100 if r['Q_exp'] > 0 else 0
            err_net = (Q_net / r['Q_exp'] - 1) * 100 if r['Q_exp'] > 0 else 0
            print(f"  {r['name']:>12s} | {Q_fp:>8.4f} | {Q_net:>8.4f} | {r['Q_exp']:>8.4f} | {err_fp:>+6.1f}% | {err_net:>+6.1f}%")

# Witness
witness = {
    'name': 'qvalue-from-certificates',
    'q': q0, 'm_e': M_E_MEV,
    'results': results,
}
out = Path(__file__).with_suffix('.witness.json')
out.write_text(json.dumps(witness, indent=2, default=float))
print(f"\n  Witness: {out.name}")
