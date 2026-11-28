import sys; sys.path.insert(0,'.'); sys.path.insert(0, __import__('os').path.dirname(__file__))
from two_colour_probe import *
t,z=sp.symbols('t z')
h=sp.symbols('h')
def burau(wd,n=3):
    M=sp.eye(n-1)
    for (i,e) in wd:
        B=sp.eye(n-1)
        # reduced Burau
        B[i,i]=-t
        if i>0: B[i,i-1]=t
        if i<n-2: B[i,i+1]=1
        if e<0: B=B.inv()
        M=B*M
    return M
def conway(wd,n=3):
    D=sp.factor(sp.cancel((sp.eye(n-1)-burau(wd,n)).det()*(1-t)/(1-t**n)))
    # symmetrise
    p=sp.Poly(sp.expand(D*t**20),t); deg=[m[0] for m in p.monoms()]
    sh=(max(deg)+min(deg))
    Ds=sp.expand(D*t**20*t**sp.Rational(-sh,2))
    return Ds
def lkof(wd):
    cyc,cid,sw=components(wd)
    pos=list(range(3));l=0
    for (i,e) in wd:
        if cid[pos[i]]!=cid[pos[i+1]]: l+=e
        pos[i],pos[i+1]=pos[i+1],pos[i]
    return sp.Rational(l,2)
def k23(wd):
    cyc,cid,sw=components(wd); cs=(1,1)
    M,c=word_rep(wd,[1,1,1])
    J=qtrace(M,c)*sp.prod([theta(1)**(-sw[i]) for i in range(2)])
    C=sp.simplify(J/qi(2)**2)
    ser=sp.expand(sp.simplify(sp.series(sp.log(C.subs(s,sp.exp(h/2))),h,0,4).removeO()))
    return ser.coeff(h,2)/9, ser.coeff(h,3)/9
import itertools
fam={}
for k in range(-2,3):
    fam[f's0^{2*k+2} s1- s0 s1-']=[P(0)]*(2*k+2) if k>=-1 else [N(0)]*(-(2*k+2))
for nm in list(fam):
    fam[nm]=fam[nm]+[N(1),P(0),N(1)]
fam['s0^2 s1 s0 s1-']=[P(0),P(0),P(1),P(0),N(1)]
fam['s0^2 s1 s0 s1']=[P(0),P(0),P(1),P(0),P(1)]
fam['s0^4 s1- s0^-1 s1-']=[P(0)]*4+[N(1),N(0),N(1)]
for nm,wd in fam.items():
    cyc,_,_=components(wd)
    if len(cyc)!=2: print(nm,'comps',len(cyc)); continue
    k2,k3=k23(wd); L=lkof(wd); cw=conway(wd)
    print(nm,'lk',L,'k2',k2,'k3',k3,'k3+(lk^3-lk)/9=',sp.nsimplify(k3+(L**3-L)/9),'Alex(sym)=',cw);sys.stdout.flush()
