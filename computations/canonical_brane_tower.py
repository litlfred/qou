"""Canonical T_2 / T_3 brane-tower replacement — Markov-trace form.

Per `prop:mass-endomorphism-tower §Algebraic form`, T_2 / T_3 should
NOT use the archimedean Φ_q(|V̂_i|) specialisation (which the paper
flags as PATHOLOGICAL: Φ_q(0.99) ≈ 6.7e5, amplifies tiny p/n
asymmetries by ~10^5×, predicts T-³He ≈ -737 MeV vs CODATA +0.019 MeV).

The canonical form uses `Vol_q^(S)(β)` = Markov trace over the
transfer-matrix chain supported on subset S of generators:

  T_2 = Σ_i z · Vol_q^({i})(β)       (single-gen)
  T_3 = z² Σ_{i<j} Vol_q^({i, j})(β) (pair-gen)

Each Vol_q^(S) is a Laurent polynomial in q^(1/2) — Markov-invariant
by construction (different reduced words give the same Markov trace).

## Implementation

For a canonical atom braid word `word = [(c, d, gen), ...]`:

- Single-gen sub-word at i: `[(c, d, gen) for (c, d, gen) in word if gen == i]`
- Pair-gen sub-word at {i, j}: `[(c, d, gen) for (c, d, gen) in word if gen in {i, j}]`

Markov trace of each sub-word via the existing
`markov_trace_canonical.tr_M_word` machinery (cached, Markov-axiom
recursive reducer).
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from hecke_core import h as H_VAL, z as Z_MARK  # noqa: E402
from mass_at_3A_proper import chi_lambda_of_word  # noqa: E402
from hecke_characters import build_seminormal_matrices  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402


def vol_q_S(word: list, S: set[int], n_total_gens: int,
            q_val: float) -> mp.mpf:
    """Markov trace Vol_q^(S)(β) of the sub-word supported on S.

    Per `prop:mass-endomorphism-tower §Algebraic form`, this is the
    canonical Markov-invariant form of the per-subset volume — a
    Laurent polynomial in q^(1/2) by construction.

    Computed via Σ_λ y_λ(q) · χ^λ_q(sub_word) over partitions of
    the sub-strand-count n_sub = |S| + 1 — the same per-irrep
    Hoefsmit machinery used for T_1 (F1 ⁴He probe / V2 chirality).
    """
    # Extract sub-word in original order, remapping generator indices
    # to 0..|S|-1 so the result lives in H_{|S|+1}(q).
    sub = [(c, d, gen) for (c, d, gen) in word if gen in S]
    if not sub:
        return mp.mpf(0)

    sorted_S = sorted(S)
    gen_remap = {g: i for i, g in enumerate(sorted_S)}
    sub_remapped = [(c, d, gen_remap[gen]) for (c, d, gen) in sub]
    n_sub_strands = len(sorted_S) + 1     # |S| generators → |S|+1 strands
    n_sub_gens = len(sorted_S)            # n_sub_strands - 1

    y_vals = y_lambda_at(n_sub_strands, q_val=q_val)
    total = mp.mpf(0)
    for shape, y in y_vals.items():
        sigmas, dim, _ = build_seminormal_matrices(shape, q=q_val)
        if dim == 0:
            continue
        chi = chi_lambda_of_word(sigmas, dim, sub_remapped, n_sub_gens)
        # NOTE: chi is float64 (chi_lambda_of_word uses numpy/scipy matrix
        # arithmetic at native float precision).  The float→mpf conversion
        # is direct (no repr round-trip needed); the upstream float64 floor
        # is the real precision limit — promoting matrix ops to mpmath is
        # a separate refactor tracked for future precision tightening.
        total += mp.mpf(y) * mp.mpf(chi)
    return total


def term2_canonical(word: list, n_gens: int, q_val: float) -> mp.mpf:
    """T_2 = Σ_i z · Vol_q^({i})(β)   — canonical Markov-invariant form."""
    total = mp.mpf(0)
    for i in range(n_gens):
        vol_i = vol_q_S(word, {i}, n_gens, q_val)
        total += Z_MARK * vol_i
    return total


def term3_canonical(word: list, n_gens: int, q_val: float) -> mp.mpf:
    """T_3 = z² Σ_{i<j} Vol_q^({i, j})(β) — canonical Markov-invariant form."""
    from itertools import combinations
    total = mp.mpf(0)
    for i, j in combinations(range(n_gens), 2):
        vol_ij = vol_q_S(word, {i, j}, n_gens, q_val)
        total += Z_MARK ** 2 * vol_ij
    return total


def t2_t3_canonical_compare_to_old(Z: int, N: int) -> dict:
    """Compute canonical T_2/T_3 for an atom via the algebraic Markov form."""
    from mass_at_3A_proper import atom_braid_word_3A
    from q_parameter import Q as Q_0
    q_val = float(Q_0)
    word = atom_braid_word_3A(Z, N, include_inter=True)
    n_strands = 3 * (Z + N)
    n_gens = n_strands - 1

    return {
        "atom": f"(Z={Z}, N={N})",
        "n_strands": n_strands,
        "word_length": len(word),
        "t2_canonical_Markov_trace": float(term2_canonical(word, n_gens, q_val)),
        "t3_canonical_Markov_trace": float(term3_canonical(word, n_gens, q_val)),
    }


if __name__ == "__main__":
    print("Canonical T_2/T_3 sanity check (Markov-trace form):")
    print()
    for label, Z, N in [("p", 1, 0), ("n", 0, 1), ("D", 1, 1),
                          ("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]:
        try:
            r = t2_t3_canonical_compare_to_old(Z, N)
            print(f"  {label:>5}: n_strands={r['n_strands']:>2}  "
                  f"|word|={r['word_length']:>2}  "
                  f"T_2(canonical) = {r['t2_canonical_Markov_trace']:>+12.4f}  "
                  f"T_3(canonical) = {r['t3_canonical_Markov_trace']:>+12.4f}")
        except Exception as exc:
            print(f"  {label:>5}: ERROR {type(exc).__name__}: {exc}")
