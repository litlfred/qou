import sys
import time
import pyhecke_native

def generate_syts_10_2(n):
    syts = []
    for a in range(2, n):
        for b in range(a + 1, n + 1):
            if a == 2 and b == 3:
                continue
            # Build the SYT
            row1 = [a, b]
            row0 = [x for x in range(1, n + 1) if x not in row1]
            syts.append([row0, row1])
    return syts

def inverse_rsk(P, Q):
    n = sum(len(r) for r in P)
    P = [list(r) for r in P]
    Q = [list(r) for r in Q]
    
    perm = [0] * n
    for k in range(n, 0, -1):
        # Find k in Q
        r_k, c_k = -1, -1
        for i, row in enumerate(Q):
            for j, val in enumerate(row):
                if val == k:
                    r_k, c_k = i, j
                    break
            if r_k != -1: break
        
        Q[r_k].pop()
        
        # Unbump from P. 
        # Crucial fix: we pop the element at (r_k, c_k) which is the END of row r_k.
        x = P[r_k].pop()
        
        r = r_k
        while r > 0:
            r -= 1
            # Find largest element y in row r strictly less than x
            # Since row is sorted, scan from right to left
            for c in range(len(P[r]) - 1, -1, -1):
                if P[r][c] < x:
                    y = P[r][c]
                    P[r][c] = x
                    x = y
                    break
        perm[k - 1] = x
    return tuple(perm)

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
    print(f"Finding canonical left cell for lambda={lam} in S_{n} via inverse RSK...")
    
    syts = generate_syts_10_2(n)
    print(f"Number of SYTs (f^lambda) = {len(syts)}")
    
    Q_can = canonical_Q(lam)
    cell_words = []
    max_len = 0
    for P in syts:
        w = inverse_rsk(P, Q_can)
        cell_words.append(list(w))
        l = sum(1 for i in range(n) for j in range(i+1, n) if w[i] > w[j])
        max_len = max(max_len, l)
        
    print(f"Generated {len(cell_words)} permutations. Max length = {max_len}")
    
    t0 = time.time()
    try:
        res = pyhecke_native.kl_betti_sum_rust(n, cell_words)
        dt = time.time() - t0
        print(f"S_{n} lambda={lam} Betti sum = {res} (took {dt:.4f} sec)")
    except Exception as e:
        print(f"S_{n} failed: {e}")
        
if __name__ == '__main__':
    main()
