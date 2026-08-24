---
# qou-j7ln
title: Hook lengths under addCell — the first brick for the arbitrary-z corner identity
status: in-progress
type: task
priority: normal
created_at: 2026-08-24T13:03:43Z
updated_at: 2026-08-24T13:49:49Z
---

## Landed — PR #5645

`QOU/SchurWeyl/HookLengthAddCell.lean`, sorry-free, axiom-clean, pure ℕ × ℕ combinatorics.

- `rowLen_of_isAddableCell` / `colLen_of_isAddableCell` — an addable cell sits at the end of its
  row and the bottom of its column.
- `hookLength_addCell_self` — the added cell's own hook is `1`.
- `hookLength_addCell_of_mem` — every other cell gains `1` **iff** it shares the new cell's row or
  column, `0` otherwise.

**The statement is cleaner than the arm/leg case split I budgeted for.** For `x ∈ ν` the *order*
conditions come free: sharing `s`'s row forces `x.2 < rowLen ν x.1 = s.2` automatically, and
symmetrically for the column. So the hook grows by `1` on exactly the union of `s`'s row and
column, and those meet only at `s`, which is not in `ν` — one `if`, not two cases.

**Corpus-grepped before writing**: no hook-under-`addCell` or hook-under-`eraseCorner` lemma
existed. The `hookLength` infrastructure that does exist (`HookLengthFormula`, `QHookProduct`,
`WenzlSchurElement`, `YoungDiagramCells`) is about the hook-length *formula* and product
identities, not about how a hook moves under a shape change. `qou-68e1` is adjacent (consolidating
`schurElement`'s product form) but a different item; untouched.

### Next brick, and an honest estimate

The weight ratio itself:

    w_{ν+s} / w_ν = N(s) / [ (q²−1) · ∏_{x ∈ arm(s) ∪ leg(s)} (q^{2(h(x)+1)}−1)/(q^{2h(x)}−1) ]

The numerator half is free (per-cell, diagram-independent). The arm/leg product is the work, and it
has **no counterpart in the two-row case** — there `schurPrincipal_twoRow` telescoped the entire
hook-content product, which is exactly the shortcut arbitrary `z` does not get. I am not putting a
timeline on it. Nothing downstream is blocked: convention D is canonical per the 2026-08-15 ruling
and its identification is proved and merged (`91bf8fcb4`).


## Second brick landed — and a scoping finding that changes what "next" means

`QOU/SchurWeyl/OcneanuWeightAddCell.lean`, sorry-free, generic `[Field R]`:
`ocneanuNumProd_addCell` (the numerator gains exactly one factor — `Finset.prod_insert`, nothing
more) and `ocneanuDenProd_addCell` (the denominator gains `q²−1`, and every old factor shifts by
one step iff its cell shares the new cell's row or column).

Named `…Prod` because the corpus already has `ocneanuNumFactor_eq_zero_of_content_neg_two` and
`ocneanuNumFactor_conventionD`, which are about **one cell's** factor. Grepped before writing this
time, having got that order wrong earlier in the arc.

### The Schur route does not generalise, and that is structural

I had been treating arbitrary `z` as "the same proof, harder". It is not. The convention-D proof
went entirely through the bridge to `schurPrincipal 2 (q²)` — Pieri, the two-row telescoping, the
≥3-row vanishing. **That route is unavailable at generic `z`, and the reason is a type:**

    schurPrincipal (r : ℕ) (Q : R) (μ : YoungDiagram)

`r` is the **number of variables** in the principal specialisation, so it is inherently a positive
integer. And the corpus's own parameter relation (`pow_level_mul_eq_of_markovParameter`) pins

    Q^r · (1 − Q + z) = z,   i.e.   Q^r = z / (1 − Q + z)

so a Wenzl level exists only when that element happens to be an **integer** power of `Q`.
Convention D is the case `Q = q²`, `Q^r = q⁴`, `r = 2` (`wenzlLevel_conventionD`). Generic `z` is
off that lattice: there is no `r`, hence no `schurPrincipal r Q` to bridge to, hence no Pieri and
no telescoping.

**So "finish the arbitrary-`z` corner identity" is not one more brick on this pile.** It needs
either a genuinely new hook-level identity (the arm/leg product does *not* telescope for a general
diagram — hooks along a row are not consecutive), or a different route entirely. I am not going to
guess which; recording the obstruction is worth more than a speculative attempt.

What these two bricks *are* good for regardless: they are convention-independent statements about
how the weight moves under `addCell`, so any future route needs them, and neither depends on `z`.
