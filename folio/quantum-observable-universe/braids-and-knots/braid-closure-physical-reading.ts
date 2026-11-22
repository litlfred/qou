import { remark } from "../../schema/builders";

export default remark({
  label: "rem:braid-closure-physical-reading",
  title:
    "Braid closure adds cups and caps, not crossings: two steps, and what an unseen " +
    "intermediate is",
  interprets: "prop:closure-unseen-subword",
  uses: [
    "prop:closure-unseen-subword",
    "rem:categorical-trace-is-the-markov-trace",
    "rem:observation-braid",
    "prop:helicity-conservation",
  ],
  cites: ["reshetikhin-turaev1990", "komendarczyk2008"],
  tags: [
    "braid-closure",
    "interpretation",
    "entanglement",
    "observation",
    "helicity",
  ],
});
