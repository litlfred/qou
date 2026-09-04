"""Does length additivity hold at EVERY descent node, not just the first?

The corpus probe reports "SOME node works" and "the FIRST node works". Unfolding
the inversion-containment criterion suggests something stronger: row-standardness
alone forces it at ANY descent node, via

    t(i,c) >= t(i,j) > t(i+1,j) >= t(i+1,c')   for c >= j, c' <= j.

If that is right, the Lean theorem needs no minimality hypothesis at all -- which
is a much easier theorem and a stronger result. Decisive test, exact integers.
"""
import sys
sys.path.insert(0, 'computations/hecke')
from murphy_garnir_length_additivity_probe import (
    partitions, row_superstandard, garnir_tableau, row_standard_tableaux,
    is_standard, descent_nodes, d_of, perm_from_tableaux, compose, length)

tot_t = tot_nodes = bad = 0
chain_bad = 0
for n in (3, 4, 5, 6):
    for lam in partitions(n):
        for t in row_standard_tableaux(lam):
            if is_standard(t, lam):
                continue
            tot_t += 1
            dt = d_of(t, lam)
            for (i, j) in descent_nodes(t, lam):
                tot_nodes += 1
                g = garnir_tableau(lam, i, j)
                w = perm_from_tableaux(g, t, lam)
                dg = d_of(g, lam)
                assert compose(w, dg) == dt, "convention error"
                if length(dt) != length(dg) + length(w):
                    bad += 1
                    if bad <= 3:
                        print(f"  FAILS lam={lam} t={t} node=({i},{j})")
                # and check the chain inequality the derivation rests on
                for c in range(j, lam[i]):
                    for cp in range(0, j + 1):
                        if not (t[i][c] > t[i + 1][cp]):
                            chain_bad += 1
print(f"n=3..6: {tot_t} row-standard non-standard tableaux, {tot_nodes} descent nodes")
print(f"    additivity FAILS at a descent node: {bad}")
print(f"    chain inequality t(i,c) > t(i+1,c') violated: {chain_bad}")
print("EVERY DESCENT NODE WORKS" if bad == 0 else "MINIMALITY IS NEEDED")
