import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:wedderburn-mass-formula",
  proofs: ["prf:wedderburn-mass-formula"],
  title: "Three-invariant atomic mass formula",
  lean: { ref: "qou:QOU.WedderburnMass.atomicMass",
    validation: "not_checked",
  },
});
