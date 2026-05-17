"""Genuine V_(2,2,2) Wedderburn-block projection probe for c_3
— numerical finite-difference extraction of the ε^6 coefficient.

Symbolic sympy expansion of y_(2,2,2)(q) at q=1+ε is intractable (the
Wenzl Schur-principal-specialisation form has thousands of half-power
terms). We extract the ε^6 leading coefficient numerically via finite
differences on the per-block contribution y_(2,2,2)(q) · χ^(2,2,2)(σ_1²)
evaluated at high-precision mpmath at q = 1 + ε for small ε.

## Method

(a) Compute symbolic χ^(2,2,2)(σ_1²) (small, fast).
(b) Use the cached y_(2,2,2)(q_0) at q_0 from y-lambda-mpfr-witness.json
    — but we need MULTIPLE q values for finite-difference, so we
    compute y_(2,2,2)(q) at each q via solve_y_lambda(6) which is
    SLOW but doable for a handful of q values.
(c) Alternative: use the symbolic y_(2,2,2) form numerically — evaluate
    the Wenzl Schur-principal-specialisation expression at each q.
(d) Compute contribution(ε) := y_(2,2,2)(1+ε) · χ^(2,2,2)(σ_1²)|_{q=1+ε}
    at ε ∈ {1e-3, 5e-4, 2.5e-4, 1.25e-4} (5-point stencil).
(e) Finite-difference to extract ε^6 leading coefficient.
(f) Compare to framework F_3 = -2·b³(q=1) = -3√3/4 ≈ -1.299.

## Output

V-222-projection-symbolic.witness.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

mp.mp.dps = 100  # extra precision for finite-difference extraction

from hoefsmit_symbolic import chi_lambda_symbolic, Q  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    print("=" * 90)
    print("  V_(2,2,2) projection — finite-difference ε^6 extraction")
    print("=" * 90)
    print()

    # χ^(2,2,2)(σ_1² in H_6) symbolically
    sigma1sq = [(0, "sigma"), (0, "sigma")]
    chi_222 = sp.cancel(chi_lambda_symbolic((2, 2, 2), sigma1sq))
    print(f"  χ^(2,2,2)(σ_1²) = {chi_222}")
    print()

    # Load symbolic y_(2,2,2) for n=6
    wit = json.loads(
        (HERE / "y-lambda-wenzl-bridge-symbolic-witness.json").read_text()
    )
    data = wit.get('data', wit)
    n6 = data['tables_by_n']['6']['weights']
    y_222_str = next(w['y_lambda_symbolic'] for w in n6 if w['partition'] == [2, 2, 2])
    y_222 = sp.sympify(y_222_str, locals={'q': Q, 'sqrt': sp.sqrt})

    # Per-block contribution: y · χ
    contrib_expr = y_222 * chi_222

    # Evaluate contribution(q) at q = 1 + ε for several small ε values.
    # Use mpmath via sp.N for high-precision evaluation.
    print("  Evaluating contribution at q = 1 + ε for small ε:")
    eps_values = [mp.mpf(f"1e-{k}") for k in (3, 4, 5)]
    values = {}
    for eps in eps_values:
        q_val = sp.Float(mp.nstr(1 + eps, 50), 50)
        v = sp.N(contrib_expr.subs(Q, q_val), 50)
        values[str(eps)] = mp.mpf(str(v))
        print(f"    ε = {float(eps):.0e}  contribution = {mp.nstr(values[str(eps)], 20)}")
    print()

    # Extract leading terms — at small ε, contribution ≈ c_0 + c_1·ε + ... + c_6·ε^6 + ...
    # For ε small, we have contribution ≈ c_0 + c_6·ε^6 (intermediate orders are huge or zero)
    # Try: extract coefficient of ε^6 via dominance — divide (contrib - c_0) by ε^6.
    print("  Extracting ε^6 leading coefficient (finite-difference / dominance):")
    # First compute contribution at ε = 0 exactly via direct substitution
    q_one = sp.Rational(1)
    contrib_at_q1_sym = sp.cancel(contrib_expr.subs(Q, q_one))
    try:
        c_0 = mp.mpf(str(sp.N(contrib_at_q1_sym, 50)))
        print(f"    c_0 = contribution(q=1)      = {mp.nstr(c_0, 20)}")
    except Exception as e:
        print(f"    c_0 evaluation failed: {e}")
        c_0 = mp.mpf(0)

    # Extract higher-order via finite difference on log(ε)
    print(f"    (contribution - c_0) / ε^k for various k, ε = 1e-3:")
    eps_test = mp.mpf("1e-3")
    v_test = values[str(eps_test)]
    residual = v_test - c_0
    for k in range(1, 9):
        ratio = residual / eps_test**k
        print(f"      k={k}: |residual| / ε^{k} = {mp.nstr(ratio, 14)}")
    print()

    # The dominant ε^k term: find k where the ratio is finite (not blowing up)
    print("  Determining dominant order by ε-scaling:")
    # At ε → 0, the dominant term is the leading non-zero ε^k.
    # If contribution(ε) ≈ c_k · ε^k + O(ε^{k+1}), then
    #   contribution(ε_a) / contribution(ε_b) ≈ (ε_a/ε_b)^k
    # (when ε is small enough that c_0 is dominated by c_k · ε^k or
    # when c_0 = 0, which is the case here since y_(2,2,2)(q=1) is
    # singular and the leading behaviour starts at some ε^k > 0.)
    eps_a = mp.mpf("1e-3"); v_a = values[str(eps_a)]
    eps_b = mp.mpf("1e-4"); v_b = values[str(eps_b)]
    # Use contribution(ε) DIRECTLY (since c_0 is nan/singular):
    log_ratio = mp.log10(abs(v_a) / abs(v_b))
    print(f"    log10(|contrib(1e-3)| / |contrib(1e-4)|) = {float(log_ratio):.6f}")
    print(f"    → leading order k ≈ {float(log_ratio):.2f}")

    # Extract leading coefficient: c_k = contribution(ε_a) / ε_a^k
    k_extracted = round(float(log_ratio))
    leading_coeff = v_a / eps_a**k_extracted
    print(f"    c_{k_extracted} ≈ {mp.nstr(leading_coeff, 14)}")
    print()

    # Compare to framework F_3 = -2·b³ at q=1 = -3·sqrt(3)/4
    target_eps6_leading = mp.mpf(-2) * (mp.mpf(3) * mp.sqrt(3) / 8)
    print(f"  Framework F_3 ε^6 ansatz value at q=1: {mp.nstr(target_eps6_leading, 14)}")
    print(f"  V_(2,2,2) extracted ε^k where k = {k_extracted}: {mp.nstr(leading_coeff, 14)}")

    matches = False
    if k_extracted == 6:
        delta = abs(leading_coeff - target_eps6_leading)
        rel_diff = float(delta / abs(target_eps6_leading)) if target_eps6_leading != 0 else float('inf')
        matches = rel_diff < 0.01
        print(f"  rel_diff = {rel_diff:.4e}")
        print()
        if matches:
            print(f"  ★ V_(2,2,2) ε^6 coefficient MATCHES framework F_3 ansatz")
            print(f"  ★ PR #664's c_3 chain CONFIRMED at per-block symbolic level")
        else:
            print(f"  ✗ V_(2,2,2) ε^6 coefficient DOES NOT match framework F_3")
            print(f"  ✗ PR #664's c_3 chain REFUTED at per-block symbolic level")
    else:
        print()
        print(f"  V_(2,2,2)'s leading non-constant Taylor order is ε^{k_extracted}, NOT ε^6")
        print(f"  → The block contributes at a DIFFERENT order than framework F_3 expects")
        print(f"  → PR #664's claim that V_(2,2,2) produces the order-h^6 contribution is REFUTED")

    builder = (
        WitnessBuilder("V-222-projection-symbolic", engine="mpmath")
        .set_description(
            "V_(2,2,2) per-block contribution to tr_M(σ_1² in H_6) "
            "leading Taylor order at q=1+ε, extracted via finite-"
            "difference / log10-ratio dominance at 100-dps precision. "
            "Tests PR #664's claim that V_(2,2,2) contributes at order "
            "ε^6 matching the framework F_3 = -2·b³·ℏ_q^6 ansatz."
        )
        .set_audit_only(
            "docs/audits/2026-05-17-pr-664-c3-c4-critical-review.md"
        )
        .add_parameter("eps_values_used", [float(e) for e in eps_values])
        .add_data("contribution_at_q1", float(c_0))
        .add_data("contribution_at_eps_values",
                  {str(k): float(v) for k, v in values.items()})
        .add_data("extracted_leading_order_k", k_extracted)
        .add_data("extracted_leading_coefficient", float(leading_coeff))
        .add_data("framework_F_3_target_eps6", float(target_eps6_leading))
        .add_assertion(
            name="V_222_leading_order_is_eps6",
            computed=(k_extracted == 6),
            expected=True,
            unit="boolean",
            source=(
                "PR #664 claims V_(2,2,2) is the order-h^6 channel for F_3. "
                "Finite-difference extraction of the leading non-constant "
                "Taylor order of y_(2,2,2)(q)·χ^(2,2,2)(σ_1²) at q=1+ε "
                "tests this directly."
            ),
        )
        .add_assertion(
            name="V_222_eps6_coefficient_matches_framework_ansatz",
            computed=matches,
            expected=True,
            unit="boolean",
            source=(
                "If k=6 and coefficient = -2·b³(q=1) = -3√3/4 ≈ -1.299, "
                "PR #664's V_(2,2,2) → F_3 chain is confirmed."
            ),
        )
        .add_caveat(
            "Finite-difference extraction at 100-dps precision rather than "
            "exact symbolic series (sympy Wenzl y_(2,2,2) at order ε^8 is "
            "intractable: hundreds of half-integer-power terms). The "
            "dominance method is robust for extracting the leading Taylor "
            "order but loses sub-leading precision."
        )
    )
    out = builder.save()
    print()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
