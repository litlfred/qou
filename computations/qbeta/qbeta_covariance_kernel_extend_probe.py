#!/usr/bin/env python3
"""Extend the numerical check of cov(k) <= 0 past the recorded k <= 40.

Epic `qou-x631` conjectures

    cov(k) = SUM_{lam |- k} (f^lam)^3 * ( SUM_{cell} c(cell)^2  -  C(k,2) )  <=  0

equivalently T_3(k) = SUM_lam (f^lam)^2 chi^lam(3-cycle) <= 0, equivalently
Cov_Planch(f^lam, SUM c^2) <= 0. It is the sole open input of the Delta_lam
super-exponential growth bound, and five attack routes have been eliminated
across the epic's phases 0-2. The bean records the identity as verified for
k <= 40.

*** THIS IS EVIDENCE, NOT A PROOF, AND EXTENDING IT DOES NOT NARROW THE GAP ***

A conjecture with five eliminated routes is not short of confidence; it is short
of an argument. Verifying more k adds nothing to the proof and is recorded here
only because it is cheap and because a counterexample, if one existed, would end
the epic outright. Read the result as "no counterexample below the stated bound",
never as support for the conjecture being true.

*** EXACT ARITHMETIC THROUGHOUT ***

f^lam is computed by the Frame-Robinson-Thrall hook-length formula in Python
integers, and SUM c^2 and C(k,2) are integers, so cov(k) is an exact integer and
its SIGN is exact. No float appears anywhere in this file -- deliberately, since
f^lam at k = 55 already exceeds 10^25 and (f^lam)^3 exceeds 10^76, where a double
would have lost the sign of a near-cancelling sum long before the answer.
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


def partitions(n: int, cap: int | None = None):
    """Weakly decreasing partitions of `n`, largest part <= cap."""
    if cap is None:
        cap = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, cap), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def hook_dim(lam: tuple[int, ...], nfact: int) -> int:
    """f^lam by the hook-length formula -- exact integer division."""
    conj = []
    if lam:
        for j in range(lam[0]):
            conj.append(sum(1 for r in lam if r > j))
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= row - j + conj[j] - i - 1
    return nfact // prod


def content_sq_sum(lam: tuple[int, ...]) -> int:
    return sum((j - i) ** 2 for i, row in enumerate(lam) for j in range(row))


def cov(k: int) -> int:
    nfact = 1
    for i in range(2, k + 1):
        nfact *= i
    binom = k * (k - 1) // 2
    total = 0
    for lam in partitions(k):
        f = hook_dim(lam, nfact)
        total += f * f * f * (content_sq_sum(lam) - binom)
    return total


def main() -> int:
    t0 = time.monotonic()
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 52
    a, ok = [], True

    print("=" * 78)
    print("1. REPRODUCE THE SMALL CASES BEFORE TRUSTING THE MACHINERY")
    print("=" * 78)
    # f^lam for k=4 is 1,3,2,3,1 over (4),(3,1),(2,2),(2,1,1),(1^4) -- sums of
    # squares 1+9+4+9+1 = 24 = 4!. If the hook formula were wrong this fails here
    # rather than silently at k=50.
    f4 = {lam: hook_dim(lam, 24) for lam in partitions(4)}
    a.append({"name": "hook_formula_reproduces_sum_of_squares_eq_factorial",
              "computed": sum(v * v for v in f4.values()), "expected": 24,
              "passed": sum(v * v for v in f4.values()) == 24})
    ok &= a[-1]["passed"]
    print(f"  [{'PASS' if a[-1]['passed'] else 'FAIL'}] "
          f"sum (f^lam)^2 = 4! : {a[-1]['computed']}")
    a.append({"name": "hook_formula_reproduces_f_21_eq_2",
              "computed": hook_dim((2, 1), 6), "expected": 2,
              "passed": hook_dim((2, 1), 6) == 2})
    ok &= a[-1]["passed"]
    print(f"  [{'PASS' if a[-1]['passed'] else 'FAIL'}] f^(2,1) = 2 : "
          f"{a[-1]['computed']}")

    print()
    print("=" * 78)
    print(f"2. cov(k) FOR k = 1 .. {limit}   (exact integers; sign is exact)")
    print("=" * 78)
    first_positive = None
    values = {}
    for k in range(1, limit + 1):
        c = cov(k)
        values[k] = c
        if c > 0 and first_positive is None:
            first_positive = k
        if k <= 12 or k % 5 == 0 or k >= limit - 2:
            sign = "<= 0" if c <= 0 else ">>> POSITIVE <<<"
            print(f"    k={k:>3}  cov={str(c)[:34]:<34} {sign}")

    a.append({"name": "no_counterexample_up_to_limit",
              "computed": first_positive, "expected": None,
              "passed": first_positive is None,
              "note": f"cov(k) <= 0 for every k <= {limit}. Evidence only -- a "
                      "conjecture with five eliminated routes is short of an "
                      "argument, not of confidence"})
    ok &= a[-1]["passed"]
    print()
    print(f"  [{'PASS' if a[-1]['passed'] else 'FAIL'}] "
          f"no_counterexample_up_to_limit: first positive k = {first_positive}")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))
    try:
        head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        head = "unknown"
    out = HERE / "qbeta-covariance-kernel-extend.witness.json"
    out.write_text(json.dumps({
        "computation": "qbeta-covariance-kernel-extend",
        "assertions": a, "allPassed": bool(ok),
        "parameters": {"limit": limit, "epic": "qou-x631",
                       "conjecture": "cov(k) = sum_lam (f^lam)^3 (sum c^2 - C(k,2)) <= 0",
                       "arithmetic": "exact integers; no float64 anywhere"},
        "data": {"cov_by_k": {str(k): str(v) for k, v in values.items()}},
        "provenance": {"headSha": head,
                       "producer": "computations/qbeta/qbeta_covariance_kernel_extend_probe.py",
                       "elapsed_s": round(time.monotonic() - t0, 3)},
    }, indent=2) + "\n")
    print(f"witness -> {out.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
