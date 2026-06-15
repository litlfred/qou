#!/usr/bin/env python3
"""
Conjugate-partition symmetry for Hecke characters.

In the symmetric-convention Iwahori-Hecke algebra H_n(q) (generator
eigenvalues q and -q^{-1}), the irreducible representations indexed
by λ and its conjugate λ' are related by a sign twist.  This lets
us derive χ^{λ'}(T_w) from χ^λ(T_w), halving the character-
evaluation cost in Ocneanu-weight inversion.

The formula candidates (test empirically — Ram 1991 vs Macdonald
I.5 Ex. 23 use slightly different conventions):

  (A) Macdonald / "standard":
      χ^{λ'}(T_w) = (-1)^{ℓ(w)} · χ^λ(T_w) |_{q → q^{-1}}

  (B) Ram 1991 (Hoefsmit convention):
      χ^{λ'}(T_w) = χ^λ(T_w) |_{q → -q^{-1}}   [equivalent to A up to a global sign]

  (C) User's guess — combined q-inversion and word-length twist:
      χ^{λ'}(T_w) = χ^λ(T_w) |_{q → -q^{-1}} · (-q)^{-2 ℓ(w)}

The unit test `test_conjugate_character_formula` selects whichever
formula holds for the hecke_characters.build_seminormal_matrices
convention at multiple (n, w) test points.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))


def conjugate_partition(lam: tuple[int, ...]) -> tuple[int, ...]:
    """Conjugate (transpose) of a partition.  (3, 2, 1) → (3, 2, 1);
    (4, 1) → (2, 1, 1, 1)."""
    if not lam:
        return ()
    rows = list(lam)
    max_col = rows[0]
    return tuple(sum(1 for r in rows if r > j) for j in range(max_col))


def is_self_conjugate(lam: tuple[int, ...]) -> bool:
    return conjugate_partition(lam) == tuple(lam)


def conjugate_pair_representatives(n: int) -> tuple[
        list[tuple[int, ...]], list[tuple[tuple[int, ...], tuple[int, ...]]]]:
    """Split partitions of n into self-conjugate + (λ, λ') pairs.

    Returns (self_conj, pairs) where ``pairs`` lists each pair exactly
    once with the lex-smaller representative first.
    """
    from hecke_characters import partitions_of
    seen = set()
    self_conj = []
    pairs = []
    for lam in partitions_of(n):
        lam = tuple(lam)
        if lam in seen:
            continue
        lp = conjugate_partition(lam)
        if lp == lam:
            self_conj.append(lam)
            seen.add(lam)
        else:
            rep = min(lam, lp)
            other = max(lam, lp)
            pairs.append((rep, other))
            seen.add(lam)
            seen.add(lp)
    return self_conj, pairs


# ── Convention detector (empirical) ─────────────────────────

def _eval_chi_direct(shape: tuple[int, ...], word: tuple[int, ...],
                       q_val: float) -> float:
    """Evaluate χ^λ(T_w) directly via Hoefsmit seminormal matrices."""
    import numpy as np
    # F6 (PR follow-up #582): numerical-q Hoefsmit through BlockCache.
    # Per Gemini review on #583: use the *provided* q_val (not the
    # global q_0) so detect_conjugate_formula's convention-detection
    # loop sees the correct cache. h = q − q⁻¹ is derived from q_val.
    from syt_prefix_cache import BlockCache, build_seminormal_matrices_cached
    h_val = q_val - 1.0 / q_val
    cache = BlockCache(q_val, h_val)
    sigmas, dim, _ = build_seminormal_matrices_cached(shape, cache=cache)
    if dim == 0:
        return 0.0
    try:
        from scipy.sparse import issparse, eye as speye
        is_sparse = issparse(sigmas[0]) if sigmas else False
    except ImportError:
        is_sparse = False
    if is_sparse:
        prod = speye(dim, format="csr")
    else:
        prod = np.eye(dim)
    for g in word:
        if 0 <= g < len(sigmas):
            prod = prod @ sigmas[g]
        else:
            return float("nan")
    if is_sparse:
        return float(prod.diagonal().sum())
    return float(np.trace(prod))


def _build_seminormal_at_q(shape: tuple[int, ...], q_alt: float):
    """Build Hoefsmit matrices using an alternate q value.

    Returns (sigmas, dim).  Mirrors hecke_characters.build_seminormal_matrices
    but parameterises q so we can evaluate at q → -q^{-1} etc.
    """
    import math
    import numpy as np
    from hecke_characters import standard_young_tableaux

    syts, cells, contents = standard_young_tableaux(shape)
    dim = len(syts)
    if dim == 0:
        return [], 0
    n = sum(shape)
    h_alt = q_alt - 1.0 / q_alt
    sigmas = []
    for k in range(1, n):
        mat = np.zeros((dim, dim))
        done = set()
        for i in range(dim):
            if i in done:
                continue
            ci_k = syts[i][k]
            ci_k1 = syts[i][k + 1]
            rho = contents[ci_k1] - contents[ci_k]
            denom_a = 1.0 - q_alt ** (-2 * rho)
            if abs(denom_a) < 1e-15:
                a = 0.0
            else:
                a = h_alt / denom_a
            swap = dict(syts[i])
            swap[k] = ci_k1
            swap[k + 1] = ci_k
            j = None
            for jj in range(dim):
                if jj == i:
                    continue
                if syts[jj] == swap:
                    j = jj
                    break
            if j is None:
                mat[i, i] = a
                done.add(i)
            else:
                denom_ap = 1.0 - q_alt ** (2 * rho)
                if abs(denom_ap) < 1e-15:
                    a_prime = 0.0
                else:
                    a_prime = h_alt / denom_ap
                b_sq = a * a_prime + 1.0
                b = math.sqrt(abs(b_sq))
                mat[i, i] = a
                mat[j, j] = a_prime
                mat[i, j] = b
                mat[j, i] = b
                done.add(i)
                done.add(j)
        sigmas.append(mat)
    return sigmas, dim


def _chi_at_q(shape: tuple[int, ...], word: tuple[int, ...],
               q_val: float) -> float:
    """Evaluate χ^λ(T_w) with an arbitrary q (possibly negative)."""
    import numpy as np
    sigmas, dim = _build_seminormal_at_q(shape, q_val)
    if dim == 0:
        return 0.0
    prod = np.eye(dim)
    for g in word:
        prod = prod @ sigmas[g]
    return float(np.trace(prod))


def detect_conjugate_formula(test_cases: list[tuple[
        tuple[int, ...], tuple[int, ...], float]],
        tol: float = 1e-9,
        verbose: bool = False) -> str | None:
    """Identify which conjugation formula holds for our Hoefsmit build.

    Tries candidates (A), (B), (C) at each test case and returns the
    one that matches χ^{λ'}(T_w) directly at every point.  Returns
    None if no candidate fits (indicates a different convention we
    haven't enumerated).
    """
    candidates = {
        "A_q_inv_times_sign": lambda chi, q, lw: (
            ((-1) ** lw) * _chi_at_q_inverse(chi)),
        "B_q_neg_inv": lambda chi, q, lw: chi,  # see _chi_B below
        "C_q_neg_inv_times_power": lambda chi, q, lw: chi * (-q) ** (-2 * lw),
    }
    # We can't build candidate values from chi directly (it's a scalar),
    # we must re-evaluate the conjugate partition via the substituted q.
    # So we actually compute χ^{λ'}(T_w) via _chi_at_q for the substituted
    # q and compare to χ^{λ'}(T_w) at original q.
    votes = {name: 0 for name in
             ["A_q_inv_sign", "B_q_neg_inv", "C_q_neg_inv_times_power"]}
    total = 0
    for (lam, word, q_val) in test_cases:
        lp = conjugate_partition(lam)
        chi_lp_direct = _eval_chi_direct(lp, word, q_val)
        lw = len(word)
        # (A): χ^{λ'}(T_w) = (-1)^{ℓ(w)} · χ^λ(T_w) |_{q → q^{-1}}
        chi_A = ((-1) ** lw) * _chi_at_q(lam, word, 1.0 / q_val)
        # (B): χ^{λ'}(T_w) = χ^λ(T_w) |_{q → -q^{-1}}
        chi_B = _chi_at_q(lam, word, -1.0 / q_val)
        # (C): above but multiplied by (-q)^{-2 ℓ(w)}
        chi_C = _chi_at_q(lam, word, -1.0 / q_val) * (-q_val) ** (-2 * lw)
        if verbose:
            print(f"λ={lam}  w={word}  "
                  f"χ^λ'(direct)={chi_lp_direct:+.6f}  "
                  f"A={chi_A:+.6f}  B={chi_B:+.6f}  C={chi_C:+.6f}")
        for name, val in [("A_q_inv_sign", chi_A),
                          ("B_q_neg_inv", chi_B),
                          ("C_q_neg_inv_times_power", chi_C)]:
            if abs(val - chi_lp_direct) < tol:
                votes[name] += 1
        total += 1
    # Choose any formula matching ALL cases
    for name, v in votes.items():
        if v == total:
            return name
    return None


def _chi_at_q_inverse(chi):
    """Placeholder for compatibility — not used externally."""
    return chi


# ── Fast conjugate-character evaluator ──────────────────────

def conjugate_character_value(lam: tuple[int, ...],
                                 word: tuple[int, ...],
                                 q_val: float,
                                 *, formula: str) -> float:
    """Compute χ^{λ'}(T_w) from λ via the detected formula.

    ``formula`` must be one of the keys returned by
    ``detect_conjugate_formula`` (run that once per session to
    calibrate).  Evaluates via alternate-q seminormal without
    building the λ' matrices.
    """
    lw = len(word)
    if formula == "A_q_inv_sign":
        return ((-1) ** lw) * _chi_at_q(lam, word, 1.0 / q_val)
    if formula == "B_q_neg_inv":
        return _chi_at_q(lam, word, -1.0 / q_val)
    if formula == "C_q_neg_inv_times_power":
        return _chi_at_q(lam, word, -1.0 / q_val) * (-q_val) ** (-2 * lw)
    raise ValueError(f"Unknown conjugation formula: {formula}")


# ── CLI: run the convention detector ────────────────────────

if __name__ == "__main__":
    from q_parameter import Q as Q0
    from hecke_characters import partitions_of

    print("=" * 80)
    print("CONJUGATE-CHARACTER FORMULA DETECTOR")
    print("Tests Hoefsmit-convention χ^{λ'}(T_w) against 3 candidate formulas.")
    print(f"q₀ = {Q0:.6f}")
    print("=" * 80)

    # Build test cases: pick several (λ, word) combinations per n
    test_words_by_n = {
        4: [(), (0,), (1,), (0, 1), (1, 2, 1), (0, 1, 2, 1)],
        5: [(0, 2), (0, 1, 2, 3), (1, 2, 3, 0, 1)],
        6: [(0, 1, 2), (0, 2, 4), (1, 2, 3, 4), (0, 1, 0, 2, 1)],
    }

    all_cases = []
    for n, words in test_words_by_n.items():
        for lam in partitions_of(n):
            lam = tuple(lam)
            if is_self_conjugate(lam):
                continue
            for w in words:
                all_cases.append((lam, w, Q0))
    print(f"\nBuilt {len(all_cases)} test cases "
          f"(non-self-conjugate λ × sample words).")

    # Visual check on a handful
    print("\nSample evaluations (first 6):")
    detect_conjugate_formula(all_cases[:6], verbose=True)

    print("\nFull detection across all cases:")
    winner = detect_conjugate_formula(all_cases, tol=1e-9, verbose=False)
    if winner is None:
        print("  ✗ No candidate formula matches at all test points.")
        print("  Further investigation needed — convention may be different.")
    else:
        print(f"  ✓ Formula matching all {len(all_cases)} cases: {winner}")

    # Self-conjugate invariance check
    print("\nSelf-conjugate partitions (χ^{λ'} = χ^λ trivially):")
    for n in [4, 5, 6]:
        for lam in partitions_of(n):
            lam = tuple(lam)
            if is_self_conjugate(lam):
                print(f"  n={n}: {lam}")
