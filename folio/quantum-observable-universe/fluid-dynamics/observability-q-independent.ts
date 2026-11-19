import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:observability-q-independent",
  lean: { ref: "qou:QOU.FluidDynamics.observability_q_independent", validation: "not_checked" },
  title:
    "Observability is a base property: $\\mathrm{Hom}(\\mathbf{1}, \\mathrm{Ad}(A)) = 0$ is independent of the aether section",
  uses: ["def:substrate-line-bundle"],
  tags: [
    "observability",
    "q-independent",
    "base-property",
    "categorical",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Mathematical novelty: independence of Hom-spaces from the differential layer d_q carries observability across the transition from the regular deformed phase (q > 1) to the classical point (q = 1).",
    },
  ],
});
