"""Exact H_3(q) arithmetic for the four-term chiral photon (def:photon).

gamma(phi) = 1 + phi0 s0 + phi1 s1 + phi01 s0 s1^{-1}   (owner ruling 2026-11-18,
confirmed 2026-11-20, bean qou-99qc). s1^{-1} = s1 - h, h = q - q^{-1}.

Elements are dicts {reduced word: coefficient} over the six reduced words of S_3,
coefficients sympy expressions in the symbol q. No floats, no anchor.
Markov trace: convention D, z = q^3/(q^2+1) (AGENTS.md R1).
Wedderburn blocks: sym (s -> q), alt (s -> -q^{-1}), std (2x2, solved below).
"""
from __future__ import annotations

import sympy as sp

q = sp.Symbol("q", positive=True)
h = q - 1 / q
WORDS = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
NAMES = {(): "1", (0,): "s0", (1,): "s1", (0, 1): "L+", (1, 0): "L-", (0, 1, 0): "e-"}
GRADE = {w: len(w) for w in WORDS}


def _canon(w):
    return (0, 1, 0) if w == (1, 0, 1) else w


def _gen_times(s, w):
    w = _canon(w)
    if len(w) == 3:
        return {w: h, (1 - s, s): 1}
    if w and w[0] == s:
        return {w: h, w[1:]: 1}
    return {_canon((s,) + w): 1}


def simp(a):
    out = {}
    for w, c in a.items():
        c = sp.factor(sp.simplify(c))
        if c != 0:
            out[w] = c
    return out


def mul(a, b):
    out = {}
    for wa, ca in a.items():
        for wb, cb in b.items():
            cur = {wb: cb * ca}
            for s in reversed(wa):
                nxt = {}
                for w, c in cur.items():
                    for w2, c2 in _gen_times(s, w).items():
                        nxt[w2] = nxt.get(w2, 0) + c * c2
                cur = nxt
            for w, c in cur.items():
                out[w] = out.get(w, 0) + c
    return simp(out)


def add(*xs):
    out = {}
    for x in xs:
        for w, c in x.items():
            out[w] = out.get(w, 0) + c
    return simp(out)


def scale(c, x):
    return simp({w: c * v for w, v in x.items()})


ONE, S0, S1 = {(): 1}, {(0,): 1}, {(1,): 1}
S0INV = {(0,): 1, (): -h}
S1INV = {(1,): 1, (): -h}
V = mul(S0, S1INV)          # chiral vertex s0 s1^{-1}
LP = {(0, 1): 1}            # L+ = s0 s1, the superseded fourth term


def word(*letters):
    """Product of signed generators: +1 -> s0, -1 -> s0^-1, +2 -> s1, -2 -> s1^-1."""
    m = {1: S0, -1: S0INV, 2: S1, -2: S1INV}
    out = ONE
    for g in letters:
        out = mul(out, m[g])
    return out


def gamma(a0, a1, a01):
    """def:photon (chiral vertex)."""
    return add(ONE, scale(a0, S0), scale(a1, S1), scale(a01, V))


def gamma_straight(a0, a1, a01):
    """The superseded straight form 1 + a0 s0 + a1 s1 + a01 s0 s1."""
    return add(ONE, scale(a0, S0), scale(a1, S1), scale(a01, LP))


# The only corpus-derived colour weights: the eigenvalue pair of
# mass-theory/borromean-two-photon-factorisation (V^3 = gamma_plus * gamma_minus).
GAMMA_PLUS = gamma(0, 0, q * h)
GAMMA_MINUS = gamma(0, 0, -h / q)

# ---- Markov trace, convention D ------------------------------------------
z = q**3 / (q**2 + 1)
TR_BASIS = {(): 1, (0,): z, (1,): z, (0, 1): z**2, (1, 0): z**2, (0, 1, 0): z * (h * z + 1)}


def trace(a):
    return sp.factor(sp.simplify(sum(c * TR_BASIS[w] for w, c in a.items())))


# ---- Wedderburn blocks --------------------------------------------------
def _std():
    a, b, d = sp.symbols("a b d")
    M0 = sp.Matrix([[q, 0], [0, -1 / q]])
    M1 = sp.Matrix([[a, b], [1, d]])
    eqs = list(M1 * M1 - h * M1 - sp.eye(2)) + list(M0 * M1 * M0 - M1 * M0 * M1)
    sol = sp.solve(eqs, [a, b, d], dict=True)
    sol = [s for s in sol if sp.simplify(s[a] - s[d]) != 0][0]
    return M0, M1.subs(sol).applyfunc(sp.simplify)


STD0, STD1 = _std()
IRREP = {"sym": (sp.Matrix([[q]]), sp.Matrix([[q]])),
         "std": (STD0, STD1),
         "alt": (sp.Matrix([[-1 / q]]), sp.Matrix([[-1 / q]]))}


def block(a, lam):
    M0, M1 = IRREP[lam]
    n = M0.shape[0]
    out = sp.zeros(n, n)
    for w, c in a.items():
        M = sp.eye(n)
        for s in w:
            M = M * (M0 if s == 0 else M1)
        out += c * M
    return out.applyfunc(lambda e: sp.factor(sp.simplify(e)))


def chi(a, lam):
    return sp.factor(sp.simplify(block(a, lam).trace()))


def grades(a):
    return sorted({GRADE[w] for w in a})


def _selfcheck():
    # relations in the std rep, vertex identity, factorisation
    assert block(mul(S1, S1INV), "std") == sp.eye(2)
    assert add(V, scale(-1, add(LP, scale(-h, S0)))) == {}
    assert add(mul(mul(V, V), V), scale(-1, mul(GAMMA_PLUS, GAMMA_MINUS))) == {}
    for f in (sp.Symbol("x"), 0):
        pass
    x0, x1, x2 = sp.symbols("x0 x1 x2")
    assert add(gamma(x0, x1, x2), scale(-1, gamma_straight(x0 - h * x2, x1, x2))) == {}
    # tr_M is a trace: tr(ab) = tr(ba) on a sample pair
    assert sp.simplify(trace(mul(V, S1)) - trace(mul(S1, V))) == 0
    return True


_selfcheck()
