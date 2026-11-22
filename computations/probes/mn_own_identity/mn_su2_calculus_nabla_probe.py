"""Pre-registered in PREREGISTRATION-su2-calculus-nabla.md. Exact sympy, no floats.

U_q(sl2) on (C^2)^{x3} via the coproduct; Reeb = Cartan xi_tot, horizontal = E, F.
Normalised states in W_p = (2,1), W_n = (1,2): expectations and K-weighted Reeb matter term.
"""
import json, itertools, sympy as sp

q = sp.symbols('q', positive=True)
I2 = sp.eye(2)
E1 = sp.Matrix([[0, 1], [0, 0]]); F1 = sp.Matrix([[0, 0], [1, 0]])
H1 = sp.diag(1, -1); K1 = sp.diag(q, 1/q); xi1 = H1/2
kp = sp.kronecker_product
def tri(a, b, c): return kp(kp(a, b), c)
# iterated coproduct: E -> E K K + 1 E K + 1 1 E ; F -> F 1 1 + K^-1 F 1 + K^-1 K^-1 F
Ki = K1.inv()
E = tri(E1, K1, K1) + tri(I2, E1, K1) + tri(I2, I2, E1)
F = tri(F1, I2, I2) + tri(Ki, F1, I2) + tri(Ki, Ki, F1)
K = tri(K1, K1, K1)
xi = tri(xi1, I2, I2) + tri(I2, xi1, I2) + tri(I2, I2, xi1)
checks = {
  "KE=q^2EK": bool(sp.simplify(K*E - q**2*E*K) == sp.zeros(8)),
  "KF=q^-2FK": bool(sp.simplify(K*F - F*K/q**2) == sp.zeros(8)),
  "[E,F]=(K-K^-1)/(q-q^-1)": bool(sp.simplify(E*F - F*E - (K - K.inv())/(q - 1/q)) == sp.zeros(8)),
}
basis = list(itertools.product([0, 1], repeat=3))  # 0 = u (e1), 1 = d (e2)
def wspace(nup): return [i for i, b in enumerate(basis) if b.count(0) == nup]
res = {"checks": checks}
a = sp.symbols('a0:3')
for name, nup in [("proton_W(2,1)", 2), ("neutron_W(1,2)", 1)]:
    idx = wspace(nup)
    psi = sp.zeros(8, 1)
    for k, i in enumerate(idx): psi[i] = a[k]
    nrm = (psi.T*psi)[0]
    phi = psi.T/nrm
    ev = lambda X: sp.simplify((phi*X*psi)[0])
    w = sp.simplify((K*psi)[idx[0]]/psi[idx[0]])
    res[name] = {
      "T1_<E>": str(ev(E)), "T1_<F>": str(ev(F)),
      "T2_<xi>": str(ev(xi)),
      "K_weight_w": str(w),
      "T3_tr(K psi phi xi)": str(sp.simplify((K*psi*phi*xi).trace())),
    }
p, n = res["proton_W(2,1)"], res["neutron_W(1,2)"]
diff = sp.simplify(sp.sympify(n["T3_tr(K psi phi xi)"]) - sp.sympify(p["T3_tr(K psi phi xi)"]))
res["T3_n_minus_p"] = str(sp.factor(diff))
res["verdict"] = {
  "T1": "horizontal expectation 0 for every normalised weight state: mu = 0 under the flat connection",
  "12": "not attainable in this class (mu = 0)",
}
out = json.dumps(res, indent=2); print(out)
open(__file__.replace('.py', '.out.json'), 'w').write(out + "\n")
