import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:qou-p-neq-np",
  title:
    "$\\mathrm{P} \\neq \\mathrm{NP}$ at non-torsion $q \\in \\mathbb{G}_m$",
  lean: { ref: "qou:QOU.Information.QouPNeqNp", validation: "stub" },
  tags: [
    "P-vs-NP",
    "Gm-torsion",
    "obstruction",
    "millennium-problem",
    "substrate-parameter",
    "computational-horizon",
  ],
  uses: ["conj:p-vs-np-boundary"],
});
