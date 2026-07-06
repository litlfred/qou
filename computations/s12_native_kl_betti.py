import sys
import time
import pyhecke_native
from rsk import inverse_rsk, canonical_Q, generate_syt

def main():
    n = 12
    lam = (10, 2)
    print(f"Finding canonical left cell for lambda={lam} in S_{n} via inverse RSK...")
    
    Q_can = canonical_Q(lam)
    cell_words = []
    max_len = 0
    count = 0
    for P in generate_syt(lam):
        w = inverse_rsk(P, Q_can)
        cell_words.append(list(w))
        l = sum(1 for i in range(n) for j in range(i+1, n) if w[i] > w[j])
        max_len = max(max_len, l)
        count += 1
        
    print(f"Number of SYTs (f^lambda) = {count}")
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
