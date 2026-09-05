"""Cut a positive-dimensional Ptolemy component to dimension 0 with random hyperplanes.

msolve refuses to parametrise a positive-dimensional ideal.  Adding d generic linear
forms, where d is the dimension, leaves finitely many points -- and over a large field a
random slice meets every component, so non-emptiness is preserved with high probability.
The point count then confirms the slice landed, and over Q the same construction yields
algebraic solutions that are genuine complex representations.
"""
import sys, random
src, nslice, ch = sys.argv[1], int(sys.argv[2]), sys.argv[3]
L = open(src).read().strip().split('\n')
vs = L[0].split(','); polys = [p.rstrip(',').strip() for p in L[2:] if p.strip().rstrip(',')]
random.seed(20260905 + nslice)
lin = []
for i in range(nslice):
    cs = [random.randint(1, 30000) for _ in vs]
    lin.append(" + ".join(f"{c}*{v}" for c, v in zip(cs, vs)) + f" + {random.randint(1,30000)}")
out = src.replace('.ms', f'_sl{nslice}.ms')
with open(out, 'w') as f:
    f.write(",".join(vs) + "\n" + ch + "\n" + ",\n".join(polys + lin) + "\n")
print(f"{out}: {len(vs)} vars, {len(polys)}+{nslice} eqs")
