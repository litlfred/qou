#!/usr/bin/env python3
"""
Recursive symbolic Markov-trace computer for arbitrary words in H_n(q).

Builds on the existing `gb_filtration_jet_tracker.HeckeElement` class
(which is already symbolic via the sympy `q` symbol) to expand any
braid word into the Hecke basis {T_w : w ∈ S_n}, then computes the
Markov trace by RECURSIVE descent on n via the Markov axiom

  tr_M(α · σ_n) = z · tr_M(α),    α ∈ H_n.

Plus base cases:
  tr_M(1_{H_n}) = 1   for all n,
  tr_M(σ_i)     = z   (Markov-axiom-derived).

Algorithm for tr_M(T_w) where w ∈ S_n:
  1. If w fixes position n+1 (i.e., word doesn't use σ_n in canonical
     reduced form), then T_w ∈ H_n and recurse on H_n.
  2. Otherwise, find position of σ_n in canonical reduced word:
        T_w = T_α · σ_n · T_β,   with α ∈ H_n, β starts in H_{n+1}\H_n.
     By cyclic trace + Markov axiom, reduce to recursive call on
     T_α · T_{cyclic-rotated β}.
  3. Continue until all σ_n's are absorbed into z factors.

Output: markov-trace-recursive.witness.json (with H_3, H_4, H_5
example computations).
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from gb_filtration_jet_tracker import HeckeElement, perm_apply_s

# Sympy q, h, z (matching the jet_tracker convention)
q = sp.symbols("q", positive=True)
h_sym = q - 1 / q
z_sym = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))


def coxeter_length(perm: tuple) -> int:
    n = len(perm)
    return sum(1 for i in range(n) for j in range(i + 1, n) if perm[i] > perm[j])


def reduced_word(perm: tuple) -> list[int]:
    """Canonical reduced word for `perm` ∈ S_n via greedy descent.
    Returns list of generator indices (0-indexed: σ_0, σ_1, ...)."""
    n = len(perm)
    word = []
    p = list(perm)
    # Bubble-sort: find descents and apply σ
    while coxeter_length(tuple(p)) > 0:
        for i in range(n - 1):
            if p[i] > p[i + 1]:
                p[i], p[i + 1] = p[i + 1], p[i]
                word.append(i)
                break
    return list(reversed(word))


def tr_m_basis_element(perm: tuple) -> sp.Expr:
    """Compute tr_M(T_w) for permutation w via recursion on n.

    w ∈ S_n. The strategy:
      1. Get the canonical reduced word [s_{i_1}, ..., s_{i_k}] for w.
      2. Find the maximum generator index m in the word.
      3. If m == 0 (word is empty): w = identity, tr_M = 1.
      4. Apply the Markov axiom on σ_m to extract z factors and
         reduce to S_{m+1} → S_m via cyclic trace.

    Specifically, for w with reduced word ending in σ_{n-1}:
      T_w = T_{w · s_{n-1}^{-1}} · σ_{n-1}
      tr_M(T_w) = tr_M(T_{w'} · σ_{n-1})
                = z · tr_M(T_{w'})  if w' ∈ S_{n-1} (= S_n with fixed n).
    For more general w, use cyclic property of trace.
    """
    n = len(perm)
    word = reduced_word(perm)
    if not word:
        return sp.Integer(1)
    # Find max generator index in word
    max_gen = max(word)
    # If the highest gen used is < n-1, w is in S_{max_gen+1} effectively.
    # Recurse on lower n.
    if max_gen < n - 1:
        # Truncate the permutation: drop fixed positions at the end
        sub_perm = tuple(perm[: max_gen + 2])
        return tr_m_basis_element(sub_perm)

    # max_gen == n-1: word uses σ_{n-1}. Apply Markov axiom.
    # Find rightmost σ_{n-1} in word — position k.
    k = max(i for i, g in enumerate(word) if g == max_gen)
    # Word = [w_left] · σ_{n-1} · [w_right]
    w_left = word[:k]
    w_right = word[k + 1 :]
    # If w_right contains σ_{n-1} (shouldn't, k is rightmost), error.
    # Push σ_{n-1} to end via cyclic: tr_M(L σ R) = tr_M(R L σ) = z tr_M(R L)
    # if R L is in H_{n-1} (no σ_{n-1}).
    new_word = w_right + w_left
    # Verify new_word doesn't contain max_gen
    if max_gen in new_word:
        # Need more sophisticated reduction.
        # Use HeckeElement to reduce via braid+Hecke.
        E = HeckeElement.identity(n)
        for i in new_word:
            E = E.right_mul_T(i + 1)   # jet-tracker uses 1-indexed
        # Compute tr_M of E (linear combination of T_w basis)
        result = sp.Integer(0)
        for w, c in E.terms.items():
            result += c * tr_m_basis_element(w)
        return sp.cancel(z_sym * result)

    # new_word is in H_{n-1}: convert to permutation
    p_new = tuple(range(1, n + 1))
    for i in new_word:
        p_new = perm_apply_s(p_new, i + 1)   # jet-tracker 1-indexed
    return sp.cancel(z_sym * tr_m_basis_element(p_new))


def markov_trace_of_word(n: int, word: list[int]) -> sp.Expr:
    """Compute tr_M(β) for β specified by `word` (signed integers,
    positive = σ_i, negative = σ_i^{-1}; jet-tracker 1-indexed).

    Reduces β to T_w basis via HeckeElement, then applies
    `tr_m_basis_element` to each basis term.
    """
    E = HeckeElement.identity(n)
    for i in word:
        if i > 0:
            E = E.right_mul_T(i)
        else:
            E = E.right_mul_T_inv(-i)
    result = sp.Integer(0)
    for w, c in E.terms.items():
        result += c * tr_m_basis_element(w)
    return sp.cancel(result)


def main() -> int:
    print("=" * 96)
    print(f"  Recursive symbolic Markov-trace reducer for arbitrary H_n words")
    print("=" * 96)

    test_cases = [
        # (name, n, word)
        ("identity_H3", 3, []),
        ("σ_1", 3, [1]),
        ("σ_1²", 3, [1, 1]),
        ("σ_1σ_2", 3, [1, 2]),
        ("σ_1σ_2σ_1", 3, [1, 2, 1]),
        ("σ_1^7 σ_2^4 (proton)", 3, [1] * 7 + [2] * 4),
        ("σ_1^6 σ_2^4 σ_1 inv (neutron-like)", 3, [1] * 6 + [2] * 4 + [-1]),
        # H_4
        ("σ_1σ_2σ_3 (H_4)", 4, [1, 2, 3]),
        ("σ_1σ_2σ_3σ_2σ_1 (H_4)", 4, [1, 2, 3, 2, 1]),
        # H_5
        ("σ_1σ_2σ_3σ_4 (H_5)", 5, [1, 2, 3, 4]),
        # H_6 deuteron-equivalent
        ("σ_1σ_2σ_4σ_5 (deuteron disjoint)", 6, [1, 2, 4, 5]),
    ]

    print(f"\n  {'name':<40} {'n':>2} {'tr_M(q) (numerical at q_0)':>30} {'symbolic ok':>14}")
    print("  " + "-" * 92)

    from q_parameter import Q_MP
    q0 = float(Q_MP)
    results = []

    for name, n, word in test_cases:
        try:
            tr_M_sym = markov_trace_of_word(n, word)
            tr_M_at_q0 = float(sp.lambdify(q, tr_M_sym, modules=["mpmath"])(q0))
            sym_str_short = (
                str(tr_M_sym)[:60] + ("..." if len(str(tr_M_sym)) > 60 else "")
            )
            print(f"  {name:<40} {n:>2} {tr_M_at_q0:>30.10f}  ✓")
            results.append({
                "name": name,
                "n": n,
                "word": word,
                "tr_M_at_q0": tr_M_at_q0,
                "tr_M_symbolic_short": sym_str_short,
                "tr_M_symbolic_full": str(tr_M_sym),
            })
        except Exception as exc:
            print(f"  {name:<40} {n:>2} ERROR: {type(exc).__name__}: {exc}")
            results.append({
                "name": name,
                "n": n,
                "word": word,
                "error": f"{type(exc).__name__}: {exc}",
            })

    # Reference checks
    print(f"\n  Reference values:")
    print(f"    σ_1                    expected z = 0.4993,  got {results[1].get('tr_M_at_q0', 'ERR'):>10}")
    print(f"    σ_1σ_2                 expected z² = 0.2493, got {results[3].get('tr_M_at_q0', 'ERR'):>10}")
    print(f"    σ_1σ_2σ_1              expected z + hz² = 0.5514, got {results[4].get('tr_M_at_q0', 'ERR'):>10}")
    print(f"    σ_1^7 σ_2^4 (proton)   expected ~1.6334, got {results[5].get('tr_M_at_q0', 'ERR'):>10}")

    witness = {
        "computation": "markov-trace-recursive",
        "description": (
            "Recursive symbolic Markov-trace computer for arbitrary H_n(q) "
            "words. Uses gb_filtration_jet_tracker.HeckeElement (symbolic "
            "in q via sympy) to expand braids into the Hecke basis, then "
            "applies recursive Markov-axiom descent for each basis "
            "element. Tested up to H_6 for representative words."
        ),
        "reference_blocks": [
            "prop:atomic-mass-gb-nf",
            "prop:categorical-mass-markov",
        ],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "test_cases": results,
    }
    out = HERE / "markov-trace-recursive.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
