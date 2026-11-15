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
 * with denominator q^7(q^2+1)^2 after substituting h, z in q — one
 * (q^2+1) per Markov peel, the convention-D signature.
 *
 * Numerical anchor at q_0:
 *   tr_M(σ_1^7 σ_2^4)(q_0) ≈ 1.88432  (char_fast seminormal agrees to 14 digits)
 *   ρ_p^CODATA = (m_p/m_e) / |tr_M(σ_1^7σ_2^4)|(q_0) ≈ 974.44.
 *
 * The 1.63315 / 1124.3 / q^{10}(q+1)^3 this comment carried until
 * 2026-08-23 were convention-C values under a convention-D declaration.
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
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-23",
      body: `**Three numbers in this block were convention-C values printed under a convention-D declaration, and are corrected here.** The statement says \`z = q³/(q²+1)\` (**convention D**) and then quoted \`1.63315\`, \`ρ_p ≈ 1124.3\` and a denominator \`q^{10}(q+1)^3\`. Re-derived from this block's own recurrence at the proton pin, working in \`v = √q\` so the radicals do not distort the factorisation:

| | convention C | convention D (canonical) |
|---|---|---|
| denominator | \`q⁸(q+1)\` | \`q⁷(q²+1)²\` |
| \`tr_M(σ₁⁷σ₂⁴)(q₀)\` | 1.63315337744905 | 1.88431946725498 |
| \`ρ_p\` | 1124.30 | 974.44 |

The printed figures were the C column, 15.4 % from D. The stated denominator matched **neither** — \`(q+1)\` is a convention-C signature that D cannot produce (D carries one \`q²+1\` per Markov peel), and the exponents \`q^{10}\` and the cube are separately unexplained by either.

**This diagnosis was already in the sidecar and is re-confirmed, not new.** A prior agent (\`agent:h00\`) recorded it with the same two values — but under the criterion \`trap-superlative\`, a *language-trap* check. Nobody triaging language traps would act on a convention mislabel, and nobody grepping for convention problems would look there, which is presumably why it sat unfixed. Filed under the wrong criterion is close to not filed.

**The comparison claim survives the correction, and was understated.** "Matches the seminormal-derived \`char_fast\` Markov trace to better than 0.1 %" reads like a convention discriminator; it is not. The seminormal route takes its \`y_λ\` from the same three axioms, so it follows whichever \`z\` it is given and reproduces the closed form **in either frame** — measured at 14 digits in each, not 0.1 %. The block now says so.

**A by-product worth recording.** Solving the Markov weights at the canonical \`z\` returns \`y_{(1,1,1)} = −1.07e-17\`, i.e. exactly zero — the \`y_{(1³)} = 0\` that AGENTS.md records as forced by the mass fibre's row cap. That is the same fact as the convention-D Gram radical in \`prop:gram-matrix-h3-symbolic\`: the sign representation drops out of the trace, so the Gram form degenerates in precisely that direction. The two blocks were found separately and are one phenomenon.`,
      see: "computations/markov/markov_trace_axiomatic_proton.py",
    },
  ],
  computation: {
    engine: "sympy",
    script:
      "computations/markov/markov_trace_atomic_proton_full.py",
    witness: [
      "computations/markov/markov-trace-atomic-proton-full.witness.json",
      "computations/markov/markov-trace-axiomatic-proton.witness.json",
    ],
    status: "verified",
    // status was "verified" until 2026-08-23 without ever having been checked;
    // the cited witness's own `allPassed` was false. It went "failed" when
    // scripts/check-computation-status.py first compared the two, and back to
    // "verified" once the producer was fixed — which took removing assertions,
    // not adding tolerance.
    //
    // The two red assertions (`anti_self_reciprocal`, `symmetric_under_q_inv`)
    // were SPURIOUS on four counts. They cited "§ anti-self-reciprocal" and
    // "§ q-inverse symmetry" of this block, which has neither section. They
    // were computed on σ_1σ_2σ_1, not on the σ_1^7σ_2^4 this block states.
    // Neither property holds, in convention C or D. And they are unsatisfiable
    // as a PAIR whatever the trace: f(1/q) = f(q) together with f(1/q) = -f(q)
    // forces f == 0, yet both carried expected=1.0 — so the witness could not
    // have gone green under any convention or any braid word.
    //
    // The producer now witnesses what the block claims — the σ_1^7σ_2^4 closed
    // form, its exact denominator, its value at q_0, and ρ_p — and reports the
    // q → 1/q ratio as data. It also moved off float64 (it was downcasting
    // q_0 through `float()`).,
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
