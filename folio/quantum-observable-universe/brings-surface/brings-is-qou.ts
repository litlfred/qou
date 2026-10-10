import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:brings-is-qou",
  lean: { ref: "qou:QOU.Brings.brings_is_qou",
    validation: "not_checked",
  },
  title: "Bring's surface is a quantum observable universe",
  uses: [
    "def:brings-surface",
    "thm:qu-to-qou",
  ],
  proofs: ["prf:brings-is-qou"],
});
