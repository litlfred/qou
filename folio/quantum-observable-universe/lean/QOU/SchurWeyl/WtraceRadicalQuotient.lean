/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.WtraceRadicalIdeal
import QOU.MathlibExt.RingConLiftAlgHom

/-!
# `H_n(q)/rad(wtrace) ≅ ∏_{ℓ(λ) ≤ 2} M_{f^λ}`

`WtraceRadicalIdeal` supplies the two halves of the first isomorphism theorem
(`traceRadicalIdeal_eq_ker` and `twoRowProduct_surjective`); this file turns them into an
`≃ₐ`, which the pinned Mathlib cannot do for a `RingCon` quotient.

The generic lift that gap calls for now lives in `QOU.MathlibExt.RingConLiftAlgHom`, split
out under §7c because it mentions no `ℝ`.  🛑 **`traceQuotEquiv` below does not use it** —
see `twoRowQuotHom`'s docstring for the instance collision that forces an inlined
construction.  Do not read the split as a dependency.
-/

namespace QOU.SchurWeyl.WtraceRadicalQuotient

open QOU.Mathlib QOU.SchurWeyl QOU.SchurWeyl.SeminormalRep
open QOU.SchurWeyl.WtraceRadicalTwoRow QOU.SchurWeyl.WtraceRadicalIdeal
open QOU.QBeta.TemperleyLiebTower QOU.QBeta.MarkovTraceQuotient


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

**Not** built from `RingConLiftAlgHom.liftAlgHom`, and the reason is a live instance collision rather
than a stylistic choice: there are **two** `Algebra ℝ` instances on this type — Mathlib's
`RingCon.instAlgebraQuotient` and the corpus's own
`QBeta.MarkovTraceQuotient.instAlgebraTraceQuot` — so `liftAlgHom`'s output (which picks
Mathlib's) and a signature written against `TraceQuot` (which picks the corpus's) are
different `AlgHom` types and do not unify.  Spelling the type as `.ringCon.Quotient` does
not help: `instAlgebraTraceQuot` matches whenever the ideal *is* a `traceRadicalIdeal`.
`TwoRowBlocks` adds a second, smaller mismatch of the same kind (`Pi.semiring` against
`Pi.ring.toSemiring`).  So this is inlined against the corpus's instances; `liftAlgHom`
stays as the general-purpose piece in `QOU.MathlibExt.RingConLiftAlgHom`, which is
what would go upstream.

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
piece was a lift out of a `RingCon` quotient.

🛑 **Corrected:** an earlier version of this line credited `liftAlgHom` for supplying that
piece.  It does not — `twoRowQuotHom`, which this is `AlgEquiv.ofBijective` of, is inlined
against the corpus's algebra instances for the reason its own docstring gives, and
`liftAlgHom` (now `QOU.MathlibExt.RingConLiftAlgHom.liftAlgHom`) is on no critical path
here.  The two statements contradicted each other fifty lines apart. -/
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

/-- **The isomorphism is not between one-point algebras.**

`AlgEquiv.ofBijective` would accept a bijection of trivial algebras just as happily, so this
forecloses the vacuous reading structurally rather than by inspection: `wtrace 1 = 1 ≠ 0`,
so `1` is not in the radical, so the class of `1` is not the class of `0`.  Its image
`twoRowProduct 1 = 1` is therefore nonzero in `TwoRowBlocks n`, which also says the target
is not the one-point ring. -/
theorem traceQuot_one_ne_zero {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : ℝ) ^ i ≠ 1) (n : ℕ) :
    ((1 : Hecke ℝ q q⁻¹ n) :
        TraceQuot (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n)) ≠ 0 :=
  quot_one_ne_zero (wtrace q hq0 hq2 n) (wtrace_cyclic q hq0 hq2 n)
    (by rw [wtrace_one q hq0 hq2 hq21 hgen n]; exact one_ne_zero)

end Application


end QOU.SchurWeyl.WtraceRadicalQuotient
