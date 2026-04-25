import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:infinitesimal-frobenius",
  title:
    "Infinitesimal Frobenius pairing: $\\int_A \\circ \\mu = \\mathrm{id} + O(\\varepsilon)$",
  tags: [
    "surreal-numbers",
    "frobenius",
    "infinitesimal",
    "axiom-relaxation",
    "open-problem",
  ],
  uses: [
    "def:frobenius-pairing",
    "def:quantum-observable-universe",
    "def:standard-part-functor",
    "conj:archimedean-stpart",
  ],
  cites: ["robinson1966"],
});
