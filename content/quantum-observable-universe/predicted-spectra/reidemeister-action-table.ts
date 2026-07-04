import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:reidemeister-action-table",
  title:
    "Reidemeister moves on the categorical action: complete accounting",
  tags: [
    "reidemeister",
    "hecke-algebra",
    "lagrangian",
    "action",
    "writhe",
    "volume",
    "energy",
    "mass",
    "invariant",
  ],
  lean: { ref: "qou:QOU.Archimedean.reidemeister_action_table",
    validation: "not_checked",
  },
  uses: ["thm:markov-trace-factorization"],
});
