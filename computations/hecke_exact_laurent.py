#!/usr/bin/env python3
"""Fast EXACT Hecke reduction: sparse Z[q,q^-1] instead of sympy.

Why this exists
---------------
The pure-sympy reducer in `jet_history_retention_probe` calls `sp.simplify()`
on every coefficient addition. That, not the algebra, is the wall: the H_9
support is ~500 terms, nowhere near the 9! = 362880 a dense-basis estimate
suggests. Measured by the H_9 investigation: H_6 14.7 s -> 0.001 s, H_9
191 s -> 0.016 s.

Coefficients here are dicts {exponent: int} over Z[q, q^-1] -- exact, no
floats, no mpmath, canonical by construction (zero coefficients are dropped),
so equality is dict equality and needs no simplification pass.

Correctness is not assumed: `crosscheck_against_sympy()` verifies support and
every coefficient against the sympy reducer on H_6, and is run by __main__.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

#: A Laurent polynomial is {exponent: coefficient}, both int. Empty dict = 0.
Lau = dict

ONE: Lau = {0: 1}
#: A = q - q^-1, the Hecke structure constant.
A_COEF: Lau = {1: 1, -1: -1}


def lau_add(x: Lau, y: Lau) -> Lau:
    out = dict(x)
    for e, c in y.items():
        v = out.get(e, 0) + c
        if v:
            out[e] = v
        else:
            out.pop(e, None)
    return out


def lau_mul(x: Lau, y: Lau) -> Lau:
    out: Lau = {}
    for e1, c1 in x.items():
        for e2, c2 in y.items():
            e = e1 + e2
            v = out.get(e, 0) + c1 * c2
            if v:
                out[e] = v
            else:
                out.pop(e, None)
    return out


def lau_neg(x: Lau) -> Lau:
    return {e: -c for e, c in x.items()}


def perm_apply_s(perm: tuple, i: int) -> tuple:
    p = list(perm)
    p[i - 1], p[i] = p[i], p[i - 1]
    return tuple(p)


def coxeter_length(perm: tuple) -> int:
    n = len(perm)
    return sum(1 for a in range(n) for b in range(a + 1, n) if perm[a] > perm[b])


class FastHecke:
    """Element of H_n(q) as {permutation: Lau}."""

    __slots__ = ("n", "terms")

    def __init__(self, n: int, terms: dict | None = None):
        self.n = n
        self.terms = dict(terms) if terms else {}

    @staticmethod
    def one(n: int) -> "FastHecke":
        return FastHecke(n, {tuple(range(1, n + 1)): dict(ONE)})

    def _add(self, w, c: Lau) -> None:
        cur = lau_add(self.terms.get(w, {}), c)
        if cur:
            self.terms[w] = cur
        else:
            self.terms.pop(w, None)

    def mul_gen(self, i: int, inverse: bool = False) -> "FastHecke":
        out = FastHecke(self.n)
        for w, c in self.terms.items():
            wsi = perm_apply_s(w, i)
            if coxeter_length(wsi) > coxeter_length(w):
                out._add(wsi, c)
            else:
                out._add(w, lau_mul(c, A_COEF))
                out._add(wsi, c)
            if inverse:
                out._add(w, lau_neg(lau_mul(c, A_COEF)))
        return out

    def profile(self) -> dict:
        prof: dict = {}
        for w, c in self.terms.items():
            prof.setdefault(coxeter_length(w), {})[w] = c
        return prof


def word_to_elem_fast(n: int, word) -> "FastHecke":
    E = FastHecke.one(n)
    for g in word:
        E = E.mul_gen(abs(g), inverse=(g < 0))
    return E


def n_differing(X: "FastHecke", Y: "FastHecke") -> int:
    """Coefficients differing. Exact dict comparison -- no simplification."""
    return sum(1 for w in set(X.terms) | set(Y.terms)
               if X.terms.get(w, {}) != Y.terms.get(w, {}))


def crosscheck_against_sympy() -> bool:
    """Verify this backend against the sympy reducer on H_6. Not optional."""
    import sympy as sp
    from jet_history_retention_probe import word_to_elem, q
    from isospin_triplet_filtration_probe import P_A, N_B, BRIDGE

    word = P_A + N_B + [BRIDGE, BRIDGE]
    slow, _ = word_to_elem(6, word)
    fast = word_to_elem_fast(6, word)
    if set(slow.terms) != set(fast.terms):
        print("  CROSSCHECK FAILED: support differs")
        return False
    bad = 0
    for w, c_slow in slow.terms.items():
        c_fast = sum(co * q ** e for e, co in fast.terms[w].items())
        if sp.simplify(c_slow - c_fast) != 0:
            bad += 1
    print(f"  crosscheck vs sympy on H_6: support identical "
          f"({len(slow.terms)} terms), coefficients differing: {bad}")
    return bad == 0


if __name__ == "__main__":
    import time
    ok = crosscheck_against_sympy()
    assert ok, "fast backend disagrees with sympy -- do not use it"
    from isospin_triplet_filtration_probe import P_A, N_B, BRIDGE
    t = time.time()
    word_to_elem_fast(6, P_A + N_B + [BRIDGE, BRIDGE])
    print(f"  H_6 build: {time.time() - t:.4f} s")
