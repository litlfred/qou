#!/usr/bin/env python3
"""H × trefoil × H: compute NF of H₂ with trefoil knot operator."""

import math, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0, HA as h, q_int

z = 1.0/(q0**0.5+qi0**0.5)
TR_M = [1.0, z, z, z**2, z**2, z**3]
NF_NAMES = ["gamma", "s0", "s1", "L+", "L-", "e-"]
E_mol = 511000.0*(qi0/(q_int(9)*q_int(10)))**2/(q0+qi0)**2

def hm(nf,c,d,g):
    r=[0.0]*6
    if g==0:
        t=[(0,[(1,c),(0,d)]),(1,[(1,c*h),(0,c),(1,d)]),(2,[(3,c),(2,d)]),(3,[(3,c*h),(2,c),(3,d)]),(4,[(5,c),(4,d)]),(5,[(5,c*h),(4,c),(5,d)])]
    else:
        t=[(0,[(2,c),(0,d)]),(1,[(4,c),(1,d)]),(2,[(2,c*h),(0,c),(2,d)]),(3,[(5,c),(3,d)]),(4,[(4,c*h),(1,c),(4,d)]),(5,[(5,c*h),(3,c),(5,d)])]
    for si,tgts in t:
        if abs(nf[si])<1e-15: continue
        for ti,co in tgts: r[ti]+=nf[si]*co
    return r

def nf_tr(nf): return sum(nf[i]*TR_M[i] for i in range(6))

def show(label, nf):
    t = nf_tr(nf)
    Phi = math.log(abs(t)) if abs(t)>1e-300 else float('inf')
    nf_str = ", ".join("{:+.6f}".format(v) for v in nf)
    print("  " + label)
    print("    NF = [" + nf_str + "]")
    print("    net = {:+.6f}, tr_M = {:.6e}, Phi_1 = {:.6f}".format(sum(nf), t, Phi))
    return t, Phi

def build_H():
    nf = [1,0,0,0,0,0]
    for _ in range(3):
        nf = hm(nf,1,0,0); nf = hm(nf,1,-h,1)
    nf = hm(nf,1,0,0); nf = hm(nf,1,-h/2,1); nf = hm(nf,1,-h/2,0)
    nf = hm(nf,1,0,0); nf = hm(nf,1,0,0)
    nf = hm(nf,1,-h,1)
    return nf

def apply_H(nf):
    for _ in range(3):
        nf = hm(nf,1,0,0); nf = hm(nf,1,-h,1)
    nf = hm(nf,1,0,0); nf = hm(nf,1,-h/2,1); nf = hm(nf,1,-h/2,0)
    nf = hm(nf,1,0,0); nf = hm(nf,1,0,0)
    nf = hm(nf,1,-h,1)
    return nf

nf_H = build_H()
print("=" * 70)
print("H x [KNOT OPERATOR] x H")
print("=" * 70)
print()

tr_H, Phi_H = show("H atom", nf_H)
print()

nf_ub = apply_H(list(nf_H))
tr_ub, Phi_ub = show("H x H (unbonded)", nf_ub)
print()

# ── Trefoil variants ──────────────────────────────────────────

operators = [
    # Positive trefoils (writhe +3)
    ("T(2,3) = s0 s1 s0",           [(0,1,0),(1,1,0),(0,1,0)]),
    ("T(2,3) = s1 s0 s1",           [(1,1,0),(0,1,0),(1,1,0)]),
    # Inverse trefoils (writhe -3)
    ("T(2,3)^-1 = s0i s1i s0i",     [(0,1,-h),(1,1,-h),(0,1,-h)]),
    ("T(2,3)^-1 = s1i s0i s1i",     [(1,1,-h),(0,1,-h),(1,1,-h)]),
    # Other 3-crossing operators for comparison
    ("s1i s1i s1i (writhe -3)",      [(1,1,-h),(1,1,-h),(1,1,-h)]),
    ("s0i s1i s0i (from prev LP)",   [(0,1,-h),(1,1,-h),(0,1,-h)]),
    # Hopf link (writhe -2)
    ("s1i s1i (Hopf, writhe -2)",    [(1,1,-h),(1,1,-h)]),
    # 2-crossing from H2 LP
    ("s1i s1i (from H2 LP, n=2)",    [(1,1,-h),(1,1,-h)]),
]

print("=" * 70)
print("KNOT OPERATORS BETWEEN TWO H ATOMS")
print("=" * 70)
print()

results = []
for label, ops in operators:
    nf = list(nf_H)
    for gen, c, d in ops:
        nf = hm(nf, c, d, gen)
    nf = apply_H(nf)

    t = nf_tr(nf)
    Phi = math.log(abs(t)) if abs(t) > 1e-300 else float('inf')
    bind = Phi_ub - Phi
    E = bind * E_mol
    writhe = sum(-1 if d < 0 else +1 for _, _, d in ops)

    tr_val, Phi_val = show(label, nf)
    print("    writhe = {:+d}, binding = {:.6f}, E = {:.4f} eV".format(writhe, bind, E))
    print()
    results.append((label, writhe, bind, E))

print("=" * 70)
print("SUMMARY")
print("=" * 70)
print()
print("  {:>35s}  {:>6s} {:>10s} {:>10s}".format("Operator", "writhe", "binding", "E(eV)"))
print("  " + "-" * 65)
print("  {:>35s}  {:>6s} {:>10s} {:>10s}".format("unbonded", "0", "0", "0"))
for label, w, bind, E in results:
    marker = " <--" if 3.5 < E < 5.5 else ""
    print("  {:>35s}  {:>+6d} {:>10.6f} {:>10.4f}{}".format(label, w, bind, E, marker))

print()
print("  Observed D_0(H2) = 4.478 eV")
