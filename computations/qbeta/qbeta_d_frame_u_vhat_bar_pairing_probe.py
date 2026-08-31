#!/usr/bin/env python3
"""
qou-cds1: the ladder variable u and the traced volume Vhat carry OPPOSITE
bar-weights, so u*Vhat is bar-invariant — and both are built on [2]_q.

# Ref: .beans/qou-cds1--s1-science-re-derive-the-qbeta-ck-ladder-under-d-n.md

FOLLOWS the log-coordinate result (PR #6211): in theta = log q the bar
involution is theta -> -theta, and

    Vhat_D = e^theta * cosh(2theta)/cosh(theta) = q * [2]_{q^2}/[2]_q

so Vhat_D is a bar-ODD monomial times a bar-EVEN factor, and the D ladder
should resum log Vhat rather than Vhat.

THIS ASKS THE NEXT QUESTION: what is the ladder's own expansion variable doing
under bar? The ladder is Pi(1 + c_k u^k) with u = b*hbar_q^2,
hbar_q = (q-1)/q, and the Hoefsmit b = sqrt(q^4+q^2+1)/(q^2+1)
(`_h4_route_ladder_scan.py:25`). Nothing in the corpus states u's bar-weight.

WHAT IS TESTED (sympy exact; no anchor, no fit, no c_k):

  1.  b = sqrt([3]_{q^2}) / [2]_q          -- b is a RATIO OF q-INTEGERS,
      since q^4+q^2+1 = q^2*[3]_{q^2} and q^2+1 = q*[2]_q.
  2.  b is bar-EVEN. ([3]_x and [2]_x are both invariant under x -> 1/x.)
  3.  hbar_q is a bar-eigenvector of weight +1: bar(hbar) = -q*hbar.
      Hence hbar^2 has weight +2 and, with b even, u has bar-weight +2.
  4.  Vhat_D has bar-weight -2 (Step 7).
  5.  THEREFORE u * Vhat_D is bar-INVARIANT — the weights cancel exactly.
  6.  b and Vhat_D/q share the denominator [2]_q, so it cancels in their
      ratio, leaving [2]_{q^2}/sqrt([3]_{q^2}): a pure q^2-object.

WHY IT MATTERS, and the honest limit of it. A resummation needs a
bar-invariant to organise around; Step 8 showed the D invariant Vhat/q is not
constant, closing the additive route. Item 5 exhibits a DIFFERENT invariant,
built from the ladder's own variable rather than from Vhat alone. That is a
candidate organising object, NOT a resummation: no series is exhibited, no c_k
is proposed, extracted or wired, and nothing here says the ladder must be
organised this way. Scope (a).

NO FLOAT64: sympy exact throughout.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402

import sympy as sp  # noqa: E402

q = sp.symbols("q", positive=True)
bar = lambda e: sp.simplify(sp.powsimp(e.subs(q, 1 / q), force=True))  # noqa: E731
qint = lambda n, x: sum(x ** (n - 1 - 2 * i) for i in range(n))        # noqa: E731

h = q - 1 / q
hbar_q = (q - 1) / q
b = sp.sqrt(q ** 4 + q ** 2 + 1) / (q ** 2 + 1)
u = b * hbar_q ** 2
z_D = q ** 3 / (q ** 2 + 1)
V_D = sp.simplify(z_D * h + 1)

br2 = lambda x: x + 1 / x            # noqa: E731  [2]_x
br3 = lambda x: x + 1 + 1 / x        # noqa: E731  [3]_x

A = []


def check(name, passed, note=""):
    A.append((name, bool(passed)))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
    if note:
        print(f"          {note}")


print("=" * 78)
print(" qou-cds1 — u and Vhat carry opposite bar-weights")
print("=" * 78)

# 1 -- b in q-integer form
check("b_is_sqrt([3]_{q^2})_over_[2]_q",
      sp.simplify(b - sp.sqrt(br3(q ** 2)) / br2(q)) == 0,
      "q^4+q^2+1 = q^2*[3]_{q^2} and q^2+1 = q*[2]_q, so the q's cancel")

# 2 -- b is bar-even
check("b_is_bar_EVEN", sp.simplify(bar(b) - b) == 0,
      "[3]_x and [2]_x are each invariant under x -> 1/x")

# 3 -- hbar_q's bar-weight, and hence u's
check("hbar_q_satisfies_bar(hbar)_eq_minus_q_hbar",
      sp.simplify(bar(hbar_q) + q * hbar_q) == 0,
      f"bar(hbar_q) = {bar(hbar_q)}")
check("u_has_bar_weight_PLUS_2",
      sp.simplify(bar(u) - q ** 2 * u) == 0,
      "bar(u) = q^2 * u   (hbar^2 gives q^2; b is even)")

# 4 -- Vhat_D's bar-weight (Step 7, re-verified here)
check("Vhat_D_has_bar_weight_MINUS_2",
      sp.simplify(bar(V_D) - V_D / q ** 2) == 0,
      "bar(Vhat) = Vhat/q^2   (reproduces Step 7)")

# 5 -- THE PAIRING
prod = sp.simplify(u * V_D)
check("u_times_Vhat_D_is_bar_INVARIANT",
      sp.simplify(bar(prod) - prod) == 0,
      f"u*Vhat_D = {sp.simplify(sp.radsimp(prod))}")

# ... and the additive counterpart does NOT cancel, which is the contrast
check("u_PLUS_Vhat_D_is_NOT_bar_invariant",
      sp.simplify(bar(u + V_D) - (u + V_D)) != 0,
      "the cancellation is multiplicative, matching the multiplicative action")

# 6 -- the shared [2]_q denominator
ratio = sp.simplify(sp.radsimp((V_D / q) / b))
check("Vhat_over_q_divided_by_b_is_a_pure_q^2_object",
      sp.simplify(ratio - br2(q ** 2) / sp.sqrt(br3(q ** 2))) == 0,
      f"(Vhat_D/q)/b = [2]_{{q^2}}/sqrt([3]_{{q^2}}) = {ratio}   "
      "-- the [2]_q cancels")

print("\n" + "=" * 78)
npass = sum(1 for _, p in A if p)
print(f" {npass}/{len(A)} checks passed")
print("=" * 78)
print("""
THE STRUCTURE.

    object      bar-weight     q-integer form
    ------      ----------     --------------
    u           +2             sqrt([3]_{q^2})/[2]_q * hbar_q^2
    Vhat_D      -2             q * [2]_{q^2}/[2]_q
    u * Vhat_D   0             BAR-INVARIANT

The ladder's own expansion variable carries exactly the weight that cancels
Vhat's. Under C this question does not arise: the action is affine there, and
weights are not what organises it.

WHAT THIS IS. A candidate organising object for a D-frame resummation --
something bar-invariant that involves the ladder variable, where Step 8 showed
Vhat/q alone is invariant but not constant.

WHAT THIS IS NOT. A resummation. No series is exhibited, no c_k is proposed,
extracted or wired, and nothing here shows the ladder MUST be organised this
way -- only that the weights permit it. Step 8's closure of the ADDITIVE route
is untouched and remains correct. Scope (a): symbolic, three objects.
""")
sys.exit(0 if npass == len(A) else 1)
