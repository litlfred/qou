import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:chirality-from-frobenius-self-pairing",
  title:
    "Chirality factor from Frobenius self-pairing: $a_K = \\langle \\beta, \\beta^{\\ast} \\rangle_\\tau$",
  // The ref now names a DECLARATION, not the module. The bare
  // `QOU.BraidKnot.chirality_frobenius_self_pairing` matched the file
  // `QOU/BraidKnot/chirality_frobenius_self_pairing.lean` but no declaration
  // inside it.
  //
  // Target: `chirality_amphichiral_via_qInt3`, the derivation (field-generic,
  // `field_simp; ring`) of the amphichiral chirality factor `1 − h² = 4 − [3]_q`
  // — item 2 of this block. The Fricke identity feeding it is
  // `chirality_figure_eight_character` in the same module.
  //
  // Items 1 (chiral, `a_K = 1 + w(K)·h + O(h²)`) and 3 (Borromean product over
  // amphichiral sublinks) are NOT formalised.
  lean: {
    ref: "qou:QOU.BraidKnot.ChiralityFrobenius.chirality_frobenius_self_pairing.chirality_amphichiral_via_qInt3",
    validation: "not_checked",
  },
  uses: [
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
