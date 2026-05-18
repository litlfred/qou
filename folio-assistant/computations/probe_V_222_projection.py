"""V_(2,2,2) Wedderburn-block projection probe — refutes PR #664 c_3 claim.

PR #664's `prop:hopf-jones-c3-categorical` claims:
  "V_(2,2,2) is the Hopf-mediated channel of V_(2,1)⊗V_(2,1) in H_6
   that produces the order-h^6 contribution F_3 = -2·b³·ℏ_q^6."

This probe DIRECTLY tests that claim by computing the per-Wedderburn-block
contribution to tr_M(σ_1² in H_6):

  contrib_λ := y_λ(q) · χ^λ(σ_1²)

for each partition λ ⊢ 6, then asking: does the V_(2,2,2) contribution
equal the framework's F_3 = -2·b³·ℏ_q^6 value?

## Method

(a) Load cached y_λ(q_0) for n=6 from
    `y-lambda-jones-markov-witness.json` (11 partitions; Wenzl values).
(b) Compute χ^λ(σ_1²) symbolically via Hoefsmit seminormal, evaluate
    at q_0 to 50 dps.
(c) Per-block contribution = y_λ · χ^λ at q_0.
(d) Compare V_(2,2,2) contribution to framework F_3 ansatz value at q_0:
    -2 · b³(q_0) · ℏ_q(q_0)^6.

## Result (substantive new finding)

At q_0 ≈ 1.10998:

  V_(2,2,2) per-block contribution :  +0.003788
  Framework F_3 = -2·b³·ℏ_q^6      :  -1.3 × 10^{-6}

  RATIO  : ~3000×
  SIGN   : OPPOSITE (V_(2,2,2) positive, F_3 negative)

**V_(2,2,2) is NOT the channel producing F_3.** PR #664's central claim
is empirically refuted by direct per-block computation.

## Where could F_3 ≈ -1.3×10⁻⁶ come from?

Looking at the per-block decomposition at q_0:

  λ                contribution
  (4, 2)          +0.395886    largest channel
  (5, 1)          +0.338426
  (3, 2, 1)       +0.119654
  (4, 1, 1)       +0.107809
  (3, 3)          +0.075115
  (6,)            +0.072922
  (2, 2, 2)       +0.003788    ← claimed PR #664 channel
  (2, 2, 1, 1)    -0.002930
  (3, 1, 1, 1)    -0.006715
  (2, 1^4)        +0.000442
  (1^6)           -0.000010

The TOTAL is tr_M(σ_1²) = 1.10439, matching the closed form
1 + (q-1)·q^{-1/2} at q_0. None of the per-block contributions is at
the 10⁻⁶ scale matching the framework F_3 ansatz value.

**Conclusion:** F_3 = -2·b³·ℏ_q^6 (PR #657 Track-C / PR #664 ansatz)
does not arise from any single Wedderburn block of σ_1² in H_6 at the
level of per-block contributions to tr_M. The framework's
"V_(2,2,2) → Hopf channel → -2·b³·ℏ_q^6" derivation chain does not
go through at the per-block level.

This is a third critical-review finding (after the dual-tr_M
discrepancy and the F_n bare-Markov mismatch) showing PR #664's
F_3 derivation is structurally incomplete.

Output: V-222-projection-probe.witness.json
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


from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

from hoefsmit_symbolic import chi_lambda_symbolic, Q  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    print("=" * 90)
    print("  V_(2,2,2) projection probe — per-block contribution to tr_M(σ_1² in H_6)")
    print("=" * 90)
    print()

    # ─── Load cached y_λ(q_0) for n=6 ───
    witness = json.loads(
        (HERE / "y-lambda-jones-markov-witness.json").read_text()
    )
    n6 = {tuple(w['partition']): mp.mpf(str(w['y_lambda'])) for w in witness['tables_by_n']['6']['weights']}

    # ─── Compute per-block contribution at q_0 ───
    q_val = sp.Float(Q_50_DIGIT_STR, 50)
    q0_mp = mp.mpf(Q_50_DIGIT_STR)
    sigma1sq = [(0, "sigma"), (0, "sigma")]

    rows = []
    total = mp.mpf(0)
    print("  Per-block contribution y_λ · χ^λ(σ_1²) at q_0:")
    print(f"  {'λ':>20} {'y_λ':>16} {'χ^λ':>14} {'contribution':>16}")
    for shape, y in sorted(n6.items()):
        chi_sym = chi_lambda_symbolic(shape, sigma1sq)
        chi_num = mp.mpf(str(sp.N(chi_sym.subs(Q, q_val), 50)))
        contrib = y * chi_num
        total += contrib
        marker = "  <-- V_(2,2,2)" if shape == (2, 2, 2) else ""
        print(f"  {str(shape):>20} {float(y):>+16.10f} {float(chi_num):>+14.6f} {float(contrib):>+16.6f}{marker}")
        rows.append({
            "partition": list(shape),
            "y_lambda_at_q0": float(y),
            "chi_lambda_at_q0": float(chi_num),  # noqa: I8 — display / raw-dict emit
            "per_block_contribution_at_q0": float(contrib),
        })

    print()
    print(f"  Total tr_M(σ_1² in H_6) = {mp.nstr(total, 18)}")
    closed_form = 1 + (q0_mp - 1) / mp.sqrt(q0_mp)
    print(f"  Closed form 1 + (q-1)/√q = {mp.nstr(closed_form, 18)}")
    print(f"  |diff| = {mp.nstr(abs(total - closed_form), 4)}")
    print()

    # ─── Compute framework F_3 ansatz value at q_0 ───
    # F_3 = -2 · b³ · ℏ_q^6, where b² = (q^4+q^2+1)/(q^2+1)^2
    b_sq_at_q0 = (q0_mp ** 4 + q0_mp ** 2 + 1) / (q0_mp ** 2 + 1) ** 2
    b_at_q0 = mp.sqrt(b_sq_at_q0)
    b_cubed_at_q0 = b_at_q0 ** 3
    hbar_at_q0 = (q0_mp - 1) / q0_mp
    F_3_value_at_q0 = -2 * b_cubed_at_q0 * hbar_at_q0 ** 6

    print("  Framework F_3 ansatz at q_0:")
    print(f"    b²(q_0)        = {mp.nstr(b_sq_at_q0, 12)}")
    print(f"    b(q_0)         = {mp.nstr(b_at_q0, 12)}")
    print(f"    b³(q_0)        = {mp.nstr(b_cubed_at_q0, 12)}")
    print(f"    ℏ_q(q_0)       = {mp.nstr(hbar_at_q0, 12)}")
    print(f"    ℏ_q^6(q_0)     = {mp.nstr(hbar_at_q0**6, 12)}")
    print(f"    F_3 = -2·b³·ℏ_q^6 = {mp.nstr(F_3_value_at_q0, 12)}")
    print()

    # ─── The decisive comparison ───
    v222_contrib = next(r['per_block_contribution_at_q0'] for r in rows if tuple(r['partition']) == (2, 2, 2))
    ratio = abs(v222_contrib / float(F_3_value_at_q0)) if F_3_value_at_q0 != 0 else float('inf')
    same_sign = (v222_contrib > 0) == (float(F_3_value_at_q0) > 0)

    print("  ── DECISIVE COMPARISON ──")
    print(f"    V_(2,2,2) per-block contribution : {v222_contrib:+.6e}")
    print(f"    Framework F_3 = -2·b³·ℏ_q^6      : {float(F_3_value_at_q0):+.6e}")
    print(f"    Ratio (magnitudes)               : {ratio:.2e}×")
    print(f"    Same sign?                       : {same_sign}")
    print()
    if not same_sign:
        print("    !! OPPOSITE SIGN — V_(2,2,2) cannot produce F_3.")
    if ratio > 100 or ratio < 0.01:
        print(f"    !! MAGNITUDE MISMATCH ({ratio:.0e}×) — V_(2,2,2) ≠ F_3 channel.")
    print()
    print("  Verdict: PR #664's claim 'V_(2,2,2) → F_3 = -2·b³·ℏ_q^6' is")
    print("  empirically refuted by direct per-block computation. The")
    print("  V_(2,2,2) channel contributes +3.8e-3 at q_0; the framework")
    print("  F_3 ansatz value at q_0 is -1.3e-6 — opposite sign, off by")
    print("  ~3000×. The 'Hopf-mediated V_(2,2,2)' channel chain does")
    print("  not go through at the per-block level.")
    print()

    builder = (
        WitnessBuilder("V-222-projection-probe", engine="python")
        .set_description(
            "Per-Wedderburn-block contribution probe for V_(2,2,2) inside "
            "tr_M(σ_1² in H_6). REFUTES PR #664's claim that V_(2,2,2) is "
            "the channel producing the framework F_3 = -2·b³·ℏ_q^6: the "
            "V_(2,2,2) per-block contribution at q_0 is +3.8e-3, while the "
            "framework F_3 ansatz value at q_0 is -1.3e-6 — opposite sign, "
            "off by ~3000×. None of the 11 per-block contributions match "
            "the F_3 ansatz at q_0."
        )
        .set_audit_only(
            "docs/audits/2026-05-17-F-n-derivation-analysis.md"
        )
        .add_parameter("q_0", Q_50_DIGIT_STR)
        .add_data("per_block_contributions", rows)
        .add_data("total_trM_sigma1_sq", float(total))
        .add_data("closed_form_1_plus_q_minus_1_over_sqrt_q", float(closed_form))
        .add_data("V_222_contribution_at_q0", v222_contrib)
        .add_data("framework_F_3_value_at_q0", float(F_3_value_at_q0))
        .add_data("ratio_magnitude_V222_over_F3", ratio)
        .add_data("same_sign", same_sign)
        .add_assertion(
            name="V_222_contribution_and_F_3_have_opposite_sign",
            computed=not same_sign,
            expected=True,
            unit="boolean",
            source=(
                "V_(2,2,2) contribution to tr_M(σ_1²) at q_0 is positive "
                "(+3.8e-3); framework F_3 = -2·b³·ℏ_q^6 ansatz at q_0 is "
                "negative (-1.3e-6). Opposite signs."
            ),
        )
        .add_assertion(
            name="V_222_contribution_magnitude_mismatches_F_3",
            computed=bool(ratio > 100 or ratio < 0.01),
            expected=True,
            unit="boolean",
            source=(
                "Magnitude ratio |V_(2,2,2)| / |F_3| ≈ 3000× at q_0. "
                "V_(2,2,2) channel does NOT produce the F_3 value."
            ),
        )
        .add_caveat(
            "This probe refutes the SPECIFIC PR #664 / PR #657 Track-C claim "
            "that V_(2,2,2) inside H_6 is the channel producing the "
            "F_3 = -2·b³·ℏ_q^6 factor. The framework's c_3 = -2 (symbol "
            "coefficient in F_3) value may still be empirically extractable "
            "from PR #655's residual fit, but it does NOT arise from the "
            "V_(2,2,2) Wedderburn projection chain as claimed."
        )
    )
    out = builder.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
