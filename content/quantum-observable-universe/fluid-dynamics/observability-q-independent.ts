import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:observability-q-independent",
  proofs: ["prf:observability-q-independent"],
  lean: { ref: "qou:QOU.FluidDynamics.observability_q_independent", validation: "not_checked" },
  title:
    "Observability is a base property: $\\mathrm{Hom}(\\mathbf{1}, \\mathrm{Ad}(A)) = 0$ is independent of the substrate section",
  uses: ["def:substrate-line-bundle"],
  tags: [
    "observability",
    "q-independent",
    "base-property",
    "categorical",
  ],
});
