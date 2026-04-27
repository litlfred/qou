import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:feynman-eigenbasis-decomposition",
  lean: { ref: "qou:QOU.FeynmanPathIntegrals.eigenbasis_decomposition",
    validation: "not_checked",
  },
  title: "Eigenbasis decomposition for the Feynman amplitude",
  tags: ["schur-weyl", "eigenbasis", "feynman", "hecke", "decomposition"],
  uses: ["prop:knot-eigenbasis-complete"],
  proofs: ["prf:feynman-eigenbasis-decomposition"],
});
