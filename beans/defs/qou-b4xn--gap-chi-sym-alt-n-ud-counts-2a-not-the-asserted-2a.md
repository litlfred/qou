---
# qou-b4xn
title: 'GAP: chi_sym_alt n_ud counts 2A, not the asserted 2A+1, on all four atoms'
status: completed
type: task
priority: normal
created_at: 2026-08-26T15:54:34Z
updated_at: 2026-08-26T17:02:17Z
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


## Closed 2026-08-26 (PR #5833, commit `6dd79a2a9`)

The "off by one" is real, and it is also this producer's 5.11e-9 residual —
three things turned out to be one thing.

### The count

Measured directly, `atom_braid_word_3A(2,2)` has 47 letters:

| letter | `d` | count (A=4) | braid gen? | colour? |
|---|---|---|---|---|
| σ | `0` | 23 | yes | — |
| σ⁻¹ | `−h` | 15 | yes | — |
| ud pair | `−h/2` | **8** = 2A | no | no |
| p-n interface | `−h(½ − δ/4)` | **1** | no | **yes**, δ ≈ 0.001376 |

So `2A` letters are `ud` and `2A+1` are **averaged**. The assertion was pairing
an averaged count against a `ud` name. Both numbers were right; the pairing was
not. Split into `n_ud == 2A` and `n_averaged == 2A+1`.

`classify_factor` had been dropping the p-n letter into its
`other(c=..., d=...)` branch, where `count_factor_types` filed it under a key
nothing asserted on. It now has its own class, `pn_color`.

### I got the arithmetic wrong first

I read the docstring's "two per nucleon plus one per interface" as
`2A + (A−1) = 3A−1` and went looking for a docstring bug. **There is none.**
Only the p-n interface is averaged — pp is a plain σ, nn a plain σ⁻¹, already
isospin-distinct by chirality — so there is exactly one averaged interface
regardless of A, and `2A+1` is right. `3A−1` equals `2A+1` only at A=2, which is
what made the misreading survive the deuteron.

### The same mismatch is the residual

The closed form `−(1 + H_A²/4)^(2A+1)` folds the colour-weighted p-n letter in
as if it were a `2A+1`-th `ud` letter. Carrying it as itself:

| | rel error |
|---|---|
| `f_ud^(2A+1)` (colour-blind, as stated) | 5.1139e-09 |
| `f_ud^(2A) · f_pn` (p-n carried) | **1.2e-14** |

1.2e-14 is the float64 floor of the inputs (`qou-oppb` tail), not a residual.

### Why it was 5e-9 and not 7e-4 — the part worth keeping

`f(d) = d² − 1 + d·h`, so `f'(d) = 2d + h`, which **vanishes identically at
`d = −h/2`**. The `ud` letter sits at a *stationary point* of the per-factor
product, so the colour weighting costs **second** order:
`Δd/d = 6.88e-4` → `Δf = (Δd)² = 5.16984e-9`.

Predicted 5.11397e-9 from that alone, against 5.11395e-9 measured. Six
significant figures.

That stationary point is why float64 hid it. The old `tolerance=1e-3` was
justified by a comment about "~0.05% numerical noise" in the seminormal matrices
— there is none — and a real, identifiable, second-order colour term sat
200,000× inside it. It took this morning's mpmath conversion to make it visible
and this to identify it.

### Kept, not replaced

The colour-blind form is still emitted and still asserted. It is the form stated
in the corpus and formalised in the Lean sibling, and it is exactly true for a
colour-blind word (`pn_convention="strict_averaged"`) — it is simply not the word
this producer builds. Both predictions ship; the exact one is asserted at 1e-12.

16 assertions, all passed (was 8 with 4 failures). 0 raw float64 fields.

### Follow-on

`qou-cdqu` — the Lean sibling's `FactorType` has three constructors and the word
has four letter types, so `chiPairProduct_eq` is sorry-free and true about a
colour-blind alphabet, with nothing in the file saying so. Its `nUd` is the `2A`
count, which agrees with this fix.
