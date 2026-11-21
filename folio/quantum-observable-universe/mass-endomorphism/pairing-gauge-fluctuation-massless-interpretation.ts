import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:pairing-gauge-fluctuation-massless",
  label: "rem:pairing-gauge-fluctuation-massless-interpretation",
  title:
    "Interpretation: pairing fluctuations as a graviton candidate",
  tags: [
    "interpretation",
    "graviton",
    "pairing",
    "gauge-invariance",
    "zero-mode",
  ],
  uses: [
    "prop:pairing-gauge-fluctuation-massless",
    "conj:mass-endomorphism",
    "def:frobenius-pairing",
  ],
});
