/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.Algebra.Group.Basic
import Mathlib.Tactic

/-!
# Can `T = 0` be proved?  No — and that is a theorem, not a gap

Bean `qou-gzs0`, follow-up. Companion to
[`SignCoherentTwist.lean`](SignCoherentTwist.lean).

## The question

`qou-gzs0` established that the ribbon layer's only free parameter is an integer
framing `T`, contributing the weight `θ^T = q^{T/2}`, and that its quantum
(5.36 %) is ~4·10⁴ times coarser than the L2 gaps. The natural follow-up is
whether the framework *pins* `T = 0`, which would remove the parameter entirely.

It does not, and the reason is structural rather than a missing lemma.

## Why `T = 0` is not provable from the ribbon axioms

`framing_unobservable_iff_trivial_twist`: the framing weight is blind to `T`
**exactly** when `θ = 1`.

So at `q ≠ 1` — the whole substrate regime, `q₀ ≈ 1.11` — the framing is
*observable*: distinct `T` give distinct weights. A quantity that changes the
prediction cannot be fixed by the axioms that leave it free; it has to be
**pinned by a stated convention**. "`T = 0`" is therefore a normalisation
choice to be declared, not a proposition to be derived.

The converse is the classical boundary: `θ = 1` is `q = 1`, where framing
genuinely carries no information. That is consistent with
`BalancedCategory.ofSymmetric` making the symmetric case `θ = 𝟙`.

## What *is* provable, and is worth having

* `bar_invariant_forces_zero` — the bar involution negates the twist, so any
  **self-conjugate** state has `T = 0`. This is a genuine derivation of `T = 0`,
  on the sector where it applies (bar-invariant states; amphichirality).
* `zero_framing_is_weight_one` — `T = 0` is the multiplicative unit, i.e. the
  choice "no framing correction".

## The caveat that matters for the mass path

`qou-gzs0` found that `canonical_mass`'s `F_Bor` carries `/q³`, which is
**exactly** `q^{T/2}` at `T = −6` (−2 per Borromean component). If that factor
*is* the framing, then the operative convention in the mass formula is `T = −6`,
**not** `T = 0` — and proving `T = 0` would contradict the working formula rather
than support it.

So the target to settle is not "prove `T = 0`" but "**declare which framing the
mass path uses**", and that is a corpus/owner ruling, not a Lean obligation.
This file exists to make the choice visible as a choice.
-/

namespace QOU.StandardModel.FramingIsAChoice

/-- The ribbon weight of an integer framing, `θ ^ T`, in a commutative group of
units. -/
def framingWeight {M : Type*} [CommGroup M] (θ : M) (T : ℤ) : M := θ ^ T

@[simp] theorem framingWeight_zero {M : Type*} [CommGroup M] (θ : M) :
    framingWeight θ 0 = 1 := by
  simp [framingWeight]

/-- **`T = 0` is the "no correction" choice.** -/
theorem zero_framing_is_weight_one {M : Type*} [CommGroup M] (θ : M) :
    framingWeight θ 0 = 1 := framingWeight_zero θ

/-- **The framing is unobservable exactly when the twist is trivial.**

If every framing gives the same weight then `θ = 1`; conversely `θ = 1` makes
every weight `1`. So at `θ ≠ 1` — i.e. `q ≠ 1`, the substrate regime — distinct
framings give distinct predictions, and `T` must be fixed by a stated
convention. This is why `T = 0` cannot be a theorem of the ribbon axioms: they
are precisely the axioms that leave `T` free. -/
theorem framing_unobservable_iff_trivial_twist {M : Type*} [CommGroup M] (θ : M) :
    (∀ T : ℤ, framingWeight θ T = 1) ↔ θ = 1 := by
  constructor
  · intro h
    have := h 1
    simpa [framingWeight] using this
  · rintro rfl
    intro T
    simp [framingWeight]

/-- Sharper form: a **nontrivial** twist separates some pair of framings, so the
prediction genuinely depends on the choice. -/
theorem exists_framing_pair_distinguished {M : Type*} [CommGroup M] {θ : M}
    (hθ : θ ≠ 1) : ∃ T₁ T₂ : ℤ, framingWeight θ T₁ ≠ framingWeight θ T₂ := by
  refine ⟨1, 0, ?_⟩
  simpa [framingWeight] using hθ

/-- **Where `T = 0` IS derivable: self-conjugate states.**

The bar involution negates the per-strand twist (`TwistDatum.bar`), so a state
equal to its own conjugate satisfies `t = −t` pointwise, forcing `t = 0`. This
is a real derivation of zero framing — on the bar-invariant sector only. -/
theorem bar_invariant_forces_zero {n : ℕ} {t : Fin n → ℤ}
    (h : ∀ i, t i = -(t i)) : ∀ i, t i = 0 := by
  intro i
  have := h i
  omega

/-- Consequently a self-conjugate state has zero **total** twist, hence weight
`1`: it needs no framing convention at all. -/
theorem bar_invariant_total_zero {t : Fin 3 → ℤ}
    (h : ∀ i, t i = -(t i)) : t 0 + t 1 + t 2 = 0 := by
  have h0 := bar_invariant_forces_zero h 0
  have h1 := bar_invariant_forces_zero h 1
  have h2 := bar_invariant_forces_zero h 2
  omega

end QOU.StandardModel.FramingIsAChoice
