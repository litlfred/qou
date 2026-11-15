#!/usr/bin/env python3
"""Compare reading-3 passes (gg-four-strand.witness.json) with the pure-braid condition.

The permutation of a gamma-gamma word forgets orientation: V_s and Vbar_s both map to s_{s+1}s_{s+2}.
Exploratory check (post hoc, not pre-registered); exact combinatorics, no floats. Bean qou-a1hh.
"""
import json, itertools
wit=json.load(open('gg-four-strand.witness.json')); res=wit['results']
def perm(ts):
    p=list(range(4))
    for t in ts:
        s=int(t[1])+1
        for g in (s,s+1):           # s_g swaps positions g-1,g (0-indexed)
            p[g-1],p[g]=p[g],p[g-1]
    return tuple(p)
from collections import Counter
for m in range(1,7):
    c=Counter()
    for ts in itertools.product(["V0","B0","V1","B1"],repeat=m):
        name=".".join(ts); pure=perm(ts)==(0,1,2,3); ps=res[name]['passes_alone']
        c[(pure,ps)]+=1
    print(m, "pure&pass",c[(True,True)],"pure&fail",c[(True,False)],"notpure&pass",c[(False,True)],"notpure&fail",c[(False,False)])
