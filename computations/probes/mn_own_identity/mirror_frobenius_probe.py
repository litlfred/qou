"""Pre-registered in PREREGISTRATION-pairing-ratio-and-mirror.md (part B).

A = Q[x]/(x^2), basis (1, x). S = id. Delta(a) = t*(1 (x) a), t = Delta(1) in A(x)A.
Stated Frobenius relation Delta(ab) = Delta(a)(1(x)b) holds by construction.
Impose counit laws, coassociativity, cocommutativity (needed for S = id antipode laws
with symmetric braiding), solve exactly, then test the mirror Delta(ab) = (a(x)1)Delta(b).
"""
import json, itertools, sympy as sp

t = sp.symbols('t0:4')          # t = sum t[2i+j] e_i (x) e_j, e0 = 1, e1 = x
e = sp.symbols('e0:2')          # counit values eps(1), eps(x)
# multiplication table: e0*e0=e0, e0*e1=e1, e1*e0=e1, e1*e1=0
def mul(i, j):
    v = [0, 0]
    if i == 0: v[j] = 1
    elif j == 0: v[1] = 1
    return v
def mulvec(a, b):  # a, b coefficient vectors
    out = [0, 0]
    for i in range(2):
        for j in range(2):
            m = mul(i, j)
            for k in range(2): out[k] += a[i]*b[j]*m[k]
    return out
def tensor_mul(T, U):  # (A(x)A) product, T,U 2x2 coefficient arrays
    out = [[0,0],[0,0]]
    for i,j,k,l in itertools.product(range(2), repeat=4):
        a = mul(i,k); b = mul(j,l)
        for m in range(2):
            for n in range(2):
                out[m][n] += T[i][j]*U[k][l]*a[m]*b[n]
    return out
T = [[t[0], t[1]], [t[2], t[3]]]
def basis(i): return [[1,0],[0,0]] if False else None
def unitT(): return [[1,0],[0,0]]
def a_tensor_1(i):
    M = [[0,0],[0,0]]; M[i][0] = 1; return M
def one_tensor_a(i):
    M = [[0,0],[0,0]]; M[0][i] = 1; return M
def Delta(i):  # Delta(e_i) = t * (1 (x) e_i)
    return tensor_mul(T, one_tensor_a(i))
eqs = []
for i in range(2):
    D = Delta(i)
    # (eps (x) id) Delta = id ; (id (x) eps) Delta = id
    left = [sum(D[a][b]*e[a] for a in range(2)) for b in range(2)]
    right = [sum(D[a][b]*e[b] for b in range(2)) for a in range(2)]
    target = [1 if k == i else 0 for k in range(2)]
    eqs += [sp.expand(left[k]-target[k]) for k in range(2)]
    eqs += [sp.expand(right[k]-target[k]) for k in range(2)]
    # cocommutativity
    eqs += [sp.expand(D[a][b]-D[b][a]) for a in range(2) for b in range(2)]
    # coassociativity: (Delta (x) id)Delta = (id (x) Delta)Delta
    L = {}; R = {}
    for a, b in itertools.product(range(2), repeat=2):
        c = D[a][b]
        Da = Delta(a); Db = Delta(b)
        for m, n in itertools.product(range(2), repeat=2):
            L[(m,n,b)] = L.get((m,n,b),0) + c*Da[m][n]
            R[(a,m,n)] = R.get((a,m,n),0) + c*Db[m][n]
    for key in set(L)|set(R):
        eqs.append(sp.expand(L.get(key,0)-R.get(key,0)))
eqs = [x for x in set(eqs) if x != 0]
sols = sp.solve(eqs, list(t)+list(e), dict=True)
report = {"n_equations": len(eqs), "solutions": []}
for s in sols:
    Ts = [[sp.simplify(T[i][j].subs(s)) for j in range(2)] for i in range(2)]
    mirror_ok = True
    for i in range(2):
        for j in range(2):
            lhs = tensor_mul(Ts, one_tensor_a(mul(i,j).index(1))) if any(mul(i,j)) else [[0,0],[0,0]]
            Dj = tensor_mul(Ts, one_tensor_a(j))
            rhs = tensor_mul(a_tensor_1(i), Dj)
            if any(sp.simplify(lhs[m][n]-rhs[m][n]) != 0 for m in range(2) for n in range(2)):
                mirror_ok = False
    report["solutions"].append({"t": str(Ts), "eps": [str(sp.simplify(x.subs(s))) for x in e],
                                "free_symbols": str(set().union(*[sp.sympify(x).free_symbols for row in Ts for x in row])),
                                "mirror_relation_holds": mirror_ok})
out = json.dumps(report, indent=2); print(out)
open(__file__.replace('.py','.out.json'),'w').write(out+"\n")
