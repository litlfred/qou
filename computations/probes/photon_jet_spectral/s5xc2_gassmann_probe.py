#!/usr/bin/env python3
"""P9: Gassmann (almost-conjugate, non-conjugate) subgroup pairs in S5 x C2, the full
automorphism group of Bring's surface including orientation-reversing maps.
Subgroups enumerated as all joins of cyclic subgroups (complete for finite groups).
Never reads q0."""
import itertools, json
from pathlib import Path
n = 5
els = [(p, s) for p in itertools.permutations(range(n)) for s in (0, 1)]
def mul(a, b): return (tuple(a[0][b[0][i]] for i in range(n)), (a[1] + b[1]) % 2)
def inv(a):
    r = [0]*n
    for i, x in enumerate(a[0]): r[x] = i
    return (tuple(r), a[1])
e = (tuple(range(n)), 0)
def closure(gens):
    S = {e}; fr = [e]
    while fr:
        nf = []
        for x in fr:
            for g in gens:
                y = mul(x, g)
                if y not in S: S.add(y); nf.append(y)
        fr = nf
    return frozenset(S)
cyc = {closure([g]) for g in els}
subs = set(cyc); frontier = set(cyc)
while frontier:
    new = set()
    for H in frontier:
        for C in cyc:
            if not C <= H:
                J = closure(list(H) + list(C))
                if J not in subs: new.add(J)
    subs |= new; frontier = new
# conjugacy classes of elements
def conj(x, g): return mul(mul(g, x), inv(g))
cls = {}
for x in els:
    if x in cls: continue
    C = frozenset(conj(x, g) for g in els)
    for y in C: cls[y] = C
classes = list(set(cls.values()))
cid = {c: i for i, c in enumerate(classes)}
def profile(H):
    d = [0]*len(classes)
    for h in H: d[cid[cls[h]]] += 1
    return tuple(d)
def conjH(H, g): return frozenset(conj(h, g) for h in H)
reps = []; seen = set()
for H in subs:
    if H in seen: continue
    orb = {conjH(H, g) for g in els}; seen |= orb; reps.append(H)
byp = {}
for H in reps: byp.setdefault(profile(H), []).append(H)
pairs = [(len(v[0]), len(v)) for k, v in byp.items() if len(v) > 1]
out = {'q0Anchor': 'independent', 'q0AnchorReason': 'finite group theory; never reads q0',
       'group': 'S5 x C2', 'order': len(els), 'subgroups': len(subs),
       'conjugacy_classes_of_subgroups': len(reps), 'gassmann_profiles_with_multiple_classes': pairs}
Path(__file__).with_name('s5xc2-gassmann.witness.json').write_text(json.dumps(out, indent=1))
print(out)
