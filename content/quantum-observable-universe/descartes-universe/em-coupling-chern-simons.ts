import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:em-coupling-chern-simons",
  title:
    "Fine structure constant with Chern-Simons correction on Bring's surface",
  lean: {
    decl: "QOU.DescartesUniverse.em_coupling_chern_simons",
    validation: "not_checked",
  },
  uses: [
    "prop:em-coupling-projection",
    "def:brings-surface",
    "prop:torus-knot-generators",
    "def:knot-particle-generation",
    "thm:topological-mass",
  ],
  tags: [
    "fine-structure",
    "chern-simons",
    "brings-surface",
    "genus-4",
    "torus-knot",
    "gram-matrix",
  ],
});
