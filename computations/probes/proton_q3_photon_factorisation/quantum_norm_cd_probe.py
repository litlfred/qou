#!/usr/bin/env python3
"""Two "quantum norm 1" readings for the ruled photon in H_3(q).

Photon (owner ruling, STRICT):
    gamma(a,b,c) = 1 + a*s0 + b*s1 + c*s0*s1^{-1},   s^2 = h s + 1,  h = q - 1/q.
Ruled Borromean photons: g1 = gamma(0,0,q h), g2 = gamma(0,0,-h/q).
Anti-involution dagger: q -> 1/q on coefficients, s -> s^{-1}, words reversed.

Option C (unitarity at |q| = 1).  q = e^{i theta}, so conj(q) = 1/q; free
coefficients a,b,c get independent conjugate symbols ab,bb,cb.  We DERIVE the
Hermitian form H on the 2-dim block from S_i^* H S_i = H (both i), then test
rho(gamma)^* H rho(gamma) = H on every block.

Option D (Markov-trace sphere, convention D).  We DERIVE the Ocneanu weights
y_lambda of tau = sum_lambda y_lambda chi_lambda on H_3 from
    tau(1) = 1,  tau(s0) = z tau(1),  tau(s0 s1) = z tau(s0)
(Markov property tau(x s_{n}) = z tau(x) for x in H_n), check y_(1^3) = 0 at
z = q^3/(q^2+1), then compute tau(gamma gamma^dagger).

Everything is exact sympy in Q(q)[a,b,c,ab,bb,cb]; no floats.  Exit 0 iff all
checks pass.  Writes quantum_norm_cd_result.json next to this file.
"""
import json
import pathlib
import sys

import sympy as sp

q = sp.symbols('q')                 # generic; |q|=1 enters only via conj(q)=1/q
a, b, c, ab, bb, cb = sp.symbols('a b c ab bb cb')
h = q - 1/q
I2 = sp.eye(2)

S0 = sp.Matrix([[q, 0], [1, -1/q]])
S1 = sp.Matrix([[-1/q, 1], [0, q]])
checks = {}
checks['hecke_quadratic'] = all(sp.simplify(S*S - h*S - I2) == sp.zeros(2) for S in (S0, S1))
checks['braid_relation'] = sp.simplify(S0*S1*S0 - S1*S0*S1) == sp.zeros(2)

# ---- blocks: generator images ------------------------------------------------
BLOCKS = {
    'trivial': (sp.Matrix([[q]]), sp.Matrix([[q]])),
    'sign': (sp.Matrix([[-1/q]]), sp.Matrix([[-1/q]])),
    'two_dim': (S0, S1),
}

# element = list of (coeff, word), word = tuple of (gen, +-1)
def photon(x, y, w):
    return [(1, ()), (x, ((0, 1),)), (y, ((1, 1),)), (w, ((0, 1), (1, -1)))]

CONJ = {q: 1/q, a: ab, b: bb, c: cb, ab: a, bb: b, cb: c}

def bar(expr):
    return sp.sympify(expr).xreplace(CONJ)

def dagger(el):
    return [(bar(co), tuple((g, -e) for (g, e) in reversed(wd))) for co, wd in el]

def mul(x, y):
    return [(cx*cy, wx + wy) for cx, wx in x for cy, wy in y]

def rho(el, blk):
    G = BLOCKS[blk]
    n = G[0].shape[0]
    M = sp.zeros(n)
    for co, wd in el:
        W = sp.eye(n)
        for g, e in wd:
            W = W * (G[g] if e == 1 else G[g].inv())
        M += sp.sympify(co) * W
    return sp.simplify(M)

def mbar(M):
    return M.applyfunc(bar)

# ---- C1: derive the Hermitian form -------------------------------------------
x11, x12, x21, x22 = sp.symbols('x11 x12 x21 x22')
X = sp.Matrix([[x11, x12], [x21, x22]])
eqs = []
for S in (S0, S1):
    eqs += list(sp.simplify(mbar(S).T * X * S - X))
sol = sp.solve(eqs, [x11, x12, x21], dict=True)
assert len(sol) == 1
Hform = sp.simplify(X.subs(sol[0]).subs(x22, 1))      # one-dim solution space; normalise x22 = 1
checks['C_form_solution_space_dim_1'] = sp.simplify(Hform[1, 1]) == 1 and len(sol) == 1
checks['C_form_hermitian'] = sp.simplify(mbar(Hform).T - Hform) == sp.zeros(2)
for i, S in enumerate((S0, S1)):
    checks[f'C_S{i}_unitary'] = sp.simplify(mbar(S).T*Hform*S - Hform) == sp.zeros(2)
detH = sp.factor(sp.simplify(Hform.det()))
# on |q|=1, q = e^{i th}:  [2]_q = 2 cos th
th = sp.symbols('theta', real=True)
detH_theta = sp.simplify(sp.expand_complex(detH.subs(q, sp.exp(sp.I*th))).rewrite(sp.cos))
# H-adjoint of rho(s) is rho(s^{-1}) => H-unitarity of rho(g) <=> rho(g g^dag) = 1 when coeffs bar-real
checks['C_adjoint_is_dagger'] = all(
    sp.simplify(Hform.inv()*mbar(S).T*Hform - S.inv()) == sp.zeros(2) for S in (S0, S1))

def unitary_defect(el, blk):
    M = rho(el, blk)
    Hb = Hform if blk == 'two_dim' else sp.eye(1)
    return sp.simplify(mbar(M).T*Hb*M - Hb)

g1 = photon(0, 0, q*h)
g2 = photon(0, 0, -h/q)
P = mul(g1, g2)
named = {'g1=gamma(0,0,qh)': g1, 'g2=gamma(0,0,-h/q)': g2, 'g1*g2': P}

C_results = {}
for nm, el in named.items():
    C_results[nm] = {}
    for blk in BLOCKS:
        D = unitary_defect(el, blk)
        C_results[nm][blk] = {'unitary': D == sp.zeros(*D.shape),
                              'defect_M*HM-H': [[str(sp.factor(v)) for v in row] for row in D.tolist()]}
# cross-check: unitarity defect agrees with rho(g g^dag) - 1 route
for nm, el in named.items():
    for blk in BLOCKS:
        Mgg = rho(mul(el, dagger(el)), blk)
        u1 = C_results[nm][blk]['unitary']
        u2 = sp.simplify(Mgg - sp.eye(Mgg.shape[0])) == sp.zeros(*Mgg.shape)
        checks[f'C_crosscheck_{nm}_{blk}'] = (u1 == u2)

# g1*g2 = (s0 s1^{-1})^3 (sorry-free Lean: borromeanV3A_eq_switched_photon_product); V^dag = V^{-1},
# so P P^dag = 1 is automatic for any braid word -- record it as such.
V3w = [(1, ((0, 1), (1, -1)) * 3)]
checks['C_P_equals_V3_all_blocks'] = all(
    sp.simplify(rho(P, blk) - rho(V3w, blk)) == sp.zeros(*rho(P, blk).shape) for blk in BLOCKS)
checks['C_V3_not_identity_two_dim'] = sp.simplify(rho(V3w, 'two_dim') - I2) != sp.zeros(2)
checks['C_V3_det1_two_dim'] = sp.simplify(rho(V3w, 'two_dim').det() - 1) == 0
# general gamma: per-block unitarity conditions
G = photon(a, b, c)
C_general = {}
for blk in BLOCKS:
    D = unitary_defect(G, blk)
    C_general[blk] = [[str(sp.factor(sp.expand(v))) for v in row] for row in D.tolist()]
# trivial block value and sign block value
triv_val = sp.expand(rho(G, 'trivial')[0, 0])
sign_val = sp.expand(rho(G, 'sign')[0, 0])
checks['C_trivial_value'] = sp.simplify(triv_val - (1 + (a + b)*q + c)) == 0
checks['C_sign_value'] = sp.simplify(sign_val - (1 - (a + b)/q + c)) == 0
# chiral-only family gamma(0,0,c) on the 2-dim block: V = S0 S1^{-1}, eigenvalues
V = sp.simplify(S0*S1.inv())
V_ev = [sp.simplify(e) for e in V.eigenvals()]
trV = sp.simplify(V.trace())
# condition for 1 + cV unitary: |c|^2 + c V + cb V^{-1} = 0 on both eigenvalues lam, 1/lam
lam = sp.symbols('lam')
chiral_eq = [sp.expand(c*cb + c*lam + cb/lam), sp.expand(c*cb + c/lam + cb*lam)]
chiral_sol = sp.solve(chiral_eq, [c, cb], dict=True)
chiral_note = ("1+cV unitary on 2-dim block requires c*cb + c*lam + cb/lam = 0 and "
               "c*cb + c/lam + cb*lam = 0 (lam, 1/lam eigenvalues of V); subtracting gives "
               "(c - cb)(lam - 1/lam) = 0; solutions: " + str(chiral_sol))

cstar = q**2 - 1 + 1/q**2          # = -tr V, from the chiral solution above
checks['C_chiral_cstar_unitary_two_dim'] = unitary_defect(photon(0, 0, cstar), 'two_dim') == sp.zeros(2)
checks['C_chiral_cstar_not_unitary_trivial'] = unitary_defect(photon(0, 0, cstar), 'trivial') != sp.zeros(1)
# ---- D: Ocneanu weights -------------------------------------------------------
z = sp.symbols('z')
y3, y21, y111 = sp.symbols('y3 y21 y111')
chi = {blk: (lambda el, blk=blk: sp.simplify(rho(el, blk).trace())) for blk in BLOCKS}
dimfac = {'trivial': y3, 'two_dim': y21, 'sign': y111}
def tau_sym(el):
    return sum(dimfac[blk]*chi[blk](el) for blk in BLOCKS)
one = [(1, ())]
s0 = [(1, ((0, 1),))]
s1 = [(1, ((1, 1),))]
s0s1 = [(1, ((0, 1), (1, 1)))]
markov = [sp.Eq(tau_sym(one), 1), sp.Eq(tau_sym(s0), z), sp.Eq(tau_sym(s0s1), z**2)]
ysol = sp.solve(markov, [y3, y21, y111], dict=True)[0]
ysol = {k: sp.factor(v) for k, v in ysol.items()}
zD = q**3/(q**2 + 1)
yD = {k: sp.factor(sp.simplify(v.subs(z, zD))) for k, v in ysol.items()}
checks['D_y111_zero_at_zD'] = sp.simplify(yD[y111]) == 0

def tau(el, zz=zD):
    w = {y3: yD[y3], y21: yD[y21], y111: yD[y111]} if zz is zD else \
        {k: v.subs(z, zz) for k, v in ysol.items()}
    return sp.simplify(tau_sym(el).subs(w))

# verify Markov property on full basis at z_D: tau(x s1) = z tau(x), x in {1, s0}; also tau(s1)=z
checks['D_markov_tau1'] = sp.simplify(tau(one) - 1) == 0
checks['D_markov_s0'] = sp.simplify(tau(s0) - zD) == 0
checks['D_markov_s1'] = sp.simplify(tau(s1) - zD) == 0
checks['D_markov_s0s1'] = sp.simplify(tau(s0s1) - zD**2) == 0
checks['D_markov_s1inv_x'] = sp.simplify(tau([(1, ((0, 1), (1, -1)))]) - zD*(zD - h)) == 0

D_results = {}
for nm, el in named.items():
    val = sp.factor(sp.simplify(tau(mul(el, dagger(el)))))
    D_results[nm] = {'tau_g_gdag': str(val), 'equals_1': sp.simplify(val - 1) == 0}
# coefficient table of tau(g g^dag) - 1 in the monomials
expr = sp.expand(sp.simplify(tau(mul(G, dagger(G))) - 1))
poly = sp.Poly(sp.together(expr).as_numer_denom()[0], a, b, c, ab, bb, cb)
den1 = sp.factor(sp.together(expr).as_numer_denom()[1])
coeffs = {str(m): str(sp.factor(sp.cancel(co/den1))) for m, co in
          zip([sp.Mul(*[v**e for v, e in zip((a, b, c, ab, bb, cb), mon)]) for mon in poly.monoms()],
              poly.coeffs())}

# chiral-only general: tau(gamma(0,0,c) gamma(0,0,c)^dag)
Gc = photon(0, 0, c)
tau_chiral = sp.factor(sp.simplify(tau(mul(Gc, dagger(Gc)))))
# substitute c = k*h*q^m style? report tau-1 = 0 condition solved for cb
cond_chiral = sp.solve(sp.Eq(tau_chiral, 1), cb)

# consistency: since g2 = g1^dag-coefficient form, check g2 == dagger(g1) image in 2-dim? record
checks['g1dag_coeff_is_g2_coeff'] = sp.simplify(bar(q*h) - (-h/q)) == 0

ok = all(bool(v) for v in checks.values())
out = {
    'photon': 'gamma(a,b,c) = 1 + a s0 + b s1 + c s0 s1^{-1}',
    'checks': {k: bool(v) for k, v in checks.items()},
    'C': {
        'hermitian_form_H': [[str(sp.factor(v)) for v in row] for row in Hform.tolist()],
        'det_H': str(detH),
        'det_H_at_q=e^{i theta}': str(detH_theta),
        'note_positivity': 'H Hermitian; positive definite iff det_H > 0 (H22 = 1 > 0)',
        'named_photons': C_results,
        'general_unitarity_defect_per_block': C_general,
        'trivial_value': str(triv_val), 'sign_value': str(sign_val),
        'V=S0 S1^-1': [[str(v) for v in row] for row in V.tolist()],
        'tr_V': str(trV), 'V_eigenvalues': [str(e) for e in V_ev],
        'chiral_family_note': chiral_note,
    },
    'D': {
        'ocneanu_weights_generic_z': {str(k): str(v) for k, v in ysol.items()},
        'z_D': str(zD),
        'weights_at_z_D': {str(k): str(v) for k, v in yD.items()},
        'named_photons': D_results,
        'tau(g g^dag)-1 coefficients (bar symbols ab,bb,cb = coeff(q->1/q))': coeffs,
        'tau_chiral(c)': str(tau_chiral),
        'tau_chiral=1 solved for cb': [str(s) for s in cond_chiral],
    },
    'all_checks_pass': ok,
}
path = pathlib.Path(__file__).with_name('quantum_norm_cd_result.json')
path.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
sys.exit(0 if ok else 1)
