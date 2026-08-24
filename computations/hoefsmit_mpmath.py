#!/usr/bin/env python3
"""Hoefsmit seminormal matrices and braid characters in **mpmath**, not float64.

The canonical fast path — ``pyhecke.syt_prefix_cache.build_seminormal_matrices_cached``
plus ``mass_at_3A_proper.chi_lambda_of_word`` — is float64 **by construction**:
``BlockCache`` computes its block values with ``math.sqrt`` against a ``1e-15``
degeneracy threshold, and the character routine accumulates the word into a
``numpy`` matrix and returns ``float(np.trace(...))``. Handing those functions a
50-dps ``mpf`` for ``q`` does not make them exact; numpy coerces on contact.

That matters under AGENTS.md §"PROBES ARE NOT EXEMPT": a probe whose substrate
block serialises a 50-digit ``q0`` while its payload is float64 advertises a
precision it does not have. This module supplies the same construction carried
end to end in ``mpmath``, so a probe can either compute in it or measure what
the float64 path was costing.

The formulas are Hoefsmit's, identical to the cached builder:

    ρ  = content(cell of k+1) − content(cell of k)
    a  = h / (1 − q^{−2ρ}),   a' = h / (1 − q^{2ρ}),   b = sqrt(|a·a' + 1|)

with the diagonal case ``a`` when the (k, k+1) transposition fixes the tableau,
and the 2×2 block ``[[a, b], [b, a']]`` on the swap pair otherwise.

Cost: dimensions at λ ⊢ 6 reach 16, so a 23-crossing word is ~10⁶ mpf products
per partition — a few seconds at 50 dps. Do not reach for this at λ ⊢ 12.
"""
from __future__ import annotations

import mpmath as mp


class BlockCacheMP:
    """Memoized (a, a', b) by content distance ρ, in mpmath.

    Mirrors ``pyhecke.syt_prefix_cache.BlockCache`` exactly, with two
    differences that are the whole point: ``mp.sqrt`` in place of
    ``math.sqrt``, and a degeneracy threshold tied to the working precision
    rather than the fixed float64 ``1e-15``.
    """

    def __init__(self, q, h=None):
        self.q = mp.mpf(q)
        self.h = mp.mpf(h) if h is not None else self.q - 1 / self.q
        self.hits = 0
        self.misses = 0
        self._by_rho: dict[int, tuple] = {}
        # Degeneracy guard scaled to the working precision, not to float64.
        self._eps = mp.mpf(10) ** (-(mp.mp.dps - 5))

    def get(self, rho: int):
        cached = self._by_rho.get(rho)
        if cached is not None:
            self.hits += 1
            return cached
        self.misses += 1
        q, h = self.q, self.h
        denom_a = 1 - q ** (-2 * rho)
        a = h / denom_a if abs(denom_a) > self._eps else mp.mpf(0)
        denom_ap = 1 - q ** (2 * rho)
        a_prime = h / denom_ap if abs(denom_ap) > self._eps else mp.mpf(0)
        b = mp.sqrt(abs(a * a_prime + 1))
        entry = (a, a_prime, b)
        self._by_rho[rho] = entry
        return entry


def seminormal_matrices_mp(shape, *, cache: BlockCacheMP):
    """``(sigmas, dim, syts)`` with ``sigmas`` a list of ``mp.matrix``.

    Same signature and same SYT ordering as
    ``build_seminormal_matrices_cached``, so results are directly comparable
    element by element.
    """
    from hecke_characters import standard_young_tableaux

    syts, cells, contents = standard_young_tableaux(shape)
    dim = len(syts)
    if dim == 0:
        return [], dim, syts
    n = sum(shape)

    syt_keys = [tuple(sorted(T.items())) for T in syts]
    syt_to_idx = {k: i for i, k in enumerate(syt_keys)}

    sigmas = []
    for k in range(1, n):
        M = mp.zeros(dim, dim)
        processed = [False] * dim
        for i in range(dim):
            if processed[i]:
                continue
            ci_k = syts[i][k]
            ci_k1 = syts[i][k + 1]
            a, a_prime, b = cache.get(contents[ci_k1] - contents[ci_k])

            Ti = dict(syts[i])
            Ti[k] = ci_k1
            Ti[k + 1] = ci_k
            j = syt_to_idx.get(tuple(sorted(Ti.items())))

            if j is None or j == i:
                M[i, i] = a
                processed[i] = True
            else:
                M[i, i] = a
                M[j, j] = a_prime
                M[i, j] = b
                M[j, i] = b
                processed[i] = True
                processed[j] = True
        sigmas.append(M)
    return sigmas, dim, syts


def chi_lambda_of_word_mp(sigmas, dim, word, n_gens_required: int):
    """χ_λ(W) = tr Π_k (c_k·σ_{g_k} + d_k·I), as an ``mpf``.

    ``word`` is the list of ``(c, d, gen_idx)`` triples from
    ``atom_braid_word_3A``; its offsets are already exact mpf, so nothing here
    reintroduces a float. Accumulation order matches
    ``mass_at_3A_proper.chi_lambda_of_word`` (``product = product @ M``).
    """
    if dim == 0:
        return mp.mpf(0)
    product = mp.eye(dim)
    I = mp.eye(dim)
    for (c, d, g) in word:
        if g >= len(sigmas):
            raise IndexError(
                f"word uses generator σ_{g} but only {len(sigmas)} seminormal "
                f"matrices were provided (partition too small)")
        product = product * (mp.mpf(c) * sigmas[g] + mp.mpf(d) * I)
    return mp.fsum(product[i, i] for i in range(dim))


def _sparse_rows(M, dim):
    """``mpmath`` matrix -> list of ``[(col, value), ...]`` per row, zeros dropped.

    The seminormal ``sigma_i`` are block-diagonal with 1x1 and 2x2 blocks, so a
    row holds at most 2 nonzeros regardless of ``dim``. That sparsity is the
    whole basis of `chi_lambda_of_word_sparse_mp` below; it is a property of
    Hoefsmit's construction, not an empirical observation about these words.
    """
    rows = [[] for _ in range(dim)]
    # mpmath stores a matrix as a dict of its NONZERO entries, so reading that
    # directly is O(nnz). The obvious `for j in range(dim): M[i, j]` scan is
    # O(dim^2) -- at dim=4158 that is 17M lookups per generator, ~11x over the
    # word's generators, which would cost more than the trace it feeds.
    # The attribute is name-mangled rather than public, hence the fallback.
    data = getattr(M, "_matrix__data", None)
    if isinstance(data, dict):
        for (i, j), v in data.items():
            if v != 0:
                rows[i].append((j, v))
        for row in rows:
            row.sort()
        return rows
    for i in range(dim):
        rows[i] = [(j, M[i, j]) for j in range(dim) if M[i, j] != 0]
    return rows


def chi_lambda_of_word_sparse_mp(sigmas, dim, word, n_gens_required: int):
    """Exact ``chi_lambda(W)``, same value as `chi_lambda_of_word_mp`, ~80x faster.

    WHY THIS EXISTS. The dense routine materialises the product, which is
    ``O(dim^3 * len(word))`` in mpmath arithmetic. At the sizes the A=4 [1^4]
    Schur-Weyl object needs that is not slow, it is unaffordable -- MEASURED at
    the canonical dps=70, one irrep of the ten:

        dim = 132   (6,6), the smallest      ~80 s
        dim = 4158  (5,3,3,1), the largest   ~705 h by cubic scaling
        all ten irreps                       ~1135 h

    THE METHOD. Only the trace is wanted, so the product need never exist:

        tr(prod_k M_k) = sum_i e_i^T (prod_k M_k) e_i

    Propagate ONE row vector through the factors as a dict of nonzeros --
    ``v <- c * (v @ sigma_g) + d * v`` -- and read component ``i`` at the end.
    Since ``sigma_g`` carries <= 2 nonzeros per row, each factor costs
    ``O(nnz(v))``, so the whole trace is ``O(dim^2 * len(word) * nnz_per_row)``
    rather than ``O(dim^3 * len(word))``.

    MEASURED, at dps=70, against the dense routine on the A=4 word (47 factors):

        dim=132   dense  20.472734309881028753   ~80 s
                  sparse 20.472734309881028753    ~1 s     (80-85x, two runs)
                  relative difference 7.077e-71

    THE VALUE ABOVE IS AT THE CANONICAL 50-DIGIT q. An earlier version of this
    note quoted 20.472734309881024467, which came from `mpf(str(q_parameter.Q))`
    -- and `q_parameter.Q` is a Python FLOAT, so that pins the substrate to 16
    digits. The dense-vs-sparse agreement was unaffected (same q on both sides),
    but the character itself was a float64-q character, differing from the
    probe's at ~1e-16 for a reason having nothing to do with either routine.

    7e-71 at a 70-digit working precision is agreement to the arithmetic, not a
    float64 floor -- the distinction that makes the timing mean anything. Over
    the ten irreps this is ~36 min (nnz/row = 1, as at dim=132) to ~73 min
    (nnz/row = 2, which the larger irreps carry), against ~1135 h dense.

    PRIOR ART, found AFTER writing this and credited here rather than quietly:
    `computations/hoefsmit_sparse_prototype_probe.py` (bean `qou-bk0q`, landed
    2026-08-23) established the same structural fact first -- "at most 2
    nonzeros per row: a diagonal entry plus, where a swap partner exists, one
    symmetric off-diagonal pair", with measured densities of 1.31 % at dim 120
    and 0.34 % at dim 462. It also notes the pairs form a partial MATCHING, so
    the column updates cannot alias.

    The two are COMPLEMENTARY, not duplicates. That probe attacks MEMORY in
    float64 -- eleven dense generators at dim 7700 occupy 5.22 GB, which is
    what hangs the He-4 atom of `rho_k_co_casimir_extended` -- and vectorises
    the step into three numpy expressions. This routine attacks PRECISION: it
    keeps mpmath end to end, where no vectorisation is available and the win
    has to come from not materialising the product at all. Anyone extending
    either should read both.

    I should have found it before building this; a corpus grep for "sparse" +
    "hoefsmit" would have. Recording that rather than presenting the structural
    observation as new.

    ACCUMULATION ORDER is left-to-right, matching `chi_lambda_of_word_mp` and
    `mass_at_3A_proper.chi_lambda_of_word`. That is why the two agree exactly
    rather than merely closely, and it is worth preserving: mpmath addition is
    not associative, so a reordering would show up as a small disagreement and
    be indistinguishable from a bug.

    SET `mp.dps` FIRST. This module does not, and neither does `_precision` on
    import -- its own docstring says so. At mpmath's default 15 both routines
    silently compute at float64 grade and agree to ~1e-16 for that reason
    alone, which is a measurement of the arithmetic rather than of the braid
    (bean `qou-fmoi`).
    """
    if dim == 0:
        return mp.mpf(0)
    for (_c, _d, g) in word:
        if g >= len(sigmas):
            raise IndexError(
                f"word uses generator sigma_{g} but only {len(sigmas)} "
                f"seminormal matrices were provided (partition too small)")
    sig_rows = [_sparse_rows(M, dim) for M in sigmas]
    # Coerce the word's offsets once rather than per basis vector: `dim` is up
    # to 4158, so this saves ~4158x the mpf construction cost.
    coerced = [(mp.mpf(c), mp.mpf(d), g) for (c, d, g) in word]
    zero = mp.mpf(0)
    diagonal = []
    for start in range(dim):
        v = {start: mp.mpf(1)}
        for (c, d, g) in coerced:
            rows = sig_rows[g]
            nv = {}
            for i, vi in v.items():
                if d != 0:
                    nv[i] = nv.get(i, zero) + d * vi
                cvi = c * vi
                if cvi != 0:
                    for j, sv in rows[i]:
                        nv[j] = nv.get(j, zero) + cvi * sv
            v = {k: val for k, val in nv.items() if val != 0}
        diagonal.append(v.get(start, zero))
    # fsum, as the dense routine does -- exact summation over `dim` terms.
    return mp.fsum(diagonal)
