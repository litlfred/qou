"""Sparse + diagonal-only `ρ_ξ(W)` for the A-operator combiner.

Because `A^λ_{ξν}(I)` is block-diagonal in `V_ξ` (`a_operator_recursive.py`,
`interface_blocks` sets only matching-inner-index entries), the combiner
contraction `Tr[A·(ρ_ξ⊗ρ_ν)]` uses **only the diagonal** of `ρ_ξ(W_inner)`.
The ⁴He cross-check nonetheless builds the full dense `d_ξ×d_ξ` matrix
(`O(d_ξ³·|W|)` time, `O(d_ξ²)` memory). This module computes exactly what is
needed, two ways:

  * `rho_word_full_sparse` — the full `d_ξ×d_ξ` matrix via sparse right-multiply
    by `c·σ_g + d·I` (the Young seminormal `σ_g` are block `1×1`/`2×2`): `O(d²)`
    per crossing, not `O(d³)`. For A≤5 where the `d×d` matrix fits.
  * `rho_word_diag` — the diagonal only, one column at a time via sparse
    mat-vec chains: `O(d²·|W|)` time but `O(d)` memory. Removes the `d×d`
    storage wall that blocks the largest A=6 blocks (`d_ξ≤2.9·10⁵` at ξ⊢15).

Both are exact reorganisations of the same arithmetic (verified against the
direct `prod` build and the `chi_young` combiner identity to 50 dps in
`computations/probes/rho_xi_diagonal_verify.py`). No fit, no production change.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from young_seminormal import standard_tableaux, _content_by_index  # noqa: E402


def sparse_generators(xi, q_str: str, dps: int):
    """Sparse Young seminormal generators of irrep `ξ` — built directly.

    Returns `(nz, d)` where `nz[g]` is a list of `(i, j, value)` triples for
    `ρ_ξ(σ_{g+1})` (0-based `g`, i.e. the 1-based generator `g+1`), and
    `d = d_ξ`. Emits only the `1×1`/`2×2` nonzeros (`O(d)` per generator), via
    the same non-symmetric rule as `young_seminormal.seminormal_sigma` — so it
    never materialises a `d×d` matrix (the A=6 memory enabler).
    """
    q = mp.mpf(q_str)
    qi = 1 / q
    syts = standard_tableaux(xi)
    cont = _content_by_index(xi)
    d = len(syts)
    index = {tuple(sorted(t.items())): k for k, t in enumerate(syts)}
    n = sum(xi)
    nz = []
    for i in range(1, n):                                # 1-based generator σ_i
        entries = []
        for k, t in enumerate(syts):
            bi, bj = t[i], t[i + 1]
            delta = cont[bj] - cont[bi]
            if delta == 1:                              # same row
                entries.append((k, k, q))
            elif delta == -1:                           # same column
                entries.append((k, k, -qi))
            else:                                       # 2×2 block (set once)
                u = dict(t)
                u[i], u[i + 1] = t[i + 1], t[i]
                ku = index[tuple(sorted(u.items()))]
                if k < ku:
                    diag_t = (q - qi) / (1 - q ** (-2 * delta))
                    diag_u = (q - qi) - diag_t
                    entries.append((k, k, diag_t))
                    entries.append((ku, ku, diag_u))
                    entries.append((k, ku, mp.mpf(1)))
                    entries.append((ku, k, diag_t * diag_u + 1))
        nz.append(entries)
    return nz, d


def rho_word_full_sparse(xi, q_str: str, dps: int, word):
    """Full `ρ_ξ(word) = ∏_k (c_k·σ_{g_k} + d_k·I)` via sparse right-multiply.

    `word` is a list of `(c, d, g)` triples (0-based `g`). `O(d²·|word|)` time.
    """
    nz, d = sparse_generators(xi, q_str, dps)
    M = mp.eye(d)
    for (c, dc, g) in word:
        # N = M·(c·σ_g + dc·I) = dc·M + c·(M·σ_g); (M·σ_g)[:,l] += σ_g[k,l]·M[:,k]
        N = dc * M
        for (k, l, v) in nz[g]:
            cv = c * v
            for i in range(d):
                N[i, l] += cv * M[i, k]
        M = N
    return M, d


def rho_word_diag(xi, q_str: str, dps: int, word):
    """`diag(ρ_ξ(word))` column-by-column. `O(d²·|word|)` time, `O(d)` memory.

    `diag[a] = (ρ_ξ(word)·e_a)[a]`, with `ρ_ξ(word)·e_a = G_1(…(G_m·e_a))`
    applied by sweeping `word` in reverse. Returns `(diag_list, d)`.
    """
    nz, d = sparse_generators(xi, q_str, dps)
    rev = list(reversed(word))
    diag = [mp.mpf(0)] * d
    for a in range(d):
        v = [mp.mpf(0)] * d
        v[a] = mp.mpf(1)
        for (c, dc, g) in rev:
            # w = (c·σ_g + dc·I)·v ; (σ_g·v)[i] += σ_g[i,j]·v[j]
            w = [dc * v[i] for i in range(d)]
            for (i, j, val) in nz[g]:
                vj = v[j]
                if vj != 0:
                    w[i] += c * val * vj
            v = w
        diag[a] = v[a]
    return diag, d


def combiner_value_streaming(blocks, RB, word, q_str: str, dps: int):
    """χ-combiner `Σ_{ξ,ν} Tr[A^{ξν}·(ρ_ξ(word)⊗ρ_ν)]` — contraction-only, streamed.

    Because `A^λ_{ξν}` is block-diagonal in `V_ξ`, the contraction reduces to
    `Σ_ξ Σ_a v_a · diag(ρ_ξ(word))[a]` with `v_a = Σ_ν Σ_{b,b'} A^{ξν}_{a,b,b'}
    ρ_ν[b',b]` a precomputed scalar per inner-basis index `a`. Each
    `diag(ρ_ξ)[a]` is produced one column at a time and consumed immediately, so
    `ρ_ξ` is never materialised — `O(d_ξ)` memory (the only form that fits the
    largest A=6 blocks). `blocks = {(ξ,ν): A}`, `RB = {ν: ρ_ν(block)}` (small).

    Exactly the diagonal-only contraction of `interface_blocks` reorganised; same
    arithmetic, `O(Σ_ξ d_ξ²·|word|)` time (the irreducible cost — see the cost
    probe). No fit.
    """
    from collections import defaultdict
    by_xi = defaultdict(list)
    for (xi, nu), A in blocks.items():
        by_xi[xi].append((nu, A))

    total = mp.mpf(0)
    rev = list(reversed(word))
    for xi, nus in by_xi.items():
        nz, d = sparse_generators(xi, q_str, dps)
        # v[a] = Σ_ν Σ_{b,b'} A^{ξν}[a·d_ν+b, a·d_ν+b'] · ρ_ν[b',b]
        v = [mp.mpf(0)] * d
        for (nu, A) in nus:
            d_nu = RB[nu].rows
            for a in range(d):
                s = mp.mpf(0)
                for b in range(d_nu):
                    for bp in range(d_nu):
                        s += A[a * d_nu + b, a * d_nu + bp] * RB[nu][bp, b]
                v[a] += s
        # stream: diag(ρ_ξ(word))[a] = (ρ_ξ(word)·e_a)[a], one column at a time
        for a in range(d):
            if v[a] == 0:
                continue
            vec = [mp.mpf(0)] * d
            vec[a] = mp.mpf(1)
            for (c, dc, g) in rev:
                w = [dc * vec[i] for i in range(d)]
                for (i, j, val) in nz[g]:
                    vj = vec[j]
                    if vj != 0:
                        w[i] += c * val * vj
                vec = w
            total += v[a] * vec[a]
    return total
