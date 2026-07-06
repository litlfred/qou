import sys
import sympy as sp
from collections import defaultdict
import pyhecke_native
from kazhdan_lusztig import permutations_S_n

def rsk(w):
    P = []
    Q = []
    for i, x in enumerate(w):
        r = 0
        while r < len(P):
            idx = -1
            for c in range(len(P[r])):
                if P[r][c] > x:
                    idx = c
                    break
            if idx == -1:
                P[r].append(x)
                Q[r].append(i + 1)
                break
            else:
                x, P[r][idx] = P[r][idx], x
                r += 1
        if r == len(P):
            P.append([x])
            Q.append([i + 1])
    return tuple(len(row) for row in P)

def partitions_of(n):
    if n == 0: yield ()
    for p in partitions_of(n - 1):
        yield (p[0] + 1,) + p[1:]
        if len(p) == 1 or p[1] < p[0]:
            yield (1,) + p

def get_flambda(lam):
    def hook_length(lam, i, j):
        return (lam[i] - j) + sum(1 for row in lam[i+1:] if row > j)
    import math
    n = sum(lam)
    f = math.factorial(n)
    for i in range(len(lam)):
        for j in range(lam[i]):
            f //= hook_length(lam, i, j)
    return f

def main():
    print("Collecting KL Betti sums up to S_6 to derive proxy...")
    for n in range(3, 7):
        perms = permutations_S_n(n)
        left_cells = defaultdict(list)
        for p in perms:
            lam = rsk(p)
            left_cells[lam].append(p)
        
        # for each shape, pick a canonical left cell (the one containing the first element)
        # WARNING (2026-06-25): the Betti sum is NOT cell-invariant — distinct left
        # cells of the same shape give different sums (e.g. (3,3): 6..23 over S_6).
        # This first-cell choice picks the low end; probe_option_e_probe4_kl_batch.py's
        # canonical_Q picks a high cell. B_λ is therefore not a function of λ.
        # See kl_betti_cell_dependence_probe.py + kl-betti-cell-dependence.witness.json.
        shape_betti = {}
        for lam, p_list in left_cells.items():
            # pick one element from the shape to find its left cell
            w0 = p_list[0]
            # wait, a left cell is determined by the Q tableau. 
            # let's group by Q tableau:
            q_cells = defaultdict(list)
            for p in perms:
                P = []
                Q = []
                for i, x in enumerate(p):
                    r = 0
                    while r < len(P):
                        idx = -1
                        for c in range(len(P[r])):
                            if P[r][c] > x:
                                idx = c
                                break
                        if idx == -1:
                            P[r].append(x)
                            Q[r].append(i + 1)
                            break
                        else:
                            x, P[r][idx] = P[r][idx], x
                            r += 1
                    if r == len(P):
                        P.append([x])
                        Q.append([i + 1])
                q_tup = tuple(tuple(row) for row in Q)
                q_cells[q_tup].append(p)
            
            # just pick the first Q cell for shape lam
            cell_words = []
            for q_tup, words in q_cells.items():
                if tuple(len(row) for row in q_tup) == lam:
                    cell_words = words
                    break
            
            w_tuples = [list(w) for w in cell_words]
            try:
                b_sum = pyhecke_native.kl_betti_sum_rust(n, w_tuples)
            except Exception as e:
                print(f"Error computing rust sum for S_{n}: {e}")
                b_sum = 0
            shape_betti[lam] = b_sum
            
        print(f"\\n--- S_{n} ---")
        for lam in sorted(shape_betti.keys(), reverse=True):
            f_lam = get_flambda(lam)
            b = shape_betti[lam]
            print(f"  lam={str(lam):12s} f^lam={f_lam:<3}  Betti={b:<4}  (Betti/f^lam = {b/f_lam:.2f})")

if __name__ == '__main__':
    main()
