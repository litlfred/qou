"""H20: why swapped-pair orbits carry +v^-2. See h20_preregistration.md."""
from fractions import Fraction as Fr
import itertools, sys
v = Fr(2); h = v - 1/v

def run(N, n):
    def R_apply(i, vec):
        out = {}
        for b, c in vec.items():
            x, y = b[i-1], b[i]
            def add(t, w): out[t] = out.get(t, 0) + w
            if x == y: add(b, c*v)
            else:
                sw = b[:i-1] + (y, x) + b[i+1:]
                if x < y: add(sw, c)
                else: add(sw, c); add(b, c*h)
        return {k: w for k, w in out.items() if w}
    def J_apply(vec):
        return {tuple(N-1-a for a in reversed(b)): c for b, c in vec.items()}
    def lin(vec_a, vec_b, ca, cb):
        out = {}
        for k, w in vec_a.items(): out[k] = out.get(k, 0) + ca*w
        for k, w in vec_b.items(): out[k] = out.get(k, 0) + cb*w
        return {k: w for k, w in out.items() if w}
    def P(i, sign, vec):   # sign +: eigenvalue v ; sign -: eigenvalue -1/v
        Tv = R_apply(i, vec)
        if sign > 0: return lin(Tv, vec, 1/(v + 1/v), (1/v)/(v + 1/v))
        return lin(Tv, vec, 1/(-1/v - v), (-v)/(-1/v - v))
    basis = list(itertools.product(range(N), repeat=n))
    def trJ(op):
        return sum((J_apply(op({b: Fr(1)}))).get(b, 0) for b in basis)
    pairs = sorted({(i, n-i) for i in range(1, n) if i + 2 <= n - i})
    allpass = True
    for (i, j) in pairs:
        cp = trJ(lambda x: P(i, 1, P(j, 1, x)))
        cm = trJ(lambda x: P(i, -1, P(j, -1, x)))
        cmix = trJ(lambda x: P(i, 1, P(j, -1, x))) + trJ(lambda x: P(i, -1, P(j, 1, x)))
        p = []
        for k in range(11):
            def A(x, k=k):
                for _ in range(k): x = R_apply(i, R_apply(j, x))
                return x
            p.append(trJ(A))
        match = all(p[k] == cp*v**(2*k) + cm*v**(-2*k) for k in range(11))
        ok = (cmix == 0) and match
        allpass &= ok
        print(f"N = {N}, n = {n}, pair ({i},{j}): c+ = {cp}, c- = {cm}, c_mix = {cmix}; "
              f"p_k = c+ v^2k + c- v^-2k for k=0..10: {match}; pass: {ok}")
        sys.stdout.flush()
    return allpass

res = True
for N in (2, 3):
    for n in (4, 5, 6, 7):
        res &= run(N, n)
print("OVERALL PASS:", res)
