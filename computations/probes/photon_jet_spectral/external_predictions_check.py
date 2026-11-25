#!/usr/bin/env python3
"""Exact checks of the external AI's follow-up predictions (pasted by the owner 2026-11-25).
C: rank of mu_sym: Sym^2(W) -> H3 and whether [s0,s1] is in its image.
2.2: *-Gram with s* = s^{-1}: tr(V* s0) vs tr(V* s1).
3: S6 outer-automorphism claim: are the point-stabiliser S5 and the transitive S5 almost conjugate?
B: grouplike coproduct Delta(s)=s(x)s is incompatible with the Hecke relation unless h=0."""
import itertools, json, sympy as sp
from pathlib import Path
import importlib.util
spec = importlib.util.spec_from_file_location('p', Path(__file__).with_name('photon_jet_probe.py'))
src = Path(__file__).with_name('photon_jet_probe.py').read_text().split('res = {}')[0]
ns = {}; exec(src, ns)
S0, S1, V, I6, h, q, trM, vec, z = ns['S0'], ns['S1'], ns['V'], ns['I6'], ns['h'], ns['q'], ns['trM'], ns['vec'], ns['z']
out = {'q0Anchor': 'independent', 'q0AnchorReason': 'symbolic in q over Q(q) or at rational q; never reads the substrate q0'}
Wl = [S0, S1, V]
sym = [Wl[i]*Wl[j] + Wl[j]*Wl[i] for i in range(3) for j in range(i, 3)]
Msym = sp.Matrix.hstack(*[vec(m) for m in sym])
out['C_rank_mu_sym'] = int(Msym.rank(simplify=True))
comm = vec(S0*S1 - S1*S0)
out['C_commutator_in_im_mu_sym'] = int(sp.Matrix.hstack(Msym, comm).rank(simplify=True)) == out['C_rank_mu_sym']
S0i, S1i = S0 - h*I6, S1 - h*I6
Vstar = S1*S0i   # (s0 s1^{-1})^* = s1 s0^{-1} under s* = s^{-1} (anti-automorphism)
a = sp.factor(trM(Vstar*S0, z)); b = sp.factor(trM(Vstar*S1, z))
out['2.2_tr(V*s0)'] = str(a); out['2.2_tr(V*s1)'] = str(b); out['2.2_diff'] = str(sp.factor(b - a))
# S6: point stabiliser S5 vs transitive S5 (image under outer automorphism)
def cyc_type(p):
    seen=set(); t=[]
    for i in range(6):
        if i in seen: continue
        L=0; j=i
        while j not in seen: seen.add(j); j=p[j]; L+=1
        t.append(L)
    return tuple(sorted(t))
def mul(a,b): return tuple(a[b[i]] for i in range(6))
def close(gens):
    e=tuple(range(6)); S={e}; fr=[e]
    while fr:
        nf=[]
        for x in fr:
            for g in gens:
                y=mul(x,g)
                if y not in S: S.add(y); nf.append(y)
        fr=nf
    return S
stab = close([(1,0,2,3,4,5),(1,2,3,4,0,5)])
# transitive S5 = PGL(2,5) acting on 6 points of P^1(F5): x->x+1, x->2x, x->-1/x ; points 0..4, inf=5
def mob(f):
    return tuple(f(x) for x in range(6))
def inv5(x): return pow(x,3,5)
add1 = mob(lambda x: 5 if x==5 else (x+1)%5)
dbl  = mob(lambda x: 5 if x==5 else (2*x)%5)
negi = mob(lambda x: 0 if x==5 else (5 if x==0 else (-inv5(x))%5))
trans = close([add1, dbl, negi])
prof = lambda H: sorted({c: sum(1 for g in H if cyc_type(g)==c) for c in set(map(cyc_type,H))}.items())
out['3_orders'] = [len(stab), len(trans)]
out['3_profile_point_stabiliser'] = str(prof(stab)); out['3_profile_transitive'] = str(prof(trans))
out['3_almost_conjugate'] = prof(stab) == prof(trans)
# B: grouplike Delta(s)=s(x)s: in a pair of irreps s->q, s->-1/q the product eigenvalue -1 must satisfy x^2 = h x + 1
out['B_grouplike_constraint_at_eig_-1'] = str(sp.factor((-1)**2 - (h*(-1) + 1)))
Path(__file__).with_name('external-predictions-check.witness.json').write_text(json.dumps(out, indent=1))
for k,v in out.items(): print(k, ':', v)
