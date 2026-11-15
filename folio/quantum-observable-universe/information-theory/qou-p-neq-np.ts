import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:qou-p-neq-np",
  title:
    "$\\mathrm{P} \\neq \\mathrm{NP}$ at non-torsion $q \\in \\mathbb{G}_m$",
  lean: { ref: "qou:QOU.Information.QouPNeqNp", validation: "stub" },
  tags: [
    "tier:famous",
    "P-vs-NP",
    "Gm-torsion",
    "obstruction",
    "millennium-problem",
    "substrate-parameter",
    "computational-horizon",
  ],
  uses: [
    "conj:p-vs-np-boundary",
    "ex:chi-minus-six-derivation",
    "prf:qou-obstruction-reduction",
  ],
  cites: ["jaeger1990", "aharonov2009", "freedman2003", "cook1971"],
  authorNotes: [
    {
      kind: "refined-framing",
      body: "Earlier drafts stated the G_m-torsion dichotomy backwards.",
    },
  ],
});
