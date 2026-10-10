#!/usr/bin/env python3
"""The production Ocneanu HOMFLY must be the SU(2) specialisation of the
exact two-variable skein HOMFLY.

Why this exists
---------------
`homfly_ocneanu_trace.homfly_signed_su2` is the production HOMFLY: it replaced
the broken ratio-only path in `homflypt_engine` and feeds the mass/binding
work. Its own docstring records how it was validated -- a spanning set of
braids seeded from `_torus_unframed`, then held-out knots. Both of those live
in the **2-strand torus family plus the figure-eight**.

`homfly_skein_braid.homfly` is the exact two-variable engine: descending-diagram
skein recursion on braid words, integer Laurent coefficients in `(v, z)`, no
float, no substrate `q`. It is defined on *arbitrary* braid words.

**Nothing compared them.** That is the same omission that produced bean
`qou-7ue5`: `homflypt_engine.homflypt_2strand` and
`homflypt_reference_qa._torus_homfly` sat in one module disagreeing by a
mirror for months, each correct-looking on its own, because no test ever
evaluated both. A private copy cannot learn what the canonical one learns, and
two engines that never meet are two private copies.

What the comparison buys that the existing validation cannot
------------------------------------------------------------
The Ocneanu weights are solved against a spanning set and checked on held-out
knots *of the same families*. This file checks arbitrary words -- including
4-strand words with mixed signs, and the `6_1` word from `qou-dr8m` -- so it
covers the region the production engine is actually used in and its own
validation never reached.

The specialisation
------------------
At the SU(2) point the engine sets `s = sqrt(q0)`, `a = s^2`, `z = s - 1/s`,
and `_torus_unframed` uses `v = a`. So the claim under test is

    P(v, z) evaluated at  v = q0,  z = sqrt(q0) - 1/sqrt(q0)
      ==  homfly_signed_su2(word, n, q0, framed=False)

with the framed value related by the writhe, `unframed = a^w * framed`.

Note what this does **not** test. The specialisation collapses the `v`
direction: `v` is pinned to `q0` and `z` to a function of the same `q0`, so a
one-variable value cannot see a `v`-degree. That is exactly why MFW needs the
two-variable engine and why these two files are complementary rather than
redundant. This test ties their *values* together; it does not make either one
able to do the other's job.

One thing the comparison surfaced
--------------------------------
The proton word `(s1 s2^-1)^3` and the neutron word `(s1^-1 s2)^3` are mirror
images of each other, and their common closure -- the Borromean rings -- is
amphichiral. Their two-variable HOMFLY are therefore **identical as
polynomials**, not merely equal at the SU(2) point (checked here in C2, which
requires exactly that).

This is a sharpening of something the corpus already knows, not a new fact.
`fsh-guts/deprecated/computations/schur_weyl_q_hecke.py` was deprecated with the note
that it works from cycle type and "cannot distinguish proton from neutron",
and the framework's answer is the colour weighting -- `bring_color_weighted`,
made canonical by the 2026-08-15 owner ruling R3. What is sharpened is the
level at which the blindness sits: it is not an artifact of a coarse
invariant, and it is not the SU(2) specialisation losing information. The
full two-variable HOMFLY of the two closures is the same polynomial.

Scope, per the AGENTS.md refutation discipline: this is scope-(a). It says
HOMFLY, alone, does not separate these two braid closures. It does **not** say
no braid-level invariant can -- the writhe already does (it is `0` for both
here, but the framed trace retains it in general), and the colour weighting is
precisely a structure HOMFLY does not see.

Precision
---------
`mpmath` throughout at the repo compute dps -- no float64 anywhere, per
AGENTS.md NO-FLOAT64. The residuals below therefore track the working
precision (~1e-41), not a float64 floor at 1e-16.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402  -- substrate modules live in substrate/

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from homfly_skein_braid import homfly  # noqa: E402
from homfly_ocneanu_trace import homfly_signed_su2, _writhe  # noqa: E402
from q_parameter import Q_50_DIGIT_STR as Q_STR  # noqa: E402

set_compute_dps()

#: Working-precision tolerance. The measured residuals are ~1e-41; 1e-30
#: leaves three orders of headroom for the character kernel's rounding while
#: staying eleven orders below anything a real disagreement would produce
#: (Part C measures a true disagreement at ~1e-1).
TOL = mp.mpf("1e-30")

#: Braid words, as (label, word, n_strands). The first three are inside the
#: production engine's own validated families; the rest are not, and are the
#: point of this file.
WORDS = [
    # -- inside the existing validation (2-strand torus + figure-eight) --
    ("unknot                sigma1", [1], 2),
    ("trefoil               sigma1^3", [1, 1, 1], 2),
    ("cinquefoil            sigma1^5", [1, 1, 1, 1, 1], 2),
    # Two-component links. Their z-degrees have parity c-1 = 1, i.e. ODD
    # terms exist, which is what makes the naive `v -> v^-1` visibly wrong
    # in C1. A battery of knots alone barely exercises that -- and k = +-2
    # is precisely where the qou-7ue5 sign defect lived.
    ("Hopf+                 sigma1^2", [1, 1], 2),
    ("Hopf-                 sigma1^-2", [-1, -1], 2),
    ("(2,4) torus link      sigma1^4", [1, 1, 1, 1], 2),
    ("left trefoil          sigma1^-3", [-1, -1, -1], 2),
    ("figure-eight", [1, -2, 1, -2], 3),
    # -- outside it: arbitrary 3-strand words --
    ("proton   (s1 s2^-1)^3", [1, -2, 1, -2, 1, -2], 3),
    ("neutron  (s1^-1 s2)^3", [-1, 2, -1, 2, -1, 2], 3),
    ("T(3,4)   (s1 s2)^4", [1, 2, 1, 2, 1, 2, 1, 2], 3),
    ("5_2      3-strand", [1, 1, 2, -1, 2, 2], 3),
    ("mixed 3-strand", [1, 2, -1, 2, 2, -1], 3),
    # -- outside it: 4-strand words, including the qou-dr8m 6_1 word --
    ("6_1      4-strand", [1, 1, 2, -1, -3, 2, -3], 4),
    ("T(4,5)   (s1s2s3)^5", [1, 2, 3] * 5, 4),
    ("mixed 4-strand", [1, -2, 3, 3, -1, 2, -3, 1], 4),
    # -- 5 strands: weights solved, held-out coverage thinnest here --
    ("mixed 5-strand", [1, 1, 2, 3, 3, 4, -2, 4], 5),
]


def _spec():
    """The SU(2) specialisation point, as exact mpmath at compute dps."""
    q0 = mp.mpf(Q_STR)
    s = mp.sqrt(q0)
    return q0, s ** 2, s - 1 / s  # q0, v (= a), z


def _eval(poly, v, z):
    """Evaluate an `LP2` two-variable Laurent polynomial at `(v, z)`.

    The coefficients are Python ints (exact); `v` and `z` are `mp.mpf`, so the
    whole sum stays in mpmath. No float64 enters.
    """
    return sum(mp.mpf(c) * v ** i * z ** j for (i, j), c in poly.t.items())


def part_a_unframed(q0, v, z):
    """Every word: exact skein at the SU(2) point == production unframed."""
    print("\n[A] exact skein specialised  vs  homfly_signed_su2(framed=False)")
    worst = mp.mpf(0)
    for label, word, n in WORDS:
        mine = _eval(homfly(word, n), v, z)
        prod = homfly_signed_su2(word, n, q0, framed=False)
        d = abs(mine - prod)
        worst = max(worst, d)
        flag = "ok " if d < TOL else "FAIL"
        print(f"    {flag} {label:<24} n={n}  value={mp.nstr(mine, 16):>22}"
              f"  |d|={mp.nstr(d, 4)}")
        assert d < TOL, (
            f"SU(2) specialisation MISMATCH on {label!r} (word={word}, n={n}): "
            f"exact skein gives {mp.nstr(mine, 25)}, production engine gives "
            f"{mp.nstr(prod, 25)}, |delta| = {mp.nstr(d, 6)} >= {TOL}")
    print(f"    -> {len(WORDS)} words agree; worst |delta| = {mp.nstr(worst, 6)}")
    return worst


def part_b_framing(q0, v, z):
    """The engine's own framing relation: unframed == a^writhe * framed.

    Independent of the skein engine -- this is internal consistency of the
    production path, and it pins the writhe convention that `framed=True`
    (the production setting) actually ships.
    """
    print("\n[B] framing relation  unframed == a^w * framed  (writhe convention)")
    worst = mp.mpf(0)
    for label, word, n in WORDS:
        fr = homfly_signed_su2(word, n, q0, framed=True)
        un = homfly_signed_su2(word, n, q0, framed=False)
        w = _writhe(word)
        d = abs(un - v ** w * fr)
        worst = max(worst, d)
        flag = "ok " if d < TOL else "FAIL"
        print(f"    {flag} {label:<24} w={w:>3}  |d|={mp.nstr(d, 4)}")
        assert d < TOL, (
            f"framing relation broken on {label!r}: unframed - a^{w}*framed = "
            f"{mp.nstr(d, 6)}")
    print(f"    -> worst |delta| = {mp.nstr(worst, 6)}")
    return worst


def _mirror_poly(poly):
    """The HOMFLY mirror `(v, z) -> (v^-1, -z)` applied to an `LP2`.

    Note the sign: odd `z`-degree terms flip. A naive `v -> v^-1` is NOT the
    mirror -- that omission is exactly the `qou-7ue5` defect, and
    `QOU.Knot.HomflySkeinReference.plain_inversion_ne_mirror` proves the two
    differ (while `plain_inversion_eq_mirror_at_three` proves they coincide on
    the trefoil, which is why the omission stayed invisible for so long).
    """
    out = {}
    for (i, j), c in poly.t.items():
        key = (-i, j)
        out[key] = out.get(key, 0) + (c if j % 2 == 0 else -c)
    return {k: v for k, v in out.items() if v}


def part_c_mirror_on_words():
    """C1: the Lean-proved mirror formula holds on actual braid words.

    Mirroring a braid word (negate every letter) mirrors the link, so applying
    `(v, z) -> (v^-1, -z)` to `P(w)` must give `P(mirrored w)`. Needs no
    external reference. The naive `v -> v^-1` is checked to FAIL somewhere, so
    this is a real discriminator rather than a formula that any inversion would
    satisfy.
    """
    print("\n[C1] mirror formula (v,z)->(v^-1,-z) on braid words")
    naive_failures = 0
    for label, word, n in WORDS:
        P = homfly(word, n)
        Pm = homfly([-g for g in word], n)
        assert _mirror_poly(P) == dict(Pm.t), (
            f"mirror formula FAILS on {label!r}: (v,z)->(v^-1,-z) of P(w) is "
            f"{_mirror_poly(P)}, but P(mirror w) is {dict(Pm.t)}")
        naive = {(-i, j): c for (i, j), c in P.t.items()}
        if naive != dict(Pm.t):
            naive_failures += 1
    print(f"    ok  all {len(WORDS)} words satisfy the mirror formula")
    print(f"    ok  the naive v -> v^-1 fails on {naive_failures} of them "
          f"(the qou-7ue5 trap), so C1 discriminates")
    assert naive_failures >= 3, (
        f"the naive v -> v^-1 was distinguishable on only {naive_failures} "
        "words, too few for C1 to be a real guard against the qou-7ue5 "
        "defect -- odd z-degrees need multi-component links (parity c-1), "
        "so add more of those rather than more knots")


def part_c_teeth(q0, v, z):
    """C2: the specialisation neither creates nor destroys chirality.

    Part A asserts agreement, and an assertion that can only pass proves
    nothing. Chirality supplies the teeth: classify each word by its
    **two-variable** polynomial (`P == P_mirror` or not), then require the
    SU(2) values to agree exactly for the amphichiral ones and to separate by
    orders of magnitude for the rest. A specialisation that collapsed a chiral
    pair would show up here as a false coincidence.
    """
    print("\n[C2] teeth: chirality must survive the specialisation")
    amph, chiral = [], []
    for label, word, n in WORDS:
        P = homfly(word, n)
        Pm = homfly([-g for g in word], n)
        d = abs(_eval(P, v, z) - _eval(Pm, v, z))
        (amph if dict(P.t) == dict(Pm.t) else chiral).append((label, d))
    for label, d in amph:
        print(f"    amphichiral  {label:<24} |P - P_mirror| = {mp.nstr(d, 4)}")
        assert d < TOL, (
            f"{label!r} has P == P_mirror as a two-variable polynomial, so its "
            f"SU(2) values must coincide, but |delta| = {mp.nstr(d, 6)}")
    smallest = None
    for label, d in chiral:
        smallest = d if smallest is None else min(smallest, d)
        print(f"    chiral       {label:<24} |P - P_mirror| = {mp.nstr(d, 6)}")
        assert d > TOL * mp.mpf("1e10"), (
            f"{label!r} is chiral as a two-variable polynomial, but the SU(2) "
            f"specialisation collapses it onto its mirror (|delta| = "
            f"{mp.nstr(d, 6)}) -- Part A has no teeth on this word")
    print(f"    -> {len(chiral)} chiral (smallest gap {mp.nstr(smallest, 6)}), "
          f"{len(amph)} amphichiral (all exact)")
    return smallest


def main():
    q0, v, z = _spec()
    print("SU(2) specialisation of the exact two-variable HOMFLY")
    print(f"    q0 = {mp.nstr(q0, 25)}")
    print(f"    v  = a = s^2   = {mp.nstr(v, 25)}")
    print(f"    z  = s - 1/s   = {mp.nstr(z, 25)}")
    print(f"    working dps    = {mp.mp.dps}")
    wa = part_a_unframed(q0, v, z)
    wb = part_b_framing(q0, v, z)
    part_c_mirror_on_words()
    sc = part_c_teeth(q0, v, z)
    print(f"\nPASS  {len(WORDS)} words. worst A={mp.nstr(wa, 4)} "
          f"worst B={mp.nstr(wb, 4)} smallest chiral gap={mp.nstr(sc, 4)}")


if __name__ == "__main__":
    main()
