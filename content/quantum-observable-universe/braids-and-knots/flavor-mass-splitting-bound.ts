import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:flavor-mass-splitting-bound",
  lean: { ref: "qou:QOU.FlavorDressing.flavor_mass_splitting_bound",
    validation: "not_checked",
  },
  title: "Two-sided substrate bound on the dressed-quark splitting",
  tags: [
    "flavor",
    "dressing",
    "quark-mass",
    "substrate-bound",
    "splitting-only",
  ],
  uses: [
    "def:flavor-dressing-functor",
    "prop:flavor-dressed-mass-from-substrate-split",
    "prop:flavor-split-substrate",
  ],
  proofs: ["prf:flavor-mass-splitting-bound"],
});
