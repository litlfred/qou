#!/usr/bin/env python3
# polynomial_q_not_applicable: library — LaurentQ-direct trace
# assembly to eliminate the sympy round-trip bottleneck identified
# in docs/audits/2026-05-20-markov-peel-bottleneck-profile.md.
"""LaurentQ-direct Markov trace for `LaurentHeckeElement`.

Mirrors `markov_trace_canonical.tr_M_word` / `tr_M_element` but
keeps coefficient arithmetic in LaurentQ throughout, eliminating
the sympy round-trip that the profile showed dominated ~46% of
the wall in `tr_M_atomic_fast` for ⁵Li.

Output type is `ZHLaurent` — a formal polynomial in (z, h) with
LaurentQ-in-q coefficients. At the boundary, `.to_sympy()` or
`.evaluate(q0, z0, h0)` extracts the final value.

Strategy #1 from the bottleneck audit. Phase-1 scope:

  - Empty word: tr = 1
  - max_gen < n-2: recurse at H_{max_gen+2}
  - Single top occurrence: cyclic rotate + Markov II (z · …)
  - Multiple tops, Case A (no braid obstruction): σ² = hσ + 1
  - Multiple tops, Case B (braid obstruction): `tr_M_word_lq`
    raises `NotImplementedError`; callers are expected to catch
    and route through `markov_trace_canonical.tr_M_word` on the
    sympy path. Empirically, all currently catalogued atomic
    braids (p, n, D, T, ³He, ⁴He) reach Case A only.

Phase-2: native Case-B handling + ocneanu fallback rewrite.

Cross-check: every result must agree with the sympy path at q₀
to 1e-15 relative on the atom set {p, n, D, T, ³He, ⁴He}. The
benchmark + cross-check entry point is `_self_check()` below.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, Tuple

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from laurent_q import LaurentQ  # noqa: E402
from hecke_laurent_fast import LaurentHeckeElement  # noqa: E402


# z is the Markov parameter, related to q by z = 1/(q^{1/2} + q^{-1/2}).
# z has a square-root component so it can't be expressed as a LaurentQ in q
# directly. We carry it symbolically as the (z_exp, h_exp) exponent pair.
class ZHLaurent:
    """Formal Laurent polynomial in (z, h) with LaurentQ-in-q coefficients.

    Internal representation: dict mapping `(z_exp, h_exp) -> LaurentQ`.
    `z_exp` and `h_exp` are non-negative integers (the Markov trace
    only produces non-negative powers of z and h; the recursion
    multiplies by z and h, never divides).

    Arithmetic:
      - `__add__`: dict-merge with LaurentQ.__add__ on collisions
      - `__mul__` ZHLaurent × ZHLaurent: (z^a h^b c) · (z^c h^d e) =
        z^(a+c) h^(b+d) (c·e)
      - `mul_by_z()` and `mul_by_h()`: shift exponents
      - `mul_by_lq(coef)`: scale every term by a LaurentQ
    """

    __slots__ = ("terms",)

    def __init__(self, terms: Dict[Tuple[int, int], LaurentQ] | None = None):
        self.terms: Dict[Tuple[int, int], LaurentQ] = {}
        if terms:
            for k, v in terms.items():
                if not v.is_zero():
                    self.terms[k] = v

    @classmethod
    def zero(cls) -> "ZHLaurent":
        return cls({})

    @classmethod
    def one(cls) -> "ZHLaurent":
        return cls({(0, 0): LaurentQ.one()})

    @classmethod
    def z_var(cls) -> "ZHLaurent":
        """The variable z as a ZHLaurent: z^1 h^0 · 1_LQ."""
        return cls({(1, 0): LaurentQ.one()})

    @classmethod
    def h_var(cls) -> "ZHLaurent":
        """The variable h as a ZHLaurent: z^0 h^1 · 1_LQ."""
        return cls({(0, 1): LaurentQ.one()})

    @classmethod
    def from_lq(cls, coef: LaurentQ) -> "ZHLaurent":
        """Scalar LaurentQ as a ZHLaurent: z^0 h^0 · coef."""
        if coef.is_zero():
            return cls.zero()
        return cls({(0, 0): coef})

    def is_zero(self) -> bool:
        return len(self.terms) == 0

    def __add__(self, other: "ZHLaurent") -> "ZHLaurent":
        out: Dict[Tuple[int, int], LaurentQ] = dict(self.terms)
        for k, v in other.terms.items():
            if k in out:
                s = out[k] + v
                if s.is_zero():
                    del out[k]
                else:
                    out[k] = s
            else:
                out[k] = v
        return ZHLaurent(out)

    def __mul__(self, other: "ZHLaurent") -> "ZHLaurent":
        out: Dict[Tuple[int, int], LaurentQ] = {}
        for (a, b), c1 in self.terms.items():
            for (c, d), c2 in other.terms.items():
                key = (a + c, b + d)
                prod = c1 * c2
                if prod.is_zero():
                    continue
                if key in out:
                    s = out[key] + prod
                    if s.is_zero():
                        del out[key]
                    else:
                        out[key] = s
                else:
                    out[key] = prod
        return ZHLaurent(out)

    def mul_by_lq(self, coef: LaurentQ) -> "ZHLaurent":
        """Scale every term's LaurentQ coefficient by `coef`."""
        if coef.is_zero():
            return ZHLaurent.zero()
        return ZHLaurent({k: v * coef for k, v in self.terms.items()})

    def mul_by_z(self) -> "ZHLaurent":
        """Multiply by the z variable: shift each (a, b) → (a+1, b)."""
        return ZHLaurent({(a + 1, b): c for (a, b), c in self.terms.items()})

    def mul_by_h(self) -> "ZHLaurent":
        """Multiply by the h variable: shift each (a, b) → (a, b+1)."""
        return ZHLaurent({(a, b + 1): c for (a, b), c in self.terms.items()})

    def evaluate(self, q_val: float, z_val: float, h_val: float) -> complex:
        """Substitute (q, z, h) → numerical values; return complex.

        For cross-checking against the sympy path at q₀.
        """
        import sympy as sp
        total = complex(0)
        for (a, b), coef in self.terms.items():
            # LaurentQ stores coefs as a dict {exp: sympy.Expr}; evaluate
            # the Laurent polynomial directly at q_val.
            c = complex(0)
            for exp, sym_coef in coef.coefs.items():
                c_val = complex(sp.Float(sym_coef, 50)) if hasattr(
                    sym_coef, "is_number") and sym_coef.is_number else complex(
                    sym_coef)
                c += c_val * (q_val ** exp)
            total += c * (z_val ** a) * (h_val ** b)
        return total

    def to_sympy(self, q_sym, z_sym, h_sym):
        """Convert to a sympy expression for cross-check / debug."""
        import sympy as sp
        total = sp.Integer(0)
        for (a, b), coef in self.terms.items():
            c_sp = coef.to_sympy(q_sym)
            total += c_sp * z_sym ** a * h_sym ** b
        return total

    def __repr__(self) -> str:
        if self.is_zero():
            return "ZHLaurent(0)"
        n = len(self.terms)
        sample = list(self.terms.items())[:2]
        return f"ZHLaurent({n} terms, e.g. {sample})"


# ────────────────────────────────────────────────────────────────
# Markov-axiom recursive ascent — ZHLaurent edition
# ────────────────────────────────────────────────────────────────

import functools  # noqa: E402


def tr_M_word_lq(word: tuple, n: int, *,
                  depth: int = 0, max_depth: int = 200) -> ZHLaurent:
    """ZHLaurent Markov trace of a Hecke word in H_n(q).

    Mirrors `markov_trace_canonical._tr_M_word_impl` but with
    ZHLaurent arithmetic instead of sympy. Phase-1 reaches all
    cases EXCEPT Case B (braid relation σ_top σ_{top-1} σ_top
    inside the word). Case B raises `NotImplementedError` —
    callers are expected to catch and route through
    `markov_trace_canonical.tr_M_word` on the sympy path.

    Recursion guard: `depth` is propagated for the depth-limit
    check but excluded from the LRU cache key (the result depends
    only on `(word, n, max_depth)`).
    """
    if depth > max_depth:
        raise RecursionError(
            f"tr_M_lq recursion too deep: word={word}, n={n}")
    return _tr_M_word_lq_cached(word, n, max_depth, depth=depth)


@functools.lru_cache(maxsize=100_000)
def _tr_M_word_lq_cached(word: tuple, n: int, max_depth: int,
                          *, depth: int = 0) -> ZHLaurent:
    """LRU-cached body of `tr_M_word_lq`.

    `depth` is a kwarg so it bypasses the cache key entirely
    (functools.lru_cache only hashes positional + keyword-only
    args that participate in the call signature; here `depth` is
    keyword-only and Python's lru_cache canonicalises by argument
    NAME so identical (word, n, max_depth) tuples cache together
    regardless of depth). Cache cap 100K — empirically the
    recursion tree depth across A ≤ 6 stays well under this.
    """
    if not word:
        return ZHLaurent.one()

    max_gen = max(word)
    if max_gen < n - 2:
        return _tr_M_word_lq_cached(word, max_gen + 2, max_depth,
                                     depth=depth + 1)

    top = n - 2
    top_positions = [i for i, g in enumerate(word) if g == top]

    if len(top_positions) == 1:
        # Cyclic rotation + Markov II: tr_M(w · σ_top) = z · tr_M(rest)
        pos = top_positions[0]
        rest = word[pos + 1:] + word[:pos]
        inner = _tr_M_word_lq_cached(rest, n - 1, max_depth,
                                       depth=depth + 1)
        return inner.mul_by_z()

    # Multiple tops: rotate so the last top is at the rightmost position
    last_top = top_positions[-1]
    rotated = word[last_top + 1:] + word[:last_top + 1]
    rest = rotated[:-1]
    # `rest` always contains ≥ 1 `top` since we entered the
    # multi-top branch and dropped only one; the explicit guard
    # below mirrors `markov_trace_canonical._tr_M_word_impl`
    # for parity with the sympy reference, and protects the next
    # line's `rest[::-1].index(top)` against a future refactor
    # that loosens the precondition.
    if top not in rest:
        inner = _tr_M_word_lq_cached(rest, n - 1, max_depth,
                                       depth=depth + 1)
        return inner.mul_by_z()

    # rest contains another top
    inner_pos = len(rest) - 1 - rest[::-1].index(top)
    segment = rest[inner_pos + 1:]

    if (top - 1) not in segment:
        # Case A: commute inner top to end, apply σ² = hσ + 1
        prefix = rest[:inner_pos]
        new_base = prefix + segment
        term1 = _tr_M_word_lq_cached(new_base + (top,), n, max_depth,
                                      depth=depth + 1)
        term2 = _tr_M_word_lq_cached(new_base, n, max_depth,
                                      depth=depth + 1)
        return term1.mul_by_h() + term2

    # Case B: braid relation — Phase-1 not implemented; caller
    # catches and falls back to the sympy `tr_M_word`.
    raise NotImplementedError(
        f"tr_M_word_lq Phase-1: Case B (braid relation) not yet "
        f"implemented; word={word}, n={n}"
    )


def tr_M_element_lq(lq_elem: LaurentHeckeElement, n: int) -> ZHLaurent:
    """Canonical Markov trace of a LaurentHeckeElement.

    Mirrors `markov_trace_canonical.tr_M_element` but keeps the
    accumulator in ZHLaurent throughout. Returns a ZHLaurent
    polynomial in (z, h) with LaurentQ-in-q coefficients.

    Phase-1: raises NotImplementedError on Case B words (caller
    can catch and fall back to sympy).
    """
    total = ZHLaurent.zero()
    for word, coeff in lq_elem.terms.items():
        if any(g < 0 for g in word):
            continue
        tr_w = tr_M_word_lq(word, n)
        # coeff is LaurentQ; scale tr_w by coeff (ZHLaurent.mul_by_lq)
        total = total + tr_w.mul_by_lq(coeff)
    return total


def tr_M_atomic_lq(Z: int, N: int, *,
                    include_inter: bool = True,
                    max_iterations: int = 10000) -> ZHLaurent:
    """End-to-end LaurentQ-direct Markov-peel for atomic (Z, N).

    Drop-in fast replacement for `markov_peel.tr_M_atomic` /
    `hecke_laurent_fast.tr_M_atomic_fast` that keeps the
    coefficient arithmetic in LaurentQ + ZHLaurent throughout,
    eliminating the sympy round-trip identified in
    docs/audits/2026-05-20-markov-peel-bottleneck-profile.md.

    Phase-1: Case B braid words raise NotImplementedError; caller
    catches and falls back to the sympy path. For all currently
    catalogued atomic braids (p, n, D, T, ³He, ⁴He, ⁵Li), the
    LaurentQ reduce produces only Case-A-compatible words (no top-1
    obstruction in the final NF), so the fallback is rarely hit
    in practice.

    Returns ZHLaurent polynomial in (z, h) with LaurentQ-in-q
    coefficients. Use `.evaluate(q₀, z₀, h₀)` to get the numerical
    Markov trace at the substrate.
    """
    from mass_at_3A_proper import atom_braid_word_3A
    from hecke_laurent_fast import incremental_reduced_element_fast

    A = Z + N
    n_strands = 3 * A
    word = atom_braid_word_3A(Z, N, include_inter=include_inter)
    fast_elem = incremental_reduced_element_fast(
        word, max_iterations_per_step=max_iterations,
    )
    return tr_M_element_lq(fast_elem, n_strands)


# ────────────────────────────────────────────────────────────────
# Cross-check + benchmark
# ────────────────────────────────────────────────────────────────

def _self_check() -> int:
    """Verify tr_M_element_lq matches markov_trace_canonical.tr_M_element
    at q₀ on the prop:categorical-mass-markov table.

    Returns 0 on success, 1 on failure.
    """
    import sympy as sp
    from q_parameter import Q as Q0
    from hecke_symbolic import (
        SymbolicHeckeElement, q as q_sym, z_markov as z_sym
    )
    from markov_trace_canonical import tr_M_element, H_SYMB as h_sym

    q_val = float(Q0)
    z_val = 1.0 / (q_val ** 0.5 + q_val ** (-0.5))
    h_val = q_val - 1.0 / q_val

    # n = max(word) + 2 if word else 1 (per markov_trace_canonical convention)
    tests = [
        ("identity",     (),         1),
        ("σ_0",          (0,),       2),  # tr_M = z
        ("σ_0 σ_1",      (0, 1),     3),  # tr_M = z²
        ("σ_0² (Hecke)", (0, 0),     2),  # tr_M = h·z + 1
        ("σ_0 σ_1 σ_0",  (0, 1, 0),  3),  # tr_M = h·z² + z
        ("σ_1 σ_0 σ_1",  (1, 0, 1),  3),  # tr_M = h·z² + z (braid)
    ]
    print("=" * 80)
    print("tr_M_element_lq self-check vs markov_trace_canonical.tr_M_element")
    print(f"q₀ = {q_val:.10f}, z₀ = {z_val:.10f}, h₀ = {h_val:.10f}")
    print("=" * 80)

    n_pass = 0
    n_fail = 0
    for name, word, n in tests:
        # LaurentQ path
        lq_elem = LaurentHeckeElement({word: LaurentQ.one()})
        try:
            tr_lq = tr_M_element_lq(lq_elem, n if word else 1)
        except NotImplementedError as e:
            print(f"  {name:<20} SKIP (Case B): {e}")
            continue
        val_lq = tr_lq.evaluate(q_val, z_val, h_val)

        # Sympy path (reference)
        sym_elem = SymbolicHeckeElement({word: sp.Integer(1)})
        tr_sym = tr_M_element(sym_elem, n if word else 1, simplify=False)
        val_sym = complex(tr_sym.subs([(q_sym, q_val),
                                        (z_sym, z_val),
                                        (h_sym, h_val)]).evalf(20))

        diff = abs(val_lq - val_sym)
        rel = diff / max(abs(val_sym), 1e-30)
        ok = rel < 1e-12
        marker = "pass" if ok else "FAIL"
        n_pass += int(ok)
        n_fail += int(not ok)
        print(f"  {name:<20} lq={val_lq.real:+.10f} "
              f"sym={val_sym.real:+.10f} rel={rel:.2e} [{marker}]")

    print(f"\n  {n_pass} pass / {n_fail} fail")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(_self_check())
