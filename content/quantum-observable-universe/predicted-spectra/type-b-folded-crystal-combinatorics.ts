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
    {
      kind: "status",
      body:
        "**theorem (unconditional).** This is the combinatorial primitive underlying the Type-B folding shortcut from AGENTS.md §7b: *'Fold the $\\mathfrak{sl}_n$ Cartan datum into a Type B datum; the resulting Kashiwara graph is a symmetric crystal, and its GS normal forms are bar-involution ($q \\mapsto q^{-1}$) invariant by construction.'* The proof is direct integer arithmetic and is sorry-free in the Lean file [`type-b-folded-crystal-combinatorics.lean`](type-b-folded-crystal-combinatorics.lean).",
    },
  ],
});
