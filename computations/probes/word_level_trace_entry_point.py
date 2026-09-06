#!/usr/bin/env python3
"""Word-level Markov-trace entry point, and the test the (Z,N) route cannot do.

WHY THIS EXISTS
---------------
`c1_leading_coefficient_derived_probe.tr_M_series(Z, N, include_inter, P)` is
parameterised by nucleon counts.  Every word it can build has letter census
`Z*(6,3,2) + N*(5,4,2)`, i.e. lies in the cone spanned by the two nucleon
words.  Any hypothesis of the form "the trace's log-derivative is a linear
functional of the letter census" is fitted by two generators and therefore
agrees on that whole cone automatically -- it cannot be tested from (Z,N) data
at any A.

Reading `tr_M_series`, the word is the ONLY channel by which (Z,N) enters:
`crossings` is built, and Z and N are never used again.  So a word-level entry
point is a wrapper, not a rewrite.  This module does NOT modify that probe
(it belongs to qou-pdg9); it imports its internals.

🛑 CONVENTION -- READ BEFORE USING ANY NUMBER FROM THIS MODULE
------------------------------------------------------------
`atom_canonical_crossings` changed its default `intra_order` from `"grouped"`
to `"borromean"` in 7db032fb48 (qou-hu1f, 2026-09-05).  Measured here across
pn / pp / 4He, that change:

    MOVES     f1/f0        37/2, 21, 37      ->  1/2, 3, 1
    MOVES     c1 (Delta tr) 37/16, 19/8, 259/128 -> 1/16, 1/8, 7/128
    PRESERVES c0 (the floor)                 1/8, 1/8, 7/128
    PRESERVES L0, L1 (the LOG-RATIO)         2, 2, 8  and  0, -2, 0

So the docstring claim in that commit -- "Log-RATIO consumers need no change:
the ratio is invariant" -- is CORRECT and was verified here, but it does NOT
cover a DIFFERENCE.  `Delta tr = tr_free - tr_atom` is a difference, so the
whole c_k family is convention-dependent.

This module therefore PINS `intra_order` (see `INTRA_ORDER`) rather than
inheriting a default that can move underneath it.

PRECISION
---------
Everything here is exact: `Ser` carries `fractions.Fraction` coefficients and
the returned log-derivative is a `Fraction`.  No float64 anywhere, no witness
emitted.

USAGE
-----
    from word_level_trace_entry_point import tr_M_series_from_word, log_derivative
    s  = tr_M_series_from_word(crossings, n, P)      # crossings: [(g, kind)]
    ld = log_derivative(crossings, n, P)             # exact Fraction f1/f0
"""
from __future__ import annotations

import importlib.util
import sys
from fractions import Fraction as F
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

_spec = importlib.util.spec_from_file_location(
    "_c1p", _HERE / "c1_leading_coefficient_derived_probe.py")
_c1p = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_c1p)


def tr_M_series_from_word(crossings, n: int, P: int, *, colour_weighted: bool = True):
    """Markov-trace series of an ARBITRARY word.

    `crossings` is a list of `(generator_index, kind)` pairs with kind in
    `canonical_braid_crossings.CTYPES`; `n` is the strand count, which must
    exceed every generator index by at least one.  Returns the probe's `Ser`.

    This is exactly the body of `tr_M_series` with the `atom_canonical_crossings`
    call lifted out, so it agrees with that function by construction on every
    word that function can build -- asserted in `_selftest` below rather than
    assumed.
    """
    q = _c1p.Ser.eps(P)
    facs = _c1p.factors_for(crossings, q, colour_weighted=colour_weighted)
    ys, _ = _c1p.y_lambda_series(n, P)
    tot = _c1p.Ser.const(0)
    for lam in _c1p.two_row_partitions(n):
        tot = tot + ys[tuple(lam)] * _c1p.chi_at(lam, facs, q)
    return tot


def log_derivative(crossings, n: int, P: int = 3) -> F:
    """Exact `f1/f0` -- the first-order logarithmic derivative at q = 1."""
    s = tr_M_series_from_word(crossings, n, P)
    return F(str(s.coeff(1))) / F(str(s.coeff(0)))


# `intra_order` for words built here.  MUST be pinned: `atom_canonical_crossings`
# changed its default from "grouped" to "borromean" in 7db032fb48 (qou-hu1f,
# 2026-09-05), which MOVES every non-ratio quantity -- see the module docstring.
INTRA_ORDER = "grouped"


def _selftest() -> int:
    """Gate: the word-level route must reproduce the (Z,N) route exactly."""
    from canonical_braid_crossings import atom_canonical_crossings
    expect = {(1, 1): F(37, 2), (2, 0): F(21), (0, 2): F(16)}
    bad = []
    for (Z, N), exp in expect.items():
        got = log_derivative(
            atom_canonical_crossings(Z, N, include_inter=False,
                                     intra_order=INTRA_ORDER), 3 * (Z + N), 3)
        print(f"  Z={Z} N={N}  f1/f0 = {got}   expected {exp}   {got == exp}")
        if got != exp:
            bad.append((Z, N, str(got), str(exp)))
    if bad:
        print(f"SELFTEST FAILED: {bad}")
        return 1
    print("SELFTEST OK -- word-level route reproduces the (Z,N) route")
    return 0


if __name__ == "__main__":
    raise SystemExit(_selftest())
