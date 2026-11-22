import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([local substrate $q$](#prop:local-substrate-q))" },
  ],
  label: "prop:hadron-q-self-correction",
  title:
    "Effective substrate parameter: hadron self-deformation of $q$",
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
