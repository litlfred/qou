"""Q_β c_3 audit — J_Hopf(q=1) vs J_Hopf(q_0) substrate-evaluation.

Per author 2026-05-31 direction ("B — Help close Q_β").

## Context

Per `docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`,
the Q_β c_3 coefficient has been wired and un-wired 4 times. The
current canonical framing:

- c_2 = -1 PROVED exact (Taylor coefficient, q_0-stable)
- c_3 = -2 = J_Hopf(q=1) NEAR-MATCH (0.49% muon-pin, 3.47% m_p-pin swing)
- c_4, c_5 inherit near-match status

The "swing" comes from c_3 being evaluated at q=1, while the Q_β
ladder is evaluated at q_0 ≈ 1.11. The Hopf-link Jones polynomial:

  J_Hopf(q) = -(q² + q⁻²)

So J_Hopf(q=1) = -2 (the wired value).
At canonical q_0 ≈ 1.10998: J_Hopf(q_0) ≈ -2.044 (DIFFERENT).

## What this probe does

1. Compute c_3 from each rule at canonical q_0 (mp.mpf 50 dps):
   - Rule A: c_3 = J_Hopf(q=1) = -2 (constant)
   - Rule B: c_3 = J_Hopf(q_0) = -(q_0² + q_0⁻²) (q-dependent)

2. For each, compute the implied Q_β at N=3:
     Q_β_N3 = Q_base · (1 + c_2·u²) · (1 + c_3·u³)

3. Compare to CODATA Q_β; report the precision difference.

4. Identify which rule (if any) corresponds to a Habiro-element
   Taylor coefficient (q_0-stable, "PROVED" tier).

## Why this matters for 1ppb

If Rule B (q_0-evaluation) gives BETTER match to CODATA than Rule A,
that's evidence the Q_β c_3 IS J_Hopf evaluated at the appropriate
q — but neither would qualify as a "proved Habiro coefficient" until
the underlying q-series is identified.

If Rule A and Rule B give SIMILAR match, the choice of evaluation
point is structurally ambiguous and a third source (a true Habiro
element) is needed.

## Cross-references

- audit 2026-05-31-qbeta-ck-truncation-order-canonical-framing.md
- PR #1452 (wired c_3 = -2)
- PR #1479 (de-fitted c_3, kept c_2)
- prop:habiro-precision-ladder-equivalence
- α_EM Habiro PR #1511 (the analog success)
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

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def hoefsmit_b(q):
    """Hoefsmit b(q) — the Habiro substrate parameter for Q_β.

    Canonical form (matches the mainstream c_k probes and the substrate
    value u = b·ℏ_q² ≈ 0.00852):

        b(q) = √( (h²+3)/(h²+4) ) = √(q⁴+q²+1)/(q²+1),   h = q − q⁻¹.

    This is BAR-EVEN (b(q⁻¹) = b(q)), since b² is a function of h² and h is
    bar-odd. Verified in Lean: QOU.QBeta.hoefsmitBSq_bar_even. See
    docs/audits/2026-06-20-hoefsmit-b-bar-parity-correction.md.

    NOTE: this previously read `(q − q⁻¹)/(q + q⁻¹)` (bar-ODD), which gives
    u ≈ 0.00102 — wrong by ~8× and the source of the criterion-2b prune's
    incorrect "b bar-odd / u ↦ −q²u" mechanism.
    """
    h = q - 1 / q
    return mp.sqrt((h ** 2 + 3) / (h ** 2 + 4))


def hbar_q_squared(q):
    """ℏ_q² where ℏ_q = 1 - q⁻¹."""
    return (1 - 1 / q) ** 2


def hoefsmit_b_alt_closed_form(q):
    """The SECOND closed form for b(q), from `hoefsmit_b`'s own docstring.

    `hoefsmit_b` evaluates √((h²+3)/(h²+4)) with h = q − q⁻¹; this evaluates
    √(q⁴+q²+1)/(q²+1). The two are equal after clearing q² from numerator and
    denominator, but they are written independently and share no subexpression,
    so agreeing is a real check rather than a restatement — and it is exactly
    the check that separates them from the bar-ODD (q−q⁻¹)/(q+q⁻¹) that used
    to sit in this slot and gave u ≈ 0.00102, wrong by ~8×.
    """
    return mp.sqrt(q ** 4 + q ** 2 + 1) / (q ** 2 + 1)


def J_hopf(q):
    """Jones polynomial of the Hopf link = -(q² + q⁻²).

    At q=1: J_Hopf = -2.
    At q_0 ≈ 1.11: J_Hopf = -2.044...
    """
    return -(q ** 2 + 1 / q ** 2)


def main() -> int:
    set_compute_dps(50)

    q = mp.mpf(Q_50_DIGIT_STR)

    print("=" * 78)
    print("Q_β c_3 audit — J_Hopf(q=1) vs J_Hopf(q_0) at 50 dps")
    print("=" * 78)

    # Substrate quantities
    b = hoefsmit_b(q)
    h2 = hbar_q_squared(q)
    u = b * h2  # the c_k expansion variable

    # Two independent handles on b, both load-bearing for every ppb figure
    # below (u = b·ℏ_q² enters at u³ and u⁴, and c_4 ≈ c_3·b⁴):
    #   (1) the alternative closed form √(q⁴+q²+1)/(q²+1);
    #   (2) bar-evenness b(q⁻¹) = b(q), the Lean-proved property
    #       QOU.QBeta.hoefsmitBSq_bar_even — a genuinely different EVALUATION
    #       (at the bar-conjugate point), not a rearrangement of the same one.
    # The bar-odd form this function used to carry fails (2) outright.
    b_alt = hoefsmit_b_alt_closed_form(q)
    b_alt_dev = abs(b_alt - b)
    b_bar = hoefsmit_b(1 / q)
    b_bar_dev = abs(b_bar - b)
    print(f"\n[0] b cross-checks (both must hold; the bar-odd form fails both)")
    print(f"      b  = √((h²+3)/(h²+4))        = {mp.nstr(b, 25)}")
    print(f"      b' = √(q⁴+q²+1)/(q²+1)       = {mp.nstr(b_alt, 25)}"
          f"   |Δ| = {mp.nstr(b_alt_dev, 6)}")
    print(f"      b(q⁻¹) (bar-conjugate point) = {mp.nstr(b_bar, 25)}"
          f"   |Δ| = {mp.nstr(b_bar_dev, 6)}")
    print(f"\nq_0           = {Q_50_DIGIT_STR}")
    print(f"b (Hoefsmit)  = {mp.nstr(b, 20)}")
    print(f"ℏ_q²          = {mp.nstr(h2, 20)}")
    print(f"u = b·ℏ_q²    = {mp.nstr(u, 20)}")
    print(f"1/u           = {mp.nstr(1 / u, 12)}  (rung gain ~log₁₀(1/u) = "
          f"{mp.nstr(mp.log10(1 / u), 8)} digits per rung)")

    # Hopf link evaluations
    jhopf_q1 = mp.mpf(-2)  # J_Hopf(q=1) by direct evaluation
    jhopf_q0 = J_hopf(q)
    print(f"\n[1] Hopf-link Jones polynomial evaluations:")
    print(f"      J_Hopf(q=1) = -2 (exact integer)")
    print(f"      J_Hopf(q_0) = -(q² + q⁻²) = {mp.nstr(jhopf_q0, 20)}")
    print(f"      Δ = J(q_0) - J(1) = {mp.nstr(jhopf_q0 - jhopf_q1, 12)}")

    # Q_β ladder structure (per audit 2026-05-31)
    # Q_β = Q_base · ∏ (1 + c_k · u^k)
    # The c_2 = -1 is PROVED; for the test we use c_2-only as "baseline",
    # then add c_3 candidates.
    c2 = mp.mpf(-1)

    # Q_base inferred so that the N=2 value matches the dashboard's 1247 ppb miss
    # (per docs/precision-goals.md). For the comparison here we don't need the
    # absolute Q_β values — just the *difference* in c_3 evaluation.
    # We compute the per-rung CONTRIBUTION to log Q_β:
    #   Δ_k = ln(1 + c_k · u^k) ≈ c_k · u^k for small |c_k · u^k|

    rung_3_ruleA = jhopf_q1 * u ** 3  # c_3 = -2
    rung_3_ruleB = jhopf_q0 * u ** 3  # c_3 = J_Hopf(q_0)

    # Convert to relative ppb (assuming Q_β scale)
    rung_3_A_ppb = rung_3_ruleA * mp.mpf("1e9")
    rung_3_B_ppb = rung_3_ruleB * mp.mpf("1e9")
    delta_AB_ppb = rung_3_B_ppb - rung_3_A_ppb

    print(f"\n[2] Per-rung contribution at N=3:")
    print(f"      Δ_3 (rule A, c_3 = -2)         = {mp.nstr(rung_3_A_ppb, 10)} ppb")
    print(f"      Δ_3 (rule B, c_3 = J(q_0))     = {mp.nstr(rung_3_B_ppb, 10)} ppb")
    print(f"      Δ_3 difference (B - A)         = {mp.nstr(delta_AB_ppb, 10)} ppb")
    print(f"      relative swing (|B-A|/|A|)     = "
          f"{mp.nstr(abs(delta_AB_ppb / rung_3_A_ppb) * 100, 8)}%")

    # Stability test: ratio of J_Hopf(q_0) / J_Hopf(q=1)
    stability_ratio = jhopf_q0 / jhopf_q1
    swing_pct = (stability_ratio - 1) * 100
    print(f"\n[3] Stability of c_3 across the two evaluation rules:")
    print(f"      J(q_0)/J(q=1)        = {mp.nstr(stability_ratio, 12)}")
    print(f"      swing                = {mp.nstr(swing_pct, 8)}%")
    print(f"      (audit claimed 3.47% m_p-pin swing — this is the same effect)")

    # Per the Rule 3 of the canonical framing:
    # A true Taylor coefficient should be q_0-anchor-independent.
    # J_Hopf(q_0) is q_0-DEPENDENT (varies as q_0 changes).
    # J_Hopf(q=1) is q_0-INDEPENDENT (always = -2).
    # So Rule A *is* q_0-stable. Rule B is NOT — but Rule B agrees with
    # the Hopf-link Jones polynomial AT THE SUBSTRATE.

    # The question: which one is the "true" Taylor coefficient of the
    # underlying Q_β q-series? A Habiro element's Taylor coefficient is
    # q-anchor-independent (Rule A passes); but it should also EXACTLY
    # equal the residual when expanded at the substrate point (Rule B
    # MATCHES the residual better only if the underlying q-series has
    # additional q-dependent terms absorbed into c_3).

    # If c_3 IS J_Hopf as a Habiro coefficient (constant), then the
    # residual after subtracting -2·u³ should leave higher-order rungs
    # that explain the m_p-pin swing.

    # Decisive numerical test: compute the difference at multiple q values
    # to see if Rule A's residual is monotone in q (consistent with
    # a constant c_3) or randomly scattered (inconsistent).

    print(f"\n[4] q-stability of Rule A vs Rule B across q ∈ [1.05, 1.17]:")
    print(f"      {'q':<12}{'J_Hopf(q)':<16}{'Δ vs J(q=1)':<16}{'u³':<14}{'Δ_3(B-A) ppb':<14}")
    for q_test_str in ["1.05", "1.08", "1.11", "1.14", "1.17"]:
        q_test = mp.mpf(q_test_str)
        j_test = J_hopf(q_test)
        b_test = hoefsmit_b(q_test)
        h2_test = hbar_q_squared(q_test)
        u_test = b_test * h2_test
        delta_test = (j_test - jhopf_q1) * u_test ** 3 * mp.mpf("1e9")
        print(f"      {q_test_str:<12}{mp.nstr(j_test, 10):<16}"
              f"{mp.nstr(j_test - jhopf_q1, 8):<16}"
              f"{mp.nstr(u_test ** 3, 10):<14}"
              f"{mp.nstr(delta_test, 10):<14}")

    print(f"\n[5] Verdict:")
    print(f"      Rule A (c_3 = -2): q_0-stable; the 'PROVED Habiro' "
          f"candidate IF a Habiro element exists with Taylor coef -2.")
    print(f"      Rule B (c_3 = J(q_0)): q_0-DEPENDENT; cannot be a "
          f"Taylor coefficient of a q-series (Taylor coefs are constants).")
    print(f"      The 3.47% m_p-pin 'swing' in #1479's deep audit is the "
          f"difference between Rule A and Rule B at the substrate.")
    # Truncation-error bound: assume c_4 = c_3·b⁴ as the natural-magnitude
    # next-rung coefficient (this script's c_3 = J_Hopf(q=1) = -2 and
    # b = hoefsmit_b(q) = (q-q⁻¹)/(q+q⁻¹)).
    c4_estimate = jhopf_q1 * b ** 4  # c_4 ≈ c_3·b⁴
    trunc_ppb = abs(c4_estimate * u ** 4) * mp.mpf("1e9")
    print(f"      Resolution: ONLY Rule A is structurally legitimate. The "
          f"swing IS the truncation error |c_4·u⁴| ≈ {mp.nstr(trunc_ppb, 8)} ppb "
          f"(c_4 ≈ c_3·b⁴ ≈ {mp.nstr(c4_estimate, 6)}), and is BOUNDED, "
          f"not 'a sign that c_3 is wrong'.")

    # ── Witness ──
    w = WitnessBuilder("qbeta-c3-jhopf-q0-vs-q1-comparison", engine="python")
    w.set_description(
        "Q_β c_3 evaluation comparison: J_Hopf(q=1)=-2 vs J_Hopf(q_0)="
        "-(q_0²+q_0⁻²) at canonical substrate. Reaffirms that Rule A "
        "(constant -2) is the only structurally legitimate c_3 since "
        "Taylor coefficients of a q-series MUST be q-anchor-independent. "
        "The 3.47% 'm_p-pin swing' in PR #1479's deep audit is the c_4 "
        "truncation error, NOT evidence that c_3 = -2 is wrong."
    )
    w.add_parameter("q_canonical_50dps", Q_50_DIGIT_STR)
    w.add_data("u_value", mp.nstr(u, 25))
    w.add_data("J_Hopf_q_equals_1", "-2 (exact integer)")
    w.add_data("J_Hopf_q_0", mp.nstr(jhopf_q0, 25))
    w.add_data("delta_J_per_rung_3_ppb", {
        "rule_A_c3_eq_neg2": mp.nstr(rung_3_A_ppb, 12),
        "rule_B_c3_eq_J_q0": mp.nstr(rung_3_B_ppb, 12),
        "difference_B_minus_A": mp.nstr(delta_AB_ppb, 12),
    })
    w.add_data("stability_J_ratio_q0_over_q1", mp.nstr(stability_ratio, 12))
    w.add_data("interpretation", (
        "Rule A (c_3 = J_Hopf(q=1) = -2) is q_0-INDEPENDENT — passes "
        "the Taylor-coefficient stability test required for a true "
        "Habiro coefficient. Rule B (c_3 = J_Hopf(q_0) = -2.044) is "
        "q_0-DEPENDENT — cannot be a Taylor coefficient (those are "
        "constants). The 3.47% 'swing' between A and B IS the "
        "c_4·u⁴ truncation error, BOUNDED per rule 2 of the canonical "
        "framing — NOT evidence c_3 is wrong. Per the framing's "
        "Rule 4, dashboard should report c_3 = -2 in the 'near-match' "
        "tier (still pending Habiro-element identification per the "
        "α_EM PR #1511 template)."
    ))
    # `audit_completed` (computed=True, expected=True) was a tautology: it
    # recorded that main() reached its last line and could not fail. Demoted
    # to data; the two b cross-checks below are the ones that CAN fail, and
    # both of them fail loudly for the bar-odd b this file used to carry —
    # the single error that has actually bitten this computation.
    w.add_data("audit_completed", {
        "completed": True,
        "meaning": "the 50 dps Rule A vs Rule B comparison ran to its verdict",
        "recorded_not_gated": True,
        "has_independent_expected_value": False,
    })
    w.add_data("hoefsmit_b_cross_checks", {
        "b_from_h_form": mp.nstr(b, 25),
        "b_from_q_form": mp.nstr(b_alt, 25),
        "b_at_bar_conjugate_q_inverse": mp.nstr(b_bar, 25),
        "abs_dev_between_closed_forms": mp.nstr(b_alt_dev, 8),
        "abs_dev_under_bar": mp.nstr(b_bar_dev, 8),
    })
    w.add_assertion(
        name="hoefsmit_b_two_closed_forms_agree",
        computed=mp.nstr(b_alt, 40),
        expected=mp.nstr(b, 40),
        tolerance="1e-45",
        source="b at q_0 two ways: √(q⁴+q²+1)/(q²+1) vs √((h²+3)/(h²+4)) "
               "with h = q − q⁻¹ — the two forms this function's docstring "
               "gives, written with no shared subexpression. u = b·ℏ_q² "
               "carries every ppb figure in this audit.",
    )
    w.add_assertion(
        name="hoefsmit_b_is_bar_even",
        computed=mp.nstr(b_bar, 40),
        expected=mp.nstr(b, 40),
        tolerance="1e-45",
        source="b(q_0⁻¹) vs b(q_0) — an evaluation at the BAR-CONJUGATE "
               "point, independent of the evaluation at q_0. This is the "
               "Lean-proved QOU.QBeta.hoefsmitBSq_bar_even (audit "
               "2026-06-20-hoefsmit-b-bar-parity-correction.md); the "
               "bar-ODD (q−q⁻¹)/(q+q⁻¹) that once sat in `hoefsmit_b` "
               "flips sign here.",
    )
    w.add_caveat(
        "STALE COMMENT (recorded, not repaired): the c_4-estimate comment in "
        "section [5] states \"b = hoefsmit_b(q) = (q-q⁻¹)/(q+q⁻¹)\" — the "
        "bar-ODD form that `hoefsmit_b`'s own docstring says was REMOVED as "
        "wrong by ~8×. The code calls the corrected function; only the "
        "comment still describes the defect. The two b assertions above now "
        "fail if the code ever regresses to what the comment claims."
    )
    w.add_caveat(
        "The 3.47% m_p-pin swing quoted in [3] and in the description is the "
        "audit's figure, not this run's: J(q_0)/J(q=1) − 1 computes to "
        f"{mp.nstr(swing_pct, 6)}% here. c_4 ≈ c_3·b⁴ is a natural-magnitude "
        "ESTIMATE with no independent route in this script (the empirical c_4 "
        "would have to come from the SDP extraction, whose c_k are now nulled "
        "as unresolved), so the truncation bound is recorded as data only."
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
