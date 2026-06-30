#!/usr/bin/env python3
"""b0vf — averaged-crossing per-λ χ via {σ, drop} branch decomposition.

The Hoefsmit producer (`chi_at_q0_via_hoefsmit_mpfr.py`) computes
χ^λ(W) where W is the atomic braid word as a product of Hecke factors
`c·σ_g + d·I` (c=1; d ∈ {0, -h, -h/2, -h(½-δ/4)}).  The pure-Python
seminormal trace is O(dim²·|W|) per partition → multi-week for the big
λ ⊢ 12 of ⁴He.

This module instead uses the EXACT linear-algebra identity that each
factor `σ_g + d·I` is, in the Hecke algebra:

    d = 0          →  σ_g                    (positive crossing)
    d = -h         →  σ_g - h·I = σ_g^{-1}   (negative crossing; Hecke
                                              identity σ^{-1}=σ-h)
    d = -h/2       →  σ_g - (h/2)·I          (averaged = (σ+σ^{-1})/2)
    d = -h(½-δ/4)  →  σ_g - c·I              (colour-weighted averaged)

Only the last two are genuine 2-branch {keep σ_g (coeff 1), drop to I
(coeff d)} linear combinations.  By multilinearity of the character,

    χ^λ(W) = Σ_{branches} (Π coeff) · χ^λ(signed-braid-word)

where each branch's word is a pure signed braid word fed to the
canonical Rust kernel `pyhecke_native.chi_lambda_all_partitions_mpfr`
(correct at q≠1 — the Hoefsmit seminormal character).  #branches =
2^(#mixed crossings); for ⁴He that is 2^9 = 512 (not 2^24).

This file is a VALIDATION harness: it reproduces a complete witness
(deuteron by default) and diffs per-λ.  No witness is written here.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401
import itertools
import json
import sys
import time
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))

import pyhecke_native as pn  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402


def prepared_word(Z: int, N: int, q_str: str):
    """Replicate chi_at_q0_via_hoefsmit_mpfr.build_chi_cache_at_q0's word
    preparation, including the colour-weighted δ→mpf upgrade."""
    word = atom_braid_word_3A(Z, N)
    try:
        from canonical_braid_crossings import _avg_color_delta
        _qm = mp.mpf(q_str)
        _hm = _qm - mp.mpf(1) / _qm
        _cw_d = -_hm * (mp.mpf(1) / 2 - _avg_color_delta() / 4)
        _cw_f64 = float(_cw_d)
        word = [(c, _cw_d if abs(float(d) - _cw_f64) < 1e-9 else d, g)
                for (c, d, g) in word]
    except Exception:
        pass
    return word


def classify(word, q):
    """Tag each (c,d,g) crossing.

    The Rust kernel encodes a crossing as (sign, g1) with sign ∈
    {1: σ, -1: σ^{-1}, 0: averaged (σ+σ^{-1})/2 = σ - h/2·I}.  These
    three are passed through directly.  The colour-weighted crossing
    d = -h(½-δ/4) is NOT one of the three, so it becomes a 2-branch
    {keep σ_g (sign 1, coeff 1), drop to I (coeff d_mp)} mix tag.

    Returns a tagged list in source order:
      ('fix', (sign, g1)) | ('mix', g1, d_mp)
    """
    h = q - mp.mpf(1) / q
    tol = mp.mpf("1e-10")  # matches _word_to_signed inter-class gap
    tagged = []
    for (c, d, g) in word:
        assert abs(mp.mpf(str(c)) - 1) < 1e-12, f"c={c} != 1 unsupported"
        d_mp = d if isinstance(d, mp.mpf) else mp.mpf(str(d))
        g1 = int(g) + 1
        if abs(d_mp) < tol:
            tagged.append(('fix', (1, g1)))               # σ_g
        elif abs(d_mp + h) < tol:
            tagged.append(('fix', (-1, g1)))              # σ_g^{-1}
        elif abs(d_mp + h / 2) < tol:
            tagged.append(('fix', (0, g1)))               # averaged
        else:
            tagged.append(('mix', g1, d_mp))              # colour-weighted
    return tagged


def chi_by_branch(Z, N, q_str, dps=50, verbose=True):
    q = mp.mpf(q_str)
    n = 3 * (Z + N)
    word = prepared_word(Z, N, q_str)
    tagged = classify(word, q)
    mixed_idx = [i for i, t in enumerate(tagged) if t[0] == 'mix']
    k = len(mixed_idx)
    if verbose:
        print(f"  n={n} |W|={len(word)} fixed={len(word)-k} mixed={k} "
              f"→ {2**k} branches", flush=True)
    chi_total: dict[tuple, mp.mpf] = {}
    t0 = time.time()
    for b, signs in enumerate(itertools.product([1, 0], repeat=k)):
        # signs[j]=1 → keep σ_g (coeff 1); 0 → drop to I (coeff d_mp)
        coeff = mp.mpf(1)
        bword = []
        si = 0
        for t in tagged:
            if t[0] == 'fix':
                bword.append(t[1])
            else:
                _, g1, d_mp = t
                if signs[si] == 1:
                    bword.append((1, g1))     # keep σ_g
                else:
                    coeff *= d_mp             # drop to identity
                si += 1
        if coeff == 0:
            continue
        out = pn.chi_lambda_all_partitions_mpfr(n, bword, q_str, dps)
        for lam, s in out:
            key = tuple(lam)
            chi_total[key] = chi_total.get(key, mp.mpf(0)) + coeff * mp.mpf(s)
        if verbose and (b + 1) % 64 == 0:
            print(f"    branch {b+1}/{2**k}  {time.time()-t0:.1f}s", flush=True)
    if verbose:
        print(f"  done {2**k} branches in {time.time()-t0:.1f}s", flush=True)
    return chi_total, n


def validate(atom_label, Z, N, witness_name):
    w = json.load(open(HERE / witness_name))
    q_str = w["q_0_50dps"]
    mp.mp.dps = 60
    chi_total, n = chi_by_branch(Z, N, q_str, dps=50)
    stored = {tuple(e["partition"]): mp.mpf(e["chi_lambda"])
              for e in w["by_partition"]}
    worst = mp.mpf(0)
    nbad = 0
    for lam, cs in sorted(stored.items()):
        got = chi_total.get(lam)
        if got is None:
            print(f"  MISSING {lam}")
            nbad += 1
            continue
        rel = abs(got - cs) / (abs(cs) if cs != 0 else mp.mpf(1))
        worst = max(worst, rel)
        if rel > mp.mpf(10) ** (-40):
            nbad += 1
            print(f"  λ={lam}: stored={mp.nstr(cs,20)} got={mp.nstr(got,20)} rel={mp.nstr(rel,3)}")
    # scalar tr_M cross-check
    print(f"  [{atom_label}] {len(stored)} partitions compared, "
          f"worst rel-err = {mp.nstr(worst,4)}, n_bad(>1e-40)={nbad}")
    return worst, nbad


if __name__ == "__main__":
    print("=== DEUTERON validation (11 partitions, complete witness) ===")
    validate("deuteron", 1, 1, "chi-deuteron-h6-at-q0-50dps.witness.json")


def he4_full_check():
    """Compute all 77 ⁴He per-λ χ at the muon pin; cross-check the 27
    known partitions vs the partial witness AND Σ y_λ χ_λ vs markov-peel."""
    import time as _t
    pw = json.load(open(HERE / "chi-helium-4-h12-at-q0-50dps.witness.json"))
    q_str = pw["q_0_50dps"]
    mp.mp.dps = 60
    print(f"=== ⁴He all-77 via branch decomposition (q0={q_str[:18]}…) ===")
    t0 = _t.time()
    chi_total, n = chi_by_branch(2, 2, q_str, dps=50)
    print(f"  computed {len(chi_total)} partitions in {_t.time()-t0:.1f}s")
    # cross-check 27 known
    stored = {tuple(e["partition"]): mp.mpf(e["chi_lambda"])
              for e in pw["by_partition"]}
    worst = mp.mpf(0)
    for lam, cs in stored.items():
        got = chi_total[lam]
        rel = abs(got - cs) / (abs(cs) if cs != 0 else mp.mpf(1))
        worst = max(worst, rel)
    print(f"  27 known partitions: worst rel-err = {mp.nstr(worst,4)}")
    # full Σ y_λ χ_λ vs markov-peel
    from tr_m_wenzl_bridge_mpfr import _load_y_lambda
    y = _load_y_lambda(12, None)
    s = mp.mpf(0)
    for lam, chi in chi_total.items():
        s += mp.mpf(str(y[lam])) * chi
    mpv = mp.mpf("0.055358426266783106469852047498437740316331036735298")
    print(f"  Σ y_λ χ_λ (77/77)      = {mp.nstr(s,30)}")
    print(f"  markov-peel (complete) = {mp.nstr(mpv,30)}")
    print(f"  rel gap vs markov-peel = {mp.nstr(abs(s-mpv)/abs(mpv),4)}")
    partial_sum = mp.mpf(pw["tr_M_at_q0"])
    print(f"  (old 27/77 partial     = {mp.nstr(partial_sum,30)}, "
          f"gap {mp.nstr(abs(partial_sum-mpv)/abs(mpv),3)})")
    return chi_total, s
