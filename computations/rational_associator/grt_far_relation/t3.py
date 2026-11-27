# Exact computations over Q (fractions.Fraction) in U(t3), truncated by degree.
# Generators u = t_ab (0), v = t_ac (1), w = t_bc (2); DK3 relations [u,v+w], [v,u+w], [w,u+v].
# Checks the t-compatibility identity TCompat of FarRelation.lean,
#   g(v,w) v g(v,w)^-1 = g(u,w) (v+w) g(u,w)^-1 - w,
# (equivalently H2: g(v,w) v g(v,w)^-1 + g(u,w) u g(u,w)^-1 + w = u+v+w, as u+v+w is central)
# against (5.13) g(u,v)g(v,u)=1 and the mu=0 hexagon (5.14) g(w,u)g(v,w)g(u,v)=1,
# for g = exp(l) with l a Lie element of degree 2 or 3.
import itertools
from fractions import Fraction as Fr
def add(*xs):
    r={}
    for x in xs:
        for k,v in x.items(): r[k]=r.get(k,0)+v
    return {k:v for k,v in r.items() if v}
def sc(c,x): return {k:c*v for k,v in x.items()}
def mul(a,b,D):
    r={}
    for k1,v1 in a.items():
        for k2,v2 in b.items():
            if len(k1)+len(k2)<=D: r[k1+k2]=r.get(k1+k2,0)+v1*v2
    return {k:v for k,v in r.items() if v}
def br(a,b,D): return add(mul(a,b,D),sc(-1,mul(b,a,D)))
U={(0,):Fr(1)}; V={(1,):Fr(1)}; W={(2,):Fr(1)}; ONE={():Fr(1)}
# DK3 relations: [u,v+w],[v,u+w],[w,u+v]
R2=[br(U,add(V,W),9),br(V,add(U,W),9),br(W,add(U,V),9)]
def ideal_red(D):
    # returns reducer for degree-D homogeneous elements, exact
    words=list(itertools.product(range(3),repeat=D)); piv={}
    def reduce(v):
        v=dict(v)
        while True:
            cs=[c for c in v if c in piv]
            if not cs: return v
            c=min(cs); f=v[c]
            for k,x in piv[c].items():
                nv=v.get(k,0)-f*x
                if nv: v[k]=nv
                else: v.pop(k,None)
    for k in range(D-1):
        for a in itertools.product(range(3),repeat=k):
            for b in itertools.product(range(3),repeat=D-2-k):
                for r in R2:
                    g={}
                    for w,c in r.items(): g[a+w+b]=g.get(a+w+b,0)+c
                    g=reduce({x:y for x,y in g.items() if y})
                    if g:
                        c=min(g); f=g[c]; piv[c]={x:y/f for x,y in g.items()}
    return reduce, len(words)-len(piv)
RED={}
def iszero(x,D):
    for d in range(1,D+1):
        if d not in RED: RED[d]=ideal_red(d)
        part={k:v for k,v in x.items() if len(k)==d}
        if d<2:
            if part: return False
            continue
        if RED[d][0](part): return False
    return True
def ev(p,a,b,D):  # p: dict word over {0:X,1:Y}
    r={}
    for w,c in p.items():
        t=ONE
        for l in w: t=mul(t,a if l==0 else b,D)
        r=add(r,sc(c,t))
    return r
def inv1(g,D): # inverse of 1+n
    n=add(g,sc(-1,ONE)); r=ONE; t=ONE
    for k in range(1,D+1):
        t=mul(t,sc(-1,n),D); r=add(r,t)
    return r
X={(0,):Fr(1)}; Y={(1,):Fr(1)}
def lbr(a,b): return br(a,b,9)
def expL(l,D):
    r=ONE;t=ONE
    for k in range(1,D+1):
        t=sc(Fr(1,k),mul(t,l,D)); r=add(r,t)
    return r
sig3=add(lbr(X,lbr(X,Y)),lbr(Y,lbr(X,Y)))
xy=lbr(X,Y)
def conj(g,x,D): return mul(mul(inv1(g,D),x,D),g,D)   # g^-1 x g
def H1(gp,D):
    guv=ev(gp,U,V,D); guw=ev(gp,U,W,D)
    lhs=add(conj(guv,V,D),U,conj(guw,W,D))
    return add(lhs,sc(-1,add(U,V,W)))
def hex514(gp,D,A,B,C):
    return add(mul(mul(ev(gp,C,A,D),ev(gp,B,C,D),D),ev(gp,A,B,D),D),sc(-1,ONE))
def anti(gp,D,A,B): return add(mul(ev(gp,A,B,D),ev(gp,B,A,D),D),sc(-1,ONE))
def conjR(g,x,D): return mul(mul(g,x,D),inv1(g,D),D)  # g x g^-1
def H2(gp,D):
    gvw=ev(gp,V,W,D); guw=ev(gp,U,W,D)
    return add(conjR(gvw,V,D),conjR(guw,U,D),W,sc(-1,add(U,V,W)))
print('H2 sig3 deg5',iszero(H2(expL(sig3,5),5),5),'H2 xy deg4',iszero(H2(expL(xy,4),4),4))
# generic degree-3 element a*XXY + b*YXY: which (a,b) satisfy H2 at deg 4?
for ab in [(1,0),(0,1),(1,-1),(1,1)]:
    l=add(sc(ab[0],lbr(X,lbr(X,Y))),sc(ab[1],lbr(Y,lbr(X,Y))))
    print('H2',ab,iszero(H2(expL(l,4),4),4),'5.14',iszero(hex514(expL(l,4),4,U,V,W),4),'5.13',iszero(anti(expL(l,4),4,U,V),4))
def TC(gp,D):
    gvw=ev(gp,V,W,D); guw=ev(gp,U,W,D)
    return add(conjR(gvw,V,D),sc(-1,conjR(guw,add(V,W),D)),W)
print('TCompat sig3 deg5',iszero(TC(expL(sig3,5),5),5),'TCompat xy deg4',iszero(TC(expL(xy,4),4),4))
