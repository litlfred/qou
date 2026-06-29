import { definition } from "../../schema/builders";

export default definition({
  label: "def:polynomial-observable-subcategory",
  title: "Polynomial observable subcategory of a resolution tree",
  tags: [
    "P-vs-NP",
    "resolution-tree",
    "observable-subcategory",
    "markov-trace",
    "complexity",
    "computational-horizon",
  ],
  lean: {
    ref: "qou:QOU.PvsNPBoundary.polynomialObservableSubcategory",
    validation: "not_checked",
  },
  uses: [
    "rem:skein-turing-machine",
    "def:observable-subcategory",
  ],
});
