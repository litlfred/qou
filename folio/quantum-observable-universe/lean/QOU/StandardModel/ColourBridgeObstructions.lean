import QOU.MathlibExt.OctonionColourActionBaseModule
import QOU.MathlibExt.OctonionComplexStructure
import Mathlib.LinearAlgebra.Determinant
import Mathlib.LinearAlgebra.LinearIndependent.Lemmas

set_option maxHeartbeats 4000000
set_option maxSynthPendingDepth 5

/-!
# QOU.StandardModel.ColourBridgeObstructions — what a bridge between the two SU(3)s needs

Bean `qou-cb3r` (parent `qou-8lxd`). Audit:
`docs/audits/2026-11-15-colour-stabilizer-bridge.md`.

`conj:sm-colour-stabilizer-action` asks for a faithful action of the octonion colour stabilizer
`su3 e = ker (D ↦ D e) ⊂ Der 𝕆` on the framework's three-strand state space. The corpus already
records (`OctonionColourActionBaseModule`) that the abstract class is satisfied tautologically by
`𝕆` itself. This file proves three further facts that decide what an honest bridge to the
**tower** side (the level-3 `gl₃` Jimbo action on `V^{⊗n}`, `V = ℚ³`) must supply.

1. **The class cannot tell a bridge from a selection.** `colourStabilizerAction_of_finrank_le`:
   whenever `finrank g ≤ (finrank V)²` an instance exists, built from bases alone. So an instance
   on the tower's `V = ℚ³` (`8 ≤ 9`) is free and carries no information; closing the class on the
   tower side proves nothing. The dimension obstruction already in the corpus
   (`not_colourStabilizerAction_of_dim_sq_lt`) is therefore sharp: the class is equivalent to
   `finrank g ≤ (finrank V)²`.

2. **The tower's colour triplet has no complex structure; the octonion one does.**
   `no_complex_structure_of_odd_finrank`: on a space of odd dimension over an ordered field there
   is no `J` with `J ∘ J = −1` (determinant: `det(J)² = (−1)^{odd} = −1`). The tower fundamental
   `ℚ³` is odd-dimensional; the octonion colour triplet is the 6-dimensional `ℚ`-space `ℂ³_e`
   with `J = L_e` (`Le_sq_eq_neg_id`). So no `ℚ`-linear isomorphism between them can intertwine
   a complex structure: a bridge must first complexify the tower fundamental.

3. **The octonion side does not fix which complex structure.** `su3_neg`: `su3 (−e) = su3 e`, and
   `Le_neg_ne` with `negLe_commutes`: `−L_e = L_{−e}` is a second complex structure, different
   from `L_e`, commuting with the same stabilizer. The stabilizer determines the line `ℚe` but not
   its orientation, i.e. not which of `3`, `3̄` is the quark triplet. Matching it to the tower's
   strand orientation is a one-bit choice (charge conjugation), recorded in the audit.

## Base ring (§7c)

Results 1 and 3 over `ℚ` (the corpus's octonion carrier); result 2 over a generic linearly
ordered field `K`, since it needs only `det(J)² ≥ 0`.

LaTeX label: `prop:colour-bridge-obstructions`
-/

namespace QOU.StandardModel.ColourBridgeObstructions

open Module QOU.StandardModel QOU.MathlibExt.OctonionDerivations

/-! ### 1. The class is equivalent to a dimension inequality -/

/-- **Any `g` with `finrank g ≤ (finrank V)²` acts faithfully on `V`**, by a map built from bases
only. Together with `not_colourStabilizerAction_of_dim_sq_lt` this makes
`ColourStabilizerAction g V` equivalent to `finrank g ≤ (finrank V)²`: the class records a
dimension count, not a bridge. -/
theorem colourStabilizerAction_of_finrank_le
    (g : Type*) [AddCommGroup g] [Module ℚ g] [FiniteDimensional ℚ g]
    (V : Type*) [AddCommGroup V] [Module ℚ V] [FiniteDimensional ℚ V]
    (h : finrank ℚ g ≤ finrank ℚ V * finrank ℚ V) :
    ColourStabilizerAction g V := by
  have hE : finrank ℚ (V →ₗ[ℚ] V) = finrank ℚ V * finrank ℚ V :=
    Module.finrank_linearMap ℚ ℚ V V
  have h' : finrank ℚ g ≤ finrank ℚ (V →ₗ[ℚ] V) := hE ▸ h
  let bg := Module.finBasis ℚ g
  let bE := Module.finBasis ℚ (V →ₗ[ℚ] V)
  let f : g →ₗ[ℚ] (V →ₗ[ℚ] V) := bg.constr ℚ (fun i => bE (Fin.castLE h' i))
  refine ⟨⟨f, ?_⟩⟩
  apply LinearMap.injective_of_linearIndependent (v := bg) bg.span_eq
  have hcomp : (f ∘ bg) = bE ∘ Fin.castLE h' := by
    funext i
    simp [f, Basis.constr_basis]
  rw [hcomp]
  exact bE.linearIndependent.comp _ (Fin.castLE_injective h')

/-- The tower's colour triplet `ℚ³` already satisfies the class for any 8-dimensional colour
algebra, with no reference to octonions or to the Hecke structure. -/
theorem colourStabilizerAction_on_three
    (g : Type*) [AddCommGroup g] [Module ℚ g] [FiniteDimensional ℚ g] (h8 : finrank ℚ g = 8) :
    ColourStabilizerAction g (Fin 3 → ℚ) := by
  apply colourStabilizerAction_of_finrank_le
  simp [h8]

/-! ### 2. No complex structure in odd dimension -/

/-- **No complex structure on an odd-dimensional space** over a linearly ordered field:
`det(J)² = det(J ∘ J) = det(−1) = (−1)^{dim} = −1` is impossible. -/
theorem no_complex_structure_of_odd_finrank
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {V : Type*} [AddCommGroup V] [Module K V] [FiniteDimensional K V]
    (hodd : Odd (finrank K V)) (J : V →ₗ[K] V) :
    J ∘ₗ J ≠ -LinearMap.id := by
  intro hJ
  have h := congrArg LinearMap.det hJ
  have hneg : (-LinearMap.id : V →ₗ[K] V) = (-1 : K) • LinearMap.id := by simp
  rw [LinearMap.det_comp, hneg, LinearMap.det_smul, LinearMap.det_id, mul_one,
    hodd.neg_one_pow] at h
  nlinarith [sq_nonneg (LinearMap.det J)]

/-- The tower's colour triplet `ℚ³` carries no complex structure. -/
theorem tower_triplet_no_complex_structure (J : (Fin 3 → ℚ) →ₗ[ℚ] (Fin 3 → ℚ)) :
    J ∘ₗ J ≠ -LinearMap.id :=
  no_complex_structure_of_odd_finrank (by simp) J

/-! ### 3. The stabilizer does not fix the orientation of `e` -/

/-- **`su3 (−e) = su3 e`**: a derivation kills `−e` iff it kills `e`. -/
theorem su3_neg (e : Fin 8 → ℚ) : su3 (-e) = su3 e := by
  ext D
  simp only [mem_su3_iff, map_neg, neg_eq_zero]

/-- Left multiplication by `−e` is `−L_e`: the second complex structure is `L_{−e}`. -/
theorem octMulₗ_neg (e : Fin 8 → ℚ) : octMulₗ (-e) = -octMulₗ e :=
  map_neg octMulₗ e

/-- `−L_e` is also a complex structure. -/
theorem negLe_sq_eq_neg_id : (-Le) ∘ₗ (-Le) = -LinearMap.id := by
  rw [LinearMap.neg_comp, LinearMap.comp_neg, neg_neg, Le_sq_eq_neg_id]

/-- Every element of the stabilizer of `e₁` commutes with `−L_{e₁}` as well as with `L_{e₁}`. -/
theorem negLe_commutes {D : Der𝕆} (hD : D ∈ su3 stdIm) :
    D.1 ∘ₗ (-Le) = (-Le) ∘ₗ D.1 := by
  rw [LinearMap.comp_neg, LinearMap.neg_comp, su3_comp_Le_eq_Le_comp hD]

/-- The two complex structures are different. -/
theorem Le_neg_ne : Le ≠ -Le := by
  intro h
  have h2 : Le ∘ₗ Le = -(Le ∘ₗ Le) := by
    conv_lhs => rw [h]
    rw [LinearMap.neg_comp]
  rw [Le_sq_eq_neg_id, neg_neg] at h2
  have := LinearMap.congr_fun h2 (Pi.single 0 1)
  have h0 := congrFun this 0
  simp at h0
  norm_num at h0

end QOU.StandardModel.ColourBridgeObstructions
