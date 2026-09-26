/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.WtraceRadicalIdeal

/-!
# `H_n(q)/rad(wtrace) ≅ ∏_{ℓ(λ) ≤ 2} M_{f^λ}`

DRAFT — not yet compiled.  `WtraceRadicalIdeal` supplies the two halves of the first
isomorphism theorem (`traceRadicalIdeal_eq_ker` and `twoRowProduct_surjective`); what is
missing from the pinned Mathlib is the *lift out of the quotient*, so this file builds it.

`Mathlib/GroupTheory/Congruence/Basic.lean` has `Con.lift` for **monoid** congruences;
`Mathlib/RingTheory/Congruence/` has no ring analogue and
`Mathlib/RingTheory/TwoSidedIdeal/` carries only `ker`, `mem_ker`, `ker_eq_bot`.  So
`liftAlgHom` below is the general-purpose piece and belongs upstream eventually.
-/

namespace QOU.SchurWeyl.WtraceRadicalQuotient

open QOU.Mathlib QOU.SchurWeyl QOU.SchurWeyl.SeminormalRep
open QOU.SchurWeyl.WtraceRadicalTwoRow QOU.SchurWeyl.WtraceRadicalIdeal
open QOU.QBeta.TemperleyLiebTower QOU.QBeta.MarkovTraceQuotient

section Lift

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
variable {B : Type*} [Ring B] [Algebra R B]

/-- **An algebra hom out of a `RingCon` quotient.**  The ring-theoretic analogue of
Mathlib's `Con.lift`, which exists only for monoid congruences. -/
def liftAlgHom (c : RingCon A) (f : A →ₐ[R] B) (H : ∀ x y : A, c x y → f x = f y) :
    c.Quotient →ₐ[R] B where
  toFun := Quotient.lift (⇑f) H
  map_one' := map_one f
  map_mul' := by rintro ⟨a⟩ ⟨b⟩; exact map_mul f a b
  map_zero' := map_zero f
  map_add' := by rintro ⟨a⟩ ⟨b⟩; exact map_add f a b
  commutes' r := f.commutes r

@[simp] theorem liftAlgHom_coe (c : RingCon A) (f : A →ₐ[R] B)
    (H : ∀ x y : A, c x y → f x = f y) (a : A) :
    liftAlgHom c f H (a : c.Quotient) = f a := rfl

@[simp] theorem liftAlgHom_mk (c : RingCon A) (f : A →ₐ[R] B)
    (H : ∀ x y : A, c x y → f x = f y) (a : A) :
    liftAlgHom c f H (c.mk' a) = f a := rfl

/-- The lift is **injective** exactly when the congruence is the whole kernel. -/
theorem liftAlgHom_injective (c : RingCon A) (f : A →ₐ[R] B)
    (H : ∀ x y : A, c x y → f x = f y) (Hconv : ∀ x y : A, f x = f y → c x y) :
    Function.Injective (liftAlgHom c f H) := by
  rintro ⟨a⟩ ⟨b⟩ hab
  have h : f a = f b := hab
  exact Quotient.sound (Hconv a b h)

end Lift

section Application

/-- The target of the two-row projection: one matrix block per at-most-two-row partition. -/
abbrev TwoRowBlocks (n : ℕ) : Type :=
  ∀ lam : TwoRowIdx n, Matrix (StandardYoungTableau (partitionShape lam.1))
    (StandardYoungTableau (partitionShape lam.1)) ℝ

/-- **Two elements are congruent mod the radical iff the two-row projection cannot tell them
apart.**  `traceRadicalIdeal_eq_ker` transported to the congruence; it is the hypothesis the
lift needs, and in *both* directions at once, which is why it is stated as an iff. -/
theorem ringCon_iff_twoRowProduct_eq {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ k : ℕ, 0 < k → (q ^ 2 : ℝ) ^ k ≠ 1) (n : ℕ) (x y : Hecke ℝ q q⁻¹ n) :
    (traceRadicalIdeal (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n)).ringCon x y
      ↔ twoRowProduct q hq0 hq2 n x = twoRowProduct q hq0 hq2 n y := by
  rw [TwoSidedIdeal.rel_iff, traceRadicalIdeal_eq_ker hq0 hq2 hq21 hgen n,
    TwoSidedIdeal.mem_ker, map_sub, sub_eq_zero]

/-- The two-row projection, descended to the quotient.

**Not** built from `liftAlgHom` above, and the reason is a live instance collision rather
than a stylistic choice: there are **two** `Algebra ℝ` instances on this type — Mathlib's
`RingCon.instAlgebraQuotient` and the corpus's own
`QBeta.MarkovTraceQuotient.instAlgebraTraceQuot` — so `liftAlgHom`'s output (which picks
Mathlib's) and a signature written against `TraceQuot` (which picks the corpus's) are
different `AlgHom` types and do not unify.  Spelling the type as `.ringCon.Quotient` does
not help: `instAlgebraTraceQuot` matches whenever the ideal *is* a `traceRadicalIdeal`.
`TwoRowBlocks` adds a second, smaller mismatch of the same kind (`Pi.semiring` against
`Pi.ring.toSemiring`).  So this is inlined against the corpus's instances; `liftAlgHom`
stays as the general-purpose piece, which is what would go upstream.

That duplication is a defect in its own right and is **not fixed here** — changing which
instance the corpus uses is a behavioural change across every `quotMk` consumer, so it is
recorded rather than touched. -/
noncomputable def twoRowQuotHom {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ k : ℕ, 0 < k → (q ^ 2 : ℝ) ^ k ≠ 1) (n : ℕ) :
    TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n) →ₐ[ℝ] TwoRowBlocks n where
  toFun := Quotient.lift (⇑(twoRowProduct q hq0 hq2 n))
    (fun x y h => (ringCon_iff_twoRowProduct_eq hq0 hq2 hq21 hgen n x y).mp h)
  map_one' := map_one (twoRowProduct q hq0 hq2 n)
  map_mul' := by rintro ⟨a⟩ ⟨b⟩; exact map_mul (twoRowProduct q hq0 hq2 n) a b
  map_zero' := map_zero (twoRowProduct q hq0 hq2 n)
  map_add' := by rintro ⟨a⟩ ⟨b⟩; exact map_add (twoRowProduct q hq0 hq2 n) a b
  commutes' r := (twoRowProduct q hq0 hq2 n).commutes r

@[simp] theorem twoRowQuotHom_coe {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ k : ℕ, 0 < k → (q ^ 2 : ℝ) ^ k ≠ 1) (n : ℕ) (x : Hecke ℝ q q⁻¹ n) :
    twoRowQuotHom hq0 hq2 hq21 hgen n
        (x : TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n))
      = twoRowProduct q hq0 hq2 n x := rfl

/-- **Injective** by the ⊆ half of the kernel identity, **surjective** by
`twoRowProduct_surjective`. -/
theorem twoRowQuotHom_bijective {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ k : ℕ, 0 < k → (q ^ 2 : ℝ) ^ k ≠ 1) (n : ℕ) :
    Function.Bijective (twoRowQuotHom hq0 hq2 hq21 hgen n) := by
  constructor
  · rintro ⟨a⟩ ⟨b⟩ hab
    exact Quotient.sound ((ringCon_iff_twoRowProduct_eq hq0 hq2 hq21 hgen n a b).mpr hab)
  intro f
  obtain ⟨b, hb⟩ := twoRowProduct_surjective q hq0 hq2 n f
  refine ⟨(b : TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n)), ?_⟩
  rw [twoRowQuotHom_coe]
  exact hb

/-- **`H_n(q) / rad(wtrace) ≅ ∏_{ℓ(λ) ≤ 2} M_{f^λ}(ℝ)`**, for every `n`, at convention D.

`WtraceRadicalIdeal` supplied the two halves of the first isomorphism theorem; the missing
piece was a lift out of a `RingCon` quotient, which `liftAlgHom` above provides. -/
noncomputable def traceQuotEquiv {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ k : ℕ, 0 < k → (q ^ 2 : ℝ) ^ k ≠ 1) (n : ℕ) :
    TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n) ≃ₐ[ℝ] TwoRowBlocks n :=
  AlgEquiv.ofBijective _ (twoRowQuotHom_bijective hq0 hq2 hq21 hgen n)

@[simp] theorem traceQuotEquiv_coe {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ k : ℕ, 0 < k → (q ^ 2 : ℝ) ^ k ≠ 1) (n : ℕ) (x : Hecke ℝ q q⁻¹ n) :
    traceQuotEquiv hq0 hq2 hq21 hgen n
        (x : TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n))
      = twoRowProduct q hq0 hq2 n x := rfl

end Application


end QOU.SchurWeyl.WtraceRadicalQuotient
