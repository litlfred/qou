#!/usr/bin/env python3
"""qou-cds1 entry 14 — the third-slot test entry 13 asked for. The rule FAILS it.

Entry 13 argued that K(delta) = cos(delta/2) is not free but RULE-DETERMINED:
fixed by entry 2's `X := bar-midpoint of X_naive`, applied one slot over. It
noted that the rule's C-limit check at the N=1 slot is vacuous, so the N=1
application inherits all its authority from the offset slot, and it named the
test that would settle the matter -- A THIRD SLOT WHERE THE RULE IS NON-VACUOUS
UNDER C. This probe finds one and runs it.

THE THIRD SLOT: the N=2 ladder factor, `1 - u^2`, whose u^2 coefficient is the
corpus's structural `c_2 = -1` (no fit, no CODATA, no q_0). Under C the ladder
variable u is bar-COVARIANT (bar(u)/u = q^2), so the rule is non-vacuous there,
exactly as required.

THE RESULT: the rule does not reproduce c_2. Its bar-midpoint has u^2
coefficient -(q^4 + 1)/2, which at the proton pin is -1.25898 against the known
-1 -- 25.90 % off. The rule PASSES at the offset slot (entry 2: it re-derives
C's offset 1 = cosh(0) and C's alpha) and FAILS here.

    slot            C-frame        verdict
    offset          non-vacuous    PASSES  (entry 2)
    N=1 factor      vacuous        no evidence available
    N=2 factor      non-vacuous    FAILS, 25.90 %

SO ENTRY 13'S STATUS CLAIM IS WITHDRAWN. It leaned on an implicit universality
of the rule; that universality is now measured false. K = cos(delta/2) is
rule-TRANSPORTED from a slot where the rule works, to a slot where it cannot be
tested, past a slot where it demonstrably fails.

THE DEFENCE, AND WHAT IT COSTS. One can read the rule not as "apply everywhere"
but as "re-express in bar-invariant form", vacuous wherever that is already
done. Under D the N=2 slot IS vacuous (X = u*Vhat is bar-invariant, verified
here rather than assumed), so on that reading the C-frame N=2 test is outside
the rule's remit. But entry 2's validation is a C-frame check of exactly the
same kind. So the dichotomy is sharp and it has no comfortable branch:

  * the C-frame check is legitimate  =>  the rule FAILS at N=2;
  * it is not                        =>  entry 2's validation goes too, and the
                                         rule is validated NOWHERE.

Either way K is not rule-determined in entry 13's strong sense, and entry 12's
7656x freedom is reinstated as live.

ALSO VERIFIED HERE, because entry 11 asserted it rather than computing it:
Vhat = z*h + 1 gives Vhat_D = (q^4+1)/(q^2+1) = 1.12808874411 (matching the
value the arc records), bar(Vhat_D)/Vhat_D = q^-2 against bar(u)/u = q^2, hence
bar(X)/X = 1 exactly. Entry 4 is confirmed. My first pass at this probe guessed
Vhat = q^2 from the offset cosh(2 log q) and got bar(X)/X = q^-2, i.e. appeared
to REFUTE entry 4 -- a wrong Vhat, not a wrong entry.

Scope (a). No c_k produced, proposed or fitted; Q_beta stays at 1279 ppb.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import sympy as sp

Q0 = "1.1099785827513808075916690956107688798744991218736"
_results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    _results.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name} — {detail}")


def main() -> int:
    q = sp.symbols("q", positive=True)
    bar = lambda e: sp.cancel(sp.simplify(e.subs(q, 1 / q)))
    q0 = sp.Rational(Q0)

    h = q - 1 / q
    zD = q**3 / (q**2 + 1)
    u = (q - 1) ** 2 * sp.sqrt(q**4 + q**2 + 1) / (q**4 + q**2)
    VD = sp.cancel(zD * h + 1)
    X = sp.simplify(u * VD)

    print("=" * 72)
    print("  qou-cds1 entry 14 — the third slot exists, and the rule fails it")
    print("=" * 72)

    print("\n-- first, entry 4 verified rather than asserted (entry 11 only asserted it)")
    check("Vhat_D_is_z_h_plus_one",
          sp.simplify(VD - (q**4 + 1) / (q**2 + 1)) == 0,
          f"Vhat_D = (q^4+1)/(q^2+1) = {sp.N(VD.subs(q, q0), 12)}, matching the arc's 1.1280887")
    check("u_and_Vhat_carry_opposite_bar_weights",
          sp.simplify(sp.cancel(bar(u) / u) - q**2) == 0
          and sp.simplify(sp.cancel(bar(VD) / VD) - q ** (-2)) == 0,
          "bar(u)/u = q^2 and bar(Vhat_D)/Vhat_D = q^-2")
    check("X_equals_u_Vhat_is_bar_invariant",
          sp.simplify(sp.cancel(bar(X) / X) - 1) == 0,
          "bar(X)/X = 1 exactly — entry 4 confirmed by computation")

    print("\n-- the third slot: N=2 ladder factor under C, where u is bar-COVARIANT")
    N2C = 1 - u**2
    midC = sp.simplify((N2C + bar(N2C)) / 2)
    coeff = sp.simplify((midC - 1) / u**2)
    at_q0 = sp.N(coeff.subs(q, q0), 15)
    off = sp.N(sp.Abs(at_q0 + 1) * 100, 6)
    check("rule_is_NON_VACUOUS_at_the_N2_slot_under_C",
          sp.simplify(midC - N2C) != 0,
          "so this slot CAN test the rule, which is what entry 13 asked for")
    check("rule_does_NOT_reproduce_the_structural_c2",
          sp.simplify(coeff + 1) != 0,
          f"bar-midpoint gives u^2 coefficient -(q^4+1)/2 = {at_q0} at q0, not -1 — {off} % off")

    print("\n-- and under D the same slot is vacuous, so it offers no rescue there")
    N2D = 1 - X**2
    check("rule_is_vacuous_at_the_N2_slot_under_D",
          sp.simplify(sp.simplify((N2D + bar(N2D)) / 2) - N2D) == 0,
          "X is bar-invariant, so the rule says nothing at N=2 in the target frame")

    n_pass = sum(1 for _, ok, _ in _results if ok)
    print("\n" + "=" * 72)
    print(f"  {n_pass}/{len(_results)} assertions passed")
    print("  ENTRY 13'S STATUS CLAIM IS WITHDRAWN. The bar-midpoint rule passes")
    print("  at the offset slot and FAILS at the N=2 slot by 25.90 %, so it does")
    print("  not transport universally — which is the only thing entry 13's")
    print("  'rule-determined' rested on. K = cos(delta/2) is rule-TRANSPORTED")
    print("  past a slot where the rule demonstrably fails, and entry 12's 7656x")
    print("  freedom is reinstated as live.")
    print("  Scope (a). No c_k produced; Q_beta stays at 1279 ppb.")
    print("=" * 72)
    return 0 if n_pass == len(_results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
