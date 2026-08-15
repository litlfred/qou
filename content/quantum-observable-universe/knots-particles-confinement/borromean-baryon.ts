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
  // The three-strand word realising the baryon costs exactly the three
  // pairwise crossings that prop:pairwise-interaction-decomposition (part 3)
  // shows to be the minimum for a mutually-interacting triple.
  uses: ["def:hadron", "prop:pairwise-interaction-decomposition"],
});
