"""Reflection equation for the sl3 Jimbo braiding: R K1 R K1 = K1 R K1 R, K1 = K (x) 1.
Exact sympy over Q(q). Step 1: diagonal K. Step 2: general K (Groebner/solve, time-boxed)."""
import sympy as sp, itertools
q = sp.symbols('q', positive=True)
N = 3
R = sp.zeros(9, 9)
for i in range(N):
    for j in range(N):
        s = i*N + j
        if i == j: R[s, s] = q
        elif i < j: R[j*N+i, s] = 1
        else: R[j*N+i, s] = 1; R[s, s] = q - 1/q
k = sp.symbols('k0:9'); K = sp.Matrix(3, 3, k)
K1 = sp.kronecker_product(K, sp.eye(3))
E = (R*K1*R*K1 - K1*R*K1*R).applyfunc(sp.expand)
eqs = [e for e in set(E) if e != 0]
diag = {k[1]: 0, k[2]: 0, k[3]: 0, k[5]: 0, k[6]: 0, k[7]: 0}
deq = list({sp.factor(e.subs(diag)) for e in eqs} - {0})
print("diagonal K: remaining equations:", deq)
print("diagonal solutions:", sp.solve(deq, [k[0], k[4], k[8]], dict=True))
G = sp.groebner(eqs, *k, q, order='lex', domain='QQ') if False else None
sols = sp.solve(eqs, list(k), dict=True)
print("general solutions (%d families):" % len(sols))
for s in sols:
    print("  ", sp.Matrix(3, 3, [sp.factor(x.subs(s)) for x in k]).tolist())
