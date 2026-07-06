import numpy as np
np.set_printoptions(suppress=True)
r=8; nsite=4
def so(site,spin): return 2*site+spin
T=np.zeros((r,r)); Rf=np.zeros((r,r))
for site in range(nsite):
    for spin in range(2):
        T[so((site+1)%4,spin),so(site,spin)]=1
        Rf[so((4-site)%4,spin),so(site,spin)]=1
Sz1=np.zeros((r,r)); Sp1=np.zeros((r,r)); Sm1=np.zeros((r,r))
for site in range(nsite):
    Sz1[so(site,0),so(site,0)]=+0.5; Sz1[so(site,1),so(site,1)]=-0.5   # FIX: spin-1/2
    Sp1[so(site,0),so(site,1)]=1; Sm1[so(site,1),so(site,0)]=1

pairs=[(i,j) for i in range(r) for j in range(i+1,r)]
P=len(pairs); pidx={p:k for k,p in enumerate(pairs)}
def wedge_group(g):
    M=np.zeros((P,P))
    for k,(i,j) in enumerate(pairs):
        gi=g[:,i]; gj=g[:,j]
        for a in range(r):
            if abs(gi[a])<1e-12: continue
            for b in range(r):
                if abs(gj[b])<1e-12 or a==b: continue
                aa,bb=(a,b) if a<b else (b,a); sgn=1 if a<b else -1
                M[pidx[(aa,bb)],k]+=sgn*gi[a]*gj[b]
    return M
def wedge_gen(O):
    M=np.zeros((P,P))
    for k,(i,j) in enumerate(pairs):
        for a in range(r):
            if abs(O[a,i])>1e-12 and a!=j:
                aa,bb=(a,j) if a<j else (j,a); M[pidx[(aa,bb)],k]+=(1 if a<j else -1)*O[a,i]
            if abs(O[a,j])>1e-12 and a!=i:
                aa,bb=(i,a) if i<a else (a,i); M[pidx[(aa,bb)],k]+=(1 if i<a else -1)*O[a,j]
    return M

Tw=wedge_group(T); Rw=wedge_group(Rf)
Szw=wedge_gen(Sz1); Spw=wedge_gen(Sp1); Smw=wedge_gen(Sm1)
S2=Szw@Szw+0.5*(Spw@Smw+Smw@Spw)
w,V=np.linalg.eigh(S2); w=np.round(w,5)
print("S^2 eigenvalues (expect 0=singlet, 2=triplet):", dict(zip(*[list(x) for x in np.unique(w,return_counts=True)])))

# projectors onto S=0 (val 0) and S=1 (val 2)
def sector(val):
    cols=[i for i in range(P) if abs(w[i]-val)<1e-4]; return V[:,cols]
B0=sector(0.0); B1=sector(2.0)
print("dim S=0 sector =",B0.shape[1]," dim S=1 sector =",B1.shape[1])

# D4 character table, classes [E,2C4,C2,2sv,2sd], sizes [1,2,1,2,2]
irr={'A1':[1,1,1,1,1],'A2':[1,1,1,-1,-1],'B1':[1,-1,1,1,-1],'B2':[1,-1,1,-1,1],'E':[2,0,-2,0,0]}
sizes=[1,2,1,2,2]
reps=[np.eye(P), Tw, Tw@Tw, Rw, Tw@Rw]   # E, C4, C2, sigma_v, sigma_d
def char_on(Bsub, spinmult):
    proj=Bsub@Bsub.T
    return [np.trace(Bsub.T@g@Bsub)/spinmult for g in reps]
def decompose(chi):
    out={}
    for name,c in irr.items():
        m=sum(sizes[k]*c[k]*chi[k] for k in range(5))/8
        if round(m)!=0: out[name]=int(round(m))
    return out
c0=char_on(B0,1)           # S=0: spin mult 1
c1=char_on(B1,3)           # S=1: triplet 3-fold; divide to get spatial multiplicities
print("\nS=0 (Sym^2 C^4) under D4:", decompose(c0))
print("S=1 (Lambda^2 C^4) under D4:", decompose(c1))
blocks=list(decompose(c0).values())+list(decompose(c1).values())
print("\nNON-ABELIAN (D4 x SU(2)) SDP block sizes:", sorted(blocks,reverse=True))
print("   max block =",max(blocks)," sum size^3 =",sum(b**3 for b in blocks),
      " commutant dim Sum m^2 =",sum(b*b for b in blocks))
