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
