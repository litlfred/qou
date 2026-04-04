import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:qou-p-neq-np",
  title:
    "$\\mathrm{P} \\neq \\mathrm{NP}$ at non-torsion $q \\in \\mathbb{G}_m$",
  tags: [
    "P-vs-NP",
    "Gm-torsion",
    "obstruction",
    "millennium-problem",
    "substrate-parameter",
    "computational-horizon",
  ],
  uses: [
    "def:skein-resolution-obstruction",
    "thm:qou-obstruction-reduction",
    "rem:kummer-filtration-obstruction",
    "rem:substrate-gm-torsion",
    "conj:p-vs-np-boundary",
  ],
});
