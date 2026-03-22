import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:skew-poisson-integration",
  title: "Integration of skewed-Poisson structures",
  uses: ["def:witt-vector-lift"],
  proofs: ["prf:skew-poisson-integration"],
});
