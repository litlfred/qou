import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:t-beta-markov-frobenius-collapse",
  title:
    "Minimum-Frobenius-norm collapse $T_\\beta = S \\cdot 1$ on $H_n(R, q)$",
  lean: {
    ref: "qou:QOU.Nuclear.QBeta.MarkovFrobeniusCollapse.t_beta_collapse",
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
