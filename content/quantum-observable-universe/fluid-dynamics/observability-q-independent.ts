import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:observability-q-independent",
  lean: {
    decl: "QOU.FluidDynamics.observability_q_independent",
    file: "QOU/FluidDynamics.lean",
    validation: "not_checked",
  },
  title:
    "Observability is a base property: $\\mathrm{Hom}(\\mathbf{1}, \\mathrm{Ad}(A)) = 0$ is independent of the substrate section",
  uses: [
    "def:substrate-line-bundle",
    "def:quantum-observable-universe",
    "def:substrate-parameter",
  ],
  tags: [
    "observability",
    "q-independent",
    "base-property",
    "categorical",
  ],
});
