import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:parallel-fibre-noninteraction",
  title: "Parallel fibres are non-interacting (split-link trace multiplicativity)",
  lean: {
    ref: "qou:QOU.Information.OneDimChannel.ParallelNonInteraction.parallel_noninteraction",
    validation: "not_checked",
  },
  uses: ["def:one-dim-qou-channel"],
  tags: [
    "optical-fibre",
    "non-interaction",
    "markov-trace",
    "split-link",
    "commutative-monoid",
  ],
});
