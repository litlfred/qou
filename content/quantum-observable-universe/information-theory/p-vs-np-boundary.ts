import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "prop:p-vs-np-boundary",
  lean: { ref: "qou:QOU.PvsNPBoundary.boundary_dichotomy" },
  title:
    "$\\mathrm{P} \\neq \\mathrm{NP}$ as jet horizon opacity",
  tags: [
    "P-vs-NP",
    "jet-horizon",
    "boundary-condition",
    "complexity",
    "information-barrier",
    "event-horizon",
    "computational-horizon",
  ],
  uses: [
    "prop:p-bandwidth-bound",
    "def:polynomial-observable-subcategory",
    "def:computational-boundary",
    "rem:substrate-gm-torsion",
  ],
  cites: ["cook1971", "freedman2003"],
});
