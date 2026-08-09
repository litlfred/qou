---
# qou-ut3p
title: 'MATHLIB-INFRA: full row rank ⇒ nonzero maximal minor (rectangular) — absent from Mathlib'
status: completed
type: task
priority: high
created_at: 2026-08-08T09:39:42Z
updated_at: 2026-08-08T09:40:09Z
---


**DONE in the same session it was opened** —
`QOU/MathlibExt/RankMinor.lean`, 0 `sorry`, `lake build` green (1711 jobs),
all four declarations axiom-clean (`propext, Classical.choice, Quot.sound`).

## What it is

    exists_selector_det_ne_zero (M : Matrix (Fin r) (Fin n) K)
      (hM : LinearIndependent K M.row) :
      ∃ f : Selector r n, (minorA M f).det ≠ 0

over any field. Linearly independent rows force **some** strictly monotone
`r`-column selection to have invertible square submatrix.

## Why it exists — it is Cauchy–Binet's missing hypothesis

`qou-8yph` delivered `CauchyBinet.det_gram_map_ne_zero`, which takes *"one
`r × r` minor of the integer matrix is nonzero"* and returns *"`det (N Nᵀ) ≠ 0`
over every characteristic-zero field"*. But a caller never has a minor in
hand — it has **linear independence**. This file is the bridge, and the
composite at the bottom is the statement a caller can actually discharge:

    det_gram_map_ne_zero_of_linearIndependent
      (M : Matrix (Fin r) (Fin n) ℤ)
      (hM : LinearIndependent ℚ (M.map (Int.cast : ℤ → ℚ)).row) :
      ((M.map (Int.cast : ℤ → k)) * (M.map (Int.cast : ℤ → k))ᵀ).det ≠ 0

for any `[Field k] [CharZero k]`. Rank argument over `ℚ`, sum of squares over
`ℤ`, and only the `≠ 0` crosses into `k` — `k` is never ordered.

## Mathlib coverage — checked at the pinned rev, not assumed

- `Matrix.linearIndependent_rows_iff_isUnit` / `_cols_iff_isUnit` — **square
  only** (`{A : Matrix m m K}`).
- `Matrix.rank`, `rank_eq_finrank_span_cols`, `rank_eq_finrank_span_row`,
  `LinearIndependent.rank_matrix` — a rank API, but nothing tying rank to
  minors.
- Minors: the only files under `LinearAlgebra/Matrix/` mentioning them at all
  are `Adjugate.lean` and `PosDef.lean`. There is no rectangular minor API.

So the rank ⇒ nonzero-minor direction is genuinely absent.

## The one idea worth remembering

**Stay in the index world.** The usual textbook argument — "column rank is
`r`, so pick `r` independent columns" — extracts a set of *vectors*, and then
you have to convert it back into a set of column *indices*, which needs a
section of the column map and is where this proof normally bogs down in Lean.

`exists_linearIndepOn_extension` avoids it entirely: it is stated for
`LinearIndepOn K v b` with `b : Set ι`, so what comes back **is already a set
of indices**. Three lines later `Finset.orderEmbOfFin` turns it into the
`StrictMono` selector `Selector r n` wants. No section, no choice function,
no vector-to-index step.

## Friction (each cost a compile)

- `Basis` is `Module.Basis` at this revision. The error is a bare
  `Unknown identifier 'Basis'`, which reads like a missing import; the imports
  were fine.
- `RingHom.map_det` is stated with `f.mapMatrix`, which is `Matrix.map` on the
  nose but not syntactically, so `rw` will not fire against a goal phrased with
  `.map`. Bridge with `have hmm : f.mapMatrix A = A.map ⇑f := rfl` first — same
  workaround as in CauchyBinet, worth knowing it recurs.
- `Set.range (fun x : ↥b => f x)` vs `f '' b`: `← Set.image_eq_range` rewrites;
  `Set.range_restrict` does not (the lambda is not syntactically
  `Set.restrict`).

## What this does NOT do

It does not close `sp01` / `qou-0xyc`. That still needs the Specht-specific
plumbing: the explicit integer coordinate matrix of the standard polytabloids,
and the identification of `bilinM` restricted to `S^μ` with `M Mᵀ`. What is
now available off the shelf is everything downstream of that identification.

Worth recording: `SpechtIrreducible.lean`'s own Stage-2 docstring sketches a
route (ℚ positive-definiteness ⇒ `det G` a nonzero integer) that does **not**
need Cauchy–Binet. Both routes need the same plumbing; the Cauchy–Binet route
additionally avoids needing "the Gram matrix of an independent set under a
positive-definite bilinear form is invertible", which `bilinM` does not get
for free (it is not an `InnerProductSpace`).
