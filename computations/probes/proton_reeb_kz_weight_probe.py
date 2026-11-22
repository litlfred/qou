"""Reeb weight on the proton weight space from the KZ identification.

Audit: docs/audits/2026-11-21-proton-two-twelve-count-survey.md section 4. Issue #8967.
Lean twin: QOU/MassTheory/ProtonReebKZWeight.lean.

Exact part (sympy): R = 2*kappa*sum_{i<j}(P_ij - c) on the one-e2 weight space of (C^2)^3,
built from the permutation action, not from the closed form J.
Comparison part (mpmath, 50 dps): kappa_0 = ln q0 / (2 pi i) at the proton pin, so
k^2 = -9 kappa_0^2 = 9 (ln q0)^2 / (4 pi^2). This is a comparison, not a proof input.
"""
import itertools
import sympy as sp
import mpmath as mp

kappa, c = sp.symbols("kappa c")
states = [s for s in itertools.product([0, 1], repeat=3) if sum(s) == 1]  # one e2

def P(i, j):
    M = sp.zeros(3, 3)
    for b, s in enumerate(states):
        t = list(s); t[i], t[j] = t[j], t[i]
        M[states.index(tuple(t)), b] = 1
    return M

S = P(0, 1) + P(0, 2) + P(1, 2)
R = 2 * kappa * (S - 3 * c * sp.eye(3))
R2 = sp.expand(R * R)
off = sp.factor(R2[0, 1])
print("sum P_ij on W_p =", S.tolist())
print("off-diagonal of R^2 =", off, "-> zero iff c = 1/2 (kappa != 0)")
R2h = sp.simplify(R2.subs(c, sp.Rational(1, 2)))
print("R^2 at c=1/2 =", R2h.tolist())
tr = sp.simplify(R2h.trace())
print("trace =", tr, "; trace = -12 iff kappa^2 =", sp.solve(sp.Eq(tr, -12), kappa**2))

mp.mp.dps = 50
from qou_substrate.constants import Q_50_DIGIT_STR  # proton pin (default), 50 digits
q0 = mp.mpf(Q_50_DIGIT_STR)
k2 = 9 * mp.log(q0) ** 2 / (4 * mp.pi ** 2)
print("q0 (proton pin) =", mp.nstr(q0, 20))
print("k^2 at q0 = 9 (ln q0)^2 / (4 pi^2) =", mp.nstr(k2, 20), "; k =", mp.nstr(mp.sqrt(k2), 20))
print("q needed for k = 2: exp(+-4 pi/3) =", mp.nstr(mp.exp(4 * mp.pi / 3), 20), mp.nstr(mp.exp(-4 * mp.pi / 3), 20))
