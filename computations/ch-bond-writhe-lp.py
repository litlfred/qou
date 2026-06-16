#!/usr/bin/env python3
"""
C-H bond: two-level LP dual.

Degree 0: minimize trace (categorical action) → binding exists
Degree 1: minimize writhe → selects which operator

Writhe = algebraic crossing number = Σ exponents.
  σ contributes +1, σ⁻¹ contributes -1.

For each (n, writhe) pair, find min-trace operator and compute binding.

Usage:
    cd computations
    python3 ch-bond-writhe-lp.py
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import math
import itertools
import sys
from pathlib import Path
from mpmath import mp

sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0, HA as h, q_int
from witness_base import WitnessBuilder

z = 1.0 / (q0**0.5 + qi0**0.5)
TR_M = [1.0, z, z, z**2, z**2, z**3]
TWO_Q = q0 + qi0
from hecke_core import alpha_em, E_MOL as E_mol

def hm(nf, c, d, g):
    r = [0.0]*6
    if g == 0:
        t = [(0,[(1,c),(0,d)]),(1,[(1,c*h),(0,c),(1,d)]),(2,[(3,c),(2,d)]),(3,[(3,c*h),(2,c),(3,d)]),(4,[(5,c),(4,d)]),(5,[(5,c*h),(4,c),(5,d)])]
    else:
        t = [(0,[(2,c),(0,d)]),(1,[(4,c),(1,d)]),(2,[(2,c*h),(0,c),(2,d)]),(3,[(5,c),(3,d)]),(4,[(4,c*h),(1,c),(4,d)]),(5,[(5,c*h),(3,c),(5,d)])]
    for si, tgts in t:
        if abs(nf[si]) < 1e-15: continue
        for ti, co in tgts: r[ti] += nf[si] * co
    return r

def tr(nf):
    return sum(nf[i] * TR_M[i] for i in range(6))

def build_atom(Z, N):
    nf = [1,0,0,0,0,0]
    pc, nc = 0, 0
    for k in range(Z+N):
        ip = (k%2==0 and pc<Z) or nc>=N
        if ip:
            for _ in range(3): nf=hm(nf,1,0,0); nf=hm(nf,1,-h,1)
            nf=hm(nf,1,0,0); nf=hm(nf,1,-h/2,1); nf=hm(nf,1,-h/2,0)
            nf=hm(nf,1,0,0); nf=hm(nf,1,0,0); pc+=1
        else:
            for _ in range(3): nf=hm(nf,1,0,0); nf=hm(nf,1,-h,1)
            nf=hm(nf,1,0,0); nf=hm(nf,1,-h/2,1); nf=hm(nf,1,-h/2,0)
            for _ in range(4): nf=hm(nf,1,0,0); nc+=1
    for _ in range(Z): nf=hm(nf,1,-h,1)
    return nf

def apply_atom(nf, Z, N):
    pc, nc = 0, 0
    for k in range(Z+N):
        ip = (k%2==0 and pc<Z) or nc>=N
        if ip:
            for _ in range(3): nf=hm(nf,1,0,0); nf=hm(nf,1,-h,1)
            nf=hm(nf,1,0,0); nf=hm(nf,1,-h/2,1); nf=hm(nf,1,-h/2,0)
            nf=hm(nf,1,0,0); nf=hm(nf,1,0,0); pc+=1
        else:
            for _ in range(3): nf=hm(nf,1,0,0); nf=hm(nf,1,-h,1)
            nf=hm(nf,1,0,0); nf=hm(nf,1,-h/2,1); nf=hm(nf,1,-h/2,0)
            for _ in range(4): nf=hm(nf,1,0,0); nc+=1
    for _ in range(Z): nf=hm(nf,1,-h,1)
    return nf

# Operators with writhe annotation
# σ: writhe +1, σ⁻¹: writhe -1
OPS = [
    ("σ₀",   0, 1.0, 0.0,  +1),
    ("σ₁",   1, 1.0, 0.0,  +1),
    ("σ₀⁻¹", 0, 1.0, -h,   -1),
    ("σ₁⁻¹", 1, 1.0, -h,   -1),
]

print("=" * 70)
print("C-H BOND: TWO-LEVEL LP DUAL")
print("  Degree 0: minimize trace")
print("  Degree 1: minimize writhe")
print("=" * 70)
print(f"q = {q0:.10f}, E_mol = {E_mol:.4f} eV")
print()

nf_C = build_atom(6, 6)
nf_ub = apply_atom(list(nf_C), 1, 0)
tr_ub = tr(nf_ub)
Phi_ub = mp.log(abs(tr_ub))
print(f"Unbonded C×H: tr_M = {tr_ub:.6e}, Phi_1 = {float(Phi_ub):.6f}")
print()

# ══════════════════════════════════════════════════════════════
# Scan all (n, writhe) pairs
# ══════════════════════════════════════════════════════════════

print("=" * 70)
print("(n, writhe) → min-trace operator → binding energy")
print("=" * 70)
print()
print(f"{'n':>3} {'w':>4} {'best operator':>28} {'|tr_M|':>12} "
      f"{'Phi_1':>10} {'bind':>10} {'E(eV)':>10}")
print("-" * 82)

all_data = []

for n in range(1, 5):
    # Group by writhe
    writhe_groups = {}
    for ops in itertools.product(OPS, repeat=n):
        w = sum(o[4] for o in ops)
        if w not in writhe_groups:
            writhe_groups[w] = []

        nf = list(nf_C)
        for name, gen, c, d, _ in ops:
            nf = hm(nf, c, d, gen)
        nf = apply_atom(nf, 1, 0)

        t = tr(nf)
        if abs(t) < 1e-300:
            continue
        Phi = mp.log(abs(t))
        bind = Phi_ub - Phi
        E = bind * E_mol
        label = ",".join(o[0] for o in ops)

        writhe_groups[w].append({
            'ops': label, 'tr': t, 'Phi': Phi,
            'bind': bind, 'E': E, 'abs_tr': abs(t),
        })

    # For each writhe, find min |tr_M|
    for w in sorted(writhe_groups.keys()):
        group = writhe_groups[w]
        # Degree 0: min |tr_M|
        best = min(group, key=lambda r: r['abs_tr'])
        marker = ""
        if 3.5 < best['E'] < 5.5:
            marker = " ←←←"
        print(f"{n:>3} {w:>+4} {best['ops']:>28} {best['abs_tr']:>12.4e} "
              f"{float(best['Phi']):>10.4f} {float(best['bind']):>10.6f} {float(best['E']):>10.4f}{marker}")

        all_data.append({
            'n': n, 'w': w, 'ops': best['ops'],
            'tr': best['tr'], 'Phi': best['Phi'],
            'bind': best['bind'], 'E': best['E'],
        })

# ══════════════════════════════════════════════════════════════
# Degree 1 selection: at each n, which writhe gives correct binding?
# ══════════════════════════════════════════════════════════════

print()
print("=" * 70)
print("DEGREE 1 SELECTION: minimize writhe subject to positive binding")
print("=" * 70)
print()

obs_E = 4.48

for n in range(1, 5):
    n_data = [d for d in all_data if d['n'] == n]
    # Filter: positive binding only
    bound = [d for d in n_data if d['bind'] > 0]
    if not bound:
        print(f"  n={n}: no positive binding at any writhe")
        continue

    # Degree 1: minimize writhe (most negative first)
    bound.sort(key=lambda d: d['w'])
    best_w = bound[0]

    # Also find closest to observed
    closest = min(n_data, key=lambda d: abs(d['E'] - obs_E))

    print(f"  n={n}:")
    print(f"    Min writhe with binding > 0: w={best_w['w']}, "
          f"ops={best_w['ops']}, E={float(best_w['E']):.4f} eV")
    print(f"    Closest to {obs_E} eV:       w={closest['w']}, "
          f"ops={closest['ops']}, E={float(closest['E']):.4f} eV "
          f"(err: {float((closest['E']/obs_E - 1)*100):+.1f}%)")
    print()

# ══════════════════════════════════════════════════════════════
# Apply to all bond types
# ══════════════════════════════════════════════════════════════

print("=" * 70)
print("ALL BOND TYPES: (n, min-writhe) selection")
print("=" * 70)
print()

bond_types = [
    ("H-H", 1, 0, 1, 0, 4.478),
    ("C-H", 6, 6, 1, 0, 4.48),
    ("C-O", 6, 6, 8, 8, 3.70),
    ("C-C", 6, 6, 6, 6, 3.60),
    ("O-H", 8, 8, 1, 0, 4.82),
]

bond_results = {}

for bname, ZA, NA, ZB, NB, obs in bond_types:
    nfA = build_atom(ZA, NA)
    nf_u = apply_atom(list(nfA), ZB, NB)
    tr_u = tr(nf_u)
    Phi_u = mp.log(abs(tr_u)) if abs(tr_u) > 1e-300 else float('inf')

    print(f"--- {bname} ---")

    best_at_n = {}
    for n in range(1, 5):
        writhe_best = {}
        for ops in itertools.product(OPS, repeat=n):
            w = sum(o[4] for o in ops)
            nf = list(nfA)
            for name, gen, c, d, _ in ops:
                nf = hm(nf, c, d, gen)
            nf = apply_atom(nf, ZB, NB)
            t = tr(nf)
            if abs(t) < 1e-300: continue
            Phi = mp.log(abs(t))
            bind = Phi_u - Phi
            E = bind * E_mol
            label = ",".join(o[0] for o in ops)

            if w not in writhe_best or abs(t) < writhe_best[w]['abs_tr']:
                writhe_best[w] = {
                    'ops': label, 'tr': t, 'abs_tr': abs(t),
                    'Phi': Phi, 'bind': bind, 'E': E, 'w': w,
                }

        # At this n: min writhe with positive binding
        bound = [v for v in writhe_best.values() if v['bind'] > 0]
        if bound:
            bound.sort(key=lambda d: d['w'])  # min writhe
            best_at_n[n] = bound[0]

    # Select: smallest n with positive binding at min writhe
    if best_at_n:
        first_n = min(best_at_n.keys())
        sel = best_at_n[first_n]
        bond_results[bname] = sel
        print(f"  LP selects: n={first_n}, w={sel['w']}, ops={sel['ops']}")
        print(f"    E = {float(sel['E']):.4f} eV (obs: {obs:.2f}, err: {float((sel['E']/obs-1)*100):+.1f}%)")
    else:
        print(f"  No positive binding found")
    print()

# ══════════════════════════════════════════════════════════════
# Molecules
# ══════════════════════════════════════════════════════════════

print("=" * 70)
print("MOLECULES (min-writhe LP selection)")
print("=" * 70)
print()

hh = bond_results.get('H-H', {}).get('E', 0)
ch = bond_results.get('C-H', {}).get('E', 0)
co = bond_results.get('C-O', {}).get('E', 0)
cc = bond_results.get('C-C', {}).get('E', 0)

molecules = [
    ("H₂",   1*hh,          4.478),
    ("CO",    3*co,          11.09),
    ("CO₂",  4*co,          16.56),
    ("CH₄",  4*ch,          17.9),
    ("C₆H₆", 9*cc + 6*ch,  57.4),
]

print(f"  {'Mol':>6} {'Predicted':>10} {'Observed':>10} {'Error':>8}")
print("  " + "-" * 38)
for name, pred, obs in molecules:
    err = float((pred/obs - 1)*100) if pred > 0 and obs > 0 else float('nan')
    print(f"  {name:>6} {float(pred):>8.2f} eV {obs:>8.2f} eV {err:>+7.1f}%")

print()

# ══════════════════════════════════════════════════════════════
# Witness
# ══════════════════════════════════════════════════════════════

w = WitnessBuilder("ch-bond-writhe-lp", engine="python")
w.set_description(
    "Molecular bonds from two-level LP dual. "
    "Degree 0: minimize |tr_M|. Degree 1: minimize writhe. "
    "Selects smallest n with positive binding at minimum writhe."
)
w.set_content_block("def:molecular-braid")
w.add_parameter("q", q0)
w.add_parameter("E_mol_eV", E_mol)

for bname, data in bond_results.items():
    w.add_data(f"bond_{bname}", {
        "n": len(data['ops'].split(',')),
        "writhe": data['w'],
        "ops": data['ops'],
        "E_eV": float(data['E']),
    })

w.add_data("molecules", [{"name": n, "pred_eV": p, "obs_eV": o}
                          for n, p, o in molecules])

for name, pred, obs in molecules:
    w.add_assertion(
        f"{name} positive binding",
        computed=pred > 0,
        expected=True,
        source="min-writhe LP",
    )

w.save()
print("Done.")
