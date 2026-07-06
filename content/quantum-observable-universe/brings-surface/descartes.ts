import { theorem } from "../../schema/builders";

export default theorem({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "thm:descartes",
  lean: { ref: "qou:QOU.Archimedean.descartes",
    validation: "not_checked",
  },
  title: "Descartes theorem",
  tags: ["archimedean-universe", "terminal-object", "brings-surface"],
  uses: [
    "prop:brings-is-qou",
    "prop:genus-maximal-descent",
  ],
  proofs: ["prf:descartes"],
});
