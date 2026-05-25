import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:skein-mass-from-linking",
  lean: { ref: "qou:QOU.BraidsKnots.skein_mass_from_linking",
    validation: "not_checked",
  },
  title: "Mass functional on a Skein resolution: linking-energy plus constituent volume",
  tags: ["skein-resolution", "binding-energy", "torus-knot", "hopf-link"],
  uses: ["def:hadron"],
  proofs: ["prf:skein-mass-from-linking"],
});
