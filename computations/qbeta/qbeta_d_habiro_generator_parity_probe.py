#!/usr/bin/env python3
"""
qou-cds1: the D-frame Habiro generator must be bar-INVARIANT, not bar-odd —
and c_2 = -1 discriminates the two expansion variables after all.

# Ref: content/quantum-observable-universe/lean/QOU/BraidKnot/QBetaHabiroGeneratorRigidity.lean
# Ref: .beans/qou-cds1--s1-science-re-derive-the-qbeta-ck-ladder-under-d-n.md

WHERE THIS CAME FROM. Asked where to look for a structural replacement for
`cos(alpha_eff)`, the corpus answers itself: AGENTS.md names the Q_beta Habiro
element as the permanent fix, and QBetaHabiroGeneratorRigidity.lean carries the
open class `QBetaSingleHabiroGenerator` (verified: NO instance). Its class
statement is parity-free — `exists rho, c_{k+1} = rho * c_k`. But its DOCSTRING
names the intended rho as "the categorical BAR-ODD ('sinh partner') Habiro
element dual to the bar-even [2]_q prefactor of alpha_EM".

THE HYPOTHESIS, stated because everything below is conditional on it: under D
each ladder factor `(1 + c_k X^k)` must be bar-INVARIANT, since Q_beta is an
observable and D's grading is multiplicative (this arc, entries 3-8). Under C
this does NOT apply — C's action is affine and weights are not its grading — so
nothing here is a claim about the C ladder.

WHAT FOLLOWS, given that hypothesis. Bar-invariance of every factor forces
w(c_k) + k*w(X) = 0, hence bar(rho)/rho = (bar(X)/X)^{-1}:

    X = u        bar(X)/X = q^2   ->  forced bar(rho)/rho = q^{-2}
    X = u*Vhat   bar(X)/X = 1     ->  forced bar(rho)/rho = 1   (BAR-INVARIANT)

NEITHER IS -1. So a bar-ODD generator is inconsistent with the rank-1 law under
either expansion variable. The docstring's "sinh partner" reading is a C-frame
intuition — dual to alpha_EM's bar-even [2]_q, where the affine action makes
odd/even the natural pairing — and it does not carry to D.

*** AND c_2 = -1 DISCRIMINATES AFTER ALL. *** An earlier entry of mine recorded
that testing the forced form against c_2 = -1 "does not discriminate", because
c_2 = -1 is the x^2 coefficient of the shape `1 - x^2` and survives any
substitution of x. That is true of its VALUE and I stand by it. But its
BAR-WEIGHT is a different question, and that one does discriminate:

    c_2 = -1 is a rational constant, so bar(c_2)/c_2 = 1  -> weight 0.

    X = u*Vhat requires w(c_k) = 0 for all k          -> CONSISTENT with c_2
    X = u      requires w(c_2) = -4, i.e. ratio q^{-4} -> INCONSISTENT with c_2

So the one rung the corpus DERIVES rather than extracts is compatible with the
forced form and incompatible with the naive one. That is a real discriminator,
and it is evidence FOR `Pi(1 + c_k (u*Vhat)^k)` — obtained without fitting
anything, from the weight of a value that was already proved.

NOT CLAIMED. That the forced form IS the D ladder; the argument is conditional
on the bar-invariance hypothesis above, which is motivated but not proved. No
c_k is proposed, extracted or wired. No instance of QBetaSingleHabiroGenerator
is produced — the open state is untouched. Scope (a).

NO FLOAT64: sympy exact throughout.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402

import sympy as sp  # noqa: E402

q = sp.symbols("q", positive=True)
bar = lambda e: sp.simplify(sp.powsimp(sp.radsimp(e.subs(q, 1 / q)), force=True))  # noqa: E731
h = q - 1 / q
hbar = (q - 1) / q
b = sp.sqrt(q ** 4 + q ** 2 + 1) / (q ** 2 + 1)
u = b * hbar ** 2
V_D = sp.simplify(q ** 3 / (q ** 2 + 1) * h + 1)

A = []


def check(name, passed, note=""):
    A.append((name, bool(passed)))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
    if note:
        print(f"          {note}")


def wt(X):
    return sp.simplify(sp.radsimp(bar(X) / X))


print("=" * 78)
print(" qou-cds1 — the D-frame generator's forced parity")
print("=" * 78)

check("u_has_bar_ratio_q_squared", sp.simplify(wt(u) - q ** 2) == 0)
check("u_Vhat_has_bar_ratio_1", sp.simplify(wt(u * V_D) - 1) == 0)

# the forced rho parity, per expansion variable
rho_u = sp.simplify(1 / wt(u))
rho_uV = sp.simplify(1 / wt(u * V_D))
check("X_eq_u_forces_rho_ratio_q_minus_2", sp.simplify(rho_u - q ** -2) == 0)
check("X_eq_u_Vhat_forces_rho_BAR_INVARIANT", sp.simplify(rho_uV - 1) == 0)
check("NEITHER_forced_parity_is_bar_ODD",
      sp.simplify(rho_u + 1) != 0 and sp.simplify(rho_uV + 1) != 0,
      "bar-odd means ratio -1; neither q^{-2} nor 1 is -1. The docstring's "
      "'sinh partner' intent is a C-frame reading that does not carry to D.")

# c_2 = -1 discriminates BY WEIGHT (not by value)
c2 = sp.Integer(-1)
check("c_2_is_bar_INVARIANT_weight_0", sp.simplify(bar(c2) / c2 - 1) == 0,
      "c_2 = -1 is a rational constant, so its bar-ratio is 1")
check("X_eq_u_Vhat_is_CONSISTENT_with_c_2",
      sp.simplify(bar(c2 * (u * V_D) ** 2) / (c2 * (u * V_D) ** 2) - 1) == 0,
      "the k=2 factor's c_2*X^2 term is bar-invariant — matches the `1`")
check("X_eq_u_is_INCONSISTENT_with_c_2",
      sp.simplify(bar(c2 * u ** 2) / (c2 * u ** 2) - 1) != 0,
      f"c_2*u^2 has bar-ratio {sp.simplify(sp.radsimp(bar(c2*u**2)/(c2*u**2)))} "
      "!= 1, so that factor cannot be bar-invariant")

print("\n" + "=" * 78)
npass = sum(1 for _, p in A if p)
print(f" {npass}/{len(A)} checks passed")
print("=" * 78)
print("""
TWO RESULTS.

1. THE GENERATOR'S PARITY IS FORCED, and is NOT bar-odd.

       X = u        ->  bar(rho)/rho = q^{-2}
       X = u*Vhat   ->  bar(rho)/rho = 1        BAR-INVARIANT

   The open class QBetaSingleHabiroGenerator is parity-free in its STATEMENT,
   so nothing in Lean has to change. Its DOCSTRING's intended bar-odd "sinh
   partner" is a C-frame reading — dual to alpha_EM's bar-even [2]_q, natural
   where the action is affine — and it does not carry to D. The D-frame search
   target is a BAR-INVARIANT generator.

2. c_2 = -1 DISCRIMINATES AFTER ALL — by WEIGHT, not by value.

   I recorded earlier that this test "does not discriminate". That holds for
   its VALUE (the x^2 coefficient of 1 - x^2 is -1 for any x) and I stand by
   it. Its BAR-WEIGHT is a different question: c_2 = -1 is a rational constant,
   weight 0, which X = u*Vhat REQUIRES and X = u FORBIDS.

   So the one rung the corpus derives rather than extracts is compatible with
   the forced form and incompatible with the naive one — evidence obtained from
   an already-proved value, with nothing fitted.

CONDITIONAL on the bar-invariance hypothesis, which is motivated by D's
multiplicative grading but not proved. No c_k proposed; no instance produced.
""")
sys.exit(0 if npass == len(A) else 1)
