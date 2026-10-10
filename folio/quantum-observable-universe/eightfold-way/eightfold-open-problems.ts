import { remark } from "../../schema/builders";

/**
 * Open problems in the eightfold-way derivation.
 *
 * Consolidates all gaps identified during the chapter's construction.
 * Each gap is stated precisely with its discriminator test, so that
 * future work can be targeted and claims can be falsified.
 */
export default remark({
  label: "rem:eightfold-open-problems",
  title: "Open problems",
  interprets: "prop:schur-weyl-eightfold",
  uses: [
    "prop:a2-from-three-strands",
    "prop:color-su3-from-g2",
    "prop:schur-weyl-eightfold",
    "rem:flavor-charge-assignments",
  ],
});
