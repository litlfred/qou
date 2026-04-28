import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:deuteron-binding-energy",
  lean: { ref: "qou:QOU.HadronicMass.deuteron_binding_energy",
    validation: "not_checked",
  },
  title: "Deuteron binding energy from Skein-polynomial smoothing",
  tags: ["deuteron", "binding-energy", "skein-polynomial", "codata"],
  uses: ["lem:nucleon-mass-splitting"],
  proofs: ["prf:deuteron-binding-energy"],
});
