import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:skew-poisson-integration",
  lean: { ref: "qou:QOU.Archimedean.skew_poisson_integration",
    validation: "not_checked",
  },
  title: "Integration of skewed-Poisson structures",
  uses: ["def:witt-vector-lift"],
  proofs: ["prf:skew-poisson-integration"],
});
