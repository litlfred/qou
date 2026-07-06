import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Logic.Equiv.Basic
import Mathlib.Logic.Equiv.Fin.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Arg
import Mathlib.GroupTheory.OrderOfElement

/-!
# Color–spacetime `S₅` factorization of the mass trace

Formalisation of [`prop:color-spacetime-s5-factorization`](color-spacetime-s5-factorization.md).

On the categorical Markov trace `tr_M` of a Bring-embeddable knot, three
observables are three structures on the *one* trace object `H₂(q) ⊕ H₃(q)`
(whose `2 + 3 = 5` irreducible representations are the Bring fivefold):

* **mass** `= ‖tr_M‖` — the modulus;
* **electromagnetism** `= arg tr_M` — a continuous `U(1)` framing /
  Chern–Simons phase (the imaginary channel of the complex volume `𝔙`),
  carried by the *spacetime* sector;
* **color** `=` the discrete `S₃` irreducible-representation grading,
  carried by the *color* sector.

Bring's five homogeneous coordinates split as
`(x₀,x₁) = spacetime | (x₂,x₃,x₄) = color`, and the substrate Galois group
is `S₅ ⊇ S₂ × S₃`. The factorisation is faithful and the color factor fixes
the spacetime coordinates: color and electromagnetism are orthogonal at the
`S₂ × S₃` level, so the discrete color label is not a function of the
continuous phase. They are related only by the `S₅` generators outside
`S₂ × S₃`.

The final section proves the **discreteness gate**: a continuous winding
phase cannot factor through a finite group, so `arg tr_M` (nonzero winding)
is never a color character. This is the formal statement that closes
"color ≠ phase".

Ref: [jones1985] https://doi.org/10.2307/1971403
Ref: [neumann-zagier1985] https://doi.org/10.1016/0040-9383(85)90004-7
-/

namespace QOU.MassEndomorphism

open Equiv

/-! ## 1. The `2 + 3 = 5` index split (spacetime ⊕ color) -/

/-- The Bring index decomposition `(spacetime ⊕ color) ≃ Fin 5`. -/
abbrev brIdx : Fin 2 ⊕ Fin 3 ≃ Fin 5 := finSumFinEquiv

/-- The trace algebra `H₂ ⊕ H₃` carries `2 + 3 = 5` irreps — the Bring
    fivefold. -/
theorem spacetime_color_card : Fintype.card (Fin 2 ⊕ Fin 3) = 5 := by decide

/-! ## 2. `S₂ × S₃ ↪ S₅`, with the color factor fixing spacetime -/

/-- The Galois embedding `S₂ × S₃ → S₅`: block-permute spacetime ⊕ color,
    then relabel along `Fin 2 ⊕ Fin 3 ≃ Fin 5`. -/
def colorSpacetimeEmbed : Perm (Fin 2) × Perm (Fin 3) → Perm (Fin 5) :=
  fun p => brIdx.permCongr (Equiv.Perm.sumCongrHom (Fin 2) (Fin 3) p)

/-- **The factorisation is faithful:** `S₂ × S₃ ↪ S₅`. -/
theorem colorSpacetimeEmbed_injective :
    Function.Injective colorSpacetimeEmbed := by
  intro a b h
  apply Equiv.Perm.sumCongrHom_injective
  exact brIdx.permCongr.injective h

/-- **Color fixes spacetime.** With the spacetime factor trivial, the color
    permutation `τ ∈ S₃` acts on `Fin 5` fixing every spacetime index
    `brIdx (Sum.inl i)`. This is "the `S₃ ⊂ S₅` keeps the spacetime
    coordinates invariant". -/
theorem color_fixes_spacetime (τ : Perm (Fin 3)) (i : Fin 2) :
    colorSpacetimeEmbed (1, τ) (brIdx (Sum.inl i)) = brIdx (Sum.inl i) := by
  simp [colorSpacetimeEmbed, Equiv.permCongr_apply, Equiv.Perm.sumCongrHom]

/-- **Spacetime fixes color.** Dually, the spacetime factor `S₂` fixes every
    color index — the two sectors are orthogonal inside `S₅`. -/
theorem spacetime_fixes_color (ρ : Perm (Fin 2)) (j : Fin 3) :
    colorSpacetimeEmbed (ρ, 1) (brIdx (Sum.inr j)) = brIdx (Sum.inr j) := by
  simp [colorSpacetimeEmbed, Equiv.permCongr_apply, Equiv.Perm.sumCongrHom]

/-! ## 3. mass = modulus, electromagnetism = phase (polar decomposition) -/

/-- **Polar decomposition of the trace scalar.** `tr_M = ‖tr_M‖·exp(i·arg)`:
    the modulus is mass, the argument is the `U(1)` electromagnetic / framing
    phase. The multiplicative companion of the additive `Re + i·Im = 𝔙`
    reconstruction (`complex_volume_unification`). -/
theorem trace_polar (z : ℂ) :
    (‖z‖ : ℂ) * Complex.exp (Complex.arg z * Complex.I) = z :=
  Complex.norm_mul_exp_arg_mul_I z

/-- mass is a nonnegative modulus. -/
theorem mass_nonneg (z : ℂ) : 0 ≤ ‖z‖ := norm_nonneg z

/-- the electromagnetic phase lies in `(-π, π]`. -/
theorem em_phase_mem (z : ℂ) : Complex.arg z ∈ Set.Ioc (-Real.pi) Real.pi :=
  ⟨Complex.neg_pi_lt_arg z, Complex.arg_le_pi z⟩

/-! ## 4. The discreteness gate: color ≠ phase

A continuous winding phase is an additive character of the connected
parameter `ℝ`; the discrete color label is a character valued in a *finite*
group `μ₅`. The two cannot coincide, because every additive homomorphism
from the divisible group `ℝ` to a finite group is trivial. -/

/-- **Discreteness gate.** Any additive homomorphism from `ℝ` (the connected
    winding parameter) to a finite group is trivial. The continuous
    framing / Chern–Simons winding cannot factor through the finite color
    group. -/
theorem winding_hom_to_finite_trivial
    {G : Type*} [AddCommGroup G] [Finite G] (f : ℝ →+ G) : f = 0 := by
  haveI : Fintype G := Fintype.ofFinite G
  haveI : Nonempty G := ⟨0⟩
  ext x
  have hc : (Fintype.card G : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr Fintype.card_ne_zero
  have hx : (Fintype.card G) • (x / (Fintype.card G : ℝ)) = x := by
    rw [nsmul_eq_mul]; field_simp
  calc f x = f ((Fintype.card G) • (x / (Fintype.card G : ℝ))) := by rw [hx]
    _ = (Fintype.card G) • f (x / (Fintype.card G : ℝ)) := by rw [map_nsmul]
    _ = 0 := by rw [card_nsmul_eq_zero]
