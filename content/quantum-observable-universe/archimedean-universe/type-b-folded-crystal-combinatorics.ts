import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:type-b-folded-crystal-combinatorics",
  title:
    "Type-B folded crystal combinatorics: $c(\\lambda) + c(\\lambda^T) = 0$ summand-by-summand",
  uses: [
    "prop:crystal-basis-resolves-mass-tower-open-problems",
    "prop:chirality-writhe-ribbon-derivation",
  ],
  cites: ["kashiwara1991", "brundankleshchev2009", "lecouvey2007"],
  tags: [
    "type-b-folding",
    "kashiwara-crystal",
    "partition-content",
    "transpose-involution",
    "chirality-factor",
    "combinatorics",
  ],
  lean: {
    ref: "qou:QOU.Descartes.TypeBCrystal.PartitionWithCells.content_sum_plus_transpose_content_sum_eq_zero",
    validation: "not_checked",
  },
});
