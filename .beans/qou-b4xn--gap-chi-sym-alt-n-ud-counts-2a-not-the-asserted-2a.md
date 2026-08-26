---
# qou-b4xn
title: 'GAP: chi_sym_alt n_ud counts 2A, not the asserted 2A+1, on all four atoms'
status: todo
type: task
created_at: 2026-08-26T15:54:34Z
updated_at: 2026-08-26T15:54:34Z
---

`computations/chi_sym_alt_closed_form.py` asserts, for every atom, that the
u-d factor count of `atom_braid_word_3A(A)` equals `2A + 1`, glossed in the
producer's own `closed_form` data block as "2 per nucleon + 1 p->n transition".

Measured (integer counts, `tolerance=0`, untouched by the 2026-08-26 mpmath
conversion -- this is not a precision finding):

| atom | A  | expected 2A+1 | observed n_ud |
|------|----|---------------|---------------|
| D    | 2  | 5             | 4             |
| T    | 3  | 7             | 6             |
| 3He  | 3  | 7             | 6             |
| 4He  | 4  | 9             | 8             |

`observed = 2A` exactly, in all four. The "+1 p->n transition" factor is not
present in the word the builder emits. So one of these is wrong and it is not
yet established which:

- the word builder omits a factor it should emit, or
- the `2A + 1` claim (and its "+1 p->n transition" gloss) is wrong and the
  count is `2A`.

The second reading has a check available: the closed form the same producer
verifies is `-(1 + H_A^2/4)^(2A+1)`, and it PASSES to 5.1e-9 with the exponent
`2A+1`. If the true factor count were `2A`, the product of `2A` factors each
equal to `-(1 + H_A^2/4)` would be off by one whole factor -- roughly 5.5%,
not 5e-9. So the EXPONENT `2A+1` is corroborated by the numerics and the
discrepancy is in `classify_factor` / `atom_braid_word_3A` disagreeing about
which factors count as "u-d", not in the closed form.

That makes this most likely a classification bug in the assertion's counting
path rather than a wrong claim -- but it has NOT been bisected, and the above
is an inference from the passing product assertion, not a measurement of the
word.

Next honest step: dump the factor list from `atom_braid_word_3A(2)` and read
off which of the 4 (or 5) factors `classify_factor` labels, and what the fifth
is if the word has five.

Surfaced while draining this producer's 36 raw float64 fields (PR #5833,
commit 544c49d8a). Not fixed there: out of scope (combinatorics, not
precision) and the fix direction is not yet established.
