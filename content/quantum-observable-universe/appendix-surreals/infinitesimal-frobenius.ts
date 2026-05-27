import { conjecture } from "../../schema/builders";

export default proposition({
  label: "prop:infinitesimal-frobenius",
  title:
    "Infinitesimal Frobenius pairing: $\\int_A \\circ \\mu = \\mathrm{id} + O(\\varepsilon)$",
  lean: { ref: "qou:QOU.AppendixSurreals.InfinitesimalFrobenius", validation: "stub" },
  tags: [
    "surreal-numbers",
    "frobenius",
    "infinitesimal",
    "axiom-relaxation",
    "open-problem",
  ],
  uses: ["prop:archimedean-stpart"],
  cites: ["robinson1966"],
});
