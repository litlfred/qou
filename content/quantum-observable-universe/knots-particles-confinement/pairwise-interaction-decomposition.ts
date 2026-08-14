import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:pairwise-interaction-decomposition",
  title: "Every interaction decomposes into two-particle crossings",
  tags: [
    "braiding",
    "yang-baxter",
    "reidemeister",
    "hexagon",
    "two-body",
    "decomposition",
  ],
  lean: {
    ref: "qou:QOU.Braiding.pairwise_interaction_decomposition",
    validation: "not_checked",
  },
  uses: ["def:quantum-universe"],
  cites: ["kassel1995", "turaev2010"],
});
