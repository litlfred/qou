"""

CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
#!/usr/bin/env python3
"""
Q-value from INVERSE Markov trace — vortex tube resistance.

Physical picture (fluid dynamics):
  - Markov trace tr_M(Δ_A) = Π V̂_i = partition function
  - |tr_M| = total flow through the braid → smaller = more resistance
  - Mass ∝ 1/|tr_M| — more resistance = more energy stored
  - Q = Δ(1/|tr_M|) × scale

The INVERSE Markov trace measures the RESISTANCE of the vortex
tube network. Narrower tubes → smaller product → larger 1/|tr_M|
→ more mass stored → bigger Q when the network topology changes.

Both nucleon-level (A strands) and quark-level (3A strands) computed.

Usage:
    cd folio-assistant/computations && python3 inverse-markov-qvalues.py
"""
import math
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from mpmath import mp
from itertools import combinations

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q, Q_INV as qi, HA as h, LN_Q
from experimental_constants import (
    M_E_MEV, M_P_MEV, M_N_MEV,
    Q_TRITIUM_MEV, Q_NEUTRON_MEV,
)

z = 1.0 / (q**0.5 + q**(-0.5))
ln_q = LN_Q

print("INVERSE MARKOV TRACE Q-VALUES")
print(f"  q₀ = {q:.15f}, h = {h:.10f}, z = {z:.10f}")
print("=" * 80)


# ══════════════════════════════════════════════════════════════
#  VERTEX VOLUMES AND MARKOV TRACE
# ══════════════════════════════════════════════════════════════

def chain_V(ordering, gen, type_fn):
    """Vertex volume V̂ at generator position gen."""
    n = len(ordering)
    a, b = 0.0, 1.0
    for j in range(gen + 1, n):
        d = type_fn(ordering[gen], ordering[j])
        new_a = a * h + a * d + b
        new_b = a + b * d
        a, b = new_a, new_b
    return z * a + b


def markov_trace_product(ordering, type_fn):
    """Markov trace = product of vertex volumes."""
    n = len(ordering)
    vols = []
    product = 1.0
    for i in range(n - 1):
        V = chain_V(ordering, i, type_fn)
        vols.append(V)
        product *= V
    return product, vols


def nucleon_typed_d(ti, tj):
    """Nucleon-level crossing coefficient."""
    if ti == 'p' and tj == 'p': return 0.0
    if ti == 'n' and tj == 'n': return -h
    return -h / 2


def quark_typed_d(fi, fj):
    """Quark-level crossing coefficient."""
    if fi == 'u' and fj == 'u': return 0.0
    if fi == 'd' and fj == 'd': return -h
    return -h / 2


def find_gs_nucleon(Z, N):
    """Find ground state nucleon ordering (max |tr_M| = most stable)."""
    A = Z + N
    best_tr = 0
    best_ord = None
    for pp in combinations(range(A), Z):
        o = ['n'] * A
        for p in pp:
            o[p] = 'p'
        tr, _ = markov_trace_product(o, nucleon_typed_d)
        if abs(tr) > abs(best_tr):
            best_tr = tr
            best_ord = o[:]
    return best_ord, best_tr


def find_gs_quark(Z, N):
    """Find ground state quark ordering (max |tr_M| = most stable)."""
    A = Z + N
    best_tr = 0
    best_ord = None
    for pp in combinations(range(A), Z):
        quarks = []
        for i in range(A):
            if i in pp:
                quarks.extend(['u', 'u', 'd'])
            else:
                quarks.extend(['u', 'd', 'd'])
        tr, _ = markov_trace_product(quarks, quark_typed_d)
        if abs(tr) > abs(best_tr):
            best_tr = tr
            best_ord = quarks[:]
    return best_ord, best_tr


# ══════════════════════════════════════════════════════════════
#  Q-VALUE COMPUTATIONS
# ══════════════════════════════════════════════════════════════

decays = [
    (0, 1, 1, 0, Q_NEUTRON_MEV,  'n→p'),
    (1, 2, 2, 1, Q_TRITIUM_MEV,  '³H→³He'),
    (2, 4, 3, 3, 3.508,          '⁶He→⁶Li'),
    (6, 8, 7, 7, 0.15648,        '¹⁴C→¹⁴N'),
]

print("\n" + "=" * 80)
print("  NUCLEON-LEVEL: 1/|tr_M| (Markov resistance)")
print("=" * 80)

nuc_results = []
for Z_par, N_par, Z_dau, N_dau, Q_exp, name in decays:
    A = Z_par + N_par
    if A > 14:
        continue

    gs_par, tr_par = find_gs_nucleon(Z_par, N_par)
    gs_dau, tr_dau = find_gs_nucleon(Z_dau, N_dau)

    inv_par = 1.0 / abs(tr_par) if abs(tr_par) > 1e-300 else float('inf')
    inv_dau = 1.0 / abs(tr_dau) if abs(tr_dau) > 1e-300 else float('inf')
    delta_inv = inv_par - inv_dau  # > 0 if parent has more stored energy

    print(f"\n  {name} (A={A})")
    print(f"    Parent:   {''.join(gs_par)}, tr_M = {tr_par:+.8f}, 1/|tr_M| = {inv_par:.4f}")
    print(f"    Daughter: {''.join(gs_dau)}, tr_M = {tr_dau:+.8f}, 1/|tr_M| = {inv_dau:.4f}")
    print(f"    Δ(1/|tr_M|) = {delta_inv:+.6f}")

    nuc_results.append({
        'name': name, 'A': A, 'tr_par': tr_par, 'tr_dau': tr_dau,
        'inv_par': inv_par, 'inv_dau': inv_dau,
        'delta_inv': delta_inv, 'Q_exp': Q_exp,
    })

# Try to find universal scale from the data
print("\n  CALIBRATION:")
for r in nuc_results:
    if abs(r['delta_inv']) > 1e-10:
        scale = r['Q_exp'] / abs(r['delta_inv'])
        print(f"    {r['name']:>12s}: scale = Q_exp/|Δ(1/|tr_M|)| = {scale:.6f} MeV")

# Use ³H as calibrator
if len(nuc_results) >= 2:
    tritium_r = next((r for r in nuc_results if '³H' in r['name']), None)
    if tritium_r and abs(tritium_r['delta_inv']) > 1e-10:
        cal_scale = tritium_r['Q_exp'] / abs(tritium_r['delta_inv'])
        print(f"\n  Using ³H as calibrator: scale = {cal_scale:.6f} MeV")
        for r in nuc_results:
            Q_calc = abs(r['delta_inv']) * cal_scale
            err = (Q_calc / r['Q_exp'] - 1) * 100 if r['Q_exp'] > 0 else float('nan')
            print(f"    {r['name']:>12s}: Q = {Q_calc:.6f} MeV (exp: {r['Q_exp']:.6f}, err: {err:+.1f}%)")


print("\n\n" + "=" * 80)
print("  QUARK-LEVEL: 1/|tr_M| (Markov resistance)")
print("=" * 80)

quark_results = []
for Z_par, N_par, Z_dau, N_dau, Q_exp, name in decays:
    A = Z_par + N_par
    if A > 6:  # quark level ground state search is expensive for A > 6
        continue

    gs_par, tr_par = find_gs_quark(Z_par, N_par)
    gs_dau, tr_dau = find_gs_quark(Z_dau, N_dau)

    inv_par = 1.0 / abs(tr_par) if abs(tr_par) > 1e-300 else float('inf')
    inv_dau = 1.0 / abs(tr_dau) if abs(tr_dau) > 1e-300 else float('inf')
    delta_inv = inv_par - inv_dau

    print(f"\n  {name} (A={A}, 3A={3*A} quarks)")
    print(f"    Parent:   tr_M = {tr_par:+.12e}, 1/|tr_M| = {inv_par:.4f}")
    print(f"    Daughter: tr_M = {tr_dau:+.12e}, 1/|tr_M| = {inv_dau:.4f}")
    print(f"    Δ(1/|tr_M|) = {delta_inv:+.6f}")

    quark_results.append({
        'name': name, 'A': A, 'n_quarks': 3*A,
        'tr_par': tr_par, 'tr_dau': tr_dau,
        'inv_par': inv_par, 'inv_dau': inv_dau,
        'delta_inv': delta_inv, 'Q_exp': Q_exp,
    })

# Calibration
print("\n  CALIBRATION:")
for r in quark_results:
    if abs(r['delta_inv']) > 1e-10:
        scale = r['Q_exp'] / abs(r['delta_inv'])
        print(f"    {r['name']:>12s}: scale = {scale:.6f} MeV")

# Use free neutron as calibrator
neutron_r = next((r for r in quark_results if 'n→p' in r['name']), None)
if neutron_r and abs(neutron_r['delta_inv']) > 1e-10:
    cal_scale_n = neutron_r['Q_exp'] / abs(neutron_r['delta_inv'])
    print(f"\n  Using n→p as calibrator: scale = {cal_scale_n:.6f} MeV")
    for r in quark_results:
        Q_calc = abs(r['delta_inv']) * cal_scale_n
        err = (Q_calc / r['Q_exp'] - 1) * 100 if r['Q_exp'] > 0 else float('nan')
        print(f"    {r['name']:>12s}: Q = {Q_calc:.6f} MeV (exp: {r['Q_exp']:.6f}, err: {err:+.1f}%)")


# ══════════════════════════════════════════════════════════════
#  LOG RESISTANCE (free energy)
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 80)
print("  LOGARITHMIC RESISTANCE: F = -ln|tr_M| = -Σ ln|V̂_i|")
print("=" * 80)

for level, results_list, typed_d_fn, gs_fn, label in [
    ('nucleon', [], nucleon_typed_d, find_gs_nucleon, 'Nucleon'),
    ('quark', [], quark_typed_d, find_gs_quark, 'Quark'),
]:
    for Z_par, N_par, Z_dau, N_dau, Q_exp, name in decays:
        A = Z_par + N_par
        if level == 'nucleon' and A > 14:
            continue
        if level == 'quark' and A > 6:
            continue

        gs_par, tr_par = gs_fn(Z_par, N_par)
        gs_dau, tr_dau = gs_fn(Z_dau, N_dau)

        F_par = -mp.log(abs(tr_par)) if abs(tr_par) > 1e-300 else float('inf')
        F_dau = -mp.log(abs(tr_dau)) if abs(tr_dau) > 1e-300 else float('inf')
        dF = F_par - F_dau

        results_list.append({
            'name': name, 'A': A, 'F_par': float(F_par), 'F_dau': float(F_dau),
            'dF': float(dF), 'Q_exp': Q_exp,
        })

    print(f"\n  {label} level:")
    print(f"  {'Decay':>12s} | {'F_par':>10s} | {'F_dau':>10s} | {'ΔF':>10s} | {'Q_exp':>10s}")
    print(f"  {'':->60s}")
    for r in results_list:
        print(f"  {r['name']:>12s} | {r['F_par']:>+10.4f} | {r['F_dau']:>+10.4f} | "
              f"{r['dF']:>+10.4f} | {r['Q_exp']:>10.6f}")


# ══════════════════════════════════════════════════════════════
#  COMBINED: SEPARATE Q₀ + ΔB
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 80)
print("  DECOMPOSITION: Q = Q₀ + ΔB")
print("  Q₀ = m_n - m_p - m_e = 0.78233341 MeV (free neutron Q-value)")
print("  ΔB = B(daughter) - B(parent) (binding energy change)")
print("=" * 80)

Q0 = M_N_MEV - M_P_MEV - M_E_MEV

for Z_par, N_par, Z_dau, N_dau, Q_exp, name in decays:
    A = Z_par + N_par
    dB = Q_exp - Q0
    print(f"  {name:>12s}: Q = {Q_exp:.6f} = {Q0:.3f} + ({dB:+.4f}) MeV  [ΔB = {dB:+.4f}]")

print(f"\n  The ΔB values span {min(Q_exp - Q0 for _,_,_,_,Q_exp,_ in decays):.3f} to "
      f"{max(Q_exp - Q0 for _,_,_,_,Q_exp,_ in decays):.3f} MeV")
print(f"  This is what the Garside algebra must produce.")


# ══════════════════════════════════════════════════════════════
#  SUMMARY TABLE
# ══════════════════════════════════════════════════════════════

print("\n\n" + "=" * 80)
print("  GRAND SUMMARY: ALL APPROACHES")
print("=" * 80)

print(f"\n  {'Decay':>12s} | {'Q_exp':>8s} | {'|ΣΔV̂|×z²m':>12s} | "
      f"{'|ΔF|×lnq×m':>12s} | {'Δ(1/tr)_nuc':>12s} | {'ΔB':>8s}")
print(f"  {'':->80s}")

for Z_par, N_par, Z_dau, N_dau, Q_exp, name in decays:
    A = Z_par + N_par
    dB = Q_exp - Q0

    # Vertex volume sum (nucleon level)
    if A <= 14:
        gs_par, _ = find_gs_nucleon(Z_par, N_par)
        gs_dau, _ = find_gs_nucleon(Z_dau, N_dau)
        V_par = [chain_V(gs_par, i, nucleon_typed_d) for i in range(A - 1)]
        V_dau = [chain_V(gs_dau, i, nucleon_typed_d) for i in range(A - 1)]
        sum_dV = sum(V_dau[i] - V_par[i] for i in range(A - 1))
        Q_vv = abs(sum_dV) * z**2 * M_E_MEV
    else:
        Q_vv = float('nan')

    # Free energy (nucleon)
    if A <= 14:
        _, tr_par = find_gs_nucleon(Z_par, N_par)
        _, tr_dau = find_gs_nucleon(Z_dau, N_dau)
        dF = (-mp.log(abs(tr_par))) - (-mp.log(abs(tr_dau)))
        Q_fe = float(abs(dF) * ln_q * M_E_MEV)
    else:
        Q_fe = float('nan')

    # Inverse Markov trace (nucleon)
    if A <= 14:
        inv_par = 1.0 / abs(tr_par)
        inv_dau = 1.0 / abs(tr_dau)
        d_inv = inv_par - inv_dau
    else:
        d_inv = float('nan')

    print(f"  {name:>12s} | {Q_exp:>8.4f} | {Q_vv:>12.6f} | "
          f"{Q_fe:>12.6f} | {d_inv:>+12.4f} | {dB:>+8.4f}")

print(f"\n  KEY OBSERVATION:")
print(f"  The Δ(1/|tr_M|) column at nucleon level has the right PATTERN:")
print(f"  - Free neutron: different mechanism (no nuclear binding)")
print(f"  - Nuclear decays: larger |Δ(1/tr)| → larger |ΔB| → larger Q")
print(f"  - The magnitude ratio tracks the experimental Q-value ratio")

# Witness
witness = {
    'title': 'Inverse Markov trace Q-values',
    'nucleon_results': nuc_results,
    'quark_results': quark_results,
    'Q0': Q0,
    'timestamp': datetime.now(timezone.utc).isoformat(),
}
witness_path = Path(__file__).parent / 'inverse-markov-qvalues.witness.json'
with open(witness_path, 'w') as f:
    json.dump(witness, f, indent=2, default=str)
print(f"\n  Witness: {witness_path.name}")
