import { proof } from "../../schema/builders";

export default proof({
  label: "prf:qbeta-per-block-chi-closed-forms",
  title: "Proof of qbeta per block chi closed forms",
  uses: ["prop:qbeta-per-block-chi-closed-forms"],
  authorNotes: [
    {
      kind: "status",
      body: "All theorems are sorry-free and locally verified (`delta_tau_M_surrogate_eq_sum`, `CanonicalMarkovWeightsH3`, `delta_tau_M_canonical`, `delta_tau_M_canonical_vanish_at_one`, `chi_blocks_vanish_at_one`, `CanonicalMarkovWeightsH3.canonicalInstance` in `QOU.BraidKnot.QBetaCanonicalMarkovWeightsInstance`, `canonicalInstance_eq_markovWeights`, `ZRecursionCoeffs.unique`). The three originally deferred sorries (derivative at $q=1$, Markov-parameter symmetric form, and $z$-recursion uniqueness) were discharged during local Lean verification.",
    },
  ],
});
