import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "def:borromean-baryon",
  title: "Borromean baryon",
  tags: ["borromean", "baryon", "unknot", "color-confinement", "link"],
  lean: { ref: "qou:QOU.Braiding.BorromeanBaryon",
    validation: "not_checked",
  },
  uses: ["def:hadron"],
});
