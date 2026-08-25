#!/usr/bin/env python3
"""Is the mirror split/Coulomb ratio constant in A, as its witness says?

`computations/mirror-nuclei-coulomb-systematics.witness.json` reports

    split_AME / dE_C = 0.84 +/- 0.06, "≈constant across A=3–39"

This probe tests that description against the witness's own eight rows. It is
read-only: it re-reads the committed witness and computes, it does not re-run
the Coulomb model or touch any producer.

PRECISION. Exact `Fraction` arithmetic end to end -- the inputs are exact
decimal strings, so nothing here needs mpmath and nothing is computed in
float64. The two square roots (Pearson r, the rms figures) are taken with
`decimal` at 50 digits. `float()` appears only inside display formatting.
AGENTS.md: probes are not exempt from the no-float64 rule.

Verdict: the description understates a significant monotone trend. Reported
rather than fixed here -- correcting the witness's `description` is a producer
edit.
"""
from __future__ import annotations

import json
import pathlib
from decimal import Decimal, getcontext
from fractions import Fraction as F

getcontext().prec = 50

WITNESS = pathlib.Path(__file__).resolve().parents[1] / "mirror-nuclei-coulomb-systematics.witness.json"
T_CRIT_6DOF_05 = Decimal("2.447")  # two-sided, 6 degrees of freedom


def _sqrt(fr: F) -> Decimal:
    return (Decimal(fr.numerator) / Decimal(fr.denominator)).sqrt()


def _dec(fr: F) -> Decimal:
    return Decimal(fr.numerator) / Decimal(fr.denominator)


def main() -> int:
    rows = json.loads(WITNESS.read_text())["data"]["mirror_pairs"]
    A = [F(int(r["A"])) for r in rows]
    R = [F(str(r["ratio"])) for r in rows]
    n = len(A)

    mA, mR = sum(A) / n, sum(R) / n
    sAA = sum((a - mA) ** 2 for a in A)
    sRR = sum((r - mR) ** 2 for r in R)
    sAR = sum((a - mA) * (r - mR) for a, r in zip(A, R))

    r2 = sAR * sAR / (sAA * sRR)          # exact
    r = _sqrt(r2)
    slope = sAR / sAA
    intercept = mR - slope * mA
    t = r * Decimal(n - 2).sqrt() / (Decimal(1) - _dec(r2)).sqrt()

    resid_line = sum((y - (intercept + slope * a)) ** 2 for a, y in zip(A, R))
    rms_line, rms_mean = _sqrt(resid_line / n), _sqrt(sRR / n)

    print(f"n = {n} mirror pairs, A = {[int(a) for a in A]}")
    print(f"quoted mean ratio      : {float(mR):.6f}")
    print(f"Pearson r (ratio vs A) : {str(r)[:8]}")
    print(f"t ({n - 2} dof)             : {str(t)[:6]}   [|t| > {T_CRIT_6DOF_05} => p < 0.05]")
    print(f"slope per unit A       : {float(slope):.7f}")
    print(f"line at A=3            : {float(intercept + slope * 3):.6f}")
    print(f"line at A=39           : {float(intercept + slope * 39):.6f}")
    print(f"rms about the line     : {str(rms_line)[:8]}")
    print(f"rms about the mean     : {str(rms_mean)[:8]}")

    trending = t > T_CRIT_6DOF_05
    line_better = rms_line < rms_mean
    print()
    print(f"significant monotone trend : {trending}")
    print(f"line beats mean in rms     : {line_better}")
    print()
    print("CONSEQUENCE for front 4-B: the A=3 (3H/3He) datum is "
          f"{float(R[0]):.4f}, not the quoted {float(mR):.4f}. Using the")
    print("chain mean for the He-3 case would be off by ~1.15 sd. The ratio is")
    print("not a constant, so any use of it must say WHICH A it is evaluated at.")

    # Guard: this probe's whole point is the two verdicts above. If either
    # flips, the conclusion in the audit is stale and must be re-read.
    if not (trending and line_better):
        print("\nGUARD TRIPPED: the trend no longer reproduces -- "
              "docs/audits/2026-08-25-4b-meson-route-does-not-transport.md is stale.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
