#!/usr/bin/env python3
"""
C-H bond from LP dual: check if C×H unbonded product is LP-stable.

If the product violates Frobenius Gx ≥ 0, covalent crossings are
REQUIRED — same mechanism as the gluon.

Then scan crossing operators to find the minimum-crossing restoration.

Usage:
    cd computations
    python3 ch-bond-lp.py
"""

import math
import itertools
import numpy as np
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0, HA as h, q_int
# z/NF_BASIS/TR_M now owned by pyhecke.gram (M2b inversion). Keep local
# bootstrap for dev mode; the installed-pyhecke path is preferred.
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parents[2] / "tools" / "pyhecke" / "python"))
from pyhecke.gram import z as _PG_Z, NF_BASIS as _PG_NF_BASIS, TR_M as _PG_TR_M  # noqa: E402


z = _PG_Z  # moved to pyhecke.gram
NF_BASIS = _PG_NF_BASIS  # moved to pyhecke.gram
NF_NAMES = ["γ", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]
TR_M = np.array([1.0, z, z, z**2, z**2, z**3])

TWO_Q = q0 + qi0
from hecke_core import alpha_em, E_MOL as E_mol


def hecke_mul(nf, c, d, gen):
    r = [0.0]*6
    if gen == 0:
        tables = [(0,[(1,c),(0,d)]),(1,[(1,c*h),(0,c),(1,d)]),(2,[(3,c),(2,d)]),(3,[(3,c*h),(2,c),(3,d)]),(4,[(5,c),(4,d)]),(5,[(5,c*h),(4,c),(5,d)])]
    else:
        tables = [(0,[(2,c),(0,d)]),(1,[(4,c),(1,d)]),(2,[(2,c*h),(0,c),(2,d)]),(3,[(5,c),(3,d)]),(4,[(4,c*h),(1,c),(4,d)]),(5,[(5,c*h),(3,c),(5,d)])]
    for si, tgts in tables:
        if abs(nf[si]) < 1e-15: continue
        for ti, co in tgts: r[ti] += nf[si] * co
    return r


def nf_trace(nf):
    return sum(nf[i] * TR_M[i] for i in range(6))


# Gram matrix
def hecke_mul_dict(t1, t2):
    result = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            w = w1 + w2
            result[w] = result.get(w, 0.0) + c1 * c2
    return {w: c for w, c in result.items() if abs(c) > 1e-15}

def reduce_nf_dict(terms):
    changed = True
    while changed:
        changed = False
        new_terms = {}
        for word, coeff in terms.items():
            if abs(coeff) < 1e-15: continue
            done = False
            for pos in range(len(word) - 1):
                if word[pos] == word[pos + 1]:
                    i = word[pos]
                    pre, suf = word[:pos], word[pos + 2:]
                    new_terms[pre+(i,)+suf] = new_terms.get(pre+(i,)+suf, 0.0) + coeff*h
                    new_terms[pre+suf] = new_terms.get(pre+suf, 0.0) + coeff
                    done = changed = True; break
            if done: continue
            for pos in range(len(word) - 2):
                a, b, c = word[pos], word[pos+1], word[pos+2]
                if a == c and abs(a-b) == 1:
                    nt = (b,a,b)
                    if nt < (a,b,a):
                        nw = word[:pos]+nt+word[pos+3:]
                        new_terms[nw] = new_terms.get(nw, 0.0) + coeff
                        done = changed = True; break
            if not done:
                new_terms[word] = new_terms.get(word, 0.0) + coeff
        terms = {w: c for w, c in new_terms.items() if abs(c) > 1e-15}
    return terms

def to_vec(terms):
    return np.array([terms.get(b, 0.0) for b in NF_BASIS])

G = np.zeros((6, 6))
for i in range(6):
    for j in range(6):
        prod = hecke_mul_dict({NF_BASIS[i]: 1.0}, {NF_BASIS[j]: 1.0})
        nf = reduce_nf_dict(prod)
        vec = to_vec(nf)
        G[i, j] = sum(vec[k] * TR_M[k] for k in range(6))


def check_frob(nf, label=""):
    x = np.array(nf)
    Gx = G @ x
    viol = [(i, Gx[i]) for i in range(6) if Gx[i] < -1e-10]
    tr = nf_trace(nf)
    Phi = math.log(abs(tr)) if abs(tr) > 1e-300 else float('inf')
    if label:
        print(f"  {label}")
        print(f"    tr_M = {tr:.6e}, Phi_1 = {Phi:.6f}, net = {sum(nf):.6f}")
        for i in range(6):
            s = "✗" if Gx[i] < -1e-10 else "✓"
            print(f"    Gx[{NF_NAMES[i]}] = {Gx[i]:+.6e} {s}")
        print(f"    LP stable: {'YES' if not viol else 'NO'}")
    return len(viol) == 0, Gx, tr, Phi


# ══════════════════════════════════════════════════════════════
# Build atoms
# ══════════════════════════════════════════════════════════════

def build_proton():
    nf = [1.0,0,0,0,0,0]
    for _ in range(3):
        nf = hecke_mul(nf, 1, 0, 0)
        nf = hecke_mul(nf, 1, -h, 1)
    nf = hecke_mul(nf, 1, 0, 0)
    nf = hecke_mul(nf, 1, -h/2, 1)
    nf = hecke_mul(nf, 1, -h/2, 0)
    nf = hecke_mul(nf, 1, 0, 0)
    nf = hecke_mul(nf, 1, 0, 0)
    return nf

def build_neutron():
    nf = [1.0,0,0,0,0,0]
    for _ in range(3):
        nf = hecke_mul(nf, 1, 0, 0)
        nf = hecke_mul(nf, 1, -h, 1)
    nf = hecke_mul(nf, 1, 0, 0)
    nf = hecke_mul(nf, 1, -h/2, 1)
    nf = hecke_mul(nf, 1, -h/2, 0)
    for _ in range(4):
        nf = hecke_mul(nf, 1, 0, 0)
    return nf

def apply_nucleon(nf, is_proton):
    if is_proton:
        for _ in range(3):
            nf = hecke_mul(nf, 1, 0, 0)
            nf = hecke_mul(nf, 1, -h, 1)
        nf = hecke_mul(nf, 1, 0, 0)
        nf = hecke_mul(nf, 1, -h/2, 1)
        nf = hecke_mul(nf, 1, -h/2, 0)
        nf = hecke_mul(nf, 1, 0, 0)
        nf = hecke_mul(nf, 1, 0, 0)
    else:
        for _ in range(3):
            nf = hecke_mul(nf, 1, 0, 0)
            nf = hecke_mul(nf, 1, -h, 1)
        nf = hecke_mul(nf, 1, 0, 0)
        nf = hecke_mul(nf, 1, -h/2, 1)
        nf = hecke_mul(nf, 1, -h/2, 0)
        for _ in range(4):
            nf = hecke_mul(nf, 1, 0, 0)
    return nf

def build_atom(Z, N):
    nf = [1.0,0,0,0,0,0]
    pc, nc = 0, 0
    for k in range(Z+N):
        is_p = (k%2==0 and pc<Z) or nc>=N
        nf = apply_nucleon(nf, is_p)
        if is_p: pc += 1
        else: nc += 1
    for _ in range(Z):
        nf = hecke_mul(nf, 1, -h, 1)
    return nf

def apply_atom(nf, Z, N):
    pc, nc = 0, 0
    for k in range(Z+N):
        is_p = (k%2==0 and pc<Z) or nc>=N
        nf = apply_nucleon(nf, is_p)
        if is_p: pc += 1
        else: nc += 1
    for _ in range(Z):
        nf = hecke_mul(nf, 1, -h, 1)
    return nf


# ══════════════════════════════════════════════════════════════
# C-H system
# ══════════════════════════════════════════════════════════════

OPS = [
    ("σ₀",  0, 1.0, 0.0),
    ("σ₁",  1, 1.0, 0.0),
    ("σ₀⁻¹",0, 1.0, -h),
    ("σ₁⁻¹",1, 1.0, -h),
]

print("=" * 70)
print("C-H BOND FROM LP DUAL")
print("=" * 70)
print(f"q = {q0:.10f}, h = {h:.10f}")
print(f"E_mol = {E_mol:.4f} eV")
print()

# Isolated atoms
nf_C = build_atom(6, 6)
nf_H = build_atom(1, 0)

print("--- Isolated atoms ---")
check_frob(nf_C, "C(6,6)")
print()
check_frob(nf_H, "H(1,0)")
print()

# Unbonded C×H product
nf_CH_unbonded = apply_atom(list(nf_C), 1, 0)
print("--- Unbonded C×H product ---")
stable_ub, Gx_ub, tr_ub, Phi_ub = check_frob(nf_CH_unbonded, "C × H (no bond)")
print()

# ══════════════════════════════════════════════════════════════
# Scan bond operators: which RESTORE or IMPROVE Frobenius?
# ══════════════════════════════════════════════════════════════

print("=" * 70)
print("SCAN: bond operators n = 1..4")
print("=" * 70)

for n in range(1, 5):
    print(f"\n--- n = {n} crossings ---")

    results = []
    for ops in itertools.product(OPS, repeat=n):
        nf = list(nf_C)
        for name, gen, c, d in ops:
            nf = hecke_mul(nf, c, d, gen)
        nf = apply_atom(nf, 1, 0)

        x = np.array(nf)
        Gx = G @ x
        tr = nf_trace(nf)
        Phi = math.log(abs(tr)) if abs(tr) > 1e-300 else float('inf')
        n_viol = sum(1 for v in Gx if v < -1e-10)
        min_Gx = min(Gx)
        bind = Phi_ub - Phi
        E = bind * E_mol
        label = ",".join(o[0] for o in ops)

        results.append({
            'ops': label, 'tr': tr, 'Phi': Phi,
            'bind': bind, 'E': E,
            'stable': n_viol == 0, 'n_viol': n_viol,
            'min_Gx': min_Gx,
        })

    # Sort: stable first, then by minimum trace (most bound)
    results.sort(key=lambda r: (-int(r['stable']), r['Phi']))

    n_stable = sum(1 for r in results if r['stable'])
    print(f"  {n_stable}/{len(results)} Frobenius-feasible")
    print()
    print(f"  {'Operator':>28} {'stable':>6} {'min(Gx)':>10} {'tr_M':>12} "
          f"{'Phi_1':>10} {'binding':>10} {'E(eV)':>10}")
    print("  " + "-" * 90)

    for r in results[:8]:
        s = "YES" if r['stable'] else "no"
        print(f"  {r['ops']:>28} {s:>6} {r['min_Gx']:>10.4f} {r['tr']:>12.4e} "
              f"{r['Phi']:>10.4f} {r['bind']:>10.6f} {r['E']:>10.4f}")

# ══════════════════════════════════════════════════════════════
# Summary: the LP-selected C-H bond
# ══════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"\n  Unbonded C×H: Phi_1 = {Phi_ub:.6f}, tr_M = {tr_ub:.6e}")
print(f"  Frobenius stable: {'YES' if stable_ub else 'NO'}")
print()
print(f"  Observed D₀(C-H) = 4.48 eV")
print(f"  Bond formation is EXOTHERMIC → bonded Phi_1 < unbonded Phi_1")
print()

# Find the LP-optimal: Frobenius-feasible + minimum Phi_1
all_results = []
for n in range(1, 5):
    for ops in itertools.product(OPS, repeat=n):
        nf = list(nf_C)
        for name, gen, c, d in ops:
            nf = hecke_mul(nf, c, d, gen)
        nf = apply_atom(nf, 1, 0)
        x = np.array(nf)
        Gx = G @ x
        tr = nf_trace(nf)
        Phi = math.log(abs(tr)) if abs(tr) > 1e-300 else float('inf')
        n_viol = sum(1 for v in Gx if v < -1e-10)
        bind = Phi_ub - Phi
        E = bind * E_mol
        label = ",".join(o[0] for o in ops)
        all_results.append({
            'n': n, 'ops': label, 'Phi': Phi, 'bind': bind,
            'E': E, 'stable': n_viol == 0, 'tr': tr,
        })

# Among Frobenius-feasible, find min Phi_1 at each n
print("  LP-optimal (Frobenius feasible, min Phi_1) at each n:")
print(f"  {'n':>3} {'Operator':>28} {'Phi_1':>10} {'binding':>10} {'E(eV)':>10}")
print("  " + "-" * 65)

for n in range(1, 5):
    feasible = [r for r in all_results if r['n'] == n and r['stable']]
    if feasible:
        best = min(feasible, key=lambda r: r['Phi'])
        print(f"  {n:>3} {best['ops']:>28} {best['Phi']:>10.4f} "
              f"{best['bind']:>10.6f} {best['E']:>10.4f}")

# Overall best
feasible_all = [r for r in all_results if r['stable'] and r['bind'] > 0]
if feasible_all:
    best = max(feasible_all, key=lambda r: r['bind'])
    print(f"\n  BEST: n={best['n']}, ops={best['ops']}")
    print(f"    Phi_1 = {best['Phi']:.6f}")
    print(f"    binding = {best['bind']:.6f}")
    print(f"    E = {best['E']:.4f} eV (obs: 4.48 eV)")
    print(f"    error = {(best['E']/4.48 - 1)*100:+.1f}%")


# ══════════════════════════════════════════════════════════════
#  SDP LIFT VALIDATION  (see sdp_moment_lift.py / docs/ilp-sdp-audit.md)
# ══════════════════════════════════════════════════════════════
print(f"\n{'=' * 70}\n  SDP LIFT VALIDATION\n{'=' * 70}")
try:
    from sdp_moment_lift import lp_vs_sdp_report
    import numpy as _np
    # Markov-trace basis vector (matches NF_BASIS above)
    _z = 1.0 / (q0**0.5 + qi0**0.5)
    _tr_m = _np.array([1.0, _z, _z, _z**2, _z**2, _z**3])
    _rep = lp_vs_sdp_report(
        c=_tr_m, G=G, A_eq=_np.ones((1, 6)),
        b_eq=_np.array([1.0]),
        label="ch-bond/unit-net")
    for _l in _rep.summary_lines():
        print(_l)
except ImportError as _e:
    print(f"  (cvxpy not available: {_e})")
except Exception as _e:
    print(f"  (SDP lift failed: {_e})")
