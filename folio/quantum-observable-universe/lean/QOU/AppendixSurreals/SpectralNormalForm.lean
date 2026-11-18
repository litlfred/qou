import QOU.AppendixSurreals.Asymptotics

/-!
# QOU.AppendixSurreals.SpectralNormalForm — conjecture carrier

**§3b-cond class axiomatisation** for content block
[`conj:spectral-normal-form`](../../../appendix-surreals/spectral-normal-form.md):
*Spectral gap closure and singularity formation as `q → 1` read from normal-form
exponents*.

Primary conjecture carrier with **no instance** — the honest open state per
AGENTS.md §3b-tax.

## What changed (bean `qou-ffwk`)

The previous field schema was a scalar plus a field asserting that it vanishes,
inhabited by `⟨0, rfl⟩`. The class chose its own witness, so it asserted nothing
and a downstream `[SpectralNormalForm]` hypothesis was not a meaningful
conditional.

Unlike the three carriers refined before it, this one needed **no invented
types**: `SurrealField`, `IsInfinitesimal`, `IsFinite` and `OmegaOrder.Ow` all
already exist in this library, so the conjecture can be stated in the corpus's
own vocabulary rather than against caller-supplied stand-ins.

## What the conjecture actually says

The block states three parts. What they share, and what makes them a
conjecture rather than a definition, is a **bridge between two independent
structures on `K`**: the *order* (infinitesimal, finite — from
`SurrealField`'s `LinearOrder`) and the *valuation* (`Ow`, the leading Conway
exponent). `OmegaOrder` axiomatises `Ow`'s multiplicativity and its behaviour
under real rescaling and **says nothing relating it to the order**. The
conjecture is exactly that relation:

* **Part 1 (gap closure).** "The gap `Δ` closes in the classical limit iff
  `Ow(Δ) < 0` (i.e. `Δ` is infinitesimal)" — the block's own "i.e." identifies
  closure with being infinitesimal, so the content is
  `IsInfinitesimal x ↔ Ow x < 0`.
* **Part 3 (singularity formation).** "A divergence has `Ow(λ) > 0`" — a value
  blows up exactly when it fails to be finite, so the content is
  `¬ IsFinite x ↔ Ow x > 0`.

Both are stated for `x ≠ 0`, and that side condition is **load-bearing rather
than decorative**: `0` is infinitesimal (`zero_isInfinitesimal`) while
`Ow 0 = ⊤` by `Ow_zero`, and `⊤` is not `< 0`. Without the hypothesis part 1 is
outright false at zero. The same applies to part 3, where `0` is finite and `⊤`
is `> 0`.

**Part 2 is deliberately not a field.** It reads off *rates* — `Ow(Δ) = -1` is
linear closure, `Ow(Δ) = -n` polynomial of order `n`, and a value strictly
between `-ω·2` and `-ω` signals transcendental quantum-dilogarithm behaviour.
That is a classification of the exponent once parts 1 and 3 are granted, not an
independent assertion, and encoding a rate table as class fields would claim the
classification is part of what must be assumed.

## Anti-vacuity: what the class forces that `OmegaOrder` does not

`Ow_normalises_on_ofReal` below derives, from the two fields, that `Ow` is
**exactly `0`** on every non-zero embedded real. That is not available from
`OmegaOrder` alone: its `Ow_ofReal_mul` says rescaling by a non-zero real leaves
the leading exponent *unchanged*, which is a statement about differences and
never pins an absolute value. So the class genuinely adds content, and an
instance cannot be produced by fixing up `Ow` on a whim.

**No non-emptiness witness is supplied, and what blocks it has narrowed.**
When this carrier was written, `OmegaOrder` had no instance anywhere, so the
missing piece was the valuation itself. That half is now closed: bean `qou-x20w`
generalised `OmegaOrder` to carry its exponent group separately and populated it
from Mathlib's Hahn series (`HahnOmegaOrder.lean`), so the valuation axioms are
demonstrably consistent.

What remains is the **other** hypothesis. This class also needs
`IsInfinitesimal` and `IsFinite`, hence `[SurrealField K]` — and `SurrealField`
requires `omegaSurreal` exceeding every natural, so no archimedean carrier can
serve and the Hahn model does not qualify either.
`HyperrealLimitTransfer.lean` has a `SurrealField ℝ*` model, but as a `def`
rather than an instance, and with no `Ow` for it.

So satisfiability is still untested in either direction, but the gap is now one
construction — a non-archimedean ordered field carrying both a birthday function
and a leading-exponent valuation — rather than two. Recorded rather than papered
over with a degenerate instance.

## Base ring (§7c)

`K` is a generic `[SurrealField K]`. `ℝ` enters only through
`SurrealField.ofReal`, the embedding that is part of the structure itself, and
through `IsInfinitesimal`'s comparison against embedded reals — both inherited
from the corpus's own definitions rather than introduced here. No numerical
substrate value appears, and nothing is compared against a measured quantity.
-/

namespace QOU.AppendixSurreals

open SurrealField OmegaOrder

universe u w

/-- **Spectral normal form**: the surreal order and the ω-adic valuation agree
about smallness and largeness.

The conjecture of
[`conj:spectral-normal-form`](../../../appendix-surreals/spectral-normal-form.md),
which is what lets spectral gap closure and singularity formation as `q → 1` be
read directly off leading exponents, with no analytic limit.

`K` is the caller's surreal carrier together with its ω-adic order. An instance
**is** the conjecture, for that carrier. None is provided — and see the header:
no `OmegaOrder` instance exists anywhere in this tree, so the class has not been
exhibited satisfiable either. -/
class SpectralNormalForm (K : Type u) [SurrealField K]
    (Γ : Type w) [AddCommMonoid Γ] [LinearOrder Γ] [OmegaOrder K ℝ Γ] : Prop where
  /-- **Part 1 — gap closure.** A non-zero value is infinitesimal exactly when
      its leading exponent is negative. Applied to `Δ = λ₂ − λ₁`, this is
      "the gap closes in the classical limit iff `Ow(Δ) < 0`".

      The hypothesis `x ≠ 0` is load-bearing: `0` is infinitesimal but has
      `Ow 0 = ⊤`, so the biconditional is false there. -/
  infinitesimal_iff_Ow_neg :
    ∀ x : K, x ≠ 0 → (IsInfinitesimal x ↔ Ow (S := ℝ) (Γ := Γ) x < (0 : WithTop Γ))
  /-- **Part 3 — singularity formation.** A non-zero value fails to be finite
      exactly when its leading exponent is positive. Applied to an eigenvalue,
      this is "a divergence has `Ow(λ) > 0`", and the exponent is what
      classifies the divergence type.

      The hypothesis `x ≠ 0` is load-bearing for the same reason. -/
  not_finite_iff_Ow_pos :
    ∀ x : K, x ≠ 0 → (¬ IsFinite x ↔ (0 : WithTop Γ) < Ow (S := ℝ) (Γ := Γ) x)

-- **No instance is provided — that is the honest open state** (AGENTS.md
-- §3b-tax).  History: this file previously carried
--     axiom conj_spectral_normal_form : SpectralNormalForm
--     noncomputable instance : SpectralNormalForm := conj_spectral_normal_form
-- i.e. the conjecture was asserted by `axiom` and installed as a global
-- instance, so every downstream `[SpectralNormalForm]` resolved for free and
-- the assumption was invisible outside `#print axioms`.  Removed, not
-- completed.  The field schema is now content-bearing as well; see the header.
--
-- Note for `qou-ffwk`'s inventory: that bean greps for the old vanishing
-- field's name, which is deliberately written nowhere in this file — not even
-- in this history — so the file drops out of the grep instead of matching it
-- forever from its own changelog.

namespace SpectralNormalForm

variable {K : Type u} [SurrealField K]
  {Γ : Type w} [AddCommMonoid Γ] [LinearOrder Γ] [OmegaOrder K ℝ Γ]

/-- **The class pins `Ow` on the embedded reals** — anti-vacuity.

For non-zero `r : ℝ`, both fields fire and force `Ow (ofReal r) = 0` exactly.
`OmegaOrder` alone cannot give this: `Ow_ofReal_mul` says rescaling by a
non-zero real leaves the leading exponent unchanged, which constrains
differences and never fixes an absolute value.

So the two fields are not inert decoration — they have a consequence that
constrains `Ow` on a set the caller does not choose, and an instance cannot be
manufactured by adjusting `Ow` freely. -/
theorem Ow_normalises_on_ofReal [h : SpectralNormalForm K Γ] (r : ℝ) (hr : r ≠ 0) :
    Ow (S := ℝ) (Γ := Γ) (ofReal r : K) = (0 : WithTop Γ) := by
  have hne : (ofReal r : K) ≠ 0 := fun hz =>
    hr ((map_eq_zero_iff _ (ofReal_strictMono (K := K)).injective).mp hz)
  have hnotinf : ¬ IsInfinitesimal (ofReal r : K) := fun hinf =>
    hr ((ofReal_isInfinitesimal_iff_eq_zero (K := K) r).mp hinf)
  have hfin : IsFinite (ofReal r : K) := ofReal_isFinite r
  have h1 := (h.infinitesimal_iff_Ow_neg _ hne)
  have h3 := (h.not_finite_iff_Ow_pos _ hne)
  have hlt : ¬ (Ow (S := ℝ) (Γ := Γ) (ofReal r : K) < (0 : WithTop Γ)) := fun hc => hnotinf (h1.mpr hc)
  have hgt : ¬ ((0 : WithTop Γ) < Ow (S := ℝ) (Γ := Γ) (ofReal r : K)) := fun hc => (h3.mpr hc) hfin
  exact le_antisymm (not_lt.mp hgt) (not_lt.mp hlt)

/-- **The two parts are about the same value at most one way.**

A non-zero value cannot be both infinitesimal and non-finite: parts 1 and 3
would put its leading exponent strictly below and strictly above `0`. Exercises
both fields together, and is the statement that the conjecture is internally
coherent rather than describing two unrelated regimes. -/
theorem not_infinitesimal_and_not_finite [h : SpectralNormalForm K Γ]
    (x : K) (hx : x ≠ 0) : ¬ (IsInfinitesimal x ∧ ¬ IsFinite x) := by
  rintro ⟨hinf, hnfin⟩
  have hneg : Ow (S := ℝ) (Γ := Γ) x < (0 : WithTop Γ) := (h.infinitesimal_iff_Ow_neg x hx).mp hinf
  have hpos : (0 : WithTop Γ) < Ow (S := ℝ) (Γ := Γ) x := (h.not_finite_iff_Ow_pos x hx).mp hnfin
  exact absurd (hneg.trans hpos) (lt_irrefl _)

/-- **Every non-zero infinitesimal element is finite under `SpectralNormalForm`.** -/
theorem isFinite_of_isInfinitesimal [h : SpectralNormalForm K Γ]
    (x : K) (hx : x ≠ 0) (hinf : IsInfinitesimal x) : IsFinite x := by
  by_contra hnfin
  exact not_infinitesimal_and_not_finite (h := h) x hx ⟨hinf, hnfin⟩

/-- **Complete valuation characterisation of the finite non-infinitesimal regime.**
    A non-zero surreal element has leading exponent `Ow x = 0` if and only if it
    is finite and not infinitesimal. -/
theorem Ow_zero_iff_finite_and_not_infinitesimal [h : SpectralNormalForm K Γ]
    (x : K) (hx : x ≠ 0) :
    Ow (S := ℝ) (Γ := Γ) x = (0 : WithTop Γ) ↔ (IsFinite x ∧ ¬ IsInfinitesimal x) := by
  have h1 := h.infinitesimal_iff_Ow_neg x hx
  have h3 := h.not_finite_iff_Ow_pos x hx
  constructor
  · intro h0
    refine ⟨?_, ?_⟩
    · by_contra hnfin
      have hpos := h3.mp hnfin
      rw [h0] at hpos
      exact lt_irrefl _ hpos
    · intro hinf
      have hneg := h1.mp hinf
      rw [h0] at hneg
      exact lt_irrefl _ hneg
  · rintro ⟨hfin, hninf⟩
    have hlt : ¬ (Ow (S := ℝ) (Γ := Γ) x < (0 : WithTop Γ)) :=
      fun hc => hninf (h1.mpr hc)
    have hgt : ¬ ((0 : WithTop Γ) < Ow (S := ℝ) (Γ := Γ) x) :=
      fun hc => (h3.mpr hc) hfin
    exact le_antisymm (not_lt.mp hgt) (not_lt.mp hlt)

end SpectralNormalForm

end QOU.AppendixSurreals
