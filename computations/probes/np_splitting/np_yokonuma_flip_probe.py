"""Coloured-strand flip probe. PRE-REGISTERED: np_yokonuma_flip_preregistration.md (commit 711b82f418).
Algebra, trace system and basis copied verbatim from np_yokonuma_coloured_probe.py.
Exact over Q(q, z, x, phi0, phi1, phi01). No float, no CODATA, nothing fitted."""
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

def tr(X): return sp.factor(sp.simplify(trs(X).subs(sol)))
def proj(c):
    X=dict(one)
    for j,cj in enumerate(c):
        eps=1 if cj=='u' else -1
        X=mul(X,lin(scal(sp.Rational(1,2),one),scal(sp.Rational(eps,2),Tg[j])))
    return X
def phi(X): return {(a,w):(-1)**sum(a)*c for (a,w),c in X.items()}
def eq(X,Y):
    k=set(X)|set(Y); return all(sp.simplify(X.get(i,0)-Y.get(i,0))==0 for i in k)
zD=q**3/(q**2+1)
# Y1: automorphism
bad=0
for b1 in basis:
    for b2 in basis:
        B1={b1:sp.Integer(1)}; B2={b2:sp.Integer(1)}
        if not eq(phi(mul(B1,B2)),mul(phi(B1),phi(B2))): bad+=1
print('Y1 automorphism: failures',bad,'of',len(basis)**2, 'PASS' if bad==0 else 'FAIL')
# Y2: trace invariance
b0=bx=0
for b in basis:
    B={b:sp.Integer(1)}
    t1=tr(phi(B)); t0=tr(B)
    if sp.simplify((t1-t0).subs(x,0))!=0: b0+=1
    if sp.simplify(t1-t0.subs(x,-x))!=0: bx+=1
print('Y2 trace phi-invariant at x=0: failures',b0,'/48;  tr(phi b)(x)=tr(b)(-x): failures',bx,'/48', 'PASS' if b0==bx==0 else 'FAIL')
f0,f1,f01=sp.symbols('phi0 phi1 phi01')
def pw(*fs): 
    X=dict(one)
    for f in fs: X=mul(X,f)
    return X
G12i=mul(G[1],Ginv[2])
def photon(a,b,c): return lin(lin(lin(dict(one),scal(a,G[1])),scal(b,G[2])),scal(c,G12i))
hh=q-1/q
words={'V3=(g1 g2^-1)^3':pw(G12i,G12i,G12i),
 'photon gamma(0,0,q h)':photon(0,0,q*hh),
 'photon gamma(0,0,-h/q)':photon(0,0,-hh/q),
 'product of the two photons':mul(photon(0,0,q*hh),photon(0,0,-hh/q)),
 'generic photon':photon(f0,f1,f01),
 'half twist g1g2g1':pw(G[1],G[2],G[1]),
 'full twist (g1g2g1)^2':pw(G[1],G[2],G[1],G[1],G[2],G[1])}
flip={'u':'d','d':'u'}
y3=y4=0; n=0
for nm,W in words.items():
    print('==',nm)
    if nm.startswith('product'):
        print('   product == V3 :', eq(W,words['V3=(g1 g2^-1)^3']))
    for c in ('uud','udu','duu'):
        cn=''.join(flip[s] for s in c)
        tp=tr(mul(proj(c),W)); tn=tr(mul(proj(cn),W)); n+=1
        ok3=sp.simplify((tn-tp).subs(x,0))==0; ok4=sp.simplify(tn-tp.subs(x,-x))==0
        y3+=not ok3; y4+=not ok4
        print(f'   p={c} n={cn}: tr_p(x=0, z=zD)=',sp.factor(sp.simplify(tp.subs({x:0,z:zD}))),
              '| n-p at x=0 is 0:',ok3,'| tr_n(x)=tr_p(-x):',ok4)
        print('      n-p (symbolic x, z=zD) =',sp.factor(sp.simplify((tn-tp).subs(z,zD))))
print('Y3: failures',y3,'of',n,'PASS' if y3==0 else 'FAIL')
print('Y4: failures',y4,'of',n,'PASS' if y4==0 else 'FAIL')
