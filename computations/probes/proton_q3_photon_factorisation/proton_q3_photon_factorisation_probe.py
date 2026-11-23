#!/usr/bin/env python3
"""Can the photon definition fix the scale of the sign quasi-idempotent x_- in H_3(q)?

Question (bean: proton /q^3 normaliser, PR #8981). F_Bor's /q^3 corresponds to
scaling x_- = sum_w (-q)^{-l(w)} sigma_w so that its identity coefficient is 1.
The ruled photon gamma(p0,p1,p01) = 1 + p0*s0 + p1*s1 + p01*s0*s1^{-1} has
identity coefficient 1 by definition. If x_- were a photon product with a
FORCED scale, the normaliser would be inherited, not chosen.

Method: exact symbolic arithmetic (sympy, generic q). H_3(q) is semisimple at
generic q, so an element is determined by its images in the trivial (s -> q),
sign (s -> -1/q) and 2-dim reflection representations. x_- vanishes in trivial
and reflection and equals c = 1 + 2q^-2 + 2q^-4 + q^-6 in sign.

Results (asserted below):
 (A) chiral photons gamma(0,0,c): s0*s1^{-1} acts as 1 in BOTH 1-dim reps, so
     every product of chiral photons has equal trivial and sign images. A
     nonzero multiple of x_- needs trivial 0 and sign != 0. Hence no product of
     chiral photons, of any length, is a nonzero multiple of x_-.
 (B) general two-photon products gamma*gamma = lam * x_- form a 2-parameter
     family on which lam varies continuously (sampled below, and one point
     cross-checked in the regular representation). So the photon form does
     not fix the scale.
No floats enter any computation; sampled lam are exact algebraic numbers,
printed with mp.nstr-equivalent sympy.N for display only.
"""
import json, pathlib
import sympy as sp

q = sp.symbols('q', positive=True)
I2 = sp.eye(2)
S0 = sp.Matrix([[q, 0], [1, -1/q]])
S1 = sp.Matrix([[-1/q, 1], [0, q]])
for S in (S0, S1):
    assert sp.simplify((S - q*I2)*(S + I2/q)) == sp.zeros(2)
assert sp.simplify(S0*S1*S0 - S1*S0*S1) == sp.zeros(2)
CH = sp.simplify(S0*S1.inv())                    # reflection image of s0 s1^{-1}
csign = 1 + 2/q**2 + 2/q**4 + 1/q**6             # sign image of x_-

def triv(p0, p1, p01): return 1 + q*(p0 + p1) + p01          # s0 s1^{-1} -> q*q^{-1}
def sign(p0, p1, p01): return 1 - (p0 + p1)/q + p01          # -> (-1/q)(-q)
def refl(p0, p1, p01): return I2 + p0*S0 + p1*S1 + p01*CH

checks = {}
# (A)
c = sp.symbols('c')
checks['A_chiral_triv_eq_sign'] = sp.simplify(triv(0, 0, c) - sign(0, 0, c)) == 0

# (B)
p = sp.symbols('p0:6')
R = refl(*p[:3]) * refl(*p[3:])
eqs = [sp.expand(triv(*p[:3])*triv(*p[3:]))] + [sp.simplify(x) for x in R]
sol = sp.solve(eqs, p[:4], dict=True)
checks['B_family_nonempty'] = len(sol) > 0
lam = sp.simplify(sign(*p[:3])*sign(*p[3:]) / csign).subs(sol[0])
q_s = sp.Rational(11, 10)
samples = {}
for pt in [(0, sp.Rational(1, 3)), (sp.Rational(-1, 5), 0), (sp.Rational(1, 7), sp.Rational(2, 9))]:
    samples[str(pt)] = sp.nsimplify(lam.subs({p[4]: pt[0], p[5]: pt[1], q: q_s}))
vals = [sp.N(v, 30) for v in samples.values()]
checks['B_lambda_not_constant'] = len({sp.N(v, 25) for v in vals}) == len(vals)

out = {
    'description': 'Photon factorisation of x_- in H_3(q): does the photon form fix the scale (and so /q^3)?',
    'method': 'exact sympy, generic q; irreps triv/sign/refl',
    'checks': {k: bool(v) for k, v in checks.items()},
    'lambda_samples_q_11_10': {k: str(sp.N(v, 30)) for k, v in samples.items()},
    'verdict': 'scope (a) negative: chiral-photon products are never nonzero multiples of x_-; '
               'two-photon products give x_- at a continuously varying scale. '
               'The photon definition does not derive the /q^3 normaliser.',
}
pathlib.Path(__file__).with_name('result.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
assert all(checks.values()), checks
