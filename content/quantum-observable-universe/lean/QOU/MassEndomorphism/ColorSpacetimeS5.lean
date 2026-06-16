import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Logic.Equiv.Basic
import Mathlib.Logic.Equiv.Fin.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Arg

/-!
# Color–spacetime `S₅` factorization (investigation Lean)

Formal backbone for the mass-trace phase synthesis
([`docs/audits/2026-06-16-mass-trace-phase-c5-vs-u1.md`]).

On the categorical Markov trace `tr_M` of a Bring-embeddable knot:

* **mass** `= |tr_M|` (modulus);
* **EM** `= arg tr_M` — a continuous `U(1)` framing / Chern–Simons phase
  (the `Im 𝔙` channel), living in the *spacetime* sector;
* **color** `=` the discrete `S₃` irrep grading, living in the *color* sector.

The Bring substrate has 5 homogeneous coordinates split
`(x₀,x₁) = spacetime | (x₂,x₃,x₄) = color`
(`brings-qou-4tuple.md`), the trace algebra is `H₂(q) ⊕ H₃(q)` with
`2 + 3 = 5` irreps (`cohomological-embedding.md`), and the Galois group is
`S₅ ⊇ S₂ × S₃`. The owner's structural point: the `S₃` (color) embeds into
`S₅` **fixing the spacetime block** — so color and EM are orthogonal at the
`S₂ × S₃` level, and "color from within EM" is an `S₅` statement (the
generators outside `S₂ × S₃`), not a `U(1)` statement.

This file proves the two clean, decisive pieces:
1. `S₂ × S₃ ↪ S₅` is injective, and the color factor fixes spacetime;
2. the polar decomposition `tr = |tr|·exp(i·arg tr)` (mass = modulus,
   EM = phase, on one scalar).
-/

namespace QOU.MassEndomorphism

open Equiv

/-! ## 1. The `2 + 3 = 5` index split (spacetime ⊕ color) -/

/-- The Bring index decomposition `(spacetime ⊕ color) ≃ Fin 5`. -/
abbrev brIdx : Fin 2 ⊕ Fin 3 ≃ Fin 5 := finSumFinEquiv

theorem spacetime_color_card : Fintype.card (Fin 2 ⊕ Fin 3) = 5 := by decide

/-! ## 2. `S₂ × S₃ ↪ S₅`, color factor fixes spacetime -/

/-- The Galois embedding `S₂ × S₃ → S₅`: block-permute spacetime ⊕ color,
    then relabel `Fin 2 ⊕ Fin 3 ≃ Fin 5`. -/
def colorSpacetimeEmbed : Perm (Fin 2) × Perm (Fin 3) → Perm (Fin 5) :=
  fun p => brIdx.permCongr (Equiv.Perm.sumCongrHom (Fin 2) (Fin 3) p)

/-- `S₂ × S₃` embeds in `S₅`: the factorization is faithful. -/
theorem colorSpacetimeEmbed_injective :
    Function.Injective colorSpacetimeEmbed := by
  intro a b h
  apply Equiv.Perm.sumCongrHom_injective
  exact brIdx.permCongr.injective h

/-- **Color fixes spacetime.** With the spacetime factor trivial, the color
    permutation `τ ∈ S₃` acts as a permutation of `Fin 5` that fixes every
    spacetime index `brIdx (Sum.inl i)` (`i : Fin 2`). This is the formal
    content of "the `S₃ ⊂ S₅` keeps the spacetime coordinates invariant". -/
theorem color_fixes_spacetime (τ : Perm (Fin 3)) (i : Fin 2) :
    colorSpacetimeEmbed (1, τ) (brIdx (Sum.inl i)) = brIdx (Sum.inl i) := by
  simp [colorSpacetimeEmbed, Equiv.permCongr_apply, Equiv.Perm.sumCongrHom]

/-- Conversely the spacetime factor `S₂` moves spacetime indices and fixes
    color indices — the two sectors are orthogonal inside `S₅`. -/
theorem spacetime_fixes_color (ρ : Perm (Fin 2)) (j : Fin 3) :
    colorSpacetimeEmbed (ρ, 1) (brIdx (Sum.inr j)) = brIdx (Sum.inr j) := by
  simp [colorSpacetimeEmbed, Equiv.permCongr_apply, Equiv.Perm.sumCongrHom]

/-! ## 3. mass = modulus, EM = phase (polar decomposition of the trace) -/

/-- **Polar decomposition of the trace scalar.** `tr_M = |tr_M|·exp(i·arg)`:
    the modulus is mass, the argument is the `U(1)` (EM / framing) phase.
    Together they reconstruct the one complex trace — the multiplicative
    companion of the additive `Re + i·Im = 𝔙` reconstruction
    (`complex_volume_unification`). -/
theorem trace_polar (z : ℂ) :
    (‖z‖ : ℂ) * Complex.exp (Complex.arg z * Complex.I) = z :=
  Complex.norm_mul_exp_arg_mul_I z

/-- The two observable shadows of the trace scalar are independent
    coordinates: mass `‖z‖ ≥ 0` (modulus) and EM phase `arg z ∈ (-π, π]`. -/
theorem mass_nonneg (z : ℂ) : 0 ≤ ‖z‖ := norm_nonneg z

theorem em_phase_mem (z : ℂ) : Complex.arg z ∈ Set.Ioc (-Real.pi) Real.pi :=
  ⟨Complex.neg_pi_lt_arg z, Complex.arg_le_pi z⟩

end QOU.MassEndomorphism
