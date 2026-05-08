import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:wedderburn-mass-formula",
  title: "Three-invariant atomic mass formula",
  lean: { ref: "qou:QOU.WedderburnMass.atomicMass",
    validation: "not_checked",
  },
  uses: [
    "prop:atomic-mass-gb-nf",
    "prop:three-parameters-wedderburn",
    "prop:binding-scale-catalan",
    "def:atomic-braid",
  ],
});
