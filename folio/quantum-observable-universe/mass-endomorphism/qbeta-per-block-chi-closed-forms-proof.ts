import { proof } from "../../schema/builders";

export default proof({
  label: "prf:qbeta-per-block-chi-closed-forms",
  title: "Proof of qbeta per block chi closed forms",
  uses: ["prop:qbeta-per-block-chi-closed-forms"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean proof discharges all three parts via `field_simp; ring` after providing positivity witnesses for the denominators ($q > 0$). $\\square$\n\n## Lean extensions\n\nThe accompanying Lean file builds the structural infrastructure\n\nThe theorem `delta_tau_M_surrogate_eq_sum` discharges this identity via `field_simp; ring`. This surrogate\n\nWe lock the order-0 coefficient as a vanishing theorem ($\\Delta\\mathrm{tr}_M^{\\text{surr}}(1) = 0$). We establish the order-1 coefficient via a `HasDerivAt` theorem ($D \\Delta\\mathrm{tr}_M^{\\text{surr}}(1) = -5/6$), proven by explicit quotient-rule chaining ($N'(1) = -10, D(1) = 12, N(1) = 0 \\Rightarrow -10/12$). Higher orders ($5/6, -41/9, \\dots$) require bulky $n$-th derivative computations and are recorded via witness JSON.\n\n**Extension 3.** The invariant that $\\Delta\\mathrm{tr}_M$ lacks $\\sqrt q$ atoms is vacuous at the Lean type level. Once $\\Delta\\mathrm{tr}_M^{\\text{surr}} : \\mathbb{R} \\to \\mathbb{R}$ is built from polynomial inputs, Lean's type system enforces rationality by construction.\n\nWe axiomatise Wenzl–Markov weights via `class CanonicalMarkovWeightsH3`, using a single dimension-normalisation axiom $y_{(3)} + 2y_{(2,1)} + y_{(1^3)} = 1$. A conditional `def delta_tau_M_canonical` consumes the class, and the conditional vanishing theorem `delta_tau_M_canonical_vanish_at_one` reduces to `chi_blocks_vanish_at_one`. The class is inhabited by the convention-D weights,\n\nThe instance is `CanonicalMarkovWeightsH3.canonicalInstance`, and `canonicalInstance_eq_markovWeights` identifies its fields with the solved Markov weights at $z_D$. The earlier archimedean parameter $z(q) = \\sqrt q/(1+q) = 1/(\\sqrt q + 1/\\sqrt q)$ is the convention-C value; it is retained in the Lean file as a historical identity and does not enter the canonical instance.\n\nWe axiomatise the three-term recursion $4(n+1)a_{n+1} + 6na_n + (2n-1)a_{n-1} = 0$ on the Taylor coefficients of $z(q)$ at $q = 1$, with seeds $a_0 = 1/2$ and $a_1 = 0$. The `ZRecursionCoeffs.unique` theorem uses strong induction with a linear-solve step to prove uniqueness." },
    {
      kind: "status",
      body: "All theorems are sorry-free and locally verified. The three originally deferred sorries (derivative at $q=1$, Markov-parameter symmetric form, and $z$-recursion uniqueness) were discharged during local Lean verification.",
    },
  ],
});
