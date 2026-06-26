import { theorem } from "../../schema/builders";

export default theorem({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "While the specific result is a straightforward categorical triviality (that Hom-spaces over a fixed monoidal category do not depend on the differential layer $d_q$), the mathematical novelty lies in establishing this exact independence as the formal mechanism that permits properties to safely propagate from the deformed observable phase space ($q > 1$) directly to the unphysical/classical substrate ($q = 1$) without discontinuity." },
  ],
  label: "thm:observability-q-independent",
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
