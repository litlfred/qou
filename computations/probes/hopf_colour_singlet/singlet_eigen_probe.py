"""Exact probe: Jimbo gl3 R-matrix acts on the q-antisymmetric singlet by -1/q.
See PREREGISTRATION.md (written before this ran). Exact over Q(q); no floats."""
import itertools, json, sympy as sp
q = sp.symbols('q', positive=True)
n = 3
def E(i, j):
    M = sp.zeros(n); M[i, j] = 1; return M
kron = sp.kronecker_product
R = sp.zeros(n*n)
for i in range(n):
    R += q*kron(E(i, i), E(i, i))
for i in range(n):
    for j in range(n):
        if i != j:
            R += kron(E(j, i), E(i, j))
for i in range(n):
    for j in range(i+1, n):
        R += (q - 1/q)*kron(E(j, j), E(i, i))
I3, I9 = sp.eye(n), sp.eye(n*n)
checks = {}
checks['1_hecke'] = sp.simplify((R - q*I9)*(R + I9/q)) == sp.zeros(9)
R12, R23 = kron(R, I3), kron(I3, R)
checks['2_braid'] = sp.simplify(R12*R23*R12 - R23*R12*R23) == sp.zeros(27)
A = (R12 + sp.eye(27)/q).col_join(R23 + sp.eye(27)/q)
ns = A.nullspace(simplify=True)
checks['3_dim_singlet_eq_1'] = len(ns) == 1
v = sp.simplify(ns[0]); v = sp.simplify(v / [x for x in v if x != 0][0])
idx = list(itertools.product(range(n), repeat=3))
support = [idx[k] for k in range(27) if v[k] != 0]
checks['5_weight_111'] = all(sorted(t) == [0, 1, 2] for t in support) and len(support) == 6
def sign(p):
    s = 1
    for a in range(3):
        for b in range(a+1, 3):
            if p[a] > p[b]: s = -s
    return s
v1 = [v[idx.index(t)].subs(q, 1) for t in support]
checks['4_classical_eps'] = all(sp.simplify(v1[k]*sign(support[0]) - sign(support[k])*v1[0]) == 0 for k in range(6))
out = {'checks': checks, 'singlet': {str(tuple(a+1 for a in t)): str(v[idx.index(t)]) for t in support},
       'all_pass': all(checks.values())}
print(json.dumps(out, indent=1))
