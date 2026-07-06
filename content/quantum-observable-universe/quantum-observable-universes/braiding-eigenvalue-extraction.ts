import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:braiding-eigenvalue-extraction",
  title:
    "Extraction of $q$ from the braiding eigenvalues",
  cites: ["kassel1995", "woronowicz1988"],
  tags: [
    "braiding",
    "eigenvalue",
    "substrate-parameter",
    "hecke-algebra",
    "categorical",
  ],
  lean: { ref: "qou:QOU.braiding_eigenvalue_extraction",
    validation: "not_checked",
  },
  uses: ["prop:tannaka-krein-reconstruction"],
});
