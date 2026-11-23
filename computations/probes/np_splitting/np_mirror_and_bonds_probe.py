"""Mirror rule on V^3 and coloured bond factors. PRE-REGISTERED: np_mirror_and_bonds_preregistration.md
(commit 51776331e6c). Algebra/trace copied verbatim from np_yokonuma_coloured_probe.py. Exact over Q(q);
x = 0, z = z_D. mpmath only for display at the proton q0. No CODATA selects anything."""
import sympy as sp, mpmath as mp, itertools
q,z,x=sp.symbols('q z x'); h=q-1/q
P3=list(itertools.permutations(range(3)))
def comp(a,b): return tuple(a[b[i]] for i in range(3))
def ln(p): return sum(1 for i in range(3) for j in range(i+1,3) if p[i]>p[j])
S={1:(1,0,2),2:(0,2,1)}
red={(0,1,2):[],S[1]:[1],S[2]:[2],comp(S[1],S[2]):[1,2],comp(S[2],S[1]):[2,1],comp(comp(S[1],S[2]),S[1]):[1,2,1]}
def add(d,k,v):
    d[k]=d.get(k,0)+v
def swap(a,i): a=list(a); a[i-1],a[i]=a[i],a[i-1]; return tuple(a)
def tflip(a,js): a=list(a); [a.__setitem__(j,a[j]^1) for j in js]; return tuple(a)
def lg(i,X):  # g_i * X
    out={}
    for (a,w),c in X.items():
        b=swap(a,i); sw=comp(S[i],w)
        if ln(sw)>ln(w): add(out,(b,sw),c)
        else:
            add(out,(b,sw),c)
            add(out,(b,w),h*c/2); add(out,(tflip(b,[i-1,i]),w),h*c/2)
    return out
def lt(j,X): return {(tflip(a,[j]),w):c for (a,w),c in X.items()}
def mul(X,Y):
    out={}
    for (a,w),c in X.items():
        T=dict(Y)
        for s in reversed(red[w]): T=lg(s,T)
        for j in range(3):
            if a[j]: T=lt(j,T)
        for k,v in T.items(): add(out,k,c*v)
    return {k:sp.together(v) for k,v in out.items() if sp.simplify(v)!=0}
basis=[(a,w) for a in itertools.product((0,1),repeat=3) for w in P3]
one={((0,0,0),(0,1,2)):sp.Integer(1)}
G={i:{((0,0,0),S[i]):sp.Integer(1)} for i in (1,2)}
Tg={j:{(tuple(1 if k==j else 0 for k in range(3)),(0,1,2)):sp.Integer(1)} for j in range(3)}
E={i:{((0,0,0),(0,1,2)):sp.Rational(1,2),(tuple(1 if k in (i-1,i) else 0 for k in range(3)),(0,1,2)):sp.Rational(1,2)} for i in (1,2)}
def lin(X,Y,s=1): 
    out=dict(X); [add(out,k,s*v) for k,v in Y.items()]; return out
def scal(c,X): return {k:c*v for k,v in X.items()}
Ginv={i:lin(G[i],scal(-h,E[i])) for i in (1,2)}
U={b:sp.Symbol('T%d'%n) for n,b in enumerate(basis)}
def trs(X): return sum(c*U[k] for k,c in X.items())
eqs=[U[((0,0,0),(0,1,2))]-1]
for b in basis:
    B={b:sp.Integer(1)}
    for s in list(G.values())+list(Tg.values()):
        eqs.append(trs(mul(s,B))-trs(mul(B,s)))
def inY(b,n):
    a,w=b; return all(a[k]==0 for k in range(n,3)) and all(w[k]==k for k in range(n,3))
for b in basis:
    B={b:sp.Integer(1)}
    if inY(b,2): eqs+= [trs(mul(B,G[2]))-z*U[b], trs(mul(B,Tg[2]))-x*U[b]]
    if inY(b,1): eqs+= [trs(mul(B,G[1]))-z*U[b], trs(mul(B,Tg[1]))-x*U[b]]
sol=sp.solve(eqs,list(U.values()),dict=True)
assert len(sol)==1, sol
sol=sol[0]; print('trace solved; free symbols left:',set().union(*[sp.sympify(v).free_symbols for v in sol.values()]))

zD=q**3/(q**2+1)
def tr(X): return sp.factor(sp.simplify(trs(X).subs(sol).subs({x:0,z:zD})))
def proj(c):
    X=dict(one)
    for j,cj in enumerate(c):
        if cj=='*': continue
        eps=1 if cj in 'up' else -1
        X=mul(X,lin(scal(sp.Rational(1,2),one),scal(sp.Rational(eps,2),Tg[j])))
    return X
def word(c,letters,rule):
    """letters: list of (i, +1/-1). rule M: invert when both strands are d/n."""
    pos=[0,1,2]; X=dict(one)
    for (i,e) in letters:
        a,b=pos[i-1],pos[i]
        if rule=='M' and c[a] in 'dn' and c[b] in 'dn': e=-e
        X=mul(X,G[i] if e>0 else Ginv[i]); pos[i-1],pos[i]=b,a
    return X
def s(c,letters,rule):
    d=tr(proj(c)); 
    return sp.factor(sp.simplify(tr(mul(proj(c),word(c,letters,rule)))/d)) if d!=0 else None
import mpmath as mp
mp.mp.dps=40
from qou_substrate.constants import q_at
q0=mp.mpf(q_at(mp.mp.dps)); me=mp.mpf('0.51099895069'); hb=1-1/q0
E0f=me/(q0*(q0-1))/(1-hb**2)
def ev(e): return sp.lambdify(q,e,'mpmath')(q0)
V3=[(1,1),(2,-1)]*3
print('=== Probe A: V^3 = (g1 g2^-1)^3, s_c = tr(pi_c W)/tr(pi_c)')
flip={'u':'d','d':'u'}
signs={}
for rule in ('0','M'):
    for c in ('uud','udu','duu'):
        cn=''.join(flip[t] for t in c)
        sp_,sn=s(c,V3,rule),s(cn,V3,rule); eps=sp.factor(sp.simplify(sn-sp_))
        print(f' rule {rule}: p={c} s_p={sp_} | n={cn} s_n={sn}')
        print(f'    eps=s_n-s_p={eps}  at q0: {mp.nstr(ev(eps),10)}   E0full*|eps| = {mp.nstr(E0f*abs(ev(eps)),8)} MeV')
        signs[(rule,c)]=sp.sign(ev(eps)) if eps!=0 else 0
print(' A1 (rule 0 all eps=0):', all(signs[('0',c)]==0 for c in ('uud','udu','duu')))
print(' A2 (rule M some eps!=0):', any(signs[('M',c)]!=0 for c in ('uud','udu','duu')))
print(' A3 (rule M signs differ across placements):', len(set(signs[('M',c)] for c in ('uud','udu','duu')))>1, [signs[('M',c)] for c in ('uud','udu','duu')])
print('=== Probe B: bond factors mu_c = tr(pi_c W)/tr(pi_c); mu<1 binds')
B1=[(1,1)]; B2=[(1,1),(1,1)]
for nm,L in (('B1 g',B1),('B2 g^2',B2)):
    for rule in ('0','M'):
        out={}
        for lab,c in (('pp','pp*'),('nn','nn*'),('pn','pn*'),('np','np*')):
            out[lab]=s(c,L,rule)
        vals={k:(mp.nstr(ev(v),10) if v is not None and v!=0 else v) for k,v in out.items()}
        print(f' {nm} rule {rule}:',out,' at q0:',vals)
for rule in ('0','M'):
    print(f' B3 G^3=(g1 g2^-1)^3 rule {rule}:')
    import itertools
    for c in itertools.product('pn',repeat=3):
        c=''.join(c); v=s(c,V3,rule)
        print(f'    {c}: mu={v}  at q0: {mp.nstr(ev(v),10) if v not in (None,0) else v}')
