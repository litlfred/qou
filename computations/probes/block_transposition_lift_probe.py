#!/usr/bin/env python3
"""block_transposition_lift_probe — LIFTS the two-nucleon isospin channel
asymmetry from the n=2 interface to the physical 3-strands-per-nucleon
construction, which is the step `main`'s `t7qv/m896` explicitly did not take.

Three results, one positive, one negative, one structural:

  * the n=2 cap of exactly 1 does **NOT** survive the lift (max 5 within a
    block, 9 across blocks);
  * **provided both channels are exponentially weighted**, the achievable
    asymmetries form a **small discrete set** whose ceiling is **9**, so
    `Delta_{3,3}` alone cannot supply nature's `33.7` -- exhaustively over all
    11 Wedderburn blocks of `H_6`, not by sampling; and
  * that proviso is not idle.  Three blocks carry eigenvalues of modulus
    **exactly 1**, for which the asymmetry is unbounded rather than merely
    large -- and **every one of those blocks is trace-blind**, while no
    trace-visible block contains one.  Both halves are exact, with no
    exceptions in either direction.

Bean `qou-brng`, arc `bk-crossing-mass-binding`.  Follows
`isospin_channel_R_is_one_everywhere_probe` (this session) and `main`'s
`1d9d3500f5` (`t7qv/m896`, landed 2026-09-01).

## THE SETUP, and why the lift is forced rather than chosen

`t7qv/m896` established, and this session re-derived independently from the
minimal polynomial, that at the **two-strand** interface the channel asymmetry
is capped at exactly 1:

    "The achievable asymmetry |L(T=0)|/|L(T=1)| is capped at exactly 1, attained
     only at beta = 0 where both channels equal log q to 5.7e-42."

with the identification forced by Pauli -- `1S0` needs symmetric isospin (T=1),
`3S1` antisymmetric (T=0), and the two-strand Hecke algebra has exactly two
1-dimensional blocks with eigenvalues `+q` and `-1/q`.  Its own caveat:

    "this is the n=2 interface only, not lifted to the 3-strands-per-nucleon
     construction"

**A nucleon is three strands.**  So two nucleons are six, and the operator that
exchanges them is not a single crossing `sigma` -- it is the **3-block
transposition** in `B_6`, the positive braid carrying `{1,2,3}` past `{4,5,6}`:

    Delta_{3,3} = (s3 s2 s1)(s4 s3 s2)(s5 s4 s3)      -- 9 crossings

verified here to induce the permutation `(0,1,2)(3,4,5) -> (3,4,5)(0,1,2)`
exactly.  There is no freedom in this: it is the standard block transposition,
and it is what "exchange the two nucleons" means once each is three strands.

## WHY THE CAP WAS ALWAYS GOING TO BREAK HERE

This session's catalogue established that channel asymmetry is exactly 1 for
every object built from *few* crossings -- a single crossing in any
representation, any pair exchange at any separation (band generators are
conjugates of `sigma`), `sigma^k` at any power, and any far-commuting product --
and that spread requires **at least three crossings on two non-commuting
generators**.

`Delta_{3,3}` has **nine** crossings on five generators.  It qualifies, and by
construction rather than by search: the physical three-strand nucleon forces it.

## THE MEASUREMENT: the spectrum is exactly q^k with k an INTEGER

Every eigenvalue of every `rho_lambda(Delta_{3,3})` has modulus exactly `q^k`
for an integer `k`.  This is measured, not assumed, and it is what makes the
asymmetry a *counting* quantity rather than a continuum:

    dps      30        40        60        90
    max|k - round(k)|  3.4e-7   9.1e-10   1.2e-14   1.8e-22

The deviation falls with working precision, so it is `polyroots` resolution and
not a real departure from integrality.  This probe runs at 60 dps and asserts
integrality at `1e-10`, roughly four orders inside the measured 60-dps figure.

The **channel asymmetry** generalises the n=2 quantity continuously: at n=2,
`sigma` has eigenvalues `q` and `-1/q`, i.e. `k = {+1, -1}`, and
`|L(T=0)|/|L(T=1)| = 1`.  At n=6 the same ratio is `max|k| / min|k|` over the
nonzero exponents.  So the n=2 cap of 1 and the numbers below are the same
quantity at two tower levels, not two different definitions.

## THE UNIT MODULI, and why they are not a nuisance

An eigenvalue with `k = 0` has `|lambda| = 1`, so `L = log|lambda| = 0` and the
asymmetry against any other channel *diverges*.  The first version of this
probe computed the ratio over `k != 0` and so filtered those away silently,
which would have made "ceiling 9" a stronger claim than the measurement
supports.  They are reported here instead, because where they sit is the
result:

    blocks carrying k = 0:   (4,1,1)  (3,2,1)  (3,1,1,1)     -- 3, 3, 4 rows
    blocks not carrying it:  (6,) (5,1) (4,2) (3,3) (2,2,2)
                             (2,2,1,1) (2,1,1,1,1) (1^6)

Every block in the first list has `l(lambda) >= 3` and is therefore invisible
to the Markov trace under convention D's row cap; no block with
`l(lambda) <= 2` appears there.  Both directions are asserted below.

So the unbounded asymmetry **is** available in this construction, but only from
the sector the trace cannot see -- which is the "computable but not directly
observable" class rather than a direct `n = 2` observable.  This probe does not
claim that class is reachable by subtraction; it locates it.

## SIBLING CONVERGENCE — `qou-r1yj` did this lift independently, same day

`de5c18f588` (*"t7qv/r1yj: lifting (T,S) to six strands raises the cap to 3/2 —
and costs Pauli"*) landed on `main` while this was being written, from a
different session.  It uses the **same operator**, verifies the **same
permutation before use**, and finds the **same spectrum**.  Neither probe knew
of the other; the agreement is independent confirmation, and the two numbers
are **not** in conflict.

**The spectra agree exactly.**  Restricting this probe to the four
trace-visible blocks and taking the union of exponents gives
`{-3, -1, 2, 3, 5, 6, 9}`, which is `r1yj`'s seven magnitudes.  Asserted below.

**The sign convention differs — do NOT "correct" one into the other.**  `r1yj`
reports `L/log q` with the opposite sign, so its bound `{3, 1}` and unbound
`{-2, -3, -5, -6, -9}` are the negation of the set above.  Same measurement.

**The two ratios answer different questions:**

  * `r1yj` applies the **isospin assignment** — which eigenvalues are the bound
    and unbound channels — and reports the resulting `|L_bound|/|L_unbound|`,
    best value **3/2**.
  * this probe deliberately makes **no** assignment (see *What is NOT claimed*)
    and reports the **ceiling over all assignments**: **5** within a block,
    **9** across blocks.

So `3/2 <= 5 <= 9`, and the relation is informative in one direction:
**the ceiling here bounds what any re-assignment of `r1yj`'s channels could
ever achieve.**  Its 22.47x miss against 33.7 cannot be repaired by choosing
the channels differently — the best conceivable is `33.7/9 = 3.7x`, still a
miss.  That strengthens `r1yj`'s negative rather than competing with it.

**What this probe adds:** `r1yj` scans the four *live* blocks; this scans all
**11**, and the extra seven are where the `k = 0` eigenvalues live -- the
unbounded-ratio sector, absent from the visible four.  That is consistent with
`r1yj` seeing no unit modulus, and is why the containment result above is
stated over the full block set.

`qou-m896`'s `n = 2` cap of 1 is not overturned by either probe; it was stated
at the two-strand interface and stands there.  All three should be quoted
together.

## Internal consistency checks asserted here

  * **Trivial and sign reps.** `sigma -> q` and `sigma -> -1/q`, so a
    9-crossing word must give `k = +9` and `k = -9`.  Both hit exactly.
  * **Conjugation duality.** `lambda -> lambda'` is `q -> -1/q`, so the
    exponent multisets must satisfy `k(lambda') = -k(lambda)`.  Verified for
    all 5 conjugate pairs and the one self-conjugate block `(3,2,1)`, whose
    multiset is therefore symmetric about 0.

## What is NOT claimed

  * **NOT** that this closes the binding gap.  It does not: the ceiling is 9
    and nature needs ~33.7.  Breaking the cap of 1 was necessary, not
    sufficient, and the negative here is the more useful half.
  * **NOT** a structural exclusion (scope (b)) of the block transposition as an
    *ingredient*.  This is scope **(a)**: `Delta_{3,3}` **alone**, with the
    channels drawn from its own spectrum, does not reach 33.7.  A closure that
    combines it with a further additive or higher-order term is untouched by
    this -- see the extensive-term frontier in AGENTS.md.
  * **NOT** a re-identification of the isospin channels.  `t7qv/m896` forced
    the identification at `n = 2` by Pauli.  WHICH eigenspaces of
    `Delta_{3,3}` carry `T = 0` and `T = 1` at `n = 6` is a separate question
    this probe does **not** answer -- it computes the available spectrum, not
    the assignment.  That is why the ceiling is reported as a maximum over all
    assignments rather than as a value: assigning them to fit a target would be
    exactly the anti-fit line.
  * **NOT** a bound on `|k|` for general braid words.  `|k| <= 9 =` (crossing
    number) is *observed* here, not proved.  The exhaustive claim is the narrow
    one: over all 11 blocks of `H_6`, for **this** operator, the ceiling is 9.

NO FLOAT64: `build_seminormal_matrices_mp` (the corpus's exact-arithmetic
generator builder) at 60 dps, 50-digit proton pin.  Eigenvalues come from
characteristic-polynomial roots (Faddeev-LeVerrier + `mp.polyroots`) with
escalating precision, because `mp.eig` fails to converge on several of these
blocks.

## An artefact this probe used to have, recorded so it is not reintroduced

The first version of this probe filtered near-unit moduli with a threshold
(`UNIT_FLOOR = 1e-8`) and reported a ratio of **8888561.38** for `(3,2,1)`.
That was numerical dust: at 30 dps the true `k = 0` eigenvalues of that block
resolve to `|k| ~ 3.5e-8`, just above the floor, and dividing 3 by that gives
the eight-million figure.  Two sibling blocks reported `1.00000009` from the
same cause.  The same artefact class had already been caught twice in this
session's earlier probes with a floor at `1e-15`.

The fix was not a bigger floor.  **The quantization removes the need for a
threshold at all** -- read the integer off and assert integrality, and a
"nearly zero" exponent is either exactly 0 or the run is not converged, with no
tuning parameter in between.  A threshold-free test cannot be defeated by
choosing the threshold badly.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from hecke_characters import build_seminormal_matrices_mp  # noqa: E402
from partition_utils import conjugate_partition  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION

mp.mp.dps = 60
INT_TOL = mp.mpf(10) ** -10          # measured 60-dps deviation is ~1.2e-14
WORD = [2, 1, 0, 3, 2, 1, 4, 3, 2]   # Delta_{3,3} in B_6, 0-indexed generators


def fmt(x, n=8):
    return mp.nstr(x, n)


def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def charpoly(A, n):
    """Faddeev-LeVerrier: coefficients of det(xI - A), leading first."""
    I = mp.eye(n)
    Mk, coeffs = I, [mp.mpf(1)]
    for k in range(1, n + 1):
        AM = A * Mk if k > 1 else A
        c = -sum(AM[i, i] for i in range(n)) / k
        coeffs.append(c)
        Mk = AM + c * I
    return coeffs


def roots(A, n):
    """Eigenvalues; None if the roots cannot be resolved (reported, never
    skipped silently -- a dropped block is how a survey reports a maximum it
    never searched)."""
    cp = charpoly(A, n)
    for steps, extra in ((900, 1200), (3000, 4000), (9000, 12000)):
        try:
            return mp.polyroots(cp, maxsteps=steps, extraprec=extra)
        except (mp.libmp.libhyper.NoConvergence, ZeroDivisionError):
            continue
    return None


def main() -> int:
    q = Q_MP
    lq = mp.log(q)

    print("=" * 78)
    print(" BLOCK-TRANSPOSITION LIFT — the n=2 cap breaks, but the ceiling is 9")
    print("=" * 78)
    print(f"q = {fmt(q, 17)}    log q = {fmt(lq, 12)}    dps = {mp.mp.dps}")

    print("\n[1] THE OPERATOR IS FORCED, not chosen")
    print("-" * 78)

    def pmul(p, r):
        return [p[x] for x in r]

    S = []
    for i in range(5):
        s = list(range(6))
        s[i], s[i + 1] = s[i + 1], s[i]
        S.append(s)
    perm = list(range(6))
    for g in WORD:
        perm = pmul(perm, S[g])
    print("    A nucleon is THREE strands, so two nucleons are six and the")
    print("    exchange operator is the 3-block transposition in B_6:")
    print("        Delta_{3,3} = (s3 s2 s1)(s4 s3 s2)(s5 s4 s3)   -- 9 crossings")
    print(f"    induced permutation: {perm}   target [3,4,5,0,1,2]")
    print(f"    is the block swap {{1,2,3}} <-> {{4,5,6}}?  "
          f"{perm == [3, 4, 5, 0, 1, 2]}")
    assert perm == [3, 4, 5, 0, 1, 2], "WORD must be the 3-block transposition"
    assert len(WORD) == 9, "and must carry 9 crossings"
    print("    9 crossings on 5 generators -- so by this session's catalogue it")
    print("    CAN spread, and it is forced by the physical three-strand")
    print("    nucleon rather than selected in order to spread.")

    print("\n[2] SPECTRUM PER WEDDERBURN BLOCK OF H_6")
    print("-" * 78)
    print("    Every modulus is exactly q^k with k an INTEGER (asserted, tol"
          f" {fmt(INT_TOL, 2)}).")
    print("    'ratio' = max|k| / min|k| over k != 0 — the n=2 channel")
    print("    asymmetry continued up the tower (at n=2, k = {+1,-1}, ratio 1).")
    print("      n/a   = dim 1, so the block admits no channel PAIR at all")
    print("      +INF  = block carries a k=0 eigenvalue (|lambda| = 1, L = 0),")
    print("              so a pair straddling it has UNBOUNDED asymmetry")
    print()
    print(f"    {'lambda':>18} {'dim':>4} {'rows':>4} {'blind':>6} "
          f"{'exponents k (with multiplicity)':<34} {'ratio':>7}")

    exps = {}
    unresolved = []
    worst_dev = mp.mpf(0)
    for lam in partitions(6):
        g = build_seminormal_matrices_mp(lam, q)[0]
        d = g[0].rows
        A = mp.eye(d)
        for i in WORD:
            A = A * g[i]
        r = roots(A, d)
        blind = "YES" if len(lam) > 2 else "-"
        if r is None:
            unresolved.append(lam)
            print(f"    {str(lam):>18} {d:>4} {len(lam):>4} {blind:>6} "
                  f"{'UNRESOLVED':<34} {'-':>7}")
            continue
        ks = []
        for x in r:
            kf = mp.log(abs(x)) / lq
            dev = abs(kf - mp.nint(kf))
            worst_dev = max(worst_dev, dev)
            assert dev < INT_TOL, (
                f"{lam}: modulus is not q^(integer) — k={fmt(kf, 20)}, "
                f"deviation {fmt(dev, 4)}; raise dps rather than the tolerance")
            ks.append(int(mp.nint(kf)))
        ks.sort()
        exps[lam] = tuple(ks)
        nz = [abs(k) for k in ks if k != 0]
        if d < 2:
            ratio = "n/a"          # one eigenvalue: there is no pair to compare
        elif 0 in ks:
            ratio = "+INF"         # a pair straddling |lambda| = 1 diverges
        else:
            ratio = max(nz) / min(nz)
        counts = {}
        for k in ks:
            counts[k] = counts.get(k, 0) + 1
        desc = " ".join(f"{k}^{c}" if c > 1 else f"{k}"
                        for k, c in sorted(counts.items()))
        print(f"    {str(lam):>18} {d:>4} {len(lam):>4} {blind:>6} "
              f"{desc:<34} {ratio:>7}")
    print(f"\n    worst |k - round(k)| over all blocks: {fmt(worst_dev, 4)}")
    print(f"    blocks whose roots could not be resolved: {len(unresolved)}"
          + (f"  {unresolved}" if unresolved else ""))
    assert not unresolved, "every block must resolve before a ceiling is claimed"

    print("\n[3] INTERNAL CONSISTENCY (asserted, not assumed)")
    print("-" * 78)
    print(f"    trivial (6,)  -> k = {exps[(6,)]}   "
          f"expected (9,)   [sigma -> q, 9 crossings]")
    print(f"    sign (1^6)    -> k = {exps[(1,) * 6]}   "
          f"expected (-9,)  [sigma -> -1/q]")
    assert exps[(6,)] == (9,) and exps[(1,) * 6] == (-9,)
    ok = True
    for lam, ks in exps.items():
        dual = tuple(conjugate_partition(lam))
        want = tuple(sorted(-k for k in ks))
        got = exps[dual]
        if got != want:
            ok = False
            print(f"    DUALITY FAILS: {lam} vs {dual}: {got} != {want}")
    print(f"    conjugation duality k(lambda') = -k(lambda) holds for all "
          f"{len(exps)} blocks?  {ok}")
    assert ok, "lambda -> lambda' is q -> -1/q; the exponents must negate"

    print("\n[3a] SIBLING CONVERGENCE — qou-r1yj (de5c18f588, main) agrees")
    print("-" * 78)
    visible = sorted({k for lam, ks in exps.items() if len(lam) <= 2
                      for k in ks})
    r1yj = [-3, -1, 2, 3, 5, 6, 9]
    print(f"    exponents over the four TRACE-VISIBLE blocks: {visible}")
    print(f"    qou-r1yj's seven magnitudes:                  {r1yj}")
    print(f"    identical?  {visible == r1yj}")
    assert visible == r1yj, (
        "an independent sibling measured this spectrum; a disagreement is a "
        "defect in one of the two and must be resolved, not reported")
    print("    Independent session, same operator, same permutation check,")
    print("    same spectrum.  r1yj reports L/log q with the OPPOSITE SIGN,")
    print("    so its bound {3,1} / unbound {-2,-3,-5,-6,-9} is this set")
    print("    negated — the same measurement, not a discrepancy.")
    print()
    print("    The RATIOS differ because they answer different questions:")
    print("      r1yj  applies the isospin assignment  -> 3/2 (assigned value)")
    print("      here  makes NO assignment             -> 5 in-block, 9 across")
    print("                                               (ceiling over ALL)")
    print("    So 3/2 <= 5 <= 9, and the ceiling BOUNDS what any re-assignment")
    print("    of r1yj's channels could reach: its 22.47x miss against 33.7")
    print("    cannot be repaired by choosing channels differently, since the")
    print("    best conceivable is 33.7/9 = 3.7x.  That strengthens its")
    print("    negative rather than competing with it.")
    print("    qou-m896's n=2 cap of 1 stands at the two-strand interface;")
    print("    all three results should be quoted together.")

    print("\n[3b] WHERE THE UNIT MODULI SIT — the two threads meet here")
    print("-" * 78)
    unit = sorted(L for L, ks in exps.items() if 0 in ks)
    nounit = sorted(L for L, ks in exps.items() if 0 not in ks)
    print(f"    blocks with a k=0 eigenvalue (|lambda| = 1, so L = 0):")
    for L in unit:
        print(f"        {str(L):>18}  rows={len(L)}  "
              f"{'TL-BLIND' if len(L) > 2 else 'TL-VISIBLE'}")
    print(f"    blocks without: {', '.join(str(L) for L in nounit)}")
    all_blind = all(len(L) > 2 for L in unit)
    none_visible = not any(len(L) <= 2 for L in unit)
    print(f"    every unit modulus lies in a TL-BLIND block (rows > 2)?  "
          f"{all_blind}")
    print(f"    no TL-VISIBLE block (rows <= 2) carries one?             "
          f"{none_visible}")
    assert all_blind and none_visible, (
        "the containment is exact in both directions; if it ever fails, the "
        "'unbounded asymmetry is trace-blind' reading must be re-derived")
    print()
    print("    So the UNBOUNDED asymmetry exists in this construction, but")
    print("    lives entirely in the sector the Markov trace cannot see under")
    print("    convention D's row cap l(lambda) <= 2.  That is the 'computable")
    print("    but not directly observable' class, not a direct n=2 observable.")
    print("    This probe LOCATES that class; it does not claim it is")
    print("    reachable by subtraction, which is a separate question.")

    print("\n[4] THE VERDICT — cap broken, ceiling found")
    print("-" * 78)
    need = AME_B_DEUTERON_MEV_VALIDATION / mp.mpf("0.066")
    within = {}
    for lam, ks in exps.items():
        nz = [abs(k) for k in ks if k != 0]
        if len(ks) >= 2 and 0 not in ks and nz:
            within[lam] = max(nz) / min(nz)
    best_lam = max(within, key=lambda L: within[L])
    best = within[best_lam]
    allnz = sorted({abs(k) for ks in exps.values() for k in ks if k != 0})
    cross = max(allnz) / min(allnz)
    achievable = sorted(set(within.values()))

    print("    PROVISO, stated first because it bounds everything below: the")
    print("    figures here assume BOTH channels are exponentially weighted")
    print("    (k != 0).  Section [3b] showed three blocks violate that and")
    print("    give an UNBOUNDED ratio — all of them trace-blind.")
    print()
    print(f"    n=2 interface (t7qv/m896, and this session independently):")
    print(f"        channel asymmetry CAPPED AT EXACTLY 1")
    print(f"    n=6, Delta_(3,3), channels within ONE block:")
    print(f"        max = {best} at lambda = {best_lam}"
          f"  ({len(best_lam)} rows, "
          f"{'TL-BLIND' if len(best_lam) > 2 else 'TL-VISIBLE'})")
    print(f"        achievable set over all 11 blocks: {achievable}"
          f"   — DISCRETE, not a continuum")
    print(f"    n=6, channels drawn from DIFFERENT blocks:")
    print(f"        available |k| = {allnz}, so ceiling = "
          f"{max(allnz)}/{min(allnz)} = {cross}")
    print(f"    nature requires ~ {fmt(need, 6)}   (np 1S0 virtual state, "
          f"same pair as the deuteron)")
    print()
    print(f"    exceeds the n=2 cap of 1?           {best > 1}")
    print(f"    reaches nature's value, in-block?   {best >= need}")
    print(f"    reaches it under ANY assignment?    {cross >= need}")
    assert best > 1, (
        "positive half: the n=2 cap must NOT survive the 3-strand lift")
    assert cross < need, (
        "negative half: if this ever passes, the exhaustive ceiling moved and "
        "the conclusion below must be re-derived, not edited")
    print()
    print("    POSITIVE: the cap of 1 is an artefact of treating a nucleon as")
    print("    ONE strand.  Once it is three, the exchange operator carries 9")
    print("    crossings and the asymmetry is no longer pinned.  That is what")
    print("    the n=2 result could not tell us, and what its caveat flagged.")
    print()
    print("    NEGATIVE, and the more useful half: among exponentially-weighted")
    print("    channels the asymmetry is a COUNTING quantity — a ratio of")
    print("    integers bounded by the crossing number — so it cannot be tuned.")
    print("    Exhaustively over all 11 blocks of H_6, that ceiling is")
    print(f"    {cross} and nature needs {fmt(need, 5)}.  Scope (a): Delta_(3,3) ALONE")
    print("    does not supply the observed channel asymmetry from its")
    print("    trace-visible spectrum.  A closure adding a further term is")
    print("    untouched, and so is the unbounded trace-blind sector of [3b].")

    print("\n[5] WHAT THIS DOES NOT CLAIM")
    print("-" * 78)
    print("  * NOT a structural exclusion (scope (b)) of the block")
    print("    transposition as an INGREDIENT.  Scope (a): it does not reach")
    print("    33.7 on its own trace-visible spectrum.")
    print("  * NOT a claim that the unbounded trace-blind sector of [3b] IS")
    print("    the closure.  Locating it is not reaching it — and it is now")
    print("    ANSWERED, negatively: markov_trace_family_rank_probe shows the")
    print("    Markov family spans rank n of a p(n)-dimensional character")
    print("    space, so NO subtraction over it isolates that sector (nor,")
    print("    in fact, any block of dimension > 1).  A non-trace functional")
    print("    is where a closure would have to come from.")
    print("  * NOT a re-identification of the isospin channels.  WHICH")
    print("    eigenspaces carry T=0 and T=1 at n=6 is unanswered here; that is")
    print("    why the ceiling is a maximum over assignments, not a value.")
    print("  * NOT a bound on |k| for general braid words.  |k| <= 9 = crossing")
    print("    number is OBSERVED here, not proved.  The exhaustive claim is")
    print("    narrow: over all 11 blocks of H_6, for THIS operator.")
    print("  * NOT a binding value.  Nothing wired, nothing fitted.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
