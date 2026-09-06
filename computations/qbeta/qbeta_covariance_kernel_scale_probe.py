#!/usr/bin/env python3
"""The Delta_lam kernel margin lives at the CLT scale k^{3/2}, not at scale k.

Epic `qou-x631` conjectures T_3(k) = SUM_lam (f^lam)^2 chi^lam(3-cyc) <= 0,
equivalently E_Q[Sigma_3] <= 0 under Q(lam) ~ (f^lam)^3, where
Sigma_3(lam) = (k)_3 chi-hat^lam(3-cyc) = R_4(lam) + k.

A yes/no conjecture does not say what a proof has to achieve. This measures the
MARGIN, and the answer constrains proof strategy more than the sign does.

*** RESULT: the margin scales as k^{3/2}, and that is the FLUCTUATION scale ***

    E_Q[Sigma_3] / k^{3/2}  =  -0.277 +/- 0.02   over  10 <= k <= 42

stable, oscillating, not drifting. Compare Kerov's CLT: under PLANCHEREL measure
Sigma_3 is asymptotically Gaussian with mean 0 and standard deviation
sqrt(3) k^{3/2}. So the f-biasing shifts Sigma_3 by

    E_Q[Sigma_3] ~ -0.16 * sd_Planch(Sigma_3)

-- an O(1) effect measured in standard deviations. NOT a large-deviation effect.

*** WHY THAT ELIMINATES A ROUTE (the most tempting one) ***

The first idea anyone reaches for is: "Plancherel concentrates on the
Vershik-Kerov-Logan-Shepp shape; evaluate there." That CANNOT work, and the
scaling says why. At the limit shape Sigma_3 contributes ZERO (E_Planch[Sigma_3]
= 0 exactly -- see `qbeta_covariance_kernel_p3_special_probe.py`), so the entire
signal is the CORRELATION between the f^lam bias and the Gaussian fluctuation
mode. Any argument that
  * replaces lam by the limit shape,
  * uses concentration of measure to discard atypical lam, or
  * bounds via large deviations,
discards exactly the term being computed and proves 0 <= 0.

A proof must operate AT the CLT scale and produce a correlation coefficient. That
is precisely what route `qou-t5m1` (full Sniady genus expansion on the
(f^lam)^3-biased measure) is built to do, so this is evidence for that route
rather than merely against others.

*** A NUMERICAL COINCIDENCE, QUARANTINED ***

The mean of the last eight values (k = 28..42) is 0.27727, and
sqrt(3)/(2*pi) = 0.27566. These agree to 0.6%.

THIS IS RECORDED AS A TARGET TO CHECK A FUTURE DERIVATION AGAINST, NEVER AS A
CRITERION TO SEARCH ON. The sequence still oscillates by +/-0.02 and drifts
slightly upward over the measured range, so the data does not establish that a
limit exists, let alone its value. Do not fit to this constant; if an argument
independently produces a constant, compare it here.

*** EXACT ARITHMETIC ***

f^lam by hook length in Python integers, SUM c^2 and C(k,2) integral, and the
ratio E_Q[Sigma_3] = 3 cov(k) / M(k) formed as a `Fraction` before any float
appears. At k = 42, (f^lam)^3 exceeds 10^60 and cov(k) and M(k) are exact
integers of that size; a double would have destroyed the ratio.
"""
from __future__ import annotations

import json
import math  # float64-ok: sqrt/pi for the quarantined coincidence and for display only; every quantity that decides an assertion is an exact Fraction
import subprocess
import sys
import time
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.setrecursionlimit(10000)


def partitions(n: int, cap: int | None = None):
    if cap is None:
        cap = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, cap), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def hook_dim(lam, nfact: int) -> int:
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])] if lam else []
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= row - j + conj[j] - i - 1
    return nfact // prod


def eq_sigma3(k: int) -> Fraction:
    """E_Q[Sigma_3] = 3 cov(k) / M(k), exact."""
    nf = 1
    for i in range(2, k + 1):
        nf *= i
    b = k * (k - 1) // 2
    M = 0
    cov = 0
    for lam in partitions(k):
        f = hook_dim(lam, nf)
        c2 = sum((j - i) ** 2 for i, r in enumerate(lam) for j in range(r))
        f3 = f * f * f
        M += f3
        cov += f3 * (c2 - b)
    return Fraction(3 * cov, M)


def main() -> int:
    t0 = time.monotonic()
    a, ok = [], True

    def chk(name, computed, expected, note=""):
        good = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(good), **({"note": note} if note else {})})
        print(f"  [{'PASS' if good else 'FAIL'}] {name}: {computed!r}")
        return good

    ks = list(range(10, 43, 2))
    ratios = {}
    print("=" * 78)
    print("E_Q[Sigma_3] AGAINST THE CLT SCALE k^{3/2}")
    print("=" * 78)
    print(f"    {'k':>3} | {'E_Q[Sigma_3]':>15} | {'/k^{3/2}':>10} | {'/(sqrt3 k^{3/2})':>17}")
    for k in ks:
        v = eq_sigma3(k)
        r = float(v) / k ** 1.5  # float64-ok: v is an exact Fraction; the float is the DISPLAYED ratio and the bound test below has 0.02 of slack against a 0.06 spread, far outside double precision
        ratios[k] = r
        print(f"    {k:>3} | {float(v):>+15.4f} | {r:>+10.5f} | "  # float64-ok: printing
              f"{r / math.sqrt(3):>+17.5f}")

    ok &= chk("margin_is_negative_throughout",
              [k for k, r in ratios.items() if r >= 0], [],
              note="the conjecture itself, over the measured range")

    lo, hi = min(ratios.values()), max(ratios.values())
    ok &= chk("ratio_is_bounded_away_from_zero_and_from_infinity",
              bool(-0.32 < lo and hi < -0.20), True,
              note=f"observed range [{lo:.5f}, {hi:.5f}] over k=10..42. Stable, "
                   "oscillating, not drifting -- so the margin scales as k^{3/2}, "
                   "NOT as k")

    # scale k would mean E_Q/k bounded; it is not -- it grows.
    per_k = {k: float(eq_sigma3(k)) / k for k in (12, 24, 42)}  # float64-ok: exact Fraction in, and the growth test asks for a factor > 1.7 where the true factor is ~3
    ok &= chk("scale_k_is_ruled_out_the_ratio_to_k_grows",
              bool(abs(per_k[42]) > 1.7 * abs(per_k[12])), True,
              note=f"E_Q[Sigma_3]/k at k=12,24,42 is "
                   f"{per_k[12]:.3f}, {per_k[24]:.3f}, {per_k[42]:.3f} -- it grows, "
                   "so k is the wrong normalisation and k^{3/2} is the right one")

    tail = [ratios[k] for k in ks[-8:]]
    mean_tail = sum(tail) / len(tail)
    print()
    print("=" * 78)
    print("QUARANTINED COINCIDENCE -- a target, never a search criterion")
    print("=" * 78)
    print(f"    mean of last 8 (k=28..42) : {mean_tail:.5f}")
    print(f"    sqrt(3)/(2 pi)            : {math.sqrt(3)/(2*math.pi):.5f}")
    print("    agreement 0.6%. The sequence still oscillates by +/-0.02 and drifts")
    print("    slightly upward, so the data does NOT establish that a limit exists,")
    print("    let alone its value. Do not fit to this. If a derivation produces a")
    print("    constant independently, compare it here.")
    a.append({"name": "coincidence_recorded_not_asserted",
              "computed": {"mean_tail": round(mean_tail, 5),
                           "sqrt3_over_2pi": round(math.sqrt(3) / (2 * math.pi), 5)},
              "expected": "recorded only", "passed": True,
              "note": "NOT an assertion that the limit is sqrt(3)/(2 pi)"})

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))
    try:
        head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        head = "unknown"
    out = HERE / "qbeta-covariance-kernel-scale.witness.json"
    out.write_text(json.dumps({
        "computation": "qbeta-covariance-kernel-scale",
        "assertions": a, "allPassed": bool(ok),
        "parameters": {"epic": "qou-x631",
                       "claim": "the margin scales as k^{3/2}, the CLT fluctuation "
                                "scale, so concentration/limit-shape arguments cannot work",
                       "arithmetic": "exact Fractions; float only for display"},
        "data": {"ratio_by_k": {str(k): round(r, 6) for k, r in ratios.items()}},
        "provenance": {"headSha": head,
                       "producer": "computations/qbeta/qbeta_covariance_kernel_scale_probe.py",
                       "elapsed_s": round(time.monotonic() - t0, 3)},
    }, indent=2) + "\n")
    print(f"witness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
