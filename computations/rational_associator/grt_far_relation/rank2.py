import itertools
from fractions import Fraction as Fr
gens=['12','13','14','23','24','34']
pairs=list(itertools.combinations(range(6),2))
def L(*ns):
    d={}
    for n in ns: d[gens.index(n)]=d.get(gens.index(n),0)+1
    return d
def add(*ds):
    r={}
    for d in ds:
        for k,v in d.items(): r[k]=r.get(k,0)+v
    return r
def comm(a,b):
    vec=[Fr(0)]*15
    for i,x in a.items():
        for j,y in b.items():
            if i==j: continue
            if i<j: vec[pairs.index((i,j))]+=x*y
            else: vec[pairs.index((j,i))]-=x*y
    return vec
def rank(rows):
    M=[list(r) for r in rows]; rk=0; col=0
    n=len(M[0]) if M else 0
    for col in range(n):
        piv=next((i for i in range(rk,len(M)) if M[i][col]!=0),None)
        if piv is None: continue
        M[rk],M[piv]=M[piv],M[rk]
        for i in range(len(M)):
            if i!=rk and M[i][col]!=0:
                f=M[i][col]/M[rk][col]; M[i]=[a-f*b for a,b in zip(M[i],M[rk])]
        rk+=1
    return rk
def dk3(a,b,c): return [comm(a,add(b,c)),comm(b,add(a,c)),comm(c,add(a,b))]
DK=[comm(L('12'),L('34')),comm(L('13'),L('24')),comm(L('14'),L('23'))]
DK+=dk3(L('12'),L('13'),L('23'))+dk3(L('12'),L('14'),L('24'))+dk3(L('13'),L('14'),L('34'))+dk3(L('23'),L('24'),L('34'))
brk={'P1':[L('12'),L('13','23'),L('14','24','34')],
 'P2':[L('23'),L('12','13'),L('14','24','34')],
 'P3':[L('23'),L('24','34'),L('12','13','14')],
 'P4':[L('34'),L('23','24'),L('12','13','14')],
 'P5':[L('12'),L('34'),L('13','14','23','24')]}
LOC=[]
for k,v in brk.items():
    for a,b in itertools.combinations(v,2): LOC.append(comm(a,b))
print('DK',rank(DK),'LOC',rank(LOC),'both',rank(DK+LOC))
