"""EM charge-structure factors of the nucleon with spin (and colour) included.

Exact rational arithmetic (fractions), no floats. Comparison-level quark-model check:
the colour singlet is a common factor (the photon is colour-blind), so only flavour and
spin enter. Reports <sum_{i<j} q_i q_j> (Coulomb) and <sum_{i<j} q_i q_j sigma_i.sigma_j>
(magnetic) on the S=1/2 mixed-symmetry nucleon states. The quark charges 2/3, -1/3 are
those derived on main in prop:neutral-lepton-fixes-charges (#9633, #9637).

Result: n - p = -1/3 in BOTH channels. Spin and colour add no factor to the n-p charge
structure, so the 27-44x gap of #9654 is a spatial (length) factor, not a representation one.
"""
from fractions import Fraction as F
from itertools import product
import itertools
Q={'u':F(2,3),'d':F(-1,3)}
def norm(v): 
    s=sum(c*c for c in v.values()); return {k:c/ s**0 for k,c in v.items()}
# basis states: tuples ((f0,s0),(f1,s1),(f2,s2)), s in {+1,-1}
def add(a,b,c=1):
    for k,v in b.items(): a[k]=a.get(k,0)+c*v
    return a
def sym_state(flav, spins_coeff):
    pass
# build proton spin-up: (1/sqrt18)-type; use unnormalised mixed-symmetric: chi_MS*phi_MS + chi_MA*phi_MA
def kron(fl, sp):  # fl,sp dicts over 3-tuples
    out={}
    for f,cf in fl.items():
        for s,cs in sp.items():
            out[tuple(zip(f,s))]=out.get(tuple(zip(f,s)),0)+cf*cs
    return out
U,D='u','d'; up,dn=1,-1
def phiMS(a,b):  # flavour mixed-sym for a a b  (proton a=u,b=d)
    return {(a,b,a):F(1),(b,a,a):F(1),(a,a,b):F(-2)}
def phiMA(a,b):
    return {(a,b,a):F(1),(b,a,a):F(-1)}
chiMS={(up,dn,up):F(1),(dn,up,up):F(1),(up,up,dn):F(-2)}
chiMA={(up,dn,up):F(1),(dn,up,up):F(-1)}
def nucleon(a,b):
    # phiMS normsq 6, phiMA 2; weights so total symmetric: (chiMS phiMS)/6 + (chiMA phiMA)/2 (unnormalised OK, we take ratio)
    st={}
    add(st,kron(phiMS(a,b),chiMS),F(1,6)); add(st,kron(phiMA(a,b),chiMA),F(1,2))
    return st
def sigdot(s1,s2):  # sigma_i.sigma_j acting on spin pair -> dict of (s1',s2'):coef
    if s1==s2: return {(s1,s2):F(1)}
    return {(s1,s2):F(-1),(s2,s1):F(2)}
def expect(st, op):
    num=F(0); den=sum(c*c for c in st.values())
    for k,c in st.items():
        for k2,c2 in op(k).items():
            num+=c*c2*st.get(k2,0)
    return num/den
def coul(k):
    return {k:sum(Q[k[i][0]]*Q[k[j][0]] for i,j in [(0,1),(0,2),(1,2)])}
def mag(k):
    out={}
    for i,j in [(0,1),(0,2),(1,2)]:
        qq=Q[k[i][0]]*Q[k[j][0]]
        for (a,b),c in sigdot(k[i][1],k[j][1]).items():
            kk=list(k); kk[i]=(k[i][0],a); kk[j]=(k[j][0],b); kk=tuple(kk)
            out[kk]=out.get(kk,0)+qq*c
    return out
def tot(k): # total spin^2 check via sum sigma.sigma
    out={}
    for i,j in [(0,1),(0,2),(1,2)]:
        for (a,b),c in sigdot(k[i][1],k[j][1]).items():
            kk=list(k); kk[i]=(k[i][0],a); kk[j]=(k[j][0],b); kk=tuple(kk); out[kk]=out.get(kk,0)+c
    return out
for name,(a,b) in {'p':(U,D),'n':(D,U)}.items():
    st=nucleon(a,b)
    print(name,'Coulomb Σqq =',expect(st,coul),' magnetic Σqq σ·σ =',expect(st,mag),' Σσ·σ =',expect(st,tot))

p_c=expect(nucleon(U,D),coul); n_c=expect(nucleon(D,U),coul)
p_m=expect(nucleon(U,D),mag);  n_m=expect(nucleon(D,U),mag)
assert (p_c,n_c,p_m,n_m)==(0,F(-1,3),F(4,3),F(1)), (p_c,n_c,p_m,n_m)
assert n_c-p_c == n_m-p_m == F(-1,3)
print("checks: 2/2 pass; n-p = -1/3 in Coulomb and magnetic channels")
