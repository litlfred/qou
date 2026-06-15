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
from q_parameter import Q_50_DIGIT_STR
import time

# Module-level cache keyed by:
# (ab0, ab1, ab2, shape_in, c_in) -> dict of (shape_out, c_out) -> amplitude
_H3_TRANSITION_CACHE = {}

def get_h3_transitions(ab0, ab1, ab2, q, qi, shape_in, c_in, Dc):
    """
    Compute and cache the 3-step fine-Bratteli transitions for a single nucleon (3 generators).
    The nucleon type is effectively defined by the alpha/beta tuples (ab0, ab1, ab2).
    """
    key = (ab0, ab1, ab2, shape_in, c_in)
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
    amp1 = defaultdict(mp.mpf)
    alpha, beta = ab0
    for (r, c) in _addable(shape_in):
        c_other = c - r
        f = alpha * D(c_other - c_in) + beta
        amp1[(_add(shape_in, (r, c)), c_other)] += f

    # Step 2: ab1 (Internal 1)
    amp2 = defaultdict(mp.mpf)
    alpha, beta = ab1
    for (s1, c1), a1 in amp1.items():
        for (r, c) in _addable(s1):
            c_other = c - r
            f = alpha * D(c_other - c1) + beta
            amp2[(_add(s1, (r, c)), c_other)] += a1 * f

    # Step 3: ab2 (Internal 2)
    amp3 = defaultdict(mp.mpf)
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
    """
    if mp.mp.dps < dps:
        mp.mp.dps = dps
    if q is None:
        q = mp.mpf(Q_50_DIGIT_STR)
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
    _ident = (mp.mpf(0), mp.mpf(1))
    Dc = {1: q, -1: -qi}
    hq = q - qi

    def D(delta: int):
        if delta in Dc:
            return Dc[delta]
        v = hq / (1 - q ** (-2 * delta))
        Dc[delta] = v
        return v

    amp = {((1,), 0): mp.mpf(1)}
    
    # Nucleon 0 (First 2 generators: 0 and 1)
    if n >= 3:
        for g in (0, 1):
            new_amp = defaultdict(mp.mpf)
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
        
        new_amp = defaultdict(mp.mpf)
        for (shape_in, c_in), a_in in amp.items():
            trans = get_h3_transitions(ab0, ab1, ab2, q, qi, shape_in, c_in, Dc)
            for (shape_out, c_out), f in trans.items():
                new_amp[(shape_out, c_out)] += a_in * f
        amp = dict(new_amp)

    out = defaultdict(mp.mpf)
    for (lam, _c), a in amp.items():
        out[lam] += a
    return dict(out)

if __name__ == "__main__":
    mp.mp.dps = 50
    # Small test on 6Li to benchmark cache reuse
    print("Testing 6Li (A=6)...")
    word = atom_braid_word_3A(3, 3) # 6Li
    
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
