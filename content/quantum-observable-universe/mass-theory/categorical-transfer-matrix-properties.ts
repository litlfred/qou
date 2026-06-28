import { remark } from "../../schema/builders";

export default remark({
  label: "rem:categorical-transfer-matrix-properties",
  interprets: "def:categorical-transfer-matrix",
  title:
    "Configuration space, bi-filtration, and categorification of $\\mathcal{T}(\\mathfrak{H})$",
  tags: [
    "transfer-matrix", "hadron", "vertex-operator",
    "equivalence-class", "braiding", "configuration-space",
    "interaction-filtration",
  ],
  uses: [
    "def:categorical-transfer-matrix",
    "def:hadron",
    "def:localized-hadron",
    "def:exceptional-divisor",
    "rem:knot-factorization",
    "def:vertex-operator",
    "rem:observation-braid",
    "prop:jet-prolongation",
    "rem:jet-planck-steps",
    "def:bundle-initial-conditions",
    "def:operational-entropy",
    "thm:markov-trace-product",
    "conj:crystal-graph-realization",
  ],
  cites: [
    "brundankleshchev2009",
  ],
});
