---
# qou-6e88
title: 'cauchyMul_order: the statement may need strengthening before it is provable'
status: todo
type: task
created_at: 2026-08-08T07:04:15Z
updated_at: 2026-08-08T07:04:15Z
---

`QOU/Mathlib/QGevreyOrder.lean:261`.

Unlike the other sorries this is not purely a missing proof. Per the
file's own note, the `≥` direction needs a **non-cancellation hypothesis
on the leading coefficients** — in a general normed field the
boundary/saddle term may genuinely cancel, which would make the theorem
as stated FALSE.

So the first task is not to prove it but to decide the right statement:
either add the hypothesis, or restrict the field. Worth settling before
anyone spends effort on a proof.

The `≤` direction is reportedly close: it reduces to two sorry-free
lemmas already in the file (`cauchyMul_norm_le_sum`,
`exponent_le_envelope`) plus an ε-δ assembly. That half may be the
tractable piece.
