import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:nucleon-mass-splitting",
  lean: { ref: "qou:QOU.HadronicMass.nucleon_mass_splitting",
    validation: "not_checked",
  },
  title: "Proton, neutron, and the $u$--$d$ dressed mass splitting",
  tags: ["proton", "neutron", "u-d-splitting", "dressed-quark-mass", "codata"],
  uses: ["lem:pair-skein-mass-formula"],
  proofs: ["prf:nucleon-mass-splitting"],
});
