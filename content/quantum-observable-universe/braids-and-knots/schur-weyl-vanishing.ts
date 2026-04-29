import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:schur-weyl-vanishing",
  title: "Schur-Weyl Markov-trace vanishes for partitions of height > 2",
  chapter: "braids-and-knots",
  cites: ["wenzl1988", "jones1987"],
  uses: [
    "def:hecke-mass-element",
    "prop:y-lambda-recipe-from-partition",
    "prop:atom-knot-mass-derivation",
  ],
  defines: [],
  tags: ["normalization", "habiro", "jones", "no-fitting"],
  lean: { ref: "qou:QOU.BraidKnot.schur_weyl_weight_vanish_height_gt_2" },
});
