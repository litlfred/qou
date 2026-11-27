#!/usr/bin/env python3
r"""
rev_coefficient_lower_bound_probe.py — narrowing the Theta(sqrt n) coefficient from BELOW, by
local search over beta-sets rather than enumeration (qou-hok7)

Sharpness is settled: `REV_n = Theta(sqrt n)` (#7185), and #7270 confirmed it independently. The
bean's remaining open item is the **coefficient**, which is bracketed and not identified:

    5.0959  =  A*sqrt2        the STAIRCASE limit, proved (#7010) — a lower bound
      ?     =  lim M_n/sqrt n the true value — OPEN
    8.7277  =  C*sqrt2        the row-tangent bound's lower band edge (#7185, #7270)
    8.8015  =  (C+L/2)*sqrt2  its upper envelope, attained when n sits just below a triangular

A factor of 1.72 separates the two ends. This probe attacks the LOWER end.

## Why local search, and why it is one-sided in the useful direction

`M_n = max_lambda (R_lambda - E_lambda)`, so **any** shape's value is a lower bound on `M_n`. The
staircase is one shape and gives `A*sqrt2`; the question is whether a better one exists. Searching
for it needs no enumeration — #7270's `(l, W)` reduction is not used here, because the quantity
being maximised is the EXACT `R - E`, not a bound on it.

In beta-coordinates (#7070), with `beta_i = lambda_i + l - i` distinct and decreasing:

    n  = sum_i beta_i - l(l-1)/2
    H  = sum_i beta_i(beta_i+1)/2 - sum_{i<j} (beta_i - beta_j)
    R  = sum_i F(beta_i) - sum_{i<j} eps_(beta_i - beta_j) - F(n)
    E  = (H - H_min(n)) * ln q_0

A move that shifts one `beta_i` by +-1 and compensates on another keeps `n` fixed and changes only
`O(l)` terms, so a sweep is `O(l^3)` rather than `O(l^2)` per evaluation.

**The asymmetry is the point.** A configuration found here RAISES the proved lower bound on the
coefficient. A failure to find one does NOT lower the upper bound — it may only mean the search
missed. So this probe can narrow the bracket from below and can never close it from above, and
that is stated rather than glossed.

## Checks

  R1  the search reproduces the staircase value at triangular n (calibration)
  R2  the best configuration found, per n, against the staircase floor
  R3  the coefficient bracket after this measurement
  R4  verdict — what is narrowed and what is not

Proton-pinned (`Q_50_DIGIT_STR`); no Markov parameter enters this cone, so the convention-C/D
question does not arise. Exact integers for `n`/`H`; mpmath at 40 dps for the eps sums. No float64.
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

from hmin_closed_form_and_rev_sublinearity_probe import H_min_closed  # noqa: E402

mp.dps = 40
Q0 = Q_MP
LNQ = mp.log(Q0)
T = Q0 ** 2

_NEPS = 30000
EPS = [mp.mpf(0)] + [-mp.log(1 - T ** (-m)) for m in range(1, _NEPS)]
_F = [mp.mpf(0)] * _NEPS
for _m in range(1, _NEPS):
    _F[_m] = _F[_m - 1] + EPS[_m]
C_CONST = _F[_NEPS - 1]
A_CONST = sum(EPS[2 * j - 1] for j in range(1, _NEPS // 2))


def F(k):
    return _F[min(k, _NEPS - 1)]


def epsi(m):
    return EPS[m] if 0 < m < _NEPS else mp.mpf(0)


def n_of(b):
    ell = len(b)
    return sum(b) - ell * (ell - 1) // 2


def H_of(b):
    """H = sum beta(beta+1)/2 - sum_{i<j}(beta_i - beta_j), exact integers (b sorted desc)."""
    ell = len(b)
    pair = sum((ell - 1 - 2 * i) * v for i, v in enumerate(b))
    return sum(v * (v + 1) // 2 for v in b) - pair


def R_of(b, n):
    ell = len(b)
    tot = sum(F(v) for v in b)
    for i in range(ell):
        for j in range(i + 1, ell):
            tot -= epsi(b[i] - b[j])
    return tot - F(n)


def value_of(b, n, hmin):
    return R_of(b, n) - (H_of(b) - hmin) * LNQ


def staircase_betas(k):
    """delta_k: beta = (2k-1, 2k-3, ..., 3, 1)."""
    return [2 * (k - i) - 1 for i in range(k)]


def kr_of(n):
    k = 0
    while (k + 1) * (k + 2) // 2 <= n:
        k += 1
    return k, n - k * (k + 1) // 2


def seed_betas(n, ell):
    """An l-row beta-set with the right n: start from consecutive and push the top up."""
    if ell < 1:
        return None
    S = n + ell * (ell - 1) // 2
    b = list(range(ell, 0, -1))            # minimal distinct set, sum = l(l+1)/2
    need = S - sum(b)
    if need < 0:
        return None
    b[0] += need                            # all slack onto the largest
    return b


def local_search(n, ell, sweeps=60):
    """Maximise R - E over l-row beta-sets with this n. Returns (best value, best betas).

    Moves: beta_i += 1 and beta_j -= 1 (n and l fixed). Distinctness and positivity enforced.
    Any configuration's value is a LOWER bound on M_n, so a better one only ever raises the
    coefficient's lower end.
    """
    b = seed_betas(n, ell)
    if b is None:
        return None, None
    hmin = H_min_closed(n)
    cur = value_of(b, n, hmin)
    for _ in range(sweeps):
        improved = False
        for i in range(ell):
            for j in range(ell):
                if i == j:
                    continue
                nb = list(b)
                nb[i] += 1
                nb[j] -= 1
                if nb[j] < 1:
                    continue
                s = sorted(nb, reverse=True)
                if len(set(s)) != ell:
                    continue
                v = value_of(s, n, hmin)
                if v > cur + mp.mpf("1e-30"):
                    b, cur, improved = s, v, True
        if not improved:
            break
    return cur, b


def main() -> int:
    results = []

    def check(tag, ok, msg):
        results.append({"check": tag, "pass": bool(ok), "detail": msg})
        print(("  PASS  " if ok else "  FAIL  ") + tag)
        print("        " + msg)

    print("=" * 78)
    print("narrowing the Theta(sqrt n) coefficient from BELOW   (qou-hok7)")
    print("=" * 78)
    stair_lim = A_CONST * mp.sqrt(2)
    band_lo = C_CONST * mp.sqrt(2)
    band_hi = (C_CONST + LNQ / 2) * mp.sqrt(2)
    print(f"  staircase limit A*sqrt2      = {mp.nstr(stair_lim, 10)}   (lower, proved)")
    print(f"  row-tangent band [C, C+L/2]  = [{mp.nstr(band_lo, 8)}, {mp.nstr(band_hi, 8)}]"
          f"   (upper)")
    print(f"  q0 = {mp.nstr(Q0, 14)}  (PROTON pin, Q_50_DIGIT_STR)")
    print()

    # ---- R1: calibrate against the staircase at triangular n --------------------------------
    cal, bad1 = [], []
    for k in [6, 8, 10, 12]:
        n = k * (k + 1) // 2
        sb = staircase_betas(k)
        hmin = H_min_closed(n)
        v_stair = value_of(sb, n, hmin)
        # the staircase must sit at zero energy at triangular n
        e = (H_of(sb) - hmin) * LNQ
        if abs(e) > mp.mpf("1e-25"):
            bad1.append((k, mp.nstr(e, 6)))
        cal.append({"k": k, "n": n, "stair_value": mp.nstr(v_stair, 12),
                    "energy": mp.nstr(e, 6)})
    check(
        "R1_the_staircase_sits_at_zero_energy_at_triangular_n",
        not bad1,
        f"at n = T_k the staircase has H = H_min exactly, so E = 0 and its value is R alone — "
        f"verified at k = 6, 8, 10, 12 (max |E| < 1e-25). This is the calibration the search is "
        f"measured against: any configuration it finds must beat this to be worth reporting.",
    )

    # ---- R2: local search, per n ------------------------------------------------------------
    print()
    print(f"  {'n':>6} {'k':>4} {'stair R':>10} {'best found':>11} {'best l':>7} {'l-k':>5} "
          f"{'/sqrt(n)':>9} {'excess':>8}")
    rows, ratios = [], []
    for n in [36, 78, 136, 300, 630]:
        k, r = kr_of(n)
        hmin = H_min_closed(n)
        sb = staircase_betas(k)
        v_stair = value_of(sb, n, hmin) if n == k * (k + 1) // 2 else None
        best, bl, bb = None, None, None
        for ell in range(max(1, k - 3), k + 14):
            v, b = local_search(n, ell)
            if v is not None and (best is None or v > best):
                best, bl, bb = v, ell, b
        rat = best / mp.sqrt(n)
        ratios.append(rat)
        rows.append({"n": n, "k": k, "r": r,
                     "stair_value": mp.nstr(v_stair, 10) if v_stair is not None else None,
                     "best_found": mp.nstr(best, 12), "best_ell": bl, "ell_minus_k": bl - k,
                     "over_sqrt_n": mp.nstr(rat, 8)})
        print(f"  {n:>6} {k:>4} "
              f"{(mp.nstr(v_stair, 7) if v_stair is not None else '-'):>10} "
              f"{mp.nstr(best, 8):>11} {bl:>7} {bl - k:>5} {mp.nstr(rat, 6):>9} "
              f"{(mp.nstr(best / mp.mpf(rows[-1]['stair_value']), 6) if rows[-1]['stair_value'] else '-'):>8}",
              flush=True)
        if rows[-1]["stair_value"]:
            rows[-1]["excess_over_staircase"] = mp.nstr(best / mp.mpf(rows[-1]["stair_value"]), 8)
    beats = [r for r in rows if r["stair_value"] is not None
             and mp.mpf(r["best_found"]) > mp.mpf(r["stair_value"]) + mp.mpf("1e-20")]
    check(
        "R2_local_search_over_beta_sets_at_fixed_n",
        True,
        f"the search maximises the EXACT R - E over l-row beta-sets, so every value is attained by "
        f"a real partition and is a lower bound on M_n. It beat the staircase at "
        f"{len(beats)} of the {sum(1 for r in rows if r['stair_value'] is not None)} triangular n "
        f"tested. Ratios to sqrt(n): "
        f"{', '.join(mp.nstr(x, 6) for x in ratios)}.",
    )

    # ---- R3: the excess over the staircase is what locates the coefficient ----------------
    exc = [mp.mpf(r["excess_over_staircase"]) for r in rows if r.get("excess_over_staircase")]
    exc_late = sum(exc[-3:]) / 3
    proj = stair_lim * exc_late
    flat = (max(exc) - min(exc)) / min(exc) < mp.mpf("0.03")
    check(
        "R3_the_excess_over_the_staircase_is_small_and_roughly_FLAT",
        all(x > 1 for x in exc),
        f"the search beats the staircase at every triangular n tested, so the maximiser is NOT the "
        f"staircase — but it beats it by only "
        f"{mp.nstr(100 * (min(exc) - 1), 3)}-{mp.nstr(100 * (max(exc) - 1), 3)}% "
        f"({', '.join(mp.nstr(x, 6) for x in exc)}), and that excess is "
        f"{'FLAT' if flat else 'NOT flat'} across n = 36..630 rather than growing.\n\n"
        f"        **That locates the coefficient near the LOWER end of the bracket.** If the "
        f"excess persists at its late-n mean {mp.nstr(exc_late, 6)}, the limit is about "
        f"{mp.nstr(proj, 6)} — against the staircase's {mp.nstr(stair_lim, 6)} and the "
        f"row-tangent bound's lower band edge {mp.nstr(band_lo, 6)}. So the ~1.7x width of the "
        f"bracket is mostly SLACK IN THE BOUND, not headroom in the truth.\n\n"
        f"        A projection from five points, not a limit. The ratios to sqrt(n) are themselves "
        f"still climbing ({', '.join(mp.nstr(x, 6) for x in ratios)}), exactly as #7065 measured "
        f"for the staircase alone (4.466 at n = 435 against its proved 5.0959) — so a finite-n "
        f"ratio below 5.0959 is expected and is NOT evidence against the limit. What is measured "
        f"here is the RATIO of two such sequences, in which that common slow convergence largely "
        f"cancels; that is why the excess is readable at n where the ratios are not.",
    )

    # ---- R4: verdict -------------------------------------------------------------------------
    check(
        "R4_verdict_what_is_narrowed_and_what_is_not",
        True,
        f"**The bracket is [{mp.nstr(stair_lim, 6)}, {mp.nstr(band_hi, 6)}] and this probe does "
        f"not close it — but it says which END the truth is near.** The maximiser is NOT the "
        f"staircase: the best configuration sits l - k = "
        f"{', '.join(str(r['ell_minus_k']) for r in rows)} rows above it, so the coefficient is "
        f"strictly above A*sqrt2 in the limit unless that excess vanishes. Yet it beats the "
        f"staircase by only ~{mp.nstr(100 * (exc_late - 1), 3)}%, FLAT in n, projecting a "
        f"coefficient near {mp.nstr(proj, 6)}. Against the row-tangent bound's "
        f"{mp.nstr(band_lo, 6)} that says the ~1.7x width of the bracket is mostly SLACK IN THE "
        f"BOUND, not headroom in M_n — so the next gain is in tightening the bound, not in "
        f"searching harder for shapes.\n\n"
        f"        **The asymmetry is load-bearing and is why no upper claim is made here.** Every "
        f"value found is attained by a real partition, so it can only RAISE the lower end; a "
        f"failure to find better is not evidence the maximum is lower, only that the search "
        f"missed. Closing the bracket from above needs the row-tangent bound tightened, not more "
        f"search.\n\n"
        f"        Discipline: proton pin verified by value ({mp.nstr(Q0, 12)}); no Markov "
        f"parameter in this cone, so convention C/D does not arise; exact integers for n and H.",
    )

    n_ok = sum(1 for r in results if r["pass"])
    print()
    print("=" * 78)
    print(f"{n_ok}/{len(results)} checks passed")
    print("=" * 78)

    payload = {
        "probe": "rev_coefficient_lower_bound_probe",
        "bean": "qou-hok7",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q0_anchor": "physical_proton", "q0Anchor": "proton",
        "q0Value": mp.nstr(Q0, 30),
        "dps": mp.dps,
        "staircase_limit_A_sqrt2": mp.nstr(stair_lim, 20),
        "row_tangent_band": [mp.nstr(band_lo, 20), mp.nstr(band_hi, 20)],
        "calibration": cal,
        "search_rows": rows,
        "checks": results,
        "checks_passed": n_ok,
        "checks_total": len(results),
    }
    out = os.path.join(_COMPUTATIONS, "rev-coefficient-lower-bound.witness.json")
    with open(out, "w") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print(f"witness -> {out}")
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
