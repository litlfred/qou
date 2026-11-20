#!/usr/bin/env python3
"""reduced_block_kernel — H_3 per-nucleon block caching for #2062.

This implements the Tier-3 reduced-block kernel optimization. 
By keying the cache on the per-nucleon H_3 block (which is invariant 
across isotopes) instead of the global shape λ, we reduce the 
trace calculation to an O(A) composition of these cached blocks.
This guarantees precision by NOT truncating any partitions, while 
drastically improving scale for large A.
"""
from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from chi_monotone_transfer import _addable, _add, _alpha_beta, word_to_mpfr, chi_all_lambda
from mass_at_3A_proper import atom_braid_word_3A
from q_parameter import Q_50_DIGIT_STR, Q_MP
import time
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

# Module-level cache keyed by:
# (q, dps, ab0, ab1, ab2, shape_in, c_in) -> {(shape_out, c_out): amplitude}
#
# `q` AND the working precision are both part of the key (bean `qou-h3qk`).
# They were both absent until 2026-09-04 while the body computes with `q`
# (`hq = q - qi`; `D(delta) = hq / (1 - q**(-2*delta))`), so two calls sharing
# an (ab, shape, c) key at different `q` returned whichever `q` arrived first —
# silently, with no raise and no warning. Demonstrated on a cold cache: a call
# at q = 1.9 following one at q = 1.11 returned the q = 1.11 amplitudes and
# differed from q = 1.9 computed on a fresh cache.
#
# The ab tuples are themselves functions of `q`, so most `q` pairs miss the
# cache correctly and the hazard needs two `q` reaching equal ab — but this is
# a MODULE-level dict that lives for the whole interpreter and is shared by
# unrelated callers, so "usually misses" is not a guarantee anyone can rely on.
#
# `q` is keyed by its exact 50-digit decimal, not by the mpf object: an mpf
# carries the precision it was CREATED at, so two mpf equal in value can be
# distinct objects, and `mp.nstr` gives a stable, hashable identity. `mp.mp.dps`
# joins it because a block computed at 50 dps and reused at 90 is the same
# class of silent staleness one level down.
_H3_TRANSITION_CACHE = {}


def _q_key(q):
    """Stable hashable identity for `q` + the ambient working precision."""
    return (mp.nstr(q, 50), mp.mp.dps)


def get_h3_transitions(ab0, ab1, ab2, q, qi, shape_in, c_in, Dc):
    """
    Compute and cache the 3-step fine-Bratteli transitions for a single nucleon (3 generators).
    The nucleon type is effectively defined by the alpha/beta tuples (ab0, ab1, ab2)
    TOGETHER WITH `q`, which the body below uses via `hq` and `D` — see the
    cache comment above for why leaving `q` out of the key was a live defect.
    """
    key = (_q_key(q), ab0, ab1, ab2, shape_in, c_in)
    if key in _H3_TRANSITION_CACHE:
        return _H3_TRANSITION_CACHE[key]

    hq = q - qi
    def D(delta: int):
        if delta in Dc:
            return Dc[delta]
        v = hq / (1 - q ** (-2 * delta))
        Dc[delta] = v
        return v

    # Step 1: ab0 (Junction generator)
    amp1 = defaultdict(int)
    alpha, beta = ab0
    for (r, c) in _addable(shape_in):
        c_other = c - r
        f = alpha * D(c_other - c_in) + beta
        amp1[(_add(shape_in, (r, c)), c_other)] += f

    # Step 2: ab1 (Internal 1)
    amp2 = defaultdict(int)
    alpha, beta = ab1
    for (s1, c1), a1 in amp1.items():
        for (r, c) in _addable(s1):
            c_other = c - r
            f = alpha * D(c_other - c1) + beta
            amp2[(_add(s1, (r, c)), c_other)] += a1 * f

    # Step 3: ab2 (Internal 2)
    amp3 = defaultdict(int)
    alpha, beta = ab2
    for (s2, c2), a2 in amp2.items():
        for (r, c) in _addable(s2):
            c_other = c - r
            f = alpha * D(c_other - c2) + beta
            amp3[(_add(s2, (r, c)), c_other)] += a2 * f

    # Filter out exact zeros to keep sparsity
    result = {k: v for k, v in amp3.items() if v != 0}
    _H3_TRANSITION_CACHE[key] = result
    return result

def chi_all_lambda_reduced_block(word, n: int, *, dps: int = 50, q=None):
    """
    O(A) composition of cached H_3 blocks.
    Replaces the 1-generator-at-a-time loop in chi_monotone_transfer.

    **`n` MUST be divisible by 3 for the fast path**; any other `n` is delegated
    to `chi_monotone_transfer.chi_all_lambda`, which is correct at every `n`.

    Why the guard exists (bean `qou-ym48`, added 2026-08-19). The composition
    below covers generator 0,1 for nucleon 0 and then `3k-1, 3k, 3k+1` for each
    `k` in `1 .. A-1` with `A = n // 3` — that is `2 + 3(A-1)` generators, which
    equals `n - 1` **only when `n == 3A`**. For any other `n` the trailing
    generators are silently skipped and the sweep ends holding shapes of size
    `3 * (n // 3)` instead of `n`, so every `λ ⊢ n` lookup by the caller misses
    and the whole result reads as **zero** — no exception, no warning.

    Measured before the fix, on the EMPTY word where `χ^λ` must be `dim λ`:
    `n = 3` correct, `n = 4` and `n = 5` wrong with `tr_M(1) = 0`, `n = 6`
    correct. The `y_λ` normalisation `Σ y_λ f^λ = 1` makes `tr_M(1) = 1` at every
    `n`, so a zero there is unambiguous.

    Production was never affected — `tr_m_atom_via_transfer` only ever calls this
    at `n = 3(Z+N)` — but the silence was a trap: it turned a correct Markov-step
    check at `H_4` into an apparent `0/0` degeneracy, which came within one step
    of retracting a correct result.
    """
    if mp.mp.dps < dps:
        mp.mp.dps = dps
    if n % 3 != 0:
        # Not the shape this kernel composes. Delegate rather than return zeros.
        return chi_all_lambda(word, n, dps=dps, q=q)
    if q is None:
        q = Q_MP
    qi = 1 / q
    gens = word_to_mpfr(word, q)
    
    gen_ds = defaultdict(list)
    last = -1
    for d_mp, g in gens:
        if g < last:
            raise ValueError(f"non-monotone word: gen {g} after {last}")
        last = g
        gen_ds[g].append(d_mp)
        
    ab = {g: _alpha_beta(ds, q, qi) for g, ds in gen_ds.items()}
    _ident = (0, 1)
    Dc = {1: q, -1: -qi}
    hq = q - qi

    def D(delta: int):
        if delta in Dc:
            return Dc[delta]
        v = hq / (1 - q ** (-2 * delta))
        Dc[delta] = v
        return v

    amp = {((1,), 0): 1}
    
    # Nucleon 0 (First 2 generators: 0 and 1)
    if n >= 3:
        for g in (0, 1):
            new_amp = defaultdict(int)
            alpha, beta = ab.get(g, _ident)
            for (shape, c_this), a in amp.items():
                for (r, c) in _addable(shape):
                    c_other = c - r
                    f = alpha * D(c_other - c_this) + beta
                    new_amp[(_add(shape, (r, c)), c_other)] += a * f
            amp = dict(new_amp)

    # Nucleons k >= 1 (Generators 3k-1, 3k, 3k+1)
    A = n // 3
    for k in range(1, A):
        g0 = 3*k - 1
        g1 = 3*k
        g2 = 3*k + 1
        
        ab0 = ab.get(g0, _ident)
        ab1 = ab.get(g1, _ident)
        ab2 = ab.get(g2, _ident)
        
        new_amp = defaultdict(int)
        for (shape_in, c_in), a_in in amp.items():
            trans = get_h3_transitions(ab0, ab1, ab2, q, qi, shape_in, c_in, Dc)
            for (shape_out, c_out), f in trans.items():
                new_amp[(shape_out, c_out)] += a_in * f
        amp = dict(new_amp)

    out = defaultdict(int)
    for (lam, _c), a in amp.items():
        out[lam] += a
    return dict(out)

if __name__ == "__main__":
    set_compute_dps()
    # Small test on 6Li to benchmark cache reuse
    print("Testing 6Li (A=6)...")
    # `intra_order="grouped"` is REQUIRED here and is not a workaround. This
    # self-test compares `chi_all_lambda` against this module's block
    # accelerator, and BOTH are monotone-only by construction; the production
    # default became the interleaved Borromean word on 2026-09-05 (`7db032fb48`),
    # which neither can compose, so the test refused its own input. Feeding a
    # non-monotone word here would not test the block composition, it would test
    # the guard. The interleaved word's route is `chi_general_word` (bean
    # `qou-wdij`); importing it at module scope would be circular, since it
    # imports this module.
    word = atom_braid_word_3A(3, 3, intra_order="grouped")  # 6Li
    
    t0 = time.time()
    res_orig = chi_all_lambda(word, 18)
    t1 = time.time()
    print(f"Original monotone transfer: {t1-t0:.3f} s")
    
    t0 = time.time()
    res_reduced = chi_all_lambda_reduced_block(word, 18)
    t1 = time.time()
    print(f"Reduced block kernel (cold): {t1-t0:.3f} s")
    
    t0 = time.time()
    res_reduced_warm = chi_all_lambda_reduced_block(word, 18)
    t1 = time.time()
    print(f"Reduced block kernel (warm): {t1-t0:.3f} s")
    
    max_diff = max(abs(res_orig[k] - res_reduced[k]) for k in res_orig)
    print(f"Max absolute difference: {max_diff}")
