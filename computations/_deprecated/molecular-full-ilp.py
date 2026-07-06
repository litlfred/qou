#!/usr/bin/env python3
"""
Integer LP on FULL atom tower (not valence channel).

Enumerate all braid words up to length 6 between full atoms.
3-channel vertex volumes per generator.

Usage:
    cd computations
    python3 molecular-full-ilp.py
"""

import math, sys, itertools
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0, HA as h, q_int

z = 1.0/(q0**0.5+qi0**0.5)
def qintv(k): return (q0**k - qi0**k) / h
nf3 = qintv(1)*qintv(2)*qintv(3)
dim_std = qintv(2)
w_s=1.0/nf3; w_d=dim_std**2/nf3; w_a=1.0/nf3
wt=w_s+w_d+w_a; w_s/=wt; w_d/=wt; w_a/=wt
E_mol = 511000.0*(qi0/(q_int(9)*q_int(10)))**2/(q0+qi0)**2

PROTON_G0 = [(1,0)]*3 + [(1,0)] + [(1,0)]*2 + [(1,-h/2)]
PROTON_G1 = [(1,-h)]*3 + [(1,-h/2)]
NEUTRON_G0 = [(1,0)]*3 + [(1,-h/2)] + [(1,0)] + [(1,0)] + [(1,-h/2)]
NEUTRON_G1 = [(1,-h)]*3 + [(1,-h)] + [(1,0)] + [(1,0)]
PE = (1,-h)

OPS = [
    ("σ₀",  0, 1.0, 0.0),
    ("σ₁",  1, 1.0, 0.0),
    ("σ₀⁻¹",0, 1.0, -h),
    ("σ₁⁻¹",1, 1.0, -h),
]

def vertex_volume(crossings):
    a,b = 0.0,1.0
    sp,ap = 1.0,1.0
    for c,d in crossings:
        a,b = a*c*h+a*d+b*c, a*c+b*d
        sp *= c*q0+d; ap *= -c*qi0+d
    return w_s*sp + w_d*(z*a+b) + w_a*ap

def Phi1(vols):
    return sum(math.log(abs(v)) for v in vols if abs(v)>1e-300)

def atom_gens(Z, N):
    g0, g1 = [], []
    pc, nc = 0, 0
    for k in range(Z+N):
        is_p = (k%2==0 and pc<Z) or nc>=N
        if is_p:
            g0.extend(PROTON_G0); g1.extend(PROTON_G1); pc+=1
        else:
            g0.extend(NEUTRON_G0); g1.extend(NEUTRON_G1); nc+=1
    for _ in range(Z):
        g1.append(PE)
    return g0, g1

def scan_full(ZA, NA, ZB, NB, label, obs, max_n=6):
    g0A, g1A = atom_gens(ZA, NA)
    g0B, g1B = atom_gens(ZB, NB)

    V0u = vertex_volume(g0A + g0B)
    V1u = vertex_volume(g1A + g1B)
    Phi_ub = Phi1([V0u, V1u])

    print("--- {} ({},{}) × ({},{}) ---".format(label, ZA, NA, ZB, NB))
    print("  Full atom: gen0 {}+{} = {} crossings, gen1 {}+{} = {} crossings".format(
        len(g0A), len(g0B), len(g0A)+len(g0B),
        len(g1A), len(g1B), len(g1A)+len(g1B)))
    print("  Unbonded: Φ₁ = {:.6f}".format(Phi_ub))

    for n in range(1, max_n+1):
        best_bind = -float('inf')
        best_word = None
        best_E = 0
        n_pos = 0

        for word in itertools.product(OPS, repeat=n):
            bond_g0 = [(c,d) for _,gen,c,d in word if gen==0]
            bond_g1 = [(c,d) for _,gen,c,d in word if gen==1]

            V0 = vertex_volume(g0A + bond_g0 + g0B)
            V1 = vertex_volume(g1A + bond_g1 + g1B)
            if abs(V0)<1e-300 or abs(V1)<1e-300: continue

            Phi_b = Phi1([V0, V1])
            bind = Phi_ub - Phi_b
            E = bind * E_mol
            if bind > 0: n_pos += 1
            if bind > best_bind:
                best_bind = bind
                best_word = ",".join(o[0] for o in word)
                best_E = E

        if best_word and best_bind > 0:
            err = (best_E/obs-1)*100
            m = " ←" if abs(err)<10 else ""
            print("  n={}: {} → {:.4f} eV ({:+.1f}%) [{}/{}]{}".format(
                n, best_word, best_E, err, n_pos, 4**n, m))
        else:
            print("  n={}: best {:.4f} eV (no positive binding)".format(n, best_E))

    print()


print("=" * 70)
print("INTEGER LP: FULL ATOM TOWER, ALL BRAID WORDS")
print("=" * 70)
print("  E_mol = {:.4f} eV".format(E_mol))
print()

bonds = [
    ("H-H", 1, 0, 1, 0, 4.478),
    ("C-H", 6, 6, 1, 0, 4.48),
    ("C-C", 6, 6, 6, 6, 3.60),
    ("C-O", 6, 6, 8, 8, 3.70),
    ("O-H", 8, 8, 1, 0, 4.82),
]

for bname, ZA, NA, ZB, NB, obs in bonds:
    scan_full(ZA, NA, ZB, NB, bname, obs, max_n=6)

print("Done.")
