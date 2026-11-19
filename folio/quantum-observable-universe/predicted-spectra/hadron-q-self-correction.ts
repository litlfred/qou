import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:hadron-q-self-correction",
  title:
    "Effective aether parameter: hadron self-deformation of $q$",
  tags: [
    "substrate-parameter",
    "self-energy",
    "effective-q",
    "hadron",
    "linking-number",
    "back-reaction",
  ],
  lean: { ref: "qou:QOU.Archimedean.hadron_q_self_correction",
    validation: "not_checked",
  },
  uses: ["prop:hadron-half-life"],
});
