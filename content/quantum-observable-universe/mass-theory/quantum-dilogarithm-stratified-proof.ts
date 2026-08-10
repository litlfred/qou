import { proof } from "../../schema/builders";

export default proof({
  label: "prf:quantum-dilogarithm-stratified",
  of: "prop:quantum-dilogarithm-stratified",
  uses: [
    "prop:quantum-dilogarithm-stratified",
    "cor:quantum-dilogarithm",
    "prop:categorical-mass-markov",
    "prop:curvature-rank-gb-stratification",
  ],
  tags: [
    "quantum-dilogarithm",
    "brane-tower",
    "centre-stratification",
  ],
});
