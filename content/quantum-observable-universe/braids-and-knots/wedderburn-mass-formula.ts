import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:wedderburn-mass-formula",
  title: "Three-invariant atomic mass formula",
  lean: {
    decl: "QOU.WedderburnMass.atomicMass",
    validation: "not_checked",
  },
  uses: [
    "prop:three-parameters-wedderburn",
    "prop:binding-scale-catalan",
    "thm:topological-mass",
    "def:atomic-braid",
  ],
});
