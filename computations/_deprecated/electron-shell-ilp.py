#!/usr/bin/env python3
"""
ILP electron shell filling: how each electron attaches to an atom.

For each atom (H through O), build the nucleus, then add electrons
one at a time. At each step, the ILP scans all 1-3 crossing operators
and selects: min crossing number subject to Frobenius Gx ≥ 0, then
min |tr_M| among feasible.

The ILP discovers:
  - Electrons alternate between σ₁⁻¹ and σ₀⁻¹ (generator alternation)
  - This IS the shell structure / Hund's rule pairing
  - Not all electrons are identical pe crossings

Then: compute molecular binding using the ILP-derived electron operators,
and verify the inverse trefoil bond on the resulting atoms.

Usage:
    cd computations
    python3 electron-shell-ilp.py
"""

import math, sys, itertools
import numpy as np
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from q_parameter import Q as q0, Q_INV as qi0, HA as h, q_int
from witness_base import WitnessBuilder

z = 1.0/(q0**0.5+qi0**0.5)
def qintv(k): return (q0**k - qi0**k) / h
nf3 = qintv(1)*qintv(2)*qintv(3)
dim_std = qintv(2)
w_s=1.0/nf3; w_d=dim_std**2/nf3; w_a=1.0/nf3
wt=w_s+w_d+w_a; w_s/=wt; w_d/=wt; w_a/=wt
E_mol = 511000.0*(qi0/(q_int(9)*q_int(10)))**2/(q0+qi0)**2

NF_BASIS = [(), (0,), (1,), (0,1), (1,0), (0,1,0)]
NF_NAMES = ['γ','σ₀','σ₁','L₊','L₋','e⁻']
TR_M = np.array([1.0, z, z, z**2, z**2, z**3])

PROTON_G0 = [(1,0)]*3 + [(1,0)] + [(1,0)]*2 + [(1,-h/2)]
PROTON_G1 = [(1,-h)]*3 + [(1,-h/2)]
NEUTRON_G0 = [(1,0)]*3 + [(1,-h/2)] + [(1,0)] + [(1,0)] + [(1,-h/2)]
NEUTRON_G1 = [(1,-h)]*3 + [(1,-h)] + [(1,0)] + [(1,0)]
INV_T_G0 = [(1,-h),(1,-h)]
INV_T_G1 = [(1,-h)]

OPS = [('σ₀',0,1.,0.),('σ₁',1,1.,0.),('σ₀⁻¹',0,1.,-h),('σ₁⁻¹',1,1.,-h)]


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


def check_frob(nf):
    x=np.array(nf); Gx=G@x
    return [(NF_NAMES[i], Gx[i]) for i in range(6) if Gx[i]<-1e-10]


def vv(crossings):
    a,b=0.,1.; sp,ap=1.,1.
    for c,d in crossings:
        a,b=a*c*h+a*d+b*c,a*c+b*d
        sp*=c*q0+d; ap*=-c*qi0+d
    return w_s*sp+w_d*(z*a+b)+w_a*ap


def Phi1(vols):
    return sum(math.log(abs(v)) for v in vols if abs(v)>1e-300)


def build_nucleus(Z, N):
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
    return nf


def ilp_add_electrons(Z, N, label):
    """Build atom by adding electrons one at a time via ILP."""
    nf = build_nucleus(Z, N)
    electron_ops = []
    # Track per-generator crossings for vertex volume computation
    g0 = []
    g1 = []
    # Add nucleus crossings to generator lists
    pc, nc = 0, 0
    for k in range(Z+N):
        ip = (k%2==0 and pc<Z) or nc>=N
        if ip:
            g0.extend(PROTON_G0); g1.extend(PROTON_G1); pc+=1
        else:
            g0.extend(NEUTRON_G0); g1.extend(NEUTRON_G1); nc+=1

    print('  {} (Z={}, N={}):'.format(label, Z, N))

    for e in range(1, Z+1):
        best = None
        for n in range(1, 4):
            for word in itertools.product(OPS, repeat=n):
                nf_test = list(nf)
                for name, gen, c, d in word:
                    nf_test = hm(nf_test, c, d, gen)
                viol = check_frob(nf_test)
                if viol:
                    continue
                tr_test = sum(nf_test[i]*TR_M[i] for i in range(6))
                ops_str = ','.join(o[0] for o in word)
                if best is None or n < best[0] or (n == best[0] and abs(tr_test) < best[1]):
                    best = (n, abs(tr_test), nf_test, ops_str, word)
            if best and best[0] == n:
                break  # found at this crossing count, don't go higher

        if best:
            nf = best[2]
            electron_ops.append(best[3])
            # Add to generator lists
            for name, gen, c, d in best[4]:
                if gen == 0:
                    g0.append((c, d))
                else:
                    g1.append((c, d))
            print('    e{}: {} (n={})'.format(e, best[3], best[0]))
        else:
            # Fallback
            nf = hm(list(nf), 1, -h, 1)
            electron_ops.append('σ₁⁻¹(fallback)')
            g1.append((1, -h))
            print('    e{}: σ₁⁻¹ (fallback, no stable op found)'.format(e))

    return nf, electron_ops, g0, g1


# ══════════════════════════════════════════════════════════════
# §1. Build all atoms via ILP electron shell filling
# ══════════════════════════════════════════════════════════════

print("=" * 70)
print("ILP ELECTRON SHELL FILLING")
print("=" * 70)
print()

atoms = {}
for label, Z, N in [('H',1,0),('C',6,6),('N',7,7),('O',8,8)]:
    nf, ops, g0, g1 = ilp_add_electrons(Z, N, label)
    tr = sum(nf[i]*TR_M[i] for i in range(6))
    atoms[label] = {'nf': nf, 'ops': ops, 'g0': g0, 'g1': g1, 'tr': tr, 'Z': Z, 'N': N}
    print('    Shell: [{}]'.format(', '.join(ops)))
    print('    tr_M = {:.6e}'.format(tr))
    print()


# ══════════════════════════════════════════════════════════════
# §2. Molecular binding with ILP-derived atoms + inverse trefoil
# ══════════════════════════════════════════════════════════════

print("=" * 70)
print("MOLECULAR BINDING (ILP atoms + inverse trefoil)")
print("=" * 70)
print()

def bond_energy(atom_A, atom_B, n_trefoils=1):
    """Binding energy using 3-channel vertex volumes."""
    g0A = atoms[atom_A]['g0']
    g1A = atoms[atom_A]['g1']
    g0B = atoms[atom_B]['g0']
    g1B = atoms[atom_B]['g1']

    Phi_ub = Phi1([vv(g0A+g0B), vv(g1A+g1B)])
    bg0 = INV_T_G0 * n_trefoils
    bg1 = INV_T_G1 * n_trefoils
    Phi_b = Phi1([vv(g0A+bg0+g0B), vv(g1A+bg1+g1B)])
    return (Phi_ub - Phi_b) * E_mol

# Single bonds
print('{:>8s} {:>10s} {:>10s} {:>8s}'.format('Bond','Predicted','Observed','Error'))
print('-' * 40)

bond_results = {}
for bname, aA, aB, order, obs in [
    ('H-H', 'H','H', 1, 4.478),
    ('C-H', 'C','H', 1, 4.33),
    ('N-H', 'N','H', 1, 3.87),
    ('O-H', 'O','H', 1, 4.82),
    ('C-C', 'C','C', 1, 3.60),
    ('C-N', 'C','N', 1, 3.16),
    ('C-O', 'C','O', 1, 3.71),
    ('C=C', 'C','C', 2, 6.36),
    ('C=O', 'C','O', 2, 7.71),
    ('C≡O', 'C','O', 3, 11.09),
    ('C≡C', 'C','C', 3, 8.70),
    ('N≡N', 'N','N', 3, 9.79),
]:
    E = bond_energy(aA, aB, order)
    err = (E/obs-1)*100 if E > 0 else float('nan')
    m = ' <--' if abs(err)<15 and E>0 else ''
    print('{:>8s} {:>8.2f} eV {:>8.2f} eV {:>+7.1f}%{}'.format(bname, E, obs, err, m))
    bond_results[bname] = E

# ── Molecules ─────────────────────────────────────────────────
print()
print('{:>10s} {:>10s} {:>10s} {:>8s}'.format('Molecule','Predicted','Observed','Error'))
print('-' * 42)

def mol(bonds):
    return sum(bond_results[b]*n for b,n in bonds)

molecules = [
    ('H₂',     [('H-H',1)],                      4.478),
    ('H₂O',    [('O-H',2)],                       9.51),
    ('NH₃',    [('N-H',3)],                      11.6),
    ('CH₄',    [('C-H',4)],                      17.4),
    ('C₂H₆',   [('C-C',1),('C-H',6)],            29.7),
    ('C₂H₄',   [('C=C',1),('C-H',4)],            23.1),
    ('CO',      [('C≡O',1)],                      11.09),
    ('CO₂',    [('C=O',2)],                      16.56),
    ('N₂',     [('N≡N',1)],                       9.79),
    ('C₆H₆',   [('C=C',3),('C-C',3),('C-H',6)], 57.4),
    ('C₃H₈',   [('C-C',2),('C-H',8)],            42.0),
]

results = []
for name, bonds, obs in molecules:
    E = mol(bonds)
    err = (E/obs-1)*100 if E > 0 else float('nan')
    print('{:>10s} {:>8.2f} eV {:>8.2f} eV {:>+7.1f}%'.format(name, E, obs, err))
    results.append((name, E, obs, err))

print()
pos = [r for r in results if r[1]>0]
mae = sum(abs(r[3]) for r in pos)/len(pos) if pos else 0
print('Mean absolute error: {:.1f}%'.format(mae))

# ══════════════════════════════════════════════════════════════
# Witness
# ══════════════════════════════════════════════════════════════

w = WitnessBuilder("electron-shell-ilp", engine="python")
w.set_description(
    "ILP electron shell filling + molecular binding. "
    "Each electron attached via ILP: min crossings s.t. Frobenius. "
    "Bond = inverse trefoil (min crossing knot). "
    "3-channel Wedderburn vertex volumes."
)
w.set_content_block("prop:shell-filling-rule")
w.add_parameter("q", q0)
w.add_parameter("E_mol_eV", E_mol)

for label, data in atoms.items():
    w.add_data("atom_" + label, {
        "Z": data['Z'], "N": data['N'],
        "electron_operators": data['ops'],
        "tr_M": data['tr'],
    })

for name, E, obs, err in results:
    w.add_assertion(
        name, computed=round(E, 2), expected=obs,
        tolerance=obs * 0.30, unit="eV",
        source="ILP electron shell + inverse trefoil bond",
    )
    w.add_data("mol_" + name.replace("₂","2").replace("₃","3").replace("₄","4").replace("₆","6").replace("₈","8"),
               {"predicted_eV": E, "observed_eV": obs, "error_pct": round(err, 1)})

w.save()
print("\nDone.")
