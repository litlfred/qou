#!/usr/bin/env python3
"""Read off the 3x3 sector matrices used in QOU/QBeta/BlockChargeSectorTrace.lean (exact sympy).

Jimbo R on two sites, u = bit 0. Restrict sigma_0 = R (x) 1 and sigma_1 = 1 (x) R on V^{(x)3}
to the one-u sector (basis udd, dud, ddu) and the two-u sector (basis uud, udu, duu).
"""
import sympy as sp

q = sp.symbols("q", nonzero=True)
h = q - 1 / q
R = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]])
I2 = sp.eye(2)
S = [sp.kronecker_product(R, I2), sp.kronecker_product(I2, R)]
A0 = sp.Matrix([[0, 1, 0], [1, h, 0], [0, 0, q]])
A1 = sp.Matrix([[q, 0, 0], [0, 0, 1], [0, 1, h]])


def sector(nu):
    return [i for i in range(8) if sum(1 for k in range(3) if not (i >> (2 - k)) & 1) == nu]


one, two = sector(1), sector(2)
print("one-u sector indices", one, " two-u sector indices", two)
ok = (S[0].extract(one, one) == A0 and S[1].extract(one, one) == A1
      and S[0].extract(two, two) == A1 and S[1].extract(two, two) == A0)
print("sigma0 -> A0, sigma1 -> A1 on one-u; sigma0 -> A1, sigma1 -> A0 on two-u:", ok)

# --- h^2 C on three sites, restricted to each charge sector, equals the matrix G of the Lean file ---
import np_gaudin_generic_q_probe as GQ  # noqa: E402

G = sp.Matrix([
    [(q**6 + q**4 - q**2 + 1) / q**4, (q**2 - 1)**2 / q**3, (q**2 - 1)**2 / q**2],
    [(q**2 - 1)**2 / q**3, 2 * (q**4 - q**2 + 1) / q**2, (q**2 - 1)**2 / q],
    [(q**2 - 1)**2 / q**2, (q**2 - 1)**2 / q, (q**6 - q**4 + q**2 + 1) / q**2]])


def to_sym(x):
    return sum(sp.Rational(v.numerator, v.denominator) * q**k for k, v in GQ.LP.of(x).c.items())


S6 = GQ.P.setup(GQ.q)
S6 = {k: ([[GQ.LP.of(x) for x in r] for r in v] if isinstance(v, list) else v) for k, v in S6.items()}
C3 = GQ.scaled_casimir(S6, [0, 1, 2])
# sites 3,4,5 held at d (bit 1); sites 0,1,2 run over the sector basis in the same order as above
emb = {nu: [(i << 3) | 0b111 for i in sector(nu)] for nu in (1, 2)}
okG = all(sp.simplify(sp.Matrix(3, 3, lambda a, b: to_sym(C3[emb[nu][a]][emb[nu][b]])) - G) == sp.zeros(3, 3)
          for nu in (1, 2))
print("h^2 C on sites 0,1,2 restricted to the one-u and to the two-u sector equals G:", okG)
print("G commutes with A0 and A1:",
      sp.simplify(A0 * G - G * A0) == sp.zeros(3, 3) and sp.simplify(A1 * G - G * A1) == sp.zeros(3, 3))
