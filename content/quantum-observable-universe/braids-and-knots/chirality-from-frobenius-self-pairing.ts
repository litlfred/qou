import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:chirality-from-frobenius-self-pairing",
  title:
    "Chirality factor from Frobenius self-pairing: $a_K = \\langle \\beta, \\beta^{\\ast} \\rangle_\\tau$",
  lean: {
    decl: "QOU.BraidKnot.chirality_frobenius_self_pairing",
    validation: "not_checked",
  },
  uses: [
    "prop:figure-eight-bw-coefficients",
    "thm:frobenius-codim-universal",
    "thm:jones-markov-trace",
    "thm:knot-mass-formula-unified",
    "prop:mass-formula-regime-switching",
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
