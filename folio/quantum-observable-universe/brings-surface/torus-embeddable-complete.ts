import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:torus-embeddable-complete",
  title:
    "Completeness of torus knots embeddable in the Bring's surface",
  tags: [
    "torus-knot",
    "embeddability",
    "genus",
    "completeness",
    "seifert-genus",
    "brings-surface",
  ],
  lean: { ref: "qou:QOU.Archimedean.torus_embeddable_complete",
    validation: "not_checked",
  },
  uses: ["thm:embeddability-closure"],
  examples: [
    "rem:archimedean-chirality",
    "rem:light-cone-affine",
    "rem:chirality-trefoil",
    "rem:linking-relations-table",
    "rem:chirality-trefoil-electron-positron",
    "rem:unmapped-torus-knots",
    "rem:force-knot-identification",
    "rem:diophantine-valley",
    "ex:archimedean-yekutieli",
  ],
});
