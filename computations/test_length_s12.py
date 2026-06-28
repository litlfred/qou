import sys
from rsk import inverse_rsk, canonical_Q, generate_syt

def length(perm):
    n = len(perm)
    return sum(1 for i in range(n) for j in range(i + 1, n) if perm[i] > perm[j])

def main():
    n = 12
    lam = (10, 2)
    Q_can = canonical_Q(lam)
    max_len = 0
    max_perm = None
    count = 0
    
    for P in generate_syt(lam):
        perm = inverse_rsk(P, Q_can)
        l = length(perm)
        if l > max_len:
            max_len = l
            max_perm = perm
        count += 1
        
    print(f"S_{n} lambda={lam}: found {count} words. Max length = {max_len}")
    
if __name__ == '__main__':
    main()
