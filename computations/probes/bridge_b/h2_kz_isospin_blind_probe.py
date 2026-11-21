"""Bridge B, H2: the KZ connection and single-strand diagonal data cannot split proton from neutron.

Exact over Q(q) with sympy (no float arithmetic). Checks, on (C^2)^{(x)3}:
  1. each pairwise Casimir term Omega_ij commutes with the total sl2 (E, F, H);
  2. a generic direction a*O01 + b*O02 + c*O12 has identical characteristic polynomials on the
     weight +1 (proton) and -1 (neutron) spaces;
  3. the Euler/Reeb contraction sum Omega_ij has spectrum {3/2, -3/2, -3/2} on both;
  4. under the Jimbo R-matrix: a single-strand weight h does NOT commute with R, but the total
     weight and h(x)h do; a generic diagonal single-strand datum a + b*h summed over strands does.
Audit: docs/audits/2026-11-16-bridge-b-np-mass-scale-exclusions.md.
"""
import sympy as sp
from sympy import kronecker_product as kp

e = sp.Matrix([[0, 1], [0, 0]]); f = sp.Matrix([[0, 0], [1, 0]]); H = sp.diag(1, -1); I = sp.eye(2)


def on(M, i, n=3):
    m = [I] * n; m[i] = M; r = m[0]
    for x in m[1:]:
        r = kp(r, x)
    return r


def Om(i, j):
    return on(e, i) * on(f, j) + on(f, i) * on(e, j) + on(H, i) * on(H, j) / 2


Et = sum((on(e, i) for i in range(3)), sp.zeros(8))
Ft = sum((on(f, i) for i in range(3)), sp.zeros(8))
Ht = sum((on(H, i) for i in range(3)), sp.zeros(8))
ok = True
for (i, j) in [(0, 1), (0, 2), (1, 2)]:
    c = all((Om(i, j) * X - X * Om(i, j)).is_zero_matrix for X in (Et, Ft, Ht))
    print(f"1. Omega_{i}{j} commutes with total sl2: {c}"); ok &= c

a, b, c, lam = sp.symbols('a b c lambda')
W = a * Om(0, 1) + b * Om(0, 2) + c * Om(1, 2)
idx = {w: [k for k in range(8) if Ht[k, k] == w] for w in (1, -1)}
cp = {w: sp.expand(W.extract(idx[w], idx[w]).charpoly(lam).as_expr()) for w in (1, -1)}
same = sp.simplify(cp[1] - cp[-1]) == 0
print("2. charpoly equal on p and n weight spaces:", same, "->", sp.factor(cp[1])); ok &= same

S = Om(0, 1) + Om(0, 2) + Om(1, 2)
sp_p = S.extract(idx[1], idx[1]).eigenvals(); sp_n = S.extract(idx[-1], idx[-1]).eigenvals()
print("3. Reeb contraction spectrum p:", sp_p, " n:", sp_n); ok &= (sp_p == sp_n)

q = sp.symbols('q', positive=True); h = q - 1 / q
R = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]])
x, y = sp.symbols('x y')
D = sp.diag(x + y, x - y)


def comm(X):
    return sp.simplify(R * X - X * R).is_zero_matrix


r = {"h on one strand": comm(kp(H, I)), "total h": comm(kp(H, I) + kp(I, H)),
     "h(x)h": comm(kp(H, H)), "E on one strand": comm(kp(e, I)),
     "summed diagonal datum a+b*h": comm(kp(D, I) + kp(I, D))}
for k_, v in r.items():
    print(f"4. commutes with R: {k_}: {v}")
ok &= (not r["h on one strand"]) and r["total h"] and r["h(x)h"] and r["summed diagonal datum a+b*h"]
print("transport of h through R:", sp.simplify(R * kp(H, I) * R.inv() - kp(I, H)))
print("ALL CHECKS PASS" if ok else "CHECK FAILED")
