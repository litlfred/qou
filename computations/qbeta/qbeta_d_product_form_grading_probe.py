#!/usr/bin/env python3
"""
qou-cds1: the ladder's PRODUCT FORM is weight-inhomogeneous under D — and the
weight-homogeneous replacement is forced, not searched for.

# Ref: .beans/qou-cds1--s1-science-re-derive-the-qbeta-ck-ladder-under-d-n.md

THE ARC SO FAR closed the phase family: D's bar-defect is h^2/2 and lives
outside the correction series, and D's bar-ODD slot is structure-free, so no
cos-of-a-bar-odd-phase can express it. The surviving lead was the multiplicative
form plus the bar-invariant u*Vhat. This applies that lead to the product form.

MEASURED, sympy exact:

    bar(u^k)/u^k        = q^{2k}          weight 2k, for k = 1,2,3
    bar((u*Vhat)^k)/..  = 1               weight 0,  for k = 1,2,3

    1 + c*u^k           is NEVER a bar-eigenvector — bar(f)/f depends on q for
                        every c, so no coefficient repairs it
    1 + c*(u*Vhat)^k    is EXACTLY bar-invariant for every c

So under D the ladder's own factors `(1 + c_k u^k)` each mix bar-weight 0 (the
`1`) with bar-weight 2k (the `u^k` term). That is the SAME weight-mismatch
pathology Step 2 identified in the offset `alpha = (z-1)h/2`, now found one
level up, in the product form itself. And the weight-homogeneous replacement is
forced by the grading: `(1 + c_k (u*Vhat)^k)`, because u*Vhat is the invariant.

*** THE C CONTROL, WITHOUT WHICH THIS WOULD BE AN OVERCLAIM. ***
u is convention-INDEPENDENT (u = b*hbar_q^2; neither b nor hbar involves z), so
u carries bar-weight +2 under C as well, and `1 + c*u^k` is weight-inhomogeneous
there too. That is NOT a defect in C's ladder, because under C the bar action is
AFFINE (bar(Vhat) = 2 - Vhat, Step 7) and weights are not the grading that
organises it. Confirmed here: u*Vhat_C is NOT bar-invariant, so the D repair
does not even typecheck under C.

The claim is therefore precisely: under D, where the action IS multiplicative
and weights ARE the organising grading, the ladder's product form is
inhomogeneous and no c_k repairs it. Under C the same inhomogeneity is
harmless. Two-case, like every other result in this arc.

NOT CLAIMED. That `Pi(1 + c_k (u*Vhat)^k)` IS the D ladder. Only that it is the
weight-homogeneous form, reached BY GRADING rather than by search — which is
what makes it a candidate rather than a fit. No c_k is proposed, extracted or
wired; no series is evaluated; nothing is compared to experiment. A form reached
by fitting coefficients to Q_beta would be exactly the thing this bean's
Discipline section forbids, and none is attempted. Scope (a).

NO FLOAT64: sympy exact throughout.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402

import sympy as sp  # noqa: E402

q = sp.symbols("q", positive=True)
c = sp.symbols("c", nonzero=True)
bar = lambda e: sp.simplify(sp.powsimp(sp.radsimp(e.subs(q, 1 / q)), force=True))  # noqa: E731

h = q - 1 / q
hbar_q = (q - 1) / q
b = sp.sqrt(q ** 4 + q ** 2 + 1) / (q ** 2 + 1)
u = b * hbar_q ** 2
V_D = sp.simplify(q ** 3 / (q ** 2 + 1) * h + 1)
V_C = sp.simplify(sp.sqrt(q) / (q + 1) * h + 1)

A = []


def check(name, passed, note=""):
    A.append((name, bool(passed)))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
    if note:
        print(f"          {note}")


print("=" * 78)
print(" qou-cds1 — the product form against D's grading")
print("=" * 78)

# 1 -- u^k carries weight 2k
for k in (1, 2, 3):
    w = sp.simplify(sp.radsimp(bar(u ** k) / u ** k))
    check(f"u^{k}_has_bar_weight_{2*k}", sp.simplify(w - q ** (2 * k)) == 0)

# 2 -- (u*V)^k is weight 0
for k in (1, 2, 3):
    w = sp.simplify(sp.radsimp(bar((u * V_D) ** k) / (u * V_D) ** k))
    check(f"(u_Vhat)^{k}_has_bar_weight_0", sp.simplify(w - 1) == 0)

# 3 -- no c repairs 1 + c*u^k
for k in (1, 2):
    f = 1 + c * u ** k
    r = sp.simplify(sp.radsimp(bar(f) / f))
    check(f"1_plus_c_u^{k}_is_NEVER_a_bar_eigenvector",
          sp.simplify(sp.diff(r, q)) != 0,
          "bar(f)/f depends on q for every c — no coefficient repairs it")

# 4 -- the homogeneous replacement
for k in (1, 2):
    f = 1 + c * (u * V_D) ** k
    check(f"1_plus_c_(u_Vhat)^{k}_IS_bar_invariant",
          sp.simplify(sp.radsimp(bar(f) / f) - 1) == 0,
          "exactly invariant for EVERY c — the grading, not the coefficient")

# 5 -- THE C CONTROL
check("u_is_convention_INDEPENDENT",
      "z" not in str(u) and sp.simplify(sp.diff(u, q)) != 0,
      "u = b*hbar^2; neither factor involves z, so u has weight +2 under C too")
check("u_times_Vhat_C_is_NOT_bar_invariant",
      sp.simplify(bar(u * V_C) - (u * V_C)) != 0,
      "the D repair does not typecheck under C — C's action is AFFINE, so "
      "weights are not its grading and the inhomogeneity is harmless there")

print("\n" + "=" * 78)
npass = sum(1 for _, p in A if p)
print(f" {npass}/{len(A)} checks passed")
print("=" * 78)
print("""
THE RESULT.

Under D the ladder's factors `(1 + c_k u^k)` each mix bar-weight 0 (the `1`)
with bar-weight 2k (the `u^k`). No choice of c_k repairs that — it is the
grading, not the coefficient. This is the SAME pathology Step 2 found in the
offset, one level up: in the product form itself.

The weight-homogeneous form is FORCED by the grading:

        Pi ( 1 + c_k (u * Vhat)^k )

because u*Vhat is the bar-invariant. Reached by grading, not by search.

THE C CONTROL. u is convention-independent, so `1 + c u^k` is inhomogeneous
under C as well — and that is HARMLESS there, because C's bar action is affine
and weights are not its grading. Confirmed: u*Vhat_C is not bar-invariant, so
the D repair does not even typecheck under C. Two-case, like the rest of this
arc.

NOT CLAIMED: that Pi(1 + c_k (u Vhat)^k) IS the D ladder. Only that it is the
weight-homogeneous form. No c_k proposed, extracted or wired; no series
evaluated; nothing compared to experiment. Scope (a).
""")
sys.exit(0 if npass == len(A) else 1)
