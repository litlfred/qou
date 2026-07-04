import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:shell-closure-normal-form",
  title:
    "Shell closure as symmetric Poincaré distribution in the Hecke normal form",
  tags: [
    "shell-closure",
    "normal-form",
    "hecke-algebra",
    "poincare-polynomial",
    "magic-numbers",
    "bruhat-order",
    "nuclear-structure",
    "groebner-basis",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.sequential_build_always_normal_form",
    validation: "not_checked",
  },
  uses: ["prop:skein-polynomial-transfer-matrix"],
});
