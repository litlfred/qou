import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:gs-quotient-ideals-I8-I9",
  title:
    "Quotient ideals $I_8$ (adjacency correlation) and $I_9$ (closed-shell chain collapse)",
  tags: [
    "groebner-basis",
    "quotient-ideal",
    "normal-form",
    "transfer-matrix",
    "hecke-algebra",
    "nuclear-structure",
  ],
  lean: {
    ref: "qou:QOU.OptimalNF.GSQuotientIdealsI8I9",
    validation: "not_checked",
  },
  uses: ["prop:shell-closure-normal-form"],
});
