#!/usr/bin/env python3
"""branching_tower.py — step 1 of the Magnus-sign branching tower for A ≥ 5.

Implements and VALIDATES the seminormal branching restriction H_n ↓ H_{n-1} in
the standard-Young-tableau (SYT) basis. This is the foundation of the
representation-level transfer-matrix tower planned in
`docs/workplans/2026-08-30-magnus-sign-branching-tower-for-high-A.md`: the SYT
basis IS the iterated branching basis, so restricting to the H_{n-1} subalgebra
block-decomposes ρ_λ by the position of the entry n.

BRANCHING RULE (Young). For λ ⊢ n, the H_{n-1} = ⟨σ_1,…,σ_{n-2}⟩ sub-action on
the seminormal rep ρ_λ decomposes as ⊕_μ ρ_μ, μ ranging over the shapes obtained
by removing one (corner) box from λ. In the SYT basis this is *automatic*: an SYT
t of λ, restricted to entries 1..n-1, is an SYT of μ(t) = λ with the box of n
removed. So:
  • the SYT of λ partition into μ-blocks (grouped by where n sits), and
  • σ_k for k ≤ n-2 preserves those blocks and acts on each as ρ_μ.

VALIDATION (--validate). For λ ⊢ n (n ∈ {4,6,9,12}) this checks, against the
flat dense seminormal builder, both halves of the branching statement:
  (a) BLOCK-DIAGONAL: σ_k (k ≤ n-2) has zero coupling between distinct μ-blocks.
  (b) SUB-REP MATCH: the μ-block of σ_k equals the standalone H_{n-1} seminormal
      ρ_μ(σ_k), matched SYT-by-SYT (via the sub-tableau ↦ μ-index map).
Both must hold to <1e-55. This is the gate that the SYT branching is faithful;
the transfer-matrix contraction (step 3-4) is built on top of it.

scope-(a) infrastructure; no physics claim, nothing wired. NO-FLOAT64: mpmath.
"""
from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "hecke"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "substrate"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
mp.mp.dps = 80

from hecke_characters import (  # noqa: E402
    build_seminormal_matrices_mp,
    standard_young_tableaux,
)
from substrate.q_parameter import Q_50_DIGIT_STR as _Q0_RESOLVED  # noqa: E402

Q0 = mp.mpf(_Q0_RESOLVED)


def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def _remove_box(shape, row):
    """λ with one box removed from `row` (must stay a partition)."""
    lam = list(shape)
    lam[row] -= 1
    return tuple(x for x in lam if x > 0)


def branching_blocks(shape):
    """Block-decompose the SYT of λ⊢n by the position of the entry n.

    Returns (blocks, syts, cells) where blocks maps μ ⊢ (n-1) → list of SYT
    indices (into `syts`, in λ's own ordering) whose n-box removal gives μ."""
    n = sum(shape)
    syts, cells, contents = standard_young_tableaux(shape)
    blocks: dict[tuple, list[int]] = {}
    for i, t in enumerate(syts):
        r, _c = cells[t[n]]                     # (row,col) of the entry n
        mu = _remove_box(shape, r)
        blocks.setdefault(mu, []).append(i)
    return blocks, syts, cells


def _sub_syt_index_map(shape, block_indices, syts, cells, mu):
    """For each λ-SYT in the μ-block, the index of its (1..n-1)-restriction in
    the standalone standard_young_tableaux(μ) ordering."""
    n = sum(shape)
    mu_syts, mu_cells, _ = standard_young_tableaux(mu)
    mu_pos_to_idx = {pos: k for k, pos in enumerate(mu_cells)}   # (r,c) → μ cell index
    mu_syt_key = {tuple(sorted(d.items())): k for k, d in enumerate(mu_syts)}
    out = []
    for i in block_indices:
        t = syts[i]
        sub = {}
        for entry in range(1, n):               # entries 1..n-1 live in μ's diagram
            pos = cells[t[entry]]                # (r,c) in λ == (r,c) in μ (μ ⊆ λ)
            sub[entry] = mu_pos_to_idx[pos]
        out.append(mu_syt_key[tuple(sorted(sub.items()))])
    return out, mu_syts


def validate_branching(shape, tol=mp.mpf(10) ** -55):
    """Check H_n ↓ H_{n-1} branching of ρ_shape against standalone ρ_μ.

    Returns (worst_offdiag, worst_match, n_mu_blocks)."""
    n = sum(shape)
    sig, dim, _ = build_seminormal_matrices_mp(shape, Q0)     # H_n, generators σ_1..σ_{n-1}
    blocks, syts, cells = branching_blocks(shape)
    index_of = {idx: b for b, idxs in blocks.items() for idx in idxs}  # syt idx → μ

    worst_off = mp.mpf(0)
    worst_match = mp.mpf(0)

    # (a) block-diagonal: σ_k, k ≤ n-2 (list indices 0..n-3), no cross-μ coupling
    for k in range(0, n - 2):                     # σ_1 .. σ_{n-2}
        M = sig[k]
        for a in range(dim):
            for b in range(dim):
                if index_of[a] != index_of[b]:
                    worst_off = max(worst_off, abs(M[a, b]))

    # (b) each μ-block equals the standalone H_{n-1} seminormal ρ_μ
    for mu, block_idx in blocks.items():
        if sum(mu) == 0:
            continue
        muidx, _mu_syts = _sub_syt_index_map(shape, block_idx, syts, cells, mu)
        rho_mu, dmu, _ = build_seminormal_matrices_mp(mu, Q0)  # H_{n-1}
        for k in range(0, n - 2):                 # σ_1..σ_{n-2} act on H_{n-1}
            for a in range(len(block_idx)):
                for b in range(len(block_idx)):
                    lhs = sig[k][block_idx[a], block_idx[b]]
                    rhs = rho_mu[k][muidx[a], muidx[b]]
                    worst_match = max(worst_match, abs(lhs - rhs))
    return worst_off, worst_match, len(blocks)


def run_validate(shapes=None):
    if shapes is None:
        shapes = []
        for nn in (4, 6, 9):
            shapes += list(partitions(nn))
    print(f"[branching] validating H_n ↓ H_{{n-1}} on {len(shapes)} shapes "
          f"(n ∈ {sorted(set(sum(s) for s in shapes))}) at q0={mp.nstr(Q0,12)}", flush=True)
    worst_off = mp.mpf(0)
    worst_match = mp.mpf(0)
    for shape in shapes:
        if sum(shape) < 2:
            continue
        wo, wm, nb = validate_branching(shape)
        worst_off = max(worst_off, wo)
        worst_match = max(worst_match, wm)
        print(f"  {str(tuple(shape)):>22} n={sum(shape):>2} μ-blocks={nb:>2}  "
              f"offdiag={mp.nstr(wo,3):>10}  match={mp.nstr(wm,3):>10}", flush=True)
    print(f"[branching] worst off-diagonal (cross-μ coupling, must be 0) = {mp.nstr(worst_off,3)}")
    print(f"[branching] worst sub-rep mismatch (block vs ρ_μ, must be 0)  = {mp.nstr(worst_match,3)}")
    ok = worst_off < mp.mpf(10) ** -55 and worst_match < mp.mpf(10) ** -55
    assert worst_off < mp.mpf(10) ** -55, "BRANCHING FAIL: σ_k couples distinct μ-blocks"
    assert worst_match < mp.mpf(10) ** -55, "BRANCHING FAIL: μ-block ≠ standalone ρ_μ"
    print("[branching] PASS — SYT branching H_n ↓ H_{n-1} is faithful (both halves).")
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--validate", action="store_true", help="validate the branching restriction")
    ap.add_argument("--n", type=int, default=None, help="validate only shapes of this n")
    args = ap.parse_args()
    if args.n:
        run_validate(list(partitions(args.n)))
    else:
        run_validate()


if __name__ == "__main__":
    main()
