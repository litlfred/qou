import { remark } from "../../schema/builders";

/**
 * Consolidated knot–particle–force dictionary with flavor layer.
 *
 * This remark synthesizes the eightfold-way classification developed
 * in this chapter with the knot-particle dictionary from Ch 9.
 * It adds the flavor quantum numbers (I₃, Y) to the existing
 * dictionary entries and notes which entries have derived vs open
 * charge assignments.
 */
export default remark({
  label: "rem:dictionary-flavor-layer",
  title: "The knot--particle--force dictionary: flavor supplement",
  interprets: "prop:schur-weyl-eightfold",
  uses: [
    "rem:knot-particle-dictionary",
    "prop:a2-from-three-strands",
    "rem:flavor-charge-assignments",
    "prop:meson-octet-decomposition",
    "prop:schur-weyl-eightfold",
    "prop:color-su3-from-g2",
  ],
});
