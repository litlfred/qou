"""Jet-tower expansion of D on B_3. Pre-registered in PREREGISTRATION-jet-tower.md (dce76e1655a).
Exact sympy over Q(q); no experimental input; no q0 evaluation."""
import json, itertools, sympy as sp
q = sp.symbols('q', positive=True); h = sp.symbols('h')
Rc = sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,q-1/q,0],[0,0,0,q]])
I2, I8 = sp.eye(2), sp.eye(8)
s0 = sp.kronecker_product(Rc, I2); s1 = sp.kronecker_product(I2, Rc)
basis = list(itertools.product([0,1], repeat=3))
T3 = sp.diag(*[sp.Rational(b.count(0) - b.count(1), 2) for b in basis])
hol = sp.simplify((s0*s1.inv())**3)
D = sp.simplify((hol - I8)/q + (1 - 1/q)*T3)
Wp = [i for i,b in enumerate(basis) if b.count(0) == 2]
Wn = [i for i,b in enumerate(basis) if b.count(0) == 1]
tr = lambda M, idx: sum(M[i, i] for i in idx)
q5 = sp.expand((q**5 - q**-5)/(q - 1/q))
J25 = sp.expand(-q**-14 + q**-12 - q**-10 + q**-8 + q**-4)  # Jones of T(2,5), V(t) with t = q^-2 convention; tested both ways below
J25m = J25.subs(q, 1/q)
def info(expr):
    e = sp.factor(sp.together(expr))
    if e == 0: return {"zero": True}
    num = sp.numer(e)
    fl = [str(f) for f, m in sp.factor_list(num)[1]]
    ser = sp.series(e.subs(q, 1 + h), h, 0, 12).removeO()
    lead = min((t.as_coeff_exponent(h)[1] for t in sp.Add.make_args(sp.expand(ser))), default=None)
    def divides(p):
        return sp.rem(sp.Poly(sp.numer(sp.together(num)), q), sp.Poly(sp.numer(sp.together(p)), q)).is_zero
    return {"zero": False, "factored": str(e), "at_q1": str(sp.limit(e, q, 1)),
            "leading_h_order": int(lead) if lead is not None else None,
            "numerator_irreducible_factors": fl,
            "divisible_by_[5]_q": divides(q5), "divisible_by_J_T25": divides(J25) or divides(J25m)}
out = {"preregistration": "dce76e1655a", "jet": {}}
Dk = I8
for k in range(0, 9):
    if k > 0: Dk = sp.simplify(Dk*D)
    tn, tp = sp.simplify(tr(Dk, Wn)), sp.simplify(tr(Dk, Wp))
    out["jet"][k] = {"plain": info(tn - tp), "K": info(tn/q - q*tp)}
    print(k, "plain:", out["jet"][k]["plain"].get("leading_h_order"), out["jet"][k]["plain"].get("at_q1"),
          "| K:", out["jet"][k]["K"].get("leading_h_order"), out["jet"][k]["K"].get("at_q1"), flush=True)
json.dump(out, open(__file__.replace('.py', '.out.json'), 'w'), indent=1)
