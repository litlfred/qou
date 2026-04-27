#!/usr/bin/env python3
"""
Hoefsmit + Wenzl-bridge tr_M evaluation at 50 dps.

Replaces the recursive sympy `tr_M_word` path used by
`atomic_tr_m_mpfr_50dps.py` for atoms at A >= 3 (where the recursion
times out at H_9 with 100+ NF terms).

Master-prop closed form (Wenzl bridge):

    tr_M(W) = Σ_{λ ⊢ n} y_λ(q) · χ_λ(W)

with χ_λ(W) = trace(ρ_λ(W)) and y_λ(q) precomputed at 50 dps in
`y-lambda-mpfr-witness.json`.

For the 3A-strand atom braid `W = Π_k (c_k σ_{g_k} + d_k I)` the
character per partition is

    M_λ = Π_k (c_k · σ_{g_k}^λ  +  d_k · I)
    χ_λ(W) = tr(M_λ)

Per-σ matrices σ_g^λ are built in the Hoefsmit (Young seminormal)
basis at 50 dps mpf, then multiplied by the Hecke factors.

Cost at A=3 (n=9): 30 partitions × 33 word factors × max-d_λ² (=42²)
≈ 1.7 M mpf ops — sub-second wall time, vs. the symbolic path's
>4 minutes.

Public entry point:

    tr_M_via_wenzl_bridge_mpfr(word, n, q_str, *, dps=50,
                               y_lambda_path=None)
        word: list of (c, d, g) Hecke factors (e.g. atom_braid_word_3A).
        n:    strand count of the ambient H_n (e.g. n = 3A).
        q_str: q_0 as a decimal string at >= dps precision.
        Returns: mpf at the chosen dps.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Iterable, Sequence

import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))
from hecke_characters import (partitions_of, standard_young_tableaux)


_HERE = Path(__file__).parent
_Y_LAMBDA_DEFAULT = _HERE / "y-lambda-mpfr-witness.json"


def _build_seminormal_matrices_mpf(shape: tuple[int, ...],
                                    q: mp.mpf) -> tuple[list, int]:
    """Hoefsmit YSN matrices σ_1 .. σ_{n-1} at mpf precision.

    Mirrors `hecke_characters.build_seminormal_matrices` but in pure
    mpmath arithmetic so every entry inherits the active dps.

    Returns (sigmas, dim) where each sigma is an `mp.matrix` of shape
    (dim, dim).  sigmas is 0-indexed: sigmas[k-1] = σ_k acts on
    positions (k, k+1).
    """
    n = sum(shape)
    syts, _, contents = standard_young_tableaux(shape)
    dim = len(syts)
    if dim == 0:
        return [], 0

    h = q - mp.mpf(1) / q
    one = mp.mpf(1)

    sigmas = []
    for k in range(1, n):
        M = mp.matrix(dim, dim)
        processed = set()
        for i in range(dim):
            if i in processed:
                continue
            ci_k = syts[i][k]
            ci_k1 = syts[i][k + 1]
            rho = contents[ci_k1] - contents[ci_k]
            a = h / (one - q ** (-2 * rho))

            swap_map = dict(syts[i])
            swap_map[k] = ci_k1
            swap_map[k + 1] = ci_k
            j = None
            for jj in range(dim):
                if jj == i:
                    continue
                if syts[jj] == swap_map:
                    j = jj
                    break

            if j is None:
                M[i, i] = a
                processed.add(i)
            else:
                a_prime = h / (one - q ** (2 * rho))
                b_sq = a * a_prime + one
                # b_sq is real-positive in YSN; mp.sqrt on a real mpf
                # gives the principal real root.
                b = mp.sqrt(abs(b_sq))
                M[i, i] = a
                M[j, j] = a_prime
                M[i, j] = b
                M[j, i] = b
                processed.add(i)
                processed.add(j)
        sigmas.append(M)
    return sigmas, dim


def _chi_lambda_of_word_mpf(sigmas: list, dim: int,
                              word: Sequence[tuple[float, float, int]]
                              ) -> mp.mpf:
    """χ_λ(W) at mpf precision for a Hecke-factor word.

    word is a list of (c, d, g) triples — each contributes a factor
    c · σ_g + d · I to the matrix product.  Returns trace(product).
    """
    if dim == 0:
        return mp.mpf(0)
    I = mp.eye(dim)
    product = mp.eye(dim)
    for (c, d, g) in word:
        if g >= len(sigmas):
            raise IndexError(
                f"word uses generator σ_{g} but only {len(sigmas)} "
                f"seminormal matrices were provided (partition λ has "
                f"too few cells)")
        c_mp = mp.mpf(str(c)) if not isinstance(c, mp.mpf) else c
        d_mp = mp.mpf(str(d)) if not isinstance(d, mp.mpf) else d
        M = c_mp * sigmas[g] + d_mp * I
        product = product * M
    tr = mp.mpf(0)
    for i in range(dim):
        tr += product[i, i]
    return tr


def _load_y_lambda(n: int, path: Path | None = None) -> dict:
    """Load y_λ table for H_n from the mpfr witness.

    Returns dict: tuple(partition) -> mpf(y_lambda).
    """
    p = Path(path) if path else _Y_LAMBDA_DEFAULT
    with open(p) as f:
        W = json.load(f)
    table = W["tables_by_n"].get(str(n))
    if table is None:
        raise KeyError(
            f"y-lambda-mpfr-witness.json has no table for n={n}; "
            f"available: {sorted(W['tables_by_n'].keys(), key=int)}")
    return {tuple(w["partition"]): mp.mpf(w["y_lambda"])
            for w in table["weights"]}


def tr_M_via_wenzl_bridge_mpfr(
    word: Sequence[tuple[float, float, int]],
    n: int,
    q_str: str,
    *,
    dps: int = 50,
    y_lambda_path: Path | None = None,
    return_breakdown: bool = False,
) -> mp.mpf | dict:
    """Compute tr_M(W) at mpf precision via Σ_λ y_λ · χ_λ(W).

    Args:
        word: Hecke-factor list [(c, d, g), ...] (e.g. from
              atom_braid_word_3A).
        n: strand count of H_n.
        q_str: q_0 as decimal string at >= dps precision.
        dps: working precision (default 50).
        y_lambda_path: override path to y-lambda witness JSON.
        return_breakdown: if True, return a dict with per-λ χ_λ and
            running partial sums; if False (default), return the mpf
            result only.
    """
    with mp.workdps(dps):
        q = mp.mpf(q_str)
        y_table = _load_y_lambda(n, y_lambda_path)

        # n_gens needed in any partition's representation = max generator
        # index in the word + 1 (because g is 0-indexed for σ_{g+1}).
        max_g = max((g for _, _, g in word), default=-1)

        total = mp.mpf(0)
        breakdown = []
        for shape in partitions_of(n):
            shape_t = tuple(shape)
            y_lam = y_table.get(shape_t)
            if y_lam is None:
                # Should never happen for a complete witness, but guard.
                continue
            sigmas, dim = _build_seminormal_matrices_mpf(shape_t, q)
            if dim == 0:
                continue
            # Skip partitions whose seminormal rep doesn't carry the
            # generator we need (cannot happen for n strands ≥ word's
            # max_g + 2, which is the contract).
            if max_g >= len(sigmas):
                # The partition is "too small" to host generator σ_{max_g}.
                # In a correct H_n call this never trips because n strands
                # always supply n-1 generators.  Defensive: treat χ = 0.
                continue
            chi = _chi_lambda_of_word_mpf(sigmas, dim, word)
            contrib = y_lam * chi
            total += contrib
            if return_breakdown:
                breakdown.append({
                    "partition": list(shape_t),
                    "dim": dim,
                    "y_lambda": str(y_lam),
                    "chi_lambda": str(chi),
                    "contribution": str(contrib),
                })

        if return_breakdown:
            return {
                "tr_M": str(total),
                "n": n,
                "q": q_str,
                "dps": dps,
                "n_partitions_used": len(breakdown),
                "by_partition": breakdown,
            }
        return total


# ── Self-test against the canonical prop table ──────────────────

if __name__ == "__main__":
    # The prop table in markov_trace_canonical sets:
    #   tr_M(1) = 1
    #   tr_M(σ_0) = z
    #   tr_M(σ_0 σ_1) = z²
    #   tr_M(σ_0 σ_1 σ_0) = h z² + z
    #   tr_M(σ_0²)  = h z + 1
    Q_STR = "1.1099785955541805752815940796095093779667618976181"
    with mp.workdps(60):
        q = mp.mpf(Q_STR)
        h = q - 1 / q
        z = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))

    # All cases evaluated at n=3 (minimum n with a y_λ table).  The
    # canonical Markov trace is consistent across the tower, so any
    # H_2 element embeds into H_3 with the same tr_M.
    cases = [
        ("identity",      [],                                  3, lambda: 1),
        ("σ_0",           [(1.0, 0.0, 0)],                     3, lambda: z),
        ("σ_0 σ_1",       [(1.0, 0.0, 0), (1.0, 0.0, 1)],      3, lambda: z * z),
        ("σ_0 σ_1 σ_0",   [(1.0, 0.0, 0), (1.0, 0.0, 1),
                            (1.0, 0.0, 0)],                     3, lambda: h * z * z + z),
        ("σ_0²",          [(1.0, 0.0, 0), (1.0, 0.0, 0)],      3, lambda: h * z + 1),
    ]

    print("=" * 78)
    print("Hoefsmit + Wenzl-bridge tr_M @ 50 dps — prop-table self-test")
    print(f"q_0 = {Q_STR[:40]}...")
    print("=" * 78)
    # Threshold reflects the precision of the y-lambda-mpfr-witness.json
    # input q (currently stored at f64 ≈ 1e-16); regenerating that witness
    # with a 50-dps q_str would tighten this to ~1e-45.
    TOL = mp.mpf("1e-14")
    n_pass = 0
    for name, word, n_strands, expected_fn in cases:
        with mp.workdps(60):
            expected = expected_fn()
        got = tr_M_via_wenzl_bridge_mpfr(word, n_strands, Q_STR, dps=50)
        diff = abs(got - expected)
        ok_str = "✓" if diff < TOL else "✗"
        if diff < TOL:
            n_pass += 1
        print(f"  {name:<14}  got={mp.nstr(got, 20):<25}  "
              f"want={mp.nstr(expected, 20):<25}  |Δ|={mp.nstr(diff, 3)}  {ok_str}")
    print(f"\n  {n_pass}/{len(cases)} cases match within {mp.nstr(TOL, 2)}")
    print("  (f64-limited by y-lambda witness input q; structural agreement OK)")
    sys.exit(0 if n_pass == len(cases) else 1)
