import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:trace-ratio-observable",
  title:
    "The physical observable: ratio of Markov-traced generator volumes",
  tags: [
    "markov-trace",
    "observable",
    "matrix-element",
    "half-life",
    "generator-volume",
    "ratio",
  ],
  lean: {
    decl: "QOU.Descartes.trace_ratio_observable",
    validation: "not_checked",
  },
  uses: ["thm:markov-trace-factorization"],
});
