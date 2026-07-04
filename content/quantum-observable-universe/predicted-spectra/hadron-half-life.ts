import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:hadron-half-life",
  title:
    "Hadron half-life from the $q$-deformed transition amplitude",
  tags: [
    "half-life",
    "beta-decay",
    "hadron",
    "transition-amplitude",
    "substrate-parameter",
    "valley-of-stability",
  ],
  lean: { ref: "qou:QOU.Archimedean.hadron_half_life",
    validation: "not_checked",
  },
  uses: ["prop:integer-stability"],
});
