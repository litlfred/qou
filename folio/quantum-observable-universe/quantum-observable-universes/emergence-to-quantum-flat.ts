import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:emergence-to-quantum-flat",
  lean: { ref: "qou:QOU.emergence_to_quantum_flat",
    validation: "not_checked",
  },
  title: "From Tannakian emergence to 2-group quantum flatness",
  tags: ["tannaka-krein", "2-group", "instanton"],
  uses: ["rem:self-dual-2group", "def:quantum-flatness"],
  cites: ["baez-schreiber2007"],
  proofs: ["prf:emergence-to-quantum-flat"],
});
