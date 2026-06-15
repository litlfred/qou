"""DERIVED generalizations of PR #1125 / #1153 binomial pattern + sinh partner.

Combines:
  - PR #1125 / #1165: P_m = cosh((2m+1)η)/(2 cosh η) (bar-symmetric)
  - PR #1153: Q_m = sinh((2m+1)η)/(2 cosh η) (bar-anti-symmetric)

Per /coordinate comment on PR #1153, this PR derives FOUR new identities
from the cosh/sinh definitions and verifies them symbolically:

  (I1) Q_m/P_m = tanh((2m+1)η)            [trivial from defs]
  (I2) P_m² - Q_m² = 1/[2]_q²            [Pythagorean: cosh² - sinh² = 1]
  (I3) P_m + Q_m = q^{2m+1}/[2]_q        [from cosh + sinh = e^x]
  (I4) P_m - Q_m = q^{-(2m+1)}/[2]_q     [from cosh - sinh = e^{-x}]

(I2) is a STRUCTURAL GENERALIZATION: at substrate η_0, every torus knot
T(2, 2m) satisfies a Pythagorean-like identity relating bar-symmetric
and bar-anti-symmetric mass components.

Each identity is verified for m = 0..6 via sympy symbolic simplify.

## Borromean special case (off the torus-link ladder)

The Borromean rings 𝓑₃ have closed form (PR #1081):
  tr_M(β_Bor) = (4 + h² − 3h⁴ − h⁶) / (h² + 4)

This is purely EVEN in h (bar-symmetric). The bar-anti-symmetric companion
Q_Borromean would be the odd-h part divided by [2]_q. Since the closed
form has no odd-h terms, **Q_Borromean = 0**.

This is consistent with: the baryon's mass is dominantly STRONG-force,
not EM. The Q-channel (EM partner) of the Borromean is structurally zero.

## Status

GENUINE DERIVATIONS, not empirical fits. Each identity follows from
standard hyperbolic-function identities applied to the sibling
definitions. Verified symbolically.
"""
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import subprocess
from pathlib import Path

import sympy as sp


def main():
    print("=" * 80)
    print("Pythagorean + companion identities for P_m, Q_m (T(2, 2m) torus family)")
    print("=" * 80)
    print()
    print("Definitions (from PR #1125 / #1165 / #1153):")
    print("  P_m(η) = cosh((2m+1)η) / (2 cosh η)   [bar-symmetric]")
    print("  Q_m(η) = sinh((2m+1)η) / (2 cosh η)   [bar-anti-symmetric]")
    print()

    η = sp.Symbol('η', real=True)
    m = sp.Symbol('m', integer=True, nonnegative=True)
    q = sp.exp(η)  # so q = e^η, h = q - q^{-1} = 2 sinh η, [2]_q = 2 cosh η

    print("Verifying identities symbolically for m = 0..6:")
    print()

    results = []
    for m_val in range(7):
        P_m = sp.cosh((2 * m_val + 1) * η) / (2 * sp.cosh(η))
        Q_m = sp.sinh((2 * m_val + 1) * η) / (2 * sp.cosh(η))

        # (I1) Q_m / P_m = tanh((2m+1)η)
        I1_lhs = sp.trigsimp(Q_m / P_m)
        I1_rhs = sp.tanh((2 * m_val + 1) * η)
        I1_diff = sp.trigsimp(I1_lhs - I1_rhs)
        I1_ok = I1_diff == 0

        # (I2) P_m² - Q_m² = 1 / [2]_q²
        bracket_2_q_sq = (2 * sp.cosh(η)) ** 2
        I2_lhs = sp.trigsimp(P_m ** 2 - Q_m ** 2)
        I2_rhs = 1 / bracket_2_q_sq
        I2_diff = sp.trigsimp(I2_lhs - I2_rhs)
        I2_ok = I2_diff == 0

        # (I3) P_m + Q_m = q^{2m+1} / [2]_q
        # Use exp form for clean comparison
        q_pos = sp.exp((2 * m_val + 1) * η)
        bracket_2_q = 2 * sp.cosh(η)
        I3_lhs = sp.expand_trig(P_m + Q_m)  # expand cosh/sinh in exp form
        I3_rhs = sp.expand_trig(q_pos / bracket_2_q)
        I3_diff = sp.simplify(I3_lhs - I3_rhs)
        I3_ok = I3_diff == 0

        # (I4) P_m - Q_m = q^{-(2m+1)} / [2]_q
        q_neg = sp.exp(-(2 * m_val + 1) * η)
        I4_lhs = sp.expand_trig(P_m - Q_m)
        I4_rhs = sp.expand_trig(q_neg / bracket_2_q)
        I4_diff = sp.simplify(I4_lhs - I4_rhs)
        I4_ok = I4_diff == 0

        print(f"m = {m_val}:")
        print(f"  (I1) Q/P = tanh:          {'✓' if I1_ok else '✗'}")
        print(f"  (I2) P²-Q² = 1/[2]_q²:    {'✓' if I2_ok else '✗'}")
        print(f"  (I3) P+Q = q^{2*m_val+1}/[2]_q:    {'✓' if I3_ok else '✗'}")
        print(f"  (I4) P-Q = q^-{2*m_val+1}/[2]_q:   {'✓' if I4_ok else '✗'}")

        results.append({
            "m": m_val,
            "I1_Q_over_P_eq_tanh": I1_ok,
            "I2_pythagorean": I2_ok,
            "I3_sum_eq_q_pos": I3_ok,
            "I4_diff_eq_q_neg": I4_ok,
        })

    all_ok = all(r["I1_Q_over_P_eq_tanh"] and r["I2_pythagorean"] and r["I3_sum_eq_q_pos"] and r["I4_diff_eq_q_neg"] for r in results)
    print()
    print("=" * 80)
    if all_ok:
        print("✓ ALL 4 IDENTITIES VERIFIED for m = 0..6")
        print("=" * 80)
        print()
        print("(I2) is the structural GENERALIZATION: at substrate η_0, every")
        print("torus knot T(2, 2m) satisfies a Pythagorean-like identity:")
        print("  P_m² - Q_m² = 1/[2]_q²  (independent of m!)")
        print()
        print("This is a CONSTRAINT on the bar-symmetric and bar-anti-symmetric")
        print("mass components: they're 'orthogonal' in the cosh²-sinh² sense.")
        print("Numerically at q_0:")
        from mpmath import mpf, mp
        from q_parameter import Q_50_DIGIT_STR  # noqa: E402
        mp.mp.dps = 30
        q_0 = mpf(Q_50_DIGIT_STR)  # canonical 50-digit substrate pin
        bracket_inv = 1 / (q_0 + 1 / q_0) ** 2
        print(f"  1/[2]_q² at q_0 = 1/(q_0 + q_0⁻¹)² = {float(bracket_inv):.10f}")
        print()
        # Per-particle: P_m² - Q_m² = 1/[2]_q² (CONSTANT! independent of m)
        print(f"For W (m=2), Z (m=3), H (m=4): P_m² - Q_m² = {float(bracket_inv):.10f} (same constant)")
        print()
        print("This is a NEW CATEGORICAL IDENTITY for the framework's torus-knot RT")
        print("chain: the EM-channel residual Q_m and the canonical mass P_m are")
        print("Pythagorean partners across the entire T(2, 2m) family.")
    else:
        print("✗ MISMATCH found")
        print("=" * 80)

    # Borromean special case
    print()
    print("=" * 80)
    print("Borromean (NOT torus): Q_Borromean = ?")
    print("=" * 80)
    h_sym = sp.Symbol('h')
    tr_M_borromean = (4 + h_sym ** 2 - 3 * h_sym ** 4 - h_sym ** 6) / (h_sym ** 2 + 4)
    # Bar-anti-symmetric: odd-h part
    expanded = sp.series(tr_M_borromean, h_sym, 0, 10).removeO()
    print(f"tr_M(β_Bor) series in h: {sp.expand(expanded)}")
    # Check if any odd-h terms
    odd_part = sum(
        sp.Rational(1, 1) * sp.Poly(expanded, h_sym).coeff_monomial(h_sym ** k) * h_sym ** k
        for k in range(1, 10, 2)
    )
    print(f"Odd-h part: {odd_part}")
    if odd_part == 0:
        print()
        print("✓ Borromean Markov trace has ZERO odd-h coefficients → Q_Borromean = 0")
        print()
        print("Structural prediction: the baryon (Borromean) has NO bar-anti-symmetric")
        print("(EM-channel) component in its mass formula. Consistent with the baryon")
        print("being dominantly STRONG-force.")
        print()
        print("Note: this assumes the same bar-symmetric/anti-symmetric decomposition")
        print("applies to non-torus knots; rigorously this requires generalizing")
        print("the cosh/sinh framework beyond the (2m+1)η argument.")
    else:
        print(f"\n✗ Borromean has non-zero odd-h part: {odd_part}")

    # Witness
    witness = {
        "compute": "pm_qm_pythagorean_identity",
        "description": (
            "DERIVED generalizations of PR #1125 binomial pattern + PR #1153 "
            "sinh partner. Verifies 4 identities symbolically for m = 0..6:\n"
            "  (I1) Q_m/P_m = tanh((2m+1)η)\n"
            "  (I2) P_m² - Q_m² = 1/[2]_q²  ← Pythagorean GENERALIZATION\n"
            "  (I3) P_m + Q_m = q^{2m+1}/[2]_q\n"
            "  (I4) P_m - Q_m = q^{-(2m+1)}/[2]_q\n"
            "Plus Borromean special case: Q = 0 (zero EM channel)."
        ),
        "results": results,
        "all_identities_verified": all_ok,
        "key_finding": (
            "Pythagorean identity (I2) is m-INDEPENDENT: P_m² - Q_m² = 1/[2]_q² "
            "for ALL m. This constrains the EM-channel residual Q_m and the "
            "bar-symmetric mass P_m to lie on a 'hyperbolic circle' "
            "(cosh²-sinh² = 1, normalized by 1/(2 cosh η)²)."
        ),
        "borromean_special_case": {
            "Q_Borromean": 0,
            "interpretation": (
                "Borromean Markov trace is purely even in h; no odd-h terms; "
                "so bar-anti-symmetric companion vanishes. Structural "
                "prediction: baryon has no EM-channel mass contribution "
                "(consistent with baryon mass being dominantly strong-force)."
            ),
        },
        "status": "exploratory",
        "tags": [
            "derived-generalization",
            "pythagorean-identity",
            "p_m-q_m",
            "borromean-no-Q",
            "cosh-sinh-identity",
        ],
        "scriptCommitSha": (
            subprocess.check_output(["git", "rev-parse", "HEAD"])
            .decode().strip()
        ),
    }
    out_path = Path(__file__).parent / "pm-qm-pythagorean-identity.witness.json"
    out_path.write_text(json.dumps(witness, indent=2, sort_keys=True) + "\n")
    print(f"\nWitness: {out_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
