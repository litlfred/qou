import QOU.StandardModel.ColourStabilizerAction
import QOU.Core.OctonionSU3RankSix

/-!
# QOU.StandardModel.ColourOnSingleFibreThreeStrands — colour cannot act on the single-fibre three-strand space compatibly with braiding and the fibre gauge group

`conj:sm-colour-stabilizer-action` asks for a faithful action of the colour algebra
`𝔰𝔲(3)` (the octonion stabilizer, dimension `8`) on "the three-strand state space".  Its
Lean class `ColourStabilizerAction g V` asks only for an injective **linear** map
`g →ₗ End V`.  This module makes two points precise.

1. **As formalised, the class is a dimension count.**  `colourStabilizerAction_of_finrank_le`:
   whenever `finrank g ≤ (finrank V)²` an instance exists.  For the single-fibre three-strand
   space `V^{⊗3} = ℚ⁸` (`dim V = 2`) it holds trivially (`8 ≤ 64`).  So an instance says
   nothing about colour.
2. **With the compatibility the physics needs, it fails.**  Model `V^{⊗3}` at `q = 1` by
   `Fin 8 → ℚ` (basis `|abc⟩`, `a, b, c ∈ {0, 1}`).  The braiding acts through the slot
   swaps `P₁₂, P₂₃` (the `q = 1` Hecke generators) and the fibre gauge algebra `𝔰𝔩₂` through
   the raising and lowering operators `Eₜ, Fₜ` (the coproduct on three slots).  An operator
   that commutes with all four lies in the span of two explicit matrices
   (`commutant_eq_combination`).  The commutant has dimension `≤ 2 < 8`, so **no injective
   linear map from `𝔰𝔲(3)` lands in it** (`no_colour_action_commuting_with_braiding_and_su2`).

So colour cannot act on the single-fibre three-strand states while commuting with both the
braiding and the fibre gauge group.  This is a scope-(b) exclusion with the invariant named:
the commutant of `S₃ × 𝔰𝔩₂` on `(ℚ²)^{⊗3}` is the two-dimensional algebra of the
multiplicity-free decomposition `V^{⊗3} = S^{(3)} ⊗ V_{3/2} ⊕ S^{(2,1)} ⊗ V_{1/2}`.  For
comparison (computed by exact linear algebra, not formalised here): the commutant of `𝔰𝔩₂`
alone already has dimension `5 < 8`, so commuting with the fibre gauge algebra is by itself
enough for the dimension exclusion; the commutant of the braiding alone,
`End(S³V) ⊕ End(V)`, has dimension `20`, and a dimension count does not exclude it.

Classical (`q = 1`) statement; base `ℚ`; no empirical input.
-/

namespace QOU.StandardModel.ColourOnSingleFibre

open Module

/-! ## 1. The class is a dimension count -/

/-- If `finrank g ≤ (finrank V)²` then `ColourStabilizerAction g V` holds: any
finite-dimensional space embeds linearly in one of at least its dimension. -/
theorem colourStabilizerAction_of_finrank_le
    (g : Type*) [AddCommGroup g] [Module ℚ g] [FiniteDimensional ℚ g]
    (V : Type*) [AddCommGroup V] [Module ℚ V] [FiniteDimensional ℚ V]
    (h : finrank ℚ g ≤ finrank ℚ V * finrank ℚ V) :
    ColourStabilizerAction g V := by
  have hEnd : finrank ℚ (Module.End ℚ V) = finrank ℚ V * finrank ℚ V :=
    Module.finrank_linearMap ℚ ℚ V V
  have h' : finrank ℚ g ≤ finrank ℚ (Module.End ℚ V) := hEnd ▸ h
  set a := finrank ℚ g
  set b := finrank ℚ (Module.End ℚ V)
  let eg : g ≃ₗ[ℚ] (Fin a → ℚ) := LinearEquiv.ofFinrankEq _ _ (by simp [a])
  let eE : Module.End ℚ V ≃ₗ[ℚ] (Fin b → ℚ) := LinearEquiv.ofFinrankEq _ _ (by simp [b])
  let ι : (Fin a → ℚ) →ₗ[ℚ] (Fin b → ℚ) :=
    { toFun := fun x k => if hk : k.1 < a then x ⟨k.1, hk⟩ else 0
      map_add' := by intro x y; funext k; by_cases hk : k.1 < a <;> simp [hk]
      map_smul' := by intro c x; funext k; by_cases hk : k.1 < a <;> simp [hk] }
  have hι : Function.Injective ι := by
    intro x y hxy
    funext i
    have := congrFun hxy (Fin.castLE h' i)
    simpa [ι, i.2] using this
  obtain ⟨Φ, hΦ⟩ : ∃ Φ : g →ₗ[ℚ] Module.End ℚ V, Function.Injective Φ :=
    ⟨eE.symm.toLinearMap ∘ₗ ι ∘ₗ eg.toLinearMap,
      eE.symm.injective.comp (hι.comp eg.injective)⟩
  exact ⟨⟨Φ, hΦ⟩⟩

/-! ## 2. The single-fibre three-strand space at `q = 1` -/

/-- Swap of slots 1 and 2 on `(ℚ²)^{⊗3}`, basis `|abc⟩ ↦ index 4a + 2b + c`. -/
def P₁₂ : Matrix (Fin 8) (Fin 8) ℚ :=
  !![(1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ)]

/-- Swap of slots 2 and 3. -/
def P₂₃ : Matrix (Fin 8) (Fin 8) ℚ :=
  !![(1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ)]

/-- The `𝔰𝔩₂` raising operator on three slots, `e ⊗ 1 ⊗ 1 + 1 ⊗ e ⊗ 1 + 1 ⊗ 1 ⊗ e`. -/
def Eₜ : Matrix (Fin 8) (Fin 8) ℚ :=
  !![(0 : ℚ), (1 : ℚ), (1 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ), (1 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ)]

/-- The `𝔰𝔩₂` lowering operator on three slots. -/
def Fₜ : Matrix (Fin 8) (Fin 8) ℚ :=
  !![(0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (1 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (1 : ℚ), (1 : ℚ), (0 : ℚ)]

/-- First spanning element of the commutant. -/
def B₀ : Matrix (Fin 8) (Fin 8) ℚ :=
  !![(0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (1 : ℚ), ((-1/2) : ℚ), (0 : ℚ), ((-1/2) : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), ((-1/2) : ℚ), (1 : ℚ), (0 : ℚ), ((-1/2) : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), ((-1/2) : ℚ), ((-1/2) : ℚ), (0 : ℚ);
    (0 : ℚ), ((-1/2) : ℚ), ((-1/2) : ℚ), (0 : ℚ), (1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), ((-1/2) : ℚ), (0 : ℚ), (1 : ℚ), ((-1/2) : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), ((-1/2) : ℚ), (0 : ℚ), ((-1/2) : ℚ), (1 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ)]

/-- Second spanning element of the commutant. -/
def B₁ : Matrix (Fin 8) (Fin 8) ℚ :=
  !![(1 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (1/2 : ℚ), (0 : ℚ), (1/2 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (1/2 : ℚ), (0 : ℚ), (0 : ℚ), (1/2 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (1/2 : ℚ), (1/2 : ℚ), (0 : ℚ);
    (0 : ℚ), (1/2 : ℚ), (1/2 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (1/2 : ℚ), (0 : ℚ), (0 : ℚ), (1/2 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (1/2 : ℚ), (0 : ℚ), (1/2 : ℚ), (0 : ℚ), (0 : ℚ);
    (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (0 : ℚ), (1 : ℚ)]

set_option linter.unusedSimpArgs false in
set_option linter.unreachableTactic false in
set_option linter.unnecessarySeqFocus false in
set_option maxHeartbeats 4000000 in
/-- **The commutant of braiding and `𝔰𝔩₂` is two-dimensional.**  An operator commuting with
`P₁₂, P₂₃, Eₜ, Fₜ` is `X₆₆ • B₀ + X₇₇ • B₁`.  Certificate: exact Gaussian elimination
over `ℚ`. -/
theorem commutant_eq_combination (X : Matrix (Fin 8) (Fin 8) ℚ)
    (h12 : X * P₁₂ = P₁₂ * X) (h23 : X * P₂₃ = P₂₃ * X)
    (hE : X * Eₜ = Eₜ * X) (hF : X * Fₜ = Fₜ * X) :
    X = X 6 6 • B₀ + X 7 7 • B₁ := by
  ext i j
  fin_cases i <;> fin_cases j
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (-1/2) * (congrFun (congrFun h12 1) 2) + -(congrFun (congrFun h12 2) 1) + -(congrFun (congrFun h12 3) 3) + (-1/2) * (congrFun (congrFun h12 3) 6) + (-2) * (congrFun (congrFun h23 1) 1) + (congrFun (congrFun hE 0) 1) + (congrFun (congrFun hE 1) 3) + (1/2) * (congrFun (congrFun hE 1) 6) + (congrFun (congrFun hE 3) 7)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (-1/3) * (congrFun (congrFun h12 0) 2) + (-2/3) * (congrFun (congrFun h23 0) 1) + (1/3) * (congrFun (congrFun hF 0) 0)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (-1/3) * (congrFun (congrFun h12 0) 2) + (1/3) * (congrFun (congrFun h23 0) 1) + (1/3) * (congrFun (congrFun hF 0) 0)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (-1/2) * (congrFun (congrFun h12 0) 3) + (1/2) * (congrFun (congrFun hF 0) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (2/3) * (congrFun (congrFun h12 0) 2) + (1/3) * (congrFun (congrFun h23 0) 1) + (1/3) * (congrFun (congrFun hF 0) 0)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/2) * (congrFun (congrFun h12 0) 3) + (1/2) * (congrFun (congrFun hF 0) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/2) * (congrFun (congrFun h12 0) 3) + (congrFun (congrFun h23 0) 5) + (1/2) * (congrFun (congrFun hF 0) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (congrFun (congrFun hF 0) 3)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/3) * (congrFun (congrFun h12 2) 0) + (2/3) * (congrFun (congrFun h23 1) 0) + (-1/3) * (congrFun (congrFun hE 0) 0)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/2) * (congrFun (congrFun h12 1) 2) + -(congrFun (congrFun h12 3) 3) + (congrFun (congrFun h12 3) 5) + (1/2) * (congrFun (congrFun h12 3) 6) + -(congrFun (congrFun h23 3) 5) + (congrFun (congrFun h23 5) 6) + (congrFun (congrFun hE 1) 3) + (-1/2) * (congrFun (congrFun hE 1) 6)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (-1/2) * (congrFun (congrFun h12 1) 2) + (-1/2) * (congrFun (congrFun h12 3) 5) + (-1/2) * (congrFun (congrFun h12 3) 6) + (1/2) * (congrFun (congrFun h23 3) 5) + (-1/2) * (congrFun (congrFun h23 5) 6) + (1/2) * (congrFun (congrFun hE 1) 6) + (1/2) * (congrFun (congrFun hE 3) 7)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (-1/6) * (congrFun (congrFun h12 0) 2) + (-1/2) * (congrFun (congrFun h12 1) 3) + (-1/3) * (congrFun (congrFun h23 0) 1) + (1/6) * (congrFun (congrFun hF 0) 0) + (1/2) * (congrFun (congrFun hF 1) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/2) * (congrFun (congrFun h12 1) 2) + (-1/2) * (congrFun (congrFun h12 3) 5) + (-1/2) * (congrFun (congrFun h12 3) 6) + (1/2) * (congrFun (congrFun h23 3) 5) + (-1/2) * (congrFun (congrFun h23 5) 6) + (1/2) * (congrFun (congrFun hE 1) 6) + (1/2) * (congrFun (congrFun hE 3) 7)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (-1/6) * (congrFun (congrFun h12 0) 2) + (1/2) * (congrFun (congrFun h12 1) 3) + (-1/3) * (congrFun (congrFun h23 0) 1) + (1/6) * (congrFun (congrFun hF 0) 0) + (1/2) * (congrFun (congrFun hF 1) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (-1/3) * (congrFun (congrFun h12 0) 2) + (congrFun (congrFun h12 1) 3) + (congrFun (congrFun h12 2) 3) + (1/3) * (congrFun (congrFun h23 0) 1) + (congrFun (congrFun h23 1) 3) + (congrFun (congrFun h23 1) 5) + -(congrFun (congrFun hE 0) 3) + (1/3) * (congrFun (congrFun hF 0) 0) + -(congrFun (congrFun hF 1) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/6) * (congrFun (congrFun h12 0) 3) + (1/3) * (congrFun (congrFun h12 2) 7) + (1/3) * (congrFun (congrFun h23 0) 5) + (2/3) * (congrFun (congrFun h23 1) 7) + (-1/3) * (congrFun (congrFun hE 0) 7) + (1/2) * (congrFun (congrFun hF 0) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/3) * (congrFun (congrFun h12 2) 0) + (-1/3) * (congrFun (congrFun h23 1) 0) + (-1/3) * (congrFun (congrFun hE 0) 0)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (-1/2) * (congrFun (congrFun h12 1) 2) + (-1/2) * (congrFun (congrFun h12 3) 5) + (-1/2) * (congrFun (congrFun h12 3) 6) + -(congrFun (congrFun h23 1) 1) + (1/2) * (congrFun (congrFun h23 3) 5) + (-1/2) * (congrFun (congrFun h23 5) 6) + (1/2) * (congrFun (congrFun hE 1) 6) + (1/2) * (congrFun (congrFun hE 3) 7)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/2) * (congrFun (congrFun h12 1) 2) + -(congrFun (congrFun h12 3) 3) + (congrFun (congrFun h12 3) 5) + (1/2) * (congrFun (congrFun h12 3) 6) + -(congrFun (congrFun h23 1) 2) + -(congrFun (congrFun h23 3) 5) + (congrFun (congrFun h23 5) 6) + (congrFun (congrFun hE 1) 3) + (-1/2) * (congrFun (congrFun hE 1) 6)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (-1/6) * (congrFun (congrFun h12 0) 2) + (-1/2) * (congrFun (congrFun h12 1) 3) + (-1/3) * (congrFun (congrFun h23 0) 1) + -(congrFun (congrFun h23 1) 3) + (1/6) * (congrFun (congrFun hF 0) 0) + (1/2) * (congrFun (congrFun hF 1) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/2) * (congrFun (congrFun h12 1) 2) + (-1/2) * (congrFun (congrFun h12 3) 5) + (-1/2) * (congrFun (congrFun h12 3) 6) + -(congrFun (congrFun h23 1) 4) + (1/2) * (congrFun (congrFun h23 3) 5) + (-1/2) * (congrFun (congrFun h23 5) 6) + (1/2) * (congrFun (congrFun hE 1) 6) + (1/2) * (congrFun (congrFun hE 3) 7)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (-1/3) * (congrFun (congrFun h12 0) 2) + (congrFun (congrFun h12 1) 3) + (congrFun (congrFun h12 2) 3) + (1/3) * (congrFun (congrFun h23 0) 1) + (congrFun (congrFun h23 1) 3) + -(congrFun (congrFun hE 0) 3) + (1/3) * (congrFun (congrFun hF 0) 0) + -(congrFun (congrFun hF 1) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (-1/6) * (congrFun (congrFun h12 0) 2) + (1/2) * (congrFun (congrFun h12 1) 3) + (-1/3) * (congrFun (congrFun h23 0) 1) + -(congrFun (congrFun h23 1) 6) + (1/6) * (congrFun (congrFun hF 0) 0) + (1/2) * (congrFun (congrFun hF 1) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/6) * (congrFun (congrFun h12 0) 3) + (1/3) * (congrFun (congrFun h12 2) 7) + (1/3) * (congrFun (congrFun h23 0) 5) + (-1/3) * (congrFun (congrFun h23 1) 7) + (-1/3) * (congrFun (congrFun hE 0) 7) + (1/2) * (congrFun (congrFun hF 0) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/2) * (congrFun (congrFun h12 3) 0) + (-1/2) * (congrFun (congrFun hE 1) 0)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/6) * (congrFun (congrFun h12 2) 0) + (1/2) * (congrFun (congrFun h12 3) 1) + (1/3) * (congrFun (congrFun h23 1) 0) + (-1/6) * (congrFun (congrFun hE 0) 0) + (-1/2) * (congrFun (congrFun hE 1) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/6) * (congrFun (congrFun h12 2) 0) + (1/2) * (congrFun (congrFun h12 3) 1) + (1/3) * (congrFun (congrFun h23 1) 0) + (congrFun (congrFun h23 3) 1) + (-1/6) * (congrFun (congrFun hE 0) 0) + (-1/2) * (congrFun (congrFun hE 1) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (congrFun (congrFun h12 3) 5) + (congrFun (congrFun h23 5) 6)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/6) * (congrFun (congrFun h12 2) 0) + (-1/2) * (congrFun (congrFun h12 3) 1) + (congrFun (congrFun h12 3) 2) + (1/3) * (congrFun (congrFun h23 1) 0) + -(congrFun (congrFun h23 3) 1) + (-1/6) * (congrFun (congrFun hE 0) 0) + (1/2) * (congrFun (congrFun hE 1) 1) + -(congrFun (congrFun hE 1) 2)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (-1/2) * (congrFun (congrFun h12 3) 5) + (-1/2) * (congrFun (congrFun h23 3) 5) + (-1/2) * (congrFun (congrFun h23 5) 6) + (1/2) * (congrFun (congrFun hE 3) 7)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (-1/2) * (congrFun (congrFun h12 3) 5) + (1/2) * (congrFun (congrFun h23 3) 5) + (-1/2) * (congrFun (congrFun h23 5) 6) + (1/2) * (congrFun (congrFun hE 3) 7)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (-1/3) * (congrFun (congrFun h12 0) 2) + (1/2) * (congrFun (congrFun h12 1) 3) + (1/2) * (congrFun (congrFun h12 2) 3) + (1/2) * (congrFun (congrFun h12 3) 7) + (-1/6) * (congrFun (congrFun h23 0) 1) + (1/2) * (congrFun (congrFun h23 1) 3) + (1/2) * (congrFun (congrFun h23 1) 5) + (-1/2) * (congrFun (congrFun hE 0) 3) + (-1/2) * (congrFun (congrFun hE 1) 7) + (1/3) * (congrFun (congrFun hF 0) 0)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (-2/3) * (congrFun (congrFun h12 2) 0) + (-1/3) * (congrFun (congrFun h23 1) 0) + (-1/3) * (congrFun (congrFun hE 0) 0)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (-1/2) * (congrFun (congrFun h12 1) 2) + -(congrFun (congrFun h12 2) 1) + (-1/2) * (congrFun (congrFun h12 3) 5) + (-1/2) * (congrFun (congrFun h12 3) 6) + -(congrFun (congrFun h23 1) 1) + (1/2) * (congrFun (congrFun h23 3) 5) + (-1/2) * (congrFun (congrFun h23 5) 6) + (1/2) * (congrFun (congrFun hE 1) 6) + (1/2) * (congrFun (congrFun hE 3) 7)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/2) * (congrFun (congrFun h12 1) 2) + -(congrFun (congrFun h12 2) 2) + (-1/2) * (congrFun (congrFun h12 3) 5) + (-1/2) * (congrFun (congrFun h12 3) 6) + -(congrFun (congrFun h23 1) 4) + (1/2) * (congrFun (congrFun h23 3) 5) + (-1/2) * (congrFun (congrFun h23 5) 6) + (1/2) * (congrFun (congrFun hE 1) 6) + (1/2) * (congrFun (congrFun hE 3) 7)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (-1/3) * (congrFun (congrFun h12 0) 2) + (congrFun (congrFun h12 1) 3) + (1/3) * (congrFun (congrFun h23 0) 1) + (congrFun (congrFun h23 1) 3) + -(congrFun (congrFun hE 0) 3) + (1/3) * (congrFun (congrFun hF 0) 0) + -(congrFun (congrFun hF 1) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/2) * (congrFun (congrFun h12 1) 2) + -(congrFun (congrFun h12 2) 4) + -(congrFun (congrFun h12 3) 3) + (congrFun (congrFun h12 3) 5) + (1/2) * (congrFun (congrFun h12 3) 6) + -(congrFun (congrFun h23 1) 2) + -(congrFun (congrFun h23 3) 5) + (congrFun (congrFun h23 5) 6) + (congrFun (congrFun hE 1) 3) + (-1/2) * (congrFun (congrFun hE 1) 6)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (-1/6) * (congrFun (congrFun h12 0) 2) + (-1/2) * (congrFun (congrFun h12 1) 3) + -(congrFun (congrFun h12 2) 5) + (-1/3) * (congrFun (congrFun h23 0) 1) + -(congrFun (congrFun h23 1) 3) + (1/6) * (congrFun (congrFun hF 0) 0) + (1/2) * (congrFun (congrFun hF 1) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (-1/6) * (congrFun (congrFun h12 0) 2) + (1/2) * (congrFun (congrFun h12 1) 3) + -(congrFun (congrFun h12 2) 6) + (-1/3) * (congrFun (congrFun h23 0) 1) + -(congrFun (congrFun h23 1) 6) + (1/6) * (congrFun (congrFun hF 0) 0) + (1/2) * (congrFun (congrFun hF 1) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/6) * (congrFun (congrFun h12 0) 3) + (-2/3) * (congrFun (congrFun h12 2) 7) + (1/3) * (congrFun (congrFun h23 0) 5) + (-1/3) * (congrFun (congrFun h23 1) 7) + (-1/3) * (congrFun (congrFun hE 0) 7) + (1/2) * (congrFun (congrFun hF 0) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (-1/2) * (congrFun (congrFun h12 3) 0) + (-1/2) * (congrFun (congrFun hE 1) 0)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/6) * (congrFun (congrFun h12 2) 0) + (-1/2) * (congrFun (congrFun h12 3) 1) + (1/3) * (congrFun (congrFun h23 1) 0) + (-1/6) * (congrFun (congrFun hE 0) 0) + (-1/2) * (congrFun (congrFun hE 1) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/6) * (congrFun (congrFun h12 2) 0) + (-1/2) * (congrFun (congrFun h12 3) 1) + (1/3) * (congrFun (congrFun h23 1) 0) + -(congrFun (congrFun h23 3) 1) + (-1/6) * (congrFun (congrFun hE 0) 0) + (1/2) * (congrFun (congrFun hE 1) 1) + -(congrFun (congrFun hE 1) 2)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      -(congrFun (congrFun h12 3) 3) + (-1/2) * (congrFun (congrFun h12 3) 5) + (-1/2) * (congrFun (congrFun h23 3) 5) + (-1/2) * (congrFun (congrFun h23 5) 6) + (1/2) * (congrFun (congrFun hE 3) 7)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/6) * (congrFun (congrFun h12 2) 0) + (1/2) * (congrFun (congrFun h12 3) 1) + -(congrFun (congrFun h12 3) 4) + (1/3) * (congrFun (congrFun h23 1) 0) + (congrFun (congrFun h23 3) 1) + (-1/6) * (congrFun (congrFun hE 0) 0) + (-1/2) * (congrFun (congrFun hE 1) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (congrFun (congrFun h23 5) 6)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (-1/2) * (congrFun (congrFun h12 3) 5) + -(congrFun (congrFun h12 3) 6) + (1/2) * (congrFun (congrFun h23 3) 5) + (-1/2) * (congrFun (congrFun h23 5) 6) + (1/2) * (congrFun (congrFun hE 3) 7)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (-1/3) * (congrFun (congrFun h12 0) 2) + (1/2) * (congrFun (congrFun h12 1) 3) + (1/2) * (congrFun (congrFun h12 2) 3) + (-1/2) * (congrFun (congrFun h12 3) 7) + (-1/6) * (congrFun (congrFun h23 0) 1) + (1/2) * (congrFun (congrFun h23 1) 3) + (1/2) * (congrFun (congrFun h23 1) 5) + (-1/2) * (congrFun (congrFun hE 0) 3) + (-1/2) * (congrFun (congrFun hE 1) 7) + (1/3) * (congrFun (congrFun hF 0) 0)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (-1/2) * (congrFun (congrFun h12 3) 0) + -(congrFun (congrFun h23 5) 0) + (-1/2) * (congrFun (congrFun hE 1) 0)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/6) * (congrFun (congrFun h12 2) 0) + (-1/2) * (congrFun (congrFun h12 3) 1) + (1/3) * (congrFun (congrFun h23 1) 0) + -(congrFun (congrFun h23 3) 1) + -(congrFun (congrFun h23 5) 1) + (-1/6) * (congrFun (congrFun hE 0) 0) + (1/2) * (congrFun (congrFun hE 1) 1) + -(congrFun (congrFun hE 1) 2)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/6) * (congrFun (congrFun h12 2) 0) + (-1/2) * (congrFun (congrFun h12 3) 1) + (1/3) * (congrFun (congrFun h23 1) 0) + -(congrFun (congrFun h23 5) 2) + (-1/6) * (congrFun (congrFun hE 0) 0) + (-1/2) * (congrFun (congrFun hE 1) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      -(congrFun (congrFun h12 3) 3) + (-1/2) * (congrFun (congrFun h12 3) 5) + (-1/2) * (congrFun (congrFun h23 3) 5) + -(congrFun (congrFun h23 5) 3) + (-1/2) * (congrFun (congrFun h23 5) 6) + (1/2) * (congrFun (congrFun hE 3) 7)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/6) * (congrFun (congrFun h12 2) 0) + (-1/2) * (congrFun (congrFun h12 3) 1) + (congrFun (congrFun h12 6) 2) + (1/3) * (congrFun (congrFun h23 1) 0) + -(congrFun (congrFun h23 5) 2) + (-1/6) * (congrFun (congrFun hE 0) 0) + (-1/2) * (congrFun (congrFun hE 1) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      -(congrFun (congrFun h12 3) 3) + (-1/2) * (congrFun (congrFun h12 3) 5) + (congrFun (congrFun h12 6) 3) + (-1/2) * (congrFun (congrFun h23 3) 5) + -(congrFun (congrFun h23 5) 3) + (-1/2) * (congrFun (congrFun h23 5) 6) + (1/2) * (congrFun (congrFun hE 3) 7)
  · simp [B₀, B₁]
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (-1/3) * (congrFun (congrFun h12 0) 2) + (1/2) * (congrFun (congrFun h12 1) 3) + (1/2) * (congrFun (congrFun h12 2) 3) + (-1/2) * (congrFun (congrFun h12 3) 7) + (-1/6) * (congrFun (congrFun h23 0) 1) + (1/2) * (congrFun (congrFun h23 1) 3) + (1/2) * (congrFun (congrFun h23 1) 5) + -(congrFun (congrFun h23 5) 7) + (-1/2) * (congrFun (congrFun hE 0) 3) + (-1/2) * (congrFun (congrFun hE 1) 7) + (1/3) * (congrFun (congrFun hF 0) 0)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      -(congrFun (congrFun hE 3) 0)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/2) * (congrFun (congrFun h12 3) 0) + (-1/2) * (congrFun (congrFun hE 1) 0) + -(congrFun (congrFun hE 3) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/2) * (congrFun (congrFun h12 3) 0) + (congrFun (congrFun h23 7) 1) + (-1/2) * (congrFun (congrFun hE 1) 0) + -(congrFun (congrFun hE 3) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/3) * (congrFun (congrFun h12 2) 0) + (congrFun (congrFun h12 3) 1) + (2/3) * (congrFun (congrFun h23 1) 0) + (congrFun (congrFun h23 3) 1) + (-1/3) * (congrFun (congrFun hE 0) 0) + -(congrFun (congrFun hE 1) 1) + -(congrFun (congrFun hE 3) 3)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/2) * (congrFun (congrFun h12 3) 0) + (congrFun (congrFun h12 7) 2) + (congrFun (congrFun h23 7) 1) + (-1/2) * (congrFun (congrFun hE 1) 0) + -(congrFun (congrFun hE 3) 1)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/3) * (congrFun (congrFun h12 2) 0) + (congrFun (congrFun h12 3) 1) + (congrFun (congrFun h12 7) 3) + (2/3) * (congrFun (congrFun h23 1) 0) + (congrFun (congrFun h23 3) 1) + (-1/3) * (congrFun (congrFun hE 0) 0) + -(congrFun (congrFun hE 1) 1) + -(congrFun (congrFun hE 3) 3)
  · linear_combination (norm := (simp [Matrix.mul_apply, Fin.sum_univ_eight, P₁₂, P₂₃, Eₜ, Fₜ, B₀, B₁, Matrix.add_apply, Matrix.smul_apply] <;> ring1))
      (1/3) * (congrFun (congrFun h12 2) 0) + (congrFun (congrFun h12 3) 1) + (congrFun (congrFun h12 7) 3) + (2/3) * (congrFun (congrFun h23 1) 0) + (congrFun (congrFun h23 3) 1) + (congrFun (congrFun h23 7) 5) + (-1/3) * (congrFun (congrFun hE 0) 0) + -(congrFun (congrFun hE 1) 1) + -(congrFun (congrFun hE 3) 3)
  · simp [B₀, B₁]

/-- The commutant of the braiding and the fibre gauge algebra on `(ℚ²)^{⊗3}`. -/
def commutant : Submodule ℚ (Matrix (Fin 8) (Fin 8) ℚ) where
  carrier := {X | X * P₁₂ = P₁₂ * X ∧ X * P₂₃ = P₂₃ * X ∧ X * Eₜ = Eₜ * X ∧ X * Fₜ = Fₜ * X}
  add_mem' := by
    rintro X Y ⟨a1, a2, a3, a4⟩ ⟨b1, b2, b3, b4⟩
    refine ⟨?_, ?_, ?_, ?_⟩ <;> simp only [add_mul, mul_add, *]
  zero_mem' := by simp
  smul_mem' := by
    rintro c X ⟨a1, a2, a3, a4⟩
    refine ⟨?_, ?_, ?_, ?_⟩ <;> simp only [Matrix.smul_mul, Matrix.mul_smul, *]

theorem commutant_le_span : commutant ≤ Submodule.span ℚ {B₀, B₁} := by
  rintro X ⟨h12, h23, hE, hF⟩
  rw [commutant_eq_combination X h12 h23 hE hF]
  exact Submodule.add_mem _
    (Submodule.smul_mem _ _ (Submodule.subset_span (by simp)))
    (Submodule.smul_mem _ _ (Submodule.subset_span (by simp)))

theorem finrank_commutant_le_two : finrank ℚ commutant ≤ 2 := by
  calc finrank ℚ commutant ≤ finrank ℚ (Submodule.span ℚ ({B₀, B₁} : Set _)) :=
        Submodule.finrank_mono commutant_le_span
    _ ≤ ({B₀, B₁} : Finset _).card := by
        simpa using finrank_span_finset_le_card ({B₀, B₁} : Finset (Matrix (Fin 8) (Fin 8) ℚ))
    _ ≤ 2 := Finset.card_le_two

open QOU.MathlibExt.OctonionDerivations in
/-- **No colour action on single-fibre three-strand states compatible with braiding and the
fibre gauge group.**  No injective linear map sends the colour algebra `su3 e₁` (dimension
`8`) into operators on `(ℚ²)^{⊗3}` that commute with the slot swaps and with `𝔰𝔩₂`. -/
theorem no_colour_action_commuting_with_braiding_and_su2 :
    ¬ ∃ Φ : ↥(su3 (Pi.single 1 1)) →ₗ[ℚ] commutant, Function.Injective Φ := by
  rintro ⟨Φ, hΦ⟩
  have h8 := finrank_su3_e1
  have := LinearMap.finrank_le_finrank_of_injective hΦ
  have := finrank_commutant_le_two
  omega

end QOU.StandardModel.ColourOnSingleFibre
