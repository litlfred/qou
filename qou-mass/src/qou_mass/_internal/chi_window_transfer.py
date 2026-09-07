#!/usr/bin/env python3
"""chi_window_transfer — `chi^lambda` for a BLOCK-monotone word, `d_lambda`-free.

The fine-Bratteli transfer (`chi_monotone_transfer`) is fast because it never
materialises `d_lambda`, and it is restricted to MONOTONE words because it uses
only the DIAGONAL seminormal entry per step. The corrected Borromean atom word
is not monotone — it interleaves `sigma_0` and `sigma_1` within each nucleon —
so `tr_m_atom_via_transfer` currently routes it to the general-word Rust kernel,
which is correct and `d_lambda`-BOUND: A=3 costs 0.36 s, A=4 costs 621 s, A>=5 is
impractical (bean `qou-wdij`).

This module is the `O(A)` route for that word.

## The two facts that make it work

**1. A swap does not move the shape.** `sigma_g` exchanges the boxes carrying
entries `g+1` and `g+2`. Adding two boxes in either order yields the SAME
partition, so `sigma_g` leaves `s_{g+2}` invariant and changes only *which* box
sits at level `g+1` — that is, the content `c_{g+1}`. So a state consisting of a
shape plus the **ordered contents of the last few boxes** is closed under the
generators, with no need to carry the boxes' positions.

A corollary falls out and is worth naming, because it removes a case analysis:
the swap is invalid exactly when the two boxes share a row or column adjacently,
which is exactly `|delta| = 1`. So "is the swapped tableau standard" and "is the
block 1x1" are the same test, and the 1x1 value is `q` (`delta = +1`, same row)
or `-1/q` (`delta = -1`, same column).

**2. The trace needs the chain to RETURN, and a forward sweep loses that.**
`chi^lambda(W) = sum_T <T|rho(W)|T>` — the final chain must equal the initial
one. The monotone transfer gets this for free: each `O_g` is applied once at its
own level, so only diagonal paths survive. Under interleaving an off-diagonal
move must be undone by a later one, and a plain forward sweep cannot see that.

So the state carries BOTH the initial and the current contents of the live
levels. When a level is retired — no remaining letter touches it — the two are
required to match and the level is dropped. Terms that fail are discarded; that
requirement IS the trace.

The live window is bounded (letters on generator `g` touch levels `g+1, g+2`,
and the atom word's letters are grouped into 3-strand nucleons in increasing
order), so the state space is bounded by shapes x contents^K x contents^K, never
`d_lambda`.

## Scope

Correct for ANY word, monotone or not — the retirement rule makes no
block-monotone assumption. It is *efficient* only when the word's live window
stays small, which is what "block-monotone" buys. A word that revisits generator
0 after generator `n-2` would keep every level live and the state space would
blow up; `MAX_LIVE` guards that rather than letting it consume the machine.

Validated against `chi_general_word.chi_all_lambda_general` (the Rust
general-word kernel) via `probes/chi_kernel_conformance_harness.py`. The
seminormal off-diagonal convention it uses — row form, `B = 1`,
`B' = D(delta) D(-delta) + 1`, no square root — is pinned in
`probes/seminormal_offdiagonal_convention_probe.py`.

NO float64: mpmath at the 50-dps floor throughout.
"""
from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


import mpmath as mp  # noqa: E402

from chi_monotone_transfer import _addable, _add, word_to_mpfr  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

# A word whose live window exceeds this many levels is not block-monotone in any
# useful sense; refuse rather than exhaust memory. Raised deliberately as a
# guard, not returned as a wrong answer.
MAX_LIVE = 12


def _D(delta, q, qi, h, cache):
    v = cache.get(delta)
    if v is None:
        v = h / (1 - q ** (-2 * delta))
        cache[delta] = v
    return v


def chi_all_lambda_window(word, n: int, *, dps: int = 50, q=None):
    """`{lambda |- n: chi^lambda(word)}` for an arbitrary word, `d_lambda`-free.

    State: `(shape, init_tail, cur_tail)` where the tails are the contents of the
    live levels — `init_tail` as the chain entered them, `cur_tail` as the word
    has rearranged them. A level retires when no remaining letter touches it, and
    retiring requires `init == cur` there; that requirement is the trace.
    """
    if mp.mp.dps < dps:
        mp.mp.dps = dps
    if q is None:
        q = mp.mpf(Q_50_DIGIT_STR)
    qi = 1 / q
    h = q - qi
    Dc = {1: q, -1: -qi}

    letters = list(word_to_mpfr(word, q))

    # last_touch[level] = index of the final letter that touches that level.
    # sigma_g touches levels g+1 and g+2 (1-indexed levels of the chain).
    last_touch: dict[int, int] = {}
    for idx, (_d, g) in enumerate(letters):
        last_touch[g + 1] = idx
        last_touch[g + 2] = idx

    # state: (shape, init_tail, cur_tail) -> amplitude. `lo` is the lowest live
    # level; tails cover levels lo .. frontier inclusive.
    amp: dict[tuple, object] = {((), (), ()): 1}
    frontier = 0
    lo = 1

    # Seeding the accumulators with an mpf zero rather than Python's int 0
    # removes an int->mpf coercion on the FIRST write to every key. Profiled at
    # 7Li: `mpmath.ctx_mp_python.convert` was called 3.77 million times for
    # exactly that, ~3 s of a 58 s run.
    _zero = mp.mpf(0)

    for idx, (d_mp, g) in enumerate(letters):
        # 1. extend the chain until both levels this letter needs exist
        while frontier < g + 2:
            frontier += 1
            new = defaultdict(lambda: _zero)
            for (shape, it, ct), a in amp.items():
                for (r, c) in _addable(shape):
                    s2 = _add(shape, (r, c))
                    cc = c - r
                    new[(s2, it + (cc,), ct + (cc,))] += a
            amp = dict(new)
            if frontier - lo + 1 > MAX_LIVE:
                raise ValueError(
                    f"live window {frontier - lo + 1} exceeds MAX_LIVE={MAX_LIVE}; "
                    "this word is not block-monotone in a useful sense")

        # 2. apply the letter: sigma_g + d, acting on tail positions for levels
        #    g+1 and g+2.
        #
        # Both coefficients depend ONLY on `delta` and this letter's `d`, never
        # on the state, so they are computed once per distinct delta instead of
        # once per state. At 7Li that is a few dozen evaluations replacing
        # ~130k of `diag + d_mp` and the same again of `diag * other + 1`.
        i = (g + 1) - lo
        j = (g + 2) - lo
        coef: dict[int, tuple] = {}

        def _coef(delta, _c=coef, _d=d_mp):
            v = _c.get(delta)
            if v is None:
                diag = _D(delta, q, qi, h, Dc)
                if abs(delta) == 1:
                    v = (diag + _d, None)          # 1x1 block: no swap partner
                else:
                    other = _D(-delta, q, qi, h, Dc)
                    v = (diag + _d, diag * other + 1)
                _c[delta] = v
            return v

        new = defaultdict(lambda: _zero)
        for (shape, it, ct), a in amp.items():
            ci, cj = ct[i], ct[j]
            delta = cj - ci
            on_diag, off_diag = _coef(delta)
            new[(shape, it, ct)] += a * on_diag
            if off_diag is None:
                # swapped chain is not standard: 1x1 block, sigma = q or -1/q,
                # which is exactly D(+-1).
                continue
            # 2x2 row form: diagonal D(delta), off-diagonal 1 going one way and
            # D(delta) D(-delta) + 1 the other. See the convention probe.
            swapped = list(ct)
            swapped[i], swapped[j] = cj, ci
            new[(shape, it, tuple(swapped))] += a if ci < cj else a * off_diag
        amp = dict(new)

        # 3. retire levels no later letter touches: require init == cur there.
        while lo <= frontier and last_touch.get(lo, -1) <= idx:
            k = lo - lo  # always 0: we retire from the low end
            new = defaultdict(lambda: _zero)
            for (shape, it, ct), a in amp.items():
                if it[k] != ct[k]:
                    continue                      # chain did not return: not on the diagonal
                new[(shape, it[1:], ct[1:])] += a
            amp = dict(new)
            lo += 1

    # 4. extend to n boxes; the remaining levels are untouched by any letter, so
    #    they are automatically diagonal.
    while frontier < n:
        frontier += 1
        new = defaultdict(lambda: _zero)
        for (shape, it, ct), a in amp.items():
            for (r, c) in _addable(shape):
                new[(_add(shape, (r, c)), it, ct)] += a
        amp = dict(new)

    out = defaultdict(lambda: _zero)
    for (shape, it, ct), a in amp.items():
        if it != ct:
            continue
        out[shape] += a
    return dict(out)
