import { remark } from "../../schema/builders";

export default remark({
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
    "prop:topological-mass-formula",
    "rem:skein-mass-relation",
    "prop:terminal-resolution",
    "def:substrate-parameter",
    "def:quantum-planck-constant",
  ],
});
