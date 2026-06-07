import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:infinitesimal-observability",
  title:
    "Infinitesimal observability: $\\mathrm{Hom}(\\mathbf{1}, \\mathrm{Ad}(A)) \\leq \\varepsilon$",
  lean: { ref: "qou:QOU.AppendixSurreals.InfinitesimalObservability", validation: "stub" },
  tags: [
    "tier:P",
    "surreal-numbers",
    "observability",
    "adjoint-cohomology",
    "infinitesimal",
    "axiom-relaxation",
    "open-problem",
  ],
  uses: ["conj:archimedean-stpart"],
  cites: ["robinson1966"],
});
