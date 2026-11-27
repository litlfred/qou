import itertools
from fractions import Fraction as Fr
exec(open('rank2.py').read().split("DK=[")[0])
brk={'P1':[L('12'),L('13','23'),L('14','24','34')],
 'P2':[L('23'),L('12','13'),L('14','24','34')],
 'P3':[L('23'),L('24','34'),L('12','13','14')],
 'P4':[L('34'),L('23','24'),L('12','13','14')],
 'P5':[L('12'),L('34'),L('13','14','23','24')]}

names=['12','13','14','23','24','34']
def lab(d): return '+'.join('s'+names[k] for k in sorted(d) for _ in range(d[k]))
DKp=[('12','34'),('13','24'),('14','23'),('12',('13','23')),('13',('12','23')),('23',('12','13')),
 ('12',('14','24')),('14',('12','24')),('24',('12','14')),('13',('14','34')),('14',('13','34')),('34',('13','14')),
 ('23',('24','34')),('24',('23','34')),('34',('23','24'))]
def el(x): return L(*x) if isinstance(x,tuple) else L(x)
targets=[(el(a),el(b)) for a,b in DKp]
facts=[]
for k,v in brk.items():
    for a,b in itertools.combinations(v,2): facts.append((k,a,b))
facts.append(('far',L('13'),L('24')))
FV=[comm(a,b) for _,a,b in facts]
def solve(target):
    # find c with sum c_i FV_i = target (15 eq, 16 unknowns) by gaussian elim on augmented
    n=len(FV); A=[[FV[j][i] for j in range(n)]+[target[i]] for i in range(15)]
    piv=[];r=0
    for c in range(n):
        pr=next((i for i in range(r,15) if A[i][c]!=0),None)
        if pr is None: continue
        A[r],A[pr]=A[pr],A[r]; f=A[r][c]; A[r]=[x/f for x in A[r]]
        for i in range(15):
            if i!=r and A[i][c]!=0:
                g=A[i][c]; A[i]=[x-g*y for x,y in zip(A[i],A[r])]
        piv.append(c); r+=1
    assert all(A[i][-1]==0 for i in range(r,15))
    sol=[Fr(0)]*n
    for i,c in enumerate(piv): sol[c]=A[i][-1]
    return sol
for (a,b),(x,y) in zip(DKp,targets):
    s=solve(comm(x,y))
    print(a,b,[(i,str(c)) for i,c in enumerate(s) if c])
print([(i,f[0],lab(f[1]),lab(f[2])) for i,f in enumerate(facts)])
# t-side: local commutations in terms of DK relations
DKV=[comm(x,y) for x,y in targets]
FV2=FV; FV=DKV
for i,(k,a,b) in enumerate(facts[:-1]):
    s=solve(comm(a,b)); print('loc',i,[(j,str(c)) for j,c in enumerate(s) if c])
