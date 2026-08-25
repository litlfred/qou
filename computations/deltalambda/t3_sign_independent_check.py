"""T3(k) = sum_{lambda |- k} (f^lambda)^2 * chi^lambda(3-cycle), exact integers."""
from functools import lru_cache
import sys
from math import factorial

def partitions(n, maxp=None):
    if maxp is None: maxp = n
    if n == 0: yield (); return
    for p in range(min(n, maxp), 0, -1):
        for rest in partitions(n - p, p):
            yield (p,) + rest

@lru_cache(maxsize=None)
def fdim(lam):
    """# SYT of shape lam, hook-length formula, exact."""
    lam = tuple(x for x in lam if x > 0)
    n = sum(lam)
    if n == 0: return 1
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    num = factorial(n); den = 1
    for i, row in enumerate(lam):
        for j in range(row):
            den *= (row - j) + (conj[j] - i) - 1
    return num // den

def remove_rim_hooks(lam, size):
    """Yield (mu, height) for each rim hook of given size removable from lam."""
    lam = list(lam); r = len(lam)
    # beta-numbers / first-column hook lengths
    beta = [lam[i] + (r - 1 - i) for i in range(r)]
    bset = set(beta)
    for b in beta:
        nb = b - size
        if nb >= 0 and nb not in bset:
            newbeta = sorted([x for x in beta if x != b] + [nb], reverse=True)
            # height = number of beta values strictly between nb and b
            ht = sum(1 for x in beta if nb < x < b)
            mu = [newbeta[i] - (r - 1 - i) for i in range(r)]
            mu = tuple(x for x in mu if x > 0)
            if sum(mu) == sum(lam) - size:
                yield mu, ht

def chi_3cycle(lam):
    """chi^lambda on class (3,1^{k-3}) by Murnaghan-Nakayama."""
    return sum((-1)**ht * fdim(mu) for mu, ht in remove_rim_hooks(lam, 3))

for k in range(3, int(sys.argv[1]) + 1):
    T3 = sum(fdim(l)**2 * chi_3cycle(l) for l in partitions(k))
    kf = factorial(k)
    print(f"k={k:3d}  T3={T3:>22d}   T3/k! = {T3/kf:>14.6f}   sign={'-' if T3<0 else ('0' if T3==0 else '+')}")
