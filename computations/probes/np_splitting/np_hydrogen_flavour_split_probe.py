"""Ruled flavour split eps = E_p - E_n on the four-strand hydrogen element.
PRE-REGISTERED: np_hydrogen_flavour_split_preregistration.md (commit bb861be97f2).
Exact sympy over Q(q); mpmath 40 dps at the proton q0 for display only. CODATA printed for comparison only."""
import sympy as sp, itertools, mpmath as mp
q=sp.symbols('q',positive=True); h=q-1/q
R=sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,q]]); Ri=R.inv()
def gen(i,n,inv): return sp.kronecker_product(sp.kronecker_product(sp.eye(2**i),Ri if inv else R),sp.eye(2**(n-i-2)))
def word(L,n):
    X=sp.eye(2**n)
    for i,e in L: X=X*gen(i,n,e<0)
    return X
K=sp.diag(q,1/q)
def Kn(n):
    X=sp.Matrix([[1]])
    for _ in range(n): X=sp.kronecker_product(X,K)
    return X
def proj(n,strands,nz):
    return sp.diag(*[1 if sum(1 for s in strands if b[s]==0)==nz else 0 for b in itertools.product((0,1),repeat=n)])
def E(W,n,strands,nz): return sp.factor(sp.simplify((Kn(n)*proj(n,strands,nz)*W).trace()/(q+1/q)**n))
mp.mp.dps=40
from qou_substrate.constants import q_at
q0=mp.mpf(q_at(40)); me=mp.mpf('0.51099895069'); hb=1-1/q0; E0f=me/(q0*(q0-1))/(1-hb**2)
def ev(e): return sp.lambdify(q,e,'mpmath')(q0)
V3L=[(0,1),(1,-1)]*3; V3R=[(2,1),(1,-1)]*3
capL=[(2,-1),(1,-1),(0,-1),(0,-1),(1,-1),(2,-1)]  # (s2 s1 s0 s0 s1 s2)^-1 = s2^-1 s1^-1 s0^-1 s0^-1 s1^-1 s2^-1
capR=[(0,-1),(1,-1),(2,-1),(2,-1),(1,-1),(0,-1)]
els={'W0 (V3, no capture)':(V3L,[0,1,2]),
     'W_L cabled':(V3L+capL,[0,1,2]),
     'W_R cabled':(V3R+capR,[1,2,3]),
     'W_adj,L':(V3L+[(2,-1),(2,-1)],[0,1,2]),
     'W_adj,R':(V3R+[(0,-1),(0,-1)],[1,2,3])}
W3=word([(0,1),(1,-1)]*3,3)
e3=sp.factor(sp.simplify(E(W3,3,[0,1,2],2)-E(W3,3,[0,1,2],1)))
print('3-strand eps(V3) =',e3,' at q0',mp.nstr(ev(e3),12),' E0f*eps',mp.nstr(E0f*ev(e3),10))
res={}
for nm,(L,st) in els.items():
    W=word(L,4); tp=E(W,4,st,2); tn=E(W,4,st,1); eps=sp.factor(sp.simplify(tp-tn)); res[nm]=eps
    print('==',nm); print('   E_p =',tp); print('   E_n =',tn)
    print('   t_n/t_p =',sp.factor(sp.simplify(tn/tp)))
    print('   eps =',eps,'  at q0',mp.nstr(ev(eps),12),'  E0full*|eps| =',mp.nstr(E0f*abs(ev(eps)),10),'MeV  (CODATA Q_beta 0.78233341, comparison only)')
    print('   eps - eps3(V3) =',sp.factor(sp.simplify(eps-e3)),'  at q0',mp.nstr(ev(eps-e3),12))
print('H1 W0 == 3-strand:',sp.simplify(res['W0 (V3, no capture)']-e3)==0)
