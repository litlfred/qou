import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:gram-determinant-plancherel-ratio",
  title:
    "Gram-determinant ratio $\\kappa$ as a Plancherel-weighted character product",
  lean: {
    ref: "qou:QOU.Descartes.gram_determinant_plancherel_ratio",
    validation: "not_checked",
  },
  uses: [
    "prop:force-carrier-bring-uniqueness",
    "thm:em-spectral-completeness",
    "rem:gram-matrix-spectral-connection",
  ],
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
