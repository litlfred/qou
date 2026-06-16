import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:qbeta-trace-counit-convergence",
  lean: {
    ref: "qou:QOU.Interactions.QBetaConvergence.QBetaTraceCounitConvergence",
    validation: "not_checked",
  },
  title:
    "Trace–counit convergence of the $Q_\\beta$ mass difference",
  uses: [
    "prop:qbeta-counit-closed-form",
  ],
  tags: [
    "beta-decay",
    "q-value",
    "frobenius-counit",
    "markov-trace",
    "per-braid-mass-tower",
    "conjecture",
  ],
});
