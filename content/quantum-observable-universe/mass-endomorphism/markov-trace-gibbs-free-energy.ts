import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:categorical-mass-markov",
  label: "rem:markov-trace-gibbs-free-energy",
  title:
    "The Markov trace as a temperature state: binding as a free-energy difference",
  tags: [
    "markov-trace",
    "gibbs-state",
    "free-energy",
    "information",
    "channel-entropy",
  ],
  uses: ["prop:categorical-mass-markov"],
  cites: ["jones1987"],
});
