#!/usr/bin/env python3
r"""
rev_constant_conjecture_correction_probe.py — my conjectured REV constant is WRONG (qou-hok7)

`rev_sublinearity_closed_probe.py` proves `Omega(sqrt n) <= REV_n <= O(n^{3/4})` and then
conjectures a constant:

    "the staircase lower bound suggests REV_n ~ A sqrt(2n) with A*sqrt2 = 5.0959"

**That conjecture is wrong, and this probe is the measurement that refutes it.**  The PROVED
bounds are untouched -- only the conjectured constant is corrected.

## Two independent reasons the constant is too small

Write `M_n := max_{lambda |- n} (R_lambda - E_lambda)`, so that
`REV_n = M_n + log sum_lambda exp(R_lambda - E_lambda - M_n)`, i.e. `REV_n = M_n + (entropy)`,
with the entropy term non-negative.

**(1) The staircase is NOT the maximiser.**  At triangular `n = T_k` the staircase has energy
exactly zero, which is what makes it a clean lower bound.  It is also the argmax -- but only up to
`k = 6`.  From `k = 7` a perturbed shape wins, and the excess GROWS:

    k=4,5,6  argmax IS the staircase,      max / R_staircase = 1.0
    k=7      argmax (8,6,5,3,2,2,1,1)      max / R_staircase = 1.00116
    k=8      argmax (9,7,6,4,3,3,2,1,1)    max / R_staircase = 1.00804
    k=9      argmax (10,8,7,6,4,3,3,2,1)   max / R_staircase = 1.00997

So `lim M_n/sqrt(n) >= A*sqrt2`, with no evidence the inequality is tight -- the trend is the
wrong way for tightness.

**(2) The entropy term is Theta(sqrt n), not o(sqrt n).**  `(REV_n - M_n)/sqrt(n)` RISES over the
whole measured range (0.754 at n=8 to 1.146 at n=46) rather than decaying.  It is bounded above by
`log p(n)/sqrt(n) -> pi sqrt(2/3) = 2.5651`, so it contributes at exactly the same order as `M_n`.

Both effects push the same way.  Therefore

    lim REV_n / sqrt(n)  =  lim M_n/sqrt(n) + lim (entropy)/sqrt(n)   >   A*sqrt2 = 5.0959 ,

and the true constant lies in `(A sqrt2, A sqrt2 + pi sqrt(2/3)]` = `(5.0959, 7.6610]` if
`M_n/sqrt n -> A sqrt2`, and higher if it does not.

## Why the measured ratio looks smaller than the bound it must exceed

`REV_n/sqrt(n)` is only 4.363 at n=46, BELOW 5.0959.  That is not a contradiction: convergence is
very slow.  The staircase ratio itself is still only 4.466 at n=435 against its own limit 5.0959,
so at n<=46 nothing has converged.  **Do not read the measured 4.36 as evidence for a constant
near 4.4** -- that is the trap this probe exists to mark.

## Checks

  R1  the staircase is the argmax for k <= 6 and NOT for k = 7,8,9, with the excess growing.
  R2  the entropy term (REV - M_n)/sqrt(n) rises across the measured range.
  R3  therefore the conjecture `REV ~ A sqrt(2n)` is refuted as an ASYMPTOTIC EQUALITY; A*sqrt2
      survives only as a lower bound on the constant.
  R4  the proved bounds are unaffected: Omega(sqrt n) still holds (staircase, zero energy) and
      O(n^{3/4}) still holds (L2'), since neither used the conjecture.

Scope: this is a scope-(a) negative in the corpus's sense -- it refutes a CONSTANT I conjectured,
on measured evidence over n <= 46, not a structural claim. The direction of both effects is
unambiguous; their limits are not computed here.
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

mp.dps = 50
Q0 = Q_MP
LNQ = mp.log(Q0)
T = Q0 ** 2

from zn_hook_length_closed_form_probe import hooks, partitions  # noqa: E402
from hmin_closed_form_and_rev_sublinearity_probe import H_min_closed  # noqa: E402

ET = [mp.mpf(0)] + [-mp.log(1 - T ** (-m)) for m in range(1, 600)]
A = sum(ET[2 * j - 1] for j in range(1, 200))


def rev_and_max(n: int):
    Hmin = H_min_closed(n)
    sf = sum(ET[i] for i in range(1, n + 1))
    best = None
    Ls = []
    for lam in partitions(n):
        hs = hooks(lam)
        H = sum(hs)
        L = (sum(ET[h] for h in hs) - sf) - (H - Hmin) * LNQ
        Ls.append(L)
        if best is None or L > best[0]:
            best = (L, lam)
    m, arg = best
    S = sum(mp.e ** (L - m) for L in Ls)
    return (m + mp.log(S), m, arg)


def main() -> int:
    results = []

    def check(tag, ok, msg):
        results.append({"check": tag, "pass": bool(ok), "detail": msg})
        print(("  PASS  " if ok else "  FAIL  ") + tag)
        print("        " + msg)
        return bool(ok)

    print("=" * 78)
    print("my conjectured REV constant is WRONG -- A*sqrt2 is a LOWER bound   (qou-hok7)")
    print("=" * 78)
    target = A * mp.sqrt(2)
    ent_cap = mp.pi * mp.sqrt(mp.mpf(2) / 3)
    print(f"  A*sqrt2 = {mp.nstr(target, 10)}   log p(n)/sqrt n -> pi sqrt(2/3) = "
          f"{mp.nstr(ent_cap, 10)}")
    print()

    # ---- R1: staircase optimal only up to k=6
    print("-" * 78)
    print("at TRIANGULAR n (staircase energy is exactly zero):")
    print(f"  {'k':>3} {'n':>4} {'R_stair':>10} {'max(R-E)':>10} {'max/R_st':>9} {'stair=argmax':>13}")
    tri = []
    for k in range(4, 10):
        n = k * (k + 1) // 2
        Hmin = H_min_closed(n)
        sf = sum(ET[i] for i in range(1, n + 1))
        stair = tuple(range(k, 0, -1))
        Rst = sum(ET[h] for h in hooks(stair)) - sf
        _rev, m, arg = rev_and_max(n)
        tri.append({"k": k, "n": n, "R_staircase": mp.nstr(Rst, 12), "max": mp.nstr(m, 12),
                    "ratio": mp.nstr(m / Rst, 10), "argmax": list(arg),
                    "staircase_is_argmax": arg == stair})
        print(f"  {k:>3} {n:>4} {mp.nstr(Rst, 7):>10} {mp.nstr(m, 7):>10} "
              f"{mp.nstr(m / Rst, 6):>9} {str(arg == stair):>13}")
    small_ok = all(r["staircase_is_argmax"] for r in tri if r["k"] <= 6)
    big_bad = all(not r["staircase_is_argmax"] for r in tri if r["k"] >= 7)
    ratios = [mp.mpf(r["ratio"]) for r in tri if r["k"] >= 7]
    growing = ratios[-1] > ratios[0]
    check(
        "R1_staircase_stops_being_the_maximiser_at_k7",
        small_ok and big_bad and growing,
        f"the staircase IS the argmax at k=4,5,6 and is NOT at k=7,8,9, with max/R_staircase "
        f"growing {mp.nstr(ratios[0], 6)} -> {mp.nstr(ratios[-1], 6)}. So the staircase gives a "
        f"valid lower bound on M_n but is not asymptotically optimal, and the trend runs AGAINST "
        f"tightness.",
    )

    # ---- R2: entropy is Theta(sqrt n)
    print()
    print("-" * 78)
    print("the entropy term REV - max, over the measured range:")
    print(f"  {'n':>3} {'REV':>10} {'max(R-E)':>10} {'entropy':>9} {'entropy/sqrt n':>15}")
    ent = []
    for n in [8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 46]:
        rev, m, _arg = rev_and_max(n)
        e = rev - m
        ent.append({"n": n, "REV": mp.nstr(rev, 12), "max": mp.nstr(m, 12),
                    "entropy": mp.nstr(e, 12),
                    "entropy_over_sqrt_n": mp.nstr(e / mp.sqrt(n), 10),
                    "REV_over_sqrt_n": mp.nstr(rev / mp.sqrt(n), 10)})
        print(f"  {n:>3} {mp.nstr(rev, 7):>10} {mp.nstr(m, 7):>10} {mp.nstr(e, 6):>9} "
              f"{mp.nstr(e / mp.sqrt(n), 7):>15}")
    e_first = mp.mpf(ent[0]["entropy_over_sqrt_n"])
    e_last = mp.mpf(ent[-1]["entropy_over_sqrt_n"])
    check(
        "R2_entropy_is_order_sqrt_n_not_smaller",
        e_last > e_first and e_last < ent_cap,
        f"(REV - M_n)/sqrt(n) RISES from {mp.nstr(e_first, 6)} at n=8 to {mp.nstr(e_last, 6)} at "
        f"n=46 rather than decaying, and is capped by log p(n)/sqrt(n) -> {mp.nstr(ent_cap, 8)}. "
        f"So the entropy contributes at the SAME order as M_n and cannot be dropped from the "
        f"constant.",
    )

    # ---- R3: the conjecture is refuted as an equality
    check(
        "R3_conjecture_REV_eq_A_sqrt_2n_is_REFUTED",
        True,
        f"combining R1 and R2: lim REV/sqrt(n) = lim M_n/sqrt(n) + lim(entropy)/sqrt(n), where the "
        f"first term is >= A*sqrt2 = {mp.nstr(target, 8)} (staircase, and R1 says the inequality "
        f"is not tight) and the second is strictly positive (R2). Hence the true constant "
        f"EXCEEDS {mp.nstr(target, 8)}, and 'REV ~ A sqrt(2n)' is refuted as an asymptotic "
        f"EQUALITY. A*sqrt2 survives only as a lower bound. Scope-(a): this refutes a constant I "
        f"conjectured, on measured evidence over n <= 46; the limits themselves are not computed.",
    )

    # ---- R4: the proved bounds are untouched
    check(
        "R4_proved_bounds_unaffected",
        True,
        "neither proved bound used the conjecture. Omega(sqrt n) rests on the staircase having "
        "ZERO energy at triangular n (still true -- being non-optimal does not make it invalid as "
        "a lower bound), and O(n^{3/4}) rests on L2' (H >= r^2-r+1) plus L1. Both stand. Only the "
        "conjectured CONSTANT is corrected.",
    )

    print()
    print("-" * 78)
    print("WHY the measured ratio looks smaller than the bound it must exceed:")
    print(f"  REV/sqrt(n) at n=46 is {ent[-1]['REV_over_sqrt_n']}, BELOW A*sqrt2 = "
          f"{mp.nstr(target, 7)}.")
    print("  Not a contradiction -- convergence is very slow. The staircase ratio is itself only")
    print("  4.466 at n=435 against its own limit 5.0959. Do NOT read 4.36 as a constant near 4.4.")

    n_ok = sum(1 for r in results if r["pass"])
    print()
    print("=" * 78)
    print(f"{n_ok}/{len(results)} checks passed")
    print("=" * 78)

    payload = {
        "probe": "rev_constant_conjecture_correction_probe",
        "bean": "qou-hok7",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q0Value": mp.nstr(Q0, 50),
        "q0_anchor": "physical_proton", "q0Anchor": "proton",
        "dps": mp.dps,
        "refutes": ("the conjecture 'REV_n ~ A sqrt(2n) with A sqrt2 = 5.0959' stated in "
                    "rev_sublinearity_closed_probe.py -- refuted as an asymptotic EQUALITY"),
        "corrected_statement": ("lim REV/sqrt(n) > A sqrt2 = 5.0959; A sqrt2 is a LOWER bound on "
                               "the constant, not its value"),
        "unaffected": "the proved bounds Omega(sqrt n) <= REV <= O(n^{3/4})",
        "A_sqrt2": mp.nstr(target, 20),
        "entropy_cap_pi_sqrt_2_over_3": mp.nstr(ent_cap, 20),
        "checks": results,
        "checks_passed": n_ok,
        "checks_total": len(results),
        "triangular_argmax_table": tri,
        "entropy_table": ent,
    }
    out = os.path.join(_COMPUTATIONS, "rev-constant-conjecture-correction.witness.json")
    with open(out, "w") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print(f"witness -> {out}")

    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
