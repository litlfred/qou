#!/usr/bin/env python3
"""
nh_basis_shift.py — per-NF-letter shift accounting for NH_n basis braids.

The Iwahori–Hecke algebra H_n(q) has a Gröbner–Shirshov / canonical
normal-form (NF) basis indexed by the symmetric group S_n: one
basis element T_w per permutation w, where T_w = T_{s_{i_1}} ⋯
T_{s_{i_ℓ}} for any reduced word s_{i_1} ⋯ s_{i_ℓ} of w (independent
of the choice by the braid relations).

For each NF basis braid T_w we compute:

  • shift_full(T_w) := max_{λ ⊢ n} ord_{q=0}^{(-)} χ_λ(T_w)
        — direct seminormal pole order (compare to alpha_shift_torus.py).
  • shift_per_letter_naive(T_w) := length(w) · 1
        — one σ_i per generator, each contributing pole 1 at q=0
        (the upper bound from the cycle-additive DP probe).
  • gb_reduction_count(T_w) := length(w) − shift_full(T_w)
        — the number of "cancellations" that drop the actual pole
        below the per-letter upper bound.

The per-letter additive decomposition
    shift_full(T_w) = (per-letter upper bound) − (GB reduction count)
holds *by definition* of `gb_reduction_count` here; the witness
checks (i) `shift_full ≤ length(w)` always, (ii) `gb_reduction_count
≥ 0` always, and (iii) for the cyclic generators (σ_1 ⋯ σ_{n-1})^k
that arise in the torus-knot case, `shift_full = k(n-1)` matches
`alpha_shift_torus.py` exactly with `gb_reduction_count = 0`.

Test bench: every w ∈ S_n for n ∈ {2, 3, 4, 5} (1 + 2 + 6 + 24 + 120
= 153 basis braids).

Reuses the symbolic Hoefsmit machinery from alpha_shift_torus.py.

@module folio-assistant/computations/nh_basis_shift
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from itertools import permutations
from pathlib import Path
from typing import Dict, List, Tuple

import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from alpha_shift_torus import (  # noqa: E402
    build_seminormal_matrices_sym,
    pole_order_at_zero,
)
from hecke_characters import partitions_of  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


# ──────────────────────────────────────────────────────────────────────
# Reduced words for permutations in S_n (Matsumoto / lex-min convention)
# ──────────────────────────────────────────────────────────────────────

def perm_apply(word: List[int], n: int) -> Tuple[int, ...]:
    """Apply a word in adjacent transpositions s_i (1-indexed) to id ∈ S_n.
    Returns the resulting one-line permutation as a tuple."""
    p = list(range(1, n + 1))
    for s in word:
        p[s - 1], p[s] = p[s], p[s - 1]
    return tuple(p)


def lex_min_reduced_word(perm: Tuple[int, ...]) -> List[int]:
    """Return the lex-minimum reduced word (in s_1, …, s_{n-1}) for a
    permutation given as a one-line tuple (1-indexed). Uses bubble-sort
    from the right: scan for the first descent and apply s_i, recording
    i. Iterate until sorted; the recorded sequence (reversed) is a
    reduced word, and the right-greedy choice is lex-minimum among all
    reduced expressions."""
    n = len(perm)
    p = list(perm)
    word: List[int] = []
    while True:
        # Find first descent from the left
        i = None
        for k in range(n - 1):
            if p[k] > p[k + 1]:
                i = k
                break
        if i is None:
            break
        word.append(i + 1)  # s_{i+1} swaps positions i and i+1 (1-indexed)
        p[i], p[i + 1] = p[i + 1], p[i]
    # The recorded word *applied to id* gives perm⁻¹; the reduced word
    # for perm itself is the reverse.
    return list(reversed(word))


# ──────────────────────────────────────────────────────────────────────
# Per-irrep χ_λ(T_w) for an arbitrary reduced word
# ──────────────────────────────────────────────────────────────────────

def hecke_word_matrix(word: List[int], lam: Tuple[int, ...]) -> sp.Matrix:
    """Build ρ_λ(T_w) for w = s_{i_1} ⋯ s_{i_ℓ} as the matrix product
    σ_{i_1} σ_{i_2} ⋯ σ_{i_ℓ} in the seminormal basis."""
    sigmas, dim = build_seminormal_matrices_sym(lam)
    if dim == 0:
        return sp.zeros(1, 1)
    M = sp.eye(dim)
    for s in word:
        M = sigmas[s - 1] * M
    return M


def shift_full(word: List[int], n: int) -> Tuple[int, Tuple[int, ...]]:
    """Return (max_λ pole_order(χ_λ), maximizer λ) for the braid word w."""
    best = -1
    best_lam: Tuple[int, ...] = ()
    for lam in partitions_of(n):
        M = hecke_word_matrix(word, tuple(lam))
        chi = sp.cancel(M.trace())
        po = pole_order_at_zero(chi)
        if po > best:
            best = po
            best_lam = tuple(lam)
    return best, best_lam


# ──────────────────────────────────────────────────────────────────────
# Cyclic Coxeter element word — sanity check vs alpha_shift_torus
# ──────────────────────────────────────────────────────────────────────

def cyclic_coxeter_word(n: int, k: int) -> List[int]:
    """Word for (s_1 s_2 ⋯ s_{n-1})^k in S_n's Coxeter generators."""
    return [i for _ in range(k) for i in range(1, n)]


# ──────────────────────────────────────────────────────────────────────
# Witness build
# ──────────────────────────────────────────────────────────────────────

def main() -> None:
    w = WitnessBuilder("nh-basis-shift", engine="sympy")
    w.set_description(
        "Per-NF-letter shift accounting for the NH_n basis of H_n(q). "
        "For each w ∈ S_n (n ≤ 5) we compute the seminormal pole order "
        "at q = 0 of T_w, the naive per-letter upper bound (= ℓ(w)), and "
        "the GB-reduction count = ℓ(w) − pole_order. Validates the "
        "cycle-additive DP probe upper bound and cross-checks the "
        "torus-knot Coxeter element against alpha_shift_torus.py."
    )
    w.set_content_block("prop:alpha-shift-torus-knot")
    w.add_caveat(
        "The 'GB reduction count' is defined here as ℓ(w) − pole_order, "
        "i.e. the by-definition gap between the per-letter upper bound "
        "and the actual seminormal pole order. It does not correspond to "
        "an explicit GS reduction trace; the witness merely shows the "
        "gap is non-negative on every w ∈ S_n for n ∈ {2, 3, 4, 5}."
    )

    summary: Dict[str, Dict[str, object]] = {}
    print("=" * 78)
    print(" NH_n basis braids — shift accounting (n ≤ 5)")
    print("=" * 78)

    for n in [2, 3, 4, 5]:
        print(f"\n  n = {n}  ({len([0 for _ in permutations(range(1, n + 1))])} basis braids)")
        rows: List[Dict[str, object]] = []
        max_pole = 0
        max_pole_w: Tuple[int, ...] = ()
        max_pole_word: List[int] = []
        all_nonneg = True
        for perm in permutations(range(1, n + 1)):
            word = lex_min_reduced_word(perm)
            length = len(word)
            if length == 0:
                # identity — pole order 0 trivially
                pole, lam = 0, tuple([1] * n)
            else:
                pole, lam = shift_full(word, n)
            gb = length - pole
            if gb < 0:
                all_nonneg = False
            if pole > max_pole:
                max_pole = pole
                max_pole_w = perm
                max_pole_word = word
            rows.append({
                "perm": list(perm),
                "reduced_word": word,
                "length": length,
                "pole_order_q0": pole,
                "maximizer_lambda": list(lam),
                "gb_reduction_count": gb,
            })
        # Print top of table only for visibility
        rows_sorted = sorted(rows, key=lambda r: -int(r["pole_order_q0"]))[:5]
        for r in rows_sorted:
            print(
                f"    perm={r['perm']}, ℓ(w)={r['length']:>2}, "
                f"pole={r['pole_order_q0']:>2}, λ_max={r['maximizer_lambda']}, "
                f"gb={r['gb_reduction_count']:>2}"
            )
        # Cyclic Coxeter check (longest reduced word in S_n)
        cox_word = cyclic_coxeter_word(n, 1)
        cox_pole, cox_lam = shift_full(cox_word, n)
        print(
            f"    cyclic (s_1⋯s_{n-1})^1: ℓ={n - 1}, "
            f"pole={cox_pole}, λ={cox_lam}  (expected n-1 = {n - 1} on V_{{1^n}})"
        )

        summary[f"S_{n}"] = {
            "n": n,
            "num_basis_braids": len(rows),
            "max_pole_order": max_pole,
            "max_pole_perm": list(max_pole_w),
            "max_pole_reduced_word": max_pole_word,
            "all_gb_counts_nonneg": all_nonneg,
            "cyclic_coxeter_pole": int(cox_pole),
            "cyclic_coxeter_expected": n - 1,
            "rows": rows,
        }
        w.add_assertion(
            name=f"gb_count_nonneg_S_{n}",
            computed=int(all_nonneg),
            expected=1,
        )
        w.add_assertion(
            name=f"cyclic_coxeter_pole_S_{n}",
            computed=int(cox_pole),
            expected=int(n - 1),
        )

    # Sanity-check the (p, k) torus elements at p ∈ {2, 3} against
    # alpha_shift_torus.py expectations.
    torus_checks: List[Tuple[int, int, int]] = [(2, 3, 3), (2, 5, 5), (3, 4, 8)]
    for (p, k, expected) in torus_checks:
        word = cyclic_coxeter_word(p, k)
        pole, _ = shift_full(word, p)
        print(
            f"\n  (p, k) = ({p}, {k}): cyclic word length = {len(word)}, "
            f"pole = {pole} (expected k(p-1) = {expected})"
        )
        w.add_assertion(
            name=f"cyclic_coxeter_T_{p}_{k}_pole",
            computed=int(pole),
            expected=int(expected),
        )

    w.add_data("per_S_n", summary)
    w.add_data("torus_cross_checks", [list(t) for t in torus_checks])
    out = w.save()
    print(f"\nWitness written: {out}")
    print(f"All passed: {all(a.passed for a in w.assertions)}")


if __name__ == "__main__":
    main()
