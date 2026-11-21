"""Corpus check (not a target test). Exact sympy, no floats.

def:mass-identity (mass-endomorphism/mass-identity.md) uses the holonomy linearly and expands each
crossing as T(s_a) = q*1 - e_a, T(s_a^-1) = q^-1*1 - e_a, e_a = q*1 - Rcheck_a. Then
Hol = sum over states s in {0,1}^k of w_TL(s) * TL(s); the all-zero state is prod c(l_j) * 1.
Claim checked here: for V^3 = (s0 s1^-1)^3 (writhe 0), the all-zero coefficient is 1, so
hol - 1 = the sum of the s != 0 (Temperley-Lieb loop) states, exactly.
"""
import json, itertools, sympy as sp

q = sp.symbols('q', positive=True)
Rc = sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,q-1/q,0],[0,0,0,q]])
I2, I8 = sp.eye(2), sp.eye(8)
R = [sp.kronecker_product(Rc, I2), sp.kronecker_product(I2, Rc)]
e = [q*I8 - R[0], q*I8 - R[1]]
word = [(0, +1), (1, -1)] * 3
c = {+1: q, -1: 1/q}
hol = I8
for a, s in word:
    hol = hol * (R[a] if s == +1 else R[a].inv())
hol = sp.simplify(hol)
total = sp.zeros(8); nonzero = sp.zeros(8); allzero_coeff = None
for st in itertools.product([0, 1], repeat=len(word)):
    w = sp.Integer(1); M = I8
    for (a, s), b in zip(word, st):
        if b == 0: w *= c[s]
        else: w *= -1; M = M * e[a]
    term = sp.simplify(w * M)
    total += term
    if any(st): nonzero += term
    else: allzero_coeff = sp.simplify(w)
res = {
  "checks": {
    "e_a^2 = [2]_q e_a": all(sp.simplify(x*x - (q + 1/q)*x) == sp.zeros(8) for x in e),
    "state sum = hol": sp.simplify(total - hol) == sp.zeros(8),
    "all-zero coefficient = 1 (writhe 0)": allzero_coeff == 1,
    "hol - 1 = sum of s != 0 states": sp.simplify(nonzero - (hol - I8)) == sp.zeros(8),
  },
  "states": 2 ** len(word),
  "note": ("hol - 1 is the Temperley-Lieb (s != 0) part of the corpus's own state sum for the "
           "mass identity. log hol has no counterpart in that linear expansion. This is a reason "
           "for the reading, not a proof that the nabla in D equals hol - 1."),
}
res["all_checks_pass"] = all(res["checks"].values())
s = json.dumps(res, indent=2); print(s)
open(__file__.replace('.py', '.out.json'), 'w').write(s + "\n")
