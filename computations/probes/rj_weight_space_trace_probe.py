"""Weight-space traces of the torus braid on V^{(x)r} (exact, sympy over Q(q)).

Companion to QOU/Archimedean/RossoJonesGeneral.lean (bean qou-q425).

Model: V = Q(q)^2, sigma_i = Jimbo's R-check on sites (i, i+1) exactly as
`QOU.IwahoriHecke.RMatrix.rCheck q q^{-1}`:
    R e_{xx} = q e_{xx};  R e_{01} = e_{10} + (q - q^{-1}) e_{01};  R e_{10} = e_{01}.
gamma = sigma_0 sigma_1 ... sigma_{r-2} (matrix product, `cox`).

T_m(s) := trace of gamma^s on the weight space spanned by the basis states with m ones.

The Lean file proves (sorry-free) that, for every Markov trace t with z_D,
    q^{2s} (q^2+1)^r t(gamma^s) = sum_{m=0}^{r} q^{2m} q^{2s} T_m(s),
that T_0(s) = T_r(s) = q^{s(r-1)}, and that the Rosso-Jones value follows from the
named hypothesis
    MiddleWeightTraces r s :  q^{2s} T_m(s) = q^{s(r+1)} - q^{s(r-1)}   for 0 < m < r.
This probe checks that hypothesis exactly for small (r, s), and records where it FAILS
(non-coprime s), so the hypothesis is not mistaken for a statement true for all s.

Exact arithmetic only (sympy rational functions); no floats.
"""
import itertools
import math

import sympy as sp

q = sp.symbols('q')
qi = 1 / q


def rcheck(a, b):
    if a == b:
        if b[0] == b[1]:
            return q
        return q - qi if b[0] < b[1] else 0
    return 1 if a == (b[1], b[0]) else 0


def sigma(r, i):
    states = list(itertools.product(range(2), repeat=r))
    pos = {s: k for k, s in enumerate(states)}
    M = sp.zeros(len(states), len(states))
    for b in states:
        for a in states:
            if all(a[k] == b[k] for k in range(r) if k not in (i, i + 1)):
                v = rcheck((a[i], a[i + 1]), (b[i], b[i + 1]))
                if v != 0:
                    M[pos[a], pos[b]] = v
    return M, states


def gamma(r):
    G = sp.eye(2 ** r)
    states = None
    for i in range(r - 1):
        S, states = sigma(r, i)
        G = G * S
    return G, states


def weight_traces(r, s):
    G, states = gamma(r)
    Gs = G ** s
    T = [0] * (r + 1)
    for k, u in enumerate(states):
        T[sum(u)] += Gs[k, k]
    return [sp.expand(sp.simplify(x)) for x in T]


def main():
    ok = True
    for r in range(2, 6):
        for s in range(1, 2 * r + 2):
            T = weight_traces(r, s)
            ext = sp.expand(q ** (s * (r - 1)))
            ext_ok = sp.simplify(T[0] - ext) == 0 and sp.simplify(T[r] - ext) == 0
            mid = sp.expand(q ** (s * (r + 1)) - q ** (s * (r - 1)))
            mid_ok = all(sp.simplify(q ** (2 * s) * T[m] - mid) == 0 for m in range(1, r))
            cop = math.gcd(r, s) == 1
            print(f"r={r} s={s} gcd1={cop} extremal={ext_ok} middle_hypothesis={mid_ok}")
            if not ext_ok:
                ok = False
            if cop and not mid_ok:
                ok = False
    print("ALL coprime cases satisfy MiddleWeightTraces:" , ok)


if __name__ == "__main__":
    main()
