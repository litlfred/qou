#!/usr/bin/env python3
r"""
rev_e_infinity_closed_form_probe.py — both pieces of `e_inf` are CLOSED FORMS in `q0`
(qou-hok7)

PR #7335 reduced `e_inf`, the last unknown constant of the `REV_n` asymptotics, to

    e_inf  =  2 * E_edge  +  Xrun(2s)

— one edge energy and one run, each a `k`-free maximum over an explicit shape class, each
obtained by *search*.  This probe removes the search from the two values: **both are explicit
convergent series in `q0`**, and neither needs an enumeration to evaluate once its shape is
fixed.

## The run

A run of `ell` consecutive `-1`s inside a bi-infinite arithmetic progression of gap 2 leaves
every internal gap alone and moves only the pairs that straddle it.  Collecting those by
distance and re-indexing (the swap `sum_{j<=ell} sum_{d>=j} = sum_d min(d, ell)`),

    Xrun(ell)  =  sum_{d>=1} min(d, ell) * T(d)  -  (ln q0 / 2) * ell ,
    T(d)       =  2 eps(2d) - eps(2d-1) - eps(2d+1) .

`T` is a second difference of `eps` along the progression, so it decays like `q0^(-4d)` where
`eps` itself decays like `q0^(-2d)`.  Hence `Xrun` is **asymptotically linear** with slope
exactly `-ln q0 / 2` and an intercept that converges:

    C  =  sum_{d>=1} d * T(d)
       =  - sum_{r>=1} (1/r) * (q0^r - q0^(-r))^2 * q0^(-4r) / (1 - q0^(-4r))^2 ,

the second form obtained from `eps(m) = sum_r t^(-mr)/r` with `t = q0^2`, which turns the whole
double sum into a single Lambert-type series.  **The asymptote is not reached at the value
`e_inf` uses** — at `ell = 16` the exact `min(d, ell)` form and the linear asymptote differ by
~3e-4, four orders above anything else in this arc — so the `min` is load-bearing and the
intercept is a limit, not a shortcut.

## The edge

The same expansion closes the edge.  For a block `u` on the first `T` rows of a semi-infinite
AP, every block-to-bulk tail is

    sum_{d>=m} [ eps(2d) - eps(2d+u) ]
        =  sum_{r>=1} (1/r) * (1 - q0^(-2ur)) * q0^(-4mr) / (1 - q0^(-4r)) ,

so `E_edge` is a finite sum of Lambert series plus finitely many `eps` values.  What remains
discrete is only the **choice of block** — a finite optimisation whose bounds #7335 checked
non-binding (E5 there: 75073 -> 3317656 profiles, argmax unmoved).

## What this establishes, and what it does not

It establishes that `e_inf` is an explicit convergent series in `q0` given its argmax shape, and
that both closed forms are identities in `q` rather than coincidences at the substrate anchor —
R6 checks them across a sweep of `q`, which is the check that separates the two.

It does NOT close the search: the maximising block `[3,2,1,1,1]` and run length 16 still come
from #7335's enumeration, and nothing here proves them optimal.  Nor does it prove the limit
`e_k -> e_inf` exists; that still needs the upper bound on `M_n` the arc lacks.

## Checks

  R1  the run closed form reproduces the direct AP computation at every sampled `ell`
  R2  the run intercept agrees between the `d`-sum and the Lambert series — two routes
  R3  the edge closed form reproduces the direct computation, on the argmax and on others
  R4  assembling `2 * E_edge + Xrun(16)` from the closed forms reproduces #7335's `e_inf`
  R5  `Xrun` is asymptotically linear with slope `-ln q0 / 2` to the residual `T` predicts,
      and the asymptote is NOT reached at `ell = 16`
  R6  both closed forms hold across a sweep of `q` — identities, not anchor coincidences
  R7  each half of the run collects with the same multiplicity `min(d, ell)` SEPARATELY —
      the check that ties the two Lean lemmas to the two branches this probe walks

Proton-pinned; mpmath at 60 dps with truncation bounds DERIVED from each series' own decay
rate, never chosen.  Deriving them is not automatically getting them right: the first version
gave the intercept series `_depth(4, ...)` when its terms decay like `q^(-2r)` — the
`(q^r - q^-r)^2` factor cancels half the `q^(-4r)` — and the identity read as failing at 1e-30
when it was the depth that was short.  R5 had the mirror defect, demanding the secant slope
equal `-ln q0/2` exactly where the approach is asymptotic at a rate `T` predicts.  Both were
defects in the derivation, not the mathematics, and both are fixed at the derivation.
No float64.

-- Ref: [manuscript] folio/quantum-observable-universe/lean/QOU/BraidKnot/EdgeDecoupling.lean
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMPUTATIONS = os.path.dirname(_HERE)
if _COMPUTATIONS not in sys.path:
    sys.path.insert(0, _COMPUTATIONS)

from mpmath import mp  # noqa: E402

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.dps = 60
Q0 = Q_MP

# Truncation depths, DERIVED from the decay rates rather than chosen.  `eps(m) ~ q^(-2m)` and the
# Lambert terms decay like `q^(-4r)`, so to push both tails below 1e-`TARGET` we need
# `2m ln q > TARGET ln 10` and `4r ln q > TARGET ln 10`.
TARGET_DIGITS = 55
_LN10 = mp.log(10)


def _depth(per_step_exponent: int, q: mp.mpf) -> int:
    return int(mp.ceil(TARGET_DIGITS * _LN10 / (per_step_exponent * mp.log(q)))) + 5


CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'ok ' if ok else 'FAIL'}] {name}: {detail}", flush=True)


def make_eps(q: mp.mpf):
    t = q ** 2

    def eps(m: int) -> mp.mpf:
        return -mp.log(1 - t ** (-m)) if m > 0 else mp.mpf(0)

    return eps


# --------------------------------------------------------------------------------------------
# the run
# --------------------------------------------------------------------------------------------
def run_direct(ell: int, q: mp.mpf) -> mp.mpf:
    """A run of `ell` `-1`s in a bi-infinite AP of gap 2, summed pair by pair."""
    eps = make_eps(q)
    R = _depth(2, q)
    tot = mp.mpf(0)
    for a in range(ell):
        for d in range(1, R):
            if a + d >= ell:                     # below, outside the run
                tot += eps(2 * d) - eps(2 * d - 1)
        for d in range(1, R):
            if a - d < 0:                        # above, outside the run
                tot += eps(2 * d) - eps(2 * d + 1)
    return tot - mp.log(q) * ell / 2


def run_halves_direct(ell: int, q: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    """`run_direct`'s two branches kept apart: `(upward, downward)`, pair sums only.

    The two are generated by DIFFERENT conditions — `a - d < 0` above and `a + d >= ell` below —
    and carry different kernels.  Splitting them is what makes the correspondence to
    `EdgeDecoupling.sum_tails_eq_sum_min` / `sum_heads_eq_sum_min` checkable rather than
    asserted: those two lemmas are about the two conditions separately.
    """
    eps = make_eps(q)
    R = _depth(2, q)
    up = mp.mpf(0)
    down = mp.mpf(0)
    for a in range(ell):
        for d in range(1, R):
            if a + d >= ell:
                down += eps(2 * d) - eps(2 * d - 1)
            if a - d < 0:
                up += eps(2 * d) - eps(2 * d + 1)
    return up, down


def run_halves_closed(ell: int, q: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    """The same two branches via `sum_d min(d, ell) f(d)` — the two Lean lemmas, instantiated.

    `sum_tails_eq_sum_min` at `f d = eps(2d) - eps(2d+1)` gives the upward half;
    `sum_heads_eq_sum_min` at `f d = eps(2d) - eps(2d-1)` gives the downward one.  Both use the
    same multiplicity `min(d, ell)`, which is the content of `card_filter_lt` / `card_filter_ge`.
    """
    eps = make_eps(q)
    R = _depth(2, q)
    up = mp.fsum(min(d, ell) * (eps(2 * d) - eps(2 * d + 1)) for d in range(1, R))
    down = mp.fsum(min(d, ell) * (eps(2 * d) - eps(2 * d - 1)) for d in range(1, R))
    return up, down


def run_closed(ell: int, q: mp.mpf) -> mp.mpf:
    """`sum_d min(d, ell) T(d) - (ln q / 2) ell`, the re-indexed form."""
    eps = make_eps(q)
    D = _depth(4, q)
    T = [2 * eps(2 * d) - eps(2 * d - 1) - eps(2 * d + 1) for d in range(1, D)]
    return mp.fsum(min(d, ell) * T[d - 1] for d in range(1, D)) - mp.log(q) * ell / 2


def run_intercept_dsum(q: mp.mpf) -> mp.mpf:
    eps = make_eps(q)
    D = _depth(4, q)
    return mp.fsum(d * (2 * eps(2 * d) - eps(2 * d - 1) - eps(2 * d + 1)) for d in range(1, D))


def run_intercept_lambert(q: mp.mpf) -> mp.mpf:
    """`- sum_r (1/r) (q^r - q^-r)^2 q^(-4r) / (1 - q^(-4r))^2`.

    Depth uses rate 2, NOT 4: the `(q^r - q^-r)^2` factor contributes `q^(2r)`, which cancels
    half of the `q^(-4r)`, so the terms decay like `q^(-2r)`.  Using `_depth(4, ...)` here gave
    the series half the depth it needs and the identity appeared to fail at 1e-30 — a truncation
    artefact of the derivation, not of the mathematics.
    """
    R = _depth(2, q)
    return -mp.fsum((mp.mpf(1) / r) * (q ** r - q ** (-r)) ** 2
                    * q ** (-4 * r) / (1 - q ** (-4 * r)) ** 2
                    for r in range(1, R))


# --------------------------------------------------------------------------------------------
# the edge
# --------------------------------------------------------------------------------------------
def edge_direct(u, q: mp.mpf) -> mp.mpf:
    """Block `u` at the free head of a semi-infinite AP of gap 2, summed pair by pair."""
    eps = make_eps(q)
    R = _depth(2, q)
    n = len(u)
    tot = mp.mpf(0)
    for i in range(n):
        for j in range(i + 1, n):
            tot += eps(2 * (j - i)) - eps(2 * (j - i) + u[i] - u[j])
        for d in range(n - i, R):
            tot += eps(2 * d) - eps(2 * d + u[i])
    return tot - mp.log(q) * sum(x * x for x in u) / 2


def _tail_lambert(m: int, u: int, q: mp.mpf) -> mp.mpf:
    """`sum_{d>=m} [eps(2d) - eps(2d+u)] = sum_r (1/r)(1 - q^(-2ur)) q^(-4mr)/(1 - q^(-4r))`."""
    R = _depth(4, q)
    return mp.fsum((mp.mpf(1) / r) * (1 - q ** (-2 * u * r))
                   * q ** (-4 * m * r) / (1 - q ** (-4 * r))
                   for r in range(1, R))


def edge_closed(u, q: mp.mpf) -> mp.mpf:
    eps = make_eps(q)
    n = len(u)
    tot = mp.mpf(0)
    for i in range(n):
        for j in range(i + 1, n):
            tot += eps(2 * (j - i)) - eps(2 * (j - i) + u[i] - u[j])
        tot += _tail_lambert(n - i, u[i], q)
    return tot - mp.log(q) * sum(x * x for x in u) / 2


# The argmax #7335 found.  It is an INPUT here, not a result: this probe closes the two VALUES,
# not the search that picked their shapes.
TOP = (3, 2, 1, 1, 1)
ELL = 16
TOL = mp.mpf(10) ** (-(TARGET_DIGITS - 5))    # derived from TARGET_DIGITS, not chosen

# --------------------------------------------------------------------------------------------
print("e_inf's two pieces as closed forms in q0")
print(f"  q0 = {mp.nstr(Q0, 20)} (proton pin);  mp.dps = {mp.dps}")
print(f"  series depths derived from the decay rates for {TARGET_DIGITS} digits: "
      f"eps {_depth(2, Q0)}, Lambert {_depth(4, Q0)};  comparison floor {mp.nstr(TOL, 3)}")
print(flush=True)

# --------------------------------------------------------------------------------------------
print("R1  the run closed form against the direct AP sum")
_r1 = []
for _ell in (1, 2, 3, 5, 8, 12, 16, 20, 24, 32):
    a, b = run_direct(_ell, Q0), run_closed(_ell, Q0)
    _r1.append({"ell": _ell, "direct": mp.nstr(a, 26), "closed": mp.nstr(b, 26),
                "difference": mp.nstr(a - b, 6)})
    print(f"    ell = {_ell:3d}: {mp.nstr(a, 24):28s} vs {mp.nstr(b, 24):28s}  "
          f"diff {mp.nstr(a - b, 4)}", flush=True)
_r1_worst = max(abs(mp.mpf(r["difference"])) for r in _r1)
check(
    "R1 the re-indexed run form reproduces the direct pair sum at every sampled length",
    _r1_worst < TOL,
    f"{len(_r1)} lengths from 1 to 32; worst difference {mp.nstr(_r1_worst, 4)} against a floor "
    f"of {mp.nstr(TOL, 3)} derived from the {TARGET_DIGITS}-digit truncation depths.  The direct "
    f"side walks every straddling pair of the run; the closed side is one sum over distances, "
    f"so this checks the re-indexing `sum_{{j<=ell}} sum_{{d>=j}} = sum_d min(d, ell)` rather "
    f"than restating it",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("R7  each half of the run separately — the two Lean lemmas, instantiated")
_r7 = []
for _ell in (1, 2, 3, 5, 8, 12, 16, 24):
    _ud, _dd = run_halves_direct(_ell, Q0)
    _uc, _dc = run_halves_closed(_ell, Q0)
    _r7.append({"ell": _ell,
                "up_direct": mp.nstr(_ud, 26), "up_closed": mp.nstr(_uc, 26),
                "down_direct": mp.nstr(_dd, 26), "down_closed": mp.nstr(_dc, 26),
                "up_difference": mp.nstr(_ud - _uc, 6),
                "down_difference": mp.nstr(_dd - _dc, 6)})
    print(f"    ell = {_ell:3d}:  up {mp.nstr(_ud, 18):22s} diff {mp.nstr(_ud - _uc, 4):10s}"
          f"   down {mp.nstr(_dd, 18):22s} diff {mp.nstr(_dd - _dc, 4)}", flush=True)
_r7_worst = max(max(abs(mp.mpf(r["up_difference"])), abs(mp.mpf(r["down_difference"])))
                for r in _r7)
_r7_asym = max(abs(mp.mpf(r["up_direct"]) - mp.mpf(r["down_direct"])) for r in _r7)
check(
    "R7 both halves of the run collect with the SAME multiplicity min(d, ell), separately",
    _r7_worst < TOL,
    f"{len(_r7)} lengths; worst difference {mp.nstr(_r7_worst, 4)} against a floor of "
    f"{mp.nstr(TOL, 3)}.  R1 checks the SUM of the two halves, which a compensating error in "
    f"the split would survive; this checks each half on its own, so it is the check that ties "
    f"`EdgeDecoupling.sum_tails_eq_sum_min` (upward, condition `j < d`, kernel "
    f"`eps(2d) - eps(2d+1)`) and `sum_heads_eq_sum_min` (downward, condition `ell <= j + d`, "
    f"kernel `eps(2d) - eps(2d-1)`) to the two branches the probe actually walks.  The two "
    f"halves are NOT equal to one another — they differ by up to {mp.nstr(_r7_asym, 4)}, since "
    f"the AP is asymmetric about a displaced row — so agreeing with the same multiplicity is a "
    f"statement about the counting, not about a symmetry",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("R2  the run intercept, two independent routes")
_c_d = run_intercept_dsum(Q0)
_c_l = run_intercept_lambert(Q0)
print(f"    sum_d d*T(d)     = {mp.nstr(_c_d, 30)}")
print(f"    Lambert series   = {mp.nstr(_c_l, 30)}")
print(f"    difference       = {mp.nstr(_c_d - _c_l, 6)}")
check(
    "R2 the run's intercept agrees between the distance sum and the Lambert series",
    abs(_c_d - _c_l) < TOL,
    f"C = {mp.nstr(_c_d, 26)}, difference {mp.nstr(_c_d - _c_l, 4)}.  The two routes share no "
    f"algebra: one sums the second difference `T(d)` over distances, the other expands "
    f"`eps(m) = sum_r t^(-mr)/r` and resums, giving "
    f"`C = -sum_r (1/r)(q^r - q^-r)^2 q^(-4r)/(1 - q^(-4r))^2`.  That second form is a single "
    f"Lambert-type series in q0 with no reference to the lattice at all",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("R3  the edge closed form against the direct AP sum")
_r3 = []
for _u in [TOP, (1,), (2,), (2, 1), (3, 2, 1), (1, 1, 1, 1), (4, 3, 2, 1, 1), (2, 2, 1, 1, 1)]:
    a, b = edge_direct(list(_u), Q0), edge_closed(list(_u), Q0)
    _r3.append({"block": list(_u), "direct": mp.nstr(a, 26), "closed": mp.nstr(b, 26),
                "difference": mp.nstr(a - b, 6)})
    print(f"    {str(list(_u)):18s}: {mp.nstr(a, 24):28s} vs {mp.nstr(b, 24):28s}  "
          f"diff {mp.nstr(a - b, 4)}", flush=True)
_r3_worst = max(abs(mp.mpf(r["difference"])) for r in _r3)
check(
    "R3 the Lambert-tail edge form reproduces the direct pair sum on every sampled block",
    _r3_worst < TOL,
    f"{len(_r3)} blocks including the argmax {list(TOP)}; worst difference "
    f"{mp.nstr(_r3_worst, 4)} against the {mp.nstr(TOL, 3)} floor.  Each block-to-bulk tail "
    f"`sum_{{d>=m}}[eps(2d) - eps(2d+u)]` becomes "
    f"`sum_r (1/r)(1 - q^(-2ur)) q^(-4mr)/(1 - q^(-4r))`, so the edge is a finite sum of "
    f"Lambert series plus finitely many eps values — an explicit function of q, evaluated "
    f"without any lattice sum",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("R4  e_inf assembled from the two closed forms")
_E = edge_closed(list(TOP), Q0)
_R = run_closed(ELL, Q0)
_e_inf_closed = 2 * _E + _R
_WIT = os.path.join(_HERE, "rev-e-infinity-edge-limit.witness.json")
_e_inf_search = mp.mpf(json.load(open(_WIT))["e_infinity"]["value"])
print(f"    E_edge{list(TOP)}  = {mp.nstr(_E, 28)}")
print(f"    Xrun({ELL})            = {mp.nstr(_R, 28)}")
print(f"    2*E_edge + Xrun     = {mp.nstr(_e_inf_closed, 30)}")
print(f"    #7335 search value  = {mp.nstr(_e_inf_search, 30)}")
print(f"    difference          = {mp.nstr(_e_inf_closed - _e_inf_search, 6)}")
# #7335's witness records 30 significant digits, so that recording is the floor here.
_r4_floor = abs(_e_inf_search) * mp.mpf(10) ** (-29)
check(
    "R4 the closed forms reproduce #7335's searched e_inf",
    abs(_e_inf_closed - _e_inf_search) < _r4_floor,
    f"closed {mp.nstr(_e_inf_closed, 28)} against the searched "
    f"{mp.nstr(_e_inf_search, 28)} — difference "
    f"{mp.nstr(_e_inf_closed - _e_inf_search, 4)}, at a floor of {mp.nstr(_r4_floor, 3)} set by "
    f"the 30 significant digits #7335's witness records.  #7335 obtained this number by "
    f"exhaustive search over a shape class in scaled-integer arithmetic; this obtains it by "
    f"evaluating two series.  Nothing is shared but the argmax shape",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("R5  is the run already linear at the length e_inf uses?")
_slope_exact = -mp.log(Q0) / 2
_asym = [(l, run_closed(l, Q0), _c_d + _slope_exact * l) for l in (8, 16, 24, 32, 48, 64, 96)]
for l, exact, lin in _asym:
    print(f"    ell = {l:3d}: exact {mp.nstr(exact, 22):26s} asymptote "
          f"{mp.nstr(lin, 22):26s} gap {mp.nstr(exact - lin, 4)}")
_gap16 = [g for l, e, a in _asym for g in [e - a] if l == ELL][0]
_gap96 = [g for l, e, a in _asym for g in [e - a] if l == 96][0]
_slope_num = (run_closed(200, Q0) - run_closed(100, Q0)) / 100
# The secant slope is NOT exactly -ln q0/2 at finite ell, and demanding that it be is a
# mis-specified check.  Each unit step of ell adds `S(ell+1) = sum_{d>ell} T(d)` on top of the
# linear part, so the secant over [100, 200] is off by at most the largest such increment in
# the window.  That bound is COMPUTED from the same T, not chosen.
_eps_q0 = make_eps(Q0)
_slope_bound = abs(mp.fsum(2 * _eps_q0(2 * d) - _eps_q0(2 * d - 1) - _eps_q0(2 * d + 1)
                           for d in range(101, _depth(4, Q0))))
check(
    "R5 the run is asymptotically linear with slope -ln q0 / 2 to the predicted residual, and "
    "the asymptote is NOT reached at the length e_inf uses",
    abs(_slope_num - _slope_exact) <= _slope_bound
    and abs(_gap16) > mp.mpf("1e-5") > abs(_gap96),
    f"the secant slope over ell = 100..200 is {mp.nstr(_slope_num, 22)} against "
    f"-ln q0/2 = {mp.nstr(_slope_exact, 22)}, differing by "
    f"{mp.nstr(_slope_num - _slope_exact, 4)} against a computed bound of "
    f"{mp.nstr(_slope_bound, 4)} — the largest per-step residual `sum_{{d>100}} T(d)` in that "
    f"window.  So the linear part is the quadratic cost and nothing else, and the approach is "
    f"at exactly the rate T predicts.  At ell = {ELL}, the "
    f"length e_inf actually uses, the exact form and the asymptote still differ by "
    f"{mp.nstr(_gap16, 4)}, four orders above anything else in this arc, falling to "
    f"{mp.nstr(_gap96, 4)} by ell = 96.  So `min(d, ell)` is load-bearing and the intercept C "
    f"is a limit rather than a shortcut — quoting `C - (ln q0/2) ell` as Xrun would corrupt "
    f"e_inf in its fourth decimal",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("R6  are these identities in q, or coincidences at the anchor?")
_r6 = []
for _q in ("1.03", "1.07", "1.10997858275138080760", "1.25", "1.6", "2.5"):
    q = mp.mpf(_q)
    dr, cr = run_direct(6, q), run_closed(6, q)
    de, ce = edge_direct([3, 2, 1], q), edge_closed([3, 2, 1], q)
    ci, cl = run_intercept_dsum(q), run_intercept_lambert(q)
    _r6.append({"q": _q, "run_difference": mp.nstr(dr - cr, 6),
                "edge_difference": mp.nstr(de - ce, 6),
                "intercept_difference": mp.nstr(ci - cl, 6)})
    print(f"    q = {_q:24s} run {mp.nstr(dr - cr, 4):12s} edge {mp.nstr(de - ce, 4):12s} "
          f"intercept {mp.nstr(ci - cl, 4)}", flush=True)
_r6_worst = max(max(abs(mp.mpf(r[k])) for k in
                    ("run_difference", "edge_difference", "intercept_difference")) for r in _r6)
check(
    "R6 both closed forms hold across a sweep of q — identities, not anchor coincidences",
    _r6_worst < TOL,
    f"six values of q from 1.03 to 2.5, spanning the substrate anchor; worst difference across "
    f"all three identities {mp.nstr(_r6_worst, 4)} against the {mp.nstr(TOL, 3)} floor.  This is "
    f"the check that separates an identity from a numerical coincidence: a closed form fitted to "
    f"one anchor would not survive q = 2.5, where eps decays an order faster and the series "
    f"depths derived above shrink accordingly",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print(f"  e_inf = 2 * E_edge{list(TOP)} + Xrun({ELL}) = {mp.nstr(_e_inf_closed, 30)}")
print(f"  E_edge = {mp.nstr(_E, 30)}")
print(f"  Xrun({ELL}) = {mp.nstr(_R, 30)}   (intercept C = {mp.nstr(_c_d, 24)}, "
      f"slope -ln q0/2 = {mp.nstr(_slope_exact, 24)})")
print()

_wit = {
    "schema": "https://litlfred.github.io/qou/schemas/witness/v1",
    "computedAt": datetime.now(timezone.utc).isoformat(),
    "computation": {"script": "computations/deltalambda/rev_e_infinity_closed_form_probe.py"},
    "bean": "qou-hok7",
    "anchor": "physical_proton",
    # Canonical anchor key read by the q0 audits/ratchet (the "anchor" key above is
    # a near-miss spelling they cannot see), plus scriptFile provenance.
    "q0Anchor": "proton",
    "scriptFile": os.path.basename(__file__),
    "q0Value": Q_50_DIGIT_STR,
    "description": (
        "Both pieces of e_inf -- the edge energy and the run -- are explicit convergent series "
        "in q0, so the last unknown constant of the REV_n asymptotics no longer needs an "
        "enumeration to evaluate.  The run re-indexes to sum_d min(d,ell) T(d) - (ln q0/2) ell "
        "with T the second difference of eps along the progression, whose intercept resums to a "
        "single Lambert-type series; the edge's block-to-bulk tails resum the same way.  Both "
        "are checked against the direct pair sums and across a sweep of q, so they are "
        "identities rather than anchor coincidences.  What is NOT closed is the SEARCH: the "
        "maximising block [3,2,1,1,1] and run length 16 are inputs here, taken from PR #7335, "
        "and nothing in this probe proves them optimal.  Nor does anything here prove the limit "
        "e_k -> e_inf exists -- the upper bound on M_n is still open."
    ),
    "constants": {
        "ln_q0": mp.nstr(mp.log(Q0), 30), "mp_dps": mp.dps,
        "target_digits": TARGET_DIGITS, "eps_depth": _depth(2, Q0),
        "lambert_depth": _depth(4, Q0), "comparison_floor": mp.nstr(TOL, 6),
    },
    "run_closed_form": {
        "formula": "Xrun(ell) = sum_{d>=1} min(d,ell) T(d) - (ln q0 / 2) ell",
        "T": "T(d) = 2 eps(2d) - eps(2d-1) - eps(2d+1)",
        "intercept_formula":
            "C = sum_d d T(d) = -sum_r (1/r)(q^r - q^-r)^2 q^(-4r)/(1 - q^(-4r))^2",
        "intercept_value": mp.nstr(_c_d, 30),
        "slope": mp.nstr(_slope_exact, 30),
        "value_at_16": mp.nstr(_R, 30),
        "checks_R1": _r1,
        "halves_R7": {
            "lean_upward": "QOU.BraidKnot.EdgeDecoupling.sum_tails_eq_sum_min",
            "lean_downward": "QOU.BraidKnot.EdgeDecoupling.sum_heads_eq_sum_min",
            "lean_combined": "QOU.BraidKnot.EdgeDecoupling.run_pair_sum_eq_sum_min",
            "upward_condition": "j < d", "upward_kernel": "eps(2d) - eps(2d+1)",
            "downward_condition": "ell <= j + d", "downward_kernel": "eps(2d) - eps(2d-1)",
            "max_half_asymmetry": mp.nstr(_r7_asym, 20),
            "rows": _r7,
        },
    },
    "edge_closed_form": {
        "tail_formula":
            "sum_{d>=m}[eps(2d) - eps(2d+u)] = sum_r (1/r)(1 - q^(-2ur)) q^(-4mr)/(1 - q^(-4r))",
        "block": list(TOP), "value": mp.nstr(_E, 30),
        "checks_R3": _r3,
    },
    "assembled_R4": {
        "closed": mp.nstr(_e_inf_closed, 30), "searched_7335": mp.nstr(_e_inf_search, 30),
        "difference": mp.nstr(_e_inf_closed - _e_inf_search, 20),
    },
    "asymptotics_R5": {
        "slope_exact": mp.nstr(_slope_exact, 30),
        "slope_secant_100_200": mp.nstr(_slope_num, 30),
        "slope_residual_bound": mp.nstr(_slope_bound, 20),
        "gap_at_16": mp.nstr(_gap16, 20), "gap_at_96": mp.nstr(_gap96, 20),
        "rows": [{"ell": l, "exact": mp.nstr(e, 26), "asymptote": mp.nstr(a, 26),
                  "gap": mp.nstr(e - a, 10)} for l, e, a in _asym],
    },
    "q_sweep_R6": _r6,
    "checks": [{"name": n, "ok": o, "detail": d} for n, o, d in CHECKS],
    "verdict": (
        "e_inf = 2 * E_edge + Xrun(2s) is an explicit convergent series in q0 once its argmax "
        "shape is fixed: the run re-indexes to a distance sum whose intercept is a Lambert "
        "series, and the edge's tails resum the same way.  Verified against the direct pair "
        "sums, against PR #7335's independently searched value to the 30 digits its witness "
        "records, and across a sweep of q -- identities, not anchor coincidences.  The SEARCH "
        "for the argmax shape is not closed, and the existence of the limit is still open."
    ),
}
_out = os.path.join(_HERE, "rev-e-infinity-closed-form.witness.json")
with open(_out, "w") as fh:
    json.dump(_wit, fh, indent=2)
    fh.write("\n")
print(f"wrote {_out}")

_ok = sum(1 for _, o, _ in CHECKS if o)
print(f"{_ok}/{len(CHECKS)} checks pass")
sys.exit(0 if _ok == len(CHECKS) else 1)
