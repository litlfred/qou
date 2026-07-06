import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:chirality-from-frobenius-self-pairing",
  title:
    "Chirality factor from Frobenius self-pairing: $a_K = \\langle \\beta, \\beta^{\\ast} \\rangle_\\tau$",
  lean: {
    ref: "qou:QOU.BraidKnot.chirality_frobenius_self_pairing",
    validation: "not_checked",
  },
  uses: [
    "prop:mass-formula-regime-switching",
    "def:frobenius-self-pairing-chirality",
  ],
  tags: [
    "chirality",
    "frobenius",
    "self-pairing",
    "writhe",
    "amphichiral",
    "borromean",
    "categorical",
  ],
});
