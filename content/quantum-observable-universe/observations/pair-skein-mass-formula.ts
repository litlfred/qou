import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:pair-skein-mass-formula",
  lean: { ref: "qou:QOU.HadronicMass.pair_skein_mass_formula",
    validation: "not_checked",
  },
  title: "Pair Skein mass and crossing-by-crossing recursion",
  tags: ["skein-relation", "pair-skein-mass", "borromean", "recursion"],
  uses: ["lem:nucleon-borromean-topology"],
  proofs: ["prf:pair-skein-mass-formula"],
});
