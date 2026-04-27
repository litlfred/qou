import { remark } from "../../schema/builders";

/**
 * Mass comparison table Z = 1-20.
 */
export default remark({
  label: "rem:mass-table-z1-20",
  title: "Predicted vs observed masses, $Z = 1$--$20$",
  interprets: "prop:wedderburn-mass-formula",
  uses: ["rem:kashaev-volume-density"],
});
