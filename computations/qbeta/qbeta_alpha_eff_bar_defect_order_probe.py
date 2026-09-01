#!/usr/bin/env python3
"""
qou-cds1: the ladder's alpha_eff is bar-odd in NEITHER convention — and the
reason that matters under D but not under C is the ORDER of the defect.

# Ref: .beans/qou-cds1--s1-science-re-derive-the-qbeta-ck-ladder-under-d-n.md

RECORDED AS A NEGATIVE ON MY OWN HYPOTHESIS. Having found (PR #6223) that u has
bar-weight +2 while Vhat has -2, I guessed that the ladder's `- u/2` term might
be exactly the bar-correction repairing alpha under D. It is not, and the first
reading of the refutation was also wrong. Both are recorded so the next agent
does not re-walk either.

THE LADDER USES alpha_eff, NOT alpha:

    alpha_eff = alpha - b*hbar_q^2/2 = alpha - u/2
    Q_N1      = Q_A * cos(alpha_eff)

(`_h4_route_ladder_scan.py:26`, `probes/qbeta_ck_basis_constrained_pslq.py:114`.
NOTE the symbol is OVERLOADED: `qbeta_multi_block_eigenphase_probe.py` uses
`alpha_eff` for a dimension-weighted block average, a different object. This
probe means the ladder one.)

MEASURED, sympy exact:

    convention   bar(alpha)+alpha        bar(alpha_eff)+alpha_eff
    C            0        (bar-ODD)      -u*(q^2+1)/2
    D            (q^2-1)^2/(2q^2)        (q^2-1)^2/(2q^2) - u*(q^2+1)/2

MY FIRST READING, AND WHY IT WAS WRONG. Seeing "alpha_eff is bar-odd in neither
frame", I took it to mean C's clean bar structure does not survive to the object
the ladder actually evaluates -- i.e. that Step 7's argument describes alpha but
not the ladder. That is wrong. Under C the residual is EXACTLY -u*(q^2+1)/2, a
RATIONAL multiple of u: the bar-oddness fails precisely at the order of the
correction term that caused it. That is what a truncated series does, and it is
not a defect.

WHAT IS ACTUALLY THERE. The `- u/2` term's own bar-defect is
CONVENTION-INDEPENDENT: it contributes -u*(q^2+1)/2 in both frames. What differs
is what it is added to.

    C:  total residual = O(u)                      -- vanishes with the
                                                      truncation order
    D:  total residual = (q^2-1)^2/(2q^2)  -  O(u) -- carries a piece that is
                                                      INDEPENDENT of u

So D's obstruction is not that its phase has an O(u) bar-defect. C has one too,
harmlessly. It is that D's defect has a u-INDEPENDENT part, which no order of
ladder correction can remove. That sharpens Step 7 ("bar(alpha)+alpha != 0 under
D") into a statement about the LADDER rather than about alpha alone: the
correction series is the wrong tool for this defect, because the defect does not
live in the series.

WHAT THIS IS NOT. No c_k is proposed, extracted or wired; no replacement phase
is offered. Scope (a): two conventions, one object, symbolic. Step 7 and Step 8
are both untouched -- this states one of their consequences more precisely.

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
hbar_q = (q - 1) / q
b = sp.sqrt(q ** 4 + q ** 2 + 1) / (q ** 2 + 1)
u = b * hbar_q ** 2
Z = {"C": sp.sqrt(q) / (q + 1), "D": q ** 3 / (q ** 2 + 1)}

A = []


def check(name, passed, note=""):
    A.append((name, bool(passed)))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
    if note:
        print(f"          {note}")


print("=" * 78)
print(" qou-cds1 — the ORDER of alpha_eff's bar-defect")
print("=" * 78)

res = {}
for name, z in Z.items():
    a = sp.simplify((z - 1) * h / 2)
    aeff = sp.simplify(a - u / 2)
    res[name] = (sp.simplify(bar(a) + a), sp.simplify(bar(aeff) + aeff))

# 1 -- alpha: bar-odd under C, not under D (reproduces Step 7)
check("C_alpha_is_bar_ODD", res["C"][0] == 0)
check("D_alpha_is_NOT_bar_odd", res["D"][0] != 0,
      f"bar(alpha)+alpha = {res['D'][0]}  = (q^2-1)^2/(2q^2)")
check("D_alpha_defect_is_(q^2-1)^2_over_2q^2",
      sp.simplify(res["D"][0] - (q ** 2 - 1) ** 2 / (2 * q ** 2)) == 0)

# 2 -- alpha_eff is bar-odd in NEITHER frame
check("C_alpha_eff_is_NOT_bar_odd", res["C"][1] != 0)
check("D_alpha_eff_is_NOT_bar_odd", res["D"][1] != 0)

# 3 -- the -u/2 term's own defect is CONVENTION-INDEPENDENT
u_defect = sp.simplify(-u * (q ** 2 + 1) / 2)
check("C_alpha_eff_defect_is_EXACTLY_minus_u_(q^2+1)/2",
      sp.simplify(res["C"][1] - u_defect) == 0,
      "so under C the residual is a RATIONAL multiple of u — the truncation's "
      "own order, not a defect")
check("D_alpha_eff_defect_is_alphas_defect_PLUS_the_same_u_term",
      sp.simplify(res["D"][1] - (res["D"][0] + u_defect)) == 0,
      "the -u/2 contributes the SAME -u(q^2+1)/2 in both frames")

# 4 -- the decisive difference: is the residual O(u)?
ratio_C = sp.simplify(sp.radsimp(res["C"][1] / u))
ratio_D = sp.simplify(sp.radsimp(res["D"][1] / u))
check("C_residual_over_u_is_RATIONAL_in_q",
      ratio_C.is_rational_function(q) and sp.simplify(ratio_C - (-(q ** 2 + 1) / 2)) == 0,
      f"residual/u = {ratio_C}  — no surd, so residual is exactly O(u)")
check("D_residual_over_u_is_NOT_rational_in_q",
      sp.sqrt(q ** 4 + q ** 2 + 1) in ratio_D.atoms(sp.Pow) or
      not sp.simplify(ratio_D).is_rational_function(q),
      "residual/u retains a surd, because the residual has a u-INDEPENDENT part")

print("\n" + "=" * 78)
npass = sum(1 for _, p in A if p)
print(f" {npass}/{len(A)} checks passed")
print("=" * 78)
print("""
THE POINT, stated as precisely as the algebra allows.

    C:  bar(alpha_eff)+alpha_eff = -u*(q^2+1)/2
          -> EXACTLY O(u). The bar-oddness fails only at the order of the
             correction term that caused it. Expected of a truncation.

    D:  bar(alpha_eff)+alpha_eff = (q^2-1)^2/(2q^2) - u*(q^2+1)/2
          -> carries a u-INDEPENDENT piece. No order of ladder correction
             removes it.

So D's obstruction is not "the phase has a bar-defect" — C's does too. It is
that D's defect DOES NOT LIVE IN THE SERIES, so the correction series is the
wrong instrument for it. That is Step 7's observation, sharpened from a
statement about alpha into one about the ladder.

NEGATIVE RECORDED: the `- u/2` term is NOT a bar-correction. It contributes the
same defect in both frames and repairs neither. Do not re-test this.
""")
sys.exit(0 if npass == len(A) else 1)
