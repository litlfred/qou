#!/usr/bin/env python3
"""Guard: `word_to_mpfr`'s template classifier must be SCALE-FREE in `h`.

WHY THIS EXISTS (bean `qou-v1cp`)
---------------------------------
`chi_monotone_transfer.word_to_mpfr` re-lifts a braid word's float `d` to full
dps by matching it against the four recognised crossing templates

    0            (sigma)
    -h           (sigma inverse)
    -h/2         (averaged)
    -h*(1/2 - delta/4)   (color-weighted p-n, one per live delta convention)

with `h = q - 1/q = 2*sinh(eta)`.  **Every template but the first is
proportional to `h`, which goes to zero as q goes to 1.**  The original
classifier tested each template in a fixed order against an ABSOLUTE
threshold `_TOL = 1e-9`, so once `|h| < _TOL` every template lay within `_TOL`
of every crossing and the first test won for the whole word: every `d` was
lifted to exactly 0.

The consequence was not an exception. `tr_m_atom_zn` returned plausible
numbers with the three nucleon flavours (pp / pn / nn) collapsed onto one
value, silently, below eta ~ 1e-10.  The count of distinct lifted `d` fell
3 -> 2 -> 1 exactly where `h/2` and then `h` crossed 1e-9.

WHAT THIS ASSERTS
-----------------
1. Distinct templates stay distinct at eta far below `_TOL`.  This is the
   direct regression: it fails on the pre-fix classifier.
2. The pp / nn flavour split is nonzero and scales linearly in eta over
   ten decades.  A classifier that flattens templates makes this exactly 0,
   which is what made the defect invisible -- 0.0 reads as "these are equal",
   not as "the difference was destroyed".
3. Production q0 is untouched.  At q0 the templates are separated by ~7.5e-5,
   four orders above `_TOL`, so nearest-match and first-within-tolerance agree
   and the recorded atom traces are unchanged.

NO FLOAT64: every comparison below is mpmath.  The only floats are the ones
`word_to_mpfr` itself uses as a classifier key, which is what is under test.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402

from chi_monotone_transfer import word_to_mpfr, _TOL  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from reduced_block_kernel import chi_all_lambda_reduced_block  # noqa: E402
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from tr_m_atom_via_transfer import _trM, tr_m_atom_zn  # noqa: E402

# Recorded at 90 dps on `main` BEFORE the classifier fix, and reproduced
# byte-identically after it. These are the gate on "production is untouched".
_PRODUCTION = {
    "D":   ("0.575172243917771870826535343986", "1.13171690432221008273130756812"),
    "T":   ("0.229310102104556507332090810269", "1.11784622897822657732834138483"),
    "3He": ("0.403767036851428170368670253333", "1.29667561224494401773789929523"),
    "4He": ("0.160974145442407381825873440981", "1.28078315152864641063633786713"),
}
_ZN = {"D": (1, 1), "T": (1, 2), "3He": (2, 1), "4He": (2, 2)}


def _split(eta: "mp.mpf"):
    """(#distinct lifted d for the pp word, tr_M(pp) - tr_M(nn)) at q = exp(eta)."""
    q = mp.exp(eta)
    n_distinct = len({
        mp.nstr(d, 50)
        for d, _g in word_to_mpfr(atom_braid_word_3A(2, 0, include_inter=True, q=q), q)
    })
    y = {tuple(k): mp.mpf(str(v)) for k, v in y_lambda_at(6, q).items()}
    t = [
        _trM(chi_all_lambda_reduced_block(
            atom_braid_word_3A(Z, N, include_inter=True, q=q), 6, q=q), y)
        for Z, N in ((2, 0), (0, 2))
    ]
    return n_distinct, t[0] - t[1]


def main() -> int:
    mp.mp.dps = 90
    fails = []

    # (1) + (2): templates stay distinct, and the split stays linear, well
    # below the absolute tolerance that used to flatten them.
    print(f"_TOL = {_TOL}  (absolute; h = 2*sinh(eta) crosses it near eta = 5e-10)\n")
    print(f"{'eta':>8} {'#distinct d':>12} {'tr_M(pp)-tr_M(nn)':>24} {'ratio/eta':>14}")
    for e in ("1e-3", "1e-7", "1e-9", "5e-10", "1e-10", "1e-13", "1e-20"):
        eta = mp.mpf(e)
        nd, d = _split(eta)
        ratio = d / eta
        print(f"{e:>8} {nd:>12} {mp.nstr(d, 12):>24} {mp.nstr(ratio, 10):>14}")
        if nd != 3:
            fails.append(f"eta={e}: {nd} distinct templates, want 3 "
                         "(classifier flattened them)")
        if d == 0:
            fails.append(f"eta={e}: pp/nn flavour split is exactly 0 "
                         "(the silent-collapse signature)")
        # The split is linear in eta to leading order; the coefficient is a
        # property of the words, not of eta. Assert it is stable rather than
        # pinning its value, so a legitimate change to the braid convention
        # moves it without failing this audit.
        if not (mp.mpf("1.1") < ratio < mp.mpf("1.2")):
            fails.append(f"eta={e}: (pp-nn)/eta = {mp.nstr(ratio, 10)} "
                         "outside [1.1, 1.2] — the split is no longer linear")

    # (3) production q0 untouched.
    print("\nproduction q0 (default pin, default dps):")
    for name, (a_want, f_want) in _PRODUCTION.items():
        Z, N = _ZN[name]
        ta, tf, _, _ = tr_m_atom_zn(Z, N)
        a_got, f_got = mp.nstr(ta, 30), mp.nstr(tf, 30)
        ok = (a_got == a_want and f_got == f_want)
        print(f"  {name:>4}  {'OK ' if ok else 'MOVED'}  atom={a_got}  free={f_got}")
        if not ok:
            fails.append(f"{name}: atom {a_got} != {a_want} or free {f_got} != {f_want}")

    print()
    if fails:
        for f in fails:
            print(f"  FAIL  {f}")
        return 1
    print("PASS — templates scale-free, flavour split linear, production unchanged.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
