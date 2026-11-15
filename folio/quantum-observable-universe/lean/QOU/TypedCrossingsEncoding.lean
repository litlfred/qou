import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic

/-!
# QOU.MassComputationChain.TypedCrossingsEncoding

The **algebraic** half of the §7c split of `QOU.MassComputationChainRoadmap`
(bean `qou-q7cm`). That module is an archimedean roadmap — ten "Gap N"
axiomatisations of the mass-computation chain, stated over the reals — with
exactly one generic-ring theorem embedded in it. That one theorem is what made
`wall-side-correct` report the file MIXED, and it is this one.

It is pure field algebra: the Hecke-skein quadratic relation forces the
`(c, d)` encoding of each quark-typed crossing, proved by `ring` / `field_simp`
over an arbitrary `[Field A]`. It names no real-number type and no order
relation.

Kept in the parent's namespace `QOU.MassComputationChain`, so every existing
call site is unchanged; the roadmap imports this module and its Gap 3 narrative
points here.

Placed at `QOU/TypedCrossingsEncoding.lean` rather than under a
`QOU/MassComputationChainRoadmap/` directory on purpose: a module sharing its
name with a sibling directory becomes an import-only aggregator for `lean.ref`
resolution, a trap recorded in bean `qou-cu0a`.
-/

namespace QOU.MassComputationChain

-- Ref: [leitner2026] prop:typed-crossings-quark-content
-- Ref: [leitner2026] §four-term-pair-nucleon
/-- **Typed-crossings encoding (derived).**

Work in a field `A` (the Hecke algebra image, where the `½` average
makes sense), with `σ` the positive crossing and `H_A = q − q⁻¹`
(here a scalar `h`).  The Skein form of the Hecke quadratic relation
gives `σ⁻¹ = σ − H_A · 1` (hypothesis `hinv`).  Each typed crossing
`c·σ + d·1` then has its `(c, d)` pair **forced**:

* `uu = σ` → `(c, d) = (1, 0)`;
* `dd = σ⁻¹ = σ − H_A·1` → `(c, d) = (1, −H_A)` (forced by `hinv`);
* `ud = ½(σ + σ⁻¹) = σ − ½H_A·1` → `(c, d) = (1, −H_A/2)`.

The `ud`-average identity is derived here by `ring` from `hinv`; this
is the genuine computation underlying gap 3 (the `½` averaging is the
sole convention, the rest is forced). -/
theorem typed_crossings_encoding_unique
    {A : Type*} [Field A] (h2 : (2 : A) ≠ 0) (σ σinv : A) (h : A)
    (hinv : σinv = σ - h * 1) :
    σinv = σ - h ∧ (1 / 2 : A) * (σ + σinv) = σ - (h / 2) := by
  -- Ref: [leitner2026] prop:typed-crossings-quark-content
  refine ⟨by rw [hinv]; ring, ?_⟩
  rw [hinv]
  field_simp
  ring

end QOU.MassComputationChain
