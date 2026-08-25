#!/usr/bin/env python3
"""Re-measure the ell-1 binding ceiling in the D frame.  Does it survive?

## Why this needed re-measuring

`computations/delta-lambda-l1-ceiling-sign-prune.witness.json` -- the source
of the "the existing terms reach at most 59 % of the AME target" claim -- is
`q0Anchor: "muon"`, computedAt 2026-07-17, and its ell-1 sum takes nonzero
contributions from `ell(lambda) = 3,4,5,6` blocks.  Under convention D those
blocks have `y_lambda = 0` exactly (PROVED all-n:
`QOU.QBeta.WenzlWeight.schurPrincipal_eq_zero_iff`).  So the committed
ceiling is neither proton-pinned nor D-frame, and the question "does the
ceiling survive restriction to the surviving blocks" had not been measured.

## What is measured

    ceiling  =  sum_lambda |y_lambda * chi^lambda(beta_atom) * Delta_lambda|
                / |B_AME / m_e|

three ways, so the muon-vs-proton and C-vs-D effects are separable:

  * COMMITTED   -- the y_lambda already in the chi witness (proton pin,
                   regenerated 2026-08-10, convention D).
  * D LIVE      -- y_lambda recomputed from the live closed form at the
                   proton pin, restricted to <=2 rows.  Should agree with
                   COMMITTED; the agreement is the cross-check.
  * C LIVE      -- y_lambda from the historical convention-C closed form at
                   the SAME proton q0.  This isolates the FRAME effect from
                   the PIN effect: it is not the muon witness, and it is not
                   claimed to reproduce it.

`Delta_lambda = (-1)^{n(lambda)} * dim V_lambda` -- PROVED, general n
(`dtEuler_eq_deltaLambda_unconditional`).

## The structural expectation, stated before the run -- AND IT WAS WRONG

Predicted: "dropping terms from an ell-1 sum at fixed weights can only lower
it, and under D the dropped weights are exactly zero, so the D ceiling
should come out at or below the C one."

MEASURED: the D ceiling is HIGHER at every atom (D 1.097x, T 1.008x,
He-3 1.170x, He-4 1.068x).  The prediction's error is the clause "at fixed
weights" -- the weights are NOT fixed between the frames.  Both frames
normalise to `sum_lambda y_lambda dim V_lambda = 1`, so zeroing the
`ell >= 3` blocks forces D to put ALL of that unit mass on the <=2-row
blocks, where it is multiplied by that subset's `|chi^lambda|`.  D drops
terms and enlarges the survivors; which effect wins is an empirical question
about `chi`, and the enlargement wins.

This also corrects a claim made earlier in this PR (the
`two_row_support_recount` commit message): that the D-frame ceiling is
"tighter than the C-frame bound twice over".  Two different objects were
conflated.  The CRUDE bound `max_{<=2 rows}|chi^lambda| * sum|y||Delta|`
does tighten -- `sum|y||Delta|` falls 1.0199 -> 1.0000 and the max is over a
smaller index set.  The ACTUAL ell-1 ceiling `sum|y chi Delta|`, which is
what the corpus means by "the ell-1 ceiling", LOOSENS.  A crude bound
tightening while the quantity it bounds loosens is perfectly consistent; the
error was calling them the same thing.

Nothing is fitted.  chi^lambda is read from the committed proton-pinned
witnesses; no muon-built cache is consulted, and
`wedderburn_jones_markov.y_lambda_at` is deliberately not called.
"""

from __future__ import annotations

import json
import sys
from math import factorial
from pathlib import Path

from mpmath import mp

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(REPO / "tools" / "qou-substrate" / "python"))
sys.path.insert(0, str(REPO / "computations"))

mp.dps = 60

M_E_MEV = mp.mpf("0.51099895069")

ATOMS = {
    "deuteron": ("chi-deuteron-h6-at-q0-50dps.witness.json", 6, "2.224566"),
    "tritium": ("chi-tritium-h9-at-q0-50dps.witness.json", 9, "8.481798"),
    "helium-3": ("chi-helium-3-h9-at-q0-50dps.witness.json", 9, "7.718043"),
    "helium-4": ("chi-helium-4-h12-at-q0-50dps.witness.json", 12, "28.295673"),
}


def dim_irrep(lam: tuple[int, ...]) -> int:
    n = sum(lam)
    conj = [sum(1 for i in range(len(lam)) if lam[i] > j) for j in range(lam[0])]
    prod = 1
    for i in range(len(lam)):
        for j in range(lam[i]):
            prod *= (lam[i] - j) + (conj[j] - i) - 1
    return factorial(n) // prod


def delta_lambda(lam: tuple[int, ...]) -> int:
    return (-1) ** sum(i * p for i, p in enumerate(lam)) * dim_irrep(lam)


def main() -> int:
    from qou_substrate.constants import Q_MP as Q_PROTON
    import schur_principal_mpmath as spm

    # Q_MP, not mpf(str(Q)): the f64 constant carries ~16 significant digits,

    # so mpf(str(...)) LAUNDERS it — the value looks 50-digit and is accurate

    # to 16. Read the high-precision name instead.

    q = Q_PROTON
    out = {
        "pin": {"name": "proton", "q0": mp.nstr(q, 50)},
        "supersedes": (
            "delta-lambda-l1-ceiling-sign-prune.witness.json is muon-pinned"
            " (2026-07-17) and carries nonzero ell>=3 ell-1 mass; its"
            " 0.3576-0.5918 range is not a D-frame number."
        ),
        "atoms": {},
    }

    print(f"proton pin q0 = {mp.nstr(q, 20)}   |   ceiling = l1 / |B_AME/m_e|")
    print()
    hdr = (f"{'atom':<10} {'n':>3} {'committed':>11} {'D live':>11} "
           f"{'C live':>11} {'D/C':>8} {'l>=3 C share':>13}")
    print(hdr)
    print("-" * len(hdr))

    for atom, (fn, n, b_ame) in ATOMS.items():
        p = REPO / "computations" / fn
        if not p.exists():
            print(f"{atom:<10} MISSING {fn}")
            continue
        w = json.loads(p.read_text())
        target = abs(mp.mpf(b_ame) / M_E_MEV)

        yD = spm.y_lambda_at_q0_mpmath(n, q)
        yC = spm.y_lambda_at_q0_mpmath_convention_C_HISTORICAL(n, q)

        l1_c = l1_D = l1_C = mp.mpf(0)
        l1_C_hi = mp.mpf(0)   # C-frame ell-1 mass sitting on ell>=3
        net_D = mp.mpf(0)
        for r in w["by_partition"]:
            lam = tuple(r["partition"])
            chi = mp.mpf(r["chi_lambda"])
            dl = delta_lambda(lam)
            l1_c += abs(mp.mpf(r["y_lambda"]) * chi * dl)
            tD = mp.mpf(yD[lam]) * chi * dl
            tC = mp.mpf(yC[lam]) * chi * dl
            l1_D += abs(tD)
            l1_C += abs(tC)
            net_D += tD
            if len(lam) >= 3:
                l1_C_hi += abs(tC)

        cc, cD, cC = l1_c / target, l1_D / target, l1_C / target
        print(f"{atom:<10} {n:>3} {mp.nstr(cc,8):>11} {mp.nstr(cD,8):>11} "
              f"{mp.nstr(cC,8):>11} {mp.nstr(cD/cC,6):>8} "
              f"{mp.nstr(100*l1_C_hi/l1_C,5)+'%':>13}")

        out["atoms"][atom] = {
            "n_strands": n, "B_AME_MeV": b_ame,
            "target_m_e": mp.nstr(target, 30),
            "ceiling_committed": mp.nstr(cc, 30),
            "ceiling_D_live": mp.nstr(cD, 30),
            "ceiling_C_live": mp.nstr(cC, 30),
            "ratio_D_over_C": mp.nstr(cD / cC, 30),
            "C_l1_share_on_rows_ge_3": mp.nstr(l1_C_hi / l1_C, 30),
            "net_signed_D_m_e": mp.nstr(net_D, 30),
            "B_ceiling_D_MeV": mp.nstr(M_E_MEV * l1_D, 20),
            # Tolerance 1e-15, not 1e-25: the committed witness and the live
            # closed form agree to ~18 digits (max |dy| = 7.8e-19 at n=6),
            # which is the generator's internal precision, not a frame
            # difference.  1e-25 was too tight and flagged a false mismatch.
            "committed_matches_D_live": bool(
                abs(cc - cD) < mp.mpf(10) ** -15),
        }

    print()
    all_below = all(mp.mpf(a["ceiling_D_live"]) < 1
                    for a in out["atoms"].values())
    tighter = all(mp.mpf(a["ratio_D_over_C"]) <= 1
                  for a in out["atoms"].values())
    xchk = all(a["committed_matches_D_live"] for a in out["atoms"].values())
    out["all_D_ceilings_below_target"] = bool(all_below)
    out["D_tighter_than_C_everywhere"] = bool(tighter)
    out["committed_reproduced_by_live_D"] = bool(xchk)
    mx = max(mp.mpf(a["ceiling_D_live"]) for a in out["atoms"].values())
    out["max_D_ceiling"] = mp.nstr(mx, 30)

    print(f"  every D-frame ceiling < 1 (magnitude absent) : {all_below}")
    print(f"  D ceiling <= C ceiling everywhere            : {tighter}")
    print(f"  committed y_lambda reproduced by live D      : {xchk}")
    print(f"  worst-case D-frame ceiling                   : "
          f"{mp.nstr(100*mx, 6)}% of target")

    o = HERE / "l1-ceiling-d-frame-remeasure.json"
    o.write_text(json.dumps(out, indent=2) + "\n")
    print(f"\nwrote {o.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
