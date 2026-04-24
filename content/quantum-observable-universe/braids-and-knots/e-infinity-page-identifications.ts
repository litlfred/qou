import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:e-infinity-page-identifications",
  title:
    "$E_\\infty$-page identifications with the six mass-formula terms",
  lean: {
    decl: "QOU.BraidKnot.e_infinity_identifications",
    validation: "not_checked",
  },
  uses: [
    "prop:gb-spectral-sequence",
    "thm:knot-mass-formula-unified",
    "thm:frobenius-codim-universal",
    "prop:mass-endomorphism-tower",
    "prop:gb-residue-spectral-sum",
    "prop:jet-prefix-gb-filtration",
    "prop:chirality-from-frobenius-self-pairing",
    "def:confinement-level",
    "thm:jones-markov-trace",
  ],
  tags: [
    "spectral-sequence",
    "hochschild",
    "page-identification",
    "mass-formula",
    "derivation",
  ],
});
