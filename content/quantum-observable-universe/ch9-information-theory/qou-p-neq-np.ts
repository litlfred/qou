import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:qou-p-neq-np",
  title:
    "$\\mathrm{P} \\neq \\mathrm{NP}$ at non-torsion $q \\in \\mathbb{G}_m$",
  tags: [
    "P-vs-NP",
    "Gm-torsion",
    "obstruction",
    "projective-line",
    "root-of-unity",
    "substrate-parameter",
    "computational-horizon",
    "field-dependence",
  ],
  uses: [
    "def:skein-resolution-obstruction",
    "prop:field-dependent-complexity",
    "conj:p-vs-np-boundary",
    "def:computational-horizon",
    "conj:quantum-computational-universality",
    "def:descent-involution",
    "prop:descent-eigenspaces",
    "rem:complex-substrate-interpretation",
    "rem:base-field-independence",
    "def:substrate-parameter",
    "prop:ns-obstruction-tower",
  ],
});
