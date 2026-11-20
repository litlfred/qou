#!/usr/bin/env python3
"""Does the cusp factor 1/ℏ_q² "keep the full q-dimension"? — NO, not at the pole.

Bean `qou-brng`, residual (ii). Scope-(a) probe; emits no witness, wires nothing,
moves no number.

THE QUESTION, in the bean's own words. `BrunnianBindingChannel` leaves open
*"(ii) why the surviving count channel enters as a **bare integer** while the
self/mass channel keeps the full q-dimension self-trace `lw`"*, and the bean
records that (ii) and `BindingMassRung`'s residual are the same question from two
sides: *"integer vs q-dimension is exactly cusp-factor-absent vs
cusp-factor-present."*

VERDICT, stated up front. The contrast (ii) is built on does NOT exist in the
singular part. Writing ℏ = ℏ_q = 1 − q⁻¹ and expanding the mass multiplier
lw/ℏ_q² as a Laurent series in ℏ about 0:

    lw/ℏ_q²  =  (5/2)·ℏ⁻²  +  0·ℏ⁻¹  +  3  +  3ℏ  +  (15/4)ℏ²  +  …

and the pole coefficient 5/2 is EXACTLY the CLASSICAL, undeformed dimension sum

    5/2  =  lw(q=1)  =  (1/4)·Σ_{λ⊢4} dim V_λ  =  10/4,
    dims over the five partitions of 4: 1, 3, 2, 3, 1  (sum 10).

So the cusp factor does not multiply a q-dimension at the pole — it multiplies a
rational multiple of an ordinary INTEGER count of ordinary dimensions. Every bit
of lw's q-dependence sits in the REGULAR part. At the pole the two channels are
therefore MORE alike than (ii) presumes, not less: one is an integer coordination
count, the other a quarter of the integer 10.

WHAT THIS IS AND IS NOT. It is a structural narrowing, scope (a): whatever
distinguishes the self channel from the mutual one, it CANNOT be read off the
cusp pole, because the pole is classical on both sides. It is NOT a derivation of
(ii), and it does not say why binding is a count while mass is a q-dimension sum
— that question survives intact and is the live half of this bean.

It also does not touch the bean's TITLE claim (saturated fraction = ℏ_q²), which
AGENTS.md records as suspect numerology with the volume-defect route refuted. No
empirical input of any kind enters below: every assertion is an identity over ℚ.

RELATION TO WHAT IS ALREADY RECORDED. `lw_is_framing_independent_probe.py`
established that lw is not a diagrammatic quantity at all (not writhe-, not
self-linking-valued) but `(1/4)·Σ_{λ⊢4} dim_q V_λ`, and the bean records the
consequent reframing as "A reframing, NOT an answer." This probe takes the next
step on the same object: it asks what the cusp factor actually multiplies, and
finds the answer is classical. The bean describes lw/ℏ_q² as "an order-2 pole
with residue `lw`"; the precise statement is that the ℏ⁻² coefficient is lw(1),
not lw(q), and that there is no ℏ⁻¹ term at all — the pole is pure.

EVIDENCE, two kinds kept separate (AGENTS.md).

  (A) EXACT, over ℚ via sympy Rational — no floats anywhere in the chain:
      the two closed forms for lw agree identically; h = ℏ_q·(q+1); the
      split lw/ℏ_q² = (5/2)/ℏ_q² + (3/4)(q+1)²; the five Laurent
      coefficients; and pole-coefficient == lw(1) == (1/4)Σ dim V_λ.

  (B) The anchor value, reported for the record at OUTPUT_DPS from the
      CANONICAL q₀ (q_parameter.Q_MP, 70-digit), not a pasted literal.
"""
from __future__ import annotations

import sys  # noqa: E402
from pathlib import Path  # noqa: E402

HERE = Path(__file__).resolve().parent
COMP = next(p for p in HERE.parents if p.name == "computations")
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))

import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps, fmt, OUTPUT_DPS  # noqa: E402
from q_parameter import Q_MP  # noqa: E402

set_compute_dps()

# Dimensions of the irreducible S_4 modules, by partition of 4.
DIMS_4 = {(4,): 1, (3, 1): 3, (2, 2): 2, (2, 1, 1): 3, (1, 1, 1, 1): 1}


def main() -> int:
    q, hb = sp.symbols("q hb", positive=True)
    h = q - 1 / q
    hq = 1 - 1 / q                                  # ℏ_q
    lw = sp.Rational(5, 2) + sp.Rational(3, 4) * h ** 2

    checks: list[tuple[str, bool, str]] = []

    # (A1) lw's two recorded closed forms are the same rational function.
    checks.append((
        "lw_closed_forms_agree",
        sp.simplify(lw - (3 * q ** 2 + 4 + 3 / q ** 2) / 4) == 0,
        "5/2 + (3/4)h^2  ==  (3q^2 + 4 + 3q^-2)/4  over Q(q)",
    ))

    # (A2) h factors through ℏ_q — the reason the split below exists at all.
    checks.append((
        "h_factors_through_hbar_q",
        sp.simplify(h - hq * (q + 1)) == 0,
        "h = q - q^-1 = hbar_q * (q+1)",
    ))

    # (A3) the mass multiplier splits into a pure pole plus a polynomial.
    checks.append((
        "mass_multiplier_splits",
        sp.simplify(lw / hq ** 2
                    - (sp.Rational(5, 2) / hq ** 2
                       + sp.Rational(3, 4) * (q + 1) ** 2)) == 0,
        "lw/hbar_q^2 = (5/2)/hbar_q^2 + (3/4)(q+1)^2",
    ))

    # (A4) the Laurent coefficients in ℏ_q, exactly.
    M_hb = sp.simplify((lw / hq ** 2).subs(q, 1 / (1 - hb)))
    ser = sp.expand(sp.series(M_hb, hb, 0, 3).removeO())
    coeffs = {k: sp.simplify(ser.coeff(hb, k)) for k in (-2, -1, 0, 1, 2)}
    expected = {-2: sp.Rational(5, 2), -1: sp.Integer(0), 0: sp.Integer(3),
                1: sp.Integer(3), 2: sp.Rational(15, 4)}
    checks.append((
        "laurent_coefficients_exact",
        all(sp.simplify(coeffs[k] - expected[k]) == 0 for k in expected),
        "hbar^-2..2 coefficients are 5/2, 0, 3, 3, 15/4",
    ))

    # (A5) the pole is PURE: no simple-pole term.
    checks.append((
        "pole_is_pure_no_simple_pole",
        sp.simplify(coeffs[-1]) == 0,
        "coefficient of hbar^-1 vanishes",
    ))

    # (A6) THE POINT: the pole coefficient is the CLASSICAL dimension sum.
    classical = sp.Rational(sum(DIMS_4.values()), 4)
    checks.append((
        "pole_coefficient_is_classical_dimension_sum",
        (sp.simplify(coeffs[-2] - classical) == 0
         and sp.simplify(lw.subs(q, 1) - classical) == 0),
        f"hbar^-2 coeff == lw(q=1) == (1/4)*sum_(lam|-4) dim V_lam "
        f"== {sum(DIMS_4.values())}/4",
    ))

    # (A7) and it carries no q at all — a sanity check on "classical".
    checks.append((
        "pole_coefficient_is_q_free",
        coeffs[-2].free_symbols == set(),
        "the hbar^-2 coefficient contains no q",
    ))

    print("=" * 78)
    print(" lw/hbar_q^2 : the cusp pole is CLASSICAL  (bean qou-brng, residual ii)")
    print("=" * 78)
    print("\n  Laurent series in hbar_q about 0 (exact, over Q):")
    print(f"    lw/hbar_q^2 = {sp.nsimplify(ser)}")
    print(f"\n  partitions of 4 and dim V_lam: "
          f"{ {''.join(map(str,k)): v for k, v in DIMS_4.items()} }")
    print(f"  sum dim V_lam = {sum(DIMS_4.values())};  (1/4)*sum = {classical}")
    print(f"  lw(q=1)       = {sp.simplify(lw.subs(q, 1))}")
    print(f"  hbar^-2 coeff = {coeffs[-2]}   <- classical, q-free")

    # (B) the anchor value, from the canonical q0 — reported, asserted on nothing.
    lw_num = sp.lambdify(q, lw, "mpmath")(Q_MP)
    print(f"\n  for the record, at the canonical proton pin q0 (70-digit Q_MP):")
    print(f"    lw(q0)        = {fmt(mp.mpf(lw_num))}")
    print(f"    hbar_q(q0)    = {fmt(1 - 1 / Q_MP)}")
    print(f"    OUTPUT_DPS    = {OUTPUT_DPS}")

    print("\n  CHECKS")
    ok = True
    for name, passed, why in checks:
        print(f"    [{'PASS' if passed else 'FAIL'}] {name}")
        print(f"           {why}")
        ok = ok and passed
    print(f"\n  {sum(1 for _, p, _ in checks if p)}/{len(checks)} exact checks passed")
    print("\n  SCOPE (a): the cusp pole cannot distinguish the two channels, since")
    print("  it is classical on both sides. NOT a derivation of residual (ii):")
    print("  why binding is a count while mass is a q-dimension sum is untouched.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
