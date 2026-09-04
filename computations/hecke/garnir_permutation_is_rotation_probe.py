"""Is the Garnir permutation just a CYCLIC ROTATION of the label interval [a,b]?

Hypothesis: d(g_{ij}) acts on labels as
    x |-> a + ((x - a) + (j+1)) mod (b - a + 1)   for x in [a,b],   identity elsewhere
i.e. rotate the interval [a,b] by (j+1). If so, the Lean object is a rotation on
an interval, not a bespoke bijection needing its own surjectivity proof.
"""
import sys
sys.path.insert(0, 'computations/hecke')
from murphy_garnir_length_additivity_probe import (
    partitions, row_superstandard, garnir_tableau, cells_of, entry_at)

def label_map(lam, i, j):
    """x -> label that cell-of-x-in-t^lam carries in g."""
    tl, g = row_superstandard(lam), garnir_tableau(lam, i, j)
    return {entry_at(tl, c): entry_at(g, c) for c in cells_of(lam)}

total = bad = 0
for n in (3, 4, 5, 6, 7):
    for lam in partitions(n):
        for i in range(len(lam) - 1):
            for j in range(lam[i + 1]):
                total += 1
                tl = row_superstandard(lam)
                a, b = tl[i][j], tl[i + 1][j]
                m, got = b - a + 1, label_map(lam, i, j)
                want = {}
                for x in range(1, n + 1):
                    want[x] = a + ((x - a) + (j + 1)) % m if a <= x <= b else x
                if want != got:
                    bad += 1
                    if bad <= 2:
                        print(f"  MISMATCH lam={lam} (i,j)=({i},{j}) a={a} b={b} m={m}")
                        print(f"    want {want}")
                        print(f"    got  {got}")
print(f"n=3..7: {total} cases, {bad} mismatches")
print("ROTATION CONFIRMED" if bad == 0 else "NOT A ROTATION")
