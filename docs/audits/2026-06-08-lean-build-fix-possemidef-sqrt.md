# 2026-06-08 — QOU Lean red: Mathlib PosSemidef.sqrt API drift

## Summary

The `qou` Lean package (lib `QOU`) fails to build on current `main`.
Two files are red, both byte-identical to their base — the cause is
upstream **Mathlib API drift**, not repo content:

- `content/quantum-observable-universe/lean/QOU/MathlibExt/PosSemidefTraceZero.lean`
- `content/quantum-observable-universe/lean/QOU/HeckeAlgebra/Formal.lean`
- `content/quantum-observable-universe/lean/QOU/HeckeAlgebra/Realification.lean`
  (third file with the **same** Laurent-map drift; not listed in the
  original report but in the QOU build cone via `QOU/HeckeAlgebra.lean`,
  so it is red too — fixed inline here per AGENTS.md "ride related
  fixes on the active PR")

## Two distinct Mathlib drifts

### Drift A — PSD square root moved to the continuous functional calculus

Pinned Mathlib (`f897ebcf72`, toolchain `v4.24.0`) `@[deprecated]`'d the
old `Matrix.PosSemidef.sqrt` family in favour of the C⋆-algebra `CFC.sqrt`
API (`Mathlib/Analysis/Matrix/Order.lean`, `since := "2025-09-22"`).
Because `Matrix.PosSemidef A` reduces to an `And`, the dot-notation
`hA.sqrt` no longer finds the deprecated `PosSemidef.sqrt` — it resolves
to a nonexistent `And.sqrt`. Fix maps the dot-notation to the explicit
`CFC.*` lemmas:

| Old (in QOU) | New (current Mathlib v4.24.0) |
|---|---|
| `hA.sqrt` (`PosSemidef.sqrt`) | `CFC.sqrt A` |
| `hA.sq_sqrt : Asqrt * Asqrt = A` | `CFC.sqrt_mul_sqrt_self A hA.nonneg` |
| `hA.posSemidef_sqrt : Asqrt.PosSemidef` | `(CFC.sqrt_nonneg A).posSemidef` |

`CFC.sqrt_mul_sqrt_self`/`CFC.sqrt_nonneg` take a `0 ≤ A` autoparam,
supplied explicitly via `PosSemidef.nonneg`. Requires the new import
`import Mathlib.Analysis.Matrix.Order` (matrix CStar instances + `CFC.sqrt`).

### Drift B — `LaurentPolynomial.mapRingHom` removed

`LaurentPolynomial.mapRingHom` / `LaurentPolynomial.mapRingHom_T` no
longer exist in Mathlib (the coefficient-map ring hom lives on the
`AddMonoidAlgebra` ancestor). `LaurentPolynomial R = AddMonoidAlgebra R ℤ`,
so the replacement is `AddMonoidAlgebra.mapRangeRingHom`:

| Old (in QOU) | New (current Mathlib v4.24.0) |
|---|---|
| `LaurentPolynomial.mapRingHom f` | `AddMonoidAlgebra.mapRangeRingHom f` |
| `rw [LaurentPolynomial.mapRingHom_T]` | `ext`/`simp` on `mapRange_single` |

## Status

Fixes applied; verifying green against a from-source rebuild of the
matrix-CFC Mathlib cone (toolchain restored by hand from the GitHub
release asset; `release.lean-lang.org` is 403 in this sandbox).
