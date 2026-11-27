# exact rational check: is [s13,s24]_4 in the degree-4 DK ideal? (g degree-2 part = [X,Y])
exec(open('deg4.py').read().split("import time")[0])
from fractions import Fraction as Fr
import itertools
words=list(itertools.product(range(6),repeat=4)); wi={w:i for i,w in enumerate(words)}
gens=[]
for k in range(3):
    for a in itertools.product(range(6),repeat=k):
        for b in itertools.product(range(6),repeat=2-k):
            for r in R2:
                v={}
                for w,c in r.items(): v[wi[a+w+b]]=v.get(wi[a+w+b],0)+Fr(c)
                v={i:c for i,c in v.items() if c}
                if v: gens.append(v)
piv={}  # pivot col -> row (dict), rows reduced w.r.t. earlier pivots, pivot coeff 1
def reduce(v):
    v=dict(v)
    while True:
        cols=[c for c in v if c in piv]
        if not cols: return v
        c=min(cols); f=v[c]
        for k,x in piv[c].items():
            nv=v.get(k,0)-f*x
            if nv: v[k]=nv
            else: v.pop(k,None)
for g in gens:
    v=reduce(g)
    if v:
        c=min(v); f=v[c]; piv[c]={k:x/f for k,x in v.items()}
print('rank',len(piv))
def vec(x): 
    v={}
    for w,c in x.items(): v[wi[w]]=v.get(wi[w],0)+Fr(c)
    return {k:c for k,c in v.items() if c}
r=reduce(vec(X)); print('[s13,s24]_4 residual nonzero entries:',len(r))
