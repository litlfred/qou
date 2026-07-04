import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:archimedean-condition",
  lean: { ref: "qou:QOU.ArchimedeanCondition", validation: "not_checked" },
  title: "Descartes condition",
  tags: ["archimedean-universe", "euler-characteristic"],
  uses: ["thm:qu-to-qou"],
});
