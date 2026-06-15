#!/usr/bin/env python3
"""Cross-engine regression test for ``SymbolicHeckeDivision.reduce``.

Verifies that ``engine='sympy'``, ``engine='laurent'``, and
``engine='crystal'`` produce **algebraically-equal NF coefficients**
(``sp.simplify(c_a − c_b) == 0`` term-by-term) on a battery of small
Hecke elements.  This is a semantic-equality check, not a string /
canonical-form comparison: ``(q²−1)/q`` and ``q − 1/q`` are accepted
as equal even though their printed forms differ.

This is the regression gate for Phase 1 of the S-poly → crystal-basis
migration: every script we migrate to ``engine='laurent'`` must pass
this test on inputs equivalent to its hot-path call.

Run:  python3 test_engine_equivalence.py
"""
from __future__ import annotations

import sys
import sympy as sp

from hecke_symbolic import (
    SymbolicHeckeDivision, SymbolicHeckeElement, q,
)


def _normalize_terms(elem: SymbolicHeckeElement) -> dict:
    """Return a canonical-form dict of ``{word: simplified sympy expr}``.
    Uses ``sp.together`` + ``sp.cancel`` so that
    ``(q**2 - 1)/q``  and  ``q - 1/q``  compare equal.
    """
    out = {}
    for w, c in elem.terms.items():
        c_norm = sp.cancel(sp.together(c))
        if c_norm != 0:
            out[w] = c_norm
    return out


def _assert_equal(a: SymbolicHeckeElement, b: SymbolicHeckeElement,
                   label: str) -> None:
    A = _normalize_terms(a)
    B = _normalize_terms(b)
    keys = set(A) | set(B)
    diffs = []
    for k in keys:
        ca = A.get(k, sp.Integer(0))
        cb = B.get(k, sp.Integer(0))
        if sp.simplify(ca - cb) != 0:
            diffs.append((k, ca, cb))
    if diffs:
        print(f"  ✗ {label}: {len(diffs)} term(s) differ")
        for k, ca, cb in diffs[:3]:
            print(f"      word {k}: sympy={ca}  vs  other={cb}")
        sys.exit(1)


def main() -> int:
    div = SymbolicHeckeDivision()
    print("=" * 72)
    print("ENGINE EQUIVALENCE TEST — sympy / laurent / crystal")
    print("=" * 72)

    # ── Case 1: σ_0² (Hecke relation, 2 strands) ────────────────────
    elem = SymbolicHeckeElement({(0, 0): sp.Integer(1)})
    e_sympy, _ = div.reduce(elem, engine='sympy')
    e_laurent, _ = div.reduce(elem, engine='laurent')
    e_crystal, _ = div.reduce(elem, engine='crystal')
    _assert_equal(e_sympy, e_laurent, "σ_0²:  sympy ≡ laurent")
    _assert_equal(e_sympy, e_crystal, "σ_0²:  sympy ≡ crystal")
    print(f"  ✓ σ_0² → {len(e_sympy.terms)} terms (all engines agree)")

    # ── Case 2: σ_0σ_1σ_0 (YB rewrite, 3 strands) ──────────────────
    elem = SymbolicHeckeElement({(0, 1, 0): sp.Integer(1)})
    e_sympy, _ = div.reduce(elem, engine='sympy')
    e_laurent, _ = div.reduce(elem, engine='laurent')
    e_crystal, _ = div.reduce(elem, engine='crystal')
    _assert_equal(e_sympy, e_laurent, "σ_0σ_1σ_0:  sympy ≡ laurent")
    _assert_equal(e_sympy, e_crystal, "σ_0σ_1σ_0:  sympy ≡ crystal")
    print(f"  ✓ σ_0σ_1σ_0 → {len(e_sympy.terms)} terms (all engines agree)")

    # ── Case 3: protium-style 4-strand element ─────────────────────
    elem = SymbolicHeckeElement.identity()
    types = ['u', 'u', 'd', 'e']
    for k in range(1, 4):
        for i in range(k):
            cx = div.crossing(types[i], types[k], i)
            elem = elem * cx
    e_sympy, _ = div.reduce(elem, engine='sympy')
    e_laurent, _ = div.reduce(elem, engine='laurent')
    e_crystal, _ = div.reduce(elem, engine='crystal')
    _assert_equal(e_sympy, e_laurent, "protium:  sympy ≡ laurent")
    _assert_equal(e_sympy, e_crystal, "protium:  sympy ≡ crystal")
    print(f"  ✓ protium 4-strand → {len(e_sympy.terms)} terms "
          f"(all engines agree)")

    # ── Case 4: 5-strand element with σ_3 (engine='crystal' boundary)─
    elem = SymbolicHeckeElement({(0, 1, 2, 3, 2, 1, 0): sp.Integer(1)})
    e_sympy, _ = div.reduce(elem, engine='sympy')
    e_laurent, _ = div.reduce(elem, engine='laurent')
    _assert_equal(e_sympy, e_laurent, "5-strand:  sympy ≡ laurent")
    # crystal engine should refuse this — n=5 strands > 4 cap.
    try:
        div.reduce(elem, engine='crystal')
        print("  ✗ engine='crystal' accepted 5-strand input — guard "
              "missing")
        return 1
    except NotImplementedError as exc:
        if "≤ 4 strands" not in str(exc):
            print(f"  ✗ unexpected NotImplementedError: {exc}")
            return 1
    print(f"  ✓ 5-strand σ_3-bearing → laurent ≡ sympy "
          f"({len(e_sympy.terms)} terms); crystal correctly refused")

    # ── Case 5: env-var override ───────────────────────────────────
    import os
    os.environ["QOU_REDUCE_ENGINE"] = "laurent"
    elem = SymbolicHeckeElement({(0, 0): sp.Integer(1)})
    e_env, stats_env = div.reduce(elem)
    if stats_env.get('engine') != 'laurent':
        print(f"  ✗ QOU_REDUCE_ENGINE=laurent did not route through "
              f"laurent (engine={stats_env.get('engine')!r})")
        return 1
    print("  ✓ QOU_REDUCE_ENGINE env-var override works")
    del os.environ["QOU_REDUCE_ENGINE"]

    print("\n  ✓ All engine-equivalence regressions passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
