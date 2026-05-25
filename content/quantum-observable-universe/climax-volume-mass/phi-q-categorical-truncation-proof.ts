import { proof } from "../../schema/builders";

export default proof({
  label: "prf:phi-q-categorical-truncation",
  proofOf: "prop:phi-q-categorical-truncation",
  uses: [
    "prop:spectral-sequence-collapse",
    "prop:curvature-rank-gb-stratification",
    "prop:unified-curvature-rank-mass-formula",
    "prop:categorical-mass-markov",
  ],
  tags: [
    "brane-tower",
    "spectral-sequence",
    "centre-stratification",
  ],
});
