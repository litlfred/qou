import { proof } from "../../schema/builders";

export default proof({
  label: "prf:confinement-categorical",
  title: "Proof of confinement categorical",
  uses: ["prop:confinement-categorical", "prop:spectral-sequence-collapse", "prop:unified-curvature-rank-mass-formula"],
});
