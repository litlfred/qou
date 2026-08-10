import { proof } from "../../schema/builders";

export default proof({
  label: "prf:phi-q-categorical-truncation",
  of: "prop:phi-q-categorical-truncation",
  uses: [
    "prop:phi-q-categorical-truncation",
    "prop:categorical-mass-markov",
    "prop:curvature-rank-gb-stratification",
    "prop:spectral-sequence-collapse",
    "prop:unified-curvature-rank-mass-formula",
  ],
  tags: [
    "brane-tower",
    "spectral-sequence",
    "centre-stratification",
  ],
});
