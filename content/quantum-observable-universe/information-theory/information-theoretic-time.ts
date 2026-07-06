import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:information-theoretic-time",
  title: "Information-Theoretic Time",
  tags: [
    "information-theory",
    "planck-time",
    "discrete-time",
    "statistical-mechanics",
    "reeb-flow",
    "julia-set",
  ],
  lean: { ref: "qou:QOU.informationTheoreticTime",
    validation: "leanok",
  },
  uses: [
    "prop:reeb-operations-per-planck",
    "prop:ordering-jet-compatibility",
  ],
});
