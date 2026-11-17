---
# qou-yax5
title: y_lambda / H4 block projectors are pinned to R for no reason — lift to LinearOrderedField, then generic Field + poincare-nonzero
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T17:21:11Z
updated_at: 2026-11-17T06:22:00Z
parent: qou-rtxm
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

## 2026-08-09 — step 1 done, and three corrections to this bean

Generalised in `QOU/Mathlib/HeckeAlgebra.lean`, tree green (5381 jobs, exit 0,
45 sorries — unchanged):

| declaration | was | now |
|---|---|---|
| `H3.poincare`, `_pos`, `_ne_zero` | `ℝ` | generic ordered field |
| `H3.blockSym3`, `H3.blockAlt3` | `ℝ` | ” |
| `H4.poincare`, `_pos`, `_ne_zero` | `ℝ` | ” |
| `H4.blockSym4`, `H4.blockAlt4` | `ℝ` | ” |

Backward compatible: every existing `ℝ` call site still elaborates, which the
full build confirms. The `nlinarith` positivity proofs carried over verbatim —
they only use squares-non-negative and positive coefficients.

Evidence is in the file rather than asserted here: `example`s proving
`H3.poincare (2 : ℚ) ≠ 0`, `H4.poincare (2 : ℚ) ≠ 0`,
`(0 : ℚ) < H4.poincare (-3/7 : ℚ)`, the `ℝ` counterpart still working, and
`H4.blockSym4` over both `ℚ` and `ℝ`.

### Correction 1 — `LinearOrderedField` does not exist any more

This bean recommended `[LinearOrderedField K]`. In Mathlib rev `f897ebcf` that is
**deprecated and no longer a class**, so `[LinearOrderedField K]` is an invalid
binder annotation. The spelling is

```lean
{K : Type u} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
```

### Correction 2 — the `ℝ` pinning is wider than this bean said

Not only the H4 blocks. Still on `ℝ` in the same file, for a follow-up:
`H2.markovTrace`, `H2.blockSym`, `H2.blockAlt`, `blockSum_eq_one`,
`H3.markovTrace` and its two value lemmas, `H3.sigma1_sq_eq`, `H3.sigma2_sq_eq`,
`H3.braid_relation`, `H3.blockMixed21`, `H3.blockSum_first_component`,
`H4.blockMixed22`, `H4.blockStd31`, `H4.blockStd211`,
`H4.sum_q_sq_length_eq_poincare`, `H4.markovTraceOnBasis`.

### Correction 3 — do not state block-projector facts at a fixed index

A first attempt at the `ℚ` evidence asserted `H4.blockSym4 q 0 = 1 / P(q)`. That
is **not provable**, and rightly so: it silently assumes the identity permutation
sits at basis index `0`, whereas `blockSym4`'s own docstring records that
per-index values depend on the noncomputable basis enumeration. State the
defining identity instead. The file now carries that reasoning next to the
examples.

Step 2 — fully generic `[Field K]` plus `hP : poincare q ≠ 0` — is still open and
still worth doing where the genericity is load-bearing: `P` genuinely vanishes at
roots of unity, so the hypothesis is real, and it is the shape `wedderburn₃/₄`
already carry.

## 2026-11-17 — Generic-Ring H_4(q) Poincaré Factorisation & Block Projectors (`QOU.Foundations.CalibrationJMGibbsBarPoincare`, PR #8223)
- Formalized `qInt2`, `qInt3`, `qInt4`, `h4PoincareFactored`, `h4_poincare_invertible_of_qint_invertible`, and `h4_normalized_projector_idempotent` in `folio/quantum-observable-universe/lean/QOU/Foundations/CalibrationJMGibbsBarPoincare.lean` (pure Lean 4 core, generic `CommRingOps R` per §7c, `0` `sorry`, `0` warnings, `0` vacuity audit hits; wired into `QOU.lean`).
- Commit: `71263060fde5e0d5c09fecd66cf05ada5b6cd208` | PR: `https://github.com/litlfred/qou/pull/8223`
- Kept at `status: in-progress` per merge-manager protocol.
