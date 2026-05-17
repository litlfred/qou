import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:flavor-split-substrate",
  lean: { ref: "qou:QOU.HadronicMass.flavor_split_substrate",
    validation: "not_checked",
  },
  title: "Substrate-pure derivation of the $u$--$d$ flavor split",
  tags: ["flavor-split", "u-d-splitting", "substrate-only", "no-fit",
         "hecke-substrate-atoms", "categorical-derivation"],
  uses: [
    "lem:nucleon-mass-splitting",
    "lem:pair-skein-mass-formula",
  ],
  proofs: ["prf:flavor-split-substrate"],
});
