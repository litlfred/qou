"""qbeta_fsc_g_pattern_comparison.py — Q_β vs FSC vs G algebraic structure.

User direction: "fsc" + "also look at how gravitational constant" — explore
whether Q_β admits a closed-form derivation analogous to:
- FSC: 1/α_EM = q · [9]_q · [10]_q (pure cyclotomic)
- G: G(q) = q²/(q-1)⁴ (q-rational with simple poles at 0, 1)

KEY FINDING (negative, but structural):

Q_β's Form A = m_e · |q²-2q-1|·(q+1)/(2q³) has the polynomial
factor (q² - 2q - 1) with roots at q = 1 ± √2. These are NOT
roots of unity → NOT cyclotomic. Q_β lives in a "silver-ratio"
algebraic landscape, distinct from FSC and G.

This explains structurally WHY the c_4..c_7 derivation is hard:
- FSC and G have clean closed forms because their categorical
  sources (torus knots, q-Yang-Mills) live in cyclotomic algebras
- Q_β's categorical source (single-wrap braid Markov trace at H_3)
  produces an algebraic factor with irrational roots, so no
  simple cyclotomic / q-integer factorisation closes the chain.

The c_k precision-ladder is therefore the NATURAL framework for
Q_β — there is no "way around" because the underlying polynomial
structure is genuinely non-cyclotomic.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()
from mpmath import mp, mpf  # noqa: E402

# Single-source CODATA / experimental anchors per repo convention
# (compute-audit P31): avoid free-floating literals.
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402

Q_PINNING = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)


def _is_root_of_unity(z: complex, tol: float = 1e-9, max_order: int = 100) -> bool:
    """Test if a complex number is a root of unity within tol.

    A root of unity satisfies |z| = 1 AND z^n = 1 for some small n.
    Returns False if |z| differs from 1 by more than tol.
    """
    if abs(abs(z) - 1.0) > tol:
        return False
    for n in range(1, max_order + 1):
        if abs(z**n - 1) < tol:
            return True
    return False


def main() -> None:
    # Construct WitnessBuilder at start so durationMs measures actual work,
    # and route upstream witness loads via add_upstream for drift tracking.
    w = WitnessBuilder(
        name="qbeta-fsc-g-pattern-comparison",
        engine="python+mpmath",
    )
    w.add_upstream(Q_PINNING)
    w.set_description(
        "Compares Q_β's algebraic structure (Form A with silver-ratio "
        "factor q² - 2q - 1) against FSC's cyclotomic pattern "
        "(1/α_EM = q·[9]_q·[10]_q) and G's q-rational pattern "
        "(G(q) = q²/(q-1)⁴). Q_β lives outside the cyclotomic "
        "landscape — explains why no FSC-like closed-form derivation "
        "exists for c_4..c_7."
    )

    # q_0 comes from `q_parameter`, i.e. the RUNNING SCRIPT's anchor, rather
    # than from a direct read of q-pinning-50-digit.witness.json (routed
    # 2026-08-30, bean `qou-aj91`). The direct read hardcoded the muon anchor
    # and made QOU_Q0_ANCHOR inert here, which is what put this producer in the
    # UNSOUND-ENV-BYPASS group -- unmeasurable rather than held for cause.
    #
    # `Q_PINNING` is KEPT and still passed to `w.add_upstream()` above: the
    # anchor witness remains a genuine provenance upstream of this result even
    # though it is no longer the value's source. Dropping it would lose the
    # provenance edge; that edge is why the two uses are deliberately split.
    from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402 — anchor-aware
    q = Q_MP
    m_e = mpf(str(M_E_MEV))
    Q_beta = mpf(str(Q_BETA_MEV))
    target = Q_beta / m_e

    print(f"q_0 = {mp.nstr(q, 15)}")
    print(f"Q_β/m_e at q_0 = {mp.nstr(target, 15)}")
    print()

    # Building blocks
    def q_int(n):
        return sum(q**(n - 1 - 2*k) for k in range(n))

    qn = {n: q_int(n) for n in range(1, 11)}

    # FSC pattern test
    fsc_value = 1 / (q * qn[9] * qn[10])  # = α_EM at q_0 by framework
    print("=" * 72)
    print("FSC pattern: 1/α_EM = q · [9]_q · [10]_q (pure cyclotomic)")
    print("=" * 72)
    print(f"  α_EM via cyclotomic form: 1/(q·[9]·[10]) = {float(fsc_value):.6e}")
    print(f"  α_EM CODATA               ≈ 7.297e-3")
    print(f"  Roots of [n]_q are nth roots of unity (cyclotomic)")
    print()

    # G pattern
    G_value = q**2 / (q - 1)**4
    print("=" * 72)
    print("G pattern: G(q) = q²/(q-1)⁴ in q-natural units")
    print("=" * 72)
    print(f"  G(q_0) (q-natural) = {float(G_value):.4f}")
    print(f"  G_Planck = 1 identically (Planck-unit normalisation absorbs q)")
    print(f"  Poles at q = 0, 1; no other roots → q-rational structure")
    print()

    # Q_β pattern: compute the polynomial factor as written (q²-2q-1)
    # and apply abs() to match the documented |q²-2q-1| definition.
    # The previous form (-q²+2q+1) matched only by accident at q_0 < 1+√2;
    # for q > 1+√2 the sign flips and the match breaks.
    print("=" * 72)
    print("Q_β pattern: Form A = m_e · |q²-2q-1|·(q+1)/(2q³)")
    print("=" * 72)
    poly_factor = q**2 - 2*q - 1                          # may be negative at q_0
    Form_A_over_me = abs(poly_factor) * (q + 1) / (2 * q**3)
    print(f"  Form A/m_e at q_0 = {mp.nstr(Form_A_over_me, 15)}")
    print(f"  Target Q_β/m_e   = {mp.nstr(target, 15)}")
    # mpf, not float: this is computed from Form_A_over_me and target, both mpf.
    # The float() cast that stood here put a float64 straight into the witness
    # (raw-float64 baseline). Display still goes through mp.nstr.
    miss_pct = (Form_A_over_me - target) / target * 100
    print(f"  Miss = {mp.nstr(miss_pct, 6)}% (Form A leading)")
    print()
    print(f"  Polynomial factor: (q² - 2q - 1)")
    print(f"  Roots: q = 1 ± √2 ≈ 2.4142, -0.4142")

    # Concrete non-cyclotomic check: compute the roots and verify
    # neither sits on the unit circle (root-of-unity necessary condition
    # is |z| = 1; both roots have |1+√2| ≈ 2.414 and |1-√2| ≈ 0.414).
    # Keep the roots as mpf. `_is_root_of_unity` takes a Python complex, so the
    # float() cast is confined to that call -- it is a decision at tol=1e-9,
    # where float64 is ample. What must NOT be float is the value that reaches
    # the witness: abs(root_*) below was a float64 in the raw-float64 baseline.
    sqrt2 = mp.sqrt(2)
    root_plus = 1 + sqrt2
    root_minus = 1 - sqrt2
    root_plus_is_rou = _is_root_of_unity(complex(float(root_plus), 0))
    root_minus_is_rou = _is_root_of_unity(complex(float(root_minus), 0))
    factor_is_cyclotomic = root_plus_is_rou and root_minus_is_rou

    print(f"  |1+√2| = {mp.nstr(abs(root_plus), 8)}, |1−√2| = {mp.nstr(abs(root_minus), 8)}")
    print(f"  Either on unit circle? +√2: {abs(root_plus) == 1}, −√2: {abs(root_minus) == 1}")
    print(f"  Root-of-unity check: +√2 → {root_plus_is_rou}, −√2 → {root_minus_is_rou}")
    print(f"  → polynomial factor is cyclotomic? {factor_is_cyclotomic}")
    print(f"  This 'silver-ratio' factor lives OUTSIDE the cyclotomic")
    print(f"  q-integer algebra in which FSC and G operate.")
    print()

    # Why this matters
    print("=" * 72)
    print("STRUCTURAL CONSEQUENCE")
    print("=" * 72)
    print()
    print("FSC and G have clean closed forms because:")
    print("  - α_EM source: torus knot Hecke characters → cyclotomic")
    print("    (q-integers [k]_q are products of cyclotomic polynomials)")
    print("  - G source: q-Yang-Mills variational integral → q-rational")
    print("    with poles only at 0 and 1 (Planck-unit normalisation")
    print("    further reduces to G_Planck = 1)")
    print()
    print("Q_β has NO clean closed form because:")
    print("  - Form A factor (q² - 2q - 1) has irrational roots (1 ± √2)")
    print("  - This factor comes from the single-wrap Markov-trace")
    print("    constraint at H_3 (the categorical mass identity at one")
    print("    crossing-pair); the discriminant doesn't reduce to roots")
    print("    of unity.")
    print()
    print("  - Therefore: no expansion of Q_β in q-integer products /")
    print("    cyclotomic factors converges to Form A. The precision")
    print("    ladder ∏(1 + c_k·b^k·ℏ_q^(2k)) IS the natural framework.")
    print("  - The c_4..c_7 'closed forms' (c_3·b⁴, -(b²+1/2), etc.)")
    print("    are pattern-matches in a non-cyclotomic algebra; no")
    print("    'FSC-like derivation' shortcut is available.")
    print()
    print("This is a NEGATIVE result, but a STRUCTURAL one — it explains")
    print("WHY the c_k derivation is hard, not just THAT it is hard.")

    # Witness data
    w.add_data("q_0", mp.nstr(q, 30))
    w.add_data("Q_beta_over_m_e", mp.nstr(target, 30))
    w.add_data("Form_A_over_m_e", mp.nstr(Form_A_over_me, 30))
    w.add_data("Form_A_miss_pct", mp.nstr(miss_pct, 30))
    w.add_data("polynomial_factor", "q^2 - 2q - 1")
    w.add_data("polynomial_roots", "1 ± √2 (silver ratio)")
    w.add_data("root_plus_abs", mp.nstr(abs(root_plus), 30))
    w.add_data("root_minus_abs", mp.nstr(abs(root_minus), 30))
    w.add_data("are_roots_of_unity", factor_is_cyclotomic)
    w.add_data("conclusion", (
        "Q_β admits NO clean cyclotomic / q-integer closed form. "
        "Its categorical source produces an irrational discriminant "
        "(q = 1 ± √2), distinct from FSC's cyclotomic torus knots "
        "and G's q-rational pole structure. The c_k precision-ladder "
        "IS the natural framework; no FSC-style derivation shortcut "
        "is available."
    ))
    # Concrete (non-tautological) assertion: factor is NOT cyclotomic.
    # `computed=0` records "is-cyclotomic-flag" which must be 0;
    # `expected=0` is the claim being verified. A future regression
    # (e.g., a programming error that returned True from `_is_root_of_unity`)
    # would flip computed to 1 and fail the assertion.
    w.add_assertion(
        "polynomial_factor_not_cyclotomic",
        computed=1 if factor_is_cyclotomic else 0,
        expected=0,
        tolerance=0,
        source=(
            "Roots of q²-2q-1 are 1±√2 with |1+√2|≈2.41 and |1-√2|≈0.41 — "
            "neither on the unit circle, so neither is a root of unity"
        ),
    )
    w.save()


if __name__ == "__main__":
    main()
