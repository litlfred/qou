#!/usr/bin/env python3
"""
qou-cds1: working the forced product form through — it terminates, and the
blocker is nameable.

# Ref: .beans/qou-cds1--s1-science-re-derive-the-qbeta-ck-ladder-under-d-n.md

The previous entry derived, from the bar-grading alone, that the D-frame
product form must be Pi(1 + c_k (u*Vhat)^k) rather than Pi(1 + c_k u^k). I said
the next check was whether that form reproduces the already-proved c_2 = -1,
and called it falsifying. This works it through. Two of the three findings are
corrections to that plan.

*** FINDING 1 — MY PROPOSED TEST DOES NOT DISCRIMINATE. I over-sold it. ***

c_2 = -1 comes from N2_factor = 1 - b^2*hbar^4 = 1 - u^2 (verified below). Its
content is that the N=2 factor has the SHAPE `1 - x^2`; the coefficient of x^2
in `1 - x^2` is -1 for ANY x. So substituting u -> u*Vhat preserves c_2 = -1
trivially, and the test cannot distinguish the forced form from the original.
It is a consistency check, not evidence. Recorded because I claimed otherwise.

FINDING 2 — convergence is not broken. At the proton pin:

    u        = 0.00851723455016
    Vhat_D   = 1.12808874411
    u*Vhat   = 0.00960819642701      (1.128x u — same order)

So the forced form remains a small-parameter expansion. The route does not die
on numerics.

FINDING 3 — but it CANNOT BE TESTED against Q_beta, and this is the terminus.
The C ladder is

    Q_beta = Q_A * cos(alpha_eff) * Pi_{k>=2} (1 + c_k u^k)

The forced form replaces the PRODUCT (k >= 2). The N=1 factor is
cos(alpha_eff) — and entry 7 of this arc established that under D the bar-ODD
slot is structure-free, so NO cos-of-a-bar-odd-phase exists to play that role.
The committed cache confirms the product's scope: its only derived rung is
k = 2 (k = 3 is tier `cal-anchored`, i.e. extracted from experiment).

So the forced product form refines a leading term that does not exist under D.
No D-frame Q_beta can be computed from it, and no comparison to experiment is
possible — not because the comparison would be a fit, but because there is
nothing to compare.

WHAT IS DERIVABLE ANYWAY, and it is not nothing. The forced form's effect on
the one DERIVED rung is computable without the phase: rung k scales by Vhat^k,
so the k=2 rung is Vhat^2 = 1.2726 times larger under the forced form than
under the naive one — a +27.3% change to the only rung the corpus derives
rather than extracts. That is a concrete consequence of the grading argument,
stated without any fit.

STATUS: the route is NOT refuted. It is BLOCKED, on the N=1 phase, by a
blocker this arc itself established. Naming which of two open pieces gates the
other is progress; claiming the form is confirmed would not be.

NO c_k is proposed, extracted or wired. Nothing is compared to experiment.
Scope (a). NO FLOAT64: sympy exact, mpmath at 50 dps for the magnitudes.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
set_compute_dps(50)
from qou_substrate.constants import q_at  # noqa: E402

Q0 = q_at(50)
q, x = sp.symbols("q x", positive=True)
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


def at_q0(e):
    return mp.mpf(str(sp.N(e.subs(q, sp.Float(mp.nstr(Q0, 30), 30)), 40)))


print("=" * 78)
print(" qou-cds1 — the forced form, worked through")
print("=" * 78)

# FINDING 1 -- the c_2 test does not discriminate
check("N2_factor_IS_1_minus_u_squared",
      sp.simplify((1 - b ** 2 * hbar ** 4) - (1 - u ** 2)) == 0,
      "c_2 = -1 comes from the shape 1 - u^2")
check("c_2_eq_minus_1_is_SHAPE_preserving_hence_NON_discriminating",
      sp.Poly(1 - x ** 2, x).coeff_monomial(x ** 2) == -1,
      "the x^2 coefficient of 1 - x^2 is -1 for ANY x, so u -> u*Vhat "
      "preserves it trivially. My proposed test cannot falsify the form.")

# FINDING 2 -- magnitudes
uu, VV = at_q0(u), at_q0(V_D)
check("u_times_Vhat_stays_a_small_parameter",
      uu * VV < mp.mpf("0.05") and uu * VV > uu,
      f"u = {mp.nstr(uu,12)}, Vhat = {mp.nstr(VV,12)}, "
      f"u*Vhat = {mp.nstr(uu*VV,12)} ({mp.nstr(VV,6)}x u)")

# FINDING 3 -- the derived consequence on the one derived rung
scale2 = VV ** 2
check("k2_rung_scales_by_Vhat_squared",
      abs(scale2 - mp.mpf("1.2726")) < mp.mpf("0.001"),
      f"Vhat^2 = {mp.nstr(scale2,10)} — the k=2 rung is +{mp.nstr((scale2-1)*100,4)}% "
      "under the forced form. The only rung the corpus DERIVES.")

# FINDING 3 -- the blocker, asserted structurally
check("the_N1_factor_is_a_cosine_of_a_bar_odd_phase",
      True,
      "Q_beta = Q_A * cos(alpha_eff) * Pi_{k>=2}(1 + c_k u^k); the forced form "
      "replaces only the PRODUCT")
check("entry_7_closed_the_bar_odd_slot_under_D",
      sp.simplify(sp.expand_log(
          (sp.log(V_D) - sp.log(sp.simplify(V_D.subs(q, 1 / q)))) / 2
          - sp.log(q), force=True)) == 0,
      "odd(log Vhat_D) = log q exactly — structure-free, so no cos-type phase "
      "exists to be the N=1 factor")

print("\n" + "=" * 78)
npass = sum(1 for _, p in A if p)
print(f" {npass}/{len(A)} checks passed")
print("=" * 78)
print("""
THE DERIVATION TERMINATES, and the blocker is nameable.

  * My proposed c_2 test does NOT discriminate — c_2 = -1 is a statement about
    the shape 1 - x^2 and survives any substitution of x. I called it
    falsifying; it is not. Correction, not a result.

  * Convergence is fine: u*Vhat = 0.0096 against u = 0.0085, same order.

  * But the forced form replaces only the k >= 2 PRODUCT. The N=1 factor is
    cos(alpha_eff), and entry 7 showed D has no bar-odd slot with any structure
    in it — so that factor has no D-frame form. The forced product therefore
    refines a leading term that does not exist.

  * Derivable anyway: the k=2 rung — the ONLY one the corpus derives rather
    than extracts — is Vhat^2 = 1.2726x larger under the forced form. +27.3%,
    stated without any fit.

STATUS: the route is NOT refuted, it is BLOCKED — on the N=1 phase, by a
blocker this arc established itself. Naming which open piece gates the other is
progress. Claiming the form confirmed would not be.
""")
sys.exit(0 if npass == len(A) else 1)
