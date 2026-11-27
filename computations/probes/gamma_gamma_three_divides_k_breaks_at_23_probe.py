#!/usr/bin/env python3
"""The `3 | k` pattern does NOT persist for all k. It breaks at k = 23 — and
the whole k-structure is one number, `theta/pi`.

## The question, and it is the file's own

`QOU/Mass/GammaGammaSelectionTen.lean` proves reading-3 feasibility on `H_3` is
`chi_k >= 0`, carries the Chebyshev closed forms to `k = 10`, and establishes
**`chi_k > 0  <=>  3 | k`** for `1 <= k <= 10`. Its §"What is NOT proved" names
the open item verbatim:

    "whether the `3 | k` pattern persists for all `k` — it is a statement about
     `cos(k*theta)` with `2 cos theta = -1 - h^2`, i.e. about `theta/pi`, which
     step 4 left open."

This answers it, and the answer is NO.

## The identification, checked rather than assumed

`chi_k = 2 cos(k*theta)` is the closed form the file's own remark points at, but
the file does not use it — it grinds a fresh Chebyshev polynomial per `k`, which
is why it stopped at ten. [A1] checks the identification against ALL FIVE
published closed forms `chi_6 .. chi_10` at 60 dps before anything is concluded
from it. They agree to ~1e-60. That check is the reason this file is allowed to
replace ten polynomial identities with one cosine.

## The answer

At the proton pin, `theta/pi = 0.674759090836824...`, which is **strictly above
2/3**. That single fact decides everything. Write `delta := theta - 2pi/3 > 0`
(measured `0.0254231003227` rad) and split on `k mod 3`; the `2pi/3` part is a
whole number of turns plus a fixed offset, so

    k = 3m      ->  chi_k = 2 cos(k*delta)
    k = 3m+1    ->  chi_k = 2 cos(2pi/3 + k*delta)
    k = 3m+2    ->  chi_k = 2 cos(4pi/3 + k*delta)

At `delta = 0` these are `+2, -1, -1`: the `3 | k` pattern, exactly. For
`delta > 0` the phase `k*delta` ACCUMULATES, and each branch crosses zero at its
own threshold:

    branch      feasible while / from        k threshold        first integer
    ----------  ---------------------------  -----------------  -------------
    k = 3m      k*delta <= pi/2              pi/(2 delta) = 61.79   k = 63 INFEASIBLE
    k = 3m+2    k*delta >= pi/6              pi/(6 delta) = 20.59   k = 23 FEASIBLE
    k = 3m+1    k*delta >= 5pi/6             5pi/(6 delta) = 102.97 k = 103 FEASIBLE

So the pattern holds for `1 <= k <= 22` and **fails first at k = 23**, which is
`2 mod 3` and has `chi_23 = +0.1222 > 0`. [A3] derives all three thresholds in
closed form and [A4] confirms them by direct scan — neither is quoted from the
other.

## WHAT THIS DOES NOT BREAK, and the distinction is the point

**The SELECTION of `k = 3` survives; only the CHARACTERISATION fails.**
`frobeniusSelected_borromean_ten` picks the minimum-cost feasible candidate, and
the cost is the word length `k`. Every feasible `k` other than 3 costs more than
3, whether it is `6`, `9`, or the newly-feasible `23`. So `k = 3` remains the
unique minimiser for candidates of ANY size — [A5] checks this to k = 400.

What is false for `k >= 23` is the file's summary line *"the survivors are the
powers of `V^3`"*. Past 22 the survivor set is strictly larger. A reader using
that line as a structural fact about which words are admissible — rather than as
a range-limited table — would be wrong.

## AND IT EXPLAINS THE NARROWING INTERVALS, which the file records as a puzzle

That file notes the `H_6` interval shrinking `1/10 -> 1/12 -> 1/18` and flags
that "`1 + 2 chi_8` changes sign at `x ~ 0.0581`" with "the pin `h^2 = 0.0437`
inside, with little room". The narrowing is not an artifact of proof technique
and it will not stop: `delta` is an increasing function of `x` with
`delta(0) = 0`, so the pattern survives to `k` only on an interval shrinking
like `1/k`. [A6] measures `delta(x)` and the implied `k_max(x)`.

The sharp consequence: **on any FIXED interval with `x > 0` the pattern breaks
at finite `k`**, and at the pin specifically it breaks at 23. Extending the
Chebyshev grind to `k = 11, 12, ...` would therefore have kept working for a
dozen more steps and then failed, with no warning from the method itself.

**And the file's own numbers are already at the boundary, exactly.** [A6]
measures `k_max(x)` — the largest `k` for which `3 | k <=> feasible` holds on
`(0, x]` — and at `x = 1/10`, which is precisely the Lean's `H_3` hypothesis
(`1 < q <= 23/20`), `k_max` is precisely **10**, the Lean's `k` range. That is
not luck and it is not slack: the endpoint of the interval is what sets the
bound, so `k <= 10` on `x <= 1/10` is TIGHT. Step 8 could not have taken `k` to
11 on that interval by any proof technique — it would have had to narrow the
interval first, which is exactly what the `H_6` side was already observed doing
(`1/10 -> 1/12 -> 1/18`).

## Scope

Scope-(b) for the negative — the invariant is `theta/pi > 2/3`, an exact
inequality at the pin, and the mechanism is the accumulation of `k*delta`. It
refutes "persists for all k". It does NOT refute the selection (see above), and
it says nothing about the `InterfaceBranching` hypothesis or the `H_6` side
beyond [A6]'s measurement.

Precision: mpmath at 60 dps end to end; `q_0` is the proton pin. `float` appears
nowhere. Emits no witness: the output is an argument (bean qou-pb1w).

Beans qou-ales (the selection programme), qou-99qc (the element question this
narrows).

-- Ref: [manuscript] folio/quantum-observable-universe/lean/QOU/Mass/GammaGammaSelectionTen.lean
-- Ref: [manuscript] computations/probes/gamma_gamma_selection_ten_probe.py
"""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[2]
for _p in ("tools/qou-substrate/python", "computations/substrate", "computations"):
    sys.path.insert(0, str(_ROOT / _p))

import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

DPS = 60
set_compute_dps(DPS)          # corpus convention, not a bare `mp.dps =`
TOL = mp.mpf("1e-45")

FAILURES: list[str] = []


def check(tag: str, ok: bool, msg: str) -> None:
    print(f"   [{tag}] {'PASS' if ok else 'FAIL'}  {msg}")
    if not ok:
        FAILURES.append(tag)


#: The published Chebyshev closed forms, transcribed from the Lean docstring.
#: `x = h^2`. These are what [A1] validates the cosine identification against.
CHI_POLY = {
    6:  lambda x: x**6 + 6*x**5 + 9*x**4 - 4*x**3 - 12*x**2 + 2,
    7:  lambda x: -x**7 - 7*x**6 - 14*x**5 + 21*x**3 + 7*x**2 - 7*x - 1,
    8:  lambda x: (x**8 + 8*x**7 + 20*x**6 + 8*x**5 - 30*x**4 - 24*x**3
                  + 12*x**2 + 8*x - 1),
    9:  lambda x: (-x**9 - 9*x**8 - 27*x**7 - 21*x**6 + 36*x**5 + 54*x**4
                  - 9*x**3 - 27*x**2 + 2),
    10: lambda x: (x**10 + 10*x**9 + 35*x**8 + 40*x**7 - 35*x**6 - 98*x**5
                   - 15*x**4 + 60*x**3 + 15*x**2 - 10*x - 1),
}


def theta_of(x):
    """`theta` with `2 cos theta = -1 - x`, on the principal branch."""
    return mp.acos(-(1 + x) / 2)


def main() -> int:
    q = Q_MP
    h = q - 1 / q
    x = h ** 2
    th = theta_of(x)
    delta = th - 2 * mp.pi / 3

    print("=" * 76)
    print("[A1] chi_k = 2 cos(k theta) -- checked against the FIVE published forms")
    print("=" * 76)
    print(f"   q_0    = {mp.nstr(q, 25)}")
    print(f"   h^2    = {mp.nstr(x, 25)}")
    print(f"   theta  = {mp.nstr(th, 25)}")
    worst = mp.mpf(0)
    for k in sorted(CHI_POLY):
        a = CHI_POLY[k](x)
        b = 2 * mp.cos(k * th)
        d = abs(a - b)
        worst = max(worst, d)
        print(f"   k={k:>2}  poly {mp.nstr(a, 20):>24}   2cos {mp.nstr(b, 20):>24}"
              f"   |diff| {mp.nstr(d, 3)}")
    check("A1", worst < TOL,
          f"identification holds on all five, worst |diff| = {mp.nstr(worst, 3)} "
          f"-- so one cosine replaces ten polynomial identities")

    print()
    print("=" * 76)
    print("[A2] theta/pi > 2/3 STRICTLY -- the one fact that decides everything")
    print("=" * 76)
    print(f"   theta/pi          = {mp.nstr(th / mp.pi, 25)}")
    print(f"   2/3               = {mp.nstr(mp.mpf(2) / 3, 25)}")
    print(f"   delta = theta-2pi/3 = {mp.nstr(delta, 22)} rad")
    check("A2", th / mp.pi > mp.mpf(2) / 3 and delta > 0,
          "theta/pi exceeds 2/3, so the phase k*delta ACCUMULATES with k and "
          "no pattern fixed at delta=0 can survive unboundedly")

    print()
    print("=" * 76)
    print("[A3] THE THREE THRESHOLDS, in closed form -- derived, not scanned")
    print("=" * 76)
    # k = 3m   : chi = 2cos(k d),          feasible while k d <= pi/2
    # k = 3m+1 : chi = 2cos(2pi/3 + k d),  feasible from  k d >= 5pi/6
    # k = 3m+2 : chi = 2cos(4pi/3 + k d),  feasible from  k d >= pi/6
    t0 = mp.pi / (2 * delta)
    t1 = 5 * mp.pi / (6 * delta)
    t2 = mp.pi / (6 * delta)

    def first_at_or_above(bound, residue):
        k = int(mp.floor(bound))
        while True:
            k += 1
            if k % 3 == residue and k >= bound:
                return k

    def first_above_strict(bound, residue):
        k = int(mp.floor(bound))
        while True:
            k += 1
            if k % 3 == residue and k > bound:
                return k

    k0 = first_above_strict(t0, 0)      # first 3|k that FAILS
    k1 = first_at_or_above(t1, 1)       # first k=3m+1 that PASSES
    k2 = first_at_or_above(t2, 2)       # first k=3m+2 that PASSES
    print(f"   k = 3m    feasible while k*delta <= pi/2   -> k <= {mp.nstr(t0, 8)}"
          f"   first FAILING multiple of 3 : {k0}")
    print(f"   k = 3m+2  feasible from  k*delta >= pi/6   -> k >= {mp.nstr(t2, 8)}"
          f"   first PASSING k=3m+2        : {k2}")
    print(f"   k = 3m+1  feasible from  k*delta >= 5pi/6  -> k >= {mp.nstr(t1, 8)}"
          f"   first PASSING k=3m+1        : {k1}")
    check("A3", (k0, k1, k2) == (63, 103, 23),
          f"closed-form thresholds give (63, 103, 23) for the three branches")

    print()
    print("=" * 76)
    print("[A4] DIRECT SCAN -- independent of [A3], and it must agree")
    print("=" * 76)
    scan_div_fail = None
    scan_nondiv_pass = None
    kmax_pattern = None
    for k in range(1, 401):
        feas = (2 * mp.cos(k * th)) >= 0
        div3 = (k % 3 == 0)
        if div3 and not feas and scan_div_fail is None:
            scan_div_fail = k
        if (not div3) and feas and scan_nondiv_pass is None:
            scan_nondiv_pass = k
        if div3 != feas and kmax_pattern is None:
            kmax_pattern = k - 1
    print(f"   first  3|k   INFEASIBLE : k = {scan_div_fail}"
          f"   (chi = {mp.nstr(2*mp.cos(scan_div_fail*th), 12)})")
    print(f"   first  3 nmid k FEASIBLE: k = {scan_nondiv_pass}"
          f"   (chi = {mp.nstr(2*mp.cos(scan_nondiv_pass*th), 12)})")
    print(f"   '3|k <=> feasible' holds for ALL 1 <= k <= {kmax_pattern}, "
          f"and FAILS at k = {kmax_pattern + 1}")
    check("A4a", (scan_div_fail, scan_nondiv_pass) == (k0, k2),
          "scan reproduces the closed-form thresholds exactly")
    check("A4b", kmax_pattern == 22,
          "the pattern holds to k = 22 and breaks at k = 23 -- so the Lean's "
          "k <= 10 range was safe, with 12 to spare, and NOT extendable forever")

    print()
    print("=" * 76)
    print("[A5] THE SELECTION SURVIVES -- only the CHARACTERISATION fails")
    print("=" * 76)
    feasible = [k for k in range(1, 401) if (2 * mp.cos(k * th)) >= 0]
    cheapest = min(feasible)                       # cost = word length = k
    extra = [k for k in feasible if k % 3 != 0]
    print(f"   feasible k <= 400   : {len(feasible)} of 400")
    print(f"   of those, NOT 3|k   : {len(extra)}  first few {extra[:6]}")
    print(f"   cheapest feasible k : {cheapest}   (cost is the word length)")
    check("A5", cheapest == 3,
          "k = 3 is still the unique minimum-cost feasible candidate out to "
          "k = 400, so `frobeniusSelected_borromean` is NOT threatened -- what "
          "fails is only the claim that the survivors ARE the powers of V^3")

    print()
    print("=" * 76)
    print("[A6] WHY THE INTERVALS KEEP NARROWING -- delta(x) is increasing")
    print("=" * 76)
    print("   The Lean records H_6 intervals shrinking 1/10 -> 1/12 -> 1/18 and")
    print("   flags the pin sitting inside 'with little room'. That is forced:")
    print()
    print(f"   {'x = h^2':>12} {'delta (rad)':>16} {'k_max (pattern holds)':>24}")
    prev = None
    mono = True
    for xs in ["1/1000", "1/200", "1/100", "1/50", "1/20", "1/10"]:
        xv = mp.mpf(mp.mpf(xs.split("/")[0]) / mp.mpf(xs.split("/")[1]))
        dv = theta_of(xv) - 2 * mp.pi / 3
        kk = None
        for k in range(1, 2000):
            if ((k % 3 == 0) != ((2 * mp.cos(k * theta_of(xv))) >= 0)):
                kk = k - 1
                break
        print(f"   {xs:>12} {mp.nstr(dv, 10):>16} {kk if kk else '>1999':>24}")
        if prev is not None and not (dv > prev):
            mono = False
        prev = dv
    print()
    print(f"   at the pin x = {mp.nstr(x, 12)}: delta = {mp.nstr(delta, 10)}, "
          f"k_max = 22")
    print()
    print("   NOTE the x = 1/10 row: k_max is EXACTLY 10, and 0 < x <= 1/10 is")
    print("   precisely the Lean's H_3 hypothesis (1 < q <= 23/20) while k <= 10")
    print("   is precisely its k range. So that bound is TIGHT, not slack: step 8")
    print("   could not reach k = 11 on that interval by ANY proof technique --")
    print("   it would have to narrow the interval first, which is what the H_6")
    print("   side was already seen doing (1/10 -> 1/12 -> 1/18).")
    check("A6", mono,
          "delta increases with x, so k_max ~ 1/delta shrinks -- the interval "
          "must narrow as k grows, and on any fixed x > 0 the pattern breaks "
          "at finite k")

    print()
    print("=" * 76)
    print("[A7] THE LEAN'S HYPOTHESES HOLD AT THE WITNESS k = 23")
    print("=" * 76)
    # QOU.Mass.ThreeDividesKBreaks.pattern_fails_at_residue_two takes
    #   m : N,  pi/6 <= (3m+2)*delta,  (3m+2)*delta <= 5pi/6
    # and concludes  not (3 | 3m+2)  and  chi_(3m+2) >= 0.
    # k = 23 = 3*7 + 2, so m = 7. Checking BOTH bounds explicitly: the lower one
    # is what [A3] derives, the upper one is not, and the Lean needs both.
    m_w = 7
    k_w = 3 * m_w + 2
    phase = k_w * delta
    lo, hi = mp.pi / 6, 5 * mp.pi / 6
    print(f"   m = {m_w}, k = 3m+2 = {k_w}")
    print(f"   pi/6      = {mp.nstr(lo, 18)}")
    print(f"   k * delta = {mp.nstr(phase, 18)}   <- the accumulated phase")
    print(f"   5pi/6     = {mp.nstr(hi, 18)}")
    print(f"   chi_{k_w}    = {mp.nstr(2 * mp.cos(k_w * th), 18)}")
    check("A7", k_w == 23 and lo <= phase <= hi
          and (2 * mp.cos(k_w * th)) >= 0 and k_w % 3 != 0,
          "both Lean hypotheses hold at m = 7, so `pattern_fails_at_residue_two` "
          "applies and the refutation is complete as a Lean/probe pair")

    print()
    print("=" * 76)
    print("VERDICT" if not FAILURES else "VERDICT -- NOT ESTABLISHED, see failures")
    print("=" * 76)
    if FAILURES:
        print("   An assertion failed; the argument below is NOT established by")
        print("   this run. Read the failure, not the verdict.")
        print()
    print("   The `3 | k` pattern does NOT persist for all k. It holds exactly")
    print("   for 1 <= k <= 22 and breaks at k = 23 (chi_23 = +0.1222 > 0,")
    print("   23 = 2 mod 3). The mechanism is theta/pi = 0.6747... > 2/3, so")
    print("   the phase k*delta accumulates and each residue class crosses its")
    print("   own threshold: 23, 63, 103.")
    print()
    print("   The SELECTION of k = 3 is untouched -- it is still the unique")
    print("   cheapest feasible candidate. What is false past k = 22 is the")
    print("   summary claim that the survivors ARE the powers of V^3.")
    print()
    print("   SCOPE (b), invariant: theta/pi > 2/3 at the pin.")

    print()
    if FAILURES:
        print(f"FAILED: {', '.join(FAILURES)}")
        return 1
    print("All assertions passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
