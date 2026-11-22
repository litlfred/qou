/-
  Core Levi form, re-scoped onto the vorticity plane field (owner decision
  2026-10-13, "Q1 Θ = f·ξ♭").

  Ref: [leitner2026] §Fluid dynamics / Core Levi form, prop:core-levi-form

  ## Setting

  The 3D flow domain `D` (`ℝ³` or `T³`, Euclidean metric) — **not** the state
  bundle `𝒮`, which the chapter also uses as a surface.  On the open set where
  the vorticity `ω = curl u` is non-zero put `ξ = ω/|ω|` and, for a positive
  scalar `f`, `Θ := f·ξ♭`.  Then `ker Θ = ξ^⊥`.

  ## What is proved here (pointwise algebra, generic `CommRing`)

  Vectors are `Fin 3 → R`; `C` stands for the value of `curl ξ` at the point,
  `g` for the value of `∇f`.  The differential-form facts that turn these into
  statements about `Θ` are standard and are stated, not formalised:
  `ξ♭ ∧ dξ♭ = (ξ·curl ξ) vol` (identity D1 of
  `docs/audits/2026-10-12-ns-attack-vectors-unforced.md` §2), and
  `dξ♭(v, w) = (curl ξ)·(v × w)` for the Euclidean metric.

  * `helicity_rescale` — identity D2: with `ω = f ξ` and
    `curl ω = f curl ξ + ∇f × ξ`, `ω·curl ω = f² (ξ·curl ξ)`.
  * `contact_iff_rescale` — over a domain, for `f ≠ 0`, `f²·s ≠ 0 ↔ s ≠ 0`:
    the contact criterion `ξ·curl ξ ≠ 0` does not depend on `f`, and coincides
    with `ω·curl ω ≠ 0`.
  * `levi_restriction_rank_one` / `core_levi_form` — on `ξ^⊥` (unit `ξ`), the
    2-form `(v, w) ↦ C·(v × w)` equals `(ξ·C)·(ξ·(v × w))`: the restriction of
    `dΘ` to `ker Θ` is the **single scalar** `f·(ξ·curl ξ)` times the area form
    `ξ·(v × w)` of the plane.  There is no eigenvalue pair.

  ## What was removed (2026-10-13), and why

  This file used to carry `CoreLeviData` — two Levi eigenvalues `λ∥, λ⊥`, two
  core radii, a condition number `cond = max λ / min λ`, `ℏ_q`, `C₀` — with the
  derived identity `cond = max(a⊥/a∥, a∥/a⊥)²` and the quantum-pressure
  consequence.  In dimension 3 the plane field `ker Θ` has complex rank 1, so its
  Levi form is `1 × 1`: the eigenvalue pair and its condition number are
  **undefined**, and `levi_restriction_rank_one` below is the algebraic form of
  that fact.  The removed algebra was true about abstract reals but no longer has
  a referent; it is recorded in the content block's `authorNotes` and in git
  history.

  No `sorry`, no `axiom`, no class.
-/

import Mathlib.LinearAlgebra.CrossProduct

namespace QOU.FluidDynamics

namespace CoreLevi

open Matrix

variable {R : Type*} [CommRing R]

/-- **The Levi scalar** of the plane field `ξ^⊥` at a point: `ξ·curl ξ`, given
the values `ξ` and `C = curl ξ` there. -/
def leviScalar (ξ C : Fin 3 → R) : R := ξ ⬝ᵥ C

/-- **Identity D2.**  With `ω = f ξ` and `curl ω = f·curl ξ + ∇f × ξ` (product
rule; `C = curl ξ`, `g = ∇f` at the point), the vorticity helicity density is
`ω·curl ω = f²·(ξ·curl ξ)`.  The `∇f` term drops because `ξ·(g × ξ) = 0`. -/
theorem helicity_rescale (f : R) (ξ C g : Fin 3 → R) :
    (f • ξ) ⬝ᵥ (f • C + g ⨯₃ ξ) = f ^ 2 * leviScalar ξ C := by
  rw [dotProduct_add, smul_dotProduct, dotProduct_smul, smul_dotProduct,
    dot_cross_self]
  simp only [leviScalar, smul_eq_mul, add_zero, mul_zero]
  ring

/-- **The contact criterion does not depend on the scale `f`.**  Over a ring
without zero divisors, for `f ≠ 0`: `f²·s ≠ 0 ↔ s ≠ 0`.  With
`s = ξ·curl ξ` and `Θ ∧ dΘ = f²·s·vol` this says `ker(f ξ♭)` is contact exactly
where `ξ·curl ξ ≠ 0`; with `helicity_rescale` (and `f = |ω|`) it is the same
locus as `ω·curl ω ≠ 0`. -/
theorem contact_iff_rescale [NoZeroDivisors R] {f : R} (hf : f ≠ 0) (s : R) :
    f ^ 2 * s ≠ 0 ↔ s ≠ 0 := by
  constructor
  · intro h hs; exact h (by rw [hs, mul_zero])
  · intro hs; exact mul_ne_zero (pow_ne_zero 2 hf) hs

/-- Binet–Cauchy rearranged, with no hypotheses:
`(ξ·ξ)(C·(v×w)) − (ξ·C)(ξ·(v×w)) = ((ξ×C)·v)(ξ·w) − ((ξ×C)·w)(ξ·v)`. -/
theorem levi_restriction_key (ξ C v w : Fin 3 → R) :
    (ξ ⬝ᵥ ξ) * (C ⬝ᵥ (v ⨯₃ w)) - (ξ ⬝ᵥ C) * (ξ ⬝ᵥ (v ⨯₃ w))
      = ((ξ ⨯₃ C) ⬝ᵥ v) * (ξ ⬝ᵥ w) - ((ξ ⨯₃ C) ⬝ᵥ w) * (ξ ⬝ᵥ v) := by
  have h1 := cross_dot_cross ξ C ξ (v ⨯₃ w)
  rw [cross_cross_eq_smul_sub_smul', dotProduct_sub, dotProduct_smul,
    dotProduct_smul, smul_eq_mul, smul_eq_mul, dotProduct_comm C ξ,
    dotProduct_comm v ξ] at h1
  linear_combination -h1

/-- **The Levi form on `ker Θ` has rank one.**  For a unit `ξ` and `v, w ∈ ξ^⊥`,
`C·(v × w) = (ξ·C)·(ξ·(v × w))`.  Read with `C = curl ξ`: `dξ♭` restricted to
the plane `ξ^⊥` is the scalar `ξ·curl ξ` times the plane's area form
`ξ·(v × w)`.  So the Levi datum of `ξ^⊥` is one number, not an eigenvalue
pair. -/
theorem levi_restriction_rank_one (ξ C v w : Fin 3 → R)
    (hunit : ξ ⬝ᵥ ξ = 1) (hv : ξ ⬝ᵥ v = 0) (hw : ξ ⬝ᵥ w = 0) :
    C ⬝ᵥ (v ⨯₃ w) = leviScalar ξ C * (ξ ⬝ᵥ (v ⨯₃ w)) := by
  have h := levi_restriction_key ξ C v w
  rw [hunit, hv, hw] at h
  simp only [leviScalar]
  linear_combination h

/-- **Core Levi form** ([`prop:core-levi-form`], re-scoped 2026-10-13).

For `Θ = f·ξ♭` with unit `ξ`, `C = curl ξ`, `g = ∇f` at a point:

* the restriction of `dΘ = df ∧ ξ♭ + f·dξ♭` to `ker Θ = ξ^⊥` is
  `f·(ξ·C)` times the area form — on `ξ^⊥` the `df ∧ ξ♭` term vanishes and
  `dξ♭(v, w) = C·(v × w)`; and
* the vorticity helicity density is `(f ξ)·(f C + g × ξ) = f²·(ξ·C)`.

Both conjuncts are derived from `levi_restriction_rank_one` and
`helicity_rescale`; neither is a hypothesis restated. -/
-- Ref: [leitner2026] prop:core-levi-form
theorem core_levi_form (f : R) (ξ C g v w : Fin 3 → R)
    (hunit : ξ ⬝ᵥ ξ = 1) (hv : ξ ⬝ᵥ v = 0) (hw : ξ ⬝ᵥ w = 0) :
    f * (C ⬝ᵥ (v ⨯₃ w)) = (f * leviScalar ξ C) * (ξ ⬝ᵥ (v ⨯₃ w)) ∧
      (f • ξ) ⬝ᵥ (f • C + g ⨯₃ ξ) = f ^ 2 * leviScalar ξ C := by
  refine ⟨?_, helicity_rescale f ξ C g⟩
  rw [levi_restriction_rank_one ξ C v w hunit hv hw]
  ring

/-- Non-vacuity: the rank-one form is not identically zero.  With
`ξ = e₃ = C`, `v = e₁`, `w = e₂`, both sides equal `1`. -/
example : (![0, 0, 1] : Fin 3 → ℤ) ⬝ᵥ (![1, 0, 0] ⨯₃ ![0, 1, 0]) = 1 := by
  simp [cross_apply, dotProduct, Fin.sum_univ_three]

end CoreLevi

end QOU.FluidDynamics
