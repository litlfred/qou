import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:p-vs-np-boundary",
  lean: { ref: "qou:QOU.InformationTheory.PvsNPBoundary.boundary_dichotomy" },
  title:
    "Speculative dictionary: $\\mathrm{P} \\neq \\mathrm{NP}$ as skein computational-boundary non-emptiness",
  tags: [
    "P-vs-NP",
    "jet-horizon",
    "boundary-condition",
    "complexity",
    "computational-horizon",
  ],
  uses: [
    "sec:p-vs-np-boundary-intro",
    "quantum-observable-universe:prop:p-bandwidth-bound",
    "quantum-observable-universe:def:polynomial-observable-subcategory",
    "quantum-observable-universe:def:computational-boundary",
    "quantum-observable-universe:rem:aether-gm-torsion",
  ],
  cites: ["cook1971", "freedman2003"],
});
