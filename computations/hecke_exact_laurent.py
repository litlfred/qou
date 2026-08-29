#!/usr/bin/env python3
"""Fast EXACT Hecke reduction: sparse Z[q,q^-1] instead of sympy.

Why this exists
---------------
The pure-sympy reducer in `jet_history_retention_probe` calls `sp.simplify()`
on every coefficient addition. That, not the algebra, is the wall: the H_9
support is ~500 terms, nowhere near the 9! = 362880 a dense-basis estimate
suggests. Measured: H_6 14.7 s -> 0.0015 s, H_9 191 s -> 0.018 s.

## Where the speedup actually comes from -- CORRECTED

I first described this as "sympy -> Laurent". Decomposed on the same reducer,
same word, per-coefficient-verified at every rung, that is wrong:

    coefficient kernel                  H_6      H_9     vs int-dict
    sp.simplify(sp.expand(..)) per add  16.12 s  196.0 s  x10235 / x10835
    sp.expand only                       0.030    0.202   x19 -> x5.8
    sympy raw add, no expand             0.0054   0.039   x3.4 -> x1.7
    pyhecke.laurent_q.LaurentQ           0.0071   0.071   x4.5 -> x3.3
    int-dict Z[q,q^-1] (this module)     0.0016   0.018   --

**~99.8 % of the win is deleting `sp.simplify` from the inner loop.** The
representation contributes 2-4x, and that shrinks with n (3.4x -> 1.7x). So
the thing to look for elsewhere is not "sympy" but A CANONICALISING SYMPY
CALL INSIDE A PER-TERM LOOP.

## Prior art -- this re-derives existing infrastructure

`tools/pyhecke/python/pyhecke/laurent_q.py` already implements the same
sparse {exp: coef} design (rational-valued), `computations/laurent_q.py`
shims to it, `computations/hecke/hecke_laurent_fast.py` builds Hecke elements
on it, and the compute-audit skill's pattern **P17** already prescribes this
substitution. The int-dict here is genuinely the fastest of them, but it is
a variant of a known idea, not a new one.

## 🛑 RING HAZARD -- int coefficients are NOT always enough

Coefficients here are `{exponent: int}` over **Z**[q,q^-1]. That is correct
for the plain Hecke rule (h = q - 1/q has integer coefficients), and WRONG
without warning for anything landing in Q[q,q^-1]. Known cases:

  - `hecke_symbolic.D_MIX = -(q - 1/q)/2`  -- the pn-mixed crossing
  - the colour delta (q-1)^2 (1 - q^-4)/3  -- carries a 1/3

Python's `int` will silently floor-divide or refuse, so a caller who needs Q
gets a wrong answer rather than an error. Use `fractions.Fraction` values --
the arithmetic here is generic over the coefficient type, and Fraction costs
3.1-12.9x over int while remaining ~1000x faster than sympy.
`canonical_color_bridge_tau_probe.py` does exactly this for the colour delta.

## Memory -- this module is the WRONG tool if memory is the wall

Measured retained size of the final element:

                  H_6      H_9      H_12
    int-dict     0.034 MB  0.532 MB  6.61 MB
    sympy raw    0.010     0.096     0.95 MB   <- 7x SMALLER

sympy interns and shares identical coefficient objects across terms; a fresh
dict per term throws that sharing away. If memory is the binding constraint,
this substitution moves the wall EARLIER. The fix is hash-consing the
coefficient dicts (measured 13.6x at H_12, 18.9x at H_15, H_18 in 222 MB
peak), not packing the keys -- keys are only ~10 % of the bytes.

Correctness is not assumed: `crosscheck_against_sympy()` verifies support and
every coefficient against the sympy reducer on H_6, and is asserted in
__main__ so the module cannot be used while disagreeing with what it replaces.
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
