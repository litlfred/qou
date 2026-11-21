"""Generator for QOU/QuarkState/GammaGammaFourStrandPureBound.lean (bean qou-a1hh).
Exact sympy arithmetic only; no floating point. Output is reviewed and committed by hand.
"""
import sympy as sp, itertools, json
from pathlib import Path
HERE=Path(__file__).resolve().parent
from fractions import Fraction as F
q,t=sp.symbols('q t',positive=True)
def syts(shape):
    n=sum(shape); out=[]
    def rec(f,e,pos):
        if e>n: out.append(dict(pos)); return
        for r in range(len(shape)):
            c=f[r]
            if c<shape[r] and (r==0 or f[r-1]>c):
                f[r]+=1; pos[e]=(r,c); rec(f,e+1,pos); f[r]-=1; del pos[e]
    rec([0]*len(shape),1,{}); return out
def a(d): return sp.cancel((q-1/q)*q**(2*d)/(q**(2*d)-1))
def gens(lam):
    T=syts(lam); n=len(T); G=[]
    for i in range(1,4):
        M=sp.zeros(n,n)
        for x,tt in enumerate(T):
            (r1,c1),(r2,c2)=tt[i],tt[i+1]; d=(c2-r2)-(c1-r1)
            M[x,x]=a(d)
            if r1!=r2 and c1!=c2:
                s=dict(tt); s[i],s[i+1]=tt[i+1],tt[i]; y=T.index(s)
                M[y,x]= 1 if x<y else sp.cancel(a(d)*a(-d)+1)
        G.append(M)
    return T,G
h=q-1/q
BLK={}
for lam in [(3,1),(2,2)]:
    T,G=gens(lam); n=len(T)
    let={}
    for i,g in enumerate(G):
        let['s%d'%(i+1)]=g; let['i%d'%(i+1)]=(g-h*sp.eye(n)).applyfunc(sp.cancel)
    # check inverse, braid
    for i in range(3):
        assert sp.simplify(let['s%d'%(i+1)]*let['i%d'%(i+1)]-sp.eye(n))==sp.zeros(n,n)
    G0=[g.subs(q,1) for g in G]
    BLK[lam]=(T,let,G0)
# closure table jointly
def swap(i):  # generator index i in 0..2 -> perm tuple
    p=list(range(4)); p[i],p[i+1]=p[i+1],p[i]; return tuple(p)
def comp(f,s): return tuple(f[s[x]] for x in range(4))
start=(tuple(range(4)),sp.eye(3),sp.eye(2))
tbl=[start]; key=lambda e:(e[0],tuple(e[1]),tuple(e[2]))
idx={key(start):0}; nxt={}
k=0
while k<len(tbl):
    f,A,B=tbl[k]
    for j in range(3):
        e=(comp(f,swap(j)),A*BLK[(3,1)][2][j],B*BLK[(2,2)][2][j])
        kk=key(e)
        if kk not in idx: idx[kk]=len(tbl); tbl.append(e)
        nxt[(k,j)]=idx[kk]
    k+=1
print('table size',len(tbl))
perms=[e[0] for e in tbl]; assert len(set(perms))==24
def ninf(X): return max(sum(abs(X[i,j]) for j in range(X.shape[1])) for i in range(X.shape[0]))
print('M31',max(ninf(e[1]) for e in tbl),'M22',max(ninf(e[2]) for e in tbl))
# entry bounds
def cert_ok(poly):  # poly in t, need >=0 on [0,1/10] via greedy carry
    P=sp.Poly(sp.expand(poly),t); co=[sp.Rational(c) for c in reversed(P.all_coeffs())]  # co[k]
    for kk in range(len(co)-1,0,-1):
        if co[kk]<0: co[kk-1]+=co[kk]/10; co[kk]=0
    return co[0]>=0
entries={}
for lam,(T,let,G0) in BLK.items():
    n=len(T)
    for name,M in let.items():
        P0=G0[int(name[1])-1]
        for i in range(n):
            for j in range(n):
                e=sp.cancel(M[i,j]); N,D=sp.fraction(sp.together(e))
                N=sp.expand(N); D=sp.expand(D)
                if sp.Poly(D,q).LC()<0: N,D=-N,-D
                p=sp.Rational(P0[i,j])
                assert sp.simplify(N.subs(q,1)/D.subs(q,1)-p)==0
                Nt=sp.expand(N.subs(q,1+t)); Dt=sp.expand(D.subs(q,1+t))
                assert cert_ok(Dt-sp.Rational(1,10**6)), (name,i,j,D)
                diff=Nt-p*Dt
                c=sp.Rational(0)
                while not (cert_ok(c*t*Dt-diff) and cert_ok(c*t*Dt+diff)):
                    c+=sp.Rational(1,100)
                entries[(lam,name,i,j)]=(N,D,p,c)
for lam,(T,let,G0) in BLK.items():
    n=len(T); worst=0
    for name in let:
        for i in range(n):
            s=sum(entries[(lam,name,i,j)][3] for j in range(n)); worst=max(worst,s)
    print(lam,'K row max',worst)
import pickle
pickle.dump(dict(BLK={k:(v[0],{n:list(m) for n,m in v[1].items()},[list(g) for g in v[2]]) for k,v in BLK.items()},tbl=[(e[0],list(e[1]),list(e[2])) for e in tbl],nxt=nxt,entries=entries),open(HERE/'data.pkl','wb'))
