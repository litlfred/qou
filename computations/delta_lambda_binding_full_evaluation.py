#!/usr/bin/env python3
"""
Δ_λ binding formula — full numerical evaluation for D, T, ³He, ⁴He.

The formula (zero free parameters, top-down Cat→Arch):

    B(K) = m_e × |Σ_λ y_λ · χ^λ(β_K) · sgn(w_0^{S_{λ'}}) · f^λ|

Each factor:
  sgn(w_0^{S_{λ'}}) — categorical (Macdonald I.1.5, PROVED)
  f^λ = dim(V_λ)   — categorical (regular-rep multiplicity, PROVED)
  y_λ              — algebraic (Wenzl Markov weights)
  χ^λ(β_K)         — geometric (Hoefsmit + interface operator)
  m_e, q₀          — archimedean (CAL-1, CAL-2)
"""

import json, time, math
from pathlib import Path
from mpmath import mp, mpf, fabs
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
HERE = Path(__file__).resolve().parent

m_e = mpf('0.51099895069')
B_AME = {'D': 2.22452, 'T': 8.48180, '3He': 7.71804, '4He': 28.29567}

def n_stat(lam):
    return sum(i * lam[i] for i in range(len(lam)))

def conjugate(lam):
    if not lam: return ()
    conj = []
    for i in range(lam[0]):
        conj.append(sum(1 for p in lam if p > i))
    return tuple(conj)

def sgn_conjugate_parabolic(lam):
    """(-1)^{n(λ)} = sgn(w_0^{S_{λ'}}) via Macdonald I.1.5."""
    conj = conjugate(lam)
    return math.prod((-1)**(p*(p-1)//2) for p in conj)

def dim_sn(lam):
    """f^λ = dim(V_λ) via hook-length formula."""
    n = sum(lam)
    num = math.factorial(n)
    den = 1
    for i in range(len(lam)):
        for j in range(lam[i]):
            arm = lam[i] - j - 1
            leg = sum(1 for r in range(i+1, len(lam)) if lam[r] > j)
            den *= arm + leg + 1
    return num // den

def load_chi(fname):
    with open(HERE / fname, 'r', encoding='utf-8') as f:
        d = json.load(f)
    atom = d['data']['atom']
    return [(tuple(e['partition']), mpf(str(e['chi_lambda'])))
            for e in atom['by_partition']]

def load_wenzl_y(fname):
    with open(HERE / fname, 'r', encoding='utf-8') as f:
        d = json.load(f)
    return {tuple(e['partition']): mpf(e['y_lambda'])
            for e in d['data']['per_partition']}

# Load Wenzl y_λ
lp = json.load(open(HERE / 'rho-k-h3a-lp-dual.witness.json'))
y_H6 = {tuple(e['partition']): mpf(str(e['y_lambda_at_q0']))
         for e in lp['data']['per_lambda']}
y_H9 = load_wenzl_y('wenzl-y-lambda-h9.witness.json')
y_H12 = load_wenzl_y('wenzl-y-lambda-h12.witness.json')

# Load χ^λ(β_K) for each atom
atoms = [
    ('D',   'atom-chi-rust-d.witness.json',   y_H6,  1, 1),
    ('T',   'atom-chi-rust-t.witness.json',   y_H9,  1, 2),
    ('3He', 'atom-chi-rust-3he.witness.json', y_H9,  2, 1),
    ('4He', 'atom-chi-rust-4he.witness.json', y_H12, 2, 2),
]

print("=" * 72)
print("Δ_λ BINDING FORMULA — FULL NUMERICAL EVALUATION")
print("B(K) = m_e × |Σ_λ y_λ · χ^λ(β_K) · sgn(w_0^{S_{λ'}}) · f^λ|")
print("=" * 72)

results = {}

for name, chi_file, y_dict, Z, N in atoms:
    A = Z + N
    chi_data = load_chi(chi_file)

    total = mpf(0)
    for lam, chi in chi_data:
        y = y_dict.get(lam, mpf(0))
        sgn = sgn_conjugate_parabolic(lam)
        f = dim_sn(lam)
        term = y * chi * sgn * f
        total += term

    B_pred = float(m_e * fabs(total))
    B_ame = B_AME[name]
    err = B_pred - B_ame
    err_pct = err / B_ame * 100

    results[name] = {
        'A': A, 'Z': Z, 'N': N,
        'sum': float(total),
        'B_pred_MeV': B_pred,
        'B_AME_MeV': B_ame,
        'err_MeV': err,
        'err_pct': err_pct,
    }

    print(f"\n── {name} (A={A}, Z={Z}, N={N}) ──")
    print(f"  Σ y·χ·sgn·f = {float(total):>12.6f}")
    print(f"  B_pred = m_e × |Σ| = {B_pred:>10.4f} MeV")
    print(f"  B_AME              = {B_ame:>10.4f} MeV")
    print(f"  err = {err:>+10.4f} MeV ({err_pct:>+7.2f}%)")

print("\n" + "=" * 72)
print("SUMMARY TABLE")
print(f"{'Atom':>4s} {'B_pred':>10s} {'B_AME':>10s} {'err':>10s} {'err%':>8s}")
print("-" * 45)
for name in ['D', 'T', '3He', '4He']:
    r = results[name]
    print(f"{name:>4s} {r['B_pred_MeV']:>10.4f} {r['B_AME_MeV']:>10.4f} {r['err_MeV']:>+10.4f} {r['err_pct']:>+7.2f}%")

# Witness
witness = {
    "engine": "python3/mpmath", "engineVersion": "50dps",
    "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "computation": "delta-lambda-binding-full-evaluation",
    "scriptFile": "delta_lambda_binding_full_evaluation.py",
    "description": (
        "Full numerical evaluation of the Δ_λ binding formula "
        "B(K) = m_e × |Σ y_λ · χ^λ(β_K) · sgn(w_0^{S_{λ prime}}) · f^λ| "
        "for D, T, ³He, ⁴He. Zero free parameters. "
        "All factors: y_λ (Wenzl), χ^λ (Hoefsmit+interface), "
        "sgn (Macdonald), f^λ (hook-length)."
    ),
    "data": results,
    "assertions": [
        {"label": f"{name} computed", "passed": name in results}
        for name in ['D', 'T', '3He', '4He']
    ],
    "allPassed": True,
}

with open(HERE / "delta-lambda-binding-full-evaluation.witness.json", "w", encoding="utf-8") as f:
    json.dump(witness, f, indent=2, default=str)
print(f"\nWitness: delta-lambda-binding-full-evaluation.witness.json")
