import { proposition } from "../../schema/builders";

/**
 * Direct axiomatic closed form of the Markov trace for atomic-braid
 * words in H_n(q), bypassing representation theory.
 *
 * The Markov trace tr_M : ⊔_n H_n(q) → ℚ(q) is uniquely determined by:
 *
 *   tr_M(1)            = 1                                    (normalisation)
 *   tr_M(α · σ_n)      = z · tr_M(α)  for α ∈ H_n  ⊂ H_{n+1}  (Markov axiom)
 *   tr_M(α β)          = tr_M(β α)                            (cyclicity)
 *
 * combined with the Hecke quadratic σ_i² = h σ_i + 1 (h = q - q⁻¹)
 * and the braid relations.
 *
 * For the proton's atomic-braid word σ₁⁷ σ₂⁴ ∈ H₃(q), this gives the
 * exact closed form via the Hecke-power recurrence
 *
 *   σ_i^k = a_k(h) σ_i + b_k(h),
 *   a_{k+1} = h a_k + b_k,   b_{k+1} = a_k,   a₀ = 0, b₀ = 1.
 *
 * Markov-trace values on the H₃ basis (axiom-determined):
 *   tr_M(1)          = 1,
 *   tr_M(σ_i)        = z,                  z = q^{3}/(q^{2}+1)   (convention D),
 *   tr_M(σ_1 σ_2)    = z²,
 *   tr_M(σ_1 σ_2 σ_1) = z(1 + h z) = z + h z²,
 *
 * yielding the closed form
 *
 *   tr_M(σ_1^7 σ_2^4)(q) = a_7 a_4 z² + (a_7 b_4 + b_7 a_4) z + b_7 b_4
 *
 * with denominator q^{10}(q+1)^3 after substituting h, z in q.
 *
 * Numerical anchor at q_0:
 *   tr_M(σ_1^7 σ_2^4)(q_0) ≈ 1.63315  (matches char_fast Markov to <0.1%)
 *   ρ_p^CODATA = (m_p/m_e) / |tr_M(σ_1^7σ_2^4)|(q_0) ≈ 1124.3.
 *
 * This proposition supplies the categorical-mass anchor for
 * `prop:atomic-mass-gb-nf` independent of any seminormal/Hoefsmit
 * representation construction, so it cannot fail on σ_2 IndexError-
 * type representation-coding bugs.
 */
export default proposition({
  label: "prop:markov-trace-axiomatic-closed-form",
  title:
    "Direct axiomatic closed form of the Markov trace for atomic-braid words in $H_n(q)$",
  uses: [
    "prop:markov-trace-antipode-polynomial-symmetry",
  ],
  cites: ["jones1987", "kassel1995", "wenzl1988", "kauffman1991"],
  computation: {
    engine: "sympy",
    script:
      "computations/markov/markov_trace_atomic_proton_full.py",
    witness: [
      "computations/markov/markov-trace-atomic-proton-full.witness.json",
      "computations/markov/markov-trace-axiomatic-proton.witness.json",
    ],
    status: "failed",
    // status was "verified" until 2026-08-23; the cited witness's own
    // `allPassed` is false (anti_self_reciprocal). Per ComputationStatus,
    // "failed" = script ran, witness does NOT match expected values.
    // Nothing compared the two until scripts/check-computation-status.py.,
    requires: ["sympy"],
  },
  lean: {
    ref: "qou:QOU.BraidKnot.markovTraceAxiomaticClosedForm",
    validation: "not_checked",
  },
  tags: [
    "markov-trace",
    "hecke-quadratic",
    "axiomatic-reduction",
    "closed-form",
    "atomic-braid",
    "proton",
    "categorical-mass-anchor",
  ],
});
