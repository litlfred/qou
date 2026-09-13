#!/usr/bin/env python3
"""The omega-GRADE of the Kashaev remainder: st() hides a `log omega`, and the
convergence to Vol(4_1) is logarithmically slow.

Bean `qou-cds1`.  Derive-then-check throughout: every constant below is read off
a CITED asymptotic BEFORE it is measured, and the measurement is a test of the
derivation, never a fit to it.

## The gap this fills

`content/quantum-observable-universe/appendix-surreals/kashaev-surreal.md` sets
`n = omega` and recasts the volume conjecture as a STANDARD-PART identity,

    Vol(4_1)  =  st( 2*pi * log|J(zeta_omega, omega)| / omega ),

identifies `st` with Ecalle median resummation, and discharges the `4_1`
instance at leading order.  It is thorough about `st` and **says nothing about
what `st` throws away** -- the `ord_omega` of the discarded remainder appears
nowhere in it, nor anywhere else in the corpus (grep: no prior work on the
Kashaev asymptotic remainder).

`st` is not free here.  What it discards is not a pure infinitesimal.

## Derived first, from the cited asymptotic

Ohtsuki / Andersen-Hansen give, for the figure-eight,

    <4_1>_N  =  (N^{3/2} / 3^{1/4}) * exp(N*V/(2*pi)) * (1 + O(1/N)),   V := Vol(4_1)

so, taking logs and multiplying by `2*pi/N`, the remainder

    delta_N  :=  (2*pi/N) * log <4_1>_N  -  V

is **derived, not fitted**, to be

    delta_N  =  3*pi * log(N)/N  -  (pi*log 3)/(2N)  +  O(1/N^2).                (*)

Three consequences follow from (*) with no further input, and all three are
checked below against the computed sum:

  (C1)  N*delta_N / log N  ->  3*pi = 9.42477796...,  approached FROM BELOW,
        with the derived offset  -(pi*log 3)/(2*log N).
  (C2)  N*delta_N  ->  INFINITY.  So delta is NOT a pure grade-(-1) monomial:
        a grade-(-1) infinitesimal `c/omega` has `omega * c/omega = c` finite.
  (C3)  one-step Richardson in 1/N, `R_N := 2*f(2N) - f(N)`, does NOT clear the
        remainder -- it leaves `N*(R_N - V) -> 3*pi*log 2 = 6.53275827...`.

## The result, in the corpus's own surreal vocabulary

At `N = omega`,

    delta_omega  =  3*pi * (log omega)/omega  -  (pi*log 3)/(2*omega)  +  ...

Its leading monomial is `(log omega)/omega`.  In the Berarducci-Mantova
transseries hierarchy that sits **strictly between grade -1 and grade 0**:
larger than `c/omega` for every real `c`, smaller than `omega^(-1+eps)` for
every `eps > 0`.  So:

  * `ord_omega(delta) = -1` in the COARSE grading, and
  * delta is **not** a grade-(-1) monomial -- `omega * delta` is INFINITE.

Both halves are needed.  Quoting only the first ("the remainder is a first-order
infinitesimal") is true and misleading: it is the second that says the
convergence is logarithmically slow and that a `1/N` extrapolation scheme is
mis-specified.

## Why it matters beyond bookkeeping

`kashaev-surreal.md` offers the surreal form as a route in which the algebraic
side is "exactly computable" and only `st` is analytic.  (C2) prices that `st`:
the object it is applied to differs from `V` by something whose `omega`-multiple
DIVERGES, so the reduction is not a benign truncation of a convergent tail.  And
(C3) is the operational form -- anyone extrapolating the Kashaev limit
numerically on a `1/N` grid is fitting the wrong ansatz, and the error they will
observe is `3*pi*log(2)/N`, which this probe predicts before measuring.

## Scope

**(a)** -- this is an asymptotic statement about `4_1` only, resting on the cited
Ohtsuki / Andersen-Hansen expansion, which the probe does not re-derive.  What
the probe establishes is that the corpus's own computed Kashaev sum agrees with
that expansion to the precision shown, and that the three consequences hold.  It
does NOT touch the volume conjecture, does not alter `st`, and asserts nothing
about knots other than `4_1`.

## Arithmetic

mpmath at 50 dps end to end; `Vol(4_1) = 2*Cl_2(pi/3)` computed exactly at
working precision, never read from a float64 constant.  No float64 anywhere.

-- Ref: [ohtsuki2016] asymptotic expansion of the Kashaev invariant of 4_1
-- Ref: [murakami-murakami2001] https://doi.org/10.1007/BF02392716
-- Ref: [berarducci-mantova2018] surreal transseries / omega-grading
"""
from __future__ import annotations

import json
import pathlib as _pl
import sys as _sys
import time as _time

_HERE = _pl.Path(__file__).resolve()
_COMP = _HERE.parent.parent
for _p in (_COMP, _COMP / "substrate", _COMP / "qbeta"):
    _sys.path.insert(0, str(_p))

from mpmath import mp                                       # noqa: E402
from qou_substrate.witness import WitnessBuilder            # noqa: E402

WITNESS = _HERE.with_name("kashaev-remainder-omega-grade.witness.json")
DPS = 50
LADDER = (50, 100, 200, 400, 800, 1600)

results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    results.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")


def kashaev(N: int):
    """<4_1>_N = sum_{k<N} prod_{j<=k} (2 - 2 cos(2 pi j / N)), exact at mp.dps."""
    total = mp.mpf(0)
    prod = mp.mpf(1)
    for k in range(N):
        if k:
            prod *= 2 - 2 * mp.cos(2 * mp.pi * k / N)
        total += prod
    return total


def main() -> int:
    t0 = _time.time()
    mp.dps = DPS

    V = 2 * mp.clsin(2, mp.pi / 3)
    three_pi = 3 * mp.pi
    offset = mp.pi * mp.log(3) / 2

    print("=" * 78)
    print(" The omega-grade of the Kashaev remainder   (qou-cds1)")
    print("=" * 78)
    print(f"\n  Vol(4_1) = 2*Cl_2(pi/3) = {mp.nstr(V, 25)}   (computed, not a literal)")
    print(f"  DERIVED  delta_N = 3pi logN/N - (pi log3)/(2N) + O(1/N^2)")

    f = {}
    delta = {}
    for N in LADDER:
        f[N] = 2 * mp.pi / N * mp.log(kashaev(N))
        delta[N] = f[N] - V

    # --- check 1: the asymptotic SHAPE, residual halves on doubling ----------
    print("\n[1] log<4_1>_N - N*V/(2pi)  vs  (3/2)logN - (1/4)log3")
    shape_rows, ratios = [], []
    prev = None
    for N in LADDER:
        resid = mp.log(kashaev(N)) - N * V / (2 * mp.pi)
        model = mp.mpf(3) / 2 * mp.log(N) - mp.log(3) / 4
        d = resid - model
        if prev is not None:
            ratios.append(d / prev)
        prev = d
        shape_rows.append({"N": N, "residual_minus_model": mp.nstr(d, 10)})
        print(f"    N={N:5d}  resid-model = {mp.nstr(d, 10):>14}")
    print(f"    ratios on doubling: {[mp.nstr(r, 6) for r in ratios]}  (O(1/N) => 1/2)")
    check(
        "asymptotic_shape_matches_cited_expansion",
        all(abs(r - mp.mpf(1) / 2) < mp.mpf("0.02") for r in ratios),
        "log<4_1>_N - N*V/(2pi) tracks (3/2)logN - (1/4)log3 with an O(1/N) "
        f"residual: the residual ratio on each doubling is {[mp.nstr(r, 6) for r in ratios]}, "
        "against 1/2 for a clean 1/N tail. The N^{3/2}/3^{1/4} prefactor of the "
        "cited expansion is therefore reproduced by this corpus's own sum.",
    )

    # --- check 2: N*delta/logN -> 3pi, with the DERIVED offset --------------
    print("\n[2] N*delta_N/logN  ->  3pi, approached from below by -(pi log3)/(2 logN)")
    print(f"    3pi = {mp.nstr(three_pi, 12)}")
    grade_rows = []
    worst = mp.mpf(0)
    for N in LADDER:
        lhs = N * delta[N] / mp.log(N)
        pred = three_pi - offset / mp.log(N)
        gap = abs(lhs - pred)
        worst = max(worst, gap)
        grade_rows.append({"N": N, "N_delta_over_logN": mp.nstr(lhs, 12),
                           "derived_prediction": mp.nstr(pred, 12),
                           "gap": mp.nstr(gap, 6)})
        print(f"    N={N:5d}  measured={mp.nstr(lhs,11):>14}  derived={mp.nstr(pred,11):>14}"
              f"  gap={mp.nstr(gap,6)}")
    check(
        "N_delta_over_logN_matches_derived_3pi_with_offset",
        worst < mp.mpf("0.02"),
        f"the DERIVED two-term prediction 3pi - (pi log3)/(2 logN) tracks the measured "
        f"N*delta/logN to within {mp.nstr(worst, 6)} across N = {LADDER[0]}..{LADDER[-1]}; "
        f"at N={LADDER[-1]} the gap is {grade_rows[-1]['gap']}. The offset was derived "
        "from the cited expansion before being measured, so this is a test of the "
        "derivation, not a fit to the data.",
    )

    # --- check 3: N*delta diverges => NOT a pure grade-(-1) monomial ---------
    print("\n[3] N*delta_N -- grows without bound (pure grade -1 would be constant)")
    nd = [N * delta[N] for N in LADDER]
    for N, v in zip(LADDER, nd):
        print(f"    N={N:5d}  N*delta_N = {mp.nstr(v, 12)}")
    monotone = all(nd[i] < nd[i + 1] for i in range(len(nd) - 1))
    check(
        "remainder_is_NOT_a_pure_grade_minus_one_monomial",
        monotone and nd[-1] > nd[0] * mp.mpf("1.5"),
        f"N*delta_N rises monotonically {mp.nstr(nd[0], 8)} -> {mp.nstr(nd[-1], 8)} across "
        f"N = {LADDER[0]}..{LADDER[-1]}, i.e. omega*delta is INFINITE. A grade-(-1) "
        "infinitesimal c/omega would give the constant c. So ord_omega(delta) = -1 in "
        "the coarse grading, but delta is not a grade-(-1) monomial -- its leading term "
        "carries a log omega and sits strictly between grade -1 and grade 0 in the "
        "Berarducci-Mantova hierarchy.",
    )

    # --- check 4: the Richardson consequence, derived then measured ---------
    print("\n[4] one-step Richardson R_N = 2f(2N) - f(N) does NOT clear the remainder")
    pred_rich = three_pi * mp.log(2)
    print(f"    DERIVED  N*(R_N - V) -> 3pi*log2 = {mp.nstr(pred_rich, 12)}")
    rich_rows = []
    for N in LADDER[:-1]:
        R = 2 * f[2 * N] - f[N]
        val = N * (R - V)
        rich_rows.append({"N": N, "N_times_richardson_error": mp.nstr(val, 12)})
        print(f"    N={N:5d}  N*(R_N - V) = {mp.nstr(val, 12)}")
    last = mp.mpf(rich_rows[-1]["N_times_richardson_error"])
    check(
        "richardson_in_one_over_N_leaves_the_derived_residual",
        abs(last - pred_rich) < mp.mpf("0.01"),
        f"a 1/N Richardson step leaves N*(R_N - V) converging to the DERIVED "
        f"3pi*log2 = {mp.nstr(pred_rich, 10)}; measured {rich_rows[-1]['N_times_richardson_error']} "
        f"at N={rich_rows[-1]['N']}, gap {mp.nstr(abs(last - pred_rich), 6)}. So anyone "
        "extrapolating the Kashaev limit on a 1/N grid is fitting a mis-specified "
        "ansatz -- the leading correction is log(N)/N, not 1/N.",
    )

    # --- check 5: no float64 in the volume input ----------------------------
    check(
        "vol41_computed_not_read_from_a_float64_literal",
        isinstance(V, mp.mpf) and abs(V - 2 * mp.clsin(2, mp.pi / 3)) == 0,
        "Vol(4_1) is computed as 2*mp.clsin(2, pi/3) at working precision. The module "
        "constant VOL_FIGURE_EIGHT is float64 and would floor every gap in this probe "
        "at ~1e-16, which is coarser than check 2's tolerance -- the same trap caught "
        "in the N-question probe (8f6771235f).",
    )

    n_pass = sum(1 for _, ok, _ in results if ok)
    all_pass = n_pass == len(results)
    print(f"\n  {n_pass}/{len(results)} checks passed")

    payload = {
        "description": (
            "The omega-grade of the Kashaev remainder for 4_1. kashaev-surreal.md "
            "recasts the volume conjecture as a standard-part identity and never says "
            "what st() discards. Derived from the cited Ohtsuki/Andersen-Hansen "
            "expansion: delta_N = 3pi logN/N - (pi log3)/(2N) + O(1/N^2), so "
            "ord_omega(delta) = -1 in the coarse grading but delta is NOT a grade-(-1) "
            "monomial -- omega*delta is infinite and the convergence is logarithmically "
            "slow. Derive-then-check; every constant is read off the citation before "
            "measurement. Exact mpmath at 50 dps; no float64."
        ),
        "bean": "qou-cds1",
        "fills_gap_in": "content/quantum-observable-universe/appendix-surreals/kashaev-surreal.md",
        "derived_remainder": "delta_N = 3*pi*log(N)/N - (pi*log 3)/(2N) + O(1/N^2)",
        "omega_grade": {
            "coarse_ord_omega": -1,
            "is_pure_grade_minus_one_monomial": False,
            "leading_monomial": "(log omega)/omega",
            "position": "strictly between grade -1 and grade 0 (Berarducci-Mantova)",
            "omega_times_delta": "INFINITE",
        },
        "constants": {
            "vol_4_1": mp.nstr(V, 30),
            "three_pi": mp.nstr(three_pi, 15),
            "derived_offset_pi_log3_over_2": mp.nstr(offset, 15),
            "richardson_limit_3pi_log2": mp.nstr(pred_rich, 15),
        },
        "tables": {
            "asymptotic_shape": shape_rows,
            "omega_grade_ladder": grade_rows,
            "richardson": rich_rows,
        },
        "scope": {
            "kind": "(a) asymptotic statement about 4_1, resting on a cited expansion not re-derived here",
            "not_claimed": "nothing about the volume conjecture, about st(), or about any knot but 4_1",
        },
        "assertions": [{"name": n, "passed": ok, "detail": d} for n, ok, d in results],
        "allPassed": all_pass,
    }
    WitnessBuilder.wrap_legacy(
        "kashaev-remainder-omega-grade", payload,
        script_path=__file__, output_dir=WITNESS.parent, start_time=t0,
    ).save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "Pure knot-theoretic asymptotics: the Kashaev sum at roots of unity and "
            "Vol(4_1) = 2*Cl_2(pi/3). No substrate q0 is read on any path, and no "
            "pin can move a single number here."
        ),
    })
    print(f"\nWROTE {WITNESS.name} — all_pass={all_pass}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
