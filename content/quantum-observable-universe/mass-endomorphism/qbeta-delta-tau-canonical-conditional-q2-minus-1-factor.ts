import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:qbeta-delta-tau-canonical-conditional-q2-minus-1-factor",
  title:
    "Conditional on canonical Markov weights: $\\Delta\\tau_M^{\\text{can}}(q)$ factors $(q^2 - 1)$",
  uses: [
    "prop:qbeta-per-block-chi-closed-forms",
  ],
  cites: ["wenzl1988", "hoefsmit1974"],
  tags: [
    "qbeta",
    "delta-tau-M",
    "canonical",
    "conditional",
    "3b-cond",
    "pre-archimedean",
  ],
  lean: {
    ref:
      "qou:QOU.BraidKnot.delta_tau_M_canonical_has_q2_minus_1_factor",
  },
  authorNotes: [
    {
      kind: "status",
      body: "This block is a AGENTS.md §3b-cond conditional theorem:\n\n- **Class axiomatisation.** The Lean\n  `class CanonicalMarkovWeightsH3` ([`qbeta-per-block-chi-closed-forms.lean`](qbeta-per-block-chi-closed-forms.lean))\n  is the single sorry point. A concrete instance would need to encode\n  the canonical Wenzl construction's $\\sqrt q$-bearing weights and\n  verify the normalisation axiom.\n- **Explicit hypothesis on Lean side.** The Lean theorem\n  `delta_tau_M_canonical_has_q2_minus_1_factor` carries\n  `[CanonicalMarkovWeightsH3]` as an explicit `[Instance]` hypothesis.\n- **Explicit conditional banner on narrative side.** The opening\n  \"Proposition (conditional on ...)\" above.\n- **`uses[]` includes the conjectural upstream.** The block uses\n  `prop:qbeta-per-block-chi-closed-forms`, whose Lean file hosts\n  the class declaration.\n\nOnce a concrete instance lands (closing the canonical weights gap),\nthis proposition becomes unconditional — fully verified by Lean.",
    },
  ],
});
