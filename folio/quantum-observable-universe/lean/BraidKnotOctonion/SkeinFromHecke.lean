/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Algebra.Algebra.Basic
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Algebra.Field.Rat
import Mathlib.Tactic.NoncommRing
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum

/-!
# The skein relation, derived from the Hecke quadratic relation

Mathlib has neither an Iwahori–Hecke algebra nor a skein relation: a
case-insensitive word search over the vendored tree (`leanprover/lean4:v4.24.0`,
Mathlib commit `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`) returns **0** hits for
`skein`, `Temperley`, `Kauffman`, `Jones polynomial` and `Ocneanu`, and exactly
**1** for `Hecke` — a paper title in the `NumberTheory/FLT/Basic` bibliography
comment. `CoxeterMatrix` and `CoxeterSystem` exist; no `q`-deformation of them
does.

This file supplies the purely algebraic half of the skein calculus, at the level
of a **single ring element**. Nothing here is diagrammatic and nothing here is
topological.

## The setting

`R` is any commutative ring, `A` any (possibly noncommutative) `R`-algebra,
`q qi : R` a pair of scalars, and `T : A` an element satisfying the Hecke
quadratic relation in this repository's symmetric normalisation
(AGENTS.md §7a):

  `T * T = (q - qi) * T + 1`      (`IsHeckeGenerator`)

Where the *eigenvalue factorisation* is used, `q` and `qi` are additionally
required to be mutually inverse (`q * qi = 1`), so that `qi` is a legitimate
stand-in for `q⁻¹`. Carrying `qi` as a separate scalar with an explicit
hypothesis, rather than writing `q⁻¹`, is what keeps the base ring a bare
`CommRing`: no `Field`, no `Inv`, no ordering, no archimedean structure appears
anywhere in this file (AGENTS.md §7c).

## What is a THEOREM here

Everything below is proved; there is no `sorry` and no new axiom.

* `mul_negCrossing`, `negCrossing_mul` — `T` is invertible, with the **explicit**
  two-sided inverse `T - (q - qi)`. Only the quadratic relation is used; `q` need
  not be a unit for this.
* `isUnit_of_isHeckeGenerator`, `heckeUnit` — the resulting unit of `A`.
* `sub_inv_eq`, `sub_inv_eq_smul_one` — **the skein relation.** For *any* right
  inverse `S` of `T`, `T - S = (q - qi) · 1`. This is `L₊ - L₋ = (q - q⁻¹) L₀`
  with `L₊ = T`, `L₋ = T⁻¹`, `L₀ = 1`. The content beyond `mul_negCrossing` is
  that a right inverse of `T` is forced to *be* `T - (q - qi)`, so the relation
  does not depend on which inverse one names.
* `isHeckeGenerator_of_sub_inv`, `isHeckeGenerator_iff_sub_inv` — **the converse,
  and hence the equivalence.** For an element that *has* a right inverse `S`, the
  skein relation `T - S = (q - qi)` implies the quadratic back again, so the two
  are equivalent. This is the precise sense in which "the skein relation is the
  Hecke relation"; note the standing hypothesis `T * S = 1`, without which the
  statement is not even well posed.
* `isHeckeGenerator_iff_factored` — the **eigenvalue factorisation**, as an
  equivalence: given `q * qi = 1`,
  `T * T = (q - qi) T + 1  ↔  (T - q)(T + qi) = 0`.
  Both directions. This is what licenses the reading "`T` has eigenvalues `q`
  and `-qi`", and it is the step that turns the Hecke relation into the skein
  relation.
* `factored_swap` — the factors commute past each other: `(T + qi)(T - q) = 0`
  as well.
* `isHeckeGenerator_mirror` — **the mirror involution.** `(q - qi) - T`, which is
  `-T⁻¹`, is again a Hecke generator *with the same parameters*. This is the
  algebraic shadow of reflecting a crossing: `T` and `-T⁻¹` have the same
  eigenvalue pair `{q, -qi}`.

## What is a HYPOTHESIS or a DEFINITION here

* `IsHeckeGenerator` is a **definition** — the quadratic relation, named. No
  claim is made that any particular algebra of interest contains such an element;
  §*Non-vacuity* below exhibits some that do.
* **The knot-theoretic reading is an interpretation, not a proved
  correspondence.** Calling `T` a positive crossing `L₊`, `T - (q - qi)` a
  negative crossing `L₋`, and `1` a smoothing `L₀` is the standard dictionary
  (AGENTS.md §7a; Jones, Kassel–Turaev), and it is *not formalised anywhere in
  this repository*. There is no link diagram, no Reidemeister move and no braid
  closure in this file, so nothing here proves that these three elements are the
  three resolutions of a crossing in a diagram. The theorems are theorems about
  a ring element; the topology is a reading imposed on them from outside.

## Non-vacuity

A spec nothing satisfies proves nothing, so three witnesses are exhibited, in
increasing strength:

* `isHeckeGenerator_left`, `isHeckeGenerator_right` — the two eigenvalue scalars
  `q` and `-qi`, viewed in `R` itself. These are the one-dimensional
  representations.
* `isHeckeGenerator_witness2` — a **non-scalar** witness `!![q, 1; 0, -qi]` in
  `2 × 2` matrices over any `R` with `q * qi = 1`, together with
  `witness2_ne_algebraMap`: it is not in the image of `algebraMap`, so the
  theorems above are not secretly statements about scalars.
* `exists_isHeckeGenerator_ne_algebraMap` — the same at the fully concrete
  parameters `q = 2`, `qi = 1/2` over `ℚ`, where `q ≠ -qi` so the eigenvalue
  factorisation is a genuine factorisation into distinct linear factors.

## Relation to the rest of this repository

The invertibility half of this file exists elsewhere in QOU in four
*non-interchangeable* forms, none of which subsumes this one:
`QOU.QBeta.JonesNormalisation.sigma_inv` (needs `Field R`, and imports the
Temperley–Lieb tower), `QOU.Hecke.IwahoriHecke.σ_mul_σInv` and
`QOU.SchurWeyl.HeckeAlgebra.σ_mul_σInv` (statements about the generators of two
particular `RingQuot` presentations, not about an arbitrary element),
`QOU.BraidsAndKnots.sigma_mul_sub_h` (one side only, and with `σ` a *scalar* in a
`CommRing`), and `QOU.MathlibExt.OcneanuTrace.gen_inv_eq_of_quadratic` (one side
only, inside a trace structure).

To be precise about what is *not* new: `sigma_inv` is already element-level and
already two-sided, so the invertibility statement as such is not this file's
contribution. What is new is (i) the **base ring** — carrying `qi` as a separate
scalar with `q * qi = 1` supplied only where needed drops `Field R` to a bare
`CommRing R`, and drops the Temperley–Lieb import to nothing outside Mathlib;
(ii) the factorisation stated as an **iff** rather than as a one-way consequence;
(iii) the skein relation stated against an *arbitrary* inverse, together with its
converse, so that the quadratic and the skein relation are proved *equivalent*;
and (iv) the mirror involution. Imports are Mathlib-only.

The scalar predicate `QOU.BraidsAndKnots.IsHeckeGen (σ h : R)` is the same
quadratic with the parameter pair already contracted to `h = q - qi` and the
element required to be a scalar; `IsHeckeGenerator` below is its algebra-element
refinement, and `isHeckeGenerator_left`/`isHeckeGenerator_right` generalise that
file's `isHeckeGen_q` from `Field R` with `q ≠ 0` to `CommRing R` with
`q * qi = 1`.

## References

* [jones1987] V. F. R. Jones, *Hecke algebra representations of braid groups and
  link polynomials*, Ann. of Math. 126 (1987), 335–388.
* [kasselTuraev2008] C. Kassel and V. Turaev, *Braid Groups*, GTM 247, §4
  (the Hecke algebra and the skein relation).
-/

namespace QOU.MathlibExt.SkeinRelation

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-! ## The Hecke quadratic relation -/

/-- `T` satisfies the **Hecke quadratic relation** with parameters `q`, `qi`:

  `T² = (q - qi) · T + 1`.

This is the symmetric (skein) normalisation of AGENTS.md §7a, in which `qi`
plays the role of `q⁻¹`; the Iwahori normalisation `(T - q)(T + 1) = 0` is a
different, rescaled convention and is *not* what this predicate says.

The parameter `qi` is deliberately unconstrained here — `q * qi = 1` is required
only where the eigenvalue factorisation is used, and stating the predicate
without it keeps the invertibility results below free of that hypothesis. -/
def IsHeckeGenerator (q qi : R) (T : A) : Prop :=
  T * T = algebraMap R A (q - qi) * T + 1

/-- Accessor: unfold `IsHeckeGenerator` to the underlying equation.

This is definitional unfolding, not a mathematical claim. -/
theorem IsHeckeGenerator.eq {q qi : R} {T : A} (h : IsHeckeGenerator q qi T) :
    T * T = algebraMap R A (q - qi) * T + 1 := h

/-! ## Invertibility, and the explicit inverse

`q` is **not** assumed to be a unit in this section. In the symmetric
normalisation the constant term of the quadratic is already `1`, so the inverse
falls out with no division at all — which is exactly why this normalisation is
the one the skein relation is stated in. -/

/-- The **negative crossing** `T - (q - qi)`.

Named for its role in the skein dictionary: it is the inverse of `T` whenever
`T` is a Hecke generator (`mul_negCrossing`, `negCrossing_mul`), and the
dictionary reads `T = L₊`, `negCrossing q qi T = L₋`. That reading is an
interpretation; the inverse property is the theorem. -/
def negCrossing (q qi : R) (T : A) : A :=
  T - algebraMap R A (q - qi)

variable {q qi : R} {T : A}

/-- `T · (T - (q - qi)) = 1`: the negative crossing is a right inverse. -/
theorem mul_negCrossing (hT : IsHeckeGenerator q qi T) :
    T * negCrossing q qi T = 1 := by
  have hc : algebraMap R A (q - qi) * T = T * algebraMap R A (q - qi) :=
    Algebra.commutes (q - qi) T
  rw [negCrossing, mul_sub, hT.eq, hc]
  abel

/-- `(T - (q - qi)) · T = 1`: the negative crossing is a left inverse. -/
theorem negCrossing_mul (hT : IsHeckeGenerator q qi T) :
    negCrossing q qi T * T = 1 := by
  rw [negCrossing, sub_mul, hT.eq]
  abel

/-- The unit of `A` determined by a Hecke generator, with its inverse given
explicitly rather than existentially. -/
def heckeUnit (hT : IsHeckeGenerator q qi T) : Aˣ where
  val := T
  inv := negCrossing q qi T
  val_inv := mul_negCrossing hT
  inv_val := negCrossing_mul hT

/-- **A Hecke generator is a unit**, with no hypothesis on `q` whatsoever.

`A` is not assumed commutative, so this needs both of `mul_negCrossing` and
`negCrossing_mul`; a one-sided inverse would not suffice. -/
theorem isUnit_of_isHeckeGenerator (hT : IsHeckeGenerator q qi T) : IsUnit T :=
  ⟨heckeUnit hT, rfl⟩

@[simp] theorem heckeUnit_val (hT : IsHeckeGenerator q qi T) :
    ((heckeUnit hT : Aˣ) : A) = T := rfl

@[simp] theorem heckeUnit_inv (hT : IsHeckeGenerator q qi T) :
    (((heckeUnit hT)⁻¹ : Aˣ) : A) = negCrossing q qi T := rfl

/-! ## The skein relation -/

/-- **The skein relation.** `L₊ - L₋ = (q - q⁻¹) · L₀`.

Stated against an *arbitrary* right inverse `S` of `T`, not against the
particular element `negCrossing q qi T`. That is the content: a right inverse of
a Hecke generator is forced to equal `T - (q - qi)` — it cannot be anything else
— so the difference `T - S` is determined by the parameters alone and the
relation is independent of how the negative crossing is presented. -/
theorem sub_inv_eq (hT : IsHeckeGenerator q qi T) {S : A} (hS : T * S = 1) :
    T - S = algebraMap R A (q - qi) := by
  have hSeq : S = negCrossing q qi T := by
    calc S = 1 * S := (one_mul S).symm
      _ = negCrossing q qi T * T * S := by rw [negCrossing_mul hT]
      _ = negCrossing q qi T * (T * S) := mul_assoc _ _ _
      _ = negCrossing q qi T := by rw [hS, mul_one]
  rw [hSeq, negCrossing, sub_sub_cancel]

/-- The skein relation with the smoothing `L₀ = 1` made visible:

  `T - T⁻¹ = (q - qi) • 1`. -/
theorem sub_inv_eq_smul_one (hT : IsHeckeGenerator q qi T) {S : A} (hS : T * S = 1) :
    T - S = (q - qi) • (1 : A) := by
  rw [sub_inv_eq hT hS, Algebra.algebraMap_eq_smul_one]

/-- **The converse of the skein relation.**

If `S` is a right inverse of `T` and the difference `T - S` is the scalar
`q - qi`, then `T` satisfies the Hecke quadratic. Multiplying `T - S = q - qi`
through by `T` on the right and using `T * S = 1` returns the quadratic; the
right-inverse hypothesis is doing real work and cannot be dropped, since without
it `T - S = q - qi` says nothing about `T²`. -/
theorem isHeckeGenerator_of_sub_inv {S : A} (hS : T * S = 1)
    (h : T - S = algebraMap R A (q - qi)) : IsHeckeGenerator q qi T := by
  have hSeq : S = T - algebraMap R A (q - qi) := by
    rw [← h]; abel
  have hc : algebraMap R A (q - qi) * T = T * algebraMap R A (q - qi) :=
    Algebra.commutes (q - qi) T
  rw [hSeq, mul_sub] at hS
  show T * T = algebraMap R A (q - qi) * T + 1
  rw [hc]
  exact (sub_eq_iff_eq_add.mp hS).trans (add_comm _ _)

/-- **The skein relation *is* the Hecke relation**, for an element that has a
right inverse.

This is the equivalence the file's title claims, stated where it is actually
true: fix any `S` with `T * S = 1`; then `T` satisfies the Hecke quadratic iff
`T - S = (q - qi)`. Forward is `sub_inv_eq`, backward is
`isHeckeGenerator_of_sub_inv`. The hypothesis `T * S = 1` is not removable — for
an element with no inverse there is no `L₋` to subtract. -/
theorem isHeckeGenerator_iff_sub_inv {S : A} (hS : T * S = 1) :
    IsHeckeGenerator q qi T ↔ T - S = algebraMap R A (q - qi) :=
  ⟨fun hT => sub_inv_eq hT hS, isHeckeGenerator_of_sub_inv hS⟩

/-- The skein relation for the packaged unit. -/
theorem heckeUnit_sub_inv (hT : IsHeckeGenerator q qi T) :
    ((heckeUnit hT : Aˣ) : A) - (((heckeUnit hT)⁻¹ : Aˣ) : A)
      = algebraMap R A (q - qi) :=
  sub_inv_eq hT (heckeUnit hT).val_inv

/-! ## The eigenvalue factorisation

From here on `q` and `qi` are mutually inverse, so that `qi` really is `q⁻¹`. -/

/-- The expansion underlying the factorisation. Both the forward and the reverse
direction of `isHeckeGenerator_iff_factored` are read off this one identity, and
so is `factored_swap`. -/
theorem factored_expand (hqi : q * qi = 1) (T : A) :
    (T - algebraMap R A q) * (T + algebraMap R A qi)
      = T * T - (algebraMap R A (q - qi) * T + 1) := by
  have hI : algebraMap R A qi * T = T * algebraMap R A qi := Algebra.commutes qi T
  have hprod : algebraMap R A q * algebraMap R A qi = 1 := by
    rw [← map_mul, hqi, map_one]
  have e1 : (T - algebraMap R A q) * (T + algebraMap R A qi)
      = T * T + T * algebraMap R A qi - algebraMap R A q * T
        - algebraMap R A q * algebraMap R A qi := by
    noncomm_ring
  have e2 : algebraMap R A (q - qi) * T + 1
      = algebraMap R A q * T - algebraMap R A qi * T + 1 := by
    rw [map_sub]; noncomm_ring
  rw [e1, e2, hprod, hI]
  abel

/-- **The eigenvalue factorisation, as an equivalence.**

For mutually inverse scalars `q`, `qi`, the Hecke quadratic relation
`T² = (q - qi)T + 1` holds **iff** `(T - q)(T + qi) = 0`.

The right-hand form is what licenses the phrase "`T` has eigenvalues `q` and
`-qi`", and multiplying it through by `T⁻¹` is the classical derivation of the
skein relation. Stating it as an `iff` — rather than as a one-way consequence of
the quadratic — records that the quadratic and the factored form carry the same
information.

This is an equivalence between the quadratic and the **factored** form; it is
`isHeckeGenerator_iff_sub_inv` that states the equivalence between the quadratic
and the **skein relation** itself. -/
theorem isHeckeGenerator_iff_factored (hqi : q * qi = 1) (T : A) :
    IsHeckeGenerator q qi T ↔
      (T - algebraMap R A q) * (T + algebraMap R A qi) = 0 := by
  rw [factored_expand hqi T, sub_eq_zero]
  exact Iff.rfl

/-- The two linear factors annihilate `T` in either order. -/
theorem factored_swap (hqi : q * qi = 1) (hT : IsHeckeGenerator q qi T) :
    (T + algebraMap R A qi) * (T - algebraMap R A q) = 0 := by
  have hQ : algebraMap R A q * T = T * algebraMap R A q := Algebra.commutes q T
  have hI : algebraMap R A qi * T = T * algebraMap R A qi := Algebra.commutes qi T
  have hprod : algebraMap R A qi * algebraMap R A q = 1 := by
    rw [← map_mul, mul_comm, hqi, map_one]
  have e1 : (T + algebraMap R A qi) * (T - algebraMap R A q)
      = T * T - T * algebraMap R A q + algebraMap R A qi * T
        - algebraMap R A qi * algebraMap R A q := by
    noncomm_ring
  have e2 : algebraMap R A (q - qi) * T + 1
      = algebraMap R A q * T - algebraMap R A qi * T + 1 := by
    rw [map_sub]; noncomm_ring
  rw [e1, hprod, hI, hT.eq, e2, hQ, hI]
  abel

/-! ## The mirror involution -/

/-- **`-T⁻¹` is again a Hecke generator, with the same parameters.**

Writing `h = q - qi`, the element `h - T` equals `-(T - h) = -T⁻¹`
(`mirror_eq_neg_negCrossing`), and it satisfies the *same* quadratic relation
that `T` does. The eigenvalue reading explains why: `T` has eigenvalues
`{q, -qi}`, so `T⁻¹` has `{qi, -q}` and `-T⁻¹` has `{-qi, q}` — the same pair
back again.

Two honesty notes on that paragraph. The eigenvalue reading is a *heuristic* and
it silently assumes `q * qi = 1` (it inverts `q` and `-qi`); the **theorem** does
not, and carries no such hypothesis — the proof is the direct expansion
`(h - T)² = h² - 2hT + T² = h² - hT + 1 = h(h - T) + 1`, valid for any `qi`. And
"mirror image of a crossing" is an interpretation, not a formalised
correspondence; the statement is about ring elements. -/
theorem isHeckeGenerator_mirror (hT : IsHeckeGenerator q qi T) :
    IsHeckeGenerator q qi (algebraMap R A (q - qi) - T) := by
  have hc : algebraMap R A (q - qi) * T = T * algebraMap R A (q - qi) :=
    Algebra.commutes (q - qi) T
  show (algebraMap R A (q - qi) - T) * (algebraMap R A (q - qi) - T)
      = algebraMap R A (q - qi) * (algebraMap R A (q - qi) - T) + 1
  have e1 : (algebraMap R A (q - qi) - T) * (algebraMap R A (q - qi) - T)
      = algebraMap R A (q - qi) * algebraMap R A (q - qi)
        - algebraMap R A (q - qi) * T - T * algebraMap R A (q - qi) + T * T := by
    noncomm_ring
  rw [e1, hT.eq, ← hc, mul_sub]
  abel

/-- The mirror is the negative of the negative crossing: `h - T = -(T - h)`. -/
@[simp] theorem mirror_eq_neg_negCrossing (q qi : R) (T : A) :
    algebraMap R A (q - qi) - T = -negCrossing q qi T := by
  rw [negCrossing, neg_sub]

/-- The mirror is an involution. -/
@[simp] theorem mirror_mirror (q qi : R) (T : A) :
    algebraMap R A (q - qi) - (algebraMap R A (q - qi) - T) = T :=
  sub_sub_cancel _ _

/-! ## Non-vacuity

Three witnesses. Without them every theorem above could be true only because
nothing satisfies `IsHeckeGenerator`. -/

section Vacuity

variable (q qi : R)

/-- The **first eigenvalue** `q`, in `R` viewed as an algebra over itself, is a
Hecke generator. This is the trivial one-dimensional representation. -/
theorem isHeckeGenerator_left (hqi : q * qi = 1) :
    IsHeckeGenerator (A := R) q qi q := by
  show q * q = algebraMap R R (q - qi) * q + 1
  simp only [Algebra.algebraMap_self, RingHom.id_apply]
  linear_combination hqi

/-- The **second eigenvalue** `-qi` is likewise a Hecke generator: the sign
representation. That `IsHeckeGenerator` has two distinct scalar solutions is the
content of the eigenvalue factorisation, seen from the other side. -/
theorem isHeckeGenerator_right (hqi : q * qi = 1) :
    IsHeckeGenerator (A := R) q qi (-qi) := by
  show (-qi) * (-qi) = algebraMap R R (q - qi) * (-qi) + 1
  simp only [Algebra.algebraMap_self, RingHom.id_apply]
  linear_combination hqi

/-- A **non-scalar** witness: the upper-triangular matrix with the two
eigenvalues on the diagonal.

  `!![q, 1; 0, -qi]`

Its existence is what shows the theorems above are not secretly about scalars —
see `witness2_ne_algebraMap`. -/
def witness2 : Matrix (Fin 2) (Fin 2) R := !![q, 1; 0, -qi]

/-- The `2 × 2` witness satisfies the Hecke quadratic relation. -/
theorem isHeckeGenerator_witness2 (hqi : q * qi = 1) :
    IsHeckeGenerator q qi (witness2 q qi) := by
  show witness2 q qi * witness2 q qi
      = algebraMap R (Matrix (Fin 2) (Fin 2) R) (q - qi) * witness2 q qi + 1
  rw [Algebra.algebraMap_eq_smul_one, smul_mul_assoc, one_mul]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [witness2, Matrix.mul_apply, Fin.sum_univ_two] <;>
    first
      | ring1
      | linear_combination hqi

/-- The `2 × 2` witness is **not a scalar**: it is not in the image of
`algebraMap`, because its `(0,1)` entry is `1` while every scalar matrix has
`(0,1)` entry `0`. -/
theorem witness2_ne_algebraMap [Nontrivial R] (c : R) :
    witness2 q qi ≠ algebraMap R (Matrix (Fin 2) (Fin 2) R) c := by
  intro h
  have h01 := congrArg (fun M : Matrix (Fin 2) (Fin 2) R => M 0 1) h
  simp [witness2, Algebra.algebraMap_eq_smul_one] at h01

end Vacuity

/-- A fully concrete, non-degenerate instance: over `ℚ` with `q = 2` and
`qi = 1/2`, the matrix `!![2, 1; 0, -1/2]` is a Hecke generator, is not a scalar,
and the two eigenvalues `q = 2` and `-qi = -1/2` are distinct — so the
factorisation `(T - 2)(T + 1/2) = 0` really is a factorisation into two different
linear factors, not a repeated root. -/
theorem exists_isHeckeGenerator_ne_algebraMap :
    ∃ T : Matrix (Fin 2) (Fin 2) ℚ,
      IsHeckeGenerator (2 : ℚ) (1 / 2 : ℚ) T ∧
        (∀ c : ℚ, T ≠ algebraMap ℚ (Matrix (Fin 2) (Fin 2) ℚ) c) ∧
        (2 : ℚ) ≠ -(1 / 2 : ℚ) :=
  ⟨witness2 2 (1 / 2), isHeckeGenerator_witness2 2 (1 / 2) (by norm_num),
    fun c => witness2_ne_algebraMap 2 (1 / 2) c, by norm_num⟩

end QOU.MathlibExt.SkeinRelation
