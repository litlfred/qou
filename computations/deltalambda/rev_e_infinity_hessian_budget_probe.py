#!/usr/bin/env python3
"""Measure `G`'s TRUE concavity budget for the `Xbot` integrality penalty — the one condition
that could have reopened the route `PenaltyFamilyCeiling.lean` excludes.

Bean `qou-as81` (A1), epic `qou-3e6w`.

## What is being measured, and why it decides something

`rev_e_infinity_xbot_relaxation_probe.py` bounds the INTEGER supremum of `G` by the REAL
supremum of `G_lam(u) = G(u) + lam * sum_j (u_j^2 - u_j)`, valid because every integer
`u_j >= 0` has `u_j^2 >= u_j`.  It takes the admissible range to be `lam < ln q0 / 2`, on the
grounds that `+lam sum u^2` has to be eaten by `G`'s own `-(ln q0 / 2) sum u^2` term.

`QOU.BraidKnot.PenaltyFamilyCeiling` proves that the whole penalty family is then bounded away
from closing A1: every bound it can certify is at least `sup_real G - J*lam/4`, which with
`sup_real G >= 3.27708095409687544` (the `lam = 0` ascent at `pe = 6`), `J = JPAD = 26` and
`lam = ln q0/2` is `2.937973613 = 1.3603x` the enumerated maximum, against `1.1873x` required
for `cut <= 32`.  That exclusion is **conditional on `ln q0 / 2` being the budget**, and
`ln q0 / 2` is a *sufficient* condition in the probe, not a measured one: `G` carries further
negative curvature from `Rg`, `Wg` and a `gx(...)` term per pair.  The theorem
`budget_needed_for_cut_32` states the reopening condition as a number — the budget would have
to reach `0.1096493063 = 2.1018 x ln q0/2`.

This script measures it.  `G + lam * sum(u^2 - u)` is concave iff `H_G + 2 lam I <= 0`, i.e.

    lam  <=  -lam_max(H_G) / 2 ,

so each sampled point gives an UPPER bound on the budget, and a sampled value BELOW the
requirement closes the route (the true budget is an infimum over the domain).

## Two traps this script exists to document

1. **The diagonal is not the answer, and it points the wrong way.**  `lam_max(H_G) >= max_i
   H_ii`, so the diagonal alone bounds the budget from above too — but loosely.  Measured at
   `T = 26`: `max_i H_ii = -0.826099` gives `lam <= 0.413579 = 7.93 x ln q0/2`, which looks
   like a decisive REOPENING.  The full Hessian gives `lam_max = -0.128791`, hence
   `lam <= 0.064396 = 1.2343 x`, which does not reopen anything.  The cross terms — the pair
   gains `epsx(g) - epsx(g + u_jp - u_j)` — inflate the diagonal reading by **6.42x**.  Both
   numbers are reported below so the gap is visible rather than inferred.
2. **Second-differencing `G` at the probe's own `mp.dps = 25` returns noise.**  With
   `h = 1e-18`, `(G(u+h) - 2G(u) + G(u-h))/h^2` loses ~36 digits and reported
   `H_ii ~ +9e11` — positive curvature on a function that is provably concave.  This script
   central-differences the probe's EXACT gradient `dG_coord` instead (one order of difference,
   not two) at `mp.dps = 60` with the series caches cleared, and checks the Hessian's own
   asymmetry as a conditioning witness (measured `< 1e-40`).

## No witness, deliberately

`G` lives in `rev_e_infinity_xbot_relaxation_probe.py`, which is on the unmerged `#7419`
branch; this script loads that file's definition prefix.  A witness written from here would
carry a `scriptHash` for a producer whose own cone is not on `main`, so it would be
mis-provenanced.  The numbers are printed, the commands are in this docstring, and the
conclusion is carried by Lean.  When the relaxation probe lands, fold this into it.
"""

from __future__ import annotations

import hashlib
import io
import os
import sys

import mpmath as mp

# The relaxation probe's definitions end at its R1 banner; everything above is definitions plus
# cheap setup.  Asserted rather than assumed, so a shift in that file fails loudly here.
_CUT_BANNER = 'print("R1  does the real extension reproduce the committed integer evaluator?")'

HERE = os.path.dirname(os.path.abspath(__file__))
RELAX = os.path.join(HERE, "rev_e_infinity_xbot_relaxation_probe.py")

# The two numbers the exclusion turns on, from `PenaltyFamilyCeiling.lean`.
SUP_G_LOWER = mp.mpf("3.27708095409687544")          # lam = 0 ascent at pe = 6, KKT 9.4e-14
ENUM_XBOT = mp.mpf("2.159802376118285961604")        # the enumerated Xbot maximum
NEED_CUT32 = mp.mpf("0.1096493063389068726")         # budget needed for cut <= 32
NEED_CUT27 = mp.mpf("0.1497806328604041521")         # budget needed for G1 parity
REQ_CUT32 = mp.mpf("2.5643604628939807681")          # the bound cut <= 32 requires

FD_STEP = mp.mpf(10) ** (-20)
MEASURE_DPS = 60


def _load_defs(path: str) -> dict:
    """Exec the relaxation probe's definition prefix in a private namespace."""
    lines = io.open(path, encoding="utf-8").readlines()
    cut = None
    for n, line in enumerate(lines):
        if line.rstrip("\n") == _CUT_BANNER:
            cut = n
            break
    if cut is None:
        raise SystemExit(
            "rev_e_infinity_hessian_budget_probe: could not find the R1 banner in\n"
            f"  {path}\n"
            "The definition/execution boundary moved.  Re-locate it before trusting any\n"
            "number from this script — exec'ing too far runs R1-R6 (~200 min)."
        )
    src = "".join(lines[:cut])
    ns = {"__name__": "_relax_probe_defs", "__file__": path}
    exec(compile(src, path, "exec"), ns)  # noqa: S102 — our own repo source, bounded by `cut`
    ns["_cut_line"] = cut
    ns["_src_sha"] = hashlib.sha256("".join(lines).encode()).hexdigest()[:12]
    return ns


def _hessian(ns: dict, u: list, pe: int):
    """`H_ij = d/du_j (dG/du_i)` by central difference on the probe's exact gradient.

    Returns the symmetrised matrix and the pre-symmetrisation asymmetry, which is the
    conditioning witness: `H` is symmetric exactly, so a large asymmetry means the step or the
    precision is wrong, not that the mathematics is.
    """
    dG = ns["dG_coord"]
    n = len(u)
    raw = mp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            up, um = list(u), list(u)
            up[j] += FD_STEP
            um[j] -= FD_STEP
            a = dG(up, pe, i, up[i] if j == i else u[i])
            b = dG(um, pe, i, um[i] if j == i else u[i])
            raw[i, j] = (a - b) / (2 * FD_STEP)
    asym = max(abs(raw[i, j] - raw[j, i]) for i in range(n) for j in range(n))
    sym = mp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            sym[i, j] = (raw[i, j] + raw[j, i]) / 2
    return sym, asym


def main() -> int:
    if not os.path.exists(RELAX):
        print("rev_e_infinity_hessian_budget_probe: SKIP — no measurement attempted.")
        print(f"  {RELAX}")
        print("  is absent.  `G` lives in that file, which is on the unmerged #7419 branch;")
        print("  check it out (or cherry-pick it) and re-run.  This is a SKIP, not a pass:")
        print("  nothing below was measured.")
        return 0

    ns = _load_defs(RELAX)
    load_dps = mp.mp.dps
    mp.mp.dps = MEASURE_DPS
    for key in ("_DC", "_GAMMA"):
        if isinstance(ns.get(key), dict):
            ns[key].clear()

    G = ns["G"]
    lam_max = ns["LAM_MAX"]
    jpad = ns["JPAD"]
    pemax = ns["PEMAX"]

    print("REV_n / Xbot: the TRUE concavity budget for the integrality penalty")
    print(f"  source {os.path.basename(RELAX)} sha256[:12] = {ns['_src_sha']}, "
          f"definitions through line {ns['_cut_line']}")
    print(f"  loaded at mp.dps = {load_dps}; re-measured at mp.dps = {mp.mp.dps} with the "
          f"series caches cleared")
    print(f"  probe's admissible range: lam < ln q0 / 2 = {mp.nstr(lam_max, 16)}  (SUFFICIENT, "
          f"not measured)")
    print(f"  JPAD = {jpad}, PEMAX = {pemax}")
    print(f"  reopening thresholds: cut <= 32 needs lam >= {mp.nstr(NEED_CUT32, 12)} "
          f"({mp.nstr(NEED_CUT32 / lam_max, 6)}x), G1 parity {mp.nstr(NEED_CUT27, 12)} "
          f"({mp.nstr(NEED_CUT27 / lam_max, 6)}x)")
    print()

    worst = None
    for pe in (0, 4, pemax):
        for tlen in (4, 8, 12, 20, jpad):
            for lab, val in (("0.25", "0.25"), ("0.5", "0.5"), ("1e-6", "1e-6")):
                u = [mp.mpf(val)] * tlen
                if G(u, pe) == mp.mpf("-inf"):
                    print(f"  pe={pe} T={tlen:2d} u={lab:5s}: outside the domain")
                    continue
                sym, asym = _hessian(ns, u, pe)
                ev = mp.eigsy(sym, eigvals_only=True)
                emax = max(ev)
                diag_max = max(sym[i, i] for i in range(tlen))
                budget = -emax / 2
                if worst is None or budget < worst[0]:
                    worst = (budget, pe, tlen, lab, emax, diag_max)
                print(f"  pe={pe} T={tlen:2d} u={lab:5s}: "
                      f"eig_max {mp.nstr(emax, 12):>16s}  "
                      f"diag_max {mp.nstr(diag_max, 10):>14s}  "
                      f"lam <= {mp.nstr(budget, 12):>16s} "
                      f"({mp.nstr(budget / lam_max, 6):>9s}x)  asym {mp.nstr(asym, 3)}",
                      flush=True)

    if worst is None:
        print("no sampled point was inside the domain — nothing measured")
        return 1

    budget, pe, tlen, lab, emax, diag_max = worst
    diag_budget = -diag_max / 2
    depth = mp.mpf(jpad) * budget / 4
    floor = SUP_G_LOWER - depth
    depth_lmax = mp.mpf(jpad) * lam_max / 4
    floor_lmax = SUP_G_LOWER - depth_lmax

    print()
    print(f"TIGHTEST sampled: lam <= {mp.nstr(budget, 16)} at pe = {pe}, T = {tlen}, u = {lab}")
    print(f"  = {mp.nstr(budget / lam_max, 8)} x the probe's ln q0 / 2")
    print(f"  eig_max = {mp.nstr(emax, 14)};  diagonal-only reading there would be "
          f"lam <= {mp.nstr(diag_budget, 12)} ({mp.nstr(diag_budget / lam_max, 6)}x), "
          f"i.e. the cross terms inflate it {mp.nstr(diag_budget / budget, 6)}x")
    print()
    print(f"  at ln q0 / 2:      depth {mp.nstr(depth_lmax, 14)}  floor "
          f"{mp.nstr(floor_lmax, 16)} = {mp.nstr(floor_lmax / ENUM_XBOT, 10)}x")
    print(f"  at the MEASURED budget: depth {mp.nstr(depth, 14)}  floor "
          f"{mp.nstr(floor, 16)} = {mp.nstr(floor / ENUM_XBOT, 10)}x")
    print(f"  cut <= 32 requires {mp.nstr(REQ_CUT32, 16)} = "
          f"{mp.nstr(REQ_CUT32 / ENUM_XBOT, 10)}x")
    print()

    ok32 = budget < NEED_CUT32
    ok27 = budget < NEED_CUT27
    print(f"  cut <= 32:  measured budget {'<' if ok32 else '>='} required "
          f"-> route {'CLOSED' if ok32 else 'REOPENED'}")
    print(f"  G1 parity:  measured budget {'<' if ok27 else '>='} required "
          f"-> route {'CLOSED' if ok27 else 'REOPENED'}")
    print(f"  floor at the measured budget exceeds the cut <= 32 requirement by "
          f"{mp.nstr(floor - REQ_CUT32, 12)}")
    print()
    print("Scope.  A sampled point gives an UPPER bound on the budget, which is an infimum over")
    print("the whole domain, so a value below the requirement CLOSES the route and a value above")
    print("it would not by itself establish a budget.  The budget also DECREASES with the row")
    print("count across this sample and is still decreasing at T = JPAD, so the relevant value")
    print("is at most the one reported.  Not measured here: non-uniform `u`, points near the")
    print("domain boundary, and T > JPAD.")

    return 0 if (ok32 and ok27 and floor > REQ_CUT32) else 1


if __name__ == "__main__":
    sys.exit(main())
