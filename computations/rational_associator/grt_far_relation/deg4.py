import itertools, numpy as np
p=2147483629
G=['12','13','14','23','24','34']; ix={g:i for i,g in enumerate(G)}
def T(*ns): return {(ix[n],):1 for n in ns}
def add(*xs):
    r={}
    for x in xs:
        for k,v in x.items(): r[k]=r.get(k,0)+v
    return {k:v for k,v in r.items() if v}
def sc(c,x): return {k:c*v for k,v in x.items()}
def mul(a,b):
    r={}
    for k1,v1 in a.items():
        for k2,v2 in b.items(): r[k1+k2]=r.get(k1+k2,0)+v1*v2
    return {k:v for k,v in r.items() if v}
def br(a,b): return add(mul(a,b),sc(-1,mul(b,a)))
def deg(x,d): return {k:v for k,v in x.items() if len(k)==d}
pairs=[('12','34'),('13','24'),('14','23'),('12',('13','23')),('13',('12','23')),('23',('12','13')),
 ('12',('14','24')),('14',('12','24')),('24',('12','14')),('13',('14','34')),('14',('13','34')),('34',('13','14')),
 ('23',('24','34')),('24',('23','34')),('34',('23','24'))]
def el(x): return T(*x) if isinstance(x,tuple) else T(x)
R2=[br(el(a),el(b)) for a,b in pairs]
def ideal_basis(n):
    words=list(itertools.product(range(6),repeat=n)); wi={w:i for i,w in enumerate(words)}
    rows=[]
    for k in range(n-1):
        for a in itertools.product(range(6),repeat=k):
            for b in itertools.product(range(6),repeat=n-2-k):
                for r in R2:
                    v=np.zeros(len(words),dtype=np.int64)
                    for w,c in r.items(): v[wi[a+w+b]]=(v[wi[a+w+b]]+c)%p
                    rows.append(v)
    return np.array(rows),wi
def rref(M):
    M=M.copy()%p; r=0; piv=[]
    for c in range(M.shape[1]):
        nz=np.nonzero(M[r:,c])[0]
        if len(nz)==0: continue
        i=r+nz[0]; M[[r,i]]=M[[i,r]]
        inv=pow(int(M[r,c]),p-2,p); M[r]=(M[r]*inv)%p
        col=M[:,c].copy(); col[r]=0
        nzr=np.nonzero(col)[0]
        M[nzr]=(M[nzr]-np.outer(col[nzr],M[r]))%p
        piv.append(c); r+=1
        if r==M.shape[0]: break
    return M[:r],piv
def inideal(x,B,piv,wi):
    v=np.zeros(len(wi),dtype=np.int64)
    for w,c in x.items(): v[wi[w]]=c%p
    for i,c in enumerate(piv):
        if v[c]: v=(v-v[c]*B[i])%p
    return not v.any()
t12,t13,t14,t23,t24,t34=[T(g) for g in G]
U=add(t13,t23)
def conj3(x,K): return br(x,K)   # deg3 part of (1+K)^-1 x (1+K) = x + xK - Kx
Ka=br(t12,t23); Kb=br(U,t34); Kc=br(t12,add(t23,t24))
d23=conj3(t23,Ka); d34=conj3(t34,Kb); dw=conj3(add(t23,t24),add(Kc,Kb))
d13=sc(-1,d23); d24=add(dw,sc(-1,d23))
X=add(br(t13,d24),br(d13,t24))
import time; t0=time.time()
M,wi=ideal_basis(4); B,piv=rref(M); print('ideal rank',len(piv),'of',len(wi),time.time()-t0)
print('[s13,s24]_4 in ideal:',inideal(X,B,piv,wi))
# controls: s14 = d - s24 - s34 ; check [s14,s23]_4, [s12,s34]_4
d14=sc(-1,add(d24,d34))
print('[s14,s23]',inideal(add(br(t14,d23),br(d14,t23)),B,piv,wi))
print('[s23,s24+s34]',inideal(add(br(t23,add(d24,d34)),br(d23,add(t24,t34))),B,piv,wi))
print('[s12,s14+s24]',inideal(br(t12,add(d14,d24)),B,piv,wi))
print('[s14,s12+s24]',inideal(add(br(t14,d24),br(d14,add(t12,t24))),B,piv,wi))
print('[s34,s13+s14]',inideal(add(br(t34,add(d13,d14)),br(d34,add(t13,t14))),B,piv,wi))
