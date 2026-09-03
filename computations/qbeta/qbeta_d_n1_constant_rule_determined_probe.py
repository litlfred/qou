#!/usr/bin/env python3
"""qou-cds1 entry 13 — K(delta) is NOT free in this arc: it is fixed by entry 2's rule.

Entry 10c settled N=1 uniqueness in the negative against three conditions --
(a) bar-invariance, (b) the C-frame limit, (c) log-separability -- which force
the phase shift c(delta) = delta/2 and leave the constant K(delta) free subject
only to K(0) = 1. Entry 12 then showed bar-parity is VACUOUS on K, because
delta = h^2/2 is bar-invariant. Read together those two entries suggest a 7656x
residual with nothing in the arc to close it.

THAT READING IS WRONG, and this probe says why. Entry 10 did not obtain the
midpoint factor M by searching the space of functions satisfying (a)+(b)+(c).
It obtained M by APPLYING A RULE the arc had already established one slot over:

    entry 2:   offset      :=  bar-midpoint of Vhat
    entry 10:  N=1 factor  :=  bar-midpoint of cos(alpha)

and the arithmetic bar-midpoint of cos(a_D) is not merely SOME function meeting
(a)+(b)+(c) -- it is a single determinate object,

    M = (cos(a_D) + cos(delta - a_D))/2 = cos(a_D - delta/2) * cos(delta/2),

whose constant factor is cos(delta/2), not 1. So K == 1 is not an alternative
the arc admits; it is what you get by DISCARDING the rule and keeping only the
three weaker conditions the rule happens to satisfy. K is free relative to
(a)+(b)+(c). It is not free relative to what the arc has established.

WHERE THE RULE'S AUTHORITY COMES FROM, AND WHERE IT DOES NOT. At the OFFSET
slot the rule is non-vacuous and independently checked: it reproduces convention
C's known offset 1 (as cosh(0)) and C's known alpha exactly, rather than
assuming them (entry 2). At the N=1 slot the same rule is VACUOUS under C --
alpha_C is bar-odd and cosine is even, so the C-frame N=1 factor is already its
own bar-midpoint -- so the N=1 application gets NO independent confirmation from
the C limit. It inherits its authority entirely from the offset slot.

STATUS, stated precisely because the distinction is what decides whether L2 may
use it: K = cos(delta/2) is RULE-DETERMINED AND SLOT-UNTESTED. That is strictly
stronger than "free" and strictly weaker than "derived". It is NOT a fit --
nothing was inverted against Q_beta, and the rule was fixed before this slot was
considered.

WHAT WOULD SETTLE IT: a third slot where the bar-midpoint rule is non-vacuous
under C, so the rule can be tested somewhere other than where it was built.
This probe does not find one; it states the requirement.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import sympy as sp

_results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    _results.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name} — {detail}")


def main() -> int:
    a, d = sp.symbols("a delta", real=True)

    print("=" * 72)
    print("  qou-cds1 entry 13 — K is rule-determined, not free")
    print("=" * 72)

    # --- the rule, applied at the N=1 slot -------------------------------
    # Under D, bar(a_D) = delta - a_D (entry 6: the defect is delta = h^2/2).
    bar_cos = sp.cos(d - a)
    M = (sp.cos(a) + bar_cos) / 2
    factored = sp.cos(a - d / 2) * sp.cos(d / 2)

    print("\n-- the arithmetic bar-midpoint is ONE determinate object")
    check("midpoint_factors_as_shift_times_constant",
          sp.simplify(sp.expand_trig(M - factored)) == 0,
          "(cos a + cos(delta - a))/2 = cos(a - delta/2) * cos(delta/2), exactly")
    check("its_constant_is_cos_delta_over_2_not_one",
          sp.simplify(sp.cos(d / 2) - 1) != 0,
          "K = cos(delta/2); K == 1 requires DISCARDING the rule, not choosing within it")

    # --- K == 1 also satisfies (a)+(b)+(c): the conditions are weaker -----
    K1 = sp.cos(a - d / 2)
    print("\n-- and K == 1 does satisfy the three conditions, which is exactly the point")
    check("K_equals_one_is_bar_invariant_too",
          sp.simplify(sp.expand_trig(K1.subs(a, d - a) - K1)) == 0,
          "so (a)+(b)+(c) cannot separate them — they are WEAKER than the rule")
    check("but_K_equals_one_is_NOT_the_bar_midpoint",
          sp.simplify(sp.expand_trig(K1 - M)) != 0,
          "cos(a - delta/2) is not (cos a + cos(delta - a))/2 unless delta = 0")

    # --- why the C limit gives the N=1 slot no evidence -------------------
    print("\n-- the rule's C-limit check at THIS slot is vacuous, so it tests nothing here")
    aC = sp.Symbol("a_C", real=True)          # bar-odd under C: bar(a_C) = -a_C
    midpoint_C = (sp.cos(aC) + sp.cos(-aC)) / 2
    check("C_frame_N1_factor_is_already_its_own_bar_midpoint",
          sp.simplify(midpoint_C - sp.cos(aC)) == 0,
          "cosine is even and a_C is bar-odd, so the rule is an identity under C")
    check("so_delta_zero_is_the_only_C_datum_and_it_is_K_of_zero_equals_one",
          sp.simplify(sp.cos(d / 2).subs(d, 0) - 1) == 0,
          "K(0) = 1 is ALL the C limit says — it cannot discriminate K at delta != 0")

    n_pass = sum(1 for _, ok, _ in _results if ok)
    print("\n" + "=" * 72)
    print(f"  {n_pass}/{len(_results)} assertions passed")
    print("  K = cos(delta/2) is RULE-DETERMINED AND SLOT-UNTESTED: fixed by the")
    print("  same bar-midpoint rule entry 2 established and validated at the OFFSET")
    print("  slot (where it re-derives C's offset 1 = cosh(0) and C's alpha), but")
    print("  receiving no independent confirmation at the N=1 slot, where the C")
    print("  limit is vacuous. Stronger than 'free', weaker than 'derived', and")
    print("  NOT a fit — nothing was inverted against Q_beta.")
    print("  Settling it needs a THIRD slot where the rule is non-vacuous under C.")
    print("  No c_k is produced; Q_beta stays at 1279 ppb. Scope (a).")
    print("=" * 72)
    return 0 if n_pass == len(_results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
