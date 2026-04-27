import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:e-infinity-page-identifications",
  title:
    "$E_\\infty$-page identifications with the six mass-formula terms",
  lean: {
    ref: "qou:QOU.BraidKnot.e_infinity_identifications",
    validation: "not_checked",
  },
  uses: [
    "prop:gb-spectral-sequence",
    "prop:jet-prefix-gb-filtration",
    "prop:chirality-from-frobenius-self-pairing",
  ],
  tags: [
    "spectral-sequence",
    "hochschild",
    "page-identification",
    "mass-formula",
    "derivation",
  ],
});
