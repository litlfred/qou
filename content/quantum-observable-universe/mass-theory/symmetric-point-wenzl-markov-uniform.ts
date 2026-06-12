import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:symmetric-point-wenzl-markov-uniform",
  title:
    "Uniform Wenzl/Markov measure at $q = 1$: $y_\\lambda(1) = 1/2^{n-1}$ on $H_n(q)$",
  lean: { ref: "qou:QOU.BraidsAndKnots.symmetric_point_wenzl_markov_uniform" },
  uses: [
    "prop:borromean-markov-trace-closed-form",
    "rem:symmetric-point-resolution-loss",
  ],
  cites: [
    "jones1987",
  ],
  tags: [
    "wenzl-weights",
    "markov-trace",
    "symmetric-point",
    "q-deformation",
    "categorical-derivation",
  ],
});
