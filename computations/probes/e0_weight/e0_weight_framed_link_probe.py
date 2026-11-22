"""Prereg Addendum 2 (commit f27ce7f9483): framed link invariants against E0's weight.

m(beta) = (1+q^2)^n q^(-n-2 wr) tau_D(beta), with tau_D the Jimbo state-sum trace
(the same trace as e0_weight_markov_probe.py, which checks tau(sigma) = z_D). Exact Q(q).
"""
import sympy as sp

q = sp.symbols("q", positive=True)
h = q - 1 / q
R = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]])
Ri = sp.simplify(R.inv())
K = sp.diag(q, 1 / q)
w = (q - 1) / q**3


def gen(i, n, inv):
    M = Ri if inv else R
    return sp.kronecker_product(sp.kronecker_product(sp.eye(2**i), M), sp.eye(2**(n - i - 2)))


def tau(word, n):
    M = sp.eye(2**n)
    for g in word:
        M = M * gen(abs(g) - 1, n, g < 0)
    Kn = K
    for _ in range(n - 1):
        Kn = sp.kronecker_product(Kn, K)
    return sp.simplify((Kn * M).trace() / (q + 1 / q) ** n)


def mass(word, n):
    wr = sum(1 if g > 0 else -1 for g in word)
    return sp.factor(sp.simplify((1 + q**2) ** n * q ** (-n - 2 * wr) * tau(word, n)))


assert sp.simplify(tau([1], 2) - q**3 / (q**2 + 1)) == 0, "not convention D"


def ord1(expr):
    expr = sp.factor(sp.together(expr))
    if expr == 0:
        return sp.oo
    num, den = sp.fraction(expr)
    def mult(p):
        p, k = sp.Poly(sp.expand(p), q), 0
        while p.eval(1) == 0:
            p, k = sp.Poly(sp.quo(p.as_expr(), q - 1), q), k + 1
        return k
    return mult(num) - mult(den)


O = mass([], 1)
O2 = mass([], 2)
links = {
    "R2 K=3_1 (s1^3, n=2)": ([1, 1, 1], 2, O),
    "R2 K=4_1 ((s1 s2^-1)^2, n=3)": ([1, -2, 1, -2], 3, O),
    "R3 Hopf+ (s1^2, n=2)": ([1, 1], 2, O2),
    "R3 Hopf- (s1^-2, n=2)": ([-1, -1], 2, O2),
    "R3 electron (s1 s2 s1, n=3)": ([1, 2, 1], 3, O2),
}
lines = [f"m(O) = {O},  m(O u O) = {O2},  target w = {sp.factor(w)} (ord1 1, coeff 1)", ""]
anyeq = False
for name, (word, n, ref) in links.items():
    m = mass(word, n)
    lines.append(f"{name}: m = {m}")
    for lab, X in (("ratio-1", m / ref - 1), ("difference", m - ref)):
        X = sp.factor(sp.simplify(X))
        o = ord1(X)
        c = sp.limit(X / (q - 1), q, 1) if o == 1 else None
        eq = sp.simplify(X - w) == 0
        anyeq |= eq
        v = ("EQUAL" if eq else "excluded: ord1 = %s" % o if o != 1
             else "first-order match only" if c == 1 else f"excluded: leading coeff {c}")
        lines.append(f"    {lab:10s} = {X}   ord1 = {o}  -> {v}")
lines += ["", f"any route equals w exactly: {anyeq}"]
out = "\n".join(lines)
print(out)
open(__file__.replace(".py", "_result.txt"), "w").write(out + "\n")
