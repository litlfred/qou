#!/usr/bin/env python3
"""Is the ladder phase holonomy-shaped?  A second-order test, and what discriminates.

Bean `qou-pdix`, branch 3 of the route-5 trichotomy.

## Why this test

`QOU.QBeta.EigenphaseCarrier` §3 establishes that a derivation of the ladder
phase `α` can only live in one place: an exponential/holonomy of an
independently-defined connection whose monodromy reproduces the Hecke braiding.
Branch 1 (`α` as a braid-word character) is excluded by rationality; branch 2
(`α` from an arbitrary matrix) is circular.

Before building such a connection, ask a cheap falsifiable question: **does `α`
even look like a holonomy angle?**

The Kohno–Drinfeld parametrisation fixes the scale.  The braiding is
`P·exp(ħt/2)` with `t` of eigenvalues `±1`, which matches the Hecke eigenvalues
`{q, −q⁻¹}` exactly when `q = e^{ħ/2}`, i.e. **`ħ = 2 ln q`**.  A holonomy angle
is then a multiple of `ħ`, i.e. of `ln q` — so the test is whether `α` agrees
with `c·ln q` for a *single* constant `c`.

**The scale is not free.**  `c` is fixed by the `O(t)` coefficient at `q = 1+t`.
Every higher order is then a genuine prediction that can fail.

## Result

    c·ln q  series:   t¹: c      t²: −c/2    t³: c/3

    α_C = (z_C−1)h/2  t¹: −1/2  ⇒ c = −1/2
                      t²: predicted 1/4    actual 1/4     MATCH
                      t³: predicted −1/6   actual −5/16   differ

    α_D = (z_D−1)h/2  t¹: −1/2  ⇒ c = −1/2
                      t²: predicted 1/4    actual 5/4     differ

So `α_C` is second-order consistent with a logarithmic (holonomy) form; `α_D` is
only first-order consistent.  **Neither IS a logarithm** — both fail at `t³`.

## What actually discriminates them — a structural criterion, not a coincidence

Expanding `α = (z−1)h/2` about `q = 1+t`, with `h = 2t − t² + …`:

    t¹ coefficient:  z(1) − 1        ⇒ log-match needs z(1) = 1/2
    t² coefficient:  1/4 + z′(1)     ⇒ log-match needs **z′(1) = 0**

Both conventions satisfy `z(1) = 1/2` (they agree at the classical point — see
`qbeta_zcd_classical_coincidence_probe.py`).  They differ on the derivative:

    z_C:  z′(1) = 0        z″(1) = −1/8
    z_D:  z′(1) = 1        z″(1) = 1/2

**`α` is second-order logarithmic exactly when the Markov parameter is
STATIONARY at the classical point.**  `z_C`'s only critical point on `q > 0` is
`q = 1`, and it is a *maximum*; `z_D` is not stationary there.  That is the whole
content of the second-order agreement, stated structurally.

## Scope — this is consistency, NOT a derivation

  * It does **not** derive `α`, in either convention.
  * It does **not** establish that the holonomy angle is `−ħ/4`.  The scale `c`
    was fixed from `O(t)`; what is tested is the *shape* at the next order.
  * The evidence is **one** successful prediction (`t²`).  Real — a generic
    function with the right value and first derivative need not have `t² = 1/4`
    — but modest, and `t³` fails, so `α_C` is not a logarithm either.
  * It is a **falsifiable target** for branch 3: a genuine KZ/Stokes holonomy
    should reproduce `α` through `t²` and may deviate at `t³`.  If a constructed
    holonomy misses at `t²`, the N=1 factor is wrong.

## Tension with the 2026-08-15 ruling, stated plainly

The ruling makes convention **D** canonical.  On this test the decay channel's
phase looks **C**-shaped: `α_C` passes the second-order holonomy check and `α_D`
fails it by a factor of 5.  This does not overturn the ruling — that is a
corpus-wide trace-convention decision, and this is one channel's phase — but it
does *deepen* an already-recorded tension: `QOU.QBeta.decayLadder_zC_threeRow_ne_zero`
already proves the C-frame ladder and the two-row forcing are mutually
exclusive.  Recorded, not resolved.

Exact symbolic ℚ throughout; the one numerical line is mpmath.  No float64.
"""
from __future__ import annotations

import sys

import mpmath as mp
import sympy as sp

q, t, c = sp.symbols("q t c")


def series_at_one(expr, n=7):
    return sp.series(expr.subs(q, 1 + t), t, 0, n).removeO().expand()


def main() -> int:
    failures: list[str] = []

    def check(name, ok, detail):
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
        if not ok:
            failures.append(name)

    h = q - 1 / q
    zC = sp.sqrt(q) / (1 + q)
    zD = q ** 3 / (q ** 2 + 1)
    aC = (zC - 1) * h / 2
    aD = (zD - 1) * h / 2

    print("Assertions (exact symbolic ℚ):")

    # 1. the KZ scale relation
    check(
        "1. q = e^{hbar/2} matches the Hecke eigenvalues, so hbar = 2 ln q",
        sp.simplify(sp.exp(2 * sp.log(q) / 2) - q) == 0,
        "braiding P*exp(hbar*t/2), t eigenvalues +-1 -> {e^{hbar/2}, -e^{-hbar/2}} = {q, -1/q}",
    )

    # 2-3. one-parameter log family; scale fixed at t^1, higher orders predicted
    logP = sp.Poly(series_at_one(c * sp.log(q)), t)
    for nm, a, expect_order in (("alpha_C", aC, 2), ("alpha_D", aD, 1)):
        P = sp.Poly(series_at_one(a), t)
        csol = sp.solve(sp.Eq(logP.coeff_monomial(t ** 1), P.coeff_monomial(t ** 1)), c)[0]
        agree = 1
        for k in range(2, 6):
            pred = sp.simplify(logP.coeff_monomial(t ** k).subs(c, csol))
            act = sp.simplify(P.coeff_monomial(t ** k))
            if sp.simplify(pred - act) == 0:
                agree = k
            else:
                break
        check(
            f"{'2' if nm=='alpha_C' else '3'}. {nm} agrees with c*ln(q) through t^{expect_order}",
            agree == expect_order,
            f"c fixed = {sp.nsimplify(csol)} from t^1; agreement runs to t^{agree}",
        )

    # 4. the structural discriminator: z'(1) = 0
    dC = sp.simplify(sp.diff(zC, q).subs(q, 1))
    dD = sp.simplify(sp.diff(zD, q).subs(q, 1))
    check(
        "4. the discriminator is z'(1): zero for C, nonzero for D",
        dC == 0 and dD != 0,
        f"z_C'(1) = {dC}, z_D'(1) = {dD} -- the t^2 coefficient of alpha is 1/4 + z'(1)",
    )

    # 5. z_C is stationary at q=1 and it is its MAXIMUM on q>0
    crit = sp.solve(sp.diff(zC, q), q)
    d2C = sp.simplify(sp.diff(zC, q, 2).subs(q, 1))
    check(
        "5. z_C's only critical point on q>0 is q=1, and it is a maximum",
        crit == [sp.Integer(1)] and d2C < 0,
        f"critical points {crit}; z_C''(1) = {d2C} < 0; z_C(1) = {sp.simplify(zC.subs(q,1))}",
    )

    # 6. neither alpha IS a logarithm -- both fail at t^3
    P_C = sp.Poly(series_at_one(aC), t)
    t3_C = sp.simplify(P_C.coeff_monomial(t ** 3))
    check(
        "6. alpha_C is NOT a logarithm -- t^3 differs",
        sp.simplify(t3_C - sp.Rational(-1, 6)) != 0,
        f"alpha_C t^3 = {sp.nsimplify(t3_C)} vs log's -1/6",
    )

    # 7. numerical size of the second-order agreement at the substrate
    mp.mp.dps = 30
    q0 = mp.mpf("1.1099785827513808")
    aC0 = (mp.sqrt(q0) / (1 + q0) - 1) * (q0 - 1 / q0) / 2
    log0 = -mp.log(q0) / 2
    rel = (log0 - aC0) / aC0
    check(
        "7. at q0 the log form sits within 0.5% of alpha_C",
        abs(rel) < mp.mpf("0.005"),
        f"alpha_C = {mp.nstr(aC0,12)}, -(ln q)/2 = {mp.nstr(log0,12)}, rel {mp.nstr(rel*100,5)}%",
    )

    print()
    if failures:
        print(f"FAILED {len(failures)}/7: {', '.join(failures)}")
        return 1
    print("7/7 assertions hold.")
    print()
    print("READING: alpha is second-order logarithmic exactly when the Markov")
    print("parameter is STATIONARY at the classical point. z_C is (q=1 is its")
    print("maximum on q>0); z_D is not. So the decay phase looks C-shaped on this")
    print("test. CONSISTENCY, not a derivation -- one predicted order, and t^3")
    print("fails for C too. Falsifiable target for branch 3: a real KZ/Stokes")
    print("holonomy should reproduce alpha through t^2.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
