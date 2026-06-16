import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:t-beta-markov-frobenius-collapse",
  title:
    "Min-Frobenius-norm collapse: T_β = S · 1 under the canonical Markov-trace inner product on H_n(R, q)",
  lean: {
    ref: "qou:QOU.QBeta.MarkovFrobeniusCollapse.t_beta_collapse",
    validation: "not_checked",
  },
  uses: [
    "prop:markov-trace-frobenius-selection",
  ],
  cites: ["jones1987", "wenzl1988"],
  computation: {
    engine: "sympy",
    script:
      "computations/qbeta/qbeta_markov_trace_norm_probe.py",
    witness:
      "computations/qbeta/qbeta-markov-trace-norm-probe.witness.json",
    status: "verified",
  },
  tags: [
    "markov-trace",
    "frobenius",
    "q-beta",
    "min-norm",
    "categorical-collapse",
  ],
});
