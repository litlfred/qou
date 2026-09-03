#!/usr/bin/env python3
"""
qou-cds1: the D-frame offset is the BAR-MIDPOINT, and that one rule derives
convention C's offset of 1 as well.

# Ref: .beans/qou-cds1--s1-science-re-derive-the-qbeta-ck-ladder-under-d-n.md

WHAT THIS RE-EXAMINES. Step 7 (2b1d33a778) solves for the offset `c` making
`Vhat - c - h` bar-odd under D, gets `c = (q^4+1)/(2q^2)`, and dismisses it:

    "which is q-dependent. A q-dependent offset is not a re-centring of the
     phase, it is a different object."

Step 8 (864568750c) builds on that: the D bar-invariant "MOVES WITH q: there is
no fixed centre, so no additive resummation has anything to be centred on."

DUPLICATION IS AUTHORISED here (owner, 2026-08-30, "duplicate ok"); this walks
in from a different direction and reaches a weaker conclusion than Step 8's.

THE CLAIM UNDER TEST. `(q^4+1)/(2q^2)` is not an arbitrary function of q. It is
`(q^2 + q^-2)/2` -- the BAR-MIDPOINT of Vhat, i.e. `(Vhat + bar Vhat)/2`. And
under convention C the bar-midpoint is `(Vhat + (2 - Vhat))/2 = 1`, which is
exactly C's offset. So the single rule

    offset := the bar-midpoint of Vhat

would DERIVE C's `1` rather than assume it, and hand D its `(q^2+q^-2)/2`.
That is the same consistency test Step 2's bar-weight argument passed, applied
to the offset instead of the weight.

IF IT HOLDS, the honest reading of Step 7/8 changes in scope but not in
substance: the centre is not ABSENT under D, it is q-DEPENDENT-BUT-DERIVED.
"No fixed centre" stays true; "nothing to be centred on" would be too strong.

WHAT THIS DOES NOT CLAIM. It proposes no replacement form, no c_k, and nothing
is wired. A resummation about a moving centre is not exhibited here -- only
that the centre is a named object rather than a fitted one. Scope (a).

NO FLOAT64: sympy exact symbolic throughout, mpmath only to display.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402

import sympy as sp  # noqa: E402

q = sp.symbols("q", positive=True)
h = q - 1 / q
z_C = sp.sqrt(q) / (q + 1)
z_D = q ** 3 / (q ** 2 + 1)


def bar(expr):
    """The bar involution: q -> 1/q."""
    return sp.simplify(expr.subs(q, 1 / q))


A = []


def check(name, passed, note=""):
    A.append((name, bool(passed)))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
    if note:
        print(f"          {note}")


print("=" * 78)
print(" qou-cds1 — is the D offset the BAR-MIDPOINT? (and does it derive C's 1?)")
print("=" * 78)

# ---- 0. bar is an involution on the objects we use ------------------------
check("bar_is_an_involution_on_q", sp.simplify(bar(bar(q)) - q) == 0)
check("h_is_bar_odd", sp.simplify(bar(h) + h) == 0, f"bar(h) = {bar(h)}")

# ---- 1. Vhat and the two bar actions, reproduced from Step 7 --------------
for name, z, expected in (("C", z_C, None), ("D", z_D, None)):
    V = sp.simplify(z * h + 1)
    print(f"\n  convention {name}:  Vhat = {sp.simplify(V)}")
    print(f"                     bar(Vhat) = {bar(V)}")

V_C = sp.simplify(z_C * h + 1)
V_D = sp.simplify(z_D * h + 1)

check("C_bar_action_is_affine_reflection_2_minus_V",
      sp.simplify(bar(V_C) - (2 - V_C)) == 0,
      "reproduces Step 7: bar(Vhat) = 2 - Vhat under C")
check("D_bar_action_is_multiplicative_weight_minus_2",
      sp.simplify(bar(V_D) - V_D / q ** 2) == 0,
      "reproduces Step 7: bar(Vhat) = Vhat/q^2 under D")

# ---- 2. THE BAR-MIDPOINT, in both conventions ----------------------------
mid_C = sp.simplify((V_C + bar(V_C)) / 2)
mid_D = sp.simplify((V_D + bar(V_D)) / 2)
print(f"\n  bar-midpoint under C: {mid_C}")
print(f"  bar-midpoint under D: {mid_D}")

check("C_bar_midpoint_IS_the_constant_1",
      sp.simplify(mid_C - 1) == 0,
      "so the rule 'offset := bar-midpoint' DERIVES C's offset of 1")
check("D_bar_midpoint_equals_the_Step_7_offset",
      sp.simplify(mid_D - (q ** 4 + 1) / (2 * q ** 2)) == 0,
      "the offset Step 7 solved for IS the bar-midpoint, not an arbitrary fn")
check("D_bar_midpoint_is_the_q_squared_integer_over_2",
      sp.simplify(mid_D - (q ** 2 + q ** (-2)) / 2) == 0,
      "(q^2+q^-2)/2 = [2]_{q^2}/2 = cosh(2 log q); C's 1 = cosh(0)")

# ---- 3. does the midpoint offset actually make the phase bar-odd? ---------
for name, V, mid in (("C", V_C, mid_C), ("D", V_D, mid_D)):
    phase = sp.simplify((V - mid - h) / 2)
    odd = sp.simplify(bar(phase) + phase) == 0
    check(f"{name}_phase_with_midpoint_offset_is_bar_ODD", odd,
          f"alpha_{name} = (Vhat - midpoint - h)/2 = {sp.simplify(phase)}")

# ---- 4. the C phase is the KNOWN alpha; D's is its frame-analogue ---------
alpha_C_known = sp.simplify((z_C - 1) * h / 2)
alpha_C_built = sp.simplify((V_C - mid_C - h) / 2)
check("C_midpoint_phase_reproduces_the_KNOWN_alpha",
      sp.simplify(alpha_C_known - alpha_C_built) == 0,
      "so this is not a new object under C -- it IS alpha, re-derived")

alpha_D_built = sp.simplify((V_D - mid_D - h) / 2)
alpha_D_naive = sp.simplify((z_D - 1) * h / 2)
same = sp.simplify(alpha_D_built - alpha_D_naive) == 0
check("D_midpoint_phase_DIFFERS_from_the_naive_z_swap", not same,
      f"naive (z_D-1)h/2 = {alpha_D_naive}\n          "
      f"midpoint-built  = {alpha_D_built}")

# ---- 5. the honest negative: is the D centre constant? -------------------
check("D_centre_is_NOT_constant_in_q_(Step_8_stands)",
      sp.simplify(sp.diff(mid_D, q)) != 0,
      "Step 8's 'no FIXED centre' is confirmed, not overturned")

print("\n" + "=" * 78)
npass = sum(1 for _, p in A if p)
print(f" {npass}/{len(A)} checks passed")
print("=" * 78)
print("""
READING, and it is a NARROWING of Step 7/8 rather than a refutation:

  * Step 8's "no FIXED centre" is CONFIRMED (check 5): the D centre genuinely
    moves with q.
  * But the centre is not absent and not arbitrary. It is the bar-midpoint --
    the SAME rule that, applied under C, returns the constant 1 that C's ladder
    already uses. One rule, two frames.
  * So Step 7's "a q-dependent offset is not a re-centring, it is a different
    object" is too strong as stated. It is the same object; its VALUE is
    constant in C and q-dependent in D, exactly as the bar-weight is 0 in C and
    -4 in D (Step 2). Both are two-case facts about one construction.

WHAT REMAINS OPEN, unchanged: the replacement FORM. Naming a centre does not
exhibit a resummation about it, and cos is still the wrong realisation because
the action is multiplicative. Nothing here proposes a c_k, and nothing is
wired. Scope (a): one object (Vhat), two conventions, symbolic.
""")
sys.exit(0 if npass == len(A) else 1)
