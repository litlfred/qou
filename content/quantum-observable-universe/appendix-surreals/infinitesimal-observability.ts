import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:infinitesimal-observability",
  title:
    "Infinitesimal observability: $\\mathrm{Hom}(\\mathbf{1}, \\mathrm{Ad}(A)) \\leq \\varepsilon$",
  tags: [
    "surreal-numbers",
    "observability",
    "adjoint-cohomology",
    "infinitesimal",
    "axiom-relaxation",
    "open-problem",
  ],
  uses: [
    "def:quantum-observable-universe",
    "def:standard-part-functor",
    "conj:archimedean-stpart",
  ],
  cites: ["robinson1966"],
});
