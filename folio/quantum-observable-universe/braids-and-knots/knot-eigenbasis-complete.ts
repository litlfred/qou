import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:knot-eigenbasis-complete",
  lean: { ref: "qou:QOU.Braiding.knot_eigenbasis_complete",
    validation: "not_checked",
  },
  title: "Completeness of the knot-type eigenbasis",
  tags: ["braid-group", "hecke-algebra", "knot-invariant", "schur-weyl"],
  uses: ["prop:braid-action-tensor"],
  proofs: ["prf:knot-eigenbasis-complete"],
});
