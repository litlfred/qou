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
});
