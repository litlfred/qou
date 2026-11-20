#!/usr/bin/env python3
"""regular_rep_modulus_spread_probe — RETRACTS a second claim of mine from the
same PR, and the retraction is the one that matters: `|det| = 1` does NOT close
a block of dimension > 2, so the `R <= 1` bound does not extend past the
2-dimensional case at all.

Bean `qou-brng`, arc `bk-crossing-mass-binding`.  Corrects section [3c] of
`irrep_determinant_escape_probe`, which is itself the correction to
`channel_asymmetry_letter_family_bound_probe` section [6].  Three layers of the
same over-generalisation, and this is the one that reaches the physics.

## THE RETRACTION

`irrep_determinant_escape_probe` [3c] says of the block `(3,2,1)`:

    "in (3,2,1) EVERY braid word has |det| = 1 regardless of writhe -- the
     R <= 1 argument closes that block outright"

**The first clause is true; the second does not follow.**  `R <= 1` was derived
for a 2x2 matrix, where

    log|l_1| + log|l_2| = log|det|

is ONE equation on TWO unknowns and therefore pins their ratio.  In dimension
`d` it is one equation on `d` unknowns, leaving `d - 2` free directions.  For
`d = 16` -- which is `dim (3,2,1)` -- it constrains almost nothing.  Fixing the
determinant does not fix a ratio of log-moduli unless there are only two of
them.

## THE DEMONSTRATION, in the 6-dim regular representation of H_3

Built from the multiplication table on the basis
`{1, s1, s2, s1s2, s2s1, s1s2s1}` -- canonical, no convention choices, and the
Hecke quadratic and braid relation are asserted rather than assumed.  Every
word below has `|det| = 1`:

    word          moduli                                            ratio
    s1            q,q,q,1/q,1/q,1/q                                   1.0
    s1*s2         q^2, 1,1,1,1, 1/q^2                                 1.0
    s1*s2*s1      q^3, 1,1,1,1, 1/q^3                                 1.0
    s1^2 s2^2     q^4, q^2,q^2, 1/q^2,1/q^2, 1/q^4                    2.0   <--
    s1^3 s2^-2    1.52775, 1.52775, q, 1/q, 0.654558, 0.654558       4.06   <--

So a braid word with `|det| = 1` reaches a log-modulus ratio of **exactly 2**,
and with mixed signs **4.06**.  `|det| = 1` does not close the block.

## 🛑 THE NEAR-MISS, and it is the reason this probe exists

My first test of this was the three words `s1`, `s1*s2`, `s1*s2*s1`.  All three
returned ratio **exactly 1.0**, and on that evidence I was about to conclude
that the determinant lock does hold in higher dimensions after all -- i.e. to
**retract a correct correction** on three data points.

Those three words are not representative: their 2-dimensional block happens to
be elliptic (eigenvalues on the unit circle), which is why four of the six
moduli read exactly `1.0`.  Adding one more crossing (`s1^2 s2^2`) breaks it
immediately.

That is the same defect as the two it was correcting -- a general claim tested
against a set that could not falsify it -- reached a third time in one session,
in the act of checking the second.  The lesson is not "test more words"; it is
that **a negative from a small hand-picked set is not evidence**, and the
session's own history is the argument for it.

## HOW FAR IT REACHES — 5.0, and it does NOT reach 22.25

Enumerating all 5456 words of length <= 6 in `{s1, s1^-1, s2, s2^-1}`, with
every word's roots resolved (0 unresolved, counted and reported):

    best log-modulus ratio = 5.0   at  abaab       nature needs ~ 33.7055

## 🛑 THE FIGURE THIS PROBE ALMOST REPORTED INSTEAD

With the near-unit floor set at `1e-15`, that same enumeration returned
**7752455236.0** at `AABAAB`, and the summary line read *"reaches 33.7:
True"*.  It is an artefact.  Four of `AABAAB`'s six moduli are `1` to within
`8.08e-11` -- exactly 1 as algebra, numerical dust as arithmetic, from a
repeated characteristic-polynomial root -- so the ratio was dividing a genuine
log-modulus by that dust.  The floor is now `1e-8`: four orders above the
observed `8e-11`, three below the smallest genuine log-modulus
(`log q = 0.1043`).

That is the **third** time in this probe's own lineage that a too-permissive
test produced a headline the mathematics does not support, and the second where
the wrong answer was the *flattering* one.

## AND A THIRD CORRECTION, INSIDE THE CORRECTION

My first draft of the integer-structure section claimed *"the achievable set is
DISCRETE -- ratios of integers"*, and printed a table of **rounded** `k =
log|l|/log q` beside its own `all integers? False` for the word `Baa`.  The
rounding concealed the counterexample the check was reporting.

Measured: every all-**positive** word tested has moduli that are exact integer
powers of `q` (`abaab` -> `k = 5,1,1,-1,-1,-5`; `aabb` -> `4,2,2,-2,-2,-4`),
but mixed-sign words need not -- `Baa` gives `k = 2.0321548, ...`, ratio
`2.032154824`, not rational-looking at all.  So the set is **not** discrete;
only its positive-word part is.

## 🛑 DO NOT READ THIS AS "THE BLIND SECTOR IS NOT EXCLUDED"

The `R <= 1` bound being 2-dimensional is a statement about **that bound**.  A
stronger, dimension-independent argument excludes the single-crossing isospin
criterion in **every** block, blind ones included: `sigma`'s minimal polynomial
divides `(x - q)(x + 1/q)`, so `spec(rho(sigma_i)) subset {q, -1/q}` in ANY
representation, the isospin channels are `sigma`'s spectral projectors, and the
channel asymmetry is therefore **exactly 1 everywhere**.  See
`isospin_channel_R_is_one_everywhere_probe`, which verifies it by exact matrix
identity to `5.6e-42`.

The spread measured here is a **word's** spectrum, and a word's eigenprojectors
are not `sigma`'s -- so it is not available to the channels as currently
defined.  Using it needs the channels **re-identified**, which is an open
definitional question, not a bound.

## What is NOT claimed

  * NOT that `R` as the eigenvalue criterion defines it (a per-CHANNEL
    quantity) is this max/min ratio.  This measures the SPREAD of log-moduli,
    which is what the determinant argument constrains; assigning two specific
    eigenvalues to the two isospin channels in a `d`-dimensional block is a
    separate question, unanswered here.
  * NOT a binding value, nothing wired, nothing fitted.
  * NOT that the reachable ratio settles the 33.7 target -- the search below
    reports what it found over the words enumerated, and that is a lower bound
    on what is reachable, never an upper one.

Scope **(a)** for the measurements; the one-equation-on-`d`-unknowns argument
is exact.

NO FLOAT64: mpmath `mpf` at 40 dps, 50-digit proton pin.  Eigenvalues come from
characteristic-polynomial roots (Faddeev-LeVerrier + `mp.polyroots`), not from
`mp.eig`, which fails to converge on some of these matrices.
"""

from __future__ import annotations

import itertools as _it
import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION

mp.mp.dps = 40
TOL = mp.mpf(10) ** -25
BASIS = ["e", "1", "2", "12", "21", "121"]


def fmt(x, n=10):
    return mp.nstr(x, n)


def gen(g, h):
    """Left multiplication by s_g on the regular rep of H_3."""
    M = mp.zeros(6, 6)

    def add(dst, src, c):
        M[BASIS.index(dst), BASIS.index(src)] += c

    if g == 1:
        add("1", "e", 1); add("1", "1", h); add("e", "1", 1)
        add("12", "2", 1); add("12", "12", h); add("2", "12", 1)
        add("121", "21", 1); add("121", "121", h); add("21", "121", 1)
    else:
        add("2", "e", 1); add("2", "2", h); add("e", "2", 1)
        add("21", "1", 1); add("21", "21", h); add("1", "21", 1)
        add("121", "12", 1); add("121", "121", h); add("12", "121", 1)
    return M


def charpoly(A, n=6):
    """Faddeev-LeVerrier: coefficients of det(xI - A), leading first."""
    I = mp.eye(n)
    Mk, coeffs = mp.zeros(n, n), [mp.mpf(1)]
    Mk = I
    c = mp.mpf(1)
    for k in range(1, n + 1):
        AM = A * Mk if k > 1 else A
        tr = sum(AM[i, i] for i in range(n))
        c = -tr / k
        coeffs.append(c)
        Mk = AM + c * I
    return coeffs


def moduli(A):
    """Eigenvalue moduli via char-poly roots -- robust where mp.eig is not.

    Escalates precision on NoConvergence and returns None if it still fails,
    so callers can COUNT AND REPORT the unresolved rather than skip silently.
    A quietly-dropped word is how an enumeration reports a maximum it never
    actually searched.
    """
    cp = charpoly(A)
    for steps, extra in ((200, 200), (600, 800), (2000, 2400)):
        try:
            roots = mp.polyroots(cp, maxsteps=steps, extraprec=extra)
            return sorted((abs(r) for r in roots), reverse=True)
        except (mp.libmp.libhyper.NoConvergence, ZeroDivisionError):
            continue
    return None


# Noise floor for "is this modulus exactly 1?".  MEASURED, not guessed: a
# repeated root of the char poly resolves to ~8e-11 here (see AABAAB in the
# docstring), so a 1e-15 cut lets numerical zeros through and a ratio computed
# against one is meaningless.  1e-8 sits four orders above the observed floor
# and three below the smallest genuine log-modulus (log q = 0.1043).
UNIT_FLOOR = mp.mpf(10) ** -8


def spread(A):
    """max/min over log-moduli that are genuinely non-unit.

    Returns (None, None) when the roots could not be resolved at all.

    The floor matters more than it looks: with a 1e-15 cut, the word AABAAB
    reports a ratio of 7.75e9 purely because four of its moduli are 1 to within
    8.08e-11 -- exactly 1 as algebra, noise as arithmetic.  That figure was
    briefly this probe's headline 'reaches 33.7: True'.  It does not."""
    ms = moduli(A)
    if ms is None:
        return None, None
    nz = [abs(mp.log(m)) for m in ms if abs(mp.log(m)) > UNIT_FLOOR]
    if len(nz) < 2:
        return mp.mpf(0), ms
    return max(nz) / min(nz), ms


def main() -> int:
    q = Q_MP
    h = q - 1 / q
    L1, L2 = gen(1, h), gen(2, h)
    I = mp.eye(6)
    i1, i2 = L1 - h * I, L2 - h * I      # sigma^-1 = sigma - h

    def nrm(M):
        return max(abs(M[a, b]) for a in range(6) for b in range(6))

    print("=" * 78)
    print(" REGULAR-REP MODULUS SPREAD — |det| = 1 does NOT close a d > 2 block")
    print("=" * 78)
    print(f"q = {fmt(q, 17)}   h = {fmt(h)}")

    print("\n[1] THE REPRESENTATION — relations asserted, not assumed")
    print("-" * 78)
    print(f"    quadratic residual s1 : {fmt(nrm(L1 * L1 - h * L1 - I), 3)}")
    print(f"    quadratic residual s2 : {fmt(nrm(L2 * L2 - h * L2 - I), 3)}")
    print(f"    braid relation        : {fmt(nrm(L1 * L2 * L1 - L2 * L1 * L2), 3)}")
    print(f"    inverse s1 * s1^-1    : {fmt(nrm(L1 * i1 - I), 3)}")
    for nm, M in (("s1", L1), ("s2", L2)):
        assert nrm(M * M - h * M - I) < TOL, f"{nm} must satisfy the quadratic"
    assert nrm(L1 * L2 * L1 - L2 * L1 * L2) < TOL, "braid relation must hold"
    assert nrm(L1 * i1 - I) < TOL, "sigma - h must be the inverse"

    print("\n[2] THE RETRACTION — a |det| = 1 block of dim 6, ratio 2.0")
    print("-" * 78)
    words = [("s1", L1), ("s1*s2", L1 * L2), ("s1*s2*s1", L1 * L2 * L1),
             ("s1^2 s2^2", L1 * L1 * L2 * L2),
             ("s1^3 s2^-2", L1 * L1 * L1 * i2 * i2)]
    print(f"    {'word':>12} {'|det|':>10} {'ratio':>13}   moduli")
    got2 = None
    for nm, M in words:
        r, ms = spread(M)
        dt = mp.mpf(1)
        for m in moduli(M):
            dt *= m
        print(f"    {nm:>12} {fmt(dt, 8):>10} {fmt(r, 10):>13}   "
              + ", ".join(fmt(m, 6) for m in ms))
        if nm == "s1^2 s2^2":
            got2 = (r, ms)
        assert abs(dt - 1) < mp.mpf("1e-20"), "every braid word here has |det| = 1"
    assert got2 is not None
    r2, ms2 = got2
    # The ratio is exactly 2 as ALGEBRA: the six moduli are exact powers of q.
    # Assert that -- it is the stronger check and it explains the residual.
    print()
    print("    s1^2 s2^2's moduli are EXACT POWERS OF q (checked, not eyeballed):")
    for k, mo in zip([4, 2, 2, -2, -2, -4], ms2):
        d = abs(mo - q ** k)
        print(f"      q^{k:>3} : exact {fmt(q ** k, 20):>24}  got {fmt(mo, 20):>24}"
              f"   diff {fmt(d, 4)}")
        assert d < mp.mpf("1e-18"), f"modulus must be q^{k}"
    print("    so log|l| in {4,2,2,-2,-2,-4} * log q and the ratio is 4/2 = 2")
    print("    EXACTLY, as algebra.  The measured value differs from 2 by")
    print(f"    {fmt(abs(r2 - 2), 4)} -- entirely repeated-root error in polyroots")
    print("    on the doubled q^2 (6.5e-20 there vs 1e-38 on the simple roots),")
    print("    not a statement about the mathematics.")
    assert abs(r2 - 2) < mp.mpf("1e-15"), (
        "s1^2 s2^2 must give ratio 2 to polyroots' repeated-root accuracy")
    print()
    print("    s1^2 s2^2 has |det| = 1 and ratio EXACTLY 2.  So fixing the")
    print("    determinant does NOT fix the ratio of log-moduli once there are")
    print("    more than two of them:  sum_i log|l_i| = log|det|  is ONE")
    print("    equation on d unknowns, and only at d = 2 does it pin a ratio.")
    print("    RETRACTED: '(3,2,1) is det-locked, so R <= 1 closes it'.  The")
    print("    det-lock is real (m+ = m- = 8); the closure does not follow, and")
    print("    dim (3,2,1) = 16 leaves 15 free directions.")

    print("\n[3] 🛑 THE NEAR-MISS — three words that would have reversed this")
    print("-" * 78)
    print("    My first test was exactly s1, s1*s2, s1*s2*s1.  All three give")
    print("    ratio 1.0 (above), and on that evidence I was about to RETRACT A")
    print("    CORRECT CORRECTION.  Their 2-dim block is elliptic -- eigenvalues")
    print("    on the unit circle -- which is why four of six moduli read 1.0.")
    print("    One more crossing breaks it.")
    print("    Same defect as the two claims it was correcting, reached a THIRD")
    print("    time in one session, while checking the second.  A negative from")
    print("    a small hand-picked set is not evidence.")

    print("\n[4] HOW FAR THE SPREAD REACHES — enumerated, a LOWER bound only")
    print("-" * 78)
    G = {"a": L1, "A": i1, "b": L2, "B": i2}
    best = (mp.mpf(0), "")
    seen = unresolved = 0
    unres_ex = []
    for n in range(2, 7):
        for w in _it.product("aAbB", repeat=n):
            s = "".join(w)
            M = I
            for ch in s:
                M = M * G[ch]
            seen += 1
            r, _ = spread(M)
            if r is None:
                unresolved += 1
                if len(unres_ex) < 3:
                    unres_ex.append(s)
                continue
            if r > best[0]:
                best = (r, s)
        print(f"    words of length <= {n}: {seen:>6}   best ratio = "
              f"{fmt(best[0], 10):>13}  at  {best[1]}")
    print(f"    words whose roots could not be resolved: {unresolved} / {seen}"
          + (f"   e.g. {', '.join(unres_ex)}" if unres_ex else ""))
    print("    (counted and reported, not skipped silently -- a dropped word is")
    print("     how an enumeration reports a maximum it never searched.)")
    need = AME_B_DEUTERON_MEV_VALIDATION / mp.mpf("0.066")   # the np 1S0 VIRTUAL STATE, the SAME np pair as the deuteron differing only in isospin.  CORRECTED from 0.1 (= pp/nn, a DIFFERENT PAIR), which conflated pair identity with isospin; see main 1d9d3500f5.
    print()
    print(f"    nature's channel asymmetry needs R ~ {fmt(need, 6)}")
    print(f"    best over this enumeration          {fmt(best[0], 10)}   at {best[1]}")
    print(f"    reaches it?  {best[0] >= need}")
    assert best[0] > 1, "the spread must exceed 1 somewhere -- that is the point"
    assert best[0] < mp.mpf("1e3"), (
        "a huge ratio means the unit floor let a numerical zero through")

    print("\n[4a] 🛑 THE FIGURE THIS SECTION ALMOST REPORTED")
    print("-" * 78)
    print("    With the unit floor at 1e-15 this enumeration returned")
    print("    ratio = 7752455236.0 at AABAAB, and the line above read")
    print("    'reaches it? True'.  It was an ARTEFACT: four of AABAAB's six")
    print("    moduli are 1 to within 8.08e-11 -- exactly 1 as algebra, noise")
    print("    as arithmetic, from a repeated char-poly root -- so the ratio")
    print("    was dividing a real log-modulus by numerical dust.")
    print(f"    The floor is now {fmt(UNIT_FLOOR, 3)}, four orders above the observed")
    print("    8e-11 and three below the smallest genuine log-modulus")
    print(f"    (log q = {fmt(mp.log(q), 8)}).  Honest maximum: {fmt(best[0], 8)}.")
    print("    It does NOT reach 22.25.")

    print("\n[4b] INTEGER POWERS OF q — but only for POSITIVE words")
    print("-" * 78)
    print("    For some words every modulus is an exact integer power of q, so")
    print("    the log-moduli are integer multiples of log q and the ratio is")
    print("    rational.  For others it is not.  Raw k, NOT rounded:")
    posint = negint = 0
    for s in ("abaab", "aabb", "ab", "Baa", "AABAAB", "aB"):
        M = I
        for ch in s:
            M = M * G[ch]
        ms = moduli(M)
        ks = [mp.log(m) / mp.log(q) for m in ms]
        near = all(abs(k - mp.nint(k)) < mp.mpf("1e-7") for k in ks)
        allpos = all(c in "ab" for c in s)
        print(f"      {s:>7} {'positive' if allpos else 'mixed   '}: k = "
              + ", ".join(fmt(k, 8) for k in ks))
        print(f"      {'':>7}           all integers? {near}")
        if allpos:
            posint += 1
            assert near, f"positive word {s} must have integer-power moduli"
        elif near:
            negint += 1
    print()
    print("    Every all-POSITIVE word tested has integer-power moduli; the")
    print("    mixed-sign ones need not -- Baa gives ratio 2.032154824, which")
    print("    is not rational-looking at all.")
    print()
    print("    🛑 SO MY FIRST DRAFT OF THIS SECTION WAS WRONG.  It read 'the")
    print("    achievable set is DISCRETE -- ratios of integers', and used a")
    print("    table that printed the ROUNDED k beside its own 'all integers?")
    print("    False' for Baa.  The rounding hid the counterexample the check")
    print("    was reporting.  The set is not discrete; only the positive-word")
    print("    part of it is.")
    print()
    print("    What survives: nothing here reaches 33.7055, and if a future")
    print("    attempt lands on a near-integer ratio such as 89/4 = 22.25")
    print("    (already 1.9e-4 off), that is an approximate match to a ratio")
    print("    nobody derived -- numerology, not a mechanism.")

    print()
    print("    This is a LOWER bound on what is reachable, never an upper one:")
    print("    it enumerates words of length <= 6 in ONE algebra (H_3), and the")
    print("    binding operator lives in H_6.  A larger figure elsewhere would")
    print("    not contradict it.")

    print("\n[5] WHAT THIS SETTLES")
    print("-" * 78)
    print("  RETRACTED: '|det| = 1 closes the block'.  True at d = 2 ONLY.")
    print("    Demonstrated at d = 6 with |det| = 1 and ratio exactly 2.")
    print("  ESTABLISHED: sum_i log|l_i| = log|det| is one equation on d")
    print("    unknowns.  The R <= 1 bound is a 2-DIMENSIONAL fact and does not")
    print("    extend to higher blocks.")
    print("  🛑 BUT DO NOT READ THAT AS 'the blind sector is not excluded'.")
    print("    This line used to end '...which is why the blind sector's")
    print("    high-dimensional blocks are not excluded by it' -- true about")
    print("    the BOUND, misleading about the physics.  A stronger,")
    print("    dimension-independent argument DOES exclude the single-crossing")
    print("    isospin criterion in every block, blind ones included: sigma's")
    print("    minimal polynomial divides (x-q)(x+1/q), so its spectrum is")
    print("    {q, -1/q} in ANY representation and the channel asymmetry is")
    print("    exactly 1 everywhere.  See isospin_channel_R_is_one_everywhere.")
    print("    The spread measured here is a WORD's spectrum, and a word's")
    print("    eigenprojectors are not sigma's -- so it is not available to the")
    print("    channels as currently defined.")
    print("  UNAFFECTED: the R <= 1 bound on the BOND-LETTER family stands --")
    print("    that IS a 2x2 statement, computed directly in H_2's regular rep.")
    print("  NOT CLAIMED: that the max/min log-modulus ratio IS the eigenvalue")
    print("    criterion's per-channel R.  Assigning two eigenvalues of a")
    print("    d-dim block to the two isospin channels is a separate question.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
