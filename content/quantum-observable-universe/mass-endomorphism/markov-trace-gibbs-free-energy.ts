import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:categorical-mass-markov",
  label: "rem:markov-trace-gibbs-free-energy",
  title:
    "Binding as a free-energy difference: the Markov trace in the partition-function slot",
  tags: [
    "markov-trace",
    "gibbs-state",
    "free-energy",
    "information",
    "channel-entropy",
  ],
  uses: ["prop:categorical-mass-markov"],
  cites: ["jones1987", "orellana1998"],
});
