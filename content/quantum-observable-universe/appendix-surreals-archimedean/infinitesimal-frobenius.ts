import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:infinitesimal-frobenius",
  title:
    "Infinitesimal Frobenius pairing: $\\int_A \\circ \\mu = \\mathrm{id} + O(\\varepsilon)$",
  lean: { ref: "qou:QOU.AppendixSurreals.InfinitesimalFrobenius", validation: "stub" },
  tags: [
    "tier:P",
    "surreal-numbers",
    "frobenius",
    "infinitesimal",
    "axiom-relaxation",
    "open-problem",
  ],
  uses: ["conj:archimedean-stpart"],
  cites: ["robinson1966"],
});
