#!/usr/bin/env python3
"""
28a: Per-transition α catalog across β-decays.

Build the α(transition) catalog for n→p, T→³He, ⁶He→⁶Li, ¹⁴C→¹⁴N,
⁴⁰K→⁴⁰Ca, ⁸B→⁸Be(β⁺), looking for a structural pattern.

Approach for each transition:
  1. Compute closed-form baseline via branching factorization
       Q_closed = a^Z · b^{N-1} · (a − b) · m_e
     where a, b are the per-nucleon NF channel sums.
  2. Compute residual = Q_codata − Q_closed.
  3. For each rank r, the implied α (assuming pure tail correction):
       α_r = residual / (m_e · |(q;q)_r|)
  4. Tabulate (transition, Q_codata, Q_closed, α_r at r=4..8).

Patterns to look for:
  - α_r constant in r for some transitions?
  - α_r scaling with A, Z, N, N−Z?
  - α_r related to a^Z · b^{N-1} factors?
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
Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
m_e = mp.mpf("0.51099895")
h = Q0 - QI

def qint(n): return (Q0**n - QI**n)/(Q0 - QI)
def qpoch(n):
    out = mp.mpf(1)
    for k in range(1, n+1): out *= (1 - Q0**k)
    return out

# Per-nucleon channel sums (from tritium-qvalue-symbolic + neutron-qvalue-symbolic)
# These are the "spectator normalization" a, b
a_pn = -h/2    # proton spectator (matches both n-qvalue and tritium)
b_pn = -3*(Q0**2 - 1)*(Q0**2 + 1)**2 / (4*Q0**3)  # neutron spectator (from tritium)

print(f"a (proton spectator) = {float(a_pn):.6f}")
print(f"b (neutron spectator) = {float(b_pn):.6f}")
print(f"a − b = {float(a_pn - b_pn):.6f}")
print()


# β⁻ transitions: parent (Z, N) → daughter (Z+1, N-1)
# Q_codata in MeV from AME 2020
TRANSITIONS = [
    # label, Z_parent, N_parent, Q_codata_MeV
    ("n → p",          0, 1,   "0.78233341"),
    ("³H → ³He",        1, 2,   "0.018592"),
    ("⁶He → ⁶Li",       2, 4,   "3.5077"),
    ("¹⁴C → ¹⁴N",       6, 8,   "0.156476"),
    ("¹⁰Be → ¹⁰B",      4, 6,   "0.5560"),
    ("²²Na → ²²Ne (β⁺)",11,11,  "1.8204"),  # treated by symmetry
    ("⁴⁰K → ⁴⁰Ca",     19, 21,  "1.31109"),
]


def Q_branching(Z, N):
    """Branching-factorization closed form: Q = a^Z · b^{N-1} · (a-b) · m_e."""
    if N < 1:
        return mp.mpf(0)  # no neutron to flip
    return a_pn**Z * b_pn**(N-1) * (a_pn - b_pn) * m_e


# For n→p, the framework uses a different conversion (m_e/(q(q-1)) factor)
# Per neutron-qvalue-symbolic.md.  The branching factorization Q above
# may not match for n→p directly; let's check:
print("=" * 110)
print("Branching factorization closed forms vs CODATA")
print("=" * 110)
print(f"  {'transition':<22} {'Z':>3} {'N':>3} {'Q_branching':>14} {'Q_codata':>12} {'err %':>10}")
print("-" * 110)
for label, Z, N, Q_str in TRANSITIONS:
    Q_codata = mp.mpf(Q_str)
    Q_br = Q_branching(Z, N)
    err = (Q_br - Q_codata)/Q_codata if Q_codata != 0 else mp.mpf(0)
    print(f"  {label:<22} {Z:>3} {N:>3} {float(Q_br):>14.6f} {float(Q_codata):>12.6f} {float(err)*100:>+10.2f}%")
print()

# Per-rank α catalog
print("=" * 110)
print("Per-transition fitted α at each rank: residual / (m_e·|(q;q)_r|)")
print("=" * 110)
print(f"  {'transition':<22} {'residual MeV':>14} {'α at r=3':>10} {'α r=4':>9} {'α r=5':>9} {'α r=6':>9} {'α r=7':>9}")
print("-" * 110)

results = []
for label, Z, N, Q_str in TRANSITIONS:
    Q_codata = mp.mpf(Q_str)
    Q_br = Q_branching(Z, N)
    residual = Q_codata - Q_br
    alphas = {}
    for r in range(3, 9):
        qpr = abs(qpoch(r))
        if qpr > 1e-30:
            alphas[r] = float(residual / (m_e * qpr))
        else:
            alphas[r] = float('nan')
    print(f"  {label:<22} {float(residual):>+14.6f} {alphas[3]:>+10.4f} {alphas[4]:>+9.4f} {alphas[5]:>+9.4f} {alphas[6]:>+9.4f} {alphas[7]:>+9.4f}")
    results.append({
        "transition": label, "Z": Z, "N": N, "A": Z+N,
        "Q_codata_MeV": float(Q_codata),
        "Q_branching_MeV": float(Q_br),
        "residual_MeV": float(residual),
        "alpha_at_rank": alphas
    })

# Look for patterns
print()
print("=" * 110)
print("Pattern analysis")
print("=" * 110)
print("""
Observations:
  - n→p α₄ = 0.827 (was the original fit).
  - For other transitions, the closed form may be inaccurate (Q_branching
    uses tritium-style a, b which may not generalise to higher A).
  - When Q_branching is close to Q_codata, residual is small and α_r is small.
  - When Q_branching is far from Q_codata (e.g., n→p above), residual is large.

For pattern hunting, look at:
  1. α_r/A: does it scale with mass number?
  2. α_r/(N−Z): isospin scaling?
  3. α_r/Q_codata: relative magnitude
""")

for r in [4]:
    print(f"At rank r={r}:")
    print(f"  {'transition':<22} {'α':>10} {'α/A':>10} {'α/(N−Z)':>10} {'α/Q_codata':>14}")
    for res in results:
        a = res['alpha_at_rank'][r]
        A = res['A']; NmZ = res['N'] - res['Z']; Q = res['Q_codata_MeV']
        a_over_A = a/A if A != 0 else float('nan')
        a_over_NmZ = a/NmZ if NmZ != 0 else float('inf')
        a_over_Q = a/Q if Q != 0 else float('nan')
        print(f"  {res['transition']:<22} {a:>+10.4f} {a_over_A:>+10.4f} {a_over_NmZ:>+10.4f} {a_over_Q:>+14.4f}")

out = {
    "computation": "alpha-per-transition-catalog",
    "description": ("28a: Per-transition α catalog for β-decay Q-values. "
                    "Computes closed-form Q via branching factorization, "
                    "residual to CODATA, and implied α at each rank.  "
                    "Looks for scaling patterns α(A, Z, N, N-Z, ...)."),
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "a_per_nucleon": float(a_pn),
    "b_per_nucleon": float(b_pn),
    "transitions": results,
    "verdict_pending": "review patterns in α(transition, rank) for structural relation"
}
out_path = Path(__file__).parent / "alpha-per-transition-catalog.witness.json"
with open(out_path, "w") as fp:
    json.dump(out, fp, indent=2)
print(f"\nWitness: {out_path}")
