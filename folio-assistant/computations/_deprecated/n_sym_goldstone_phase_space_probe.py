#!/usr/bin/env python3
"""N_sym candidate (b): Higgs-eaten Goldstone phase space — NEGATIVE PROBE.

This script ENUMERATES 19 candidate Goldstone-product q-arithmetic forms
against the numerical target N_sym(q_0) = 213.111807...

VERDICT: The probe is a structural enumeration only — NOT a derivation.
Best zero-free-parameter form found: [3]_q · [4]_q^3 at 0.87% off. Closer
forms exist with composite (1 + ℏ_q^2) corrections, but searching for
next-order δ₂ corrections is FISHING (per user instruction 2026-05-03;
cf. PR #514 also flagged ansatz-sweeps as multiple-comparisons fitting).

The honest path forward is CATEGORICAL DERIVATION of N_sym from:
   1. The categorical Higgs idempotent e_H : A → A in
      Rep(SU(2)_L × U(1)_Y) — currently unauthored (U2/U4 conjectures
      from PR #511 must be discharged first).
   2. The Frobenius trace of the EW symmetric-channel projector
      e_sym^EW = ⊗_k e_sym^(T(2,2k)) under <·,·>_F.
   3. Compute tr_F(e_sym^EW) as a function of q from first principles.
   4. Evaluate at q_0 and check against 213.11.

This script's role is to provide DATA for that future derivation — NOT
to substitute numerical search for the missing categorical work.
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
import sys as _sys
import mpmath
mpmath.mp.dps = 100

_sys.path.insert(0, str(Path(__file__).parent))
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR
from experimental_constants import M_E_MEV, G_F_MEV

q = mpmath.mpf(Q_50_DIGIT_STR)
hbar_q = (q - 1) / q


def q_int(n):
    if n == 0:
        return mpmath.mpf(0)
    return (q ** n - q ** (-n)) / (q - 1 / q)


def q_factorial(n):
    p = mpmath.mpf(1)
    for k in range(1, n + 1):
        p *= q_int(k)
    return p


# Target value — N_sym(q_0) per the candidate-(a) probe witness
G_F = mpmath.mpf(str(G_F_MEV))
m_e = mpmath.mpf(str(M_E_MEV))
v_weak = 1 / mpmath.sqrt(mpmath.sqrt(2) * G_F)
E_cross = (q - 1 / q) / 2
mu_0 = m_e / (3 * E_cross)
N_v = v_weak / (E_cross * mu_0)
prod_pl = (q_int(4) ** 2 / q_int(2)) * (q_int(6) ** 2 / q_int(2)) * (q_int(8) ** 2 / q_int(2))
N_sym_target = N_v / prod_pl
print(f"target N_sym(q_0) = {mpmath.nstr(N_sym_target, 20)}")
print()

# Candidate (b) — Higgs-eaten Goldstones
# Three eaten Goldstones; per QOU dictionary they live on the W± and Z
# hosts. Try multiple q-dim assignment schemes.

GOLDSTONE_ASSIGNMENTS = {
    "(b1) [4]_q · [4]_q · [6]_q":               q_int(4) * q_int(4) * q_int(6),
    "(b2) [4]_q · [4]_q · [6]_q · [2]_q":       q_int(4) * q_int(4) * q_int(6) * q_int(2),
    "(b3) [4]_q^2 · [6]_q · 2":                 q_int(4) ** 2 * q_int(6) * 2,
    "(b4) [4]_q · [4]_q · [6]_q · [8]_q":       q_int(4) * q_int(4) * q_int(6) * q_int(8),  # +Higgs scalar
    "(b5) [3]_q^3 · [6]_q":                     q_int(3) ** 3 * q_int(6),
    "(b6) [2]_q^2 · [3]_q · [6]_q":             q_int(2) ** 2 * q_int(3) * q_int(6),
    "(b7) [4]_q · [6]_q · [10]_q":              q_int(4) * q_int(6) * q_int(10),
    "(b8) [3]_q · [4]_q^3":                     q_int(3) * q_int(4) ** 3,
    "(b9) [2]_q · [4]_q · [6]_q · [8]_q":       q_int(2) * q_int(4) * q_int(6) * q_int(8),
    "(b10) [3]_q · [4]_q · [5]_q · [6]_q":      q_int(3) * q_int(4) * q_int(5) * q_int(6),
    "(b11) [2]_q · [3]_q · [4]_q^2 · [5]_q":    q_int(2) * q_int(3) * q_int(4) ** 2 * q_int(5),
    "(b12) [2]_q · [4]_q · [5]_q^2":            q_int(2) * q_int(4) * q_int(5) ** 2,
    "(b13) [4]_q · [5]_q · [10]_q":             q_int(4) * q_int(5) * q_int(10),
    "(b14) [3]_q · [4]_q · [5]_q · [3]_q":      q_int(3)**2 * q_int(4) * q_int(5),
    "(b15) [3]_q · [4]_q · [6]_q · [3]_q":      q_int(3)**2 * q_int(4) * q_int(6),
    # 4 mass eigenstates × q-dim:
    "(b16) [4]_q · [4]_q · [6]_q · [8]_q · ½":  q_int(4) ** 2 * q_int(6) * q_int(8) / 2,
    "(b17) [4]_q^2 · [6]_q^2 / [2]_q":          q_int(4) ** 2 * q_int(6) ** 2 / q_int(2),
    "(b18) [3]_q! · [5]_q · [4]_q":             q_factorial(3) * q_int(5) * q_int(4),
    "(b19) [4]_q! / [2]_q":                     q_factorial(4) / q_int(2),
}

# Compute and rank
rows = []
print(f"{'candidate':<55} {'value at q_0':>15} {'rel err vs N_sym %':>20}")
print('-' * 95)
ranked = sorted(
    GOLDSTONE_ASSIGNMENTS.items(),
    key=lambda kv: float(abs(kv[1] - N_sym_target) / N_sym_target),
)
for name, val in ranked:
    rel = abs(val - N_sym_target) / N_sym_target
    flag = " *** CLEAN" if abs(rel) < 1e-3 else (" * close" if abs(rel) < 0.05 else "")
    print(f"  {name:<53} {mpmath.nstr(val, 10):>15} {mpmath.nstr(rel*100, 5):>19}%{flag}")
    rows.append({
        'candidate': name,
        'value': mpmath.nstr(val, 25),
        'rel_err_pct': float(rel) * 100,
    })

# Now fit C(q) for each candidate: C = N_sym / GoldstoneProduct
print()
print("Inferred C(q) factor for each candidate:")
print(f"{'candidate':<55} {'C(q_0) implied':>20}")
print('-' * 80)
for name, val in ranked:
    if val == 0:
        continue
    C_impl = N_sym_target / val
    # Test if C_impl is close to a simple form
    simple_forms = {
        '1':       mpmath.mpf(1),
        '[2]_q':   q_int(2),
        '[3]_q':   q_int(3),
        '[4]_q':   q_int(4),
        '[2]_q²':  q_int(2)**2,
        'q':       q,
        'q²':      q**2,
        'q^3':     q**3,
        '½':       mpmath.mpf('0.5'),
        '⅓':       mpmath.mpf(1)/3,
        '1.0':     mpmath.mpf(1),
    }
    best_match = min(simple_forms.items(), key=lambda kv: abs(C_impl - kv[1]))
    rel_C = abs(C_impl - best_match[1]) / best_match[1] if best_match[1] != 0 else mpmath.inf
    if abs(rel_C) < 0.01:
        print(f"  {name:<53} C ≈ {best_match[0]:<10} ({mpmath.nstr(C_impl, 8)}, {mpmath.nstr(rel_C*100, 5)}% from {best_match[0]}) **")
    elif abs(rel_C) < 0.05:
        print(f"  {name:<53} C ≈ {best_match[0]:<10} ({mpmath.nstr(C_impl, 8)}, {mpmath.nstr(rel_C*100, 5)}% from {best_match[0]})")

# Best fit + verdict
best = ranked[0]
rel_best = abs(best[1] - N_sym_target) / N_sym_target
print()
print(f"Best candidate (b): {best[0]} = {mpmath.nstr(best[1], 12)} ({mpmath.nstr(rel_best*100, 5)}%)")

print()
print("=" * 70)
print("VERDICT:")
print("=" * 70)
if float(rel_best) < 1e-3:
    print(f"  CLOSURE: candidate '{best[0]}' matches N_sym to <0.1%.")
elif float(rel_best) < 0.01:
    print(f"  PROMISING: candidate '{best[0]}' matches to {float(rel_best)*100:.3f}%. Worth deepening.")
else:
    print(f"  NO CLEAN MATCH: best candidate is {float(rel_best)*100:.2f}% off.")
    print(f"  Goldstone-product form alone (without explicit C(q) factor) is")
    print(f"  insufficient. The C(q) vacuum-volume constant must contribute")
    print(f"  meaningfully. See inferred C(q) values above.")

# Witness
out = {
    'computation': 'n-sym-goldstone-phase-space-probe',
    'computedAt': datetime.now(timezone.utc).isoformat(),
    'description': (
        'Probe of conj:n-sym-symmetric-channel-normalization candidate (b) — '
        'Higgs-eaten Goldstone phase space. Tests 19 Goldstone q-dim '
        'assignment schemes against N_sym(q_0) = 213.111807. The 3 broken '
        'EW generators (W±, Z Goldstones) live on the W and Z hosts (genus '
        '1 and 2 respectively per the path-α identification).'
    ),
    'q_0_dps': mpmath.mp.dps,
    'q_0': mpmath.nstr(q, 50),
    'N_sym_target': mpmath.nstr(N_sym_target, 25),
    'candidates': rows,
    'best_candidate': best[0],
    'best_value': mpmath.nstr(best[1], 25),
    'best_rel_err_pct': float(rel_best) * 100,
    'verdict': (
        'closure' if float(rel_best) < 1e-3
        else 'promising' if float(rel_best) < 0.01
        else 'no clean match — C(q) factor needs separate categorical input'
    ),
}
out_path = WitnessBuilder.wrap_legacy("n-sym-goldstone-phase-space-probe", out, script_path=__file__, engine="python").save()
print(f"\n→ wrote {out_path}")
