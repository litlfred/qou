"""Prereg Addendum 3 (commit 84c36bfa812): is hbar_q = 1 - 1/q a one-sided (positive-word) object?

Same convention-D state-sum trace and framed mass as e0_weight_framed_link_probe.py. Exact Q(q).
Every enumerated object is reported; nothing is selected.
"""
import itertools
import sympy as sp

q = sp.symbols("q", positive=True)
h = q - 1 / q
R = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]])
K = sp.diag(q, 1 / q)
hbar = 1 - 1 / q
w = hbar / q**2

# T1: R^-1 = R - h*1, and a + b R scalar only if b = 0 (R has two distinct eigenvalues).
T1a = sp.simplify(R.inv() - (R - h * sp.eye(4))) == sp.zeros(4)
ev = sorted(set(sp.simplify(e) for e in R.eigenvals()), key=str)
T1b = len(ev) == 2

def gen(i, n):
    return sp.kronecker_product(sp.kronecker_product(sp.eye(2**i), R), sp.eye(2**(n - i - 2)))

cache = {}
def tau(word, n):
    key = (tuple(word), n)
    if key not in cache:
        M = sp.eye(2**n)
        for g in word:
            M = M * gen(g - 1, n)
        Kn = K
        for _ in range(n - 1):
            Kn = sp.kronecker_product(Kn, K)
        cache[key] = sp.factor(sp.simplify((Kn * M).trace() / (q + 1 / q) ** n))
    return cache[key]

def mass(word, n):
    return sp.factor((1 + q**2) ** n * q ** (-n - 2 * len(word)) * tau(word, n))

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

def classify(X, added):
    X = sp.factor(sp.simplify(X))
    o = ord1(X)
    if sp.simplify(X - w) == 0 or sp.simplify(X - hbar) == 0:
        return X, o, "DERIVED"
    r = sp.simplify(X / hbar)
    if r.is_Pow and r.base == q or r == 1 / q or r == q:
        k = sp.degree(sp.numer(r), q) - sp.degree(sp.denom(r), q)
        return X, o, "monomial match k=%d (%s)" % (k, "counts" if k == -2 * added else "does not count")
    if o == 1:
        c = sp.limit(X / (q - 1), q, 1)
        return X, o, "first-order match only" if c == 1 else "excluded: coeff %s" % c
    return X, o, "excluded: ord1 %s" % o

def words(n, L):
    for l in range(L + 1):
        yield from itertools.product(range(1, n), repeat=l)

lines = [f"T1: R^-1 = R - h*1: {T1a};  R has two distinct eigenvalues {ev}: {T1b}", ""]
tally = {}
def run(label, n, beta, ext):
    b = list(beta)
    for name, f in (("tau", tau), ("mass", mass)):
        A, B = f(b, n), f(b + list(ext), n)
        for nm, X in (("ratio-1", B / A - 1), ("diff", B - A)):
            X, o, v = classify(X, len(ext))
            key = v.split(":")[0].split(" k=")[0]
            tally[(label, key)] = tally.get((label, key), 0) + 1
            lines.append(f"{label} n={n} beta={b} +{list(ext)} {name:4s} {nm:7s}: ord1={o}  {v}   [{X}]")

for n in (2, 3):
    for beta in words(n, 3):
        for i in range(1, n):
            run("T2", n, beta, (i,))
for n in (2, 3):
    for beta in words(n, 2):
        for ij in itertools.product(range(1, n), repeat=2):
            run("T3", n, beta, ij)
lines.append("")
for k in sorted(tally):
    lines.append(f"tally {k[0]} {k[1]}: {tally[k]}")
lines.append(f"any DERIVED: {any(k[1] == 'DERIVED' for k in tally)}")
out = "\n".join(lines)
print(out)
open(__file__.replace(".py", "_result.txt"), "w").write(out + "\n")
