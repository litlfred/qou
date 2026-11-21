"""Reeb weight on the proton weight space from the Bring-cone Reeb triad (exact, sympy).

Audit: docs/audits/2026-11-21-proton-two-twelve-count-survey.md section 5. Issue #8967.
Lean twin: QOU/MassTheory/ProtonReebBringWeight.lean.

Per strand, H = C.1 (+) C.j (left complex structure). Right multiplication M_u is left-linear.
The matrices are computed from quaternion products (sympy Quaternion), not typed in.
On three strands R_u = sum_s M_u^(s) (Leibniz). W_p = span of the states with one e2.
"""
import itertools
import sympy as sp
from sympy.algebras.quaternion import Quaternion as Q

one, qi, qj, qk = Q(1, 0, 0, 0), Q(0, 1, 0, 0), Q(0, 0, 1, 0), Q(0, 0, 0, 1)
I = sp.I

def left_coords(p):
    # p = z1 + z2 j with z1 = a + b i, z2 = c + d i (left): (a+bi) + (c+di) j = a + b i + c j + d k
    return sp.Matrix([p.a + I * p.b, p.c + I * p.d])

def M(u):
    cols = [left_coords(e * u) for e in (one, qj)]
    return sp.Matrix.hstack(*cols)

for name, u in (("i", qi), ("j", qj), ("k", qk)):
    m = M(u)
    print(f"M_{name} on (1, j) =", m.tolist(), "; M^2 =", (m * m).tolist())

def on3(m):
    E = sp.eye(2)
    k = sp.kronecker_product
    return k(m, E, E) + k(E, m, E) + k(E, E, m)

idx = [n for n, s in enumerate(itertools.product([0, 1], repeat=3)) if sum(s) == 1]
out = [n for n in range(8) if n not in idx]
for name, u in (("i", qi), ("j", qj), ("k", qk)):
    R = on3(M(u))
    leak = R.extract(out, idx)
    R2p = (R * R).extract(idx, idx)
    print(f"u={name}: R preserves W_p: {leak.is_zero_matrix}; compressed R^2 on W_p = {R2p.tolist()}")

Rs = [on3(M(u)) for u in (qi, qj, qk)]
Cas = sum((r * r for r in Rs), sp.zeros(8, 8)).extract(idx, idx)
print("Casimir sum_u R_u^2 on W_p eigenvalues:", Cas.eigenvals())
