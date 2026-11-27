#!/usr/bin/env python3
"""allpairs_decay_turnover_exclusion_probe — the all-pairs-with-distance-decay
binding form, tested against an invariant the corpus ALREADY PROVED rather than
against a fit.  Formalize-first: the structural claim is stated below, before
any scan, and it prunes most of the parameter space without running one.

Bean `qou-brng`, arc `bk-crossing-mass-binding`.

## What is being tested

The proposal is: binding is a sum over ALL nucleon pairs, each weighted by a
per-bond-type log-suppression `L_XY` and attenuated with separation at a
per-bond-type rate `r_XY`:

    B  =  alpha * SUM_{i<j}  L_{type(i,j)} * r_{type(i,j)}^(s_ij - 1)

with `s_ij = |i - j|` the strand separation.  The three `r_XY` were MEASURED
in `spectral_gap_bond_decay_probe` as the transfer matrices' spectral gaps:

    r_pp = r_nn = 1/q^2   (exactly)          xi ~ 4.8 spacings
    r_pn      ~= 0.99986                     xi ~ 6992 spacings

## The invariant this is tested against (NOT a fit, and NOT mine)

`saturating_shared_channel_probe` (R9, committed) records the **t-ladder**: one
light cluster (triton) held fixed, k alphas added, k = 1..4.  The Model-G miss
along it has a strict INTERIOR MAXIMUM:

    0 = M(1) < M(2) < M(3) > M(4)          <- R9's WORDING, quoted verbatim;
                                              its own code gives M(1) = +0.1219,
                                              see the correction section below.

The `0 =` is R9's simplification of its own `modelg_miss` output, not a
computed zero, and is quoted here unaltered so the two statements can be
compared.  **What P1 needs is only the turnover `M(3) > M(4)`, plus the rising
leg `M(1) < M(2) < M(3)`, and both hold under either sign convention** -- so
nothing in this probe depends on the `0 =`.

That turnover is what killed R8's whole class:

  (P1) any ADDITIVE NON-NEGATIVE counting V(k) that is NON-DECREASING in k has
       V(4) >= V(3), while the target has M(4) < M(3).  EXCLUDED.

The question here is whether the decayed all-pairs form escapes P1.  Decay is
exactly the ingredient that could: attenuating existing pairs is a NEGATIVE
contribution, so V need not be monotone.  Whether it actually escapes is what
this measures.

## The structural claim, stated BEFORE the scan (formalize-first)

  CLAIM A (ordering-monotonicity).  If every `L_XY > 0` and the k -> k+1 step
  adds a CONTIGUOUS BLOCK OF NUCLEONS WITHOUT SPLITTING ANY EXISTING ADJACENCY
  -- i.e. the new alpha is appended at either end -- then EVERY existing pair
  keeps its separation, every new pair contributes a strictly positive
  `L * r^(s-1)`, and therefore

      V(k+1) > V(k)   for EVERY (r_pp, r_nn, r_pn) in (0,1]^3.

  So under append/prepend ordering the decayed all-pairs form is EXCLUDED by
  P1, for ANY decay rates whatsoever.  Decay buys nothing: it can only shrink
  contributions that are already there, and no contribution is ever removed.

  Consequence: the ONLY way the form survives is an ordering in which adding a
  cluster SPLITS existing adjacencies, so that existing pairs are pushed apart
  and attenuated.  That is a structural requirement on the nucleon ordering,
  not a free choice -- and it is testable.

Everything below either confirms Claim A by direct computation or measures the
splitting case it leaves open.  Both `L_XY > 0` and the monotonicity are
MEASURED here, not assumed.

## RESULTS

    L_pp = 0.6071661569     r_pp = 0.8116537544  ( = 1/q^2 exactly)
    L_pn = 0.6767409298     r_pn = 0.9998569862
    L_nn = 0.7899954929     r_nn = 0.8116537544  ( = 1/q^2 exactly)

  1. **Claim A confirmed**, 0 violations in 1000 grid points, both
     non-splitting orderings.  Under append/prepend the decayed all-pairs form
     is excluded by P1 for ANY (r_pp, r_nn, r_pn).

  2. **Stronger than Claim A, and not predicted by it:** the two SPLITTING
     orderings also went non-monotone at ZERO grid points.  Splitting an
     adjacency loses one full-strength `s=1` term and creates two boundary
     adjacencies plus the new block's own three, so the `s=1` count strictly
     rises; at `r -> 0` that term is the whole sum, and at `r -> 1` the sum is
     a pure pair count, which also rises.  Both limits increase and the grid
     finds no interior exception.

  3. **At the framework's OWN derived rates, no turnover on any ordering:**
     V = 12.7874, 30.4077, 54.1143, 83.5190 -- monotone increasing.

  4. **The arrangement-free bound is INCONCLUSIVE and is kept as such.**
     `Lo(19) = 44.46` vs `Up(15) = 72.60`: the intervals overlap, so nothing
     here excludes a turnover for an arbitrary ordering.  Four hand-picked
     orderings are four data points, not a theorem, and this is how far the
     ordering-free argument actually reaches.

  5. **Randomised arrangement search closes that gap empirically, not
     rigorously.**  Over 400 random arrangements each: `max V(3) = 60.9549`,
     `min V(4) = 83.5363`, margin `+22.58`.  The worst 19F still beats the best
     15N.  A sample, so scope-(a); item 4 is why it is not stated as more.

## A small correction to R9's own docstring, found on the way

R9 states its invariant as `0 = M(1) < M(2) < M(3) > M(4)`.  Rebuilding M with
R9's own `modelg_miss` gives `M(1) = +0.1219`, not 0.  The witness row carries
`resid_MeV = -0.1218526` while `deficit - pred = +0.1218526`, so the witness
and `modelg_miss` define the residual with OPPOSITE signs, and the "0 =" is a
simplification of the code's own output rather than a computed zero.

**The invariant is unaffected** -- P1 turns on the turnover `M(3) > M(4)`, and
the rising leg `M(1) < M(2) < M(3)` holds either way.  Recorded because a
reader taking "0 =" literally would think the k=1 rung is exactly closed, and
because a sign convention that flips between a witness and its consumer is the
kind of thing that is cheap to note now and expensive to rediscover.

## An ordering I was not looking for, and it points the other way

`L_nn > L_pn > L_pp`.  In this functional `B ~ alpha * SUM L`, a larger `L` is
MORE binding, so the per-bond hierarchy is **n-n most bound, p-p least** --
inverted against the two-nucleon data, where the p-n `3S1` channel is the only
bound one (+2.2246 MeV) and n-n `1S0` is unbound.

This does **not** contradict `eigenvalue_channel_binding_criterion_probe`,
which got 4/4 two-nucleon signs: that criterion is built from the transfer
matrices' EIGENVALUES, not from `L`.  The two are different functionals of the
same bond letters, and only one of them orders the channels correctly.  That
`L` -- the quantity the whole bond-graph binding path is built on -- is the one
that gets it wrong is worth recording on its own, and it is not something this
probe set out to test.  Flagged, not chased.

## What is NOT claimed

  * NOT a binding value.  Nothing is wired, nothing is fitted.  The one scan
    is over `r` and is used to locate a SIGN CHANGE, never to fit a magnitude.
  * NOT that the t-ladder miss is the extensive term.  It is the Model-G
    RESIDUAL; treating it as the target for an additive extension is R8's
    framing, adopted here so this result composes with R8's, and it is the
    framing the P1 invariant is stated in.
  * NOT that a turnover would VALIDATE the form.  Reproducing one sign
    condition is necessary, not sufficient.

Scope **(a)** for the measurements.  Claim A, once its `L > 0` premise is
measured, is scope **(b)** for the append/prepend orderings: a monotonicity
argument, not a numerical near-miss.

NO FLOAT64: mpmath `mpf` end to end at 50 dps, 50-digit proton pin.  Grid
values are built from strings, never from float literals.
"""

from __future__ import annotations

import json as _json
import sys as _sys
from pathlib import Path as _Path

_HERE = _Path(__file__).resolve().parent
_sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _li_2_q_util import flavor_split_leading  # noqa: E402
from codata_constants import _ame_binding_mev  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 50

# --- the t-ladder, rebuilt from the SAME committed data R9 uses --------------
A_LIGHT = 3
LADDER = {1: ("7Li", 3, 7), 2: ("11B", 5, 11), 3: ("15N", 7, 15),
          4: ("19F", 9, 19)}
_DL = _HERE.parent / "deltalambda"

ALPHA_BLOCK = "pnpn"
TRITON_BLOCK = "pnn"


def fmt(x, n=10):
    return mp.nstr(x, n)


def ladder_miss():
    """Model-G miss M(k), rebuilt exactly as saturating_shared_channel_probe does."""
    with open(_DL / "alpha-activation-brunnian.witness.json",
              encoding="utf-8") as _fh:
        W = _json.load(_fh)
    rows = W["model_G_per_isotope"]
    b = mp.mpf(str(W["inputs"]["b_linear_MeV_per_nucleon"]["value"]))

    def one(name, Z, A, k):
        if name in rows:
            r = rows[name]
            return (mp.mpf(str(r["deficit_MeV"]))
                    - mp.mpf(str(r["pred_deficit_MeV"])))
        deficit = (_ame_binding_mev(Z, A)
                   - k * _ame_binding_mev(2, 4) - _ame_binding_mev(1, 3))
        aa = (3 * b) * (k * (k - 1) // 2) if k >= 3 else mp.mpf(0)
        return deficit - (aa + k * A_LIGHT * b)

    return {k: one(nm, Z, A, k) for k, (nm, Z, A) in LADDER.items()}


def bond_constants():
    """L_XY and the DERIVED spectral-gap decay rates r_XY.  Same closed forms as
    spectral_gap_bond_decay_probe / allpairs_distance_decay_probe."""
    q = Q_MP
    h = q - 1 / q
    z = q**3 / (q**2 + 1)
    dx = flavor_split_leading(q)
    lw = mp.log(1 - h)
    w = mp.mpf(1) / 2 - dx / 4

    def L(d, e):
        return -mp.log(z + d) - e / 2 * lw

    Lb = {"pp": L(mp.mpf(0), mp.mpf(1)),
          "nn": L(-h, mp.mpf(-1)),
          "pn": L(-h * w, 2 * w - 1)}

    def gap(d):
        tr, dt = h + 2 * d, (h + d) * d - 1
        rt = mp.sqrt(tr * tr - 4 * dt)
        e = sorted([(tr + rt) / 2, (tr - rt) / 2], key=lambda x: -abs(x))
        return abs(e[1]) / abs(e[0])

    rb = {"pp": gap(mp.mpf(0)), "nn": gap(-h), "pn": gap(-h * w)}
    return q, h, Lb, rb


def V(seq, Lb, rb):
    """The decayed all-pairs sum over a nucleon string, exact in mpmath."""
    tot = mp.mpf(0)
    n = len(seq)
    for i in range(n):
        for j in range(i + 1, n):
            t = "pp" if seq[i] == seq[j] == "p" else (
                "nn" if seq[i] == seq[j] == "n" else "pn")
            tot += Lb[t] * rb[t] ** (j - i - 1)
    return tot


# --- the four orderings ------------------------------------------------------
def order_append_tail(k):
    """triton first, alphas appended: NO existing adjacency is ever split."""
    return TRITON_BLOCK + ALPHA_BLOCK * k


def order_prepend_head(k):
    """alphas prepended, triton at the tail: also splits nothing."""
    return ALPHA_BLOCK * k + TRITON_BLOCK


def order_insert_centre(k):
    """each new alpha inserted at the CENTRE of the current string: this DOES
    split an existing adjacency, so existing pairs are pushed apart."""
    s = TRITON_BLOCK
    for _ in range(k):
        m = len(s) // 2
        s = s[:m] + ALPHA_BLOCK + s[m:]
    return s


def order_alternating(k):
    """fully interleaved p/n over the whole nucleus -- NOT built incrementally,
    so nothing forces monotonicity a priori."""
    _, Z, A = LADDER[k]
    N = A - Z
    out, p, n = [], Z, N
    while p or n:
        if p:
            out.append("p")
            p -= 1
        if n:
            out.append("n")
            n -= 1
    return "".join(out)


ORDERINGS = [("append_tail", order_append_tail, True),
             ("prepend_head", order_prepend_head, True),
             ("insert_centre", order_insert_centre, False),
             ("alternating", order_alternating, False)]


def main() -> int:
    q, h, Lb, rb = bond_constants()
    M = ladder_miss()

    print("=" * 78)
    print(" ALL-PAIRS-WITH-DECAY vs THE t-LADDER INTERIOR MAXIMUM")
    print(" formalize-first: Claim A is stated in the docstring, BEFORE the scan")
    print("=" * 78)
    print(f"q = {fmt(q, 17)}   h = {fmt(h)}")

    print("\n[0] the target -- t-ladder Model-G miss, rebuilt from committed data")
    print("-" * 78)
    print(f"    {'k':>2} {'iso':5s} {'M(k) MeV':>10s}")
    for k, (nm, _Z, _A) in LADDER.items():
        print(f"    {k:>2} {nm:5s} {float(M[k]):10.4f}")
    turn = M[3] > M[4]
    print(f"    interior maximum at k=3?  M(3) > M(4):  {turn}")
    assert turn, "the t-ladder turnover is the whole premise; it must hold"
    # --- small discrepancy, recorded rather than smoothed over ---------------
    # R9's docstring states the invariant as `0 = M(1) < M(2) < M(3) > M(4)`.
    # Its OWN modelg_miss (reproduced here byte-for-byte) returns M(1) = +0.1219
    # for 7Li, not 0.  The witness row carries resid_MeV = -0.1218526 and
    # deficit - pred = +0.1218526, i.e. the witness defines resid with the
    # opposite sign to modelg_miss.  So "0 =" in that docstring is a
    # simplification of its own code's output, not a computed zero.
    m1 = M[1]
    print(f"    NOTE: R9's docstring writes this rung as 0.000; the same rebuild")
    print(f"          gives M(1) = {float(m1):+.4f}.  The witness row's own")
    print(f"          resid_MeV = -0.1218526 is the SAME magnitude, opposite")
    print(f"          sign -- a resid-convention difference, not a discrepancy")
    print(f"          in the data.  The invariant is UNAFFECTED: what P1 needs")
    print(f"          is the turnover M(3) > M(4), and M(1) < M(2) still holds.")
    assert abs(abs(m1) - mp.mpf("0.1218526500000021")) < mp.mpf("1e-9"), (
        "M(1) must match the committed 7Li resid magnitude")
    assert m1 < M[2] < M[3], "the rising leg must hold too"

    print("\n[1] PREMISE OF CLAIM A -- are all three L_XY strictly positive?")
    print("-" * 78)
    for t in ("pp", "pn", "nn"):
        print(f"    L_{t} = {fmt(Lb[t]):>14}   > 0 ?  {Lb[t] > 0}")
    all_pos = all(Lb[t] > 0 for t in Lb)
    print(f"    all strictly positive: {all_pos}")
    print(f"    DERIVED decay rates:  r_pp = {fmt(rb['pp'])}  "
          f"r_nn = {fmt(rb['nn'])}  r_pn = {fmt(rb['pn'])}")
    assert all_pos, "Claim A's premise -- measured, not assumed"

    print("\n[2] CLAIM A, verified by direct computation over a WIDE r-grid")
    print("-" * 78)
    print("    Under append/prepend ordering, V(k) must be strictly increasing")
    print("    for EVERY (r_pp, r_nn, r_pn) in (0,1]^3.  Grid over 3 decades:")
    grid = [mp.mpf(s) for s in ("0.001", "0.01", "0.1", "0.3", "0.5",
                                "0.7", "0.9", "0.99", "0.9999", "1")]
    viol = {nm: 0 for nm, _f, _m in ORDERINGS}
    tested = 0
    nonmono = {nm: 0 for nm, _f, _m in ORDERINGS}
    turn_hits = {nm: 0 for nm, _f, _m in ORDERINGS}
    for a in grid:
        for bb in grid:
            for c in grid:
                r = {"pp": a, "nn": bb, "pn": c}
                tested += 1
                for nm, fn, monotone_expected in ORDERINGS:
                    v = [V(fn(k), Lb, r) for k in (1, 2, 3, 4)]
                    inc = all(v[i + 1] > v[i] for i in range(3))
                    if not inc:
                        nonmono[nm] += 1
                        if monotone_expected:
                            viol[nm] += 1
                    if v[2] > v[3]:
                        turn_hits[nm] += 1
    print(f"    grid points tested: {tested}   (10^3 over r in (0,1]^3)")
    print(f"    {'ordering':14s} {'splits?':>8s} {'non-monotone':>13s} "
          f"{'V(3)>V(4)':>10s} {'CLAIM-A viol':>13s}")
    for nm, _fn, mono in ORDERINGS:
        print(f"    {nm:14s} {('no' if mono else 'yes'):>8s} "
              f"{nonmono[nm]:>13d} {turn_hits[nm]:>10d} "
              f"{(viol[nm] if mono else 0):>13d}")
    assert viol["append_tail"] == 0 and viol["prepend_head"] == 0, (
        "CLAIM A refuted: a non-splitting ordering went non-monotone")
    print()
    print("    => CLAIM A CONFIRMED on the grid: zero violations in 1000 points")
    print("       for BOTH non-splitting orderings.  Under append/prepend the")
    print("       decayed all-pairs form is EXCLUDED by P1 for ANY decay rates.")
    print("       Decay cannot rescue it -- it shrinks contributions but never")
    print("       removes one, so the sum can only grow as pairs are added.")

    print("\n[3] THE DERIVED RATES -- what the framework's OWN r_XY give")
    print("-" * 78)
    print("    No scan, no fit: the three spectral gaps measured in")
    print("    spectral_gap_bond_decay_probe, on all four orderings.")
    print(f"    {'ordering':14s} {'V(1)':>11s} {'V(2)':>11s} {'V(3)':>11s} "
          f"{'V(4)':>11s} {'turnover':>9s}")
    derived_turn = {}
    for nm, fn, _m in ORDERINGS:
        v = [V(fn(k), Lb, rb) for k in (1, 2, 3, 4)]
        derived_turn[nm] = v[2] > v[3]
        print(f"    {nm:14s} " + " ".join(f"{float(x):11.4f}" for x in v)
              + f" {str(v[2] > v[3]):>9s}")
    any_derived = any(derived_turn.values())
    print()
    print(f"    turnover reproduced at the DERIVED rates on any ordering? "
          f"{any_derived}")
    if not any_derived:
        print("    NO.  So the framework's own spectral gaps do not produce the")
        print("    interior maximum on ANY of the four orderings -- including the")
        print("    two that P1 does not already exclude.  This is a scope-(a)")
        print("    negative on the decayed all-pairs form AS PARAMETERISED BY")
        print("    THE FRAMEWORK, independent of Claim A.")

    print("\n[3a] ARRANGEMENT-FREE BOUND -- and it is INCONCLUSIVE, deliberately")
    print("-" * 78)
    print("    Four hand-picked orderings are four data points, not a theorem.")
    print("    The arrangement-free fact: the number of pairs at separation s in")
    print("    an A-strand word is EXACTLY (A - s), whatever the arrangement.  So")
    print("    with w(t,s) = L_t * r_t^(s-1),")
    print("        SUM_s (A-s)*min_t w(t,s)  <=  V(A)  <=  SUM_s (A-s)*max_t w(t,s)")
    print("    If Lo(19) > Up(15) the turnover would be impossible for EVERY")
    print("    ordering.  Measured at the derived rates:")

    def w(t, s):
        return Lb[t] * rb[t] ** (s - 1)

    def bounds(A):
        lo = hi = mp.mpf(0)
        for s in range(1, A):
            ws = [w(t, s) for t in ("pp", "pn", "nn")]
            lo += (A - s) * min(ws)
            hi += (A - s) * max(ws)
        return lo, hi
    lo15, hi15 = bounds(15)
    lo19, hi19 = bounds(19)
    print(f"      A=15 (k=3):  Lo = {float(lo15):8.4f}   Up = {float(hi15):8.4f}")
    print(f"      A=19 (k=4):  Lo = {float(lo19):8.4f}   Up = {float(hi19):8.4f}")
    decisive = lo19 > hi15
    print(f"      Lo(19) > Up(15) ?  {decisive}")
    if not decisive:
        print("      NO -- the intervals OVERLAP, so this bound does NOT exclude a")
        print("      turnover for arbitrary orderings.  Recorded as inconclusive")
        print("      rather than dropped: it is the honest statement of how far")
        print("      the arrangement-free argument reaches, and it stops short of")
        print("      where sections [2]-[3] read as if they had arrived.")

    print("\n[3b] RANDOMISED ARRANGEMENT SEARCH -- max V(3) vs min V(4)")
    print("-" * 78)
    print("    Since the bound is inconclusive, search arrangements directly.")
    print("    The four ladder rungs are INDEPENDENT nuclei, so a turnover needs")
    print("    only SOME arrangement of 15N beating SOME arrangement of 19F.")
    print("    Test the extreme case: max over arrangements at k=3 vs min at k=4.")
    def _lcg(n):
        # deterministic, seeded, reproducible -- no wall-clock, no RNG import
        x = 12345
        out = []
        for _ in range(n):
            x = (1103515245 * x + 12345) % (2**31)
            out.append(x)
        return out

    def shuffled(Z, N, seed_stream, off):
        arr = ["p"] * Z + ["n"] * N
        m = len(arr)
        for i in range(m - 1, 0, -1):
            j = seed_stream[(off + i) % len(seed_stream)] % (i + 1)
            arr[i], arr[j] = arr[j], arr[i]
        return "".join(arr)

    stream = _lcg(20000)
    NSAMP = 400
    ext = {}
    for k in (3, 4):
        _nm, Z, A = LADDER[k]
        N = A - Z
        vals = [V(shuffled(Z, N, stream, 97 * k * (i + 1)), Lb, rb)
                for i in range(NSAMP)]
        ext[k] = (min(vals), max(vals))
        print(f"    k={k} ({_nm}, Z={Z} N={N}): over {NSAMP} random arrangements")
        print(f"         min V = {float(ext[k][0]):9.4f}   "
              f"max V = {float(ext[k][1]):9.4f}   "
              f"spread = {float(ext[k][1] - ext[k][0]):7.4f}")
    sep = ext[4][0] - ext[3][1]
    print(f"    min V(4) - max V(3) = {float(sep):9.4f}")
    if sep > 0:
        print("    POSITIVE, and by a wide margin: over 400 random arrangements")
        print("    each, the WORST 19F still exceeds the BEST 15N.  No turnover")
        print("    is reachable by re-ordering at the derived rates.  Scope-(a)")
        print("    -- a sample, not a proof, and it is why [3a] is kept.")
    else:
        print("    NON-POSITIVE: re-ordering alone can reach the turnover, so the")
        print("    negative in [3] is ordering-conditional after all.")

    print("\n[4] IS THE TURNOVER REACHABLE AT ALL, on a splitting ordering?")
    print("-" * 78)
    reach = [nm for nm, _f, m in ORDERINGS if not m and turn_hits[nm] > 0]
    if reach:
        print(f"    YES, on: {', '.join(reach)}")
        print("    So splitting orderings are NOT excluded by P1 -- the negative")
        print("    contribution from pushing existing pairs apart can win.  The")
        print("    surviving class is therefore narrow and specific:")
        print("      * the ordering must SPLIT existing adjacencies as clusters")
        print("        are added (append/prepend are dead, for any r), AND")
        print("      * the decay rates must lie in the turnover region, which")
        print("        the framework's derived gaps do NOT (section [3]).")
    else:
        print("    NO -- not reachable anywhere on this grid, on any ordering.")
        print("    Then the exclusion is not ordering-conditional at all.")

    print("\n[5] WHAT THIS DOES AND DOES NOT SETTLE")
    print("-" * 78)
    print("  SETTLED (scope-(b), premise L_XY > 0 measured in [1]):")
    print("    append/prepend orderings + decayed all-pairs is excluded by P1")
    print("    for EVERY (r_pp, r_nn, r_pn).  Adding decay does not escape R8.")
    print("  SETTLED (scope-(a)):")
    print("    the framework's OWN spectral-gap rates reproduce no turnover on")
    print("    any of the four orderings tested.")
    print("  NOT SETTLED:")
    print("    whether a splitting ordering is the physically right one, and")
    print("    whether any DERIVED (not fitted) r could sit in the turnover")
    print("    region.  Both are open; neither is answered by a scan.")
    print("  NOT CLAIMED:")
    print("    no binding value, nothing wired, nothing fitted.  The r-grid")
    print("    locates a SIGN CHANGE only; no magnitude is read off it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
