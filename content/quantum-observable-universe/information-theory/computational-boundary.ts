import { definition } from "../../schema/builders";

export default definition({
  label: "def:computational-boundary",
  title: "Computational boundary of a resolution tree",
  tags: [
    "P-vs-NP",
    "computational-horizon",
    "jet-horizon",
    "resolution-tree",
    "complexity",
    "information-barrier",
  ],
  lean: {
    ref: "qou:QOU.PvsNPBoundary.computationalBoundary",
    validation: "not_checked",
  },
  uses: [
    "def:polynomial-observable-subcategory",
    "def:jet-horizon",
  ],
});
