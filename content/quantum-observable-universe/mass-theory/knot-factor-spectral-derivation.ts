import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:knot-factor-spectral-form",
  proofs: ["prf:knot-factor-spectral-form"],
  title:
    "Knot factor $a_K$ as a chirality-block Plancherel pairing",
  lean: {
    ref: "qou:QOU.BraidKnot.knot_factor_spectral_form",
    validation: "not_checked",
  },
  uses: ["rem:gram-matrix-spectral-connection"],
  tags: [
    "knot-factor",
    "chirality",
    "gram-matrix",
    "plancherel",
    "wedderburn",
    "amphicheiral",
    "borromean",
    "shell-closed",
    "no-ad-hoc-fits",
  ],
});
