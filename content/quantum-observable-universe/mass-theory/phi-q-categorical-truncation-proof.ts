import { proof } from "../../schema/builders";

export default proof({
  label: "prf:phi-q-categorical-truncation",
  of: "prop:phi-q-categorical-truncation",
  uses: [
    "prop:phi-q-categorical-truncation",
    "prop:categorical-mass-markov",
  ],
  tags: [
    "brane-tower",
    "spectral-sequence",
    "centre-stratification",
  ],
});
