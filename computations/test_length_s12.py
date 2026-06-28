import sys

def length(perm):
    n = len(perm)
    return sum(1 for i in range(n) for j in range(i + 1, n) if perm[i] > perm[j])

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
    return P, Q

def canonical_Q(lam):
    Q = []
    val = 1
    for r in lam:
        row = []
        for _ in range(r):
            row.append(val)
            val += 1
        Q.append(row)
    return Q

def main():
    n = 12
    # We only care about specific Q-tableaux.
    # Actually, we don't need to iterate all 12! to find permutations with a specific Q.
    # The Robinson-Schensted map is a bijection. We can invert RSK!
    # Let's find the max length of a permutation that inserts to canonical Q of (10,2).
    # Since Q is fixed, P ranges over all SYT of shape (10,2).
    # (10,2) has 54 SYTs.
    # We can just generate them and inverse RSK.
    print("Writing inverse RSK is hard.")
    
if __name__ == '__main__':
    main()
