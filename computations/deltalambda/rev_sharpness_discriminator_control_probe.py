#!/usr/bin/env python3
r"""
rev_sharpness_discriminator_control_probe.py — the sharpness question CANNOT be settled by
enumeration, and the reason is a control (qou-hok7)

`qou-hok7` has `Omega(sqrt n) <= REV_n <= O(n^{3/4})` both proved (#7014, #7018). Whether the
`3/4` is SHARP is the open piece. The obvious empirical attack is to scan
`M_n = max_lambda (R_lambda - E_lambda)` at larger `n` and see which of `M/sqrt(n)` or `M/n^{3/4}`
goes flat.

**That attack does not work, and this probe is the control that shows why.**

## The tempting reading

Scanning to `n = 76` (`rev_max_large_n_scan.py`) gives

    n            40        44        68        76
    M/sqrt(n)   3.123     3.188     3.590     3.686      RISING, +18%
    M/n^{3/4}   1.242     1.238     1.250     1.248      FLAT to ~1%

A flat `n^{3/4}` column against a rising `sqrt(n)` column reads as evidence that `M_n` really is
`Theta(n^{3/4})`, i.e. that the proved upper bound is sharp. **Do not draw that conclusion.**

## The control

Run the same two columns on the STAIRCASE, whose rate is not in question: it is provably
`Theta(sqrt n)` with limit `A*sqrt2 = 5.0959` (proved in #7010 — zero energy at triangular `n`,
`R_{delta_k} -> A*k`). If the discriminator worked, the staircase's `n^{3/4}` column would fall
visibly over the same range.

It does not. `R_staircase / n^{3/4}` RISES to a peak near `n = 55` and only then falls:

    n           36     45     55     78    105    153    276    435   1830
    R/n^{3/4}  1.200  1.219  1.225  1.216  1.192  1.147  1.056  0.978  0.732

Over `n = 36..78` it is flat at ~1.20-1.23 — the same range the `M_n` scan covers, at the same
value. So a provably `sqrt(n)` object is INDISTINGUISHABLE from an `n^{3/4}` one on this
statistic over exactly the reachable range, because that range straddles its peak.

The `sqrt(n)` column tells the same story from the other side: the staircase's own
`R/sqrt(n)` is still only `4.466` at `n = 435` against its limit `5.096`, i.e. **12% short after
ten times the reachable `n`**. A rising `M/sqrt(n)` is therefore exactly what a `Theta(sqrt n)`
object looks like here.

## What it would take

The staircase control only becomes decisive where its `n^{3/4}` ratio has fallen clearly below its
peak — past `n ~ 150`. A full enumeration of `M_n` needs every partition of `n`:

    p(76)  =      9,289,091      reached, ~15 min
    p(84)  =     26,543,660      reached, ~50 min
    p(150) = 40,853,235,313      1,539x p(84)

So the enumeration route is not merely expensive at the deciding scale, it is out by about three
orders of magnitude. At the ~9,000 shapes/second this container sustains, `p(150)` alone is roughly
**52 days** of scanning. **The sharpness question is closed to enumeration and must be settled
structurally**, or by a scan that does not enumerate every shape (a max over a provably sufficient
sub-family, which is itself a structural result).

## Checks

  R1  the staircase `n^{3/4}` ratio is NOT monotone — it rises, peaks near n=55, then falls
  R2  over the scanned range n=36..78 the staircase ratio is flat within 3%, matching what the
      `M_n` scan shows, so the statistic does not discriminate there
  R3  the staircase `sqrt(n)` ratio is still >10% short of its own proved limit at n=435
  R4  p(150)/p(84) exceeds 1000, quantifying the infeasibility

Exact integer partition counts; mpmath at 40 dps for the ratios. No float64.
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

mp.dps = 40
Q0 = Q_MP
T = Q0 ** 2

from zn_hook_length_closed_form_probe import hooks  # noqa: E402

ET = [mp.mpf(0)] + [-mp.log(1 - T ** (-m)) for m in range(1, 4000)]
A = sum(ET[2 * j - 1] for j in range(1, 500))


def p(n: int) -> int:
    """Exact partition count."""
    tab = [1] + [0] * n
    for k in range(1, n + 1):
        for m in range(k, n + 1):
            tab[m] += tab[m - k]
    return tab[n]


def staircase_R(k: int):
    n = k * (k + 1) // 2
    return n, sum(ET[h] for h in hooks(tuple(range(k, 0, -1)))) - sum(ET[i] for i in range(1, n + 1))


def main() -> int:
    results = []

    def check(tag, ok, msg):
        results.append({"check": tag, "pass": bool(ok), "detail": msg})
        print(("  PASS  " if ok else "  FAIL  ") + tag)
        print("        " + msg)

    print("=" * 78)
    print("the sharpness discriminator does NOT discriminate at reachable n   (qou-hok7)")
    print("=" * 78)
    target = A * mp.sqrt(2)
    print(f"  staircase limit A*sqrt2 = {mp.nstr(target, 10)}   (proved, #7010)")
    print()

    rows = []
    print(f"  {'k':>3} {'n':>5} {'R_stair':>11} {'R/sqrt n':>10} {'R/n^0.75':>10}")
    for k in [8, 9, 10, 12, 14, 17, 23, 29, 40, 60]:
        n, R = staircase_R(k)
        r34 = R / (mp.mpf(n) ** mp.mpf("0.75"))
        rs = R / mp.sqrt(n)
        rows.append({"k": k, "n": n, "R": mp.nstr(R, 12),
                     "R_over_sqrt_n": mp.nstr(rs, 10), "R_over_n34": mp.nstr(r34, 10)})
        print(f"  {k:>3} {n:>5} {mp.nstr(R, 8):>11} {mp.nstr(rs, 7):>10} {mp.nstr(r34, 7):>10}")

    v = [mp.mpf(r["R_over_n34"]) for r in rows]
    ns = [r["n"] for r in rows]
    peak_i = max(range(len(v)), key=lambda i: v[i])
    check(
        "R1_staircase_n34_ratio_is_not_monotone",
        0 < peak_i < len(v) - 1,
        f"R/n^(3/4) for the staircase RISES to a peak at n={ns[peak_i]} "
        f"({mp.nstr(v[peak_i], 7)}) and falls afterwards to {mp.nstr(v[-1], 7)} at n={ns[-1]}. "
        f"So this statistic is not monotone for a Theta(sqrt n) object, and a flat reading near "
        f"the peak carries no information about the rate.",
    )

    window = [(n, x) for n, x in zip(ns, v) if 36 <= n <= 78]
    spread = (max(x for _n, x in window) - min(x for _n, x in window)) / max(x for _n, x in window)
    check(
        "R2_flat_over_the_scanned_range_so_it_cannot_discriminate",
        spread < mp.mpf("0.03"),
        f"over n=36..78 the staircase R/n^(3/4) varies by only "
        f"{mp.nstr(100 * spread, 3)}% ({', '.join(mp.nstr(x, 6) for _n, x in window)}). The M_n "
        f"scan covers n=40..76 and shows the same flatness at the same value (~1.24). A provably "
        f"Theta(sqrt n) object is therefore INDISTINGUISHABLE from Theta(n^(3/4)) on this "
        f"statistic over exactly the reachable range.",
    )

    r435 = next(mp.mpf(r["R_over_sqrt_n"]) for r in rows if r["n"] == 435)
    shortfall = (target - r435) / target
    check(
        "R3_sqrt_n_ratio_still_far_from_its_own_proved_limit",
        shortfall > mp.mpf("0.10"),
        f"the staircase's R/sqrt(n) is {mp.nstr(r435, 8)} at n=435, still "
        f"{mp.nstr(100 * shortfall, 4)}% short of its PROVED limit {mp.nstr(target, 8)} — at ten "
        f"times the largest enumerable n. So a rising M/sqrt(n) is exactly what a Theta(sqrt n) "
        f"object looks like here and is not evidence against it.",
    )

    p84, p150 = p(84), p(150)
    ratio = p150 // p84
    check(
        "R4_enumeration_is_out_by_orders_of_magnitude_at_the_deciding_scale",
        ratio > 1000,
        f"the control only becomes decisive past n ~ 150, where the staircase ratio has clearly "
        f"left its peak. p(84) = {p84:,} (reached, ~50 min); p(150) = {p150:,} — a factor of "
        f"{ratio:,}, about three orders of magnitude. Enumeration is out of reach at the scale that "
        f"would decide the question.",
    )

    n_ok = sum(1 for r in results if r["pass"])
    print()
    print("=" * 78)
    print(f"{n_ok}/{len(results)} checks passed")
    print("CONCLUSION: sharpness is CLOSED TO ENUMERATION. It must be settled structurally, or by")
    print("a scan over a provably sufficient sub-family — which is itself a structural result.")
    print("=" * 78)

    payload = {
        "probe": "rev_sharpness_discriminator_control_probe",
        "bean": "qou-hok7",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q0_anchor": "physical_proton", "q0Anchor": "proton",
        "dps": mp.dps,
        "conclusion": ("the M/n^{3/4}-vs-M/sqrt(n) discriminator does not discriminate at "
                       "reachable n; a provably Theta(sqrt n) control shows the same flatness "
                       "over the same range. Sharpness is closed to enumeration."),
        "staircase_limit_A_sqrt2": mp.nstr(target, 20),
        "checks": results,
        "checks_passed": n_ok,
        "checks_total": len(results),
        "staircase_control": rows,
        "p_84": p84,
        "p_150": p150,
    }
    out = os.path.join(_COMPUTATIONS, "rev-sharpness-discriminator-control.witness.json")
    with open(out, "w") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print(f"witness -> {out}")
    return 0 if n_ok == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
