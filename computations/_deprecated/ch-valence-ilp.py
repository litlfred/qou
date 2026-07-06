#!/usr/bin/env python3
"""
C-H bond: enumerate ALL braid words on valence channel.

Same as h2-integer-lp.py but on the valence channel (C:4e, H:1e).
Enumerate all words in {σ₀,σ₁,σ₀⁻¹,σ₁⁻¹}^n for n=1..6.
For each word, compute 3-channel vertex volume Φ₁.
Find the word with maximum binding (minimum Φ₁ with bind > 0).

Usage:
    cd computations
    python3 ch-valence-ilp.py
"""

import math, sys, itertools
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0, HA as h, q_int

z = 1.0/(q0**0.5+qi0**0.5)
def qintv(k): return (q0**k - qi0**k) / h
nf3 = qintv(1)*qintv(2)*qintv(3)
dim_std = qintv(2)
w_s = 1.0/nf3; w_d = dim_std**2/nf3; w_a = 1.0/nf3
wt = w_s+w_d+w_a; w_s/=wt; w_d/=wt; w_a/=wt
E_mol = 511000.0*(qi0/(q_int(9)*q_int(10)))**2/(q0+qi0)**2

PROTON_G0 = [(1,0)]*3 + [(1,0)] + [(1,0)]*2 + [(1,-h/2)]
PROTON_G1 = [(1,-h)]*3 + [(1,-h/2)]
PE = (1,-h)

# Bond operator alphabet: (name, gen, c, d)
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

def valence_gens(n_val):
    g0 = list(PROTON_G0)
    g1 = list(PROTON_G1)
    for _ in range(n_val): g1.append(PE)
    return g0, g1


def scan_bond_words(vA, vB, label, obs, max_n=6):
    g0_A, g1_A = valence_gens(vA)
    g0_B, g1_B = valence_gens(vB)

    V0_ub = vertex_volume(g0_A + g0_B)
    V1_ub = vertex_volume(g1_A + g1_B)
    Phi_ub = Phi1([V0_ub, V1_ub])

    print("--- {} (valence {}+{}) ---".format(label, vA, vB))
    print("  Unbonded: Φ₁ = {:.6f}, V̂₀ = {:.4f}, V̂₁ = {:.4f}".format(
        Phi_ub, V0_ub, V1_ub))
    print()

    all_best = []

    for n in range(1, max_n+1):
        best_bind = -float('inf')
        best_word = None
        best_E = 0
        n_positive = 0

        for word in itertools.product(OPS, repeat=n):
            # Split word into gen0 and gen1 crossings
            bond_g0 = [(c,d) for name,gen,c,d in word if gen == 0]
            bond_g1 = [(c,d) for name,gen,c,d in word if gen == 1]

            V0 = vertex_volume(g0_A + bond_g0 + g0_B)
            V1 = vertex_volume(g1_A + bond_g1 + g1_B)

            if abs(V0) < 1e-300 or abs(V1) < 1e-300:
                continue

            Phi_b = Phi1([V0, V1])
            bind = Phi_ub - Phi_b
            E = bind * E_mol

            if bind > 0:
                n_positive += 1

            if bind > best_bind:
                best_bind = bind
                best_word = ",".join(o[0] for o in word)
                best_E = E
                best_V0 = V0
                best_V1 = V1
                best_Phi = Phi_b

        if best_word and best_bind > 0:
            err = (best_E/obs - 1)*100
            marker = " ←" if abs(err) < 10 else ""
            print("  n={}: {} → E={:.4f} eV (err {:+.1f}%) [{}+ / {}]{}"
                  .format(n, best_word, best_E, err, n_positive, 4**n, marker))
            print("        V̂₀={:.4f}, V̂₁={:.4f}, Φ₁={:.6f}".format(
                best_V0, best_V1, best_Phi))
            all_best.append((n, best_word, best_E, best_bind))
        elif best_word:
            print("  n={}: best is {} → E={:.4f} eV (repulsive, best bind={:.4f})".format(
                n, best_word, best_E, best_bind))
        else:
            print("  n={}: all singular".format(n))

    # Overall best
    if all_best:
        positives = [(n,w,E,b) for n,w,E,b in all_best if b > 0]
        if positives:
            closest = min(positives, key=lambda x: abs(x[2]-obs))
            print("\n  → ILP ANSWER: n={}, ops={}, E={:.4f} eV (obs {:.2f}, err {:+.1f}%)".format(
                closest[0], closest[1], closest[2], obs, (closest[2]/obs-1)*100))
            return closest
    print("\n  → No positive binding found")
    return None


print("=" * 70)
print("INTEGER LP: ENUMERATE ALL BRAID WORDS ON VALENCE CHANNEL")
print("=" * 70)
print("  3-channel vertex volumes, E_mol = {:.4f} eV".format(E_mol))
print()

bond_types = [
    ("H-H", 1, 1, 4.478),
    ("C-H", 4, 1, 4.48),
    ("C-C", 4, 4, 3.60),
    ("C-O", 4, 6, 3.70),
    ("O-H", 6, 1, 4.82),
]

results = {}
for bname, vA, vB, obs in bond_types:
    r = scan_bond_words(vA, vB, bname, obs, max_n=6)
    results[bname] = r
    print()

# Molecules
print("=" * 70)
print("MOLECULES")
print("=" * 70)
print()

def get_E(bname):
    r = results.get(bname)
    return r[2] if r else 0

molecules = [
    ("H₂",   1*get_E('H-H'),              4.478),
    ("CO",    3*get_E('C-O'),              11.09),
    ("CO₂",  4*get_E('C-O'),              16.56),
    ("CH₄",  4*get_E('C-H'),              17.9),
    ("C₆H₆", 9*get_E('C-C')+6*get_E('C-H'), 57.4),
]

print("  {:>8s} {:>10s} {:>10s} {:>8s}".format("Mol","Predicted","Observed","Error"))
print("  "+"-"*40)
for name,pred,obs in molecules:
    err = (pred/obs-1)*100 if pred>0 else float('nan')
    print("  {:>8s} {:>8.2f} eV {:>8.2f} eV {:>+7.1f}%".format(name,pred,obs,err))

print("\nDone.")
