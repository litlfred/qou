---
# qou-yax5
title: y_lambda / H4 block projectors are pinned to R for no reason — lift to LinearOrderedField, then generic Field + poincare-nonzero
status: todo
type: task
created_at: 2026-08-09T17:21:11Z
updated_at: 2026-08-09T17:21:11Z
---


The `H₄` Wedderburn projectors and the Markov-weight (`y_λ`) machinery in
`QOU/Mathlib/HeckeAlgebra.lean` are declared over `ℝ`:

```lean
noncomputable def H4.poincare (q : ℝ) : ℝ :=
  1 + 3*q^2 + 5*q^4 + 6*q^6 + 5*q^8 + 3*q^10 + q^12
theorem H4.poincare_pos (q : ℝ) : 0 < H4.poincare q := by
  unfold H4.poincare; nlinarith [...]
noncomputable def H4.blockSym4 (q : ℝ) : H4Carrier ℝ := fun i => q ^ (lengthFn 4 i) / H4.poincare q
noncomputable def H4.blockAlt4 (q : ℝ) : H4Carrier ℝ := ...
-- likewise blockMixed22, blockStd31, blockStd211, H4.markovTraceOnBasis
```

This is against the repo's own §7c convention, which the neighbouring modules
state explicitly and follow:

* `HeckeH4AlgebraLaws`: "Base ring (§7c): generic `[CommRing R]` throughout — no
  `ℝ`, no ordering, no archimedean construct."
* `HeckeH4StabilizationRung`: "generic `[CommRing R]` — no `ℝ`."
* `HeckeH4Wedderburn`: "generic `[Field K]`; no archimedean construct."

So the algebra, its presentation, its associativity and its Wedderburn
isomorphism are all generic, and only the block projectors and weights are pinned
to `ℝ`.

## What is actually needed

Only that the Poincaré polynomial `P₄(q)` be **invertible**. Nothing about `ℝ`,
and nothing archimedean beyond the *proof* of that one fact.

**Step 1 — `[LinearOrderedField K]`.** Mechanical: replace `ℝ` by `K`. The
`nlinarith` proof of `poincare_pos` goes through verbatim, because it only uses
that squares are non-negative and the coefficients positive. This alone buys
**`ℚ`**, which is what is wanted for exact `y_λ` arithmetic, and keeps `ℝ`.

**Step 2 — generic `[Field K]` + `hP : H4.poincare q ≠ 0`.** The honest general
form: `P₄` genuinely vanishes at roots of unity, so non-vanishing is a real
hypothesis, not an artefact. This is exactly the shape `HeckeH4Wedderburn`
already uses — `wedderburn₄` carries `hq`, `h2`, `h3`, `h4`, the Wenzl genericity
conditions — so the two would compose without an impedance mismatch. Over `ℚ(q)`,
the natural home for `y_λ`, `P₄` is a non-zero polynomial and hence invertible in
the fraction field.

Do step 1 first (it is a rename and immediately unblocks `ℚ`), then step 2 where
the genericity is load-bearing. Keep `ℝ`-specific corollaries where a numeric
value is genuinely wanted, derived from the generic form rather than replacing it.

## Why it matters now

`QOU/Hecke/MarkovTraceOnH3A.lean` records the route to the missing `n = 4` Markov
trace: `BilinearTrace.gram_symm_of_rep_decomp` needs `trM4` to decompose as a
weighted sum of representation traces, and `wedderburn₄` supplies the
representations. The blocker is that the weights live on `H4Carrier` over `ℝ`
while `trM4` and `H4A` are over a generic `[CommRing R]` / `[Field K]` — a base-ring
mismatch, not a mathematical one. Lifting the weights removes it.

(Note qou-x64l offers a cheaper route to that same trace — transporting the
proved ASCII cyclicity along the basis permutation. This bean is worth doing
regardless: the `ℝ` pin is a §7c violation on its own terms, and every downstream
`y_λ` result inherits it.)
