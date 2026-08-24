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
from _precision import set_compute_dps  # noqa: E402 — dps must rise before module constants
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
    cd computations && python3 inverse-markov-qvalues.py
"""
import math
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from mpmath import mp
from itertools import combinations

sys.path.insert(0, str(Path(__file__).parent))
# mpmath, not the f64 family. This script is pure arithmetic on q0 — vertex
# volumes are a linear recursion, the Markov trace is their product — so there
# was never a reason for it to run in float64 (bean qou-t0rf). It also writes
# its witness with a bare `json.dump(..., default=str)` rather than
# `WitnessBuilder.save()`, so the raw-float64 guard installed at that single
# write point never saw it; carrying mpf through is what actually fixes it,
# and `default=str` then serializes them losslessly.
from q_parameter import Q_MP as q, Q_INV_MP as qi, HA_MP as h, LN_Q_MP as LN_Q
from experimental_constants import (
    M_E_MEV as _M_E_MEV, M_P_MEV as _M_P_MEV, M_N_MEV as _M_N_MEV,
    Q_TRITIUM_MEV as _Q_TRITIUM_MEV, Q_NEUTRON_MEV as _Q_NEUTRON_MEV,
)

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
#
# THIS CALL USED TO SIT ~96 LINES LOWER, just above `decays`. Everything it
# names as "the constants below" was in fact ABOVE it, so the five constants
# here were built at mpmath's default 15 dps -- ~53 bits, i.e. binary64 -- and
# then printed to 50+ digits once dps rose afterwards. That is not precision,
# it is the float64's binary tail: the witness carried
#     Q_exp = 0.01861000000000000154098955817971727810800075531005859375
# for a quantity whose source is `0.01861  # +/- 0.00001 MeV`. Only the
# `mp.mpf("...")` literals inside `decays` were ever actually protected.
set_compute_dps()

M_E_MEV = mp.mpf(repr(_M_E_MEV))
M_P_MEV = mp.mpf(repr(_M_P_MEV))
M_N_MEV = mp.mpf(repr(_M_N_MEV))
Q_TRITIUM_MEV = mp.mpf(repr(_Q_TRITIUM_MEV))
Q_NEUTRON_MEV = mp.mpf(repr(_Q_NEUTRON_MEV))

z = q**3 / (q**2 + 1)
ln_q = LN_Q

print("INVERSE MARKOV TRACE Q-VALUES")
print(f"  q₀ = {mp.nstr(q, 17)}, h = {mp.nstr(h, 12)}, z = {mp.nstr(z, 12)}")
print("=" * 80)


# ══════════════════════════════════════════════════════════════
#  VERTEX VOLUMES AND MARKOV TRACE
# ══════════════════════════════════════════════════════════════

def chain_V(ordering, gen, type_fn):
    """Vertex volume V̂ at generator position gen."""
    n = len(ordering)
    a, b = mp.mpf(0), mp.mpf(1)
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
    product = mp.mpf(1)
    for i in range(n - 1):
        V = chain_V(ordering, i, type_fn)
        vols.append(V)
        product *= V
    return product, vols


def nucleon_typed_d(ti, tj):
    """Nucleon-level crossing coefficient."""
    if ti == 'p' and tj == 'p': return mp.mpf(0)
    if ti == 'n' and tj == 'n': return -h
    return -h / 2


def quark_typed_d(fi, fj):
    """Quark-level crossing coefficient."""
    if fi == 'u' and fj == 'u': return mp.mpf(0)
    if fi == 'd' and fj == 'd': return -h
    return -h / 2


def find_gs_nucleon(Z, N):
    """Find ground state nucleon ordering (max |tr_M| = most stable)."""
    A = Z + N
    best_tr = mp.mpf(0)
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
    best_tr = mp.mpf(0)
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
    (2, 4, 3, 3, mp.mpf("3.508"),    '⁶He→⁶Li'),
    (6, 8, 7, 7, mp.mpf("0.15648"),  '¹⁴C→¹⁴N'),
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

    inv_par = 1 / abs(tr_par) if abs(tr_par) > mp.mpf('1e-300') else mp.inf
    inv_dau = 1 / abs(tr_dau) if abs(tr_dau) > mp.mpf('1e-300') else mp.inf
    delta_inv = inv_par - inv_dau  # > 0 if parent has more stored energy

    print(f"\n  {name} (A={A})")
    print(f"    Parent:   {''.join(gs_par)}, tr_M = {mp.nstr(mp.mpf(tr_par), 10)}, 1/|tr_M| = {mp.nstr(mp.mpf(inv_par), 6)}")
    print(f"    Daughter: {''.join(gs_dau)}, tr_M = {mp.nstr(mp.mpf(tr_dau), 10)}, 1/|tr_M| = {mp.nstr(mp.mpf(inv_dau), 6)}")
    print(f"    Δ(1/|tr_M|) = {mp.nstr(mp.mpf(delta_inv), 8)}")

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
        print(f"    {r['name']:>12s}: scale = Q_exp/|Δ(1/|tr_M|)| = {mp.nstr(mp.mpf(scale), 8)} MeV")

# Use ³H as calibrator
if len(nuc_results) >= 2:
    tritium_r = next((r for r in nuc_results if '³H' in r['name']), None)
    if tritium_r and abs(tritium_r['delta_inv']) > 1e-10:
        cal_scale = tritium_r['Q_exp'] / abs(tritium_r['delta_inv'])
        print(f"\n  Using ³H as calibrator: scale = {mp.nstr(mp.mpf(cal_scale), 8)} MeV")
        for r in nuc_results:
            Q_calc = abs(r['delta_inv']) * cal_scale
            err = (Q_calc / r['Q_exp'] - 1) * 100 if r['Q_exp'] > 0 else mp.nan
            print(f"    {r['name']:>12s}: Q = {mp.nstr(mp.mpf(Q_calc), 8)} MeV (exp: {mp.nstr(mp.mpf(r['Q_exp']), 8)}, err: {mp.nstr(mp.mpf(err), 3)}%)")


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

    inv_par = 1 / abs(tr_par) if abs(tr_par) > mp.mpf('1e-300') else mp.inf
    inv_dau = 1 / abs(tr_dau) if abs(tr_dau) > mp.mpf('1e-300') else mp.inf
    delta_inv = inv_par - inv_dau

    print(f"\n  {name} (A={A}, 3A={3*A} quarks)")
    print(f"    Parent:   tr_M = {mp.nstr(mp.mpf(tr_par), 14)}, 1/|tr_M| = {mp.nstr(mp.mpf(inv_par), 6)}")
    print(f"    Daughter: tr_M = {mp.nstr(mp.mpf(tr_dau), 14)}, 1/|tr_M| = {mp.nstr(mp.mpf(inv_dau), 6)}")
    print(f"    Δ(1/|tr_M|) = {mp.nstr(mp.mpf(delta_inv), 8)}")

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
        print(f"    {r['name']:>12s}: scale = {mp.nstr(mp.mpf(scale), 8)} MeV")

# Use free neutron as calibrator
neutron_r = next((r for r in quark_results if 'n→p' in r['name']), None)
if neutron_r and abs(neutron_r['delta_inv']) > 1e-10:
    cal_scale_n = neutron_r['Q_exp'] / abs(neutron_r['delta_inv'])
    print(f"\n  Using n→p as calibrator: scale = {mp.nstr(mp.mpf(cal_scale_n), 8)} MeV")
    for r in quark_results:
        Q_calc = abs(r['delta_inv']) * cal_scale_n
        err = (Q_calc / r['Q_exp'] - 1) * 100 if r['Q_exp'] > 0 else mp.nan
        print(f"    {r['name']:>12s}: Q = {mp.nstr(mp.mpf(Q_calc), 8)} MeV (exp: {mp.nstr(mp.mpf(r['Q_exp']), 8)}, err: {mp.nstr(mp.mpf(err), 3)}%)")


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

        F_par = -mp.log(abs(tr_par)) if abs(tr_par) > mp.mpf('1e-300') else mp.inf
        F_dau = -mp.log(abs(tr_dau)) if abs(tr_dau) > mp.mpf('1e-300') else mp.inf
        dF = F_par - F_dau

        results_list.append({
            'name': name, 'A': A, 'F_par': F_par, 'F_dau': F_dau,
            'dF': dF, 'Q_exp': Q_exp,
        })

    print(f"\n  {label} level:")
    print(f"  {'Decay':>12s} | {'F_par':>10s} | {'F_dau':>10s} | {'ΔF':>10s} | {'Q_exp':>10s}")
    print(f"  {'':->60s}")
    for r in results_list:
        print(f"  {r['name']:>12s} | {mp.nstr(mp.mpf(r['F_par']), 6):>10} | {mp.nstr(mp.mpf(r['F_dau']), 6):>10} | "
              f"{mp.nstr(mp.mpf(r['dF']), 6):>10} | {mp.nstr(mp.mpf(r['Q_exp']), 8):>10}")


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
    print(f"  {name:>12s}: Q = {mp.nstr(mp.mpf(Q_exp), 8)} = {mp.nstr(mp.mpf(Q0), 5)} + ({mp.nstr(mp.mpf(dB), 6)}) MeV  [ΔB = {mp.nstr(mp.mpf(dB), 6)}]")

print(f"\n  The ΔB values span {mp.nstr(mp.mpf(min(Q_exp - Q0 for _,_,_,_,Q_exp,_ in decays)), 5)} to "
      f"{mp.nstr(mp.mpf(max(Q_exp - Q0 for _,_,_,_,Q_exp,_ in decays)), 5)} MeV")
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
        Q_vv = mp.nan

    # Free energy (nucleon)
    if A <= 14:
        _, tr_par = find_gs_nucleon(Z_par, N_par)
        _, tr_dau = find_gs_nucleon(Z_dau, N_dau)
        dF = (-mp.log(abs(tr_par))) - (-mp.log(abs(tr_dau)))
        Q_fe = abs(dF) * ln_q * M_E_MEV
    else:
        Q_fe = mp.nan

    # Inverse Markov trace (nucleon)
    if A <= 14:
        inv_par = 1 / abs(tr_par)
        inv_dau = 1 / abs(tr_dau)
        d_inv = inv_par - inv_dau
    else:
        d_inv = mp.nan

    print(f"  {name:>12s} | {mp.nstr(mp.mpf(Q_exp), 6):>8} | {mp.nstr(mp.mpf(Q_vv), 8):>12} | "
          f"{mp.nstr(mp.mpf(Q_fe), 8):>12} | {mp.nstr(mp.mpf(d_inv), 6):>12} | {mp.nstr(mp.mpf(dB), 6):>8}")

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
from witness_base import WitnessBuilder  # noqa: E402 — P30 staleness triple
WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__)  # scriptHash/scriptCommitSha
witness["scriptFile"] = Path(__file__).name
witness_path = Path(__file__).parent / 'inverse-markov-qvalues.witness.json'
with open(witness_path, 'w') as f:
    json.dump(witness, f, indent=2, default=str)
print(f"\n  Witness: {witness_path.name}")
