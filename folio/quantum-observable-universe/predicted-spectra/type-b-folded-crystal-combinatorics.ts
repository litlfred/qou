import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:type-b-folded-crystal-combinatorics",
  title:
    "Type-B folded crystal combinatorics: $c(\\lambda) + c(\\lambda^T) = 0$ summand-by-summand",
  uses: [
    "prop:crystal-basis-resolves-mass-tower-open-problems",
    "prop:chirality-writhe-ribbon-derivation",
  ],
  cites: ["kashiwara1991", "brundankleshchev2009", "lecouvey2007"],
  tags: [
    "type-b-folding",
    "kashiwara-crystal",
    "partition-content",
    "transpose-involution",
    "chirality-factor",
    "combinatorics",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.TypeBCrystal.PartitionWithCells.content_sum_plus_transpose_content_sum_eq_zero",
    validation: "not_checked",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## Lean structure\n\nSee [Table](#tbl:type-b-folded-crystal-combinatorics-table-data)." },
    { kind: "note", body: "The formalisation lives in the library tree, not in a co-located sibling: [`lean/QOU/Archimedean/TypeBFoldedCrystalCombinatorics.lean`](../lean/QOU/Archimedean/TypeBFoldedCrystalCombinatorics.lean), namespace `QOU.Archimedean.TypeBCrystal`. Contents are **integers** ($\\mathrm{col} - r$ for naturals), so per AGENTS.md §7c no archimedean specialisation over $\\mathbb{R}$ is involved or warranted." },
    {
      kind: "status",
      body:
        "**theorem (unconditional).** This is the combinatorial primitive underlying the Type-B folding shortcut from AGENTS.md §7b: *'Fold the $\\mathfrak{sl}_n$ Cartan datum into a Type B datum; the resulting Kashiwara graph is a symmetric crystal, and its GS normal forms are bar-involution ($q \\mapsto q^{-1}$) invariant by construction.'* The proof is direct integer arithmetic and is sorry-free: `#print axioms` on `PartitionWithCells.content_sum_plus_transpose_content_sum_eq_zero` and on `self_transpose_content_sum_zero` reports only `propext`, `Classical.choice`, `Quot.sound` \u2014 no `sorryAx`.",
    },
  ],
});
