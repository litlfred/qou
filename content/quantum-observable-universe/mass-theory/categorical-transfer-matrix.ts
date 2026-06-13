import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-transfer-matrix",
  lean: { ref: "qou:QOU.Torsion.CategoricalTransferMatrix", validation: "not_checked" },
  title: "Categorical transfer matrix",
  tags: [
    "transfer-matrix", "hadron", "vertex-operator",
    "equivalence-class", "braiding", "configuration-space",
    "interaction-filtration",
  ],
  uses: [
    "rem:knot-factorization",
    "rem:jet-planck-steps",
    "rem:observation-braid",
    "def:operational-entropy",
    "conj:crystal-graph-realization",
  ],
  cites: [
    "brundankleshchev2009",
  ],
});
