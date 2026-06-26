import sys
from pathlib import Path
import time
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
    return tuple(len(row) for row in P), tuple(tuple(row) for row in Q)

def canonical_Q(lam):
    Q = []
    val = 1
    for r in lam:
        row = []
        for _ in range(r):
            row.append(val)
            val += 1
        Q.append(row)
    return tuple(tuple(row) for row in Q)

def main():
    n = 12
    lam = (10, 2)
    print(f"Finding canonical left cell for lambda={lam} in S_{n}...")
    
    # Actually, we don't want to iterate 479 million permutations to find the ones with Q_can!
    # Let's do S_8 first to see if it finishes.
    n_test = 8
    lam_test = (6, 2)
    Q_can = canonical_Q(lam_test)
    
    cell_words = []
    max_len = 0
    for p in permutations_S_n(n_test):
        _, q = rsk(p)
        if q == Q_can:
            cell_words.append(list(p))
            l = sum(1 for i in range(n_test) for j in range(i+1, n_test) if p[i] > p[j])
            max_len = max(max_len, l)
            
    print(f"S_{n_test} lambda={lam_test}: found {len(cell_words)} words. Max length = {max_len}")
    
    t0 = time.time()
    try:
        res = pyhecke_native.kl_betti_sum_rust(n_test, cell_words)
        dt = time.time() - t0
        print(f"S_{n_test} Betti sum = {res} (took {dt:.4f} sec)")
    except Exception as e:
        print(f"S_{n_test} failed: {e}")

if __name__ == '__main__':
    main()
