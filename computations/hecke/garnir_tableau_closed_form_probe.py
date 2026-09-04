"""Validate a CLOSED FORM for the Garnir tableau against the corpus reference.

Claim (0-indexed rows/cols, 1-based labels, a = t^L(i,j)):
    g(i+1, c) = a + c                  for 0 <= c <= j
    g(i,   c) = a + (j+1) + (c - j)    for j <= c < rowLen(i)
all other cells keep their t^L label.

If this holds, the Lean definition can be this formula rather than a
"place a..b in order" procedure -- which is the difference between defining a
bijection by a rule and defining it by a sorting algorithm.
"""
import sys
sys.path.insert(0, 'computations/hecke')
from murphy_garnir_length_additivity_probe import (
    partitions, row_superstandard, garnir_tableau)

def closed_form(lam, i, j):
    t0 = row_superstandard(lam)
    a = t0[i][j]
    rows = [list(r) for r in t0]
    for c in range(0, j + 1):
        rows[i + 1][c] = a + c
    for c in range(j, lam[i]):
        rows[i][c] = a + (j + 1) + (c - j)
    return tuple(tuple(r) for r in rows)

total = mismatch = 0
for n in (3, 4, 5, 6, 7):
    for lam in partitions(n):
        for i in range(len(lam) - 1):
            for j in range(lam[i + 1]):        # (i+1,j) must be a cell
                total += 1
                want, got = garnir_tableau(lam, i, j), closed_form(lam, i, j)
                if want != got:
                    mismatch += 1
                    if mismatch <= 3:
                        print(f"  MISMATCH lam={lam} (i,j)=({i},{j})")
                        print(f"    reference   {want}")
                        print(f"    closed form {got}")
print(f"n=3..7: {total} Garnir tableaux checked, {mismatch} mismatches")
print("CLOSED FORM VALIDATED" if mismatch == 0 else "CLOSED FORM WRONG")
