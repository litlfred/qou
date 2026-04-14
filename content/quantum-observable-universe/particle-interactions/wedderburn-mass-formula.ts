import { proposition } from "../../schema/builders";

/**
 * Complete Wedderburn mass formula.
 */
export default proposition({
  label: "prop:wedderburn-mass-formula",
  title: "Three-invariant mass formula",
  uses: ["def:atomic-braid", "prop:atomic-lp-stability"],
});
