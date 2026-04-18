#!/usr/bin/env python3
"""
Deuteron (D = ²H) error analysis — pure level-3 pair-coupling test.

D has Z=N=1, no shell structure, no pp/nn pairs. Only a pn pair
with m_pn crossings. B_AME = 2.22 MeV tests the pair model directly.
"""
import sys
import math
from pathlib import Path
import mpmath

sys.path.insert(0, str(Path(__file__).parent))
from crt_markov import markov_trace_symbolic_eval
from mass_endomorphism import q0 as q0_f

mpmath.mp.dps = 50
q0 = mpmath.mpf(str(q0_f))
B_AME_D = 2.22  # MeV
E_0_MeV = mpmath.mpf('0.782')


def tr_M_D(m_pn, include_inter=True):
    """|tr_M(W_D)| with variable pn multiplicity."""
    return abs(markov_trace_symbolic_eval(
        1, 1, include_inter, 1, m_pn, 1, q0, precision=50))


# Get baseline |tr_M| values
tr_p = abs(markov_trace_symbolic_eval(1, 0, False, 1, 1, 1, q0, 50))
tr_n = abs(markov_trace_symbolic_eval(0, 1, False, 1, 1, 1, q0, 50))
Q_cat = tr_n - tr_p
E_0_cat = E_0_MeV / abs(Q_cat)

tr_free_D = tr_M_D(m_pn=1, include_inter=False)

print("DEUTERON ERROR ANALYSIS (D = ²H, Z=N=1, pure pn pair)")
print("=" * 72)
print(f"q_0 = {q0}")
print(f"|tr_M(p)|       = {tr_p!s}")
print(f"|tr_M(n)|       = {tr_n!s}")
print(f"|tr_M(free_D)|  = {tr_free_D!s}  (= |tr_M(p)|·|tr_M(n)|: {abs(tr_p*tr_n)!s})")
print(f"E_0_cat         = {E_0_cat!s} MeV/cat.unit")
print(f"B_AME(D)        = {B_AME_D} MeV")
print()
print(f"  {'m_pn':>5} {'|tr_M(W_D)|':>28} {'B_pred (MeV)':>18} {'B_err':>10}")
print("  " + "-" * 72)
for m_pn in range(1, 13):
    tr_atom = tr_M_D(m_pn, include_inter=True)
    B_pred = float(E_0_cat * (tr_free_D - tr_atom))
    B_err = B_pred - B_AME_D
    print(f"  {m_pn:>5d} {tr_atom!s:>28} {B_pred:>18.6f} {B_err:>+10.4f}")
