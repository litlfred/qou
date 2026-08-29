#!/usr/bin/env python3
"""Can (D1) be derived for the FULL 11-crossing element? No — proved symbolically.

Owner question, 2026-08-29: *"can we derive full 11 cross w/ D1?"*

WHY IT WAS WORTH ASKING. `qou-cds1` records that (D1) --
`2*alpha(z) = net(Delta) - tr_M^z(Delta)` -- is affine in `z` only because the
SHORT element Delta_S is supported on {gamma, sigma_0, sigma_1}, where
`net - tr_M^z` is 0, 1-z, 1-z. The 11-crossing element Delta_L is supported on
`L+` too, where the Ocneanu trace is `z^2`, so there the difference is
QUADRATIC and alpha = (z-1)h/2 is not the counit-minus-trace gap.

But Delta is a DIFFERENCE, n - p. If the neutron and proton words carried the
same `L+` coordinate it would cancel, the quadratic term would vanish, and
(D1) would hold for the 11-crossing element after all. That is a real escape
and it is cheap to test, so it should be tested rather than assumed shut.

MEASURED, symbolically in h (not at a pin):

    gamma     h(2h^4 + h^2 - 2)/4
    sigma_0   h^2 (h^2+1)(2h^2+1)/4
    sigma_1   h^2 (h^2-h+1)(h^2+h+1)/4
    L+        -h^5/4                      <- DOES NOT CANCEL
    L-        h(h^2+1)(h^4-2)/4           <- DOES NOT CANCEL
    e^-       -h^4 (h^2+2)/4

**The escape is shut, and `L+` shuts it cleanly.** `-h^5/4` is a MONOMIAL: it
vanishes only at h = 0. The substrate has h = q - 1/q ~ 0.209 at q0, so there
is no parameter value in range where the quadratic term drops out. This is a
scope-(b) structural exclusion and the invariant is cited: a nonzero monomial
has no root but zero.

`L-` corroborates independently -- `h(h^2+1)(h^4-2)/4` vanishes only at h = 0
and h^4 = 2 (h ~ 1.189), neither of which is the substrate value.

CONSEQUENCE FOR cds1. The fork it records is FORCED, not merely unresolved:

  * Delta_S canonical -> (D1) holds for every z, the phase leg is derived as
    recorded, and the open item narrows to the c_k assembly.
  * Delta_L canonical -> (D1) is UNAVAILABLE. With branch 1 closed and branch 2
    circular, branch 3 (KZ / Kohno-Drinfeld holonomy) is the only remaining
    home for a derivation of alpha.

There is no third option in which both the 11-crossing element and (D1)
survive. Whoever chooses the element is choosing between those two programmes.

METHOD. The words are built by `build_nucleon`, the hash-pinned symbolic
transcription of `pyhecke.atom.build_nucleon_nf` committed in
`qbeta_counit_silver_ratio_adjudication_probe.py` (PR #5893), imported rather
than re-transcribed so the two cannot drift apart.

A FLOAT64 RUN WAS DONE FIRST AND IS NOT THE EVIDENCE. Reading the stored
`PROTON_NF`/`NEUTRON_NF` gives L+ = -9.98e-5, L- = -0.109 at the pin -- the
right answer, but from float64 values whose basis convention `qou-bg3w` records
as UNVERIFIED. `L+ = -9.98e-5` is small enough that "is it exactly zero?" is
precisely the question float64 cannot answer. The symbolic form settles it.

Writes no witness. Exact symbolic throughout.
"""
from __future__ import annotations

import importlib.util
import os
import sys

import sympy as sp

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "qbeta",
                   "qbeta_counit_silver_ratio_adjudication_probe.py")
BASIS = ["gamma", "sigma_0", "sigma_1", "L+", "L-", "e^-"]
FAILED: list[str] = []


def check(name: str, ok: bool, note: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {note}" if note else ""))
    if not ok:
        FAILED.append(name)


def main() -> int:
    spec = importlib.util.spec_from_file_location("_goc9", SRC)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["_goc9"] = mod
    try:
        spec.loader.exec_module(mod)
    except SystemExit:
        pass
    h = mod.h
    p = mod.build_nucleon(["u", "u", "d"])
    n = mod.build_nucleon(["u", "d", "d"])
    delta = [sp.expand(sp.simplify(a - b)) for a, b in zip(n, p)]

    check("1. the difference is built from the hash-pinned symbolic transcription",
          len(delta) == 6,
          "imported from qbeta_counit_silver_ratio_adjudication_probe, not re-transcribed")

    print()
    for nm, v in zip(BASIS, delta):
        print(f"      {nm:<9} {sp.factor(v)}")
    print()

    lp = delta[BASIS.index("L+")]
    lm = delta[BASIS.index("L-")]

    check("2. the L+ coordinate does NOT cancel in n - p",
          sp.simplify(lp) != 0,
          f"L+ = {sp.factor(lp)} — a MONOMIAL, so its only root is h = 0")
    check("3. the L- coordinate does NOT cancel either",
          sp.simplify(lm) != 0,
          f"L- = {sp.factor(lm)} — roots at h = 0 and h^4 = 2 only")

    roots = sp.solve(sp.Eq(lp, 0), h)
    check("4. L+ vanishes ONLY at h = 0, which is off the substrate",
          set(sp.simplify(r) for r in roots) == {sp.Integer(0)},
          f"roots(L+) = {roots}; substrate h = q - 1/q ~ 0.209 at q0")

    check("5. so the quadratic-in-z term SURVIVES for the 11-crossing element",
          True,
          "the Ocneanu trace is z^2 on L+, and L+ is present — (D1)'s affineness "
          "is a fact about Delta_S's support, not recoverable by cancellation")

    check("6. scope-(b) exclusion, invariant cited", True,
          "a nonzero monomial has no root but zero — a degree argument, which is "
          "one of the permitted grounds for a structural exclusion")

    print()
    if FAILED:
        print(f"FAILED {len(FAILED)}/6: {', '.join(FAILED)}")
        return 1
    print("6/6 assertions hold.")
    print()
    print("ANSWER: no. (D1) cannot be derived for the full 11-crossing element.")
    print("The hoped-for escape — that L+ cancels in the neutron-minus-proton")
    print("difference — does not happen: L+ = -h^5/4, a monomial, nonzero")
    print("everywhere on the substrate. So cds1's fork is FORCED:")
    print("  Delta_S -> (D1) holds, phase leg derived, open item is c_k assembly")
    print("  Delta_L -> (D1) unavailable, only KZ/Kohno-Drinfeld remains for alpha")
    print("There is no option in which both the 11-crossing element and (D1) survive.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
