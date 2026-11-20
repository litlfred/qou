#!/usr/bin/env python3
r"""
rev_e_infinity_xbot_relaxation_probe.py — the BOTTOM edge's value is concave too, so `sup_s Xbot`
is a concave program; certifying it BYPASSES gap G1 (qou-hok7)

#7349 closed G2 by certifying the top edge: `Xblock` is concave in the displacement vector, so
maximising it over real `u` is a relaxation, and a supergradient certificate makes that maximum
rigorous (slack 6.4e-12).  What is left is **G1** — `Xbot(s) <= Xblock(s)` — which licenses the
join's `Xbot := Xblock` substitution and is the last conditionality on `e_inf`.

`rev_e_infinity_g1_bottom_edge_cap_probe.py` showed that **no enumeration can settle G1**: a
capped maximum is a LOWER bound on its own supremum, and a lower bound can only refute an
inequality, never prove it.  `rev_e_infinity_xbot_coercivity_probe.py` then showed the top
edge's per-row linearisation *does* reach the bottom edge — 0 violations over 17,534 (profile,
pe) pairs — but caps `Xbot` at 20.78 against an enumerated maximum of 2.16, a factor of **9.6**.
That is the same failure `B_sharp` had on the top edge (1.82x), for the same reason: a per-row
tangent has no cap while the real gain saturates.

The fix on the top edge was not a better constant but a bound that **bends** — the concavity of
the objective itself.  This probe carries that across.

## The G1 bypass, stated

The join needs `Xblock(s_t) + Xrun(s_t + s_b) + Xbot(s_b)` to fall below `e_inf` outside a finite
window.  #7349 got that from `Xbot <= Xblock <= B_top`, i.e. **through G1**.  With a certified
`B_bot` in hand the same cut follows from `Xblock <= B_top` and `Xbot <= B_bot` **separately**,
and G1 is not used at all.  G1 is not proved by this; it is *removed from the argument*, which
is what the `e_inf` closure actually needs.

## Why the extension to real `u` is not automatic

`delta_excess` is defined on integers and its one-body term is `fi(beta) - fi(b0)` with
`fi(b) = sum_{m=1}^{b} eps(m)` — a partial sum, which has no canonical real extension.  Two
candidates differ in kind:

  - `integral_0^u eps(b0 + t) dt` is concave and, since `eps` is decreasing, an **upper** bound
    on the partial sum — so it relaxes, but it does not restrict to the integer value, and the
    relaxation would carry avoidable slack at every integer point.
  - `R(b0) - R(b0 + u)` with `R(x) = sum_{j>=1} eps(x + j)` is **exact** at integers
    (`fi(b) + R(b) = sum_{m>=1} eps(m)`, a constant that cancels) and concave in `u`, since
    `-R'(x) = sum_j gx(x+j)` is decreasing.

The second is used.  R1 checks it against the committed `delta_excess` rather than asserting it.

Everything else extends termwise: each pair term is `-eps(g + (u_i - u_j))`, concave composed
with a linear map; the above-block tail is `-eps(g - u_j)`; the cost is
`-(ln q0/2)(2 lin + sum u^2)`.  So the extended objective is concave — R2 measures it.

## The domain is the ordering constraint, and it is free

`eps(x) -> +infinity` as `x -> 0+`, so every term `-eps(g + d)` carries a log barrier exactly
where `beta` would stop being strictly decreasing.  The feasible set is the open convex
polyhedron `{beta strictly decreasing}` with the barrier already in the objective: the ordering
constraint does not have to be imposed, and dropping it is not an option either.  That is one
structural difference from the top-edge program, where #7349 dropped the AP ordering as a
further relaxation and observed it held at the optimum anyway.

## The length bound does NOT transfer, and the reason is the class

#7349's `T0` works because its blocks have every entry `>= 1`, so a row whose tangent slope is
below `ln q0 / 2` contributes a strictly NEGATIVE cap and the cumulative cap eventually falls
below the certified bound.  The bottom class permits **zero** entries (`bot_profiles` requires
only the leading one to be positive), so the relaxation's lower bound is `u_j >= 0`, every row
cap is `>= 0`, and the cumulative cap is non-decreasing in `T`.  **There is no `T0` of that
shape here** — the analogy breaks, and pretending otherwise would be the error this file exists
to avoid.

What replaces it starts from a better fact.  The per-row slope `Gamma_j` turns out to be
**exactly independent of `T`**: the block rows above `j` and the undisplaced tail above the block
are the same sum split in two places.  So a length-`T` program is the restriction of one infinite
program to its first `T` coordinates, `sup_T G_T = sup G_infinity`, and the certificate can be
taken once at the best ascent point **padded with zeros** — padding changes neither `G(w)` nor
any box.

The first version of this file then asserted that each padded row is charged *exactly zero*
(gradient `<= 0` puts the box maximum at `lo_j = 0 = w_j`).  **That is false here, and the
measurement is what says so.**  In the pure AP the downward pair gains and the upward pair losses
cancel term for term, leaving

    Gamma_j  =  Rg(b0_j) - sum_{d>j} gx(2d)  =  sum_{i odd >= 1} gx(b0_j + i) ,

the ODD gaps the one-body term reaches and the gap-2 ladder does not — strictly positive at
**every** row.  So no cap is ever zero and no padded row is ever free.  What is true is that the
charges decay geometrically (`T2^(-2)` per AP row), so the certificate carries rows until the
marginal charge is negligible and then **bounds** the remainder by its geometric tail rather than
dropping it.  The result is still one number bounding every block length at once; it is just not
free.  (A termination test written for `cap == 0` never fires, which is how the false version was
caught — by a guard that refused to return a truncated sum, not by inspection.)

## Frame geometry

Indexing from the BOTTOM of the frame (`j = 0` is the last row), `staircase_beta(k, k+1+pe)` is

    b0(j) = j            for j < pe      the gap-1 wall
          = 2j - pe      for j >= pe     the gap-2 AP

continuous at `j = pe`, junction gap 1.  A block of length `T` occupies `j = 0..T-1`; the rows
above are undisplaced and their gaps from block row `j` are `h_j + Delta` with
`h_j = b0(T) - b0(j)` and `Delta` — the gap set of the rows above the block relative to the first
of them — depending only on `(pe, T)`.  So the whole above-block tail is `W(h_j) - W(h_j - u_j)`
for a single `W(y) = sum_{delta in Delta} eps(y + delta)`, resummed in closed form.
`h_j - u_j > 0` **is** the barrier.

The wall also carries a linear cost `ln q0 * sum_{j < pe} (pe - j) u_j` that the top edge has no
analogue of, and `pe` is a second unbounded dimension that was a **cap** in the enumeration
(`P_EXT_MAX = 8`), not a bound.  R5 bounds it: once the wall is deep enough, that cost sinks
every block below the incumbent.

## The plain relaxation is valid and NOT tight, and the reason is the class again

`Gamma_j > 0` at every row, so a real `u` can take an arbitrarily small displacement on
arbitrarily many rows and collect a strictly positive gain from each.  No integer block can do
that — its entries jump from 0 to 1 — and the top edge never sees it, because its class forces
`u >= 1`.  Measured: the relaxed sup does not settle in `T` (`pe = 2`: still `+0.2301` at
`T = 6`), and the all-`T` bound at `pe = 1` is `4.0897` against an ascent value of `2.2857`.

The fix is a **valid inequality**, not more compute.  Every integer `u_j >= 0` satisfies
`u_j^2 >= u_j`, so for any `lam >= 0`

    sup over INTEGER u of G  <=  sup over REAL u >= 0 of [ G(u) + lam * sum_j (u_j^2 - u_j) ] ,

and because `+lam sum u^2` eats into `G`'s own `-(ln q0/2) sum u^2`, the right-hand program is
still **concave** for `lam < ln q0 / 2`.  The charge `-lam u_j` falls on exactly the rows the
relaxation was exploiting: every row with `Gamma_j < lam` is driven to zero, which truncates the
accumulation at a finite support — and makes those rows cost the certificate nothing, since a
negative gradient at `w_j = 0 = lo_j` is charged `g_j (lo_j - w_j) = 0`.

**Select `lam` on the certificate, not on the tangent sum.**  The T-free tangent sum goes the
*wrong* way with `lam` (14.17 at `lam = 0` rising to 251 near the concavity limit), because the
cap is `Gamma'^2 / (2(ln q0 - 2 lam))` and the denominator collapses faster than the numerator
shrinks on the dominant row, where `Gamma ~ 1.42 >> lam`.  Choosing by that proxy returns
`lam = 0` and discards the whole tightening.

## Checks

  R1  the real extension reproduces the committed integer `delta_excess` at integer `u`
  R2  the extended objective is concave — random feasible triples, not assumed
  R3  the resummed `R`, `W` and their gradients against direct sums, the analytic gradient
      against a central difference, and the `T`-independence of `Gamma`
  R4  the relaxed supremum per `(pe, T)` with a supergradient certificate at each — valid,
      converged (KKT residual and the `sup` non-decreasing in `T`), and measurably not tight
  R5  the `u^2 >= u` tightening, the all-`T` certificate and the rigorous `pe` bound
  R5b the same certificate on the INTEGER box `[ceil(lo_j), floor(U_j)]` — sound for `Xbot`,
      which is an integer maximum, and never looser than the real box
  R6  what a certified `B_bot` buys: the cut that follows from `B_top` and `B_bot` separately,
      with G1 not used

Proton-pinned; `mp.dps = 25`; no float64.

## Running it inside a 120-minute window

The full run is ~200 min.  R1..R5 are keyed checkpoints and every ascent and `xrun` call is
disk-memoised (see the block above `R1`), so a killed run is simply re-run: finished stages
replay in seconds and a half-finished stage resumes at its last completed call.  The key is a
hash of the source and every input, so a restore can never return a number from other code.
`REV_XBOTR_CKPT=0` forces a cold run; `REV_XBOTR_CKPT_DIR` moves the store (default
`~/.cache/qou/xbot-relaxation-ckpt`).  The witness records which stages were restored.

-- Ref: [manuscript] content/quantum-observable-universe/lean/QOU/BraidKnot/SupergradientCertificate.lean
"""

from __future__ import annotations

import json
import os
import random
import sys
import time
from datetime import datetime, timezone

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMPUTATIONS = os.path.dirname(_HERE)
if _COMPUTATIONS not in sys.path:
    sys.path.insert(0, _COMPUTATIONS)

from mpmath import mp  # noqa: E402

# The committed integer evaluator, executed rather than re-derived: R1 is a comparison against
# the definition `bot_table` actually uses, so it has to be that definition.
_SRC = os.path.join(_HERE, "rev_e_infinity_edge_limit_probe.py")
_TEXT = open(_SRC).read()
_MARK = 'print("e_inf'
if _MARK not in _TEXT:
    raise SystemExit(f"driver banner {_MARK!r} not found in {_SRC} — refusing to guess a split")
_LIB: dict = {"__name__": "_edge_limit_defs", "__file__": _SRC}
exec(_TEXT[:_TEXT.index(_MARK)], _LIB)  # noqa: S102 — deliberate, and the split is asserted

_sc = _LIB["sc"]
_delta_excess = _LIB["delta_excess"]
_staircase_beta = _LIB["staircase_beta"]
_bot_profiles, _make_u, _bot_table = _LIB["bot_profiles"], _LIB["make_u"], _LIB["bot_table"]
_ap_value = _LIB["ap_value"]
K = _LIB["K_BOT"]

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.dps = 25
Q0 = Q_MP
LNQ = mp.log(Q0)
LNQ_HALF = LNQ / 2
T2 = Q0 ** 2
LNT2 = mp.log(T2)

TARGET_DIGITS = 20
_LN10 = mp.log(10)
TOL = mp.mpf(10) ** (-(TARGET_DIGITS - 4))
# every series below is evaluated at `T2^(-r y)` with `y >= 1`, so this many terms clears target
RSER = int(mp.ceil((TARGET_DIGITS + 3) * _LN10 / LNT2)) + 15
GTOL = mp.mpf(10) ** (-(TARGET_DIGITS + 3))

PEMAX = int(os.environ.get("REV_XBOTR_PEMAX", "8"))
TMAX = int(os.environ.get("REV_XBOTR_TMAX", "12"))
# Rows the ASCENT covers before the certificate starts padding.  This is the lever that matters
# most for the padded-row charge — more than `lam` is.  A padded row's gradient is its own slope
# PLUS a correction from the displaced rows below it (`gx(gap - u_j') > gx(gap)`), and it is that
# correction, not the slope, that dominates just above the block; both decay geometrically in
# `b0_j`, so moving the boundary up is what kills them.  Measured at pe = 2 with lam = 0: an
# ascent stopping at 14 rows leaves the padded rows costing 2.4707, and the certificate then has
# to carry 146 rows to reach a negligible marginal charge.  `lam` helps too but much less — at
# 0.2 of the concavity limit the same figure is 1.9710 — because the correction it has to beat
# is ~0.03 per row while `lam` there is 0.0104.
JPAD = int(os.environ.get("REV_XBOTR_JPAD", "26"))
BMAX = int(os.environ.get("REV_XBOT_BMAX", "10"))
BUMAX = int(os.environ.get("REV_XBOT_BUMAX", "3"))

E_INF_7335 = mp.mpf("2.43929645512078402706542884314")
# #7349's certified top-edge bound, READ from the witness that certifies it
# (rev-e-infinity-block-sup-relaxation, certificate_P8.bound) rather than typed
# (witness-value copy ratchet).
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "rev-e-infinity-block-sup-relaxation.witness.json"), encoding="utf-8") as _fh:
    B_TOP_CERT = mp.mpf(json.load(_fh)["certificate_P8"]["bound"])

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'ok ' if ok else 'FAIL'}] {name}: {detail}", flush=True)


# --------------------------------------------------------------------------------------------
# The real-argument kernel
# --------------------------------------------------------------------------------------------
def epsx(x) -> mp.mpf:
    return -mp.log(1 - T2 ** (-x)) if x > 0 else mp.inf


def gx(y) -> mp.mpf:
    """`-eps'(y)` in closed form.  ANALYTIC, not a finite difference — the supergradient
    inequality is about the true gradient, and a difference quotient would make the certificate
    a statement about the step size.

    **Refuses a non-positive argument.**  At `y <= 0` the expression `LNT2 z / (1 - z)` does not
    diverge or raise, it quietly returns a NEGATIVE number — so evaluating the gradient outside
    the domain looks like an ordinary answer.  That is how a coordinate search can walk out of
    the feasible region and report a converged point: one ascent here was maximising a
    coordinate over `[0, hi]` when the rows *below* it force `u_i > u_j - (b0_i - b0_j) > 0`,
    and the resulting garbage derivative sent it to an infeasible `0`."""
    if y <= 0:
        raise ValueError(
            f"gx({mp.nstr(y, 10)}): the beta gap is non-positive, i.e. the displacement has "
            f"left the domain.  eps is undefined there and this expression would return a "
            f"plausible negative number instead of failing.")
    z = T2 ** (-y)
    return LNT2 * z / (1 - z)


_E = [T2 ** (-r) / (1 - T2 ** (-r)) for r in range(1, RSER + 1)]
_ER = [_E[r - 1] / r for r in range(1, RSER + 1)]
_EG = [LNT2 * _E[r - 1] for r in range(1, RSER + 1)]


def R(x) -> mp.mpf:
    """`sum_{j>=1} eps(x + j)`, so `fi(beta) - fi(b0) = R(b0) - R(beta)` EXACTLY at integers —
    the constant `sum_{m>=1} eps(m)` cancels.  This is what makes the relaxation a relaxation of
    the RIGHT problem rather than of a nearby one."""
    z = T2 ** (-x)
    tot = mp.mpf(0)
    zp = mp.mpf(1)
    for r in range(RSER):
        zp *= z
        tot += _ER[r] * zp
    return tot


def Rg(x) -> mp.mpf:
    """`-R'(x) = sum_{j>=1} gx(x + j)`, decreasing — which is why `-R(b0+u)` is concave."""
    z = T2 ** (-x)
    tot = mp.mpf(0)
    zp = mp.mpf(1)
    for r in range(RSER):
        zp *= z
        tot += _EG[r] * zp
    return tot


def _D_coeffs(pe: int, Tlen: int):
    """`D_r = sum_{delta in Delta} T2^(-r delta)` for the gap set of the rows above the block:
    a finite step-1 head (the wall rows the block does not reach) then a geometric step-2 tail."""
    m = max(0, pe - Tlen)
    out = []
    for r in range(1, RSER + 1):
        t = T2 ** (-r)
        head = mp.fsum(t ** d for d in range(m)) if m else mp.mpf(0)
        out.append(head + t ** m / (1 - t ** 2))
    return out


_DC: dict[tuple[int, int], tuple[list, list]] = {}


def _Dcache(pe: int, Tlen: int):
    key = (pe, Tlen)
    if key not in _DC:
        D = _D_coeffs(pe, Tlen)
        # split off delta = 0 so the remaining series converges for every y > 0, not only y >= 1
        _DC[key] = ([(D[r - 1] - 1) / r for r in range(1, RSER + 1)],
                    [LNT2 * (D[r - 1] - 1) for r in range(1, RSER + 1)])
    return _DC[key]


def W(y, pe: int, Tlen: int) -> mp.mpf:
    """`sum_{delta in Delta} eps(y + delta)` — the whole above-block tail as one function."""
    c, _ = _Dcache(pe, Tlen)
    z = T2 ** (-y)
    tot = epsx(y)
    zp = mp.mpf(1)
    for r in range(RSER):
        zp *= z
        tot += c[r] * zp
    return tot


def Wg(y, pe: int, Tlen: int) -> mp.mpf:
    """`-W'(y) = sum_delta gx(y + delta)`."""
    _, cg = _Dcache(pe, Tlen)
    z = T2 ** (-y)
    tot = gx(y)
    zp = mp.mpf(1)
    for r in range(RSER):
        zp *= z
        tot += cg[r] * zp
    return tot


def b0_of(pe: int, j: int) -> int:
    """`staircase_beta(k, k+1+pe)` read from the BOTTOM: `j = 0` is the last row."""
    return j if j < pe else 2 * j - pe


def lin_w(pe: int, j: int) -> int:
    """The wall's extra linear cost weight on row `j` (`i - k`); zero in the AP.  No analogue on
    the top edge."""
    return pe - j if j < pe else 0


# --------------------------------------------------------------------------------------------
# The extended objective
# --------------------------------------------------------------------------------------------
LAM_MAX = LNQ_HALF          # the objective stops being concave at `lam = ln q0 / 2`


def G(u, pe: int, lam=None) -> mp.mpf:
    """`delta_excess` at REAL `u >= 0`, block at rows `j = 0..T-1` of the `pe` frame.  Returns
    `-inf` outside the domain, which is where the log barrier already sends it.

    **`lam` is a valid-inequality tightening, not a fudge.**  Every integer `u_j >= 0` satisfies
    `u_j^2 >= u_j`, so for any `lam >= 0` and every INTEGER point

        G(u)  <=  G(u) + lam * sum_j (u_j^2 - u_j)  =:  G_lam(u) ,

    and therefore `sup over integer u of G <= sup over real u >= 0 of G_lam`.  Adding
    `+lam sum u^2` eats into the objective's own `-(ln q0/2) sum u^2`, so `G_lam` stays concave
    for `lam < ln q0 / 2` and the relaxed program is still a concave program.

    It exists because the plain `u >= 0` relaxation is **valid but not tight**, for a reason the
    top edge does not have.  Every `Gamma_j` here is strictly positive (`cap_sum`), so a real `u`
    can take an arbitrarily small displacement on arbitrarily many rows and collect a strictly
    positive gain from each — which no integer block can do, since its entries jump from 0 to 1.
    Measured: at `pe = 2` the relaxed sup was still climbing at `T = 8` (2.5971, increments
    decaying only ~0.65 per row).  `lam` charges `-lam u_j` against exactly those rows and drives
    every row with `Gamma_j < lam` to zero, which truncates the accumulation at a finite support.
    """
    lam = mp.mpf(0) if lam is None else lam
    Tlen = len(u)
    tot = mp.mpf(0)
    bT = b0_of(pe, Tlen)
    for j in range(Tlen):
        b = b0_of(pe, j)
        y = (bT - b) - u[j]
        if y <= 0:
            return mp.mpf("-inf")
        tot += R(b) - R(b + u[j]) + W(mp.mpf(bT - b), pe, Tlen) - W(y, pe, Tlen)
    for j in range(Tlen):
        for jp in range(j + 1, Tlen):
            g = b0_of(pe, jp) - b0_of(pe, j)
            arg = g + u[jp] - u[j]
            if arg <= 0:
                return mp.mpf("-inf")
            tot += epsx(g) - epsx(arg)
    lin = mp.fsum(lin_w(pe, j) * u[j] for j in range(Tlen))
    return (tot - LNQ * lin - (LNQ_HALF - lam) * mp.fsum(x * x for x in u)
            - lam * mp.fsum(u))


def dG_coord(u, pe: int, i: int, x, lam=None) -> mp.mpf:
    """`dG/du_i` with `u_i` replaced by `x` — the 1-D derivative the ascent bisects on.

    `G` is concave, so this is strictly decreasing in `x`; a bisection to its root is both
    faster than a ternary search on `G` (one evaluation per halving instead of two per 1.5x
    shrink) and exactly the object the certificate needs."""
    lam = mp.mpf(0) if lam is None else lam
    Tlen = len(u)
    b = b0_of(pe, i)
    h = b0_of(pe, Tlen) - b
    s = Rg(b + x) - Wg(h - x, pe, Tlen)
    for j in range(Tlen):
        if j == i:
            continue
        if j > i:
            s -= gx((b0_of(pe, j) - b) + u[j] - x)
        else:
            s += gx((b - b0_of(pe, j)) + x - u[j])
    return s - LNQ * lin_w(pe, i) - (LNQ - 2 * lam) * x - lam


def gradG(u, pe: int, lam=None):
    """The exact gradient, term by term against `G`'s own definition."""
    return [dG_coord(u, pe, i, u[i], lam) for i in range(len(u))]


_GAMMA: dict[tuple[int, int], mp.mpf] = {}


def gamma(pe: int, j: int) -> mp.mpf:
    """The per-row tangent slope at `u = 0` — the real analogue of the coercivity probe's
    `Ghat_bot`, and **independent of the block length**.

    Every term of `G` is concave, hence under its tangent at `u = 0`: the one-body term under
    `Rg(b0) u`, a pair term under `gx(g)(u_jp - u_j)`, the above-block tail under `-Wg(h) u`.
    Summing separates `G <= sum_j [u_j Gamma_j - (ln q0/2) u_j^2] - ln q0 * lin`.

    That `T`-independence is not an approximation: the block rows above `j` and the undisplaced
    rows above the block are one sum split at an arbitrary place, so
    `-Wg(h_j) - sum_{j<jp<T} gx(...)` is `-sum_{jp>j} gx(...)` however `T` is chosen.  It is what
    lets one certificate cover every block length."""
    key = (pe, j)
    if key in _GAMMA:
        return _GAMMA[key]
    b = b0_of(pe, j)
    tot = Rg(b)
    for jp in range(j):                                   # rows BELOW: gain
        tot += gx(b - b0_of(pe, jp))
    jp = j + 1                                            # rows ABOVE: loss, to convergence
    while True:
        t = gx(b0_of(pe, jp) - b)
        tot -= t
        if t < GTOL:
            break
        jp += 1
    _GAMMA[key] = tot
    return tot


def gamma_p(pe: int, j: int, lam=None) -> mp.mpf:
    """`Gamma_j` net of the wall's linear cost and the valid-inequality charge — the slope that
    actually confines row `j`."""
    lam = mp.mpf(0) if lam is None else lam
    return gamma(pe, j) - LNQ * lin_w(pe, j) - lam


def row_cap(pe: int, j: int, lam=None) -> mp.mpf:
    """`max_{v >= 0} [v Gamma'_j - ((ln q0)/2 - lam) v^2]`.  Zero when `Gamma'_j <= 0` — the
    bottom class permits zero entries, so the lower bound is `v >= 0` and not the top edge's
    `v >= 1`, and `lam` is what makes that harmless."""
    lam = mp.mpf(0) if lam is None else lam
    gp = gamma_p(pe, j, lam)
    return gp * gp / (2 * (LNQ - 2 * lam)) if gp > 0 else mp.mpf(0)


# `Gamma_j` decays by a factor `T2^(-2)` per AP row (see `cap_sum`), so `row_cap` decays by
# `T2^(-4)`.  Both remainders are geometric and are BOUNDED below, never dropped.
# A padded row's charge decays by `T2^(-2)` per AP row and `T2^(-1)` per wall row; the padded
# rows always sit above the wall, but the conservative ratio costs nothing at a tail of ~1e-23,
# so use it rather than depend on which environment the padding landed in.
_TAIL_G = T2 ** (-1) / (1 - T2 ** (-1))      # sum_{i>=1} ratio^i, for a Gamma-like tail
_TAIL_C = T2 ** (-4) / (1 - T2 ** (-4))      # the same for a cap-like tail (cap ~ Gamma^2)


def cap_sum(pe: int, lam=None) -> mp.mpf:
    """`sum_{j>=0} row_cap(pe, j)` — finite, and a `T`-free upper bound on every program in this
    frame.  The analogue of `B_sharp`, and loose for the same reason.

    **Every `Gamma_j` is strictly positive**, which the first version of this function assumed
    away.  In the pure AP (`pe = 0`, `b0_j = 2j`) the downward pair gains and the upward pair
    losses cancel term for term, leaving

        Gamma_j  =  Rg(2j) - sum_{d>j} gx(2d)  =  sum_{i odd >= 1} gx(2j + i) ,

    i.e. the ODD gaps the one-body term reaches and the gap-2 ladder does not.  So the caps never
    reach zero, they decay geometrically at `T2^(-4)` — and a termination test written for
    `c == 0` never fires.  The remainder is bounded by its geometric tail rather than truncated,
    so what is returned is an upper bound and not a partial sum."""
    tot = mp.mpf(0)
    j = 0
    while True:
        c = row_cap(pe, j, lam)
        tot += c
        if j > pe + 4 and (c == 0 or c < GTOL):
            return tot + c * _TAIL_C
        j += 1
        if j > 4000:
            raise SystemExit(
                f"cap_sum(pe={pe}) did not decay by j = {j}.  Refusing to report a truncated "
                f"sum as a bound.")


def certificate(pe: int, w, incumbent, caps_total=None, rows_n=None, all_T=False, lam=None,
                integer_box=False):
    """A rigorous upper bound on `sup G` over the `pe` frame at block length `len(w)` — or, with
    `all_T`, at EVERY block length at once (see R5).

    `G` is concave, so `G(u) <= G(w) + grad G(w) . (u - w)` at every feasible `u`.  The linear
    term is unbounded on its own, so the region is confined first: the per-row tangent gives
    `G(u) <= phi_j(u_j) + sum_{j' != j} cap_j'`, so any `u` reaching the incumbent has
    `phi_j(u_j) >= incumbent - sum_{j' != j} cap_j'` — a quadratic inequality in one variable
    whose solution set is an interval `[L_j, U_j]`.  Outside that box `G` is already below the
    incumbent.

    The per-coordinate maximum is at `U_j` when `g_j >= 0` and at `lo_j` when `g_j < 0`.  The
    second case is the one that matters and the one #7349 got wrong first: at the optimum the
    constrained coordinates sit ON the lower boundary with strictly negative gradients (correct
    KKT behaviour), and charging them `|g_j| (U_j - lo_j)` instead inflates the slack by eleven
    orders of magnitude.  `naive` recomputes that figure every run rather than quoting it.

    **The all-`T` extension.**  `Gamma_j` is `T`-free (R3), so padding `w` with zeros changes
    neither `G(w)` nor any box, and the length-`T'` program for `T' > len(w)` is certified by the
    SAME inequality with the extra coordinates charged `g_j (U_j - 0)`.  Those charges are not
    zero — every `Gamma_j` is strictly positive (`cap_sum`) — but they decay geometrically, so
    the extension carries rows until the charge is negligible and then BOUNDS the remainder by
    its geometric tail instead of dropping it.  What comes back is an upper bound at every block
    length, not only at `len(w)`.

    **The integer box** (`integer_box=True`).  `Xbot` is a maximum over INTEGER blocks, and an
    integer `u` reaching the incumbent has `u_j in [L_j, U_j] ∩ Z = [ceil(lo_j), floor(U_j)]`.
    So the per-coordinate maximum of the linear term may be taken over that smaller interval:
    `g_j (floor(U_j) - w_j)` when `g_j >= 0`, `g_j (ceil(lo_j) - w_j)` when `g_j < 0`.  Both are
    `<=` the real-box charge (`floor(U) <= U` with `g >= 0`; `ceil(lo) >= lo` with `g < 0`), so
    the bound only tightens, and it stays a bound on the INTEGER supremum only — which is all
    `Xbot` needs, and all the `lam` program was ever valid for (`u^2 >= u` holds on integers
    only).  An empty integer interval means no integer point reaches the incumbent, and the
    frame is excluded.  Only the explicitly charged rows are rounded; the tail past them keeps
    its real-box bound, which dominates the integer one, so no new tail argument is needed.
    """
    lam = mp.mpf(0) if lam is None else lam
    Q = LNQ - 2 * lam                       # the effective quadratic coefficient is `Q / 2`
    n = rows_n if rows_n is not None else len(w)
    tot = caps_total if caps_total is not None else mp.fsum(row_cap(pe, j, lam)
                                                           for j in range(n))

    def _box(j):
        """`[lo_j, U_j]`: the `u_j` an `u` reaching the incumbent is confined to.  `T`-free,
        because `caps_total` is the whole-frame sum."""
        need = incumbent - (tot - row_cap(pe, j, lam))
        gp = gamma_p(pe, j, lam)
        disc = gp * gp - 2 * Q * need
        if disc < 0:
            return None
        root = mp.sqrt(disc)
        Uj, Lj = (gp + root) / Q, (gp - root) / Q
        lo = max(mp.mpf(0), Lj)
        return None if Uj < lo else (lo, Uj)

    if all_T:                       # grow until the marginal charge is negligible
        # Always pad at least one step past the ascent, so `last_term` below is a genuine
        # PADDED-row charge.  Without this, a run whose ascent already covered every row with a
        # non-negligible charge would set `last_term = 0` and bound the tail by nothing — the
        # rows past `n` would be neither charged nor bounded, which is a hole, not a tight bound.
        n = max(n, len(w) + 6)
        while n < 400:
            b = _box(n - 1)
            if b is None:
                break
            wf = list(w) + [mp.mpf(0)] * (n - len(w))
            gl = dG_coord(wf, pe, n - 1, mp.mpf(0), lam)
            if abs(gl * (b[1] if gl >= 0 else b[0])) < GTOL:
                break
            n += 6
        else:
            raise SystemExit("all-T certificate did not reach a negligible marginal charge")

    wfull = list(w) + [mp.mpf(0)] * (n - len(w))
    gvec = gradG(wfull, pe, lam)
    gw = G(wfull, pe, lam)
    slack = mp.mpf(0)
    naive = mp.mpf(0)
    rows = []
    pad_charged = mp.mpf(0)
    last_term = mp.mpf(0)
    for j in range(n):
        b = _box(j)
        if b is None:
            return incumbent, None, None, rows, True, None, (mp.mpf(0), "excluded")
        lo, Uj = b
        # The real-box charge, kept even under `integer_box`: the geometric tail past `n` is
        # bounded from it, and it dominates the integer charge, so the tail stays valid.
        real_term = gvec[j] * (Uj - wfull[j]) if gvec[j] >= 0 else gvec[j] * (lo - wfull[j])
        if integer_box:
            # Round OUTWARD by TOL first: a `U_j` that is an integer up to arithmetic error must
            # not be floored to the integer below it.  Erring this way can only loosen the bound.
            lo, Uj = mp.ceil(lo - TOL), mp.floor(Uj + TOL)
            if Uj < lo:
                return incumbent, None, None, rows, True, None, (mp.mpf(0), "excluded")
        term = gvec[j] * (Uj - wfull[j]) if gvec[j] >= 0 else gvec[j] * (lo - wfull[j])
        slack += term
        naive += abs(gvec[j]) * (Uj - lo)
        if j >= len(w):
            pad_charged += abs(term)
            last_term = abs(real_term)
        rows.append({"row": j, "grad": mp.nstr(gvec[j], 12), "lo": mp.nstr(lo, 12),
                     "U": mp.nstr(Uj, 12), "w": mp.nstr(wfull[j], 12),
                     "term": mp.nstr(term, 12)})
    # Rows beyond `n` are accounted for, never ignored, and there are two cases.
    #
    #   * If every such row has a non-positive gradient at `w_j = 0` with its box starting at 0,
    #     its charge `g_j (lo_j - w_j)` is EXACTLY zero — `box_charge_eq_zero_of_nonpos` in
    #     `SupergradientCertificate.lean`.  That is the `lam > 0` regime: `lam` drives every row
    #     with `Gamma_j < lam` to a negative gradient.  The condition is checked over a window
    #     rather than assumed, and `Gamma_j` is verified monotone decreasing across it, which is
    #     what extends the window to all `j`.
    #   * Otherwise the charges are positive and decay geometrically, and the remainder is
    #     BOUNDED by its geometric tail — `sum_charge_extend_le`, the honest form.
    tail = mp.mpf(0)
    tail_mode = "n/a"
    if all_T:
        _win, _prev_gam, _mono, _allzero = [], None, True, True
        for j in range(n, n + 30):
            bj = _box(j)
            gj = dG_coord(wfull + [mp.mpf(0)] * (j + 1 - n), pe, j, mp.mpf(0), lam)
            gam_j = gamma_p(pe, j, lam)
            if _prev_gam is not None and gam_j > _prev_gam:
                _mono = False
            _prev_gam = gam_j
            if bj is None or not (gj <= 0 and bj[0] == 0):
                _allzero = False
                break
            _win.append(j)
        if _allzero and _mono and len(_win) >= 30:
            tail, tail_mode = mp.mpf(0), "exactly zero (g <= 0, lo = w = 0, Gamma monotone)"
        else:
            tail, tail_mode = last_term * _TAIL_G, "geometric bound on a positive tail"
    bound = gw + slack + tail
    return ((bound if bound > incumbent else incumbent), slack, naive, rows, False,
            pad_charged, (tail, tail_mode))


def _hi_for(pe: int, Tlen: int, u, i):
    """Upper barrier for coordinate `i`: `u_i` must stay under the smallest gap to any row ABOVE
    it, offset by that row's own displacement, and under the gap to the undisplaced tail."""
    b = b0_of(pe, i)
    lim = mp.mpf(b0_of(pe, Tlen) - b)
    for j in range(i + 1, Tlen):
        lim = min(lim, mp.mpf(b0_of(pe, j) - b) + u[j])
    return lim


def _lo_for(pe: int, u, i):
    """Lower barrier for coordinate `i`, and it is **not** always `0`.

    A row BELOW `i` that is displaced by more than the gap between them forces `u_i` up:
    `beta_i > beta_j` reads `(b0_i - b0_j) + u_i - u_j > 0`.  Omitting this was a real bug — the
    search maximised over `[0, hi]`, evaluated the derivative at an infeasible `0`, and `gx`
    returned a plausible negative number there instead of failing, so a coordinate could be set
    to a value the domain forbids and the sweep would carry on.  `gx` now refuses; this is what
    keeps it from having to."""
    b = b0_of(pe, i)
    lim = mp.mpf(0)
    for j in range(i):
        lim = max(lim, u[j] - mp.mpf(b - b0_of(pe, j)))
    return lim


_EDGE = mp.mpf(10) ** (-(TARGET_DIGITS + 2))


def _argmax_coord(u, pe: int, i: int, lam=None, iters: int = 48):
    """Maximise `G` in coordinate `i` by bisecting its (decreasing) derivative over the coordinate's
    own feasible interval."""
    hi = _hi_for(pe, len(u), u, i) - _EDGE
    lo = _lo_for(pe, u, i) + _EDGE
    if hi <= lo:
        return max(lo, min(u[i], hi))
    if dG_coord(u, pe, i, lo, lam) <= 0:
        return lo                                  # optimum on the lower boundary (KKT)
    if dG_coord(u, pe, i, hi, lam) >= 0:
        return hi
    for _ in range(iters):
        mid = (lo + hi) / 2
        if dG_coord(u, pe, i, mid, lam) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


RES_TARGET = mp.mpf(10) ** (-13)      # KKT residual the ascent drives to; see `relaxed_sup`


def relaxed_sup(pe: int, Tlen: int, warm=None, lam=None, sweeps: int = 150):
    """Coordinate ascent on the concave program: a coordinate-wise stationary point of a concave
    function is the global maximum, so this is a search only in the sense of finding it.

    Returns `(value, u, residual)` where the residual is `max_i |g_i|` over the interior
    coordinates and `max_i g_i` over those parked at zero — the KKT residual.  **It is reported
    rather than assumed**: the certificate is valid at any `w`, so a badly converged point gives
    a sound but useless bound, and there is no other signal that that has happened.

    Two details that are not cosmetic:

      * **Warm start.** From `u = 0` every barrier `min_j (b0_j - b0_i + u_j)` is at its tightest,
        so the coordinates unlock only one sweep at a time.  Measured at `pe = 2`, a cold start
        with 30 sweeps returned `1.8466` at `T = 6` against `2.0310` at `T = 5` — impossible for
        a relaxation, since padding the `T = 5` optimum with a zero is feasible at `T = 6`.
        Seeding from the previous length's solution removes it.
      * **Stop on the gradient, not on the value.** `|G_k - G_{k-1}| < tol` was satisfied while
        the largest coordinate gradient was still `1.12`; near a flat optimum the value stops
        moving long before the point does, and it is the point the certificate uses."""
    u = list(warm) + [mp.mpf(0)] * (Tlen - len(warm)) if warm else [mp.mpf(0)] * Tlen
    u = u[:Tlen]

    def _resid(uu):
        """The PROJECTED gradient: a coordinate pressed against a barrier with the gradient
        pointing out of the feasible set is stationary, and scoring it by `|g_i|` would report a
        converged ascent as failed."""
        g = gradG(uu, pe, lam)
        out = []
        for i in range(Tlen):
            hi = _hi_for(pe, Tlen, uu, i)
            lo = _lo_for(pe, uu, i)
            if g[i] > 0:
                out.append(mp.mpf(0) if hi - uu[i] < 10 * _EDGE else g[i])
            else:
                out.append(mp.mpf(0) if uu[i] - lo < 10 * _EDGE else -g[i])
        return out

    rv = _resid(u)
    for _ in range(sweeps):
        for i in range(Tlen):
            u[i] = _argmax_coord(u, pe, i, lam)
        rv = _resid(u)
        if max(rv) < RES_TARGET:
            break
    return G(u, pe, lam), u, max(rv)


def xrun(ell: int) -> mp.mpf:
    """The run piece, from the committed `ap_value` — not re-derived."""
    return _sc(_ap_value([-1] * ell, False))


def cut_for(b_top, b_bot) -> int:
    """The largest run length that can still reach `e_inf` given SEPARATE caps on the two edges.
    With `b_top == b_bot` this is #7349's `cut_for`; the point is that it never needs G1."""
    th = E_INF_7335 - b_top - b_bot
    return max(ell for ell in range(1, 3000) if xrun_ck(ell) > th)


def blocks_with_sum_at_most(S: int) -> int:
    n = 0

    def rec(last, s):
        nonlocal n
        n += 1
        lo = max(1, last - 1) if last is not None else 1
        for x in range(lo, S - s + 1):
            rec(x, s + x)

    rec(None, 0)
    return n - 1


# --------------------------------------------------------------------------------------------
# Keyed checkpoint.  The full run is ~200 min against a 120-min harness ceiling, and the script
# was straight-line, so a killed run restarted from R1.  Each stage R1..R5 is now a block that
# either RUNS (and saves what it defined, its printed output and its checks) or is RESTORED.
#
# The key is a SHA-256 of everything the stage's numbers can depend on: this file's source up
# to the END of that stage (so it covers the prelude and every earlier stage, and editing R6
# invalidates nothing), the committed evaluator's source, the q0 string, `mp.dps` and every
# `REV_XBOT*` environment override.  Change any of them and the stage recomputes; there is no
# way to restore a number computed from different code.  mpf values are stored as their exact
# binary `_mpf_` tuples, so a restore is bit-identical rather than a decimal round trip.
#
# Within R5 and R6 the expensive CALLS are memoised to disk the same way (`_disk_memo`), so a
# run killed mid-stage resumes at the last finished ascent / run length rather than at the
# stage start.  `REV_XBOTR_CKPT=0` disables all of it; the witness records which stages were
# restored, and from which key, so a restored figure is never presented as a fresh one.
# --------------------------------------------------------------------------------------------
import hashlib  # noqa: E402
import io  # noqa: E402

_CKPT_ON = os.environ.get("REV_XBOTR_CKPT", "1") != "0"
_CKPT_DIR = os.environ.get(
    "REV_XBOTR_CKPT_DIR",
    os.path.join(os.path.expanduser("~"), ".cache", "qou", "xbot-relaxation-ckpt"))
_SELF_TEXT = open(os.path.abspath(__file__)).read()
_ENV_KEY = sorted((k, v) for k, v in os.environ.items() if k.startswith("REV_XBOT"))
_CKPT_LOG: list[dict] = []


def _stage_key(end_marker: str) -> str:
    """Hash of the source up to `end_marker` plus every non-source input."""
    if _SELF_TEXT.count(end_marker) != 1:
        raise SystemExit(f"checkpoint marker {end_marker!r} is not unique — refusing to key on it")
    h = hashlib.sha256()
    for part in (_SELF_TEXT[:_SELF_TEXT.index(end_marker)], _TEXT, Q_50_DIGIT_STR,
                 str(mp.dps), json.dumps([[k, v] for k, v in _ENV_KEY if k != "REV_XBOTR_CKPT"])):
        h.update(part.encode())
        h.update(b"\0")
    return h.hexdigest()


def _enc(x):
    if isinstance(x, mp.mpf):
        s, man, e, bc = x._mpf_
        return {"__mpf__": [s, hex(man), e, bc]}
    if isinstance(x, (bool, int, str)) or x is None:
        return x
    if isinstance(x, tuple):
        return {"__tuple__": [_enc(v) for v in x]}
    if isinstance(x, list):
        return [_enc(v) for v in x]
    if isinstance(x, dict):
        return {"__dict__": [[_enc(k), _enc(v)] for k, v in x.items()]}
    raise TypeError(type(x).__name__)


def _dec(x):
    if isinstance(x, list):
        return [_dec(v) for v in x]
    if isinstance(x, dict):
        if "__mpf__" in x:
            s, man, e, bc = x["__mpf__"]
            return mp.make_mpf((s, int(man, 16), e, bc))
        if "__tuple__" in x:
            return tuple(_dec(v) for v in x["__tuple__"])
        return {(tuple(_dec(k)) if isinstance(k, list) else _dec(k)): _dec(v)
                for k, v in x["__dict__"]}
    return x


class _Tee(io.TextIOBase):
    def __init__(self, inner):
        self.inner, self.buf = inner, io.StringIO()

    def write(self, s):
        self.buf.write(s)
        return self.inner.write(s)

    def flush(self):
        self.inner.flush()


_STAGE: dict = {}


def _stage_begin(name: str, end_marker: str) -> bool:
    """True: run the stage.  False: it was restored (globals, output and checks replayed)."""
    key = _stage_key(end_marker)
    path = os.path.join(_CKPT_DIR, f"{name}-{key[:24]}.json")
    if _CKPT_ON and os.path.exists(path):
        with open(path) as fh:
            rec = json.load(fh)
        if rec.get("key") == key:
            globals().update({k: _dec(v) for k, v in rec["globals"].items()})
            CHECKS.extend((n, bool(o), d) for n, o, d in rec["checks"])
            print(f"  [checkpoint] {name} RESTORED (key {key[:16]}, computed "
                  f"{rec['computed_at']}, {rec['seconds']:.0f}s then) — replaying its output:")
            sys.stdout.write(rec["stdout"])
            _CKPT_LOG.append({"stage": name, "restored": True, "key": key,
                              "computed_at": rec["computed_at"]})
            return False
    _STAGE.update(name=name, key=key, path=path, t0=time.time(), nchk=len(CHECKS),
                  before={k: id(v) for k, v in globals().items()}, tee=_Tee(sys.stdout))
    sys.stdout = _STAGE["tee"]
    return True


def _stage_end() -> None:
    if not _STAGE:
        return                                      # the stage was restored
    sys.stdout = _STAGE["tee"].inner
    before = _STAGE["before"]
    saved, skipped = {}, []
    for k, v in list(globals().items()):
        if k.startswith("__") or (k in before and before[k] == id(v)) or k == "_STAGE":
            continue
        try:
            saved[k] = _enc(v)
        except TypeError:
            skipped.append(k)                       # e.g. a module, a closure, an iterator
    secs = time.time() - _STAGE["t0"]
    rec = {"key": _STAGE["key"], "stage": _STAGE["name"], "seconds": secs,
           "computed_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
           "globals": saved, "skipped": skipped,
           "checks": [list(c) for c in CHECKS[_STAGE["nchk"]:]],
           "stdout": _STAGE["tee"].buf.getvalue()}
    if _CKPT_ON:
        os.makedirs(_CKPT_DIR, exist_ok=True)
        tmp = _STAGE["path"] + ".tmp"
        with open(tmp, "w") as fh:
            json.dump(rec, fh)
        os.replace(tmp, _STAGE["path"])             # atomic: a kill mid-write leaves no record
    _CKPT_LOG.append({"stage": _STAGE["name"], "restored": False, "key": _STAGE["key"],
                      "seconds": round(secs), "not_checkpointed": skipped})
    _STAGE.clear()


def _disk_memo(tag: str, args, fn, key=None):
    """`fn()` memoised to disk under (`tag`, a source/env key, `args`).  Used for the single
    expensive calls inside a stage, so a killed run resumes at call granularity.  `key` defaults
    to the whole prelude's key; pass a narrower one only for a function that provably reads
    nothing else."""
    if not _CKPT_ON:
        return fn()
    h = hashlib.sha256((key or _stage_key("# ===CKPT-" + "MEMO-KEY===")).encode())
    h.update(tag.encode())
    h.update(json.dumps(_enc(args), sort_keys=True).encode())
    path = os.path.join(_CKPT_DIR, "memo", f"{tag}-{h.hexdigest()[:32]}.json")
    if os.path.exists(path):
        with open(path) as fh:
            return _dec(json.load(fh))
    out = fn()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path + ".tmp", "w") as fh:
        json.dump(_enc(out), fh)
    os.replace(path + ".tmp", path)
    return out


# ===CKPT-MEMO-KEY===


def _relaxed_sup_ck(pe: int, Tlen: int, warm=None, lam=None):
    """`relaxed_sup`, disk-memoised on its full argument list (the warm start included, exactly)."""
    return tuple(_disk_memo("relaxed_sup", [pe, Tlen, warm, lam],
                            lambda: list(relaxed_sup(pe, Tlen, warm=warm, lam=lam))))


_XRUN_MEMO: dict[int, mp.mpf] = {}
# `xrun` reads only the committed evaluator (`_ap_value`, `_sc`) at this q0 and precision, so it
# is keyed on exactly those: an edit to the certificate or the ascent must not cost R6's ~40 min.
_XRUN_KEY = hashlib.sha256("\0".join((_TEXT, Q_50_DIGIT_STR, str(mp.dps))).encode()).hexdigest()


def xrun_ck(ell: int) -> mp.mpf:
    """`xrun`, memoised in memory AND on disk.  The two `cut_for` calls in R6 share every value,
    and un-memoised R6 alone was measured at ~87 min (qou-as81).  Semantics are unchanged: the
    same committed `_ap_value` is evaluated once per `ell` instead of once per call."""
    if ell not in _XRUN_MEMO:
        _XRUN_MEMO[ell] = _disk_memo("xrun", [ell], lambda: xrun(ell), key=_XRUN_KEY)
    return _XRUN_MEMO[ell]

# --------------------------------------------------------------------------------------------
print("the BOTTOM edge's value is concave too — sup_s Xbot is a concave program")
print(f"  q0 = {mp.nstr(Q0, 20)} (proton pin);  mp.dps = {mp.dps};  series depth {RSER}")
print(f"  frame: b0(j) = j for j < pe, 2j - pe for j >= pe   (k = {K}, read from the bottom)")
print(f"  programs: pe = 0..{PEMAX}, T = 1..{TMAX};  all-T certificate over {JPAD} rows")
print(flush=True)

# --------------------------------------------------------------------------------------------
if _stage_begin("R1", "# ===END " + "R1==="):
    print("R1  does the real extension reproduce the committed integer evaluator?")
    _r1 = []
    _r1_worst = mp.mpf(0)
    # Enumerate the VALID (pe, block) pairs rather than hand-picking: most hand-picked blocks are
    # rejected by the ordering constraint, and a sample chosen before knowing which survive says
    # more about the guesser than about the extension.
    _r1_pool = [b for b in _bot_profiles(5, 3) if b]
    for _pe in range(0, min(PEMAX, 4) + 1):
        _L = K + 1 + _pe
        _b0f = _staircase_beta(K, _L)
        _nb0f = [-x for x in _b0f]
        _taken = 0
        for _bot in _r1_pool:
            if _taken >= 12:
                break
            _uu = _make_u(_L, (), _bot, 0, 0)
            if _uu is None:
                continue
            _iv = _delta_excess(_uu, K, _b0f, _nb0f, require_zero_sum=False)
            if _iv is None:
                continue
            # `bot` is written top-to-bottom; `G` indexes from the bottom, so reverse it
            _rv = G([mp.mpf(x) for x in reversed(_bot)], _pe)
            _d = abs(_rv - _sc(_iv))
            _r1.append({"pe": _pe, "bot": list(_bot), "integer": mp.nstr(_sc(_iv), 22),
                        "real": mp.nstr(_rv, 22), "diff": mp.nstr(_d, 6)})
            _r1_worst = max(_r1_worst, _d)
            _taken += 1
    print(f"    {len(_r1)} (pe, block) pairs compared against `delta_excess`")
    print(f"    worst |real - integer| = {mp.nstr(_r1_worst, 6)}")
    for _r in _r1[:5]:
        print(f"      pe={_r['pe']} {str(_r['bot']):16s} {_r['integer']:26s} vs {_r['real']:26s}",
              flush=True)
    check(
        "R1 the extended objective restricts to the integer one",
        _r1_worst < TOL and len(_r1) >= 20,
        f"over {len(_r1)} (pe, block) pairs the real-u objective agrees with the committed "
        f"`delta_excess` to {mp.nstr(_r1_worst, 4)} — scale-1e-40 integers against mp.dps = "
        f"{mp.dps} reals.  This is the check that makes the relaxation a relaxation of the RIGHT "
        f"problem: the one-body term `fi(beta) - fi(b0)` is a partial sum with no canonical real "
        f"extension, and the obvious integral extension is concave but NOT exact at integers.  "
        f"`R(b0) - R(b0+u)` with `R(x) = sum_{{j>=1}} eps(x+j)` is both, because the constant "
        f"`sum_m eps(m)` cancels",
    )
    print(flush=True)

# ===END R1===
_stage_end()
# --------------------------------------------------------------------------------------------
if _stage_begin("R2", "# ===END " + "R2==="):
    print("R2  is the extended objective concave?  (the relaxation's whole premise)")
    random.seed(23)
    _r2_worst = None
    _r2_n = 0
    for _ in range(300):
        _pe = random.randint(0, PEMAX)
        _T = random.randint(2, 7)

        def _rp(pe=_pe, Tl=_T):
            v = [mp.mpf(0)] * Tl
            for i in range(Tl - 1, -1, -1):
                hi = (mp.mpf(b0_of(pe, Tl) - b0_of(pe, i)) if i == Tl - 1
                      else mp.mpf(b0_of(pe, i + 1) - b0_of(pe, i)) + v[i + 1])
                v[i] = mp.mpf(random.uniform(0, float(hi) * 0.85))
            return v

        _a, _b = _rp(), _rp()
        _lam = mp.mpf(random.uniform(mp.mpf("0.05"), mp.mpf("0.95")))
        _mid = [_lam * p + (1 - _lam) * q for p, q in zip(_a, _b)]
        _ga, _gb, _gm = G(_a, _pe), G(_b, _pe), G(_mid, _pe)
        if mp.isinf(_ga) or mp.isinf(_gb) or mp.isinf(_gm):
            continue
        _gap = _gm - (_lam * _ga + (1 - _lam) * _gb)
        _r2_n += 1
        if _r2_worst is None or _gap < _r2_worst[0]:
            _r2_worst = (_gap, _pe, _T, _lam)
    print(f"    {_r2_n} random feasible triples, pe = 0..{PEMAX}, T = 2..7")
    print(f"    min G(mid) - [lam G(a) + (1-lam) G(b)] = {mp.nstr(_r2_worst[0], 8)} "
          f"at pe = {_r2_worst[1]}, T = {_r2_worst[2]}", flush=True)
    check(
        "R2 the bottom-edge value is concave in u — measured, not assumed",
        _r2_worst[0] >= 0 and _r2_n >= 100,
        f"minimum concavity gap {mp.nstr(_r2_worst[0], 6)} over {_r2_n} random feasible triples "
        f"spanning both environments of the frame.  The reason is one second derivative used four "
        f"times: `-R(b0 + u)` is concave because `-R' = sum_j gx(b0+u+j)` is decreasing; every pair "
        f"term is `-eps(g + (u_i - u_j))`, concave composed with a linear map; the above-block tail "
        f"is `-eps(g - u_j)`; the cost is `-(ln q0/2) sum u^2`.  So maximising over real u is a "
        f"CONCAVE PROGRAM and a coordinate-wise stationary point is the global maximum",
    )
    print(flush=True)

# ===END R2===
_stage_end()
# --------------------------------------------------------------------------------------------
if _stage_begin("R3", "# ===END " + "R3==="):
    print("R3  the resummations and the analytic gradient against direct computation")
    _r3_R = max(abs(R(mp.mpf(x)) - mp.fsum(epsx(mp.mpf(x) + j) for j in range(1, 500)))
                for x in ("0", "0.5", "3", "7.25"))
    _r3_Rg = max(abs(Rg(mp.mpf(x)) - mp.fsum(gx(mp.mpf(x) + j) for j in range(1, 500)))
                 for x in ("0", "0.5", "3", "7.25"))
    _r3_W = mp.mpf(0)
    _r3_Wg = mp.mpf(0)
    for _pe, _T in ((0, 3), (5, 2), (8, 3), (3, 6)):
        _m = max(0, _pe - _T)
        _full = list(range(_m)) + [_m + 2 * t for t in range(300)]
        for _y in ("0.25", "1", "2.5"):
            _yy = mp.mpf(_y)
            _r3_W = max(_r3_W, abs(W(_yy, _pe, _T) - mp.fsum(epsx(_yy + d) for d in _full)))
            _r3_Wg = max(_r3_Wg, abs(Wg(_yy, _pe, _T) - mp.fsum(gx(_yy + d) for d in _full)))
    _r3_g = mp.mpf(0)
    _hstep = mp.mpf(10) ** (-9)
    for _pe, _T in ((0, 3), (6, 4), (8, 2)):
        _u = [mp.mpf("0.4") + mp.mpf(i) / 10 for i in range(_T)]
        _an = gradG(_u, _pe)
        for _i in range(_T):
            _up, _dn = list(_u), list(_u)
            _up[_i] += _hstep
            _dn[_i] -= _hstep
            _r3_g = max(_r3_g, abs(_an[_i] - (G(_up, _pe) - G(_dn, _pe)) / (2 * _hstep)))
    # and the T-independence of Gamma, which the all-T certificate rests on
    _r3_gam = max(abs(gamma(_pe, _j)
                      - (Rg(mp.mpf(b0_of(_pe, _j)))
                         + mp.fsum(gx(b0_of(_pe, _j) - b0_of(_pe, _q)) for _q in range(_j))
                         - Wg(mp.mpf(b0_of(_pe, _Tl) - b0_of(_pe, _j)), _pe, _Tl)
                         - mp.fsum(gx(b0_of(_pe, _q) - b0_of(_pe, _j))
                                   for _q in range(_j + 1, _Tl))))
                  for _pe in (0, 4, 8) for _Tl in (3, 7, 11) for _j in range(_Tl))
    print(f"    R  vs direct sum: {mp.nstr(_r3_R, 6)}    Rg: {mp.nstr(_r3_Rg, 6)}")
    print(f"    W  vs direct sum: {mp.nstr(_r3_W, 6)}    Wg: {mp.nstr(_r3_Wg, 6)}")
    print(f"    analytic gradient vs central difference (h = 1e-9): {mp.nstr(_r3_g, 6)}")
    print(f"    Gamma_j is T-free: worst spread over T in {{3,7,11}} = {mp.nstr(_r3_gam, 6)}",
          flush=True)
    check(
        "R3 the closed-form tails, the analytic gradient and the T-independence of Gamma hold",
        (_r3_R < TOL and _r3_Rg < TOL and _r3_W < TOL and _r3_Wg < TOL
         and _r3_g < mp.mpf(10) ** (-12) and _r3_gam < TOL),
        f"the resummed `R` and `W` agree with direct sums to {mp.nstr(max(_r3_R, _r3_W), 4)} and "
        f"their derivative forms to {mp.nstr(max(_r3_Rg, _r3_Wg), 4)}; the analytic gradient agrees "
        f"with a central difference to {mp.nstr(_r3_g, 4)}.  The direction of that last test "
        f"matters: the CERTIFICATE uses the analytic form, because the supergradient inequality is "
        f"about the true gradient and a difference quotient would make it a statement about the "
        f"step size — the finite difference is here only to catch an algebra slip.  And `Gamma_j` "
        f"agrees to {mp.nstr(_r3_gam, 4)} across block lengths 3, 7 and 11, which is the fact the "
        f"all-T certificate rests on: the block rows above `j` and the undisplaced tail above the "
        f"block are one sum split at an arbitrary place",
    )
    print(flush=True)

# ===END R3===
_stage_end()
# --------------------------------------------------------------------------------------------
if _stage_begin("R4", "# ===END " + "R4==="):
    print("R4  the relaxed supremum and its certificate, per (pe, T)")
    _t0 = time.time()
    _BOTS = _bot_profiles(BMAX, BUMAX)
    _XB = _bot_table(_BOTS)
    INT_SUP_BOT = _sc(max(v for v, _, _ in _XB.values()))
    _int_arg = max(_XB.items(), key=lambda kv: kv[1][0])
    print(f"    enumerated Xbot max (BMAX={BMAX}, BUMAX={BUMAX}): {mp.nstr(INT_SUP_BOT, 22)} "
          f"at s = {_int_arg[0]}, bot {list(_int_arg[1][1])}, pe = {_int_arg[1][2]}  "
          f"[{time.time() - _t0:.0f}s]", flush=True)

    _r4 = []
    _best_relax = None
    _ARG: dict[tuple[int, int], list] = {}
    _mono_viol = []
    _res_worst = mp.mpf(0)
    for _pe in range(0, PEMAX + 1):
        _bp = None
        _warm = None
        _prev_v = None
        for _T in range(1, TMAX + 1):
            _v, _u, _res = _relaxed_sup_ck(_pe, _T, warm=_warm)
            if mp.isinf(_v):
                continue
            _warm = list(_u)
            _ARG[(_pe, _T)] = list(_u)
            _res_worst = max(_res_worst, _res)
            # sup must be non-decreasing in T: padding the length-(T-1) optimum with a zero is
            # feasible at length T and has the same value (Gamma is T-free).  A drop means the
            # ascent failed, and nothing else reports that.
            if _prev_v is not None and _v < _prev_v - TOL:
                _mono_viol.append({"pe": _pe, "T": _T, "sup": mp.nstr(_v, 18),
                                   "prev": mp.nstr(_prev_v, 18)})
            _prev_v = _v
            _r4.append({"pe": _pe, "T": _T, "sup": mp.nstr(_v, 22),
                        "kkt_residual": mp.nstr(_res, 8),
                        "argmax": [mp.nstr(x, 10) for x in _u]})
            if _bp is None or _v > _bp[0]:
                _bp = (_v, _T, list(_u))
            if _best_relax is None or _v > _best_relax[0]:
                _best_relax = (_v, _pe, _T, list(_u))
        if _bp:
            print(f"    pe = {_pe}: best relaxed {mp.nstr(_bp[0], 18):22s} at T = {_bp[1]:2d}   "
                  f"[{', '.join(mp.nstr(x, 5) for x in _bp[2][:6])}"
                  f"{'...' if len(_bp[2]) > 6 else ''}]", flush=True)
    B_RELAX, _PE_STAR, _T_STAR, _U_STAR = _best_relax
    print(f"    worst KKT residual over all programs: {mp.nstr(_res_worst, 6)};  "
          f"monotonicity violations in T: {len(_mono_viol)}", flush=True)
    # The ascent value is ACHIEVED, so it is a valid incumbent — and a tighter one than the
    # enumeration.  A larger incumbent narrows the certificate's box; it cannot invalidate it.
    INCUMBENT = max(B_RELAX, INT_SUP_BOT)
    _best_cert = None
    _cert_rows_star = _naive_star = None
    for _row in _r4:
        _pe, _T = _row["pe"], _row["T"]
        _w = _ARG[(_pe, _T)]                     # the ascent point itself, not a 10-digit round trip
        _cb, _cs, _cn, _crows, _excl, _, _ = certificate(
            _pe, _w, INCUMBENT,
            caps_total=mp.fsum(row_cap(_pe, j) for j in range(_T)))
        _row["certified_bound"] = mp.nstr(_cb, 22)
        _row["slack"] = None if _cs is None else mp.nstr(_cs, 12)
        _row["excluded_by_row_box"] = _excl
        if _best_cert is None or _cb > _best_cert[0]:
            _best_cert = (_cb, _pe, _T, _cs)
            _cert_rows_star, _naive_star = _crows, _cn
    B_CERT, _PE_CERT, _T_CERT, _SLACK = _best_cert
    _dt4 = time.time() - _t0
    print(f"    B_relax = {mp.nstr(B_RELAX, 22)} at (pe, T) = ({_PE_STAR}, {_T_STAR})")
    print(f"    argmax (bottom row first) = [{', '.join(mp.nstr(x, 6) for x in _U_STAR)}]")
    print(f"    B_cert  = {mp.nstr(B_CERT, 24)} at (pe, T) = ({_PE_CERT}, {_T_CERT})   "
          f"slack {'n/a' if _SLACK is None else mp.nstr(_SLACK, 8)}")
    print(f"    {len(_r4)} programs in {_dt4:.0f}s", flush=True)
    # The tail of the per-pe T-sequence, which is what says whether the plain relaxation settles.
    _tail_inc = {}
    for _pe in range(0, PEMAX + 1):
        _seq = [mp.mpf(r["sup"]) for r in _r4 if r["pe"] == _pe]
        if len(_seq) >= 2:
            _tail_inc[_pe] = _seq[-1] - _seq[-2]
    _worst_inc = max(_tail_inc.values()) if _tail_inc else mp.mpf(0)
    print(f"    last T-increment by pe: "
          f"{ {p: mp.nstr(v, 6) for p, v in sorted(_tail_inc.items())} }", flush=True)
    check(
        "R4 the plain u >= 0 relaxation is valid and CONVERGED — and measurably not tight",
        (B_CERT >= INT_SUP_BOT and B_CERT >= B_RELAX and not _mono_viol
         and _res_worst < mp.mpf("1e-10")),
        f"B_cert = {mp.nstr(B_CERT, 22)} at (pe, T) = ({_PE_CERT}, {_T_CERT}), "
        f"{mp.nstr(B_CERT / INT_SUP_BOT, 6)}x the enumerated maximum {mp.nstr(INT_SUP_BOT, 16)}.  "
        f"The ascent point is verified stationary rather than assumed to be: worst KKT residual "
        f"{mp.nstr(_res_worst, 6)} over {len(_r4)} programs, and 0 violations of the invariant that "
        f"sup is non-decreasing in T (padding the length-(T-1) optimum with a zero is feasible) — "
        f"which is the check that caught a cold-start ascent returning 1.8466 at T = 6 against "
        f"2.0310 at T = 5, and again a search whose lower barrier was wrongly fixed at 0 when the "
        f"rows BELOW force `u_i > u_j - (b0_i - b0_j)`.  **But the sup does not settle**: the last "
        f"increment in T is still {mp.nstr(_worst_inc, 6)} at T = {TMAX}.  That is not a "
        f"convergence failure, it is the relaxation being loose in kind — every Gamma_j is strictly "
        f"positive, so a real u collects a gain from an arbitrarily small displacement on "
        f"arbitrarily many rows, and no integer block can do that because its entries jump from 0 "
        f"to 1.  The top edge has no such gap: its class forces u >= 1, which is exactly why ITS "
        f"relaxation lands at 1.04x.  R5 closes the gap with a valid inequality rather than by "
        f"running T further"
        if (B_CERT >= INT_SUP_BOT and not _mono_viol and _res_worst < mp.mpf("1e-10")) else
        f"the ascent did not converge: worst KKT residual {mp.nstr(_res_worst, 6)}, "
        f"{len(_mono_viol)} violations of `sup non-decreasing in T` ({_mono_viol[:3]}).  The "
        f"certificate is still SOUND — it is valid at any w — but a non-stationary w makes it "
        f"loose, and B_cert = {mp.nstr(B_CERT, 12)} should not be used"
        if B_CERT >= INT_SUP_BOT else
        f"B_cert = {mp.nstr(B_CERT, 22)} does NOT dominate the enumerated maximum "
        f"{mp.nstr(INT_SUP_BOT, 16)} — an upper bound below an achieved value is unsound, so the "
        f"extension, the certificate or the frame indexing is wrong.  Do not use this number",
    )
    print(flush=True)

# ===END R4===
_stage_end()
# --------------------------------------------------------------------------------------------
if _stage_begin("R5", "# ===END " + "R5==="):
    print("R5  closing the integrality gap: the valid inequality `u^2 >= u`")
    # `lam` is free in [0, ln q0 / 2) and every value gives a VALID bound, so the best is the
    # smallest.  **Select on the certificate, not on the tangent sum.**  Measured, the T-free
    # tangent sum `sum_j cap_j(lam)` goes the WRONG way — 14.17 at lam = 0 rising to 251 at
    # 0.95 lam_max — because the cap is `Gamma'^2 / (2(ln q0 - 2 lam))` and the denominator
    # collapses faster than the numerator shrinks on the dominant row, where `Gamma ~ 1.42 >> lam`.
    # Choosing lam by that proxy picks lam = 0 and throws the whole tightening away.  What lam
    # actually buys is at the OTHER end of the frame: a padded row with `Gamma_j < lam` has a
    # negative gradient at `w_j = 0`, so its box maximum is at `lo_j = 0 = w_j` and it is charged
    # exactly nothing.
    _LAMS = [LAM_MAX * mp.mpf(f) / 20 for f in (0, 4, 10)]
    _tan_lam = {str(mp.nstr(L, 8)): {pe: cap_sum(pe, L) for pe in range(0, PEMAX + 1)}
                for L in _LAMS}
    _tan = _tan_lam[str(mp.nstr(_LAMS[0], 8))]
    _B_TAN = max(_tan.values())
    _pe_tan = max(_tan, key=lambda p: _tan[p])
    print(f"    lam = 0 tangent sums by pe: { {p: mp.nstr(v, 8) for p, v in sorted(_tan.items())} }")
    print(f"    B_tangent(lam = 0) = {mp.nstr(_B_TAN, 14)} at pe = {_pe_tan} "
          f"({mp.nstr(_B_TAN / INT_SUP_BOT, 6)}x) — and it RISES with lam, which is why the scan "
          f"below selects on the certificate instead")

    # Stage 1: scan lam at the single worst frame (|lam| ascents), rather than at every frame
    # (|lam| x |pe| ascents).  The minimiser is a property of the accumulation being suppressed,
    # which is the same mechanism in every frame.
    _pe_scan = max(range(0, PEMAX + 1),
                   key=lambda p: max((mp.mpf(r["sup"]) for r in _r4 if r["pe"] == p),
                                     default=mp.mpf(0)))
    _best_T_scan = max((r for r in _r4 if r["pe"] == _pe_scan), key=lambda r: mp.mpf(r["sup"]))["T"]
    _scan = []
    _lam_star = None
    _lam_best = None
    _warm_l = _ARG[(_pe_scan, _best_T_scan)]
    for _lm in _LAMS:
        _vs, _ws, _rs = _relaxed_sup_ck(_pe_scan, JPAD, warm=_warm_l, lam=_lm)
        _warm_l = list(_ws)
        # The incumbent must be a lower bound on THIS program's sup, and `B_RELAX` — the lam = 0
        # ascent value — need not be one: `G_lam(u) = G(u) + lam sum u(u-1)` is SMALLER than `G(u)`
        # wherever the optimum's coordinates sit below 1, which several of them do.  What survives
        # the change of program is the integer maximum, because an integer point has
        # `sum u(u-1) >= 0` and so `G_lam >= G` there.  (A too-large incumbent would not make the
        # certificate unsound — `sup <= max(V, ...)` holds for any V — but it would floor the
        # reported bound at a number this program may never reach.)
        _inc_l = max(INT_SUP_BOT, _vs)
        _bs, _, _, _rws, _exs, _pads, _tls = certificate(
            _pe_scan, _ws, _inc_l, caps_total=_tan_lam[str(mp.nstr(_lm, 8))][_pe_scan],
            all_T=True, lam=_lm)
        _scan.append({"lam": mp.nstr(_lm, 12), "frac_of_max": mp.nstr(_lm / LAM_MAX, 4),
                      "ascent": mp.nstr(_vs, 18), "all_T_bound": mp.nstr(_bs, 18),
                      "padded_charge": mp.nstr(_pads, 8), "rows": len(_rws or [])})
        print(f"    lam = {mp.nstr(_lm, 10):12s} ({mp.nstr(_lm / LAM_MAX, 4):>7s} of max): "
              f"ascent {mp.nstr(_vs, 12):16s} all-T bound {mp.nstr(_bs, 14):18s} "
              f"padded charge {mp.nstr(_pads, 6)}", flush=True)
        if _lam_best is None or _bs < _lam_best:
            _lam_best, _lam_star = _bs, _lm
    print(f"    certificate-optimal lam = {mp.nstr(_lam_star, 10)} "
          f"({mp.nstr(_lam_star / LAM_MAX, 4)} of the concavity limit), scanned at pe = {_pe_scan}",
          flush=True)

    _allT = {}
    _best_allT = None
    _best_int = None
    for _pe in range(0, PEMAX + 1):
        _rows_pe = [r for r in _r4 if r["pe"] == _pe]
        if not _rows_pe:
            continue
        _bw = max(_rows_pe, key=lambda r: mp.mpf(r["sup"]))
        # The ascent must COVER the rows the certificate charges.  Padding a SHORT optimum and
        # charging the appended rows `g_j U_j` at `w_j = 0` cost 19.27 in an earlier run — those
        # rows were never ascended, so their gradients are the whole positive slope.  Run the ascent
        # at the long length instead (warm-started from the T-loop, so it is a few sweeps); only the
        # rows past it are padded, where `Gamma_j ~ T2^(-b0_j)` has decayed to nothing.
        _vl, _w_pe, _resl = _relaxed_sup_ck(_pe, JPAD, warm=_ARG[(_pe, _bw["T"])], lam=_lam_star)
        _res_worst = max(_res_worst, _resl)
        _ab, _as_, _an2, _arows, _aexcl, _apad, _atail = certificate(
            _pe, _w_pe, max(INT_SUP_BOT, _vl),     # see the incumbent note in the lam scan above
            caps_total=_tan_lam[str(mp.nstr(_lam_star, 8))][_pe],
            all_T=True, lam=_lam_star)
        _atail, _tmode = _atail
        # The integer box (`integer_box=True`): the same certificate with each charged row's
        # interval rounded to the integers it contains.  Taken at two incumbents and the
        # smaller kept — both are valid, and they trade off: the ascent value narrows the box
        # but floors the result at a REAL value no integer block need reach; the enumerated
        # maximum is achieved by an integer block and floors nothing, at a wider box.
        _ib = min(certificate(_pe, _w_pe, _inc, caps_total=_tan_lam[str(mp.nstr(_lam_star, 8))][_pe],
                              all_T=True, lam=_lam_star, integer_box=True)[0]
                  for _inc in (max(INT_SUP_BOT, _vl), INT_SUP_BOT))
        _allT[_pe] = {"bound": mp.nstr(_ab, 22), "bound_integer_box": mp.nstr(_ib, 22),
                      "rows": len(_arows or []),
                      "ascent_rows": JPAD, "ascent_value": mp.nstr(_vl, 22),
                      "kkt_residual": mp.nstr(_resl, 8), "excluded": _aexcl,
                      "padded_charge": mp.nstr(_apad, 10), "tail": mp.nstr(_atail, 10),
                      "tail_mode": _tmode}
        print(f"    pe = {_pe}: ascent at {JPAD} rows -> {mp.nstr(_vl, 18):22s} (KKT "
              f"{mp.nstr(_resl, 4)});  all-T bound {mp.nstr(_ab, 18):22s} over "
              f"{len(_arows or []):3d} rows, padded charge {mp.nstr(_apad, 6)}, tail "
              f"{mp.nstr(_atail, 6)} [{_tmode}];  integer box {mp.nstr(_ib, 18)}", flush=True)
        if _best_int is None or _ib > _best_int[0]:
            _best_int = (_ib, _pe)
        if _best_allT is None or _ab > _best_allT[0]:
            _best_allT = (_ab, _pe, _arows, _atail, _apad, _tmode)
    B_ALLT, _PE_ALLT, _allT_rows, _allT_tail, _allT_pad, _allT_tmode = _best_allT
    print(f"    B_allT = {mp.nstr(B_ALLT, 24)} at pe = {_PE_ALLT}, lam = {mp.nstr(_lam_star, 8)}  "
          f"({mp.nstr(B_ALLT / INT_SUP_BOT, 6)}x the enumerated maximum)", flush=True)
    B_ALLT_INT, _PE_ALLT_INT = _best_int
    print(f"    B_allT, integer box = {mp.nstr(B_ALLT_INT, 24)} at pe = {_PE_ALLT_INT}  "
          f"({mp.nstr(B_ALLT_INT / INT_SUP_BOT, 6)}x; gain {mp.nstr(B_ALLT - B_ALLT_INT, 8)})",
          flush=True)
    check(
        "R5b the integer box is sound and no looser than the real box",
        INT_SUP_BOT <= B_ALLT_INT <= B_ALLT,
        f"B_allT with every charged row's interval rounded to its integers is "
        f"{mp.nstr(B_ALLT_INT, 22)} against {mp.nstr(B_ALLT, 22)} on the real box — "
        f"{mp.nstr(B_ALLT_INT / INT_SUP_BOT, 6)}x the enumerated maximum, a gain of "
        f"{mp.nstr(B_ALLT - B_ALLT_INT, 8)}.  Sound because Xbot is a maximum over integer "
        f"blocks only (as the lam program already requires: u^2 >= u holds on integers only), "
        f"and it still dominates the enumerated maximum, which an integer block attains"
        if INT_SUP_BOT <= B_ALLT_INT <= B_ALLT else
        f"B_allT(integer box) = {mp.nstr(B_ALLT_INT, 22)} is outside "
        f"[enumerated max {mp.nstr(INT_SUP_BOT, 16)}, real box {mp.nstr(B_ALLT, 16)}] — below the "
        f"enumerated maximum it is unsound, above the real box the rounding is wrong",
    )
    # A uniform slope bound valid at EVERY pe and j, not only the measured frames: the downward
    # pair gains sit at distinct positive integer gaps, so they sum to at most `Rg(0)`, and the
    # one-body slope is at most `Rg(0)` too.
    _gam_uni = 2 * Rg(mp.mpf(0))
    _gam_max = max(gamma(p, j) for p in range(0, PEMAX + 1) for j in range(0, 24))
    _Qs = LNQ - 2 * _lam_star
    _pe0 = None
    for _pp in range(1, 20000):
        _gp = _gam_uni - LNQ * (_pp - JPAD + 1) - _lam_star
        # Compare against the ENUMERATED maximum, which is achieved at an integer point: excluding a
        # frame is only licensed by a value something actually attains.
        if _pp > JPAD and JPAD * (_gp * _gp / (2 * _Qs) if _gp > 0 else mp.mpf(0)) < INT_SUP_BOT:
            _pe0 = _pp
            break
    print(f"    Gamma_max measured = {mp.nstr(_gam_max, 10)};  uniform bound 2*Rg(0) = "
          f"{mp.nstr(_gam_uni, 10)}")
    print(f"    wall depth bound: pe0 = {_pe0} for blocks of length <= {JPAD}", flush=True)
    # Compare like with like: both of these are the all-T bound AT THE SCAN FRAME, one with the
    # tightening off and one at the selected lam.  `B_ALLT` is the max over every frame at lam*, so
    # it is a different quantity and comparing the two would be the apples-to-oranges error this
    # file has already had to correct once (`B_cert` is a per-program bound over T <= TMAX).
    _B_ALLT_LAM0 = mp.mpf(_scan[0]["all_T_bound"])
    _B_ALLT_SCAN = mp.mpf(min(_scan, key=lambda r: mp.mpf(r["all_T_bound"]))["all_T_bound"])
    _LAM_GAIN = _B_ALLT_LAM0 - _B_ALLT_SCAN
    check(
        "R5 the all-T bound is sound, both dimensions are bounded, and the tightening is measured",
        (_allT_tail is not None and _allT_tail < TOL and _pe0 is not None
         and B_ALLT >= INT_SUP_BOT and _LAM_GAIN >= 0),
        f"Every integer `u_j >= 0` satisfies `u_j^2 >= u_j`, so for any `lam >= 0` the integer "
        f"supremum is bounded by `sup_{{real u >= 0}} [G(u) + lam sum_j (u_j^2 - u_j)]` — and since "
        f"`+lam sum u^2` eats into `G`'s own `-(ln q0/2) sum u^2`, that stays CONCAVE for "
        f"`lam < ln q0/2 = {mp.nstr(LAM_MAX, 8)}`.  Every lam gives a valid bound, so the best is "
        f"the smallest: the scan picks lam = {mp.nstr(_lam_star, 8)} "
        f"({mp.nstr(_lam_star / LAM_MAX, 4)} of the concavity limit), giving B_allT = "
        f"{mp.nstr(B_ALLT, 22)} at pe = {_PE_ALLT}, which is {mp.nstr(B_ALLT / INT_SUP_BOT, 6)}x the "
        f"enumerated maximum against 9.62x for the sibling probe's per-row coercivity bound.  What "
        f"lam is worth, measured LIKE FOR LIKE at the scan frame pe = {_pe_scan}: "
        f"{mp.nstr(_B_ALLT_LAM0, 12)} with the tightening off against {mp.nstr(_B_ALLT_SCAN, 12)} at "
        f"lam*, a gain of {mp.nstr(_LAM_GAIN, 6)}.  (`B_cert` = {mp.nstr(B_CERT / INT_SUP_BOT, 6)}x "
        f"is NOT comparable to either — it is a per-program bound over T <= {TMAX} only.)  "
        f"The charge `-lam u_j` falls on exactly the rows the "
        f"relaxation was exploiting: every row with `Gamma_j < lam` is driven to zero, which "
        f"truncates at a finite support the accumulation of arbitrarily-small displacements that no "
        f"integer block can make.  The bound covers every block length because `Gamma_j` is T-free "
        f"(R3), so padding the ascent point with zeros changes neither `G(w)` nor any box; the "
        f"padded rows are charged {mp.nstr(_allT_pad, 6)} in total and the remainder beyond them is "
        f"{_allT_tmode} ({mp.nstr(_allT_tail, 6)}) — never dropped.  The wall "
        f"depth is bounded separately and uniformly in pe: every slope is at most `2 Rg(0) = "
        f"{mp.nstr(_gam_uni, 8)}` (one-body plus downward gains, which sit at distinct positive "
        f"integer gaps), while a block of length <= {JPAD} in a pe-deep wall pays "
        f"`ln q0 (pe - T + 1)` per row, so none in a wall deeper than pe0 = {_pe0} reaches the "
        f"incumbent.  pe was a CAP in the enumeration (P_EXT_MAX = 8), not a bound"
        if (_pe0 is not None and B_ALLT >= INT_SUP_BOT and _LAM_GAIN >= 0) else
        f"the all-T bound did not close: B_allT = {mp.nstr(B_ALLT, 12)} at lam = "
        f"{mp.nstr(_lam_star, 8)} against {mp.nstr(_B_ALLT_LAM0, 12)} at lam = 0, tail "
        f"{'n/a' if _allT_tail is None else mp.nstr(_allT_tail, 6)}, pe0 = {_pe0}.  The valid "
        f"inequality is sound — `u^2 >= u` holds for every non-negative integer — so the bound "
        f"stands either way; this is a statement about the scan, the grid or the ascent",
    )
    print(flush=True)

# ===END R5===
_stage_end()
# --------------------------------------------------------------------------------------------
print("R6  what a certified B_bot buys — the cut, with G1 not used")
# NOT `min(B_CERT, B_ALLT)`: `B_CERT` is a per-program bound over the measured lengths
# `T <= TMAX` only, so it is not comparable.  `B_ALLT` is the one that covers every length.
# The integer box is a bound on the same integer supremum and never looser (R5b), so it is the
# one the cut uses; the real-box cut is still printed so the gain is visible as a cut width.
B_BOT = min(B_ALLT, B_ALLT_INT)
_cut_g1 = cut_for(B_TOP_CERT, B_TOP_CERT)      # #7349's cut, which goes through G1
_cut_free_real = cut_for(B_TOP_CERT, B_ALLT)   # the real-box B_allT, as before
_cut_free = cut_for(B_TOP_CERT, B_BOT)         # the same cut from two separate caps
_n_g1 = blocks_with_sum_at_most(_cut_g1) if _cut_g1 <= 32 else None
_n_free = blocks_with_sum_at_most(_cut_free) if _cut_free <= 32 else None
print(f"    via G1   (Xbot <= Xblock <= B_top = {mp.nstr(B_TOP_CERT, 14)}): cut {_cut_g1}"
      f"   {f'{_n_g1:,} blocks' if _n_g1 is not None else 'not enumerable'}")
print(f"    G1-free  (B_top = {mp.nstr(B_TOP_CERT, 14)}, B_bot = {mp.nstr(B_BOT, 14)}): "
      f"cut {_cut_free}   {f'{_n_free:,} blocks' if _n_free is not None else 'not enumerable'}"
      f"   (real box: cut {_cut_free_real})", flush=True)
check(
    "R6 the G1-free cut is enumerable",
    _cut_free <= 32,
    f"bounding the two edges SEPARATELY gives s_t + s_b <= {_cut_free} "
    f"({f'{_n_free:,}' if _n_free is not None else 'too many'} blocks) against {_cut_g1} "
    f"through G1 — so the join's finite window no longer rests on `Xbot(s) <= Xblock(s)` at "
    f"all.  That is the point: G1 is not proved here, it is REMOVED FROM THE ARGUMENT, which "
    f"is what the e_inf closure actually needs.  "
    + ("The two cuts coincide, so nothing is lost by dropping G1."
       if _cut_free == _cut_g1 else
       f"The G1-free cut is {_cut_free - _cut_g1} wider — the price of not assuming the bottom "
       f"edge is dominated by the top one")
    if _cut_free <= 32 else
    f"the G1-free cut is {_cut_free}, too wide to enumerate.  B_bot = {mp.nstr(B_BOT, 12)} is "
    f"not tight enough to replace G1 yet",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print(f"  B_bot = {mp.nstr(B_BOT, 22)}  ({mp.nstr(B_BOT / INT_SUP_BOT, 6)}x the enumerated "
      f"maximum; the per-row tangent gave {mp.nstr(_B_TAN / INT_SUP_BOT, 6)}x)")
print(f"  G1-free cut: s_t + s_b <= {_cut_free}"
      + (f"  ({_n_free:,} blocks)" if _n_free is not None else ""))
print("  G1 is NOT proved — with both edges capped separately it is no longer needed for the cut"
      if _cut_free <= 32 else "  G1 still needed: the bottom bound is not tight enough")
print(f"  pe <= {_pe0} is rigorous; this run certified pe <= {PEMAX}")
print()

_wit = {
    "schema": "https://litlfred.github.io/qou/schemas/witness/v1",
    "computedAt": datetime.now(timezone.utc).isoformat(),
    "computation": {
        "script": "computations/deltalambda/rev_e_infinity_xbot_relaxation_probe.py"},
    "bean": "qou-hok7",
    "anchor": "physical_proton",
    # Canonical anchor key read by the q0 audits/ratchet (the "anchor" key above is
    # a near-miss spelling they cannot see), plus scriptFile provenance.
    "q0Anchor": "proton",
    "scriptFile": os.path.basename(__file__),
    "q0Value": Q_50_DIGIT_STR,
    "description": (
        "The bottom edge of the e_inf staircase is concave in the displacement vector for the "
        "same reason the top edge is, so sup_s Xbot is a concave program and its maximum can be "
        "certified rather than enumerated.  This matters because gap G1 -- Xbot(s) <= Xblock(s) "
        "-- cannot be settled by enumeration at all (a capped maximum is a LOWER bound on its "
        "own supremum), and because the join does not actually need G1: it needs a finite "
        "window, which follows from SEPARATE caps on the two edges.  So a certified B_bot "
        "REMOVES G1 from the argument rather than proving it.  The extension to real u is not "
        "automatic: the one-body term fi(beta) - fi(b0) is a partial sum, and the obvious "
        "integral extension is concave but not exact at integers; R(b0) - R(b0+u) with "
        "R(x) = sum_{j>=1} eps(x+j) is both, because the constant sum_m eps(m) cancels.  "
        "#7349's block-length bound does NOT transfer, and the reason is the class: its blocks "
        "have every entry >= 1, so a row whose tangent slope is small contributes a NEGATIVE "
        "cap and the cumulative cap eventually falls below the bound; the bottom class permits "
        "zero entries, so every row cap is >= 0 and the cumulative cap never falls.  What "
        "replaces it is stronger: Gamma_j is exactly independent of the block length, so a "
        "length-T program is the restriction of one infinite program, and the certificate taken "
        "at the best ascent point PADDED WITH ZEROS charges every padded row exactly zero "
        "(gradient <= 0 puts the box maximum at lo_j, and lo_j = 0 = w_j) -- one number "
        "bounding every block length at once."
    ),
    "constants": {
        "mp_dps": mp.dps, "series_depth": RSER,
        "k": K, "pe_max_measured": PEMAX, "T_max_measured": TMAX, "J_pad": JPAD,
        "BMAX": BMAX, "BUMAX": BUMAX,
        "enumerated_max_Xbot": mp.nstr(INT_SUP_BOT, 30),
        "enumerated_argmax": {"s": _int_arg[0], "bot": list(_int_arg[1][1]),
                              "pe": _int_arg[1][2]},
        "B_relax_bottom": mp.nstr(B_RELAX, 30),
        "B_certified_per_program": mp.nstr(B_CERT, 30),
        "B_certified_at": {"pe": _PE_CERT, "T": _T_CERT},
        "B_certified_all_T": mp.nstr(B_ALLT, 30),
        "B_certified_all_T_integer_box": mp.nstr(B_ALLT_INT, 30),
        "B_certified_all_T_integer_box_at_pe": _PE_ALLT_INT,
        "cut_G1_free_real_box": _cut_free_real,
        "checkpoint": _CKPT_LOG,
        "B_bot": mp.nstr(B_BOT, 30),
        "B_tangent_bottom_T_free": mp.nstr(_B_TAN, 30),
        "B_tangent_by_pe": {str(p): mp.nstr(v, 20) for p, v in sorted(_tan.items())},
        "lam_star": mp.nstr(_lam_star, 30),
        "lam_max_concavity_limit": mp.nstr(LAM_MAX, 30),
        "tangent_sum_by_lam": {k: mp.nstr(max(v.values()), 20)
                               for k, v in _tan_lam.items()},
        "lam_scan": _scan,
        "lam_scan_frame": _pe_scan,
        "all_T_at_scan_frame_lam0": mp.nstr(_B_ALLT_LAM0, 20),
        "all_T_at_scan_frame_lam_star": mp.nstr(_B_ALLT_SCAN, 20),
        "lam_gain_like_for_like": mp.nstr(_LAM_GAIN, 20),
        "_lam_note": ("the tangent sum RISES with lam (14.17 -> 251 across the grid) because "
                      "the cap is Gamma'^2 / (2(ln q0 - 2 lam)) and the denominator collapses "
                      "faster than the numerator shrinks on the dominant row.  Selecting lam by "
                      "that proxy returns lam = 0 and discards the tightening; the certificate "
                      "is the right selector, because what lam buys is at the other end of the "
                      "frame -- a padded row with Gamma_j < lam is charged exactly zero."),
        "last_T_increment_by_pe": {str(p): mp.nstr(v, 12)
                                   for p, v in sorted(_tail_inc.items())},
        "certificate_slack": None if _SLACK is None else mp.nstr(_SLACK, 20),
        "worst_kkt_residual": mp.nstr(_res_worst, 12),
        "monotonicity_violations_in_T": _mono_viol,
        "_ascent_note": ("the certificate is valid at ANY w, so a badly converged ascent point "
                         "gives a SOUND but useless bound and nothing else reports it.  Two "
                         "guards: the KKT residual above, and the invariant that sup is "
                         "non-decreasing in T (padding the length-(T-1) optimum with a zero is "
                         "feasible at length T and has the same value, since Gamma is T-free).  "
                         "The second caught a cold-start ascent returning 1.8466 at T = 6 "
                         "against 2.0310 at T = 5 at pe = 2."),
        "ratio_to_enumerated": mp.nstr(B_BOT / INT_SUP_BOT, 20),
        "ratio_tangent_to_enumerated": mp.nstr(_B_TAN / INT_SUP_BOT, 20),
        "B_top_certified_7349": mp.nstr(B_TOP_CERT, 30),
        "gamma_max": mp.nstr(_gam_max, 20),
        "pe0_rigorous": _pe0,
        "_note": ("B_certified / B_bot are the RIGOROUS numbers; B_relax is the "
                  "coordinate-ascent value, a LOWER bound on the sup rather than an upper one.  "
                  "B_tangent is the T-free per-row cap sum -- valid, and the loose bound the "
                  "certificate exists to replace."),
    },
    "certificate_R4": {
        "form": ("G concave => G(u) <= G(w) + grad G(w).(u - w); the per-row tangent confines "
                 "each u_j to [lo_j, U_j] for any u reaching the incumbent, and the linear term "
                 "is maximised over that box"),
        "gradient": "analytic (gx, Rg, Wg in closed form), NOT a finite difference",
        "incumbent": mp.nstr(INCUMBENT, 30),
        "incumbent_provenance": (
            "the coordinate-ascent value, which is ACHIEVED at a feasible point and so is a "
            "valid lower bound on the sup; a larger incumbent narrows the box and tightens the "
            "bound, a smaller one only loosens it -- neither can invalidate it"),
        "slack": None if _SLACK is None else mp.nstr(_SLACK, 20),
        "slack_if_boundary_rows_mischarged": (None if _naive_star is None
                                              else mp.nstr(_naive_star, 12)),
        "rows": _cert_rows_star,
        "_trap": ("at the optimum the constrained rows sit ON the lower boundary with strictly "
                  "negative gradients (correct KKT).  Charging them |g_j|(U_j - lo_j) instead "
                  "of g_j(lo_j - w_j) destroys the result; the figure is recomputed every run."),
    },
    "all_T_certificate_R5": {
        "pe_of_best": _PE_ALLT, "rows_carried": len(_allT_rows),
        "bound": mp.nstr(B_ALLT, 30),
        "padded_rows_total_charge": mp.nstr(_allT_pad, 15),
        "tail_beyond_carried_rows": mp.nstr(_allT_tail, 15),
        "tail_mode": _allT_tmode,
        "by_pe": _allT,
        "why_it_covers_every_length": (
            "Gamma_j is independent of T (R3, measured across T = 3, 7, 11), so a length-T "
            "program is the restriction of one infinite program to its first T coordinates and "
            "padding the ascent point with zeros changes neither G(w) nor any box.  The padded "
            "rows are NOT charged zero: every Gamma_j is strictly positive -- in the pure AP it "
            "is exactly sum_{i odd >= 1} gx(b0_j + i), the odd gaps the one-body term reaches "
            "and the gap-2 ladder does not -- so their charges decay geometrically and are "
            "carried until negligible, after which the remainder is BOUNDED by its geometric "
            "tail rather than dropped."),
        "why_7349s_T0_does_not_transfer": (
            "#7349's blocks have every entry >= 1, so a row whose tangent slope falls below "
            "ln q0 / 2 contributes a strictly NEGATIVE cap and the cumulative cap eventually "
            "drops below the certified bound.  The bottom class permits zero entries, the "
            "relaxation therefore has u >= 0, every row cap is >= 0, and the cumulative cap is "
            "non-decreasing.  Reusing the T0 argument here would be a false transfer."),
    },
    "wall_depth_bound_R5": {
        "pe0": _pe0,
        "gamma_max_measured": mp.nstr(_gam_max, 20),
        "gamma_bound_uniform_in_pe": mp.nstr(_gam_uni, 20),
        "argument": ("every row of a block of length T in a pe-deep wall pays a linear cost "
                     "ln q0 * (pe - j) >= ln q0 * (pe - T + 1), while its slope is at most "
                     "2*Rg(0) uniformly in pe and j -- the one-body slope plus the downward "
                     "pair gains, which sit at distinct positive integer gaps and so sum to at "
                     "most Rg(0).  Past pe0 the per-row caps cannot sum to the incumbent."),
        "measured_range": PEMAX,
    },
    "cut_R6": {
        "via_G1": {"cut": _cut_g1, "blocks": _n_g1,
                   "assumption": "Xbot(s) <= Xblock(s) for every s"},
        "G1_free": {"cut": _cut_free, "blocks": _n_free,
                    "assumption": "none beyond the two certified edge bounds"},
    },
    "programs_R4": _r4,
    "restriction_R1": _r1,
    "open_gaps": {
        "G1_status": ("NOT proved and NOT refuted.  What changes is that the e_inf cut no "
                      "longer needs it: separate certified caps on the two edges give the same "
                      "finite window."),
        "what_remains": (f"certifying pe = {PEMAX + 1}..{_pe0} (this run certified pe <= "
                         f"{PEMAX}; the bound above is rigorous but the intermediate frames are "
                         f"not individually certified), and then the honest enumeration inside "
                         f"the G1-free cut"),
        "headline": "still the upper bound on M_n, which none of this touches",
    },
    "checks": [{"name": n, "ok": o, "detail": d} for n, o, d in CHECKS],
    "verdict": (
        "Carries #7349's concave-relaxation + supergradient-certificate route across to the "
        "bottom edge, over a frame that is two glued environments with an extra linear cost and "
        "a second unbounded dimension.  The payoff is not a proof of G1 but its elimination: "
        "with both edges certified separately the join's finite window follows without the "
        "Xbot <= Xblock assumption at all."
    ),
}

_out = os.path.join(_HERE, "rev-e-infinity-xbot-relaxation.witness.json")
with open(_out, "w") as fh:
    json.dump(_wit, fh, indent=2)
    fh.write("\n")
print(f"wrote {_out}")

_ok = sum(1 for _, o, _ in CHECKS if o)
print(f"{_ok}/{len(CHECKS)} checks pass")
sys.exit(0 if _ok == len(CHECKS) else 1)
