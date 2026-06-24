import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:gram-determinant-plancherel-ratio",
  proofs: ["prf:gram-determinant-plancherel-ratio"],
  title:
    "Gram-determinant ratio $\\kappa$ as a Plancherel-weighted character product",
  lean: {
    ref: "qou:QOU.Archimedean.gram_determinant_plancherel_ratio",
    validation: "not_checked",
  },
  uses: ["rem:gram-matrix-spectral-connection"],
  tags: [
    "gram-matrix",
    "plancherel",
    "wedderburn",
    "character-ratio",
    "chern-simons",
    "kappa",
    "no-hand-calculation",
  ],
});
