import itertools, numpy as np, sys
exec(open('deg4.py').read().split("t12,t13,t14")[0])
p=int(sys.argv[1]) if len(sys.argv)>1 else 2147483629
def rrefp(M):
    M=M.copy()%p; r=0; piv=[]
    for c in range(M.shape[1]):
        if r==M.shape[0]: break
        nz=np.nonzero(M[r:,c])[0]
        if len(nz)==0: continue
        i=r+nz[0]; M[[r,i]]=M[[i,r]]
        M[r]=(M[r]*pow(int(M[r,c]),p-2,p))%p
        col=M[:,c].copy(); col[r]=0; nzr=np.nonzero(col)[0]
        if len(nzr): M[nzr]=(M[nzr]-(col[nzr,None]*M[r][None,:])%p)%p
        piv.append(c); r+=1
    return M[:r],piv
# degree 4
M,wi4=ideal_basis(4); B4,piv4=rrefp(M)
free4=[c for c in range(1296) if c not in set(piv4)]; fi={c:i for i,c in enumerate(free4)}
# projection of a degree-4 vector to U4 coords: v - sum v[piv]*B ; coords = entries at free cols
proj=np.zeros((1296,len(free4)),dtype=np.int64)
for w,j in wi4.items():
    v=np.zeros(1296,dtype=np.int64); v[j]=1
    for i,c in enumerate(piv4):
        if v[c]: v=(v-v[c]*B4[i])%p
    proj[j]=v[free4]
D=len(free4); print('dim U4',D)
# V⊗U4 coords: index a*D+k. map degree5 word (a,w4) -> e_a ⊗ proj[w4]
def map5(x):
    out=np.zeros(6*D,dtype=np.int64)
    for w,c in x.items():
        out[w[0]*D:(w[0]+1)*D]=(out[w[0]*D:(w[0]+1)*D]+c%p*proj[wi4[w[1:]]])%p
    return out
# relations I4⊗V: basis rows B4 (degree-4 ideal) appended with letter b
rows=[]
words4=list(wi4.keys())
for i in range(B4.shape[0]):
    nzc=np.nonzero(B4[i])[0]
    for b in range(6):
        x={}
        for c in nzc: x[words4[c]+(b,)]=int(B4[i][c])
        rows.append(map5(x))
B5,piv5=rrefp(np.array(rows)); print('rels rank',len(piv5),'dim U5',6*D-len(piv5))
def in5(x):
    v=map5(x)
    for i,c in enumerate(piv5):
        if v[c]: v=(v-v[c]*B5[i])%p
    return not v.any()
