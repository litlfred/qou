import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:demazure-fiber-markov-trace",
  title:
    "Demazure-fiber Markov-trace functional $T^{\\mathrm{Dem}}(\\lambda; w) = y_\\lambda \\cdot D_w(\\lambda) / D_{w_0}(\\lambda)$",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.demazure_fiber_markov_trace",
    validation: "not_checked",
  },
  computation: {
    engine: "sympy",
    script: "computations/demazure_markov_trace.py",
    witness: "computations/demazure-markov-trace.witness.json",
    status: "verified",
    requires: ["sympy"],
  },
  uses: ["prop:macdonald-hook-telescope"],
  cites: ["kashiwara1991", "lecouvey2007"],
  tags: [
    "demazure",
    "markov-trace",
    "resonance",
    "kashiwara-graph",
    "weight-lattice",
    "wenzl-bridge",
    "crystal-basis-shortcut",
  ],
});
