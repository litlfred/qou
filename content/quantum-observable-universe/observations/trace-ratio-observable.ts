import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:trace-ratio-observable",
  proofs: ["prf:trace-ratio-observable"],
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
  lean: { ref: "qou:QOU.Archimedean.trace_ratio_observable",
    validation: "not_checked",
  },
  uses: ["thm:markov-trace-factorization"],
  examples: [
    "ex:hadron-half-life-verification",
    "rem:hadron-half-life-regimes",
    "ex:half-life-shell-worked",
    "ex:tritium-decay-knot-equation",
    "ex:nitrogen-14-threading",
    "ex:terminal-resolution-cz",
  ],
});
