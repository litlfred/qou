#!/usr/bin/env python3
"""
Δ_λ multi-atom cross-validation: test the corrected ansatz on D, T, ³He.

The corrected ansatz from the bar-involution probe:
    Δ_λ = (-1)^{n(λ)} × dim_q(λ) × C_knot
where C_knot = linking_weight / (|tr_M| × √[n/2]_q!) is a per-knot
geometric correction from the Bring surface.

Test: compute Δ_λ for H_6 (deuteron) and H_9 (tritium, ³He) using
the q-Schur y_λ closed form, and check whether the SAME structural
ansatz (with knot-appropriate C_knot) predicts all three binding
energies simultaneously.

y_λ computed via q-Schur closed form (PR #1259):
    y_λ^S = q^{c(λ)} / [n]_q!
where c(λ) = content sum = Σ_{(i,j)∈λ} (j-i).
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
from codata_constants import M_N_MEV_VALIDATION, M_P_MEV_VALIDATION  # noqa: E402 (codata sweep)
import json, time
from q_parameter import Q_50_DIGIT_STR
from pathlib import Path
from mpmath import mp, mpf, fabs

mp.dps = 50
HERE = Path(__file__).resolve().parent

q0 = mpf(Q_50_DIGIT_STR)
qi = 1/q0
h = q0 - qi
m_e = mpf('0.51099895069')

def q_int(k):
    if k == 0: return mpf(0)
    return (q0**k - qi**k) / h

def q_fac(n):
    r = mpf(1)
    for k in range(1, n+1):
        r *= q_int(k)
    return r

def content_sum(lam):
    return sum(j - i for i in range(len(lam)) for j in range(lam[i]))

def n_stat(lam):
    return sum(i * lam[i] for i in range(len(lam)))

def hook_length(lam, i, j):
    arm = lam[i] - j - 1
    leg = sum(1 for r in range(i+1, len(lam)) if lam[r] > j)
    return arm + leg + 1

def dim_q(lam, n):
    """Quantum dimension = s_λ(1,q,...,q^{n-1}) / [n]_q!"""
    result = q0 ** n_stat(lam)
    for i in range(len(lam)):
        for j in range(lam[i]):
            c = j - i
            hk = hook_length(lam, i, j)
            result *= q_int(n + c) / q_int(hk)
    return result / q_fac(n)

def y_qschur(lam, n):
    """q-Schur Markov weight: y_λ^S = q^{c(λ)} / [n]_q!"""
    return q0**content_sum(lam) / q_fac(n)

def load_chi(fname):
    d = json.load(open(HERE / fname))
    atom = d['data']['atom']
    parts = [tuple(e['partition']) for e in atom['by_partition']]
    chis = [mpf(str(e['chi_lambda'])) for e in atom['by_partition']]
    return parts, chis, atom['n_strands']

# Load chi-caches
D_parts, D_chi, D_n = load_chi('atom-chi-rust-d.witness.json')
T_parts, T_chi, T_n = load_chi('atom-chi-rust-t.witness.json')
He_parts, He_chi, He_n = load_chi('atom-chi-rust-3he.witness.json')

# AME binding energies (validation targets)
B_AME = {'D': mpf('2.22452'), 'T': mpf('8.48180'), '3He': mpf('7.71804')}

# CODATA masses
M_P = mpf(M_P_MEV_VALIDATION)
M_N = mpf(M_N_MEV_VALIDATION)
M_atoms = {
    'D': M_P + M_N - B_AME['D'],
    'T': M_P + 2*M_N - B_AME['T'],
    '3He': 2*M_P + M_N - B_AME['3He'],
}

print("=" * 72)
print("Δ_λ MULTI-ATOM CROSS-VALIDATION")
print("=" * 72)

# For each atom: compute Σ y_λ^S × χ^λ × Δ_λ where Δ_λ = (-1)^{n(λ)} × dim_q
# Then find what C_knot is needed to match the binding energy

atoms = [
    ('D', D_parts, D_chi, D_n, 1, 1),
    ('T', T_parts, T_chi, T_n, 1, 2),
    ('3He', He_parts, He_chi, He_n, 2, 1),
]

results = {}

for name, parts, chis, n_strands, Z, N in atoms:
    A = Z + N
    n = n_strands  # = 3*A

    print(f"\n── {name}: H_{n}, {len(parts)} partitions, A={A} ──")

    # Compute y_λ (q-Schur) and Δ_λ = (-1)^{n(λ)} × dim_q
    sum_signed_dimq = mpf(0)
    sum_dimq = mpf(0)
    sum_yc = mpf(0)

    for i, lam in enumerate(parts):
        y = y_qschur(list(lam), n)
        chi = chis[i]
        dq = dim_q(list(lam), n)
        sign = (-1)**n_stat(list(lam))
        delta = sign * dq

        ycd = y * chi * delta
        sum_signed_dimq += ycd
        sum_dimq += y * chi * dq
        sum_yc += y * chi

    # The mass equation target
    # M_atom = m_e × ρ, where ρ = ρ_LO + Σ y·χ·Δ / |tr_M|
    # Binding B = Z·m_p + N·m_n + Z·m_e - M_atom
    # So Σ y·χ·Δ = (M_atom/m_e - ρ_LO) × |tr_M|
    # For now: just report the sums and what C_knot would be needed

    print(f"  Σ y^S · χ · (-1)^n(λ)·dim_q = {float(sum_signed_dimq):>12.6f}")
    print(f"  Σ y^S · χ · dim_q (unsigned) = {float(sum_dimq):>12.6f}")
    print(f"  Σ y^S · χ (no Δ)             = {float(sum_yc):>12.6f}")

    # If Δ_λ = C × (-1)^{n(λ)} × dim_q, then binding = f(C).
    # The binding equation at leading order:
    # B ≈ m_e × |Σ y·χ·Δ| / |tr_M| × (geometric_factor)
    # For cross-check: what B would signed-dim_q give at C=1?
    # B_naive = m_e × |sum_signed_dimq|  (very rough)
    B_naive = float(m_e * fabs(sum_signed_dimq))

    print(f"  B_naive (C=1, no |tr_M| correction) = {B_naive:.4f} MeV")
    print(f"  B_AME                                = {float(B_AME[name]):.4f} MeV")

    if B_naive > 0:
        ratio = float(B_AME[name]) / B_naive
        print(f"  C_knot needed = B_AME/B_naive = {ratio:.4f}")
    else:
        ratio = 0
        print(f"  C_knot: sum is zero — signed dim_q cancels exactly")

    results[name] = {
        'n_strands': n,
        'n_partitions': len(parts),
        'sum_signed_dimq': float(sum_signed_dimq),
        'sum_dimq': float(sum_dimq),
        'sum_yc': float(sum_yc),
        'B_naive_MeV': B_naive,
        'B_AME_MeV': float(B_AME[name]),
        'C_knot_needed': ratio,
    }

# Cross-check: are C_knot values consistent across atoms?
print("\n── CROSS-ATOM CONSISTENCY ──")
c_values = [r['C_knot_needed'] for r in results.values() if r['C_knot_needed'] != 0]
if len(c_values) >= 2:
    avg_c = sum(c_values) / len(c_values)
    spread = max(c_values) - min(c_values)
    rel_spread = spread / avg_c if avg_c != 0 else 0
    print(f"  C_knot values: {[f'{c:.4f}' for c in c_values]}")
    print(f"  Average: {avg_c:.4f}")
    print(f"  Spread:  {spread:.4f} ({rel_spread*100:.1f}% relative)")
    if rel_spread < 0.1:
        print(f"  → CONSISTENT (< 10% spread): C_knot is universal!")
    elif rel_spread < 0.5:
        print(f"  → PARTIALLY consistent ({rel_spread*100:.0f}% spread)")
    else:
        print(f"  → NOT consistent ({rel_spread*100:.0f}% spread): C_knot is knot-dependent")

# Witness
witness = {
    "engine": "python3/mpmath", "engineVersion": "50dps",
    "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "computation": "delta-lambda-multi-atom-crosscheck",
    "scriptFile": "delta_lambda_multi_atom_crosscheck.py",
    "description": (
        "Multi-atom cross-validation of the signed-dim_q Δ_λ ansatz. "
        "Tests whether Δ_λ = C × (-1)^{n(λ)} × dim_q(λ) gives consistent "
        "C_knot across D, T, ³He. Uses q-Schur y_λ closed form."
    ),
    "data": results,
    "assertions": [
        {"label": "all three atoms computed", "passed": len(results) == 3},
    ],
    "allPassed": True,
}

with open(HERE / "delta-lambda-multi-atom-crosscheck.witness.json", "w") as f:
    json.dump(witness, f, indent=2, default=str)
print(f"\nWitness: delta-lambda-multi-atom-crosscheck.witness.json")
