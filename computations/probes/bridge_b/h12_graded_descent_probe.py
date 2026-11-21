"""H12: graded (Koszul-signed) doubled letter; mirror-twisted trace vs Lusztig 16.7(b). Exact sympy."""
import sympy as sp
from itertools import product
q = sp.symbols('q', positive=True)

def run(odd_index):
    a = [q, -1/q]
    par = [0, 0]; par[odd_index] = 1
    idx = list(product(range(2), repeat=2))            # basis e_i (x) e_j of V(x)V
    b = sp.diag(*[a[i]*a[j]*(-1)**(par[i]*par[j]) for i, j in idx])
    P = sp.zeros(4, 4)
    for r, (i, j) in enumerate(idx):
        P[idx.index((j, i)), r] = 1
    ok1 = all(sp.simplify((P*b**k).trace() - (q**(2*k) + (-q**-2)**k)) == 0 for k in range(1, 7))
    mixed = [r for r, (i, j) in enumerate(idx) if i != j]
    ok2 = all(P[r, r] == 0 for r in mixed)
    return ok1, ok2, b, P

ok1, ok2, b, P = run(1)
print("grading: -q^-1 line odd")
print("  1. tr(P b^k) = q^{2k} + (-q^-2)^k, k=1..6:", ok1)
print("  2. mixed lines off-diagonal under P (traceless):", ok2)
# 3. two commuting doubled letters on (V(x)V)(x)(V(x)V), mirror swap acting on each pair
B1 = sp.kronecker_product(b, sp.eye(4)); B2 = sp.kronecker_product(sp.eye(4), b)
PP = sp.kronecker_product(P, P)
lus = lambda k: q**(2*k) + (-q**-2)**k
ok3 = all(sp.simplify((PP*B1**k1*B2**k2).trace() - lus(k1)*lus(k2)) == 0 for k1 in range(4) for k2 in range(4))
print("  3. two-letter factorisation, k1,k2 = 0..3:", ok3)
ok1b, _, _, _ = run(0)
print("grading: q line odd")
print("  4. criterion 1 must fail; it holds:", ok1b)
print("PASS" if (ok1 and ok2 and ok3 and not ok1b) else "FAIL")
