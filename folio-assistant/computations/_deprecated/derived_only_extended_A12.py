#!/usr/bin/env python3
"""
EXTEND derived-only formula to A=5..12 using pyhecke speedup.

The merged branch's pyhecke gives canonical Markov trace 282,329x
faster than the symbolic baseline.  Combined with my derived-only
formula (per-generator inter-gen direct Phi extraction, which was
already fast), I can extend predictions to higher A.

This script:
  1. Computes derived-only formula for A = 1..12 (D through 12C).
  2. Computes canonical pyhecke tr_M for each (independent check).
  3. Reports atomic mass + binding errors against AME.
  4. Identifies which A's the formula extends well to.

For comparison with the conjectural Term 7 (shell correction) at
A >= 5: see conj:shell-correction-term-seven.
"""
from __future__ import annotations
import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone
import time

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

import mpmath as mp
mp.mp.dps = 30

from hecke_core import (h as H_A_F, z as Z_MARKOV, _step_chain_generic)
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
H_A = Q0 - QI
me = mp.mpf(str(M_E_MEV))
z_m = mp.mpf(str(float(Z_MARKOV)))
G = mp.catalan
alpha_bind = me * 8 * G
q3_q = Q0**2 + 1 + QI**2
q2_q = Q0 + QI
HA2 = H_A**2
Wigner_unit = me * q3_q * q2_q**2


def chain_lambda_sym(chain):
    out = mp.mpf(1)
    for c, d in chain: out *= mp.mpf(c)*Q0 + mp.mpf(d)
    return out
def chain_lambda_alt(chain):
    out = mp.mpf(1)
    for c, d in chain: out *= -mp.mpf(c)/Q0 + mp.mpf(d)
    return out
def chain_std_zb(chain):
    a, b = mp.mpf(0), mp.mpf(1)
    for c, d in chain:
        cm, dm = mp.mpf(c), mp.mpf(d)
        a, b = a*(cm*H_A + dm) + b*cm, a*cm + b*dm
    return z_m * a + b
def chain_det(chain):
    D = mp.mpf(1)
    for c, d in chain:
        cm, dm = mp.mpf(c), mp.mpf(d)
        D *= (dm*(cm*H_A + dm) - cm*cm)
    return D
def per_gen_chains_full(Z, N):
    A = Z + N
    n_gens = max(1, 3*A - 1)
    ordering = ['p']*Z + ['n']*N
    gens = [[] for _ in range(n_gens)]
    for k in range(A):
        chain_k = _step_chain_generic(ordering[k], ordering[:k], n_gens, include_inter=True)
        for c, d, g in chain_k:
            gens[g].append((c, d))
    return gens
def phi_inter_gen(Z, N):
    A = Z + N
    chains = per_gen_chains_full(Z, N)
    inter_gens = [3*k + 2 for k in range(A - 1)]
    s1, s2, s3 = mp.mpf(0), mp.mpf(0), mp.mpf(0)
    for g_idx in inter_gens:
        if g_idx >= len(chains): continue
        ch = chains[g_idx]
        if not ch: continue
        v = chain_std_zb(ch); d = chain_det(ch)
        ls = chain_lambda_sym(ch); la = chain_lambda_alt(ch)
        if v != 0: s1 += mp.log(mp.fabs(v))
        if d != 0: s2 += mp.log(mp.fabs(d))
        if ls != 0 and la != 0: s3 += mp.log(mp.fabs(ls/la))
    return s1, s2, s3


# Try to use pyhecke for canonical tr_M
try:
    import pyhecke
    HAVE_PYHECKE = True
except Exception:
    HAVE_PYHECKE = False


def canonical_tr_M(Z, N, include_inter=True, precision=30):
    if not HAVE_PYHECKE:
        return None, None
    t0 = time.time()
    try:
        tr = pyhecke.trace.markov_trace_symbolic_eval(
            Z, N, include_inter, 1, 1, 1, float(Q0), precision=precision)
        return float(tr.real if hasattr(tr, 'real') else tr), time.time() - t0
    except Exception:
        return None, time.time() - t0


def main():
    print("=" * 100)
    print("EXTEND derived-only formula to A=1..12 (using merged pyhecke)")
    print("=" * 100)
    print()

    AME_BIND = {
        'D':    2.22456612, 'T':    8.481798,
        '³He':  7.718058,   '⁴He':  28.29566,
        '⁶Li':  31.99405,   '⁷Li':  39.24454,
        '⁹Be':  58.16498,   '¹⁰B':  64.75077,
        '¹²C':  92.16175,
    }
    M_H_ATOMIC = M_P_MEV + M_E_MEV
    ISOTOPES = [
        ('p (1H)', 1, 0, M_H_ATOMIC, 0.0),
        ('n',      0, 1, M_N_MEV,    0.0),
        ('D',      1, 1, 1876.12393, AME_BIND['D']),
        ('T',      1, 2, 2809.43215, AME_BIND['T']),
        ('³He',    2, 1, 2809.41347, AME_BIND['³He']),
        ('⁴He',    2, 2, 3728.40133, AME_BIND['⁴He']),
        ('⁶Li',    3, 3, 5603.05181, AME_BIND['⁶Li']),
        ('⁷Li',    3, 4, 6535.36652, AME_BIND['⁷Li']),
        ('⁹Be',    4, 5, 8394.79570, AME_BIND['⁹Be']),
        ('¹⁰B',    5, 5, 9326.43680, AME_BIND['¹⁰B']),
        ('¹²C',    6, 6, 11177.92900, AME_BIND['¹²C']),
    ]

    print(f"  pyhecke available: {HAVE_PYHECKE}")
    print()
    print(f"  {'iso':<8} {'A':>2} {'M_pred':>10} {'CODATA':>10} {'M err':>9} "
          f"{'B_pred':>10} {'AME':>10} {'B err':>10} "
          f"{'pyhecke tr_M':>14} {'dt':>7}")
    rows = []
    for name, Z, N, M_ref, B_ame in ISOTOPES:
        A = Z + N
        # Derived-only formula
        P1, P2, P3 = phi_inter_gen(Z, N)
        binding = float(alpha_bind) * (float(P1) - 2*float(q3_q)*float(P2) + float(HA2)*float(P3))
        delta_W = (-float(Wigner_unit) * (min(Z,N)/A)
                     if (A >= 2 and Z >= 1 and N >= 1) else 0.0)
        n_pp = Z*(Z-1)//2; n_nn = N*(N-1)//2
        delta_T1 = (-float(Wigner_unit) * ((n_pp + n_nn)/A)
                      if (A >= 2 and (n_pp + n_nn) > 0) else 0.0)
        M_free = Z*M_P_MEV + N*M_N_MEV + Z*M_E_MEV
        M_pred = M_free + binding + delta_W + delta_T1
        err_M = (M_pred - M_ref) / M_ref * 100
        B_pred = -(binding + delta_W + delta_T1)
        err_B = ((B_pred - B_ame) / B_ame * 100) if B_ame != 0 else 0.0

        # Canonical tr_M via pyhecke
        tr_str = "  --  "
        dt_str = "  --  "
        if HAVE_PYHECKE and A >= 1:
            tr, dt = canonical_tr_M(Z, N, include_inter=(A >= 2))
            if tr is not None:
                tr_str = f"{tr:+.4e}"
                dt_str = f"{dt:5.3f}s"

        print(f"  {name:<8} {A:>2} {M_pred:>10.3f} {M_ref:>10.3f} {err_M:>+8.3f}% "
              f"{B_pred:>+10.3f} {B_ame:>10.3f} {err_B:>+9.2f}% "
              f"{tr_str:>14} {dt_str:>7}")
        rows.append({
            'iso': name, 'Z': Z, 'N': N, 'A': A,
            'M_pred_MeV': M_pred, 'M_codata_MeV': M_ref,
            'B_pred_MeV': B_pred, 'B_AME_MeV': B_ame,
            'err_M_pct': err_M, 'err_B_pct': err_B,
            'pyhecke_tr_M': tr_str.strip(),
        })

    witness = {
        'computation': 'derived-only-extended-A12',
        'description': (
            'Extend derived-only formula to A=1..12 using pyhecke speedup '
            'for canonical Markov trace cross-check.  Tests how far the '
            'formula extends naturally and where Term 7 shell correction '
            'becomes critical.'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'have_pyhecke': HAVE_PYHECKE,
        'isotopes': rows,
    }
    out = Path(__file__).parent / "derived-only-extended-A12.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
