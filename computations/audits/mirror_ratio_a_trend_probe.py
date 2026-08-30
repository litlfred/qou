#!/usr/bin/env python3
"""Is the mirror split/Coulomb ratio constant in A, as its witness says? No.

`computations/mirror-nuclei-coulomb-systematics.witness.json` describes its
ratio as "≈constant across A=3–39", 0.84 +/- 0.06. This probe tests that against
the eight rows, and separately checks whether the committed rows still
reproduce.

TWO FINDINGS, and the second was not what this probe was written to look for.

1. THE RATIO IS NOT CONSTANT. It rises monotonically with A: Pearson r ~ 0.83,
   t ~ 3.65 on 6 dof (crit 2.447, p < 0.05), and a straight line beats the mean
   by ~44% in rms. The "+/- 0.06" is a trend, not scatter about a constant.

2. THE COMMITTED WITNESS IS NUMERICALLY STALE. Its coulomb_canonical column no
   longer reproduces: `coulomb_energy.mirror_displacement_mev` has changed on
   main since the witness was computed (2026-07-11), by an EXACTLY UNIFORM
   factor -- 1.178176504688906, identical across all eight pairs to 19
   significant figures. So it is a normalisation change, not a model change.

   Because Pearson r and the t-statistic are invariant under rescaling one
   variable, finding 1 is UNAFFECTED: r and t are identical on the stale and the
   live numbers. What moves is the absolute level -- the chain mean goes
   0.8376 -> 0.9868 and the A=3 datum 0.7650 -> 0.9013.

   That has an interpretive consequence the witness has not caught up with: its
   narrative explains "the ~0.8 factor" as "the known uniform-sphere
   over-estimate". At the current normalisation the mean is ~0.99, so there is
   essentially no over-estimate left to explain.

PRECISION. Exact `Fraction` arithmetic throughout; the square roots use
`decimal` at 50 digits. `float()` appears only in display. AGENTS.md: probes are
not exempt from the no-float64 rule.

Read-only: recomputes from `coulomb_energy` and AME, reads the witness, and
writes nothing.
"""
from __future__ import annotations

import json
import pathlib
import sys
from decimal import Decimal, getcontext
from fractions import Fraction as F

getcontext().prec = 50

_HERE = pathlib.Path(__file__).resolve()
_COMPUTATIONS = _HERE.parents[1]
# Same preamble as the producer: substrate/ then computations/ on the path, and
# the compute precision set the same way, so the live recompute is comparable.
sys.path.insert(0, str(_COMPUTATIONS / "substrate"))
sys.path.insert(0, str(_COMPUTATIONS))

from _precision import set_compute_dps  # noqa: E402
from codata_constants import _ame_binding_mev  # noqa: E402
from coulomb_energy import mirror_displacement_mev  # noqa: E402

set_compute_dps()

WITNESS = _COMPUTATIONS / "mirror-nuclei-coulomb-systematics.witness.json"
PAIRS = [("3H/3He", 1, 2, 3), ("7Li/7Be", 3, 4, 7), ("11B/11C", 5, 6, 11),
         ("13C/13N", 6, 7, 13), ("15N/15O", 7, 8, 15), ("23Na/23Mg", 11, 12, 23),
         ("27Al/27Si", 13, 14, 27), ("39K/39Ca", 19, 20, 39)]
T_CRIT_6DOF_05 = Decimal("2.447")


def _dec(fr: F) -> Decimal:
    return Decimal(fr.numerator) / Decimal(fr.denominator)


def _sqrt(fr: F) -> Decimal:
    return _dec(fr).sqrt()


def trend(A: list[F], R: list[F]) -> dict:
    n = len(A)
    mA, mR = sum(A) / n, sum(R) / n
    sAA = sum((a - mA) ** 2 for a in A)
    sRR = sum((r - mR) ** 2 for r in R)
    sAR = sum((a - mA) * (r - mR) for a, r in zip(A, R))
    r2 = sAR * sAR / (sAA * sRR)
    slope = sAR / sAA
    intercept = mR - slope * mA
    resid = sum((y - (intercept + slope * a)) ** 2 for a, y in zip(A, R))
    r = _sqrt(r2)
    return {
        "mean": mR, "r": r, "r2": r2,
        "t": r * Decimal(n - 2).sqrt() / (Decimal(1) - _dec(r2)).sqrt(),
        "slope": slope, "at3": intercept + slope * 3, "at39": intercept + slope * 39,
        "rms_line": _sqrt(resid / n), "rms_mean": _sqrt(sRR / n),
    }


def main() -> int:
    rows = json.loads(WITNESS.read_text())["data"]["mirror_pairs"]
    A = [F(int(r["A"])) for r in rows]
    R_stale = [F(str(r["ratio"])) for r in rows]

    R_live, factors = [], []
    for (nm, Z1, Z2, Aa), row in zip(PAIRS, rows):
        s = F(str(_ame_binding_mev(Z1, Aa))) - F(str(_ame_binding_mev(Z2, Aa)))
        c = F(str(mirror_displacement_mev(Z2, Z1, Aa)))
        R_live.append(s / c)
        factors.append(F(str(row["coulomb_canonical"])) / c)

    t_stale, t_live = trend(A, R_stale), trend(A, R_live)

    print("=== finding 1: the ratio is not constant ===")
    for lbl, tr in (("committed rows", t_stale), ("live recompute", t_live)):
        print(f"  {lbl:<16} mean {float(tr['mean']):.4f}  r {str(tr['r'])[:7]}  "
              f"t {str(tr['t'])[:6]}  rms line {str(tr['rms_line'])[:7]} "
              f"vs mean {str(tr['rms_mean'])[:7]}")
    trending = t_live["t"] > T_CRIT_6DOF_05
    line_better = t_live["rms_line"] < t_live["rms_mean"]
    print(f"  significant monotone trend : {trending}   line beats mean : {line_better}")

    print("\n=== finding 2: the committed witness is numerically stale ===")
    spread = max(factors) - min(factors)
    uniform = _dec(abs(spread) / min(factors)) < Decimal("1e-12")
    print(f"  committed dE_C / live dE_C = {str(_dec(factors[0]))[:21]}")
    print(f"  identical across all {len(factors)} pairs to 1e-12 : {uniform}")
    print(f"  => a uniform NORMALISATION change, not a model change")
    print(f"  chain mean {float(t_stale['mean']):.4f} -> {float(t_live['mean']):.4f};  "
          f"A=3 {float(R_stale[0]):.4f} -> {float(R_live[0]):.4f}")
    print(f"  r and t are scale-invariant, so finding 1 is unaffected: "
          f"{str(t_stale['r'])[:7]} == {str(t_live['r'])[:7]}")

    print("\nCONSEQUENCES")
    print(f"  - Quote the A you need. A=3 (3H/3He) is {float(R_live[0]):.4f} live, "
          f"not the chain mean {float(t_live['mean']):.4f}.")
    print("  - The witness's 'the ~0.8 factor is the known uniform-sphere")
    print(f"    over-estimate' no longer applies: the live mean is "
          f"{float(t_live['mean']):.3f}, so there is no over-estimate to explain.")
    print("  - Regenerating the witness WILL move every number by the factor")
    print("    above. That is an upstream coulomb_energy change, not a defect in")
    print("    this producer; whoever regenerates should audit it and say so.")

    r_same = str(t_stale["r"])[:7] == str(t_live["r"])[:7]
    if not (trending and line_better and uniform and r_same):
        print("\nGUARD TRIPPED: a verdict stopped reproducing — the audits citing "
              "this probe are stale.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
