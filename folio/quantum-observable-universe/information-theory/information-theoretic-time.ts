import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Julia set of Reeb flow](#rem:julia-set-reeb))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([bundle initial conditions](#def:bundle-initial-conditions))" },
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
