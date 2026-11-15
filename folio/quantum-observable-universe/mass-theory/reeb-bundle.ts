import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:reeb-bundle",
  lean: { ref: "qou:QOU.ReebBundle", validation: "not_checked" },
  title: "Reeb bundle over the exceptional divisor",
  tags: [
    "reeb-bundle", "exceptional-divisor", "hopf-fibration",
    "blow-up",
  ],
  uses: [
    "def:exceptional-divisor",
    "ex:q-reeb-vector-field",
  ],
});
