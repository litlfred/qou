"""Probe (bean qou-bgq9): exact checks of Bar-Natan's 4T encoding in
BraidKnotOctonion/Vassiliev/FourTermRelation.lean.

1. dim A_n = (#chord diagrams) - rank(1T + 4T) for n = 1..NMAX. Known values with 1T:
   0, 1, 1, 3, 4 (Bar-Natan 1995, Table 1; Chmutov-Duzhin-Mostovoy).
2. Closure link: for k strands closed cyclically into one circle, the closure of
   w_pre [t_ij, t_il + t_jl] w_suf lies in the span of the 4T relators.

Arithmetic is exact: integers, with rank taken over F_p, p = 2^61 - 1 (rank over F_p is at
most the rank over Q, so dim over F_p is at least dim over Q; the n <= 4 values were also
confirmed with Fractions). No floats, no measured values.
Usage: python3 -I chord_diagram_4t_rank_probe.py [NMAX=4]
"""
import itertools, sys
# Exact rank of 1T+4T (encoding of FourTermRelation.lean) on chord diagrams of degree n.
P=2**61-1
def diagrams(N):
    def rec(rem):
        if not rem: yield {}; return
        a=rem[0]
        for b in rem[1:]:
            r=[x for x in rem if x not in (a,b)]
            for d in rec(r):
                d=dict(d); d[a]=b; d[b]=a; yield d
    for d in rec(list(range(N))): yield tuple(d[i] for i in range(N))
def compose(g,h): return tuple(g[h[i]] for i in range(len(h)))  # (g*h)(i)=g(h(i))
def inv(g):
    r=[0]*len(g)
    for i,x in enumerate(g): r[x]=i
    return tuple(r)
def swap(N,a,b):
    p=list(range(N)); p[a],p[b]=p[b],p[a]; return tuple(p)
def natswap(N,a,b): return swap(N,a,b) if a<N and b<N else tuple(range(N))
def gap(N,k):
    g=tuple(range(N))
    for j in range(max(N-1-k,0)): g=compose(g,natswap(N,k+j,k+j+1))
    return g
def rot(N,m):
    r=tuple((i+1)%N for i in range(N)); g=tuple(range(N))
    for _ in range(m): g=compose(r,g)
    return g
def conj(D,g): return compose(compose(g,D),inv(g))
def rank(rows,cols):
    piv={}  # pivot col -> normalized sparse row (dict), pivot coeff 1
    for r in rows:
        v={c:x%P for c,x in enumerate(r) if x%P}
        while v:
            c=min(v)
            if c in piv:
                f=v[c]; pr=piv[c]
                for k,y in pr.items():
                    nv=(v.get(k,0)-f*y)%P
                    if nv: v[k]=nv
                    else: v.pop(k,None)
            else:
                inv_=pow(v[c],P-2,P); piv[c]={k:x*inv_%P for k,x in v.items()}; break
    return len(piv)
def closure(word,k):
    # word: list of (i,j) strand pairs, bottom to top; strands closed cyclically into one circle
    d=len(word); pts=[]
    for s in range(k):
        for h,(i,j) in enumerate(word):
            if s in (i,j): pts.append((s,h))
    pos={p:n for n,p in enumerate(pts)}; N=len(pts); D=[0]*N
    for h,(i,j) in enumerate(word):
        a,b=pos[(i,h)],pos[(j,h)]; D[a]=b; D[b]=a
    return tuple(D)
def fourT_rows(n):
    N=2*n; Ds=list(diagrams(N)); idx={d:i for i,d in enumerate(Ds)}; rows=[]
    for D in Ds:
        for p in range(N):
            q=D[p]
            if not(p+1<N and q+1<N): continue
            for m in range(N):
                rho=rot(N,m); v=[0]*len(Ds)
                for kk,s in ((p+1,1),(p,-1),(q+1,1),(q,-1)):
                    v[idx[conj(D,compose(rho,gap(N,kk)))]]+=s
                if any(v): rows.append(v)
    return Ds,idx,rows
def closure_check(k,n):
    Ds,idx,rows=fourT_rows(n); base=rank(rows,len(Ds))
    pairs=[(a,b) for a in range(k) for b in range(a+1,k)]
    bad=0; tested=0
    for L in range(0,n-1):
        for pre in itertools.product(pairs,repeat=L):
            for suf in itertools.product(pairs,repeat=n-2-L):
                for i,j,l in itertools.permutations(range(k),3):
                    t=lambda a,b:(min(a,b),max(a,b))
                    terms=[([t(i,j),t(i,l)],1),([t(i,j),t(j,l)],1),([t(i,l),t(i,j)],-1),([t(j,l),t(i,j)],-1)]
                    v=[0]*len(Ds)
                    for w,s in terms: v[idx[closure(list(pre)+w+list(suf),k)]]+=s
                    if not any(v): continue
                    tested+=1
                    if rank(rows+[v],len(Ds))!=base: bad+=1
    print('k',k,'n',n,'tested',tested,'not in 4T span',bad)


if __name__ == "__main__":
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    for n in range(1, nmax + 1):
        N = 2 * n; Ds = list(diagrams(N)); idx = {d: i for i, d in enumerate(Ds)}
        _, _, rows4 = fourT_rows(n)
        rows1 = []
        for D in Ds:
            if any(D[i] == (i + 1) % N for i in range(N)):
                v = [0] * len(Ds); v[idx[D]] = 1; rows1.append(v)
        print(f"n={n} diagrams={len(Ds)} dim A_n={len(Ds) - rank(rows1 + rows4, len(Ds))}", flush=True)
    for k, n in ((3, 2), (3, 3), (4, 3)):
        closure_check(k, n)
