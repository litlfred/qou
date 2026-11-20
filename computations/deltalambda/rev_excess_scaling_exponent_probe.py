#!/usr/bin/env python3
r"""
rev_excess_scaling_exponent_probe.py — is the excess over the staircase o(sqrt n)?  If so my own
#7286 verdict is WRONG and the coefficient IS A*sqrt2 (qou-hok7)

#7286 (merged f9eab7472ea) established two things that are in tension, and it did not notice:

  (a) the Theta(sqrt n) coefficient bracket's width is ONE term, `C - A = E_2`, the staircase's
      pair term, discarded by the row-tangent bound's `R <= (l-1)C` step; and
  (b) the staircase is BEATEN at its own row count, by +0.245 / +0.492 / +0.815 / +0.893 at
      k = 12/16/24/35.

From (b) that PR concluded "A*sqrt2 is the staircase's rate, not the optimum's, and the
coefficient is strictly above it."  **That conclusion assumes the excess is Theta(sqrt n), and
the PR never checked it.**  The excess is a difference of two quantities that are each
Theta(sqrt n); a difference growing like n^{1/4}, or log n, is o(sqrt n) and leaves the
COEFFICIENT exactly `A*sqrt2` while every measured number stays as recorded.

This is not a hypothetical distinction.  #7286's own five points already lean the other way:

    excess / sqrt n   0.0236  0.0783  0.1043  0.1129  0.0947   <- turns over
    excess / n^{1/4}  0.0579  0.2325  0.3562  0.4697  0.4743   <- flattens

Five points at triangular n cannot settle an exponent, which is why #7286 was right to decline
the reading and wrong to assert its negation.  This probe extends the lever arm and estimates
the exponent.

## Why the exponent decides the whole question

`M_n = max_lambda (R - E)`.  Rigidity (#7286 commit 2) pins a maximiser's mean beta-gap to
`2 + O(1/sqrt n)`, hence `l = sqrt(2n)(1 + o(1))`.  If additionally the excess over the
staircase is `o(sqrt n)`, then

    M_n = V(staircase) + o(sqrt n) = A*sqrt(2n) + o(sqrt n) ,

so `lim M_n / sqrt n = A*sqrt2` EXACTLY -- the coefficient is identified, the bracket collapses
from `[A*sqrt2, C*sqrt2]` to a point, and what remains open is only the subleading term.  If
instead the excess is `Theta(sqrt n)` with a positive constant, the coefficient is strictly
larger and #7286's verdict stands.

## Method, and its one-sidedness

Local search at FIXED `(n, l)` with the move `beta_i += 1, beta_j -= 1`, which preserves both.
Evaluation is INCREMENTAL (`O(l)` per candidate move rather than `O(l^2)`), which is what buys
the extra `n`.  The search is a heuristic: a value found is a genuine lower bound on `M_n`, a
value NOT found proves nothing.  So a measured exponent is an estimate of a lower envelope, and
an under-performing search at large `n` biases the exponent DOWN -- i.e. toward the conclusion
this probe would otherwise reach.  R4 states that asymmetry rather than burying it.

## Checks

  R1  calibration — reproduce #7286's five excesses with the incremental evaluator
  R2  extend the lever arm to larger n
  R3  the exponent, by successive log-log slopes and by a two-point fit at the top end
  R4  the verdict, including what would have to be true for it to be wrong

Proton-pinned; no Markov parameter in this cone, so convention C/D does not arise.  Exact
integers for n/H (identities (II)/(III), Lean as of #7282).  mpmath throughout; no float64.
"""

from __future__ import annotations

import json
import os
import sys
import time
from datetime import datetime, timezone

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMPUTATIONS = os.path.dirname(_HERE)
if _COMPUTATIONS not in sys.path:
    sys.path.insert(0, _COMPUTATIONS)

from mpmath import mp  # noqa: E402

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

from hmin_closed_form_and_rev_sublinearity_probe import H_min_closed  # noqa: E402

mp.dps = 30
Q0 = Q_MP
LNQ = mp.log(Q0)
T = Q0 ** 2

_NEPS = 4000
EPS = [mp.mpf(0)] + [-mp.log(1 - T ** (-m)) for m in range(1, _NEPS)]
_F = [mp.mpf(0)] * _NEPS
for _m in range(1, _NEPS):
    _F[_m] = _F[_m - 1] + EPS[_m]
C_CONST = _F[_NEPS - 1]
A_CONST = sum(EPS[m] for m in range(1, _NEPS, 2))
E2_CONST = sum(EPS[m] for m in range(2, _NEPS, 2))


def F(k: int) -> mp.mpf:
    return _F[k] if k < _NEPS else C_CONST


def eps(m: int) -> mp.mpf:
    return EPS[m] if 0 < m < _NEPS else mp.mpf(0)


CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'ok ' if ok else 'FAIL'}] {name}: {detail}")


# --------------------------------------------------------------------------------------------
# exact H / n / V from a beta-set  (identities (II) and (III); Lean as of PR #7282)
# --------------------------------------------------------------------------------------------
def H_of(b: list[int]) -> int:
    L = len(b)
    pair = sum((L - 1 - 2 * i) * v for i, v in enumerate(b))
    return sum(v * (v + 1) // 2 for v in b) - pair


def V_of(b: list[int], n: int, hmin: int) -> mp.mpf:
    L = len(b)
    tot = sum((F(v) for v in b), mp.mpf(0))
    for i in range(L):
        bi = b[i]
        for j in range(i + 1, L):
            tot -= eps(bi - b[j])
    return tot - F(n) - (H_of(b) - hmin) * LNQ


def _valid(b: list[int], i: int, j: int) -> bool:
    """Does `beta_i += 1, beta_j -= 1` keep the beta-set strictly decreasing and non-negative?

    🛑 The obvious two-clause test is WRONG and cost this probe a cycling run: checking only
    `b[i]+1 != b[i-1]` and `b[j]-1 != b[j+1]` misses the ADJACENT case. With `j == i-1` and a
    gap of exactly 2, both clauses pass and the move still collides (`b[i]+1 == b[i-1]-1`),
    producing a duplicate beta. `eps(0)` is 0, so the corrupted state evaluates without error
    and the best-improvement climb oscillates forever. Test the ACTUAL post-move adjacencies.
    """
    L = len(b)
    if i == j or b[j] - 1 < 0:
        return False

    def val(t: int) -> int:
        return b[t] + 1 if t == i else (b[t] - 1 if t == j else b[t])

    for t in (i - 1, i, j - 1, j):
        if 0 <= t < L - 1 and val(t) <= val(t + 1):
            return False
    return True


def delta_V(b: list[int], i: int, j: int) -> mp.mpf | None:
    """Exact change in V for `beta_i += 1, beta_j -= 1`, in O(l).  None if the move is invalid.

    Valid moves preserve the sorted order (that is what `_valid` enforces), so no re-sort is
    needed and the index-dependent `c_i = L-1-2i` coefficients stay attached to their rows.
    """
    if not _valid(b, i, j):
        return None
    L = len(b)
    bi, bj = b[i], b[j]
    d = eps(bi + 1) - eps(bj)                       # one-body
    for m in range(L):                              # two-body
        if m == i or m == j:
            continue
        bm = b[m]
        d -= eps(abs(bi + 1 - bm)) - eps(abs(bi - bm))
        d -= eps(abs(bj - 1 - bm)) - eps(abs(bj - bm))
    # 🛑 abs() is load-bearing on BOTH terms. `i > j` is a legal move (raise a lower beta,
    # lower a higher one), and then `bi - bj < 0`; `eps` returns 0 on a non-positive argument,
    # so writing these unsigned drops the (i,j) pair contribution SILENTLY. Caught by R0's
    # recompute check at a discrepancy of 0.9044 — never by the climb, which happily maximised
    # the wrong functional.
    d -= eps(abs(bi + 1 - (bj - 1))) - eps(abs(bi - bj))
    dH = (bi + 1 - bj) - 2 * (j - i)                # exact integer; no ordering assumption
    return d - dH * LNQ


def climb(b: list[int], rounds: int = 200000) -> list[int]:
    """Best-improvement hill climb on the (i,j) move set, incremental.

    Exhausting `rounds` RAISES rather than returning quietly: with exact arithmetic V strictly
    increases every step, so hitting the cap means the move accounting is wrong (see `_valid`)
    and a silent return would ship a corrupted beta-set as a result.
    """
    b = list(b)
    L = len(b)
    for _ in range(rounds):
        best_d, best_ij = mp.mpf("1e-22"), None
        for i in range(L):
            for j in range(L):
                if i == j:
                    continue
                d = delta_V(b, i, j)
                if d is not None and d > best_d:
                    best_d, best_ij = d, (i, j)
        if best_ij is None:
            return b
        i, j = best_ij
        b[i] += 1
        b[j] -= 1
    raise RuntimeError(
        f"climb exhausted {rounds} rounds on l = {L} — V must strictly increase each step, so "
        f"this means the move accounting is wrong, not that the optimum is far away"
    )


def seed_beta(n: int, L: int) -> list[int] | None:
    """A partition of n into exactly L positive parts, staircase-shaped, as beta-numbers."""
    if n < L:
        return None
    rem = n - L
    w = [L - i for i in range(L)]
    tot = sum(w)
    lam = [1 + rem * w[i] // tot for i in range(L)]
    short = n - sum(lam)
    i = 0
    while short > 0:
        lam[i % L] += 1
        short -= 1
        i += 1
    lam.sort(reverse=True)
    return [lam[i] + (L - 1 - i) for i in range(L)]


def best_over_l(n: int, k: int, extra: int = 5) -> tuple[mp.mpf, int]:
    hmin = H_min_closed(n)
    best, best_l = None, None
    for L in range(k, k + extra + 1):
        s = seed_beta(n, L)
        if s is None:
            continue
        b = climb(s)
        v = V_of(b, n, hmin)
        if best is None or v > best:
            best, best_l = v, L
    return best, best_l


# --------------------------------------------------------------------------------------------
# R0 — self-test on the incremental evaluator (the guard for the bug that cost a run)
# --------------------------------------------------------------------------------------------
print("R0  self-test — delta_V against a full recompute, and the adjacent-collision case")

# (a) the SPECIFIC blind spot: j == i-1 with a gap of exactly 2. The naive two-clause test
#     ("b[i]+1 != b[i-1]" and "b[j]-1 != b[j+1]") passes here and the move still collides.
_adj = [9, 7, 5, 3, 1]                     # all gaps 2
_naive_would_allow = (_adj[1] + 1 != _adj[0]) and (_adj[0] - 1 != _adj[1])
_we_reject = not _valid(_adj, 1, 0)        # raise beta_1, lower beta_0: 9,7 -> 8,8
check(
    "R0 the adjacent gap-2 collision is rejected (and the naive test would NOT have been)",
    _we_reject and _naive_would_allow,
    "on beta = (9,7,5,3,1), the move (i=1, j=0) gives (8,8,...) — a duplicate. The naive "
    "two-clause test allows it; _valid rejects it. This is the bug that cycled the first run",
)

# (b) delta_V must equal the full recompute on every valid move of a few configurations.
_st_n, _st_L = 36, 9
_probe_sets = [
    [15, 13, 11, 9, 7, 5, 3, 1, 0],
    [17, 12, 10, 8, 6, 4, 3, 2, 0],
    [20, 14, 11, 7, 5, 4, 2, 1, 0],
]
_worst_dv = mp.mpf(0)
_n_moves = 0
for _b in _probe_sets:
    _n0 = sum(_b) - _st_L * (_st_L - 1) // 2
    _hm = H_min_closed(_n0)
    _v0 = V_of(_b, _n0, _hm)
    for _i in range(_st_L):
        for _j in range(_st_L):
            _d = delta_V(_b, _i, _j)
            if _d is None:
                continue
            _c = list(_b)
            _c[_i] += 1
            _c[_j] -= 1
            assert all(_c[t] > _c[t + 1] for t in range(_st_L - 1)), "_valid let a bad move by"
            _worst_dv = max(_worst_dv, abs(V_of(_c, _n0, _hm) - _v0 - _d))
            _n_moves += 1
# The coverage floor is 50, not 100: the three l = 9 configurations admit 98 valid moves and a
# threshold of 100 fails the check on its own arithmetic rather than on the evaluator. (It did,
# on the run that found the abs() bug — the accuracy was already 2.0e-29.)
check(
    "R0 delta_V equals the O(l^2) recompute on every valid move",
    _worst_dv < mp.mpf("1e-25") and _n_moves >= 50,
    f"worst |delta_V - (V_after - V_before)| = {mp.nstr(_worst_dv, 4)} over {_n_moves} valid "
    f"moves on 3 configurations (~1 ulp at dps {mp.dps}); every accepted move also verified "
    f"strictly decreasing",
)

# --------------------------------------------------------------------------------------------
# R1 — calibration against #7286's committed excesses
# --------------------------------------------------------------------------------------------
print()
print("R1  calibration — reproduce #7286's five excesses with the INCREMENTAL evaluator")
_REF = {36: "0.14183108", 78: "0.69117475", 136: "1.2164376", 300: "1.9550307",
        630: "2.3763657"}
print(f"    {'n':>6} {'k':>4} {'excess':>14} {'#7286':>14} {'gap':>10}")
_cal = []
for k in (8, 12, 16, 24, 35):
    n = k * (k + 1) // 2
    hmin = H_min_closed(n)
    stair = [2 * k - 1 - 2 * i for i in range(k)]
    v_st = V_of(stair, n, hmin)
    v_best, _ = best_over_l(n, k)
    e = v_best - v_st
    ref = mp.mpf(_REF[n])
    ok = abs(e - ref) < mp.mpf("1e-6")
    _cal.append((n, e, ref, ok))
    print(f"    {n:6d} {k:4d} {mp.nstr(e, 10):>14} {_REF[n]:>14} "
          f"{mp.nstr(abs(e - ref), 4):>10}")
check(
    "R1 the incremental evaluator reproduces #7286's excesses",
    all(c[3] for c in _cal),
    f"{sum(1 for c in _cal if c[3])}/{len(_cal)} to 1e-6 — O(l) delta_V against the O(l^2) "
    f"recompute, best-improvement instead of first-improvement, same answers",
)

# --------------------------------------------------------------------------------------------
# R2 — extend the lever arm
# --------------------------------------------------------------------------------------------
print()
print("R2  extend the lever arm (progress lines: this is the long leg)")
KS = (8, 12, 16, 20, 24, 28, 35, 44, 55, 70, 88)
_rows = []
_t0 = time.time()
print(f"    {'n':>7} {'k':>4} {'best l-k':>9} {'V_stair':>14} {'excess':>12} "
      f"{'exc/sqrt n':>12} {'exc/n^.25':>11} {'sec':>7}")
for k in KS:
    n = k * (k + 1) // 2
    t = time.time()
    hmin = H_min_closed(n)
    stair = [2 * k - 1 - 2 * i for i in range(k)]
    v_st = V_of(stair, n, hmin)
    v_best, bl = best_over_l(n, k)
    e = v_best - v_st
    sn = mp.sqrt(n)
    q4 = mp.mpf(n) ** mp.mpf("0.25")
    _rows.append({"k": k, "n": n, "l": bl, "V_stair": v_st, "V_best": v_best, "excess": e,
                  "e_over_sqrtn": e / sn, "e_over_n25": e / q4, "sec": time.time() - t})
    print(f"    {n:7d} {k:4d} {bl - k:9d} {mp.nstr(v_st, 10):>14} {mp.nstr(e, 8):>12} "
          f"{mp.nstr(e / sn, 7):>12} {mp.nstr(e / q4, 7):>11} {time.time() - t:7.1f}",
          flush=True)
print(f"    total {time.time() - _t0:.1f} s")

check(
    "R2 the excess is positive at every n (the staircase is never optimal beyond k = 8)",
    all(r["excess"] > 0 for r in _rows[1:]),
    f"{sum(1 for r in _rows if r['excess'] > 0)}/{len(_rows)} positive — #7286's finding "
    f"holds over the wider range",
)

# --------------------------------------------------------------------------------------------
# R3 — the exponent
# --------------------------------------------------------------------------------------------
print()
print("R3  the exponent alpha in excess ~ n^alpha, by successive log-log slopes")
print(f"    {'n_i -> n_{i+1}':>18} {'alpha':>10}")
_slopes = []
for a, b in zip(_rows, _rows[1:]):
    if a["excess"] <= 0 or b["excess"] <= 0:
        continue
    al = mp.log(b["excess"] / a["excess"]) / mp.log(mp.mpf(b["n"]) / a["n"])
    _slopes.append((a["n"], b["n"], al))
    print(f"    {a['n']:7d} -> {b['n']:7d} {mp.nstr(al, 6):>10}")

_tail = [s[2] for s in _slopes[-3:]]
_alpha_tail = sum(_tail) / len(_tail)
# Two-point fit across the widest span in the top half.
_mid = _rows[len(_rows) // 2]
_top = _rows[-1]
_alpha_span = (mp.log(_top["excess"] / _mid["excess"])
               / mp.log(mp.mpf(_top["n"]) / _mid["n"]))
print(f"    mean of the last 3 slopes : alpha = {mp.nstr(_alpha_tail, 6)}")
print(f"    two-point n={_mid['n']} -> {_top['n']}: alpha = {mp.nstr(_alpha_span, 6)}")
print(f"    reference exponents: 1/2 = 0.5 (coefficient CHANGES), 1/4 = 0.25, 1/3 = 0.3333")

_sub = _alpha_tail < mp.mpf("0.45") and _alpha_span < mp.mpf("0.45")
check(
    "R3 the exponent is measured and reported whichever way it came out",
    True,
    f"tail-slope alpha = {mp.nstr(_alpha_tail, 5)}, span-fit alpha = "
    f"{mp.nstr(_alpha_span, 5)}; "
    + ("BOTH below 0.45, i.e. sub-sqrt" if _sub else "NOT both below 0.45"),
)

# --------------------------------------------------------------------------------------------
# R4 — the verdict
# --------------------------------------------------------------------------------------------
print()
print("R4  what this does to #7286's verdict")
_ratio = [r["e_over_sqrtn"] for r in _rows]
_falling = _ratio[-1] < max(_ratio)
print(f"    excess/sqrt n peaks at n = {_rows[_ratio.index(max(_ratio))]['n']} "
      f"and ends at {mp.nstr(_ratio[-1], 6)} (peak {mp.nstr(max(_ratio), 6)})")
check(
    "R4 excess/sqrt n is falling at the top of the range",
    _falling,
    f"end {mp.nstr(_ratio[-1], 5)} vs peak {mp.nstr(max(_ratio), 5)} — a Theta(sqrt n) excess "
    f"would have this ratio approach a positive constant from below, not turn over",
)

print()
_n_ok = sum(1 for _, ok, _ in CHECKS if ok)
print(f"=== {_n_ok}/{len(CHECKS)} checks pass ===")
print()
print("VERDICT")
if _sub and _falling:
    print("  #7286's verdict -- 'A*sqrt2 is the staircase's rate, not the optimum's, and the")
    print("  coefficient is strictly above it' -- is WITHDRAWN, and it was mine. The excess is")
    print("  real and positive at every n (R2 confirms #7286's finding), but it grows")
    print("  SUB-sqrt: alpha ~ " + mp.nstr(_alpha_tail, 4) + " against the 0.5 that a")
    print("  coefficient change requires. A sub-sqrt excess is a SUBLEADING term. Combined")
    print("  with #7286's rigidity (l = sqrt(2n)(1+o(1))), that gives")
    print()
    print("      M_n = A*sqrt(2n) + o(sqrt n)   ==>   lim M_n / sqrt n = A*sqrt2 .")
    print()
    print("  So the coefficient is IDENTIFIED as A*sqrt2 = " + mp.nstr(A_CONST * mp.sqrt(2), 10))
    print("  and the bracket [A*sqrt2, C*sqrt2] collapses to its lower end. What stays open is")
    print("  the SUBLEADING term -- the exponent itself, and its constant.")
else:
    print("  The exponent did NOT come out sub-sqrt on this range, so #7286's verdict stands:")
    print("  the coefficient is strictly above A*sqrt2. Report the measured alpha.")
print()
print("  THE ONE-SIDEDNESS, stated rather than buried. The search is a heuristic: a value")
print("  found is a true lower bound on M_n; a value missed proves nothing. An")
print("  UNDER-performing search at large n depresses the measured excess and so biases")
print("  alpha DOWNWARD -- toward exactly the conclusion above. What would overturn it is a")
print("  better search at the top of the range finding excesses large enough to restore")
print("  alpha = 1/2. R1 is the guard that the evaluator is not the weak link (it reproduces")
print("  #7286's independent search exactly); it is not a guard on search QUALITY at n the")
print("  earlier probes never reached.")
print()
print("  NOT established either way: a pair-term LOWER bound. That is still the open item, and")
print("  it is what would turn this measurement into a proof.")

_out = {
    "schema": "qou-witness/v1",
    "computedAt": datetime.now(timezone.utc).isoformat(),
    "computation": os.path.basename(__file__),
    "bean": "qou-hok7",
    "anchor": "physical_proton",
    # Canonical anchor key read by the q0 audits/ratchet (the "anchor" key
    # above is a near-miss spelling they cannot see).
    "q0Anchor": "proton",
    "q0Value": Q_50_DIGIT_STR,
    "description": (
        "Measures the exponent alpha in excess ~ n^alpha for the best-found shape over the "
        "staircase. If alpha < 1/2 the excess is subleading and the Theta(sqrt n) coefficient "
        "is A*sqrt2 exactly, withdrawing #7286's 'strictly above' verdict."
    ),
    "constants": {
        "A": mp.nstr(A_CONST, 30),
        "C": mp.nstr(C_CONST, 30),
        "E_2": mp.nstr(E2_CONST, 30),
        "A_sqrt2": mp.nstr(A_CONST * mp.sqrt(2), 30),
        "ln_q0": mp.nstr(LNQ, 30),
    },
    "calibration_R1": [
        {"n": n, "excess": mp.nstr(e, 16), "ref_7286": str(r), "agree": ok}
        for (n, e, r, ok) in _cal
    ],
    "scaling_R2": [
        {"k": r["k"], "n": r["n"], "best_l": r["l"], "V_staircase": mp.nstr(r["V_stair"], 20),
         "V_best": mp.nstr(r["V_best"], 20), "excess": mp.nstr(r["excess"], 20),
         "excess_over_sqrt_n": mp.nstr(r["e_over_sqrtn"], 16),
         "excess_over_n_quarter": mp.nstr(r["e_over_n25"], 16),
         "elapsed_sec": round(r["sec"], 2)}
        for r in _rows
    ],
    "exponent_R3": {
        "successive_slopes": [
            {"n_from": a, "n_to": b, "alpha": mp.nstr(al, 12)} for (a, b, al) in _slopes
        ],
        "alpha_tail_mean_of_3": mp.nstr(_alpha_tail, 16),
        "alpha_two_point_span": mp.nstr(_alpha_span, 16),
        "sub_sqrt": bool(_sub),
    },
    "checks": [{"name": n, "ok": ok, "detail": d} for (n, ok, d) in CHECKS],
    "verdict": (
        ("Excess grows SUB-sqrt (alpha ~ " + mp.nstr(_alpha_tail, 4) + "), so it is subleading "
         "and the coefficient is A*sqrt2 exactly; #7286's 'strictly above A*sqrt2' is "
         "WITHDRAWN. One-sided: a weak search at large n biases alpha down, toward this "
         "conclusion.")
        if (_sub and _falling) else
        ("Excess did not come out sub-sqrt on this range (alpha ~ " + mp.nstr(_alpha_tail, 4)
         + "); #7286's verdict stands.")
    ),
}
_path = os.path.join(_HERE, "rev-excess-scaling-exponent.witness.json")
with open(_path, "w", encoding="utf-8") as fh:
    json.dump(_out, fh, indent=2)
    fh.write("\n")
print()
print(f"witness -> {_path}")

sys.exit(0 if _n_ok == len(CHECKS) else 1)
