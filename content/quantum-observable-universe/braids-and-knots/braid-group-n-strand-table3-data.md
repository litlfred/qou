| Bridge | Direction | Lean | Closure |
|---|---|---|---|
| `closureN @ n=2` $\leftrightarrow$ `closure2 ∘ writhe` | n=2 specialisation | `closureN_eq_closure2` | `rfl` |
| `BraidWord 3` $\to$ `TypedBraidWord3` | n=3 conversion | `BraidWord.toBraid3` (`def`) | mapped via `BraidCrossing.toTypedB3` (`sigma`/`sigma_inv` subset) |
| `BraidWord.toBraid3_length` | length preservation | `@[simp]` lemma | `List.length_map` |
