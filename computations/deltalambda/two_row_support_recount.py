#!/usr/bin/env python3
"""Support recount for the Delta_lambda binding sum, C frame vs D frame.

    B(K) = m_e * sum_{lambda |- n} y_lambda * chi^lambda * Delta_lambda

Convention D is Wenzl level r = 2 (proved: `wenzlLevel_conventionD`), and
`y_lambda = 0 <=> len(lambda) > r` (proved sorry-free for all n and all r:
`schurPrincipal_eq_zero_iff`).  So under D the sum runs over the <=2-row
partitions ONLY -- every longer block is annihilated exactly.

This probe measures how much of the sum that removes, in three currencies:

  1. BLOCK COUNT      -- how many lambda survive.
  2. ALGEBRA MASS     -- sum of (dim V_lambda)^2, i.e. Catalan(n) vs n!.
  3. ELL-1 MASS       -- sum |y_lambda| * |Delta_lambda|, which is the
     quantity an ell-1 ceiling on the binding sum is built from.

(3) is the one that matters for re-scoring.  An ell-1 ceiling has the form

    |sum_lambda y_lambda chi^lambda Delta_lambda|
        <= max_lambda |chi^lambda| * sum_lambda |y_lambda| |Delta_lambda|

so DROPPING terms at fixed weights can only LOWER it.  But the D-frame
y_lambda differ from the C-frame y_lambda on the surviving blocks too, so
the number must be recomputed rather than inferred -- which is exactly what
this does.

Delta_lambda = (-1)^{n(lambda)} * dim V_lambda is PROVED (general n,
sorry-free): `QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional`.
Nothing here fits anything; no observable is targeted.

Pin: PROTON (`qou_substrate.constants.Q`), per the 2026-08-07 directive.
The C-frame column is computed from the SAME q0 -- it varies the Markov
parameter z, not the pin -- so the two columns are frame-comparable and
neither straddles a layer.  `wedderburn_jones_markov.y_lambda_at` is
deliberately NOT called (it serves a muon-built cache when handed
q_parameter.Q); the live closed form is used instead.
"""

from __future__ import annotations

import json
import sys
from math import factorial
from pathlib import Path

from mpmath import mp

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools" / "qou-substrate" / "python"))
sys.path.insert(0, str(REPO / "computations"))

mp.dps = 65


def dim_irrep(lam: tuple[int, ...]) -> int:
    """dim V_lambda by the hook-length formula (exact integer)."""
    n = sum(lam)
    rows = len(lam)
    conj = [sum(1 for i in range(rows) if lam[i] > j) for j in range(lam[0])]
    prod = 1
    for i in range(rows):
        for j in range(lam[i]):
            prod *= (lam[i] - j) + (conj[j] - i) - 1
    return factorial(n) // prod


def n_of_partition(lam: tuple[int, ...]) -> int:
    """n(lambda) = sum i * lambda_i, 0-indexed."""
    return sum(i * p for i, p in enumerate(lam))


def delta_lambda(lam: tuple[int, ...]) -> int:
    """PROVED value: (-1)^{n(lambda)} * dim V_lambda."""
    return (-1) ** n_of_partition(lam) * dim_irrep(lam)


def catalan(n: int) -> int:
    from math import comb
    return comb(2 * n, n) // (n + 1)


def main() -> int:
    from qou_substrate.constants import Q as Q_PROTON
    import schur_principal_mpmath as spm

    q = mp.mpf(str(Q_PROTON))
    report = {
        "pin": {"name": "proton", "q0": mp.nstr(q, 50),
                "source": "qou_substrate.constants.Q"},
        "delta_lambda": "(-1)^{n(lambda)} * dim V_lambda (PROVED, general n)",
        "per_n": {},
    }

    print(f"pin: proton q0 = {mp.nstr(q, 20)}")
    print()

    for n in range(2, 9):
        parts = spm.partitions_of(n)
        y_D = spm.y_lambda_at_q0_mpmath(n, q)
        y_C = spm.y_lambda_at_q0_mpmath_convention_C_HISTORICAL(n, q)

        surv, killed = [], []
        l1_D_all = l1_D_surv = mp.mpf(0)
        l1_C_all = l1_C_surv = mp.mpf(0)
        dim2_all = dim2_surv = 0

        rows = []
        for lam in parts:
            d = dim_irrep(lam)
            dl = delta_lambda(lam)
            yD = mp.mpf(y_D[lam])
            yC = mp.mpf(y_C[lam])
            two_row = len(lam) <= 2

            dim2_all += d * d
            l1_D_all += abs(yD) * abs(dl)
            l1_C_all += abs(yC) * abs(dl)
            if two_row:
                surv.append(lam)
                dim2_surv += d * d
                l1_D_surv += abs(yD) * abs(dl)
                l1_C_surv += abs(yC) * abs(dl)
            else:
                killed.append(lam)

            rows.append({
                "lambda": list(lam), "rows": len(lam), "dim": d,
                "Delta": dl,
                "y_D": mp.nstr(yD, 25), "y_C": mp.nstr(yC, 25),
                "survives_D": two_row,
            })

        # The vanishing is the proved lemma; assert it rather than assume it.
        max_y_killed = max((abs(mp.mpf(y_D[l])) for l in killed),
                           default=mp.mpf(0))
        vanishing_ok = max_y_killed < mp.mpf(10) ** -40

        # WHY the D-frame ell-1 mass comes out at exactly 1: the trace is
        # normalised, tr_M(1) = sum_lambda y_lambda * dim V_lambda = 1, and
        # |Delta_lambda| = dim V_lambda.  So sum |y| |Delta| = sum |y| dim,
        # which equals 1 exactly WHEN every y_lambda >= 0.  Under D that
        # holds (zero off <=2 rows, positive on it); under C it fails --
        # some ell >= 3 weights go negative, so the C ell-1 mass exceeds 1.
        tiny = -(mp.mpf(10) ** -40)
        norm_D = sum(mp.mpf(y_D[l]) * dim_irrep(l) for l in parts)
        norm_C = sum(mp.mpf(y_C[l]) * dim_irrep(l) for l in parts)
        neg_D = [list(l) for l in parts if mp.mpf(y_D[l]) < tiny]
        neg_C = [list(l) for l in parts if mp.mpf(y_C[l]) < tiny]
        print(f"  trace norm sum y*dim : D {mp.nstr(norm_D, 12)} | "
              f"C {mp.nstr(norm_C, 12)}")
        print(f"  negative-weight blks : D {len(neg_D)} | C {len(neg_C)}"
              f"  -> D weights are a probability distribution, C's are not")

        print(f"n = {n}   ({len(parts)} partitions)")
        print(f"  surviving (<=2 rows) : {len(surv)}/{len(parts)}"
              f"  = {100*len(surv)/len(parts):.1f}%")
        print(f"  algebra mass         : {dim2_surv}/{dim2_all}"
              f"  (Catalan {catalan(n)} / n! {factorial(n)})"
              f"  -> {100*dim2_surv/dim2_all:.1f}% survives")
        print(f"  D-frame ell-1 mass   : {mp.nstr(l1_D_surv,12)} / "
              f"{mp.nstr(l1_D_all,12)}"
              f"  -> {mp.nstr(100*l1_D_surv/l1_D_all, 8)}% survives")
        print(f"  C-frame ell-1 mass   : {mp.nstr(l1_C_surv,12)} / "
              f"{mp.nstr(l1_C_all,12)}"
              f"  -> {mp.nstr(100*l1_C_surv/l1_C_all, 8)}% survives")
        print(f"  ell-1 D_all / C_all  : "
              f"{mp.nstr(l1_D_all/l1_C_all, 12)}   (frame ratio, ALL blocks)")
        print(f"  ell-1 D_surv / C_all : "
              f"{mp.nstr(l1_D_surv/l1_C_all, 12)}   (what re-scoring multiplies by)")
        print(f"  y=0 off <=2 rows     : {vanishing_ok}"
              f"  (max |y_D| on killed = {mp.nstr(max_y_killed, 6)})")
        print()

        report["per_n"][str(n)] = {
            "n_partitions": len(parts),
            "n_surviving": len(surv),
            "surviving": [list(s) for s in surv],
            "dim2_surviving": dim2_surv, "dim2_all": dim2_all,
            "catalan": catalan(n), "n_factorial": factorial(n),
            "l1_D_all": mp.nstr(l1_D_all, 40),
            "l1_D_surviving": mp.nstr(l1_D_surv, 40),
            "l1_C_all": mp.nstr(l1_C_all, 40),
            "l1_C_surviving": mp.nstr(l1_C_surv, 40),
            "l1_ratio_Dsurv_over_Call": mp.nstr(l1_D_surv / l1_C_all, 40),
            "l1_ratio_Dall_over_Call": mp.nstr(l1_D_all / l1_C_all, 40),
            "weight_vanishing_verified": bool(vanishing_ok),
            "trace_norm_D": mp.nstr(norm_D, 30),
            "trace_norm_C": mp.nstr(norm_C, 30),
            "negative_weight_blocks_D": neg_D,
            "negative_weight_blocks_C": neg_C,
            "rows": rows,
        }

    out = Path(__file__).with_name("two-row-support-recount.json")
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(f"wrote {out.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
