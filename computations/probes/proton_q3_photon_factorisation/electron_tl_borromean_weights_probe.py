"""Do the ruled Borromean photon weights fit the TL two-photon electron?

Photon (owner ruling 2026-11-20): gamma(a,b,c) = 1 + a s0 + b s1 + c s0 s1^{-1} in H_3(q),
s^2 = h s + 1, h = q - 1/q.  Electron E = s0 s1 s0.  TL quotient = trivial block
(s -> q) + 2-dim block (S0, S1 below); the sign block is dropped.
Ruled Borromean weights: gamma(0,0,q h) and gamma(0,0,-h/q); product = V^3, V = s0 s1^{-1}.

Exact sympy at symbolic q, no floats, no fitting.
 (i)   gamma1 = gamma(0,0,qh) or gamma(0,0,-h/q): is the TL condition met?
 (ii)  gamma(0,0,c) gamma(0,0,c') = lam E on the TL quotient with lam != 0?
 (iii) gamma1 = gamma(0,0,c): for which c does a gamma2 = gamma(a2,b2,c2) exist?
Method for (iii): on the 2-dim block, M1 = I + cV, and {I,S0,S1,V} spans Mat_2, so the
four block equations determine (a2,b2,c2,lam) uniquely as rational functions of (q,c).
Substituting into the trivial-block equation leaves one polynomial condition F2(c) = 0.
"""
import json, sys
import sympy as sp

q = sp.symbols('q')
c, cp, a2, b2, c2, lam, x = sp.symbols('c cp a2 b2 c2 lam x')
h = q - 1/q
S0 = sp.Matrix([[q, 0], [1, -1/q]]); S1 = sp.Matrix([[-1/q, 1], [0, q]])
S1i = sp.Matrix([[-q, 1], [0, 1/q]]); I2 = sp.eye(2)
V = sp.simplify(S0*S1i)
M = lambda u, v, w: I2 + u*S0 + v*S1 + w*V
triv = lambda u, v, w: 1 + q*(u + v) + w          # s0 s1^{-1} -> 1 on trivial block
E = S0*S1*S0
Z = sp.zeros(2)
chk = {}
out = {"probe": "electron_tl_borromean_weights", "photon": "1 + a s0 + b s1 + c s0 s1^-1",
       "electron": "s0 s1 s0", "quotient": "TL (trivial + 2-dim block)",
       "V_block2": str(V.tolist()), "E_block2": str(E.tolist())}

chk["S1_S1inv"] = sp.simplify(S1*S1i - I2) == Z
chk["hecke_rel"] = sp.simplify(S0**2 - h*S0 - I2) == Z and sp.simplify(S1**2 - h*S1 - I2) == Z
chk["ruled_product_is_V3"] = (sp.simplify(M(0, 0, q*h)*M(0, 0, -h/q) - V**3) == Z
                             and sp.simplify(triv(0, 0, q*h)*triv(0, 0, -h/q) - 1) == 0)
basis = sp.Matrix([list(B) for B in (I2, S0, S1, V)])
chk["span_I_S0_S1_V_is_Mat2"] = sp.simplify(basis.det()) != 0

# ---------- (iii) general chiral gamma1 ----------
P = M(0, 0, c)*M(a2, b2, c2)
blk = [sp.numer(sp.together(sp.expand(P[i, j] - lam*E[i, j]))) for i in range(2) for j in range(2)]
sol = sp.solve(blk, [a2, b2, c2, lam], dict=True)
chk["block2_unique_solution"] = len(sol) == 1
s = {k: sp.factor(v) for k, v in sol[0].items()}
resid = sp.factor(triv(0, 0, c)*triv(s[a2], s[b2], s[c2]) - s[lam]*q**3)
F1 = sp.expand(-q**2*c**2 + (q**4 - q**2 + 1)*c - q**2)         # = -q^2 det(I + cV)
F2 = sp.expand((1 - q**2)*c**2 + (q**2 - 1)**2*c - q**2)        # TL condition
D = sp.expand(c*(q**4 - q**2 + 1) - q**2)                        # common denominator factor
chk["F1_is_minus_q2_detM1"] = sp.expand(F1 + q**2*sp.expand(sp.simplify((I2 + c*V).det()))) == 0
chk["lam_formula"] = sp.simplify(s[lam] - q*F1/((q**2 - 1)*D)) == 0
chk["triv_resid_formula"] = sp.simplify(resid + (q**4 + q**2 + 1)*F2/((q**2 - 1)*D)) == 0
chk["q4_q2_1_factor"] = sp.expand((q**2 - q + 1)*(q**2 + q + 1) - (q**4 + q**2 + 1)) == 0
# on F2 = 0, lam != 0 and denominator != 0 (resultants in c are nonzero in Q(q))
res_F1 = sp.factor(sp.resultant(F2, F1, c)); res_D = sp.factor(sp.resultant(F2, D, c))
chk["lam_nonzero_on_F2"] = res_F1 != 0
chk["denominator_nonzero_on_F2"] = res_D != 0
disc = sp.factor(sp.discriminant(F2, c))
trib = q**3 - q**2 - q - 1
chk["disc_factorisation"] = sp.expand(disc - (q**2 - 1)*trib*(q**3 + q**2 - q + 1)) == 0
chk["tribonacci_bracket"] = trib.subs(q, sp.Rational(18, 10)) < 0 < trib.subs(q, sp.Rational(19, 10))
chk["q3+q2-q+1_positive_for_q_gt_1"] = sp.expand((q**3 + q**2 - q + 1).subs(q, 1 + x)) == sp.expand(x**3 + 4*x**2 + 4*x + 2)

sqf = sp.factor_list(disc)
chk["disc_not_square_in_Qq"] = any(m % 2 == 1 and f.has(q) for f, m in sqf[1])
out["iii"] = {
    "gamma2_given_c": {str(k): str(v) for k, v in s.items()},
    "lambda_given_c": "q*F1/((q^2-1)*(c(q^4-q^2+1)-q^2)),  F1 = -q^2 det(I+cV)",
    "trivial_block_residual": str(resid),
    "TL_condition_F2": "(q^2-1) c^2 - (q^2-1)^2 c + q^2 = 0",
    "roots": "c = [(q^2-1)^2 +- sqrt((q^2-1)((q^2-1)^3 - 4q^2))] / (2(q^2-1))",
    "discriminant": str(disc),
    "resultant_F2_F1": str(res_F1), "resultant_F2_denominator": str(res_D),
    "c_not_in_Q(q)": "discriminant has an odd-multiplicity factor, so the roots are quadratic irrationals over Q(q), not rational functions",
    "reality": "disc = (q^2-1)(q^3-q^2-q-1)(q^3+q^2-q+1); for q>1 the last factor is (q-1)^3+4(q-1)^2+4(q-1)+2 > 0, so the roots are real iff q^3-q^2-q-1 >= 0, i.e. q >= the tribonacci constant (real root of q^3=q^2+q+1, bracketed in (18/10, 19/10)); at q0 ~ 1.11 the two roots are a complex-conjugate pair",
}
# rational sanity: q = 11/10 complex roots; q = 2 complex; q = 3 real
san = {}
for qv in (sp.Rational(11, 10), sp.Integer(2), sp.Integer(3)):
    d = disc.subs(q, qv)
    san[str(qv)] = {"disc": str(d), "real_roots": bool(d >= 0)}
    rts = sp.solve(F2.subs(q, qv), c)
    for r in rts:   # verify a full TL factorisation exactly at this rational q
        sub = {q: qv, c: r}
        g2 = [sp.nsimplify(sp.simplify(s[v].subs(sub))) for v in (a2, b2, c2)]
        L = sp.simplify(s[lam].subs(sub))
        okb = sp.simplify((M(0, 0, c)*M(*g2) - L*E).subs(sub)) == Z
        okt = sp.simplify((triv(0, 0, c)*triv(*g2) - L*q**3).subs(sub)) == 0
        chk[f"sanity_q{qv}_root_{sp.srepr(r)[:20]}"] = okb and okt and L != 0
out["iii"]["rational_q_sanity"] = san
chk["disc_neg_at_11_10"] = disc.subs(q, sp.Rational(11, 10)) < 0

# ---------- (i) ruled weights as gamma1 ----------
for name, w in (("qh", q*h), ("minus_h_over_q", -h/q)):
    f2v = sp.factor(F2.subs(c, w)); f1v = sp.factor(F1.subs(c, w))
    out[f"i_{name}"] = {"c": str(sp.factor(w)), "F2(c)": str(f2v), "F1(c)": str(f1v),
                        "TL_fits": f2v == 0,
                        "block2_only_gamma2": [str(sp.factor(s[v].subs(c, w))) for v in (a2, b2, c2)],
                        "block2_only_lambda": str(sp.factor(s[lam].subs(c, w))),
                        "trivial_residual": str(sp.factor(resid.subs(c, w)))}
    chk[f"i_{name}_F2_nonzero"] = sp.simplify(f2v) != 0
chk["i_F2_at_qh_is_minus_q2"] = sp.simplify(F2.subs(c, q*h) + q**2) == 0

# ---------- (ii) pure chiral pair ----------
t, d = sp.simplify(V.trace()), sp.simplify(V.det())
chk["cayley_hamilton"] = sp.simplify(V**2 - t*V + d*I2) == Z
Pp = sp.expand(M(0, 0, c)*M(0, 0, cp))
alpha, beta = 1 - c*cp*d, c + cp + c*cp*t
chk["ii_in_span_I_V"] = sp.simplify(Pp - alpha*I2 - beta*V) == Z
# entries (0,1),(1,0) of alpha I + beta V - lam E:  beta q + lam,  -beta q + lam
e01, e10 = sp.simplify(Pp[0, 1] - lam*E[0, 1]), sp.simplify(Pp[1, 0] - lam*E[1, 0])
chk["ii_offdiag"] = sp.simplify(e01 - (beta*q + lam)) == 0 and sp.simplify(e10 - (-beta*q + lam)) == 0
out["ii"] = {"trV": str(t), "detV": str(d),
             "product": "(1 - c c') I + (c + c' + c c' (1 - q^2 - q^-2)) V",
             "reason": "product lies in span{I,V}; equal to lam*E forces beta*q + lam = 0 and -beta*q + lam = 0, "
                       "so 2 lam = 0: lam = 0 (any q). Hence no factorisation E = lam gamma(0,0,c) gamma(0,0,c'), "
                       "already on the 2-dim block alone, before the trivial block is used.",
             "fits": False}

out["checks"] = {k: bool(v) for k, v in chk.items()}
ok = all(out["checks"].values())
out["all_checks_pass"] = ok
json.dump(out, open(__file__.replace('_probe.py', '_result.json'), 'w'), indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
sys.exit(0 if ok else 1)
