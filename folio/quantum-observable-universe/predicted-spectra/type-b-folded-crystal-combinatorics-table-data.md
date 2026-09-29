| Definition / theorem | Content |
|---|---|
| `Cell` | structure `(row col : ℕ)` |
| `Cell.content` | `(col : ℤ) - (row : ℤ)` |
| `Cell.transpose` | swap `row ↔ col` |
| `Cell.transpose_transpose` | involutive |
| `Cell.content_plus_transpose_content_eq_zero` | summand-by-summand cancellation, by `ring` |
| `PartitionWithCells` | structure `(cells : List Cell)` |
| `PartitionWithCells.content_sum` | `Σ c(x)` over cells |
| `PartitionWithCells.transpose` | map `Cell.transpose` over the list |
| `PartitionWithCells.content_sum_plus_transpose_content_sum_eq_zero` | partition-level cancellation, proved by induction + `linarith` |
| `PartitionWithCells.self_transpose_content_sum_zero` | self-dual partitions have content sum zero |
