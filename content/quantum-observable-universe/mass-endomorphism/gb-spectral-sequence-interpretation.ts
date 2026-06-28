import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:gb-spectral-sequence",
  label: "rem:gb-spectral-sequence-interpretation",
  title:
    "What remains open, structural value, and the Picard–Lefschetz archimedean realisation",
  tags: [
    "spectral-sequence",
    "cohomology",
    "hochschild",
    "gb-filtration",
    "picard-lefschetz",
    "derivation-chain",
  ],
  uses: [
    "prop:gb-spectral-sequence",
    "thm:frobenius-codim-universal",
    "prop:mass-formula-regime-switching",
  ],
});
