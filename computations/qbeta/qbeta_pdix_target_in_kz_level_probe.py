#!/usr/bin/env python3
"""qou-pdix 5b — the target slope expressed in the KZ connection's OWN variable.

WHY. `qou-pdix`'s surviving route is 5b, the OPEN-PATH holonomy of `qou-d0qq`'s
KZ connection (the monodromy half is excluded by the rationality invariant — see
`qbeta_pdix_step2_holonomy_slope_probe.py` and the bean). The ladder's target is
stated in `q`:

    P(q0)      = 1.997259194490263      (+/- 5.7e-7 relative)
    |P'/P|(q0) = 2.176                  (~4 figures)

But a holonomy of that connection is naturally a function of the LEVEL, not of
`q`. `qou-d0qq` fixes the level convention-free from the half-twist eigenvalue
ratio: `hbar = (2/(i*pi)) ln q`, purely imaginary at the real pin
(`hbar = -0.0664i`). So before computing any holonomy, convert the target.

RESULT. With `P = F(hbar)` the chain rule gives
`|d ln P/dq| = |d ln F/dhbar| * |dhbar/dq|`, and at the proton pin

    |hbar|            = 0.066425365618482
    |dhbar/dq|        = 0.5735423928537
    => |d ln F/dhbar| = 3.793965411          <-- an O(1) NUMBER

The whole bracket, in the same units:

    step-2 Laurent lw 2      0.0819
    step-2 Laurent lw 3      0.3911
    best declared basket     3.0273
    TARGET                   3.7940
    modular dual q~       1424.0065

WHAT THIS ADDS, AND IT IS NOT A NEW RATIO.  🛑 The conversion is multiplication
by a CONSTANT (`|dhbar/dq|` at a fixed `q0`), so **every ratio is unchanged** —
still 46x / 9.7x too flat, 1.25x at best, 375x too steep. Anyone reading the new
column as independent evidence is double-counting the same measurement. Said
explicitly because a units change that leaves ratios fixed is exactly the kind of
thing that gets re-quoted as a second confirmation.

What it DOES add is a statement about the carrier's SHAPE. In the connection's own
variable the required log-derivative is **O(1)** — not O(0.1), not O(10^3). For a
perturbative series `F = F0 (1 + a1*hbar + ...)` that reads `a1 ~ 3.794`. That is
the size of a Drinfeld-associator coefficient (the associator's entries are
multiple zeta values, O(1) rationals in `zeta(n)`), and it is NOT the size of
either a low-degree Laurent polynomial in `q` at `q0 ~ 1.11` or a
non-perturbative `exp(-1/t)`. So the bracket's qualitative conclusion —
"intermediate transcendental" — becomes a checkable target on the LEADING
COEFFICIENT of the open-path holonomy's `hbar`-expansion.

🛑 AND A NUMBER TO NOT GET EXCITED ABOUT. `a1 * |hbar| = 0.2520155`, which is
0.8 % from `1/4`. **This carries no information and must not be reported as a
finding.** `a1` is DEFINED by dividing the target by `|dhbar/dq|`, so
`a1 * |hbar|` is just the target restated in another arrangement; ANY target value
would produce some such product, and landing 0.8 % from a simple fraction is
unremarkable at that precision. Recorded here only so the next agent does not
rediscover it and read it as structure. This is the `S_leak` offset-genericity
lesson applied pre-emptively: a suggestive constant needs a genericity check, and
this one fails it trivially because the quantity is not independent of the target.

WHAT IS STILL OPEN. This is a restatement of the target, not a computation of the
holonomy. Computing the actual open-path holonomy of the KZ connection at
`hbar = -0.0664i` and reading off its leading coefficient is the next step, and it
is a real piece of work: `qou-d0qq`'s open remainder is the FRAMEWORK-side
connection (C1/C2/C3 scope-(b) dead; survivor C3' needs the deformation as an
INPUT), so what can be computed today is the KZ side alone, and any agreement
would be conditional on the `KZPullbackGenerators` interface rather than derived.

Bean: qou-pdix (stays OPEN). Consumers: none (probe). No witness by design; every
number carried as `mpf` per PROBES ARE NOT EXEMPT.
"""

import pathlib
import sys

import mpmath as mp

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path[:0] = [
    str(ROOT / p)
    for p in ("computations", "computations/substrate", "tools/qou-substrate/python")
]

from qou_substrate.constants import Q  # noqa: E402

mp.mp.dps = 50

SLOPE_TARGET = mp.mpf("2.176")
BRACKET = {
    "step-2 Laurent lw 2": mp.mpf("0.046958636"),
    "step-2 Laurent lw 3": mp.mpf("0.22430586"),
    "best declared basket": mp.mpf("1.7363"),
    "modular dual q~": mp.mpf("816.7280759"),
}

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")


def main() -> int:
    q = mp.mpf(str(Q))
    lnq = mp.log(q)

    # qou-d0qq: hbar = (2/(i pi)) ln q, purely imaginary at the real pin.
    hbar_mag = 2 * lnq / mp.pi
    dhbar_dq = 2 / (mp.pi * q)
    need = SLOPE_TARGET / dhbar_dq

    print(__doc__.split("\n")[0])
    print()
    print(f"q0        = {mp.nstr(q, 18)}")
    print(f"|hbar|    = {mp.nstr(hbar_mag, 16)}")
    print(f"|dhbar/dq|= {mp.nstr(dhbar_dq, 16)}")
    print()

    check(
        "|hbar| reproduces the level qou-d0qq records (-0.0664i)",
        abs(hbar_mag - mp.mpf("0.0664")) < mp.mpf("0.0001"),
        f"|hbar| = {mp.nstr(hbar_mag, 12)} vs the bean's 0.0664",
    )

    check(
        "the target in the KZ variable is O(1)",
        1 < need < 10,
        f"|d ln F/dhbar| = {mp.nstr(need, 10)} — neither O(0.1) (Laurent) nor "
        "O(10^3) (non-perturbative), so the carrier is a PERTURBATIVE series in "
        "hbar with an associator-sized leading coefficient",
    )

    print()
    print("  the bracket in hbar units:")
    for lbl, s in sorted(BRACKET.items(), key=lambda kv: kv[1]):
        print(f"     {lbl:<24}{mp.nstr(s / dhbar_dq, 8):>12}")
    print(f"     {'TARGET':<24}{mp.nstr(need, 8):>12}")

    # The conversion is a constant, so no ratio moves. Verify that explicitly.
    worst_ratio_q = SLOPE_TARGET / BRACKET["step-2 Laurent lw 2"]
    worst_ratio_h = need / (BRACKET["step-2 Laurent lw 2"] / dhbar_dq)
    check(
        "the unit change moves NO ratio — it is not independent evidence",
        abs(worst_ratio_q - worst_ratio_h) < mp.mpf("1e-30"),
        f"worst flat ratio is {mp.nstr(worst_ratio_q, 8)}x in q and "
        f"{mp.nstr(worst_ratio_h, 8)}x in hbar — identical, because the "
        "conversion is multiplication by a constant at fixed q0. Do not quote "
        "the hbar column as a second confirmation",
    )

    # The non-finding, recorded so it is not rediscovered as structure.
    prod = need * hbar_mag
    check(
        "a1*|hbar| ~ 1/4 is a RESTATEMENT of the target, not a finding",
        True,
        f"a1*|hbar| = {mp.nstr(prod, 10)}, {mp.nstr(abs(prod - mp.mpf('0.25')) / mp.mpf('0.25') * 100, 3)}% "
        "from 1/4 — but a1 is DEFINED by dividing the target, so this product is "
        "the target rearranged and carries no independent information. Fails the "
        "S_leak genericity test trivially",
    )

    npass = sum(1 for _, ok, _ in CHECKS if ok)
    ntot = len(CHECKS)
    print()
    print("=" * 70)
    print(f"VERDICT  {npass}/{ntot} checks pass")
    print()
    print("target in the KZ level variable   |d ln F/dhbar| = 3.793965411")
    print("what it buys                      a SHAPE constraint: a perturbative")
    print("                                  hbar-series with an O(1) (associator-")
    print("                                  sized) leading coefficient.")
    print("what it does NOT buy              any new ratio -- the conversion is a")
    print("                                  constant; every factor is unchanged.")
    print("qou-pdix                          STILL OPEN. The holonomy itself is")
    print("                                  not computed here.")
    print("=" * 70)
    return 0 if npass == ntot else 1


if __name__ == "__main__":
    raise SystemExit(main())
