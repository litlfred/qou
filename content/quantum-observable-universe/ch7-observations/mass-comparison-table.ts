import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:topological-mass-formula",
  label: "rem:mass-comparison-table",
  title: "Mass predictions from knot formulas vs.\\ CODATA/PDG values",
  tags: [
    "mass",
    "prediction",
    "CODATA",
    "PDG",
    "comparison",
    "knot",
    "experimental",
  ],
  uses: [
    "rem:knot-formula-table",
    "rem:mass-from-generators",
  ],
});
