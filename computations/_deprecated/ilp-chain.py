#!/usr/bin/env python3
"""
Full ILP chain: quarks → B₃ → gluon → atom → molecule.

At each step:
  1. Current state = NF in H₃(q)
  2. Enumerate all braid words up to length N
  3. Apply each to current state
  4. Check Frobenius G(x·w) ≥ 0
  5. Among feasible: minimize |tr_M| (categorical action)
  6. If none feasible: the system is unstable, needs the operator
  7. Apply the selected operator, update state, continue

Same protocol at every level — no assumptions about which operator.

Usage:
    cd computations
    python3 ilp-chain.py
"""

import math, sys, itertools
import numpy as np
sys.path.insert(0, '.')
from q_parameter import Q as q0, Q_INV as qi, HA as h, q_int
from witness_base import WitnessBuilder

z = 1.0/(q0**0.5+qi**0.5)
NF_NAMES = ['γ','σ₀','σ₁','L₊','L₋','e⁻']
TR_M = np.array([1.0, z, z, z**2, z**2, z**3])

# Gram matrix
NF_BASIS = [(), (0,), (1,), (0,1), (1,0), (0,1,0)]
def hm_dict(t1,t2):
    r={}
    for w1,c1 in t1.items():
        for w2,c2 in t2.items():
            w=w1+w2; r[w]=r.get(w,0.0)+c1*c2
    return {w:c for w,c in r.items() if abs(c)>1e-15}
def reduce_nf(terms):
    changed=True
    while changed:
        changed=False; new={}
        for word,coeff in terms.items():
            if abs(coeff)<1e-15: continue
            done=False
            for p in range(len(word)-1):
                if word[p]==word[p+1]:
                    i=word[p]; pre,suf=word[:p],word[p+2:]
                    new[pre+(i,)+suf]=new.get(pre+(i,)+suf,0)+coeff*h
                    new[pre+suf]=new.get(pre+suf,0)+coeff
                    done=changed=True; break
            if done: continue
            for p in range(len(word)-2):
                a,b,c=word[p],word[p+1],word[p+2]
                if a==c and abs(a-b)==1:
                    nt=(b,a,b)
                    if nt<(a,b,a):
                        nw=word[:p]+nt+word[p+3:]
                        new[nw]=new.get(nw,0)+coeff
                        done=changed=True; break
            if not done: new[word]=new.get(word,0)+coeff
        terms={w:c for w,c in new.items() if abs(c)>1e-15}
    return terms

G = np.zeros((6,6))
for i in range(6):
    for j in range(6):
        prod=hm_dict({NF_BASIS[i]:1.0},{NF_BASIS[j]:1.0})
        nf=reduce_nf(prod); vec=np.array([nf.get(b,0.0) for b in NF_BASIS])
        G[i,j]=sum(vec[k]*TR_M[k] for k in range(6))

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

def check_frob(nf):
    x=np.array(nf); Gx=G@x
    return all(v >= -1e-10 for v in Gx), Gx

def nf_tr(nf): return sum(nf[i]*TR_M[i] for i in range(6))

# Braid word generators
OPS = [
    ('σ₀',  0, 1.0, 0.0),
    ('σ₁',  1, 1.0, 0.0),
    ('σ₀⁻¹',0, 1.0, -h),
    ('σ₁⁻¹',1, 1.0, -h),
]

def apply_word(nf, word):
    """Apply a braid word (sequence of generators) to NF."""
    result = list(nf)
    for name, gen, c, d in word:
        result = hm(result, c, d, gen)
    return result

def ilp_step(nf, label, max_len=6):
    """ILP: find minimum-length braid word that keeps Frobenius stable.

    If current state is stable: find the minimum-length word that
    DESTABILIZES it (this is NOT the operator — it's the probe).

    Actually: the ILP finds the operator to APPLY. Among all words
    of length 1, 2, ..., find the one with minimum |tr_M| that
    keeps G(nf · word) ≥ 0.
    """
    stable_0, Gx_0 = check_frob(nf)
    tr_0 = nf_tr(nf)

    print('  {} state: Frob={}, tr_M={:.6e}'.format(
        label, 'STABLE' if stable_0 else 'UNSTABLE', tr_0))

    if not stable_0:
        viols = [(NF_NAMES[i], Gx_0[i]) for i in range(6) if Gx_0[i] < -1e-10]
        print('    Violations: {}'.format(
            ', '.join('{}={:.4e}'.format(n,v) for n,v in viols)))

    # Find minimum-length word that:
    # 1. Keeps state Frobenius-stable (if currently stable)
    # 2. RESTORES stability (if currently unstable)
    # Among feasible: minimize |tr_M| of the resulting state

    for n in range(1, max_len + 1):
        feasible = []
        for word in itertools.product(OPS, repeat=n):
            nf_new = apply_word(list(nf), word)
            stable, Gx = check_frob(nf_new)
            if stable:
                tr = nf_tr(nf_new)
                label_w = ''.join(o[0] for o in word)
                feasible.append((label_w, nf_new, abs(tr), tr))

        if feasible:
            # Sort by |tr_M|
            feasible.sort(key=lambda r: r[2])
            best = feasible[0]
            print('    n={}: {}/{} feasible, best={} (|tr|={:.4e})'.format(
                n, len(feasible), 4**n, best[0], best[2]))
            return best[1], best[0], n
        else:
            print('    n={}: 0/{} feasible'.format(n, 4**n))

    print('    NO feasible word up to length {}'.format(max_len))
    return None, None, 0


# ══════════════════════════════════════════════════════════════
# LEVEL 1: QUARKS → CONFINEMENT
# ══════════════════════════════════════════════════════════════

print('='*70)
print('LEVEL 1: QUARKS → CONFINEMENT (derive B₃)')
print('='*70)
print()

# Start from identity (bare quarks, no confinement)
nf = [1.0, 0, 0, 0, 0, 0]
print('Start: identity γ')
stable, Gx = check_frob(nf)
print('  Frobenius: {} (Gx = [{}])'.format(
    'STABLE' if stable else 'UNSTABLE',
    ', '.join('{:.2f}'.format(v) for v in Gx)))
print()

# Apply quark crossings: uu(σ₀) + ud(mixed) + ud(mixed)
print('Apply quark crossings (uud):')
nf = hm(nf, 1, 0, 0)          # uu → σ₀
nf = hm(nf, 1, -h/2, 1)       # ud → mixed on gen 1
nf = hm(nf, 1, -h/2, 0)       # ud → mixed on gen 0
stable, Gx = check_frob(nf)
tr = nf_tr(nf)
print('  After quarks: Frob={}, tr={:.6e}'.format(
    'STABLE' if stable else 'UNSTABLE', tr))
if not stable:
    viols = [(NF_NAMES[i], Gx[i]) for i in range(6) if Gx[i] < -1e-10]
    print('  Violations: {}'.format(
        ', '.join('{}={:.4e}'.format(n,v) for n,v in viols)))
print()

# ILP: what operator restores stability?
print('ILP: find minimum-length stabilizing operator')
nf_conf, word_conf, n_conf = ilp_step(nf, 'quarks', max_len=6)
if nf_conf is not None:
    print('  → CONFINEMENT OPERATOR: {} ({} crossings)'.format(word_conf, n_conf))
    print('  → NF: [{}]'.format(', '.join('{:+.4f}'.format(v) for v in nf_conf)))
    print('  → tr_M = {:.6e}'.format(nf_tr(nf_conf)))
else:
    print('  → Already stable, no confinement needed')
    nf_conf = nf
print()

# ══════════════════════════════════════════════════════════════
# LEVEL 2: CONFINED QUARKS → GLUON
# ══════════════════════════════════════════════════════════════

print('='*70)
print('LEVEL 2: CONFINED QUARKS → GLUON')
print('='*70)
print()

# Apply B₃ first (from level 1), then quarks
nf_b3 = [1.0, 0, 0, 0, 0, 0]
for _ in range(3):
    nf_b3 = hm(nf_b3, 1, 0, 0)
    nf_b3 = hm(nf_b3, 1, -h, 1)

# Proton: B₃ + quarks
nf_proton = list(nf_b3)
nf_proton = hm(nf_proton, 1, 0, 0)       # uu
nf_proton = hm(nf_proton, 1, -h/2, 1)    # ud
nf_proton = hm(nf_proton, 1, -h/2, 0)    # ud

stable, Gx = check_frob(nf_proton)
print('Proton (B₃+quarks, 9 crossings): Frob={}'.format(
    'STABLE' if stable else 'UNSTABLE'))
if not stable:
    viols = [(NF_NAMES[i], Gx[i]) for i in range(6) if Gx[i] < -1e-10]
    print('  Violations: {}'.format(
        ', '.join('{}={:.4e}'.format(n,v) for n,v in viols)))
print()

# ILP: what gluon operator restores stability?
print('ILP: find gluon operator')
nf_gluon, word_gluon, n_gluon = ilp_step(nf_proton, 'proton(9)', max_len=6)
if nf_gluon is not None:
    print('  → GLUON: {} ({} crossings)'.format(word_gluon, n_gluon))
print()

# ══════════════════════════════════════════════════════════════
# LEVEL 3: PROTON+GLUON → ELECTRON ATTACHMENT
# ══════════════════════════════════════════════════════════════

print('='*70)
print('LEVEL 3: PROTON+GLUON → ELECTRON ATTACHMENT')
print('='*70)
print()

# Start from proton+gluon (should be stable)
nf_pg = nf_gluon if nf_gluon is not None else nf_proton
stable, _ = check_frob(nf_pg)
print('Proton+gluon: Frob={}'.format('STABLE' if stable else 'UNSTABLE'))

# ILP: what operator attaches the electron?
# The electron IS an operator — which one?
print()
print('ILP: find electron attachment operator')
nf_H, word_e, n_e = ilp_step(nf_pg, 'proton+gluon', max_len=4)
if nf_H is not None:
    print('  → ELECTRON: {} ({} crossings)'.format(word_e, n_e))
    print('  → H atom NF: [{}]'.format(', '.join('{:+.4f}'.format(v) for v in nf_H)))
    print('  → tr_M(H) = {:.6e}'.format(nf_tr(nf_H)))
print()

# ══════════════════════════════════════════════════════════════
# LEVEL 4: H ATOM → MOLECULAR BOND
# ══════════════════════════════════════════════════════════════

print('='*70)
print('LEVEL 4: H ATOM → MOLECULAR BOND (H₂)')
print('='*70)
print()

if nf_H is not None:
    # ILP: what operator bonds H to another H?
    # Apply operator to H, then check if H×op×H is stable
    print('ILP: find bond operator for H₂')

    # The molecular state is H × bond × H
    # First apply bond to H, then apply second H
    for n in range(1, 7):
        feasible = []
        for word in itertools.product(OPS, repeat=n):
            # H × word × H
            nf_mol = apply_word(list(nf_H), word)
            # Apply second H atom crossings
            nf_mol2 = list(nf_mol)
            # Second H: same construction as first
            for _ in range(3):
                nf_mol2 = hm(nf_mol2, 1, 0, 0)
                nf_mol2 = hm(nf_mol2, 1, -h, 1)
            nf_mol2 = hm(nf_mol2, 1, 0, 0)
            nf_mol2 = hm(nf_mol2, 1, -h/2, 1)
            nf_mol2 = hm(nf_mol2, 1, -h/2, 0)
            # Gluon for second proton
            if nf_gluon is not None:
                for ch in word_gluon:
                    g = 0 if ch in ('σ','σ₀') else 1
                    c_g = 1.0
                    d_g = 0.0 if ch in ('σ₀','σ₁') else -h
                    nf_mol2 = hm(nf_mol2, c_g, d_g, g)
            # Electron for second atom
            if word_e:
                for ch in word_e:
                    g = 0 if 'σ₀' in ch else 1
                    d_g = -h if '⁻¹' in ch else 0.0
                    nf_mol2 = hm(nf_mol2, 1.0, d_g, g)

            stable, Gx = check_frob(nf_mol2)
            if stable:
                tr = nf_tr(nf_mol2)
                label_w = ''.join(o[0] for o in word)
                feasible.append((label_w, nf_mol2, abs(tr), tr))

        if feasible:
            feasible.sort(key=lambda r: r[2])
            best = feasible[0]
            print('  n={}: {}/{} feasible, best={} (|tr|={:.4e})'.format(
                n, len(feasible), 4**n, best[0], best[2]))
        else:
            print('  n={}: 0/{} feasible'.format(n, 4**n))

print()
print('='*70)
print('SUMMARY')
print('='*70)
print()
if nf_conf is not None:
    print('Level 1 (confinement): {} ({} crossings)'.format(word_conf, n_conf))
if nf_gluon is not None:
    print('Level 2 (gluon):       {} ({} crossings)'.format(word_gluon, n_gluon))
if nf_H is not None:
    print('Level 3 (electron):    {} ({} crossings)'.format(word_e, n_e))
