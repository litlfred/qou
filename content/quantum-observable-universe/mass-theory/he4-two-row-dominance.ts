import { proposition } from "../../schema/builders";

/**
 * Two-row stratum dominance in the ⁴He canonical Markov trace.
 *
 * Let β_{⁴He} = canonical atomic braid word for ⁴He (Z=2, N=2) on
 * H_12(q), 47 crossings with 3 operator-valued interfaces (pp at
 * gen 2, pn at gen 5, nn at gen 8), per
 *
 *   mass_at_3A_proper.atom_braid_word_3A(2, 2).
 *
 * Define the per-partition contribution
 *
 *   c_λ(q_0) := y_λ(q_0) · χ^λ_q(β_{⁴He})
 *
 * (Wenzl Markov weight × Hoefsmit per-irrep character at the
 * substrate parameter q_0).  Numerical evaluation at 50 dps via
 * the per-irrep numeric Hoefsmit path
 * (`wedderburn_jones_markov.global_wedderburn_sum_q_hecke_seminormal`
 * machinery) gives, across all 77 partitions of 12:
 *
 *   Σ_λ c_λ(q_0) = tr_M(β_{⁴He})(q_0) = 0.05534835.
 *
 * **Proposition.** The two-row stratum (def:two-row-stratum)
 * carries the trace at ≥ 80 %:
 *
 *   |Σ_{λ ∈ Λ²(12)} c_λ| / |tr_M(β_{⁴He})| ≥ 0.80.
 *
 * Empirically (witness): the ratio is **86.6 %**.  Top-5
 * binding-receptive blocks (all in Λ²(12)):
 *
 *   [9, 3]   29.0 %
 *   [8, 4]   23.6 %
 *   [10, 2]  13.5 %
 *   [7, 5]   10.3 %
 *   [11, 1]  10.2 %
 *
 * The trivial rep [12] contributes only 2.9 %; the sign rep
 * [1¹²] is sub-1e-9.
 *
 * Independent of (and confirming)
 * delta_lambda_2row_stratum_analysis.py — which established the
 * same pattern empirically across {D, T, ³He, ⁴He}: the dominant
 * Wedderburn block is always two-row.
 *
 * **Conditional on:** the empirical witness file
 * `he4-canonical-tr-m-block-fingerprint.witness.json`.  Per
 * AGENTS.md §3b-cond, the Lean proposition is axiomatised as a
 * class `HasHe4TwoRowDominance` whose instance encodes the
 * witness-verified 86.6 % figure.  Downstream propositions
 * consume the class as a `[HasHe4TwoRowDominance]` hypothesis.
 *
 * Used by:
 *   - rem:he4-magic-shell-fingerprint — physical interpretation
 *     (q-symmetric pairing magic shell).
 *
 * Witness:
 *   computations/he4-canonical-tr-m-block-fingerprint.witness.json
 * Probe:
 *   computations/probe_he4_canonical_tr_m_fingerprint.py
 * Audit:
 *   docs/audits/2026-05-15-three-pr-integration.md §F1 ⁴He
 */
export default proposition({
  label: "prop:he4-two-row-dominance",
  title:
    "Two-row stratum carries $\\ge 80\\%$ of $\\mathrm{tr}_M(\\beta_{^4\\mathrm{He}})$ at $q_0$ (86.6\\% empirically)",
  uses: ["def:two-row-stratum"],
  computation: {
    engine: "scipy",
    script: "computations/probe_he4_canonical_tr_m_fingerprint.py",
    witness: "computations/he4-canonical-tr-m-block-fingerprint.witness.json",
    status: "verified",
    requires: ["numpy", "scipy", "sympy", "mpmath"],
  },
  lean: { ref: "qou:QOU.BraidKnot.He4TwoRowDominance.HasHe4TwoRowDominance" },
  tags: [
    "he4",
    "doubly-magic",
    "wedderburn-decomposition",
    "two-row",
    "magic-shell",
    "su2-schur-weyl",
    "f1-fingerprint",
    "verified-empirically",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "The proposition is verified at 50-dps numerical precision in the\ncompanion witness. The Lean formalisation follows the conditional-\nclass pattern (AGENTS.md §3b-cond): the witness-verified\n$86.6\\,\\%$ figure is encoded as a class\n`HasHe4TwoRowDominance` whose only `sorry` is the empirical\ninstance, and downstream propositions such as\n`rem:he4-magic-shell-fingerprint`\ntake this class as a `[HasHe4TwoRowDominance]` typeclass\nhypothesis.",
    },
  ],
});
