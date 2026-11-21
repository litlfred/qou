# Pre-registered: level-N (N=3) Jimbo R on (C^N)^{⊗3}, K = diag(q^{N-1},...,q^{1-N}).
# Prediction (from Hecke-module argument): restricted-trace ratio n/p = q^{∓2} for adjacent (u,d),
# independent of word. Report also non-adjacent placement, labelled as a choice.
import itertools, sympy as sp
q=sp.Rational(11099785827513808,10**16)
def R(N):
    d=N*N; M=sp.zeros(d,d)
    idx=lambda i,j:i*N+j
    for i in range(N):
        for j in range(N):
            if i==j: M[idx(i,i),idx(i,i)]=q
            elif i<j: M[idx(j,i),idx(i,j)]=1
            else:
                M[idx(j,i),idx(i,j)]=1; M[idx(i,j),idx(i,j)]=q-1/q
    return M
def gen(N,k,n=3):
    I=sp.eye(N); Rm=R(N)
    if k==1: return sp.kronecker_product(Rm,I)
    return sp.kronecker_product(I,Rm)
N=3
s1,s2=gen(N,1),gen(N,2)
# hecke check
for s in (s1,s2): assert sp.simplify(s*s-(q-1/q)*s-sp.eye(N**3))==sp.zeros(N**3,N**3)
assert s1*s2*s1==s2*s1*s2
Kd=[q**(N-1-2*i) for i in range(N)]
words={'half twist s1s2s1':s1*s2*s1,'full twist (s1s2)^3':(s1*s2)**3,'s1s2':s1*s2}
def wt(state): # state tuple of basis indices
    c=[0]*N
    for x in state: c[x]+=1
    return tuple(c)
basis=list(itertools.product(range(N),repeat=3))
def restricted(W,w):
    t=0
    for b,st in enumerate(basis):
        if wt(st)==w:
            k=1
            for x in st: k*=Kd[x]
            t+=k*W[b,b]
    return t
for (u,d) in [(0,1),(1,2),(0,2)]:
    pw=[0]*N; pw[u]+=2; pw[d]+=1
    nw=[0]*N; nw[u]+=1; nw[d]+=2
    for name,W in words.items():
        r=restricted(W,tuple(nw))/restricted(W,tuple(pw))
        print(f"u=e{u+1} d=e{d+1} {name}: n/p = q^{sp.N(sp.log(r)/sp.log(q),12)}")
