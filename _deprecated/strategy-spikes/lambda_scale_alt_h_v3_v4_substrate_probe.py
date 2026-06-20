#!/usr/bin/env python3
"""Strategy H falsification probe: V_3 and V_4 are FITS, not refinements.

User challenge (2026-05-22, post-/coordinate):
  "where refinement? fitting? no good if so"

Per AGENTS.md §"three-calibration discipline" + PR #701 + PR #888,
any λ_scale candidate whose normalisation is PINNED by a desired
classical limit (rather than DERIVED from a substrate measure) is
a 4th calibration in disguise — same antipattern as
LAMBDA_PROTON_FITTED_FROM_CODATA before PR #895 rescued it with
the proved Family A theorem.

This probe documents that V_3 and V_4 (proposed in the earlier
PR #916 brief addendum as "substrate-pure refinement candidates")
fail this test: their normalisations 5/48 and 1/48 are CHOSEN to
make each evaluate to 5/2 at q=1, not derived from any natural
measure on H_4. They are FIT-SIBLINGS of Family A, not refinements
of it.

Conclusion: the V_3/V_4 axis is CLOSED-NEGATIVE for substrate-pure
work. The brief addendum §Strategy H is updated in the
accompanying commit to file V_3/V_4 alongside the q-dilog Tier 0
spike (af2d27ee on main) in the "closed-negative 2026-05-22"
section.

V_3 = (5/48) · Σ_{λ ⊢ 4} dim_q V_λ · dim_cl V_λ
    = (5/6) · (3 + h²)
    = 5/2 + (5/6)·h²

V_4 = (1/48) · Σ_{λ ⊢ 4} hook_cl V_λ · dim_q V_λ
    = (1/12) · (30 + 7·h²)
    = 5/2 + (7/12)·h²

The normalisation constants (5/48 for V_3, 1/48 for V_4) are
PINNED by the requirement that each evaluates to 5/2 at q = 1
(matching Family A's leading coefficient). They are not derived
from a category-theoretic measure; they are fits to a desired
classical limit.

Findings (this probe documents them numerically):

1. Both V_3 and V_4 give 5/2 at q=1 by construction (the 1/48 and
   5/48 normalizations are fit, not derived from any natural
   Frobenius / Plancherel measure on H_4).

2. V_3 has c_2 = +5/6 (LARGER than Family A's +3/4); evaluates
   FURTHER from the CODATA-derived target than Family A.

3. V_4 has c_2 = +7/12 (SMALLER than Family A's +3/4); evaluates
   CLOSER to the CODATA target than Family A by ~0.7 % (still
   ~2.6 % off CODATA, vs Family A's ~2.9 % off).

4. NEITHER variant has a structural justification that picks it
   over Family A: all three (V_1, V_3, V_4) are valid Wedderburn
   linear functionals on the H_4 character table, normalised
   identically to 5/2 at q=1; they differ only in the
   classical-side weight (constant 1/4 for V_1, dim_cl V_λ for
   V_3, hook_cl(V_λ) for V_4). No category-theoretic principle
   in the QOU framework selects one weighting over another.

CONCLUSION: V_3 and V_4 are not substrate-pure REFINEMENTS of
Family A; they are SIBLINGS that share Family A's leading 5/2
and differ in the (substrate-irrelevant) classical-side weight.
The framework's 3 % CODATA gap is not closeable by Wedderburn-
weighting refinements; the q-dilog tower (Strategies A/B from
the original brief) remains the recommended primary direction.
"""
from __future__ import annotations
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402

mp.mp.dps = 80


# Classical dimensions + hook products for partitions of 4 (S_4)
PARTITIONS_OF_4 = [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]
DIM_CL = {(4,): 1, (3, 1): 3, (2, 2): 2, (2, 1, 1): 3, (1, 1, 1, 1): 1}
HOOK_CL = {(4,): 24, (3, 1): 8, (2, 2): 12, (2, 1, 1): 8, (1, 1, 1, 1): 24}


def qint(n: int, q: sp.Expr) -> sp.Expr:
    """q-integer [n]_q = (q^n - q^{-n}) / (q - q^{-1})."""
    return sp.simplify((q ** n - q ** (-n)) / (q - 1 / q))


def dim_q_lambda(shape: tuple, q: sp.Expr) -> sp.Expr:
    """Quantum dimension of irrep V_λ of H_n(q), n=|λ|, via hook-content."""
    if shape == (4,):
        return sp.Integer(1)
    if shape == (3, 1) or shape == (2, 1, 1):
        return qint(3, q)
    if shape == (2, 2):
        return sp.cancel(qint(4, q) / qint(2, q))
    if shape == (1, 1, 1, 1):
        return sp.Integer(1)
    raise ValueError(f"Unsupported shape: {shape}")


def main() -> int:
    w = WitnessBuilder(
        "lambda-scale-alt-h-v3-v4-substrate-probe",
        engine="mpmath+sympy",
    )
    w.set_description(
        "Strategy H FALSIFICATION probe (post-user-challenge "
        "2026-05-22): the V_3 and V_4 normalisations (5/48 and 1/48) "
        "are FITS to the 5/2-at-q=1 classical limit, NOT derivations "
        "from a category-theoretic measure on H_4. They should not be "
        "presented as substrate-pure refinements of Family A — they "
        "are fit-siblings, exactly the antipattern that PR #888 + "
        "#895 escaped by moving from LAMBDA_*_FITTED_FROM_CODATA to "
        "the proved Family A theorem. This probe documents the "
        "fit-status numerically so the V_3/V_4 axis is closed-negative "
        "going forward."
    )
    w.set_content_block("prop:flavor-dressed-mass-from-substrate-split")
    w.add_parameter("dps", 80)

    q = sp.Symbol("q", positive=True, real=True)
    h = q - 1 / q

    # Build symbolic closed forms
    dim_q_table = {shape: dim_q_lambda(shape, q) for shape in PARTITIONS_OF_4}

    # V_1 (Family A) reference
    V1_sym = sp.cancel(sum(dim_q_table.values()) / 4)
    V1_in_h = sp.Rational(5, 2) + sp.Rational(3, 4) * h ** 2

    # V_3 = (5/48) Σ dim_q · dim_cl
    V3_raw = sum(DIM_CL[shape] * dim_q_table[shape] for shape in PARTITIONS_OF_4)
    V3_sym = sp.cancel(sp.Rational(5, 48) * V3_raw)
    V3_in_h = sp.Rational(5, 2) + sp.Rational(5, 6) * h ** 2

    # V_4 = (1/48) Σ hook_cl · dim_q
    V4_raw = sum(HOOK_CL[shape] * dim_q_table[shape] for shape in PARTITIONS_OF_4)
    V4_sym = sp.cancel(sp.Rational(1, 48) * V4_raw)
    V4_in_h = sp.Rational(5, 2) + sp.Rational(7, 12) * h ** 2

    print("Closed-form derivations:")
    print(f"  V_1 (Family A) = (1/4) Σ dim_q V_λ = {V1_sym}")
    print(f"                 = 5/2 + (3/4)·h²")
    print(f"  V_3 = (5/48) Σ dim_q V_λ · dim_cl V_λ = {V3_sym}")
    print(f"      = 5/2 + (5/6)·h²")
    print(f"  V_4 = (1/48) Σ hook_cl V_λ · dim_q V_λ = {V4_sym}")
    print(f"      = 5/2 + (7/12)·h²")
    print()

    # Verify h² identities algebraically
    for label, q_form, h_form in [
        ("V_1", V1_sym, V1_in_h),
        ("V_3", V3_sym, V3_in_h),
        ("V_4", V4_sym, V4_in_h),
    ]:
        diff = sp.simplify(h_form.subs(h ** 2, q ** 2 - 2 + q ** (-2)) - q_form)
        if diff == 0:
            print(f"  ✓ {label} q-form ≡ h-form algebraically")
        else:
            print(f"  ✗ {label} mismatch: {diff}")
        w.add_assertion(
            f"{label}_h_form_equals_q_form",
            computed=str(diff),
            expected="0",
            tolerance=None,
        )
    print()

    # Numerical at q_0
    Q0 = mp.mpf(Q_50_DIGIT_STR)
    H0 = Q0 - 1 / Q0
    V1_num = mp.mpf("2.5") + mp.mpf("0.75") * H0 ** 2
    V3_num = mp.mpf("2.5") + mp.mpf("5") / 6 * H0 ** 2
    V4_num = mp.mpf("2.5") + mp.mpf("7") / 12 * H0 ** 2

    target_codata = mp.mpf("2.4599527869")
    V1_vs_codata = (V1_num - target_codata) / target_codata
    V3_vs_codata = (V3_num - target_codata) / target_codata
    V4_vs_codata = (V4_num - target_codata) / target_codata

    V3_vs_V1 = (V3_num - V1_num) / V1_num
    V4_vs_V1 = (V4_num - V1_num) / V1_num

    print(f"At q_0 = {mp.nstr(Q0, 15)}, h² = {mp.nstr(H0**2, 15)}:")
    print(f"  V_1 (Family A) = {mp.nstr(V1_num, 16)}")
    print(f"  V_3            = {mp.nstr(V3_num, 16)}")
    print(f"  V_4            = {mp.nstr(V4_num, 16)}")
    print(f"  CODATA target  = {mp.nstr(target_codata, 16)}")
    print()
    print("Distance to CODATA (retired target — informational only):")
    print(f"  V_1 vs CODATA = {mp.nstr(V1_vs_codata * 100, 6)} %")
    print(f"  V_3 vs CODATA = {mp.nstr(V3_vs_codata * 100, 6)} %  (worse than Family A)")
    print(f"  V_4 vs CODATA = {mp.nstr(V4_vs_codata * 100, 6)} %  (better than Family A by ~0.7%)")
    print()
    print("Distance to Family A (the framework's substrate λ_scale):")
    print(f"  V_3 vs V_1 = {mp.nstr(V3_vs_V1 * 100, 6)} %")
    print(f"  V_4 vs V_1 = {mp.nstr(V4_vs_V1 * 100, 6)} %")
    print()

    # Verdict on substrate justification
    print("Substrate-justification verdict:")
    print("  V_3 normalization 5/48: chosen to give 5/2 at q=1")
    print("    (Σ dim_q·dim_cl at q=1 = 24; 24·5/48 = 5/2 ✓)")
    print("    No category-theoretic measure that naturally gives 5/48.")
    print()
    print("  V_4 normalization 1/48: chosen to give 5/2 at q=1")
    print("    (Σ hook_cl·dim at q=1 = 120; 120/48 = 5/2 ✓)")
    print("    Hook-weighting is a Frobenius-Schur-like measure but")
    print("    the 1/48 = 1/(2·n!) normalisation is still fit-pinned.")
    print()
    print("  Family A normalization 1/4: chosen to give 5/2 at q=1")
    print("    (Σ dim_q at q=1 = 10 = #involutions(S_4); 10/4 = 5/2 ✓)")
    print("    Involution-count interpretation matches Frobenius's")
    print("    'sum of squares of involutions' identity at q=1.")
    print()
    print("ALL THREE share the SAME leading 5/2; differ only in c_2.")
    print("NONE has a category-theoretic principle that selects it over")
    print("the others — V_1 (Family A) is the cluster's chosen baseline,")
    print("V_3 widens the framework gap, V_4 narrows it slightly (~0.7 %).")
    print()
    print("CONCLUSION: V_3 / V_4 axis does NOT close the 3 % framework")
    print("CODATA gap on m_p. The q-dilog tower (Strategies A/B from")
    print("docs/agent-briefs/2026-05-22-lambda-scale-qdilog-tower-direct.md)")
    print("remains the recommended primary direction.")

    w.add_data("V1_family_A_closed_form_q", str(V1_sym))
    w.add_data("V1_family_A_closed_form_h", "5/2 + (3/4)·h²")
    w.add_data("V3_closed_form_q", str(V3_sym))
    w.add_data("V3_closed_form_h", "5/2 + (5/6)·h²")
    w.add_data("V4_closed_form_q", str(V4_sym))
    w.add_data("V4_closed_form_h", "5/2 + (7/12)·h²")
    w.add_data("V1_at_q0", mp.nstr(V1_num, 20))
    w.add_data("V3_at_q0", mp.nstr(V3_num, 20))
    w.add_data("V4_at_q0", mp.nstr(V4_num, 20))
    w.add_data("codata_target", mp.nstr(target_codata, 20))
    w.add_data("V1_vs_codata_pct", mp.nstr(V1_vs_codata * 100, 10))
    w.add_data("V3_vs_codata_pct", mp.nstr(V3_vs_codata * 100, 10))
    w.add_data("V4_vs_codata_pct", mp.nstr(V4_vs_codata * 100, 10))
    w.add_data("V3_vs_V1_pct", mp.nstr(V3_vs_V1 * 100, 10))
    w.add_data("V4_vs_V1_pct", mp.nstr(V4_vs_V1 * 100, 10))
    w.add_data(
        "substrate_justification_verdict",
        "no category-theoretic principle selects V_3 or V_4 over Family A; "
        "all three normalisations are pinned by the classical 5/2 at q=1; "
        "V_3 widens the CODATA gap, V_4 narrows it by 0.7 % but still 2.6 % off",
    )
    w.add_data(
        "framework_gap_closed",
        "no (3% CODATA gap on m_p remains; q-dilog tower is the recommended direction)",
    )

    # Per probe_phiq_n_star_rule.py convention: this probe DOCUMENTS a
    # finding (no substrate-pure refinement among V_3/V_4); the
    # passing assertion is "no refinement closes the gap" (= True).
    no_refinement_closes_gap = int(
        abs(V3_vs_codata) > mp.mpf("0.01")
        and abs(V4_vs_codata) > mp.mpf("0.01")
    )
    w.add_assertion(
        "no_v3_v4_refinement_closes_3pct_codata_gap",
        computed=no_refinement_closes_gap,
        expected=1,
        tolerance=None,
        source=(
            "V_3 and V_4 are Wedderburn-sum siblings of Family A; "
            "both share 5/2 at q=1 and have positive c_2; neither "
            "closes the framework's 3 % CODATA gap on m_p."
        ),
    )

    out = w.save()
    print(f"\nWitness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
