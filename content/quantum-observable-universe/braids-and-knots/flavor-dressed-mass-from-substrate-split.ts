import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:flavor-dressed-mass-from-substrate-split",
  lean: { ref: "qou:QOU.FlavorDressing.dressed_mass_from_substrate_split",
    validation: "not_checked",
  },
  title: "Substrate-pure derivation of the dressed-quark mass splitting",
  tags: [
    "flavor",
    "dressing",
    "quark-mass",
    "substrate-derived",
    "no-fit",
  ],
  uses: [
    "def:flavor-dressing-functor",
    "prop:flavor-split-substrate",
    "lem:pair-skein-mass-formula",
  ],
  proofs: ["prf:flavor-dressed-mass-from-substrate-split"],
});
