#!/usr/bin/env python3
"""What does the cusp factor 1/ℏ_q² multiply? — a dimension SUM, and the regular
part is a partition COUNT. Both sides are Wedderburn.

Bean `qou-brng`, residual (ii). Scope-(a) probe; emits no witness, wires nothing,
moves no number. Every assertion below is an identity over ℚ(q).

THE QUESTION, in the bean's own words. `BrunnianBindingChannel` leaves open
*"(ii) why the surviving count channel enters as a **bare integer** while the
self/mass channel keeps the full q-dimension self-trace `lw`"*, and the bean
records that (ii) and `BindingMassRung`'s residual are the same question from two
sides: *"integer vs q-dimension is exactly cusp-factor-absent vs
cusp-factor-present."*

VERDICT. The mass multiplier splits exactly, and BOTH pieces count partitions:

    lw/ℏ_q²  =  (Σ_{λ⊢4} dim V_λ)/4 · ℏ_q⁻²   +   (#{λ⊢4 : dim V_λ > 1})/4 · (q+1)²
             =  (10/4)·ℏ_q⁻²               +   (3/4)·(q+1)²

equivalently, Laurent in ℏ = ℏ_q = 1 − q⁻¹ about 0:

    lw/ℏ_q²  =  (5/2)·ℏ⁻²  +  0·ℏ⁻¹  +  3  +  3ℏ  +  (15/4)ℏ²  +  …

The singular coefficient is a quarter of the ordinary DIMENSION SUM (dims
1,3,2,3,1 over the five partitions of 4, total 10). The regular tail is a
quarter of the COUNT of partitions whose q-dimension actually deforms — the
three non-one-dimensional ones — times (q+1)². The mechanism is per-partition:

    dim_q(λ)  =  dim V_λ  +  m_λ · h²,      m = (0, 1, 1, 1, 0)

so `(4)` and `(1⁴)`, the one-dimensional irreps, have dim_q = 1 exactly and
contribute POLE ONLY; the three higher-dimensional irreps carry the whole
regular tail, and carry it IDENTICALLY (each 0, 1, 1, 5/4).

CONSEQUENCE FOR RESIDUAL (ii). The regular part is not a different KIND of
object from the pole — it is the non-abelian part of the same Wedderburn
spectrum. So relocating (ii) to the regular part does not relocate it toward
topology; whatever distinguishes the self channel from the mutual one is a
question about the PROVENANCE of the two multipliers (`lw` a Wedderburn
q-dimension sum, `M` a topological coordination count), not about where in the
ℏ-expansion to look. That provenance question survives intact and is the live
half of this bean.

WHAT IS AUTOMATIC AND WHAT IS NOT — the correction this probe's first version
needed. An earlier revision headlined "the pole coefficient is classical and
q-free". The q-freeness of the LEADING Laurent coefficient is AUTOMATIC: for any
g regular at ℏ = 0, the leading coefficient of g/ℏ² is g(0), i.e. the classical
value, whatever g is. Stated as a finding it is a tautology wearing a result's
clothes. What is substantive, and is what checks A5–A9 below establish:

  * the pole is PURE — the ℏ⁻¹ coefficient vanishes — and that purity IS lw's
    bar-evenness (h² is bar-even under q ↦ q⁻¹; h is bar-odd), not a separate
    fact about the cusp factor;
  * 5/2 is a quarter of the dimension SUM, derived from the hook-length formula
    here rather than asserted;
  * 3/4 is a quarter of the deformation COUNT, likewise derived. The corpus
    records 3/4 as a bare rational; this identifies it.

A TRAP, recorded because n = 4 is not generic. The clean form
`dim_q(λ) = dim V_λ + m_λ h²` with m_λ a CONSTANT holds at n = 2 and n = 4 and
FAILS at n = 3, 5, 6, where some dim_q needs h⁴ or higher. So at other n the
regular part of lw_n/ℏ_q² is not a multiple of (q+1)² and the two-term split
above does not exist. Do not carry this split up a tower on the strength of
n = 4; check A10, which measures exactly that.

NO EMPIRICAL INPUT. Every assertion is exact over ℚ(q), with dim_q computed from
the hook-length formula in the SYMMETRIC convention (verified against lw's
recorded closed form in A0 — the fake-degree convention gives a different
function and would silently change every number here). The anchor value is
reported for the record only, from the canonical 70-digit q₀, asserted on
nothing.

RELATION TO WHAT IS ALREADY RECORDED. `lw_is_framing_independent_probe.py`
established that lw is not a diagrammatic quantity at all (not writhe-, not
self-linking-valued) but `(1/4)·Σ_{λ⊢4} dim_q V_λ`, and the bean records the
consequent reframing as "A reframing, NOT an answer." This probe takes the next
step on the same object. It does not touch the bean's TITLE claim (saturated
fraction = ℏ_q²), which AGENTS.md records as suspect numerology with the
volume-defect route refuted.
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

q, hb = sp.symbols("q hb", positive=True)


def partitions(n: int, mx: int | None = None):
    """Partitions of n in weakly decreasing order."""
    mx = n if mx is None else mx
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def hook_lengths(lam: tuple[int, ...]) -> list[int]:
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    return [lam[i] - j - 1 + conj[j] - i - 1 + 1
            for i in range(len(lam)) for j in range(lam[i])]


def q_int_symmetric(k: int):
    """[k]_q = (q^k - q^-k)/(q - q^-1), written as a Laurent polynomial."""
    return sum(q ** (k - 1 - 2 * i) for i in range(k))


def dim_q(lam: tuple[int, ...]):
    """q-analogue of the hook-length formula, symmetric convention."""
    n = sum(lam)
    num = sp.prod([q_int_symmetric(k) for k in range(1, n + 1)])
    den = sp.prod([q_int_symmetric(x) for x in hook_lengths(lam)])
    return sp.cancel(num / den)


def deformation_multiplicity(lam: tuple[int, ...]):
    """m_lam with dim_q(lam) = dim V_lam + m_lam * h^2, or None if no such constant."""
    h = q - 1 / q
    d = sp.expand(dim_q(lam))
    classical = sp.Integer(d.subs(q, 1))
    rest = sp.simplify(sp.expand(d - classical))
    if rest == 0:
        return classical, sp.Integer(0)
    m = sp.simplify(sp.cancel(rest / h ** 2))
    return classical, (None if m.free_symbols else m)


def main() -> int:
    h = q - 1 / q
    hq = 1 - 1 / q                                   # ℏ_q
    lw = sp.Rational(5, 2) + sp.Rational(3, 4) * h ** 2

    P4 = list(partitions(4))
    dims, mults = {}, {}
    for lam in P4:
        dims[lam], mults[lam] = deformation_multiplicity(lam)
    dim_sum = sum(int(v) for v in dims.values())
    mult_sum = sum(int(v) for v in mults.values() if v is not None)
    n_deformed = sum(1 for lam in P4 if int(dims[lam]) > 1)

    checks: list[tuple[str, bool, str]] = []

    # (A0) the hook-length dim_q here is the convention lw is built from.
    checks.append((
        "dimq_convention_matches_lw",
        sp.simplify(sp.expand(sum(dim_q(l) for l in P4) / 4 - lw)) == 0,
        "(1/4)*sum_(lam|-4) dim_q(lam) == lw, in the SYMMETRIC convention",
    ))

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

    # (A5) the pole is PURE: no simple-pole term. Substantive, unlike (A6).
    checks.append((
        "pole_is_pure_no_simple_pole",
        sp.simplify(coeffs[-1]) == 0,
        "coefficient of hbar^-1 vanishes",
    ))

    # (A6) and the purity IS lw's bar-evenness, not a fact about the cusp factor.
    checks.append((
        "pole_purity_is_bar_evenness",
        (sp.simplify(lw - lw.subs(q, 1 / q)) == 0
         and sp.simplify(sp.diff(lw.subs(q, 1 / (1 - hb)), hb).subs(hb, 0)) == 0),
        "lw(q) == lw(1/q)  AND  d(lw)/d(hbar)|_0 == 0 (the same statement)",
    ))

    # (A7) the pole coefficient is a quarter of the classical DIMENSION SUM,
    #      with the dimensions derived from the hook-length formula above.
    classical = sp.Rational(dim_sum, 4)
    checks.append((
        "pole_coefficient_is_classical_dimension_sum",
        (sp.simplify(coeffs[-2] - classical) == 0
         and sp.simplify(lw.subs(q, 1) - classical) == 0),
        f"hbar^-2 coeff == lw(q=1) == (1/4)*sum dim V_lam == {dim_sum}/4",
    ))

    # (A8) per-partition mechanism: dim_q = dim + m*h^2, and only the
    #      one-dimensional irreps have m = 0.
    checks.append((
        "deformation_multiplicity_tracks_nontriviality",
        (all(mults[lam] is not None for lam in P4)
         and all((int(mults[lam]) == 0) == (int(dims[lam]) == 1) for lam in P4)),
        "dim_q(lam) = dim V_lam + m_lam*h^2 with m_lam = 0 iff dim V_lam = 1",
    ))

    # (A9) THE IDENTIFICATION: the regular part is a quarter of the COUNT of
    #      deforming partitions — so 3/4 is not a bare rational.
    checks.append((
        "regular_part_is_deformation_count",
        (mult_sum == n_deformed
         and sp.simplify(lw - sp.Rational(1, 4) * (dim_sum + mult_sum * h ** 2)) == 0
         and sp.simplify(coeffs[0] - sp.Rational(mult_sum, 4) * 4) == 0),
        f"lw = (1/4)[sum dim + h^2 * #(dim>1)] = (1/4)[{dim_sum} + {mult_sum}h^2]; "
        f"regular coeff 3 == (#/4)*(q+1)^2 at q=1",
    ))

    # (A10) THE TRAP: the constant-m structure is special to n in {2,4}.
    clean = {}
    for n in (2, 3, 4, 5, 6):
        clean[n] = all(deformation_multiplicity(l)[1] is not None
                       for l in partitions(n))
    checks.append((
        "constant_m_structure_is_special_to_n_2_and_4",
        clean == {2: True, 3: False, 4: True, 5: False, 6: False},
        "dim_q = dim + m*h^2 with constant m: holds at n=2,4; fails at n=3,5,6",
    ))

    print("=" * 78)
    print(" lw/hbar_q^2 : pole = dimension SUM, regular = partition COUNT")
    print("                                      (bean qou-brng, residual ii)")
    print("=" * 78)
    print("\n  Laurent series in hbar_q about 0 (exact, over Q):")
    print(f"    lw/hbar_q^2 = {sp.nsimplify(ser)}")
    print("\n  per partition of 4 (dim_q from the hook-length formula, symmetric):")
    print("    lam           dim   dim_q                      m_lam   contributes")
    for lam in P4:
        d = sp.expand(dim_q(lam))
        m = mults[lam]
        kind = "pole only" if int(m) == 0 else "pole + regular"
        print(f"    {str(lam):<13} {str(dims[lam]):>3}   {str(d):<26} "
              f"{str(m):>5}   {kind}")
    print(f"\n    sum dim V_lam          = {dim_sum}   -> pole coeff {dim_sum}/4 "
          f"= {classical}")
    print(f"    #(lam : dim V_lam > 1) = {n_deformed}   -> regular (3/4)(q+1)^2, "
          f"value {sp.Rational(n_deformed,4)*4} at q=1")
    print(f"    lw = (1/4)[{dim_sum} + {mult_sum}*h^2] "
          f"= {sp.nsimplify(sp.expand(lw))}")
    print("\n  constant-m structure by n (the trap — n=4 is NOT generic):")
    for n, ok_n in clean.items():
        print(f"    n={n}: {'clean (dim + m h^2)' if ok_n else 'NOT clean (needs h^4+)'}")

    # the anchor value, from the canonical q0 — reported, asserted on nothing.
    lw_num = sp.lambdify(q, lw, "mpmath")(Q_MP)
    print("\n  for the record, at the canonical proton pin q0 (70-digit Q_MP):")
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
    print("\n  SCOPE (a). Both pieces of lw/hbar_q^2 count partitions, so moving")
    print("  residual (ii) to the regular part does not move it toward topology.")
    print("  NOT a derivation of (ii): why binding is a topological count while")
    print("  mass is a Wedderburn q-dimension sum is untouched and is the live half.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
