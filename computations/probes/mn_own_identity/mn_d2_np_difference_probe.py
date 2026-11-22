"""Pre-registered in PREREGISTRATION-d2-np-difference.md (6f6fa5fb819). Exact sympy, no floats.

Delta(q) = tr_{W_n}(D^2) - tr_{W_p}(D^2), D = q^-1 (hol - 1) + (1 - q^-1) T3, h = q - q^-1.
"""
import json, itertools, sympy as sp

q = sp.symbols('q', positive=True); t = sp.symbols('h')
Rc = sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,q-1/q,0],[0,0,0,q]])
I2 = sp.eye(2)
s0 = sp.kronecker_product(Rc, I2); s1 = sp.kronecker_product(I2, Rc)
hol = sp.simplify((s0*s1.inv())**3)
basis = list(itertools.product([0,1], repeat=3))
T3 = sp.diag(*[sp.Rational(b.count(0) - b.count(1), 2) for b in basis])
A = (hol - sp.eye(8))/q          # holonomy piece
B = (1 - 1/q)*T3                 # Reeb piece
def blk(M, nup):
    idx = [i for i,b in enumerate(basis) if b.count(0) == nup]
    return M.extract(idx, idx)
def tr2(X, Y, nup): return sp.simplify((blk(X, nup)*blk(Y, nup)).trace())
parts = {}
for nm, (X, Y, f) in {"holonomy^2": (A, A, 1), "reeb^2": (B, B, 1), "cross": (A, B, 2)}.items():
    parts[nm] = sp.factor(f*(tr2(X, Y, 1) - tr2(X, Y, 2)))
Delta = sp.factor(sum(parts.values()))
D = blk(A + B, 1); P = blk(A + B, 2)
direct = sp.factor(sp.simplify((D*D).trace() - (P*P).trace()))
# express in h: q = (h + sqrt(h^2+4))/2
qh = (t + sp.sqrt(t**2 + 4))/2
def lead(expr):
    s = sp.series(sp.simplify(expr.subs(q, qh)), t, 0, 12).removeO()
    s = sp.expand(s)
    for k in range(12):
        c = sp.nsimplify(s.coeff(t, k))
        if c != 0: return k, c
    return None, 0
res = {"preregistration": "6f6fa5fb819",
       "checks": {"parts sum to direct": sp.simplify(Delta - direct) == 0,
                  "hecke": sp.simplify((Rc-q*sp.eye(4))*(Rc+sp.eye(4)/q)) == sp.zeros(4)},
       "Delta_factored": str(Delta), "parts": {}}
for nm, e in parts.items():
    k, c = lead(e) if e != 0 else (None, 0)
    res["parts"][nm] = {"factored": str(e), "leading_order_h": k, "coefficient": str(c)}
k, c = lead(Delta)
res["leading_order_h"] = k; res["coefficient"] = str(c)
res["twelve_coincidence"] = (k == 12) or (c == 12) or (c == -12)
s = json.dumps(res, indent=2); print(s)
open(__file__.replace('.py', '.out.json'), 'w').write(s + "\n")
