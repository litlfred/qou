from functools import lru_cache
import sys
sys.setrecursionlimit(100000)

def partitions(n, cap=None):
    if cap is None: cap = n
    if n == 0:
        yield (); return
    for first in range(min(n, cap), 0, -1):
        for rest in partitions(n-first, first):
            yield (first,) + rest

def border_strips(lam, r):
    """Yield (resulting partition, height-1) for each border strip of size r."""
    lam = list(lam)
    n = len(lam)
    # beta-numbers method: first-column hook lengths
    beta = [lam[i] + (n - 1 - i) for i in range(n)]
    bset = set(beta)
    out = []
    for b in beta:
        nb = b - r
        if nb >= 0 and nb not in bset:
            newb = sorted([x for x in beta if x != b] + [nb], reverse=True)
            # height = number of beta values strictly between nb and b
            ht = sum(1 for x in beta if nb < x < b)
            newlam = tuple(sorted([newb[i] - (len(newb)-1-i) for i in range(len(newb))], reverse=True))
            newlam = tuple(x for x in newlam if x > 0)
            out.append((newlam, ht))
    return out

@lru_cache(maxsize=None)
def chi(lam, mu):
    """Murnaghan-Nakayama character chi^lam(mu)."""
    if not mu:
        return 1 if not lam else 0
    r, rest = mu[0], mu[1:]
    tot = 0
    for newlam, ht in border_strips(lam, r):
        tot += (-1)**ht * chi(newlam, rest)
    return tot

def hook_dim(lam, nfact):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])] if lam else []
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= row - j + conj[j] - i - 1
    return nfact // prod
