"""H14: KL bases of S_6 (equal parameters) and of its fixed group B_3 under iota (weights L = ambient length).
Laurent polynomials as dict{exponent: int}. Exact integer arithmetic."""
from itertools import permutations
from collections import deque

def padd(a, b, k=1):
    r = dict(a)
    for e, c in b.items():
        r[e] = r.get(e, 0) + k*c
        if r[e] == 0: del r[e]
    return r
def pmul(a, b):
    r = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            r[e1+e2] = r.get(e1+e2, 0) + c1*c2
    return {e: c for e, c in r.items() if c}
def pbar(a): return {-e: c for e, c in a.items()}

def compose(p, r): return tuple(p[r[i]] for i in range(len(r)))  # (p o r)

def coxeter(gens, n):
    """BFS: elements, length, and left action table for given generator permutations."""
    e = tuple(range(n)); length = {e: 0}; Q = deque([e])
    while Q:
        w = Q.popleft()
        for g in gens:
            x = compose(g, w)
            if x not in length:
                length[x] = length[w] + 1; Q.append(x)
    return length

def kl_basis(gens, L, n):
    length = coxeter(gens, n)
    elems = sorted(length, key=lambda w: length[w])
    one = tuple(range(n))
    def left_T(t_idx, X):  # T_t * X, X dict elem -> poly
        g = gens[t_idx]; vt = {L[t_idx]: 1, -L[t_idx]: -1}
        R = {}
        for y, a in X.items():
            ty = compose(g, y)
            R[ty] = padd(R.get(ty, {}), a)
            if length[ty] < length[y]:
                R[y] = padd(R.get(y, {}), pmul(vt, a))
        return {k: v for k, v in R.items() if v}
    def left_c(t_idx, X):
        R = left_T(t_idx, X)
        for y, a in X.items():
            R[y] = padd(R.get(y, {}), pmul({-L[t_idx]: 1}, a))
        return {k: v for k, v in R.items() if v}
    C = {one: {one: {0: 1}}}
    for w in elems[1:]:
        for ti, g in enumerate(gens):
            tw = compose(g, w)
            if length[tw] < length[w]: break
        X = left_c(ti, C[tw])
        for y in sorted([y for y in X if y != w], key=lambda y: -length[y]):
            a = X.get(y, {})
            nonneg = {e: c for e, c in a.items() if e >= 0}
            if nonneg:
                mu = {}
                for e, c in nonneg.items():
                    mu = padd(mu, {e: c})
                    if e > 0: mu = padd(mu, {-e: c})
                for z, b in C[y].items():
                    X[z] = padd(X.get(z, {}), pmul(mu, b), -1)
                X = {k: v for k, v in X.items() if v}
        assert X[w] == {0: 1}
        assert all(max(p) < 0 for y, p in X.items() if y != w), "degree condition"
        C[w] = X
    return C, length

def s(j, n=6):
    p = list(range(n)); p[j-1], p[j] = p[j], p[j-1]; return tuple(p)

n = 6
amb_gens = [s(j) for j in range(1, 6)]
C_amb, len_amb = kl_basis(amb_gens, [1]*5, n)
tau, b1, b2 = s(3), compose(s(2), s(4)), compose(s(1), s(5))
for name, L in (("Lusztig L=(1,2,2)", [1, 2, 2]), ("control equal L=(1,1,1)", [1, 1, 1])):
    C_f, len_f = kl_basis([tau, b1, b2], L, n)
    assert len(C_f) == 48
    ok_mod2 = ok_abs = True; diffs = 0; pairs = 0
    for x, row in C_f.items():
        for y in set(row) | set(C_amb[x]):
            if y not in C_f: continue   # only y in W
            p, pt = row.get(y, {}), C_amb[x].get(y, {})
            pairs += 1
            for e in set(p) | set(pt):
                a, at = p.get(e, 0), pt.get(e, 0)
                if (a - at) % 2: ok_mod2 = False
                if abs(a) > abs(at): ok_abs = False
                if a != at: diffs += 1
    print(f"{name}: pairs y<=x in W compared = {pairs}; mod-2 agreement: {ok_mod2}; |folded| <= ambient: {ok_abs}; coefficient positions where folded != ambient: {diffs}")

# sanity and sign profile (pre-registered item 2)
neg_amb = sum(1 for x in C_amb for y, p in C_amb[x].items() for c in p.values() if c < 0)
nontriv_amb = sum(1 for x in C_amb for y, p in C_amb[x].items() if len(p) > 1 or (y != x and any(c > 1 for c in p.values())))
print(f"sanity: ambient S_6 KL coefficients negative: {neg_amb} (KL positivity expects 0); ambient c_x count = {len(C_amb)}")
C_f, _ = kl_basis([tau, b1, b2], [1, 2, 2], n)
neg = smaller = 0
for x, row in C_f.items():
    for y in C_f:
        p, pt = row.get(y, {}), C_amb[x].get(y, {})
        for e in set(p) | set(pt):
            a, at = p.get(e, 0), pt.get(e, 0)
            if a != at:
                if a < 0: neg += 1
                else: smaller += 1
print(f"Lusztig L=(1,2,2): of the differing positions, folded coefficient negative: {neg}; nonnegative but smaller: {smaller}")
