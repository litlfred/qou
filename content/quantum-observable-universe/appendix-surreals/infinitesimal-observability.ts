import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:infinitesimal-observability",
  title:
    "Infinitesimal observability: $\\mathrm{Hom}(\\mathbf{1}, \\mathrm{Ad}(A)) \\leq \\varepsilon$",
  lean: { ref: "qou:QOU.AppendixSurreals.InfinitesimalObservability", validation: "stub" },
  tags: [
    "surreal-numbers",
    "observability",
    "adjoint-cohomology",
    "infinitesimal",
    "axiom-relaxation",
    "open-problem",
  ],
  uses: ["prop:archimedean-stpart"],
  cites: ["robinson1966"],
});
