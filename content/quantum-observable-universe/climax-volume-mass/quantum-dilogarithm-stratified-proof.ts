import { proof } from "../../schema/builders";

export default proof({
  label: "prf:quantum-dilogarithm-stratified",
  proofOf: "prop:quantum-dilogarithm-stratified",
  uses: [
    "cor:quantum-dilogarithm",
    "prop:curvature-rank-gb-stratification",
    "prop:spectral-sequence-collapse",
    "prop:categorical-mass-markov",
  ],
  tags: [
    "quantum-dilogarithm",
    "brane-tower",
    "centre-stratification",
  ],
});
