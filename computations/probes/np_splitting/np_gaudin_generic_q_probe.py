#!/usr/bin/env python3
"""Generic-q version of the q-Casimir pair readout (np_gaudin_pair_charge_probe.py, X = G-q(op=False)).

Every quantity is computed in Z[q, q^-1] (Laurent polynomials with integer/Fraction
coefficients), so the result holds identically in q, not at sample points.
The Casimir is scaled by h^2 = (q - q^-1)^2 to clear its denominator; that scale
cancels in pp = nn and multiplies the interaction by h^2.
Exact arithmetic only; no floats anywhere.
"""
from fractions import Fraction
import np_gaudin_pair_charge_probe as P


class LP:
    __slots__ = ("c",)

    def __init__(self, c=None):
        self.c = {k: v for k, v in (c or {}).items() if v}

    @staticmethod
    def of(x):
        if isinstance(x, LP):
            return x
        return LP({0: Fraction(x)}) if x else LP()

    def __add__(self, o):
        o = LP.of(o)
        d = dict(self.c)
        for k, v in o.c.items():
            d[k] = d.get(k, 0) + v
        return LP(d)

    __radd__ = __add__

    def __neg__(self):
        return LP({k: -v for k, v in self.c.items()})

    def __sub__(self, o):
        return self + (-LP.of(o))

    def __rsub__(self, o):
        return LP.of(o) - self

    def __mul__(self, o):
        o = LP.of(o)
        d = {}
        for a, x in self.c.items():
            for b, y in o.c.items():
                d[a + b] = d.get(a + b, 0) + x * y
        return LP(d)

    __rmul__ = __mul__

    def __rtruediv__(self, o):  # o / self, self must be a monomial
        assert len(self.c) == 1, "division only by a monomial"
        (k, v), = self.c.items()
        return LP.of(o) * LP({-k: 1 / v})

    def __truediv__(self, o):
        return self * (1 / LP.of(o))

    def __pow__(self, n):
        r = LP.of(1)
        base = self if n >= 0 else 1 / self
        for _ in range(abs(n)):
            r = r * base
        return r

    def __eq__(self, o):
        return self.c == LP.of(o).c

    def __hash__(self):
        return hash(tuple(sorted(self.c.items())))

    def __bool__(self):
        return bool(self.c)

    def __repr__(self):
        return " + ".join(f"{v}*q^{k}" for k, v in sorted(self.c.items())) or "0"


P.F = LP.of  # every F(...) inside the engine now builds a Laurent polynomial
q = LP({1: Fraction(1)})


def scaled_casimir(S, sites):
    """h^2 * C_q with the Ř-compatible coproduct (op=False)."""
    E = P.cop(S, "e", sites, False)
    Fm = P.cop(S, "f", sites, False)
    Kp, Km = P.Kop(S, sites)
    return P.add(P.mul(Fm, E), Kp, Km, coeffs=[S["h"] ** 2, q, 1 / q])


def main():
    S = P.setup(q)
    S = {k: ([[LP.of(x) for x in r] for r in v] if isinstance(v, list) else v) for k, v in S.items()}
    A, B, AB = [0, 1, 2], [3, 4, 5], list(range(6))
    R01 = P.two_site(0, S["Rt"])
    print("Ř commutes with Δe, Δf (op=False) on sites 0,1, generic q:",
          P.commutes(R01, P.cop(S, "e", [0, 1], False)) and P.commutes(R01, P.cop(S, "f", [0, 1], False)))
    V = [(0, False), (1, True)] * 3 + [(3, False), (4, True)] * 3
    base = P.word(S, V)
    Kd = {}
    for s in range(P.D):
        z = sum(1 for x in P.bits(s) if x == 0)
        Kd[s] = q ** (2 * z - P.N)
    CAB = scaled_casimir(S, AB)
    print("h^2 C_AB central (commutes with Δe on 6 sites), generic q:", P.commutes(CAB, P.cop(S, "e", AB, False)))
    X = P.add(CAB, scaled_casimir(S, A), scaled_casimir(S, B), coeffs=[1, -1, -1])
    T1 = P.readout(S, base, Kd, P.eye())
    TX = P.readout(S, base, Kd, X)
    keys = [(1, 1), (1, 0), (0, 1), (0, 0)]
    for k in keys:
        print(f"T1{k} = {T1[k]}\nTX{k} = {TX[k]}")
    pp, pn, np_, nn = keys
    # pp = nn  <=>  TX[pp]*T1[nn] - TX[nn]*T1[pp] == 0 in Z[q,q^-1]
    d_ppnn = TX[pp] * T1[nn] - TX[nn] * T1[pp]
    print("\nCLAIM 1 (pp = nn identically in q):", d_ppnn == 0, " residual:", d_ppnn)
    # interaction: dE_pp - dE_pn - dE_np + dE_nn == h^2 [2]_q, cleared over the product of T1's
    prod = T1[pp] * T1[pn] * T1[np_] * T1[nn]
    lhs = (TX[pp] * T1[pn] * T1[np_] * T1[nn] - TX[pn] * T1[pp] * T1[np_] * T1[nn]
           - TX[np_] * T1[pp] * T1[pn] * T1[nn] + TX[nn] * T1[pp] * T1[pn] * T1[np_])
    rhs = (S["h"] ** 2) * (q + 1 / q) * prod
    print("CLAIM 2 (pp - pn - np + nn = [2]_q identically in q):", lhs == rhs)
    d_pnnp = TX[pn] * T1[np_] - TX[np_] * T1[pn]
    print("pn = np identically?", d_pnnp == 0)
    # KZ monodromy M = beta_AB^2 (block A passed once round block B), generic q
    beta = P.word(S, [(2, False), (1, False), (0, False), (3, False), (2, False), (1, False), (4, False), (3, False), (2, False)])
    TM = P.readout(S, base, Kd, P.mul(beta, beta))
    d_M = TM[pp] * T1[nn] - TM[nn] * T1[pp]
    print("CLAIM 3 (M: pp = nn identically in q):", d_M == 0, " residual:", d_M)
    print("sector shift: T1[pp] == q^4 T1[nn]:", T1[pp] == q ** 4 * T1[nn],
          "; TX[pp] == q^4 TX[nn]:", TX[pp] == q ** 4 * TX[nn],
          "; TM[pp] == q^4 TM[nn]:", TM[pp] == q ** 4 * TM[nn])


if __name__ == "__main__":
    main()
