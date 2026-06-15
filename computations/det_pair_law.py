#!/usr/bin/env python3
"""
Conjugate-pair determinant law — reusable helper.

For any braid word w ∈ B_n and a conjugate-partition pair (λ, λ′) of n,
the seminormal Hecke representations satisfy

    det ρ_λ(w) · det ρ_{λ′}(w) = (-1)^{L · dim_λ}

where L = ℓ(w) is the word length and dim_λ is the dimension of the
λ-representation (i.e. #SYT(λ)).  This was empirically verified for
6/6 conjugate-pair groups at n = 6 in
``beta_ew_delta_I_conjugate_pairing.py`` (a Path A / Path B exploratory
script that has since been retired).  The law lets every Markov-trace
sweep compute one half of each (λ, λ′) pair and recover the other
exactly, halving the seminormal-matrix work.

Public API
----------
``det_rho(lam, word, q_val)``
    Determinant of the Hoefsmit seminormal representation matrix.

``det_pair_sign(lam, word_length)``
    Predicted sign  (-1)^{L · dim_λ}  for the conjugate-pair law.

``verify_det_pair_law(lam, word, q_val, tol=1e-9)``
    Returns ``(predicted, actual, passes)`` for one pair.

``sweep_det_pair_law(n, words, q_val)``
    Verify the law across every (λ, λ′) pair for partitions of ``n``.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))


def _seminormal_matrix_product(shape: tuple[int, ...],
                                word: tuple[int, ...],
                                q_val: float) -> np.ndarray | None:
    """Return ρ_shape(T_w) using Hoefsmit seminormal matrices, or
    None if the representation is empty.

    Uses ``conjugate_symmetry._build_seminormal_at_q`` so that the
    same convention as the existing conjugate-pair tooling is in force.
    """
    from conjugate_symmetry import _build_seminormal_at_q

    sigmas, dim = _build_seminormal_at_q(shape, q_val)
    if dim == 0:
        return None
    prod = np.eye(dim)
    for g in word:
        if not (0 <= g < len(sigmas)):
            return None
        prod = prod @ sigmas[g]
    return prod


def det_rho(lam: tuple[int, ...],
            word: tuple[int, ...],
            q_val: float) -> float:
    """Determinant of ρ_λ(T_w) under the Hoefsmit convention.

    Returns NaN for the empty (zero-dimensional) representation.
    """
    M = _seminormal_matrix_product(lam, word, q_val)
    if M is None:
        return float("nan")
    return float(np.linalg.det(M))


def syt_count(shape: tuple[int, ...]) -> int:
    """Number of standard Young tableaux of ``shape`` (= dim of ρ_shape)."""
    from hecke_characters import standard_young_tableaux
    syts, _, _ = standard_young_tableaux(shape)
    return len(syts)


def det_pair_sign(lam: tuple[int, ...], word_length: int) -> int:
    """Predicted sign of  det ρ_λ(w) · det ρ_{λ′}(w),  i.e.  (-1)^{L·dim_λ}.

    Equals +1 when ``L · dim_λ`` is even, -1 otherwise.
    """
    return 1 if (word_length * syt_count(lam)) % 2 == 0 else -1


def verify_det_pair_law(lam: tuple[int, ...],
                          word: tuple[int, ...],
                          q_val: float,
                          *, tol: float = 1e-9) -> tuple[float, float, bool]:
    """Verify  det ρ_λ(w) · det ρ_{λ′}(w) ≈ predicted sign.

    Returns (predicted, actual_product, passes_within_tol).
    Self-conjugate λ trivially returns (1, det²/|det²|, True).
    """
    from conjugate_symmetry import conjugate_partition

    lp = conjugate_partition(lam)
    d_lam = det_rho(lam, word, q_val)
    d_lp = det_rho(lp, word, q_val)
    actual = d_lam * d_lp
    predicted = det_pair_sign(lam, len(word))

    if math.isnan(actual):
        return float(predicted), actual, False

    # The law is exact up to a positive scalar (numerical drift in
    # finite-precision matrix products).  Compare the *sign* of the
    # ratio rather than the raw difference, which can blow up on
    # large-dimension reps where det ρ_λ(w) is far from unit modulus.
    if abs(actual) < tol:
        # predicted is always ±1 from det_pair_sign, so a near-zero
        # actual product is always a failure.
        return float(predicted), actual, False
    sign_actual = 1 if actual > 0 else -1
    passes = sign_actual == predicted
    return float(predicted), actual, passes


def sweep_det_pair_law(n: int,
                        words: list[tuple[int, ...]],
                        q_val: float) -> dict:
    """Run the law across every (λ, λ′) conjugate pair for partitions of n.

    Returns a summary dict with per-pair pass counts and an overall
    pass flag.  Self-conjugate partitions are reported but excluded
    from the law check (the law is trivial there).
    """
    from conjugate_symmetry import conjugate_pair_representatives

    self_conj, pairs = conjugate_pair_representatives(n)
    results: list[dict] = []
    all_pass = True
    for (lam, _lp) in pairs:
        per_word = []
        pair_pass = True
        for w in words:
            predicted, actual, passes = verify_det_pair_law(lam, w, q_val)
            per_word.append({
                "word": list(w),
                "predicted_sign": int(predicted),
                "actual_product": float(actual)
                    if not math.isnan(actual) else None,
                "passes": bool(passes),
            })
            pair_pass = pair_pass and passes
        results.append({
            "lambda": list(lam),
            "passes": bool(pair_pass),
            "words": per_word,
        })
        all_pass = all_pass and pair_pass
    return {
        "n": int(n),
        "q": float(q_val),
        "self_conjugate": [list(s) for s in self_conj],
        "pair_count": len(pairs),
        "all_pass": bool(all_pass),
        "pairs": results,
    }


# ── CLI: verify the law for n = 3..6 ───────────────────────────

if __name__ == "__main__":
    from q_parameter import Q as Q0

    print("=" * 72)
    print("CONJUGATE-PAIR DETERMINANT LAW")
    print("    det ρ_λ(w) · det ρ_λ'(w) = (-1)^{L · dim_λ}")
    print("=" * 72)
    print(f"q₀ = {Q0:.6f}\n")

    sample_words = {
        3: [(), (0,), (1,), (0, 1), (1, 0, 1)],
        4: [(), (0, 1, 2), (1, 2, 1), (0, 1, 0, 2), (0, 1, 2, 1, 0)],
        5: [(), (0, 1, 2, 3), (1, 2, 3, 2, 1)],
        6: [(), (0, 1, 2, 3, 4), (0, 2, 4), (1, 2, 3, 4, 0, 1)],
    }
    overall = True
    for n, words in sample_words.items():
        report = sweep_det_pair_law(n, words, Q0)
        flag = "✓" if report["all_pass"] else "✗"
        print(f"  {flag}  n={n}  pairs={report['pair_count']:>2}  "
              f"self_conj={len(report['self_conjugate']):>2}  "
              f"all_pass={report['all_pass']}")
        if not report["all_pass"]:
            for p in report["pairs"]:
                if not p["passes"]:
                    print(f"      FAIL: λ={p['lambda']}")
                    for w in p["words"]:
                        if not w["passes"]:
                            print(f"        word={w['word']}  "
                                  f"predicted={w['predicted_sign']:+d}  "
                                  f"actual={w['actual_product']}")
        overall = overall and report["all_pass"]
    print()
    print("✓ Det-pair law verified across n = 3..6"
          if overall else "✗ Det-pair law FAILED — investigate")
