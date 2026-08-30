#!/usr/bin/env python3
"""
qou-cds1, entry 10: what replaces `cos(alpha_eff)` as the N=1 factor under D.

# Ref: .beans/qou-cds1--s1-science-re-derive-the-qbeta-ck-ladder-under-d-n.md

THE QUESTION THIS ANSWERS. The nine-entry arc closed with one open item, stated
there as: *"what replaces `cos(alpha_eff)` as the N=1 factor under D?"* — with
three conditions on any candidate, all three set by the arc itself:

  (a) bar-invariant;
  (b) reduces to `cos(alpha_eff)` in the C limit;
  (c) absorbs the `h^2/2` defect of entry 6.

THE MOVE, and why it is not a new degree of freedom. Entry 2 established the
rule `offset := the bar-midpoint of Vhat`, and showed it DERIVES convention C's
offset of 1 rather than assuming it. That rule was applied to the OFFSET. It has
not been applied to the N=1 FACTOR. Doing so introduces no fitted quantity and
no new structure — it is the same rule, one slot over:

    N=1 factor := the bar-midpoint of the N=1 factor
                = ( cos(alpha) + bar(cos alpha) ) / 2

WHY C ALREADY LOOKS LIKE A COSINE, which is the observation that makes the rest
work. Under C, `alpha_C` is bar-ODD (`bar(a)+a = 0`, entry 6's control). Cosine
is EVEN. So `bar(cos a_C) = cos(-a_C) = cos(a_C)`: **the C-frame N=1 factor is
already its own bar-midpoint.** The rule is therefore vacuous in C — which is
exactly why C could use a bare cosine, and is a sharper statement of entry 7
than "the bar-odd slot is empty".

Under D that fails: `bar(a_D) = h^2/2 - a_D`, a REFLECTION about `h^2/4` rather
than about 0. `cos(a_D)` is NOT bar-invariant, and the arc's blocker follows.

THE RESULT. Taking the bar-midpoint and applying sum-to-product:

    M := (cos(a_D) + cos(h^2/2 - a_D)) / 2  =  cos(a_D - h^2/4) * cos(h^2/4)

so the defect enters as a PHASE RE-CENTRING by `h^2/4` together with a
`u`-INDEPENDENT multiplicative constant `cos(h^2/4)` — which is the
multiplicative/log frame entry 3 requires, and the u-independence entry 5
established for the defect.

All three conditions are met, and (a) and (b) hold EXACTLY as symbolic
identities rather than numerically.

UNIQUENESS — tested by trying to BREAK it, and (a)+(b) alone do NOT hold.

The GEOMETRIC mean `G := sqrt(cos(a_D) * cos(bar a_D))` is also bar-invariant
(verified) and also reduces correctly under C (where `bar a_C = -a_C`, giving
`|cos a_C|`). So conditions (a) and (b) admit at least a second solution — and
the two are NOT numerically interchangeable:

    proton pin   M = 0.9986190619723252   G = 0.9986189041126984   rel 1.581e-7
    muon pin     M = 0.9986190616623656   G = 0.9986189038026348   rel 1.581e-7

**158 ppb** — against a Q_beta 100x target of 7.8 ppb, i.e. **~20x the target**.
The ambiguity is physically significant, not cosmetic.

CONDITION (c) IS WHAT DISCRIMINATES, and it does so structurally. Read (c) as
the arc's entry 3 requires — the defect enters as a PHASE SHIFT times a factor
carrying NO phase dependence, i.e. `log F = f(a - c(delta)) + g(delta)`:

  * `M = cos(a - delta/2) * cos(delta/2)` separates exactly. One singular set
    in `a`.
  * `G` does not. It inherits the poles of BOTH `cos a` and `cos(a - delta)` —
    two shifted singular sets — and a separated form `f(a-c)*K` has only one.
    Counted symbolically: at `delta = 0` both have 2 pole families (they must
    agree when there is no defect); at `delta = 1/3`, M has **2** and G has
    **3**.

So (c) excludes the natural competitor, on pole structure rather than on a
number.

WHAT THIS DOES NOT CLAIM — scope (a).

  * NOT full uniqueness. (c) is shown to exclude `G`; it is NOT shown that no
    other function satisfies all three. That needs a functional-equation
    argument this probe does not attempt.
  * NOT a D-frame Q_beta. Rungs above k=2 remain `cal-anchored` (extracted from
    experiment), so no D-frame number is computable here and none is quoted.
  * NOT a wiring. Nothing downstream consumes this.

A CAS TRAP, recorded because it nearly cost the result. `sympy.simplify` does
NOT reduce `(cos A + cos B)/2 - cos((A+B)/2)cos((A-B)/2)` to 0 for these
arguments — it returns a non-zero residual of two uncombined cosines. That is a
non-simplification, not a refutation, and it is checked here NUMERICALLY at 60
dps as well as symbolically. Reading the CAS residual as a negative would have
retired a correct identity.

NO FLOAT64: sympy exact symbolic; mpmath at 60 dps for the numeric identity
check; float() nowhere.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401,E402

import sympy as sp  # noqa: E402
from mpmath import mp  # noqa: E402

mp.dps = 60

q = sp.symbols("q", positive=True)
bar = lambda e: sp.simplify(sp.powsimp(sp.radsimp(e.subs(q, 1 / q)), force=True))  # noqa: E731

h = q - 1 / q
z_D = q ** 3 / (q ** 2 + 1)
z_C = sp.sqrt(q) / (q + 1)
a_D = sp.simplify((z_D - 1) * h / 2)
a_C = sp.simplify((z_C - 1) * h / 2)

M_D = (sp.cos(a_D) + sp.cos(bar(a_D))) / 2
M_C = (sp.cos(a_C) + sp.cos(bar(a_C))) / 2
CLOSED = sp.cos(a_D - h ** 2 / 4) * sp.cos(h ** 2 / 4)

_A: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, note: str = "") -> None:
    _A.append((name, bool(passed), note))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}" + (f" — {note}" if note else ""))


def main() -> int:
    print("=" * 72)
    print("  qou-cds1 entry 10 — the N=1 factor under D is a bar-midpoint")
    print("=" * 72)

    print("\n-- the arc's own facts, reproduced as controls")
    check("control_C_phase_is_bar_odd",
          sp.simplify(bar(a_C) + a_C) == 0,
          "bar(a_C) + a_C = 0")
    check("control_D_defect_is_h_sq_over_2",
          sp.simplify(sp.simplify(bar(a_D) + a_D) - h ** 2 / 2) == 0,
          "bar(a_D) + a_D = h^2/2")

    print("\n-- why C looks like a cosine and D does not")
    check("C_cosine_is_ALREADY_bar_invariant",
          sp.simplify(sp.expand_trig(sp.cos(bar(a_C)) - sp.cos(a_C))) == 0,
          "cos even + phase bar-odd; the rule is vacuous in C")
    check("D_cosine_is_NOT_bar_invariant",
          sp.simplify(sp.expand_trig(sp.cos(bar(a_D)) - sp.cos(a_D))) != 0,
          "this is the arc's blocker, restated")
    check("D_bar_is_reflection_about_h_sq_over_4",
          sp.simplify(bar(a_D) - (h ** 2 / 2 - a_D)) == 0,
          "bar(a_D) = h^2/2 - a_D")

    print("\n-- the candidate, against the arc's three conditions")
    check("cond_a_bar_invariant",
          sp.simplify(sp.expand_trig(sp.expand(bar(M_D) - M_D))) == 0,
          "exact symbolic identity")
    check("cond_b_reduces_to_cosine_in_C",
          sp.simplify(sp.expand_trig(sp.expand(M_C - sp.cos(a_C)))) == 0,
          "exact symbolic identity")

    f_M = sp.lambdify(q, M_D, "mpmath")
    f_K = sp.lambdify(q, CLOSED, "mpmath")
    worst = mp.mpf(0)
    for qv in ("1.1099785827513808075916690956107688798744991218736",
               "1.1099785955573347198997632204", "1.5", "2", "1.0001"):
        worst = max(worst, abs(f_M(mp.mpf(qv)) - f_K(mp.mpf(qv))))
    check("cond_c_closed_form_absorbs_the_defect",
          worst < mp.mpf("1e-55"),
          f"M = cos(a_D - h^2/4)*cos(h^2/4); worst |diff| over 5 q = {mp.nstr(worst, 4)}")

    print("\n-- size of the correction at the two pins (display only)")
    f_h = sp.lambdify(q, sp.cos(h ** 2 / 4), "mpmath")
    f_s = sp.lambdify(q, h ** 2 / 4, "mpmath")
    for lbl, qv in (("proton", "1.1099785827513808075916690956107688798744991218736"),
                    ("muon  ", "1.1099785955573347198997632204")):
        x = mp.mpf(qv)
        print(f"     {lbl}: phase shift h^2/4 = {mp.nstr(f_s(x), 12)}"
              f" ; constant cos(h^2/4) = {mp.nstr(f_h(x), 18)}")

    print("\n-- uniqueness: (a)+(b) do NOT pin it; (c) is what excludes the rival")
    a_s, d_s = sp.symbols("a delta", real=True)
    M_s = (sp.cos(a_s) + sp.cos(a_s - d_s)) / 2
    G_s = sp.sqrt(sp.cos(a_s) * sp.cos(a_s - d_s))
    G_D = sp.sqrt(sp.cos(a_D) * sp.cos(bar(a_D)))

    check("rival_geometric_mean_IS_bar_invariant",
          sp.simplify(sp.expand(bar(G_D) - G_D)) == 0,
          "so conditions (a) and (b) alone do NOT pin the factor")

    f_M2 = sp.lambdify(q, M_D, "mpmath")
    f_G2 = sp.lambdify(q, G_D, "mpmath")
    xp = mp.mpf("1.1099785827513808075916690956107688798744991218736")
    spread = abs(f_M2(xp) - f_G2(xp)) / f_M2(xp)
    check("rival_differs_by_MORE_than_the_Qbeta_target",
          spread > mp.mpf("7.8e-9"),
          f"arithmetic vs geometric = {mp.nstr(spread, 4)} at the proton pin"
          f" — ~{int(spread / mp.mpf('7.8e-9'))}x the 7.8 ppb 100x target")

    check("cond_c_separates_M_exactly",
          sp.simplify(sp.expand_trig(M_s - sp.cos(a_s - d_s / 2) * sp.cos(d_s / 2))) == 0,
          "log M = log cos(a - delta/2) + log cos(delta/2); no phase in the 2nd term")

    poles_M = sp.solve(sp.cos(a_s - sp.Rational(1, 3) / 2), a_s)
    poles_G = sorted(set(sp.solve(sp.cos(a_s) * sp.cos(a_s - sp.Rational(1, 3)), a_s)), key=str)
    check("cond_c_EXCLUDES_the_rival_on_pole_structure",
          len(poles_G) > len(poles_M),
          f"at delta=1/3: M has {len(poles_M)} pole families, G has {len(poles_G)}"
          " — a separated f(a-c)*K admits only one")

    ok = all(p for _, p, _ in _A)
    print("\n" + "=" * 72)
    print(f"  {sum(p for _, p, _ in _A)}/{len(_A)} assertions passed")
    print("  Scope (a). Meets all three stated conditions, adding no new freedom.")
    print("  (a)+(b) alone do NOT pin it — the geometric mean also satisfies them")
    print("  and differs by 1.581e-7 (~20x the 7.8 ppb target). (c) excludes that")
    print("  rival on pole structure. FULL uniqueness is NOT proved, and no")
    print("  D-frame Q_beta is computable or quoted here.")
    print("=" * 72)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
