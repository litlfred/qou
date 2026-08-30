#!/usr/bin/env python3
"""
qou-cds1: what replaces the cosine under D — the decomposition is MULTIPLICATIVE,
and in log coordinates both frames become one statement.

# Ref: .beans/qou-cds1--s1-science-re-derive-the-qbeta-ck-ladder-under-d-n.md

Step 8 (864568750c) closes the additive route and leaves the replacement FORM
open: "The class is fixed (must respect the multiplicative action; the invariant
is Vhat/q), the additive route is closed ... but naming the form needs [more]."

This names it. Duplication authorised (owner, "duplicate ok", 2026-08-30).

THE MOVE: work in theta = log q, where the bar involution is simply theta -> -theta.
Every bar statement becomes a PARITY statement in theta, and the two conventions
stop looking like different phenomena.

WHAT IS TESTED (exact symbolic; nothing numerical, nothing fitted):

  1.  Vhat_D = (q^4+1)/(q^2+1)                     closed form
  2.  Vhat_D / q = (q^2+q^-2)/(q+q^-1) = [2]_{q^2}/[2]_q
                 = cosh(2 theta)/cosh(theta)       a RATIO of q-integers
  3.  Vhat_C = 1 + 2 sinh(theta/2)                 closed form
  4.  therefore
          C:  Vhat = (bar-EVEN constant 1)  +  (bar-ODD 2 sinh(theta/2))
          D:  Vhat = (bar-ODD monomial e^theta) *  (bar-EVEN cosh2/cosh)
      C decomposes ADDITIVELY, D MULTIPLICATIVELY. Same object, two frames.
  5.  the bar-midpoint of D, cosh(2 theta), is exactly the NUMERATOR of D's
      bar-even factor -- so the "moving centre" is not a separate discovery,
      it is one half of the multiplicative decomposition.

WHY THAT ANSWERS THE FORM QUESTION. cos is the resummation adapted to a SUM
whose bar-odd part is centred on a constant. Under D there is no such sum. The
object adapted to a PRODUCT is the LOGARITHM: log Vhat_D = theta +
log(cosh 2theta) - log(cosh theta), whose bar-odd part is exactly theta and
whose bar-even part is the log-ratio. So the D-frame ladder should resum
log Vhat, not Vhat -- and in that coordinate its bar-even part is a series in
theta^2, equivalently in the q^{2k}-integers.

WHAT THIS DOES NOT CLAIM. No c_k is proposed, extracted or wired. Naming the
coordinate and the parity structure is not exhibiting the ladder; the series
coefficients are untouched. Scope (a): one object (Vhat), two conventions,
symbolic. Step 8's "no FIXED centre" remains CONFIRMED -- in log coordinates
the centre is not fixed, it is the even part, which is exactly why an additive
resummation of Vhat itself cannot work.

NO FLOAT64: sympy exact; mpmath only to display one sanity value.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402

import sympy as sp  # noqa: E402

q, th = sp.symbols("q theta", positive=True)
h = q - 1 / q
z_C = sp.sqrt(q) / (q + 1)
z_D = q ** 3 / (q ** 2 + 1)
V_C = sp.simplify(z_C * h + 1)
V_D = sp.simplify(z_D * h + 1)

A = []


def check(name, passed, note=""):
    A.append((name, bool(passed)))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
    if note:
        print(f"          {note}")


print("=" * 78)
print(" qou-cds1 — the D-frame form, in log coordinates")
print("=" * 78)

# 1 -- closed form for Vhat_D
check("Vhat_D_closed_form_is_(q^4+1)/(q^2+1)",
      sp.simplify(V_D - (q ** 4 + 1) / (q ** 2 + 1)) == 0,
      f"Vhat_D = {sp.simplify(V_D)}")

# 2 -- the bar-invariant is a RATIO OF q-INTEGERS
bracket2 = lambda x: x + 1 / x          # noqa: E731  [2]_x
check("Vhat_D_over_q_is_[2]_{q^2}_over_[2]_q",
      sp.simplify(V_D / q - bracket2(q ** 2) / bracket2(q)) == 0,
      "Vhat_D/q = (q^2+q^-2)/(q+q^-1) — a ratio of q-integers, not a generic fn")

# 3 -- closed form for Vhat_C
check("Vhat_C_closed_form_is_1_plus_(sqrt q - 1/sqrt q)",
      sp.simplify(V_C - (1 + (sp.sqrt(q) - 1 / sp.sqrt(q)))) == 0,
      f"Vhat_C = {sp.simplify(V_C)}  = 1 + 2 sinh(theta/2)")

# 4 -- the two decompositions, verified as identities
even_D = sp.simplify(V_D / q)            # bar-even factor
odd_C = sp.simplify(V_C - 1)             # bar-odd summand
check("D_factorises_as_q_times_a_bar_even_factor",
      sp.simplify(V_D - q * even_D) == 0,
      "D: Vhat = e^theta * (bar-even) — MULTIPLICATIVE")
check("C_splits_as_1_plus_a_bar_odd_summand",
      sp.simplify(V_C - (1 + odd_C)) == 0,
      "C: Vhat = 1 + (bar-odd) — ADDITIVE")

# parity of each piece under bar: q -> 1/q
bar = lambda e: sp.simplify(e.subs(q, 1 / q))   # noqa: E731
check("D_even_factor_IS_bar_even", sp.simplify(bar(even_D) - even_D) == 0)
check("C_odd_summand_IS_bar_odd", sp.simplify(bar(odd_C) + odd_C) == 0)
check("D_monomial_q_IS_bar_odd_multiplicatively",
      sp.simplify(bar(q) - 1 / q) == 0,
      "bar(q) = 1/q, i.e. theta -> -theta")

# 5 -- the moving centre is the NUMERATOR of the even factor
mid_D = sp.simplify((V_D + bar(V_D)) / 2)
check("D_bar_midpoint_is_the_numerator_of_the_even_factor",
      sp.simplify(mid_D - bracket2(q ** 2) / 2) == 0,
      "midpoint = (q^2+q^-2)/2 = cosh(2 theta) = numerator of Vhat_D/q, /2")

# 6 -- log coordinates: the parity statement
#     log Vhat_D = theta + log cosh(2 theta) - log cosh(theta)
logV_D = sp.simplify(sp.log(V_D))
logform = sp.log(q) + sp.log(bracket2(q ** 2) / 2) - sp.log(bracket2(q) / 2)
check("log_Vhat_D_splits_as_theta_plus_an_EVEN_remainder",
      sp.simplify(sp.expand_log(logV_D - logform, force=True)) == 0,
      "log Vhat_D = theta + [log cosh 2theta - log cosh theta]; "
      "the bracket is bar-EVEN, theta is bar-ODD")

rem = sp.simplify(sp.log(bracket2(q ** 2) / 2) - sp.log(bracket2(q) / 2))
check("the_log_remainder_is_bar_EVEN",
      sp.simplify(sp.expand_log(bar(rem) - rem, force=True)) == 0)

print("\n" + "=" * 78)
npass = sum(1 for _, p in A if p)
print(f" {npass}/{len(A)} checks passed")
print("=" * 78)
print("""
THE FORM, named.

  C:  Vhat = 1 + 2 sinh(theta/2)          a CONSTANT plus a bar-ODD term
  D:  Vhat = e^theta * cosh(2theta)/cosh(theta)
                                          a bar-ODD MONOMIAL times a bar-EVEN
                                          RATIO OF q-INTEGERS

cos is the resummation adapted to C's shape: a sum whose bar-odd part sits on a
fixed centre. D has no such sum, which is Step 8's result and is CONFIRMED here.
The object adapted to a PRODUCT is the LOGARITHM:

      log Vhat_D  =  theta  +  [ log cosh 2theta - log cosh theta ]
                     ^odd        ^-------- even --------^

So the D-frame ladder should resum log Vhat, not Vhat. In that coordinate the
bar-odd part is exactly theta = log q, and the bar-even remainder is a series
in theta^2 — equivalently in the q^{2k}-integers, of which the "moving centre"
cosh(2 theta) is the leading one.

NOT CLAIMED: any c_k. Naming the coordinate and the parity structure is not
exhibiting the ladder. Scope (a), symbolic, one object.
""")
sys.exit(0 if npass == len(A) else 1)
