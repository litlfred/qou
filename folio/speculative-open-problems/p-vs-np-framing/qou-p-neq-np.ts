import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:qou-p-neq-np",
  title: "Speculative obstruction-residue formulation of $\\mathrm{P} \\neq \\mathrm{NP}$ at non-torsion $q$",
  lean: { ref: "qou:QOU.InformationTheory.QouPNeqNp", validation: "stub" },
  tags: [
    "tier:famous",
    "P-vs-NP",
    "Gm-torsion",
    "obstruction",
    "millennium-problem",
    "computational-horizon",
  ],
  uses: [
    "conj:p-vs-np-boundary",
    "quantum-observable-universe:conj:wigner-axiom",
    "quantum-observable-universe:prop:jvw-tractable-orders",
    "quantum-observable-universe:thm:qou-obstruction-reduction",
  ],
  cites: ["jaeger1990", "aharonov2009", "freedman2003", "cook1971"],
});
