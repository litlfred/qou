"""Is E0's weight hbar_q/q^2 a convention-D Markov trace?  Exact over Q(q).

Prereg: computations/probes/e0_weight/PREREGISTRATION.md (six fixed candidates).
"""
import sympy as sp

q = sp.symbols("q", positive=True)
h = q - 1/q
R = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]])  # Jimbo R-check
Ri = sp.simplify(R.inv())
K = sp.diag(q, 1/q)

def gen(i, n, inv=False):
    M = Ri if inv else R
    return sp.kronecker_product(sp.kronecker_product(sp.eye(2**i), M), sp.eye(2**(n - i - 2)))

def word(w, n):
    M = sp.eye(2**n)
    for g in w:
        M = M * gen(abs(g) - 1, n, g < 0)
    return M

def tr(w, n):
    Kn = K
    for _ in range(n - 1):
        Kn = sp.kronecker_product(Kn, K)
    return sp.factor(sp.simplify((Kn * word(w, n)).trace() / (q + 1/q)**n))

zD = q**3 / (q**2 + 1)
assert sp.simplify(tr([1], 2) - zD) == 0, "trace is not convention D"
target = sp.factor((q - 1) / q**3)
target5 = sp.factor(1 / (q * (q - 1)))
hb2 = ((q - 1) / q)**2

t_s = tr([1], 2)
y11 = sp.factor((q - t_s) / (q + 1/q))
y2 = sp.factor(1 - y11)
cands = {
    "C1 tr(s^-1), n=2": tr([-1], 2),
    "C2 y_(2), n=2": y2,
    "C2 y_(1,1), n=2": y11,
    "C3 tr(s0 s1 s0), n=3": tr([1, 2, 1], 3),
    "C3 tr((s0 s1 s0)^-1), n=3": tr([-1, -2, -1], 3),
    "C4 tr(s0 s1^-1), n=3": tr([1, -2], 3),
    "C4 tr((s0 s1^-1)^3), n=3": tr([1, -2] * 3, 3),
}

def verdict(x, t):
    r = sp.factor(sp.simplify(x / t))
    if sp.simplify(r - 1) == 0:
        return "EXACT"
    for k in range(-3, 4):
        if sp.simplify(r - q**k) == 0:
            return f"monomial near-match q^{k}"
    return f"no (ratio {r})"

print("target w = hbar_q/q^2 =", target, "; C5 target 1/(q(q-1)) =", target5)
for name, x in cands.items():
    print(f"{name}: {x}")
    print(f"    vs w: {verdict(x, target)}")
    print(f"    C5 (x/hbar^2) vs 1/(q(q-1)): {verdict(sp.factor(x / hb2), target5)}")
