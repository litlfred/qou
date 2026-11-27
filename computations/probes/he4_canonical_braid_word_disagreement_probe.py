#!/usr/bin/env python3
"""Two inequivalent "canonical 4He" braid words, and what phase25 was measuring.

`sublemma_2_1_h12_he4_phase25` reports 0 of 8 partitions verified, with six
residuals at O(1) and only the two one-dimensional irreps agreeing. That was
recorded as a defect in `path_b_chi_h12` (bean qou-matm). It is not.

Established here, in three steps:

1. **The branching is complete.** For all 8 targets,
   `dim lambda == sum_{eta,nu} c^lambda_{eta,nu} * d_eta * d_nu` holds exactly,
   and each eta-class size equals the sum of its ranks. So `_LR_TABLE_9_3` and
   `syt_restriction_shape` are correct.

2. **Path B is exact.** For lambda = (11,1) the H_3 Wedderburn projectors are
   idempotent, of the expected rank, mutually orthogonal, and sum to the
   identity on each eta-class; Path B reproduces `tr(rho_lambda(beta))` with
   defect 0. Path B computes exactly what it claims to.

3. **The two paths use DIFFERENT WORDS.** Path A comes from F1's witness,
   whose parameters record `atom_braid_word_3A(2, 2)`. Path B is computed on
   `he4_braid_canonical()`. Both call themselves canonical 4He at H_12 with 47
   crossings and interfaces pp@gen2 pn@gen5 nn@gen8, and they differ in 36 of
   47 positions.

The dimension split follows, and is the point of this probe. The two words
carry the **identical multiset of (c, d) factors** and the **identical
multiset of generators** -- they are the same letters attached to different
strands, in a different order. On a one-dimensional irrep the character is a
product of scalars, which commute, so any reordering gives the same number. On
dim > 1 the factors are matrices and do not commute. Hence: 2 agree at machine
zero, 6 disagree at O(1), split exactly by dimension, with no defect anywhere
in the branching machinery.

RESOLVED (qou-oppb). `atom_braid_word_3A` is the corpus convention by a wide
margin -- ~220 consumers against the 3 files in this branching cone -- and
substituting it takes phase25 from 0/8 to every partition agreeing with F1 to
its 8-significant-figure storage floor. `he4_braid_canonical` now delegates to
it, and this probe pins the old local word so the divergence stays
reproducible; it exits non-zero if that delegation is ever undone.

PRECISION, and a defect it exposed. The characters are computed with mpmath
end to end at 40 dps. This matters for the CLAIM, not merely for hygiene: the
finding asserts that two of the eight AGREE, and an agreement measured in
float64 cannot be told apart from the arithmetic floor.

The two one-dimensional irreps agree to ~1e-15, NOT to the 40 dps used, and
the reason is CORRECTED here -- see below. `he4_braid_LOCAL_PRE_FIX` computed
its offsets from `pyhecke.gram.H`, which is a Python float, so the old local
word was float64 in its letters. `atom_braid_word_3A` is NOT: it builds `h` and
`delta` inside `workdps(max(dps, 60))` from `Q_50_DIGIT_STR` and
`flavor_split_leading`, and measured against the closed form its `ud` and p-n
offsets have relative error **exactly 0.0** at 60 dps.

    -h    LOCAL -0.20906029879563936547   3A -0.20906029879563931543 (exact)
    -h/2  LOCAL -0.10453014939781968273   3A -0.10453014939781965772 (exact)

So the ~1e-15 agreement on the one-dimensional irreps is the OLD LOCAL word's
float64 error against an exact reference -- one-sided -- not a floor shared by
two flawed constructors. The multiset equality below is an equality to ~5e-17
for the same reason.

RETRACTION. This docstring previously said "**Both** constructors emit offsets
that are float64 underneath ... `atom_braid_word_3A` as an `mpf` built from one,
which is the `mpf(<float>)` pattern `scripts/precision-gates.sh` flags." That is
false, and `mass_at_3A_proper.atom_braid_word_3A` carries a long comment naming
the exact two leaks (`pyhecke.gram.h` being a float; `_avg_color_delta()`
reaching only ~5e-16) as ALREADY FIXED at the source. The error was measuring a
difference between two words and attributing it to both rather than to the one
that moved. It settles the dimension-split question either way -- 1e-15 against
a minimum of 2.34 is fifteen orders of magnitude -- but a one-sided error
reported as a shared floor is a wrong claim, and it was propagated into two
beans, a content block and two PR bodies before being caught.
"""
from __future__ import annotations

import collections
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import _path_bridge  # noqa: F401, E402
import numpy as np  # noqa: E402  (only to read the compiled seminormal entries)
import sympy as sp  # noqa: E402
from mpmath import mp  # noqa: E402

from char_fast import _compiled_sigmas  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from sublemma_2_1_h12_he4_branching import he4_braid_canonical  # noqa: E402
from sublemma_2_1_h9_tritium_verify import (  # noqa: E402
    _proton_body, _neutron_body, H)
from pyhecke.constants import pn_interface_offset_from_h as _pn_d  # noqa: E402


def he4_braid_LOCAL_PRE_FIX() -> list:
    """The word `he4_braid_canonical` built for itself before qou-oppb.

    Reconstructed here rather than imported, because the fix made
    `he4_braid_canonical` delegate to `atom_braid_word_3A` -- so importing it
    would compare the corpus word to itself and this probe would report a
    difference of zero, silently stopping demonstrating the very thing it
    exists to demonstrate. Verbatim from `sublemma_2_1_h12_he4_branching.py`
    as of commit b2028fc3b; this is now a regression pin, not live code.
    """
    word = []
    word.extend(_proton_body())
    word.append((1.0, 0.0, 2))
    word.extend([(c, d, g + 3) for (c, d, g) in _proton_body()])
    word.append((1.0, _pn_d(H), 5))
    word.extend([(c, d, g + 6) for (c, d, g) in _neutron_body()])
    word.append((1.0, -H, 8))
    word.extend([(c, d, g + 9) for (c, d, g) in _neutron_body()])
    return word

mp.dps = 40
Q0 = Q_MP

TARGETS = [(12,), (11, 1), (10, 2), (10, 1, 1),
           (3, 1, 1, 1, 1, 1, 1, 1, 1, 1), (2, 2, 1, 1, 1, 1, 1, 1, 1, 1),
           (2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (1,) * 12]

_QSYM = sp.Symbol("q")


def _sigmas_mp(lam):
    """Seminormal generator matrices for `lam`, as mpmath matrices at Q0."""
    fns, dim = _compiled_sigmas(lam, "double")
    out = []
    for fn in fns:
        arr = fn(Q0)
        arr = arr.toarray() if hasattr(arr, "toarray") else np.asarray(arr)
        M = mp.zeros(dim, dim)
        for i in range(dim):
            for j in range(dim):
                e = arr[i, j]
                M[i, j] = (mp.mpmathify(sp.N(e.subs(_QSYM, Q0), mp.dps))
                           if hasattr(e, "subs") else mp.mpmathify(e))
        out.append(M)
    return out, dim


def chi(word, sig, dim):
    """tr(rho_lambda(word)), accumulated in mpmath."""
    M = mp.eye(dim)
    for c, d, g in word:
        M = M * (sig[g] * mp.mpmathify(c) + mp.eye(dim) * mp.mpmathify(d))
    return sum(M[i, i] for i in range(dim))


def main() -> int:
    w_he4 = he4_braid_LOCAL_PRE_FIX()
    w_3a = atom_braid_word_3A(2, 2)

    live = he4_braid_canonical()
    fixed = (len(live) == len(w_3a)
             and all(a == b for a, b in zip(live, w_3a)))
    print(f"he4_braid_canonical() now delegates to atom_braid_word_3A: {fixed}"
          f"{'' if fixed else '   <-- REGRESSION, the local word is back'}")
    print()
    print(f"he4_braid_LOCAL_PRE_FIX()  {len(w_he4)} letters  (the old local build)")
    print(f"atom_braid_word_3A(2,2)    {len(w_3a)} letters  (the corpus word)")
    if len(w_he4) == len(w_3a):
        n_diff = sum(1 for a, b in zip(w_he4, w_3a)
                     if (mp.mpmathify(a[0]), mp.mpmathify(a[1]), a[2])
                     != (mp.mpmathify(b[0]), mp.mpmathify(b[1]), b[2]))
        print(f"positions differing      {n_diff} of {len(w_he4)}")

    # Compared with a TOLERANCE, by sorting both letter lists and pairing them
    # up. An exact comparison would answer "do these two constructors round
    # identically" (they do not -- see the precision note in the docstring)
    # rather than "are these the same letters", which is the question.
    srt = lambda w: sorted((mp.mpmathify(c), mp.mpmathify(d)) for c, d, _ in w)  # noqa: E731
    pairs = list(zip(srt(w_he4), srt(w_3a)))
    worst = max(max(abs(a[0] - b[0]), abs(a[1] - b[1])) for a, b in pairs)
    gen = lambda w: collections.Counter(g for _, _, g in w)  # noqa: E731
    same_fac = worst < mp.mpf("1e-13")
    same_gen = gen(w_he4) == gen(w_3a)
    print(f"\nsame multiset of (c,d) factors : {same_fac}"
          f"   (max pairwise difference {mp.nstr(worst, 4)}, float64 rounding)")
    print(f"same multiset of generators    : {same_gen}")
    if same_fac and same_gen:
        print("  -> the same letters on different strands, in a different order.")
        print("     Scalars commute; matrices do not. The dimension split below")
        print("     is that fact and nothing else.")

    print(f"\n{'lambda':<30} {'dim':>4} {'chi(he4)':>24} {'chi(3A)':>24} {'rel':>10}")
    print("-" * 96)
    rows = []
    for lam in TARGETS:
        sig, dim = _sigmas_mp(lam)
        a, b = chi(w_he4, sig, dim), chi(w_3a, sig, dim)
        rel = abs(a - b) / max(abs(a), mp.mpf("1e-60"))
        rows.append((lam, dim, a, b, rel))
        print(f"{str(lam):<30} {dim:>4} {mp.nstr(mp.re(a), 16):>24} "
              f"{mp.nstr(mp.re(b), 16):>24} {mp.nstr(rel, 3):>10}")

    ones = [r for r in rows if r[1] == 1]
    many = [r for r in rows if r[1] > 1]
    print(f"\ndim == 1 ({len(ones)}): max rel "
          f"{mp.nstr(max(r[4] for r in ones), 4)}")
    print(f"dim  > 1 ({len(many)}): min rel "
          f"{mp.nstr(min(r[4] for r in many), 4)}")
    print("\nThe gap between those two lines is the whole finding.")
    print()
    print("RESOLVED (qou-oppb): he4_braid_canonical now returns the corpus word,")
    print("and phase25 goes 0/8 -> every partition agreeing with F1's cached")
    print("character to its 8-significant-figure storage floor (5e-9 to 4.8e-8).")
    print("It still prints 0/8 because its pass threshold is rel < 1e-9, which is")
    print("unmeetable against an 8-sig-fig upstream -- that threshold measures F1's")
    print("serialization, not the mathematics, and was deliberately NOT widened.")
    return 0 if fixed else 1


if __name__ == "__main__":
    raise SystemExit(main())
