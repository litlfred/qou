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

from _precision import set_compute_dps, fmt  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402

set_compute_dps()


def _as_mpf_q(q_val) -> mp.mpf:
    """q as mpf. A Python float is refused: it caps every trace at ~1e-16
    (f64_into_mpmath_audit F64_CAST). Pass `q_parameter.Q_MP` or a string."""
    if isinstance(q_val, float):
        raise TypeError("canonical_brane_tower: pass q as mpf/str (Q_MP), "
                        "not float; a float caps the trace at ~1e-16")
    return mp.mpf(q_val)


def _z_D(q: mp.mpf) -> mp.mpf:
    """Convention-D Markov parameter z = q^3/(q^2+1) (owner ruling 2026-08-15).
    Was `hecke_core.z`, the same value as a float64 constant."""
    return q ** 3 / (q ** 2 + 1)


def _seminormal_mp(shape, q: mp.mpf):
    """Exact mpmath seminormal matrices [rho(sigma_1), ...] via the MPFR binding."""
    from a_operator.a_operator_categorical import exact_seminormal_matrices
    dps = mp.mp.dps
    return exact_seminormal_matrices(tuple(shape), mp.nstr(q, dps + 5), dps)


def _chi_mp(mats, dim: int, word) -> mp.mpf:
    """chi(W) = tr prod_k (c_k sigma_{g_k} + d_k I), all in mpf."""
    M = mp.eye(dim)
    for (c, d, g) in word:
        M = M * (mp.mpf(c) * mats[g] + mp.mpf(d) * mp.eye(dim))
    return sum(M[i, i] for i in range(dim))


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

    q = _as_mpf_q(q_val)
    y_vals = y_lambda_at(n_sub_strands, q_val=q)
    total = mp.mpf(0)
    for shape, y in y_vals.items():
        # Exact mpmath seminormal rep + mpf character (2026-11-21). This was
        # the float64 build_seminormal_matrices / chi_lambda_of_word pair,
        # which capped every Vol_q^(S) at ~1e-16; the sub-words have at most
        # three strands, so the mpf path costs nothing measurable.
        mats, dim = _seminormal_mp(shape, q)
        if dim == 0:
            continue
        total += mp.mpf(y) * _chi_mp(mats, dim, sub_remapped)
    return total


def term2_canonical(word: list, n_gens: int, q_val: float) -> mp.mpf:
    """T_2 = Σ_i z · Vol_q^({i})(β)   — canonical Markov-invariant form."""
    z = _z_D(_as_mpf_q(q_val))
    total = mp.mpf(0)
    for i in range(n_gens):
        vol_i = vol_q_S(word, {i}, n_gens, q_val)
        total += z * vol_i
    return total


def term3_canonical(word: list, n_gens: int, q_val: float) -> mp.mpf:
    """T_3 = z² Σ_{i<j} Vol_q^({i, j})(β) — canonical Markov-invariant form."""
    from itertools import combinations
    z = _z_D(_as_mpf_q(q_val))
    total = mp.mpf(0)
    for i, j in combinations(range(n_gens), 2):
        vol_ij = vol_q_S(word, {i, j}, n_gens, q_val)
        total += z ** 2 * vol_ij
    return total


def t2_t3_canonical_compare_to_old(Z: int, N: int) -> dict:
    """Compute canonical T_2/T_3 for an atom via the algebraic Markov form."""
    from mass_at_3A_proper import atom_braid_word_3A
    from q_parameter import Q_MP
    q_val = Q_MP
    word = atom_braid_word_3A(Z, N, include_inter=True, q=Q_MP)
    n_strands = 3 * (Z + N)
    n_gens = n_strands - 1

    return {
        "atom": f"(Z={Z}, N={N})",
        "n_strands": n_strands,
        "word_length": len(word),
        "t2_canonical_Markov_trace": term2_canonical(word, n_gens, q_val),
        "t3_canonical_Markov_trace": term3_canonical(word, n_gens, q_val),
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
                  f"T_2(canonical) = {mp.nstr(r['t2_canonical_Markov_trace'], 30)}  "
                  f"T_3(canonical) = {mp.nstr(r['t3_canonical_Markov_trace'], 30)}")
        except Exception as exc:
            print(f"  {label:>5}: ERROR {type(exc).__name__}: {exc}")
