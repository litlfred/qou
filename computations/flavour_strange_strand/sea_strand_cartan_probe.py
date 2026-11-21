"""Sea strand + valence Cartan weight: full n - p for V3*L4 with the sea strand traced three ways.
F_N = K_N(valence, isospin Cartan q^{+-1}) * T_N(sea).  Sea traces: bare (u+d+s), quantum
(weights q^2,1,q^-2 = q^{2rho}), isospin-quantum (q,q^-1,1). Exact; q0 for display only.
The no-sea reference is K_N * tr V3 (the existing Cartan term)."""
import itertools, sympy as sp, runpy
g = runpy.run_path('/mnt/project-files/qou-lattice-isospin-review/sea_strand_probe.py', run_name='lib')
q, L4, V3, idx = g['q'], g['L4'], g['V3'], g['idx']
M = V3*L4
def T(w, f):
    return sum(M[idx(t+(f,)), idx(t+(f,))] for t in itertools.product(range(3), repeat=3)
               if tuple(t.count(k) for k in range(3)) == w)
Tp = [sp.simplify(T((2,1,0), f)) for f in range(3)]
Tn = [sp.simplify(T((1,2,0), f)) for f in range(3)]
trV3 = -q**6 + 3*q**4 - 3*q**2 + 5 - 3/q**2 + 3/q**4 - 1/q**6
Kp, Kn = q, 1/q
ref = sp.factor((Kn - Kp)*trV3)
print("no-sea Cartan  n-p =", ref)
for lab, wts in [("bare u+d+s", [1,1,1]), ("quantum q^2rho", [q**2,1,q**-2]), ("isospin-quantum", [q,1/q,1])]:
    Sp = sum(w*t for w, t in zip(wts, Tp)); Sn = sum(w*t for w, t in zip(wts, Tn))
    np_ = sp.factor(sp.simplify(Kn*Sn - Kp*Sp)); sea_only = sp.factor(sp.simplify(Sn - Sp))
    print(f"{lab:16s} sea bare-trace part (n-p) = {sea_only}")
    print(f"{'':16s} full n-p = {np_}")
    q0 = sp.Rational('1.1099785827513808')
    print(f"{'':16s} ratio full/no-sea at q0 = {sp.N((np_/ref).subs(q,q0), 8)}   (display only)")

# Relative splitting (normalisation-free): delta = (F_n - F_p)/(F_n + F_p)
print("\nRelative splitting delta = (F_n - F_p)/(F_n + F_p):")
d0 = sp.simplify((Kn - Kp)/(Kn + Kp))
print("  no sea:", sp.factor(d0), "=", sp.N(d0.subs(q, q0), 8))
for lab, wts in [("bare u+d+s", [1,1,1]), ("quantum q^2rho", [q**2,1,q**-2]), ("isospin-quantum", [q,1/q,1])]:
    Sp = sum(w*t for w, t in zip(wts, Tp)); Sn = sum(w*t for w, t in zip(wts, Tn))
    d = sp.simplify((Kn*Sn - Kp*Sp)/(Kn*Sn + Kp*Sp))
    print(f"  {lab:16s}", sp.N(d.subs(q, q0), 8), " ratio to no-sea:", sp.N((d/d0).subs(q, q0), 8))
