import { table } from "../../schema/builders";
export default table({ label: "tbl:braid-group-n-strand-table3-data", title: "Table 3 from rem:braid-group-n-strand", uses: ["rem:braid-group-n-strand"], tags: ["extracted-table"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): | Bridge | Direction | Lean | Closure |\n|---|---|---|---|\n| `closureN @ n=2` $\\leftrightarrow$ `closure2 ∘ writhe` | n=2 specialisation | `closureN_eq_closure2` | `rfl` |\n| `BraidWord 3` $\\to$ `TypedBraidWord3` | n=3 conversion | `BraidWord.toBraid3` (`def`) | mapped via `BraidCrossing.toTypedB3` (`sigma`/`sigma_inv` subset) |\n| `BraidWord.toBraid3_length` | length preservation | `@[simp]` lemma | `List.length_map` |" },
  ],
});
