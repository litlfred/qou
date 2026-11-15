import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:torus-hopf-stability",
  title:
    "Torus knot composites on Bring's surface are stable hadrons",
  tags: [
    "stability",
    "torus-knot",
    "hadron",
    "euler-characteristic",
    "crossing-energy",
  ],
  lean: { ref: "qou:QOU.Archimedean.torus_hopf_stability",
    validation: "not_checked",
  },
});
