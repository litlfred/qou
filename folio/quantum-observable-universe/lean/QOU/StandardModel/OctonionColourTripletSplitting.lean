import QOU.MathlibExt.OctonionComplexStructure
import QOU.MathlibExt.OctonionDerivationProperties
import QOU.MathlibExt.OctonionColourActionBaseModule

/-!
# QOU.StandardModel.OctonionColourTripletSplitting — `Le`-Stable `1 ⊕ 3` Splitting `ℂ ⊕ ℂ³`
# and Faithful 6D Colour-Triplet Representation of `𝔰𝔲(3)`

This module establishes the `1 ⊕ 3` block decomposition of the Dubois-Violette–Todorov
octonionic colour geometry built on `QOU.MathlibExt.OctonionComplexStructure`:

1. **Section 1 — Orthogonal Projections `projSinglet` (`P₁`) and `projTriplet` (`P₃`)**:
   Splits the 8-dimensional rational octonion space `𝕆 = (Fin 8 → ℚ)` into the 2-dimensional
   colour-singlet plane `span(e₀, e₁) ≅ ℂ` and the 6-dimensional colour-triplet subspace
   `span(e₂, …, e₇) ≅ ℂ³`, establishing idempotency, mutual orthogonality, and completeness
   (`P₁² = P₁`, `P₃² = P₃`, `P₁ P₃ = P₃ P₁ = 0`, `P₁ + P₃ = id`).
2. **Section 2 — `Le`-Stability (`ℂ`-Linearity) of the `1 ⊕ 3` Splitting**:
   Left multiplication by the fixed imaginary unit `Le = octMulₗ stdIm` (`Le² = -id`) commutes
   with both `projSinglet` and `projTriplet` (`Le ∘ₗ P₁ = P₁ ∘ₗ Le` and `Le ∘ₗ P₃ = P₃ ∘ₗ Le`),
   so both `singletSubmodule` and `tripletSubmodule` are `Le`-invariant complex subspaces.
3. **Section 3 — Singlet Annihilation and Faithful `ℂ`-Linear 6D Colour-Triplet Restriction**:
   From the Leibniz rule (`derivation_annihilates_one`) and the anticommutator identity
   `e₁ · P₃(v) + P₃(v) · e₁ = 0`, every colour derivation `D ∈ su3 stdIm` annihilates the 2D
   singlet (`D ∘ₗ P₁ = 0`) and maps `𝕆` strictly into the 6D triplet (`P₁ ∘ₗ D = 0`,
   `P₃ ∘ₗ D = D`, `D ∘ₗ P₃ = D`). The restriction homomorphism
   `su3ToEndTriplet : ↥(su3 stdIm) →ₗ[ℚ] Module.End ℚ (Fin 6 → ℚ)` is injective
   (`su3ToEndTriplet_injective`), instantiates `ColourStabilizerAction` and
   `ColourStabilizerActionOnSU3 stdIm` on `(Fin 6 → ℚ)`, commutes with the induced 6D complex
   structure `J6` (`J6² = -id`, `su3ToEndTriplet_comm_J6`), and preserves the commutator Lie
   bracket (`su3ToEndTriplet_bracket`).

Base ring `ℚ`; exact rational linear algebra, nothing archimedean.
-/

namespace QOU.StandardModel

open QOU.MathlibExt.OctonionDerivations
open QOU.MathlibExt.DerivationRankNullity

/-! ## Section 1: Orthogonal Projections `projSinglet` (`1`) and `projTriplet` (`3`) -/

/-- Projection `P₁` onto the 2D colour-singlet subspace `span(e₀, e₁) ≅ ℂ` (indices `0, 1`). -/
def projSinglet : (Fin 8 → ℚ) →ₗ[ℚ] (Fin 8 → ℚ) where
  toFun v k := if k.1 < 2 then v k else 0
  map_add' u v := by
    funext k; dsimp; split_ifs <;> ring
  map_smul' c v := by
    funext k; dsimp; split_ifs <;> ring

/-- Projection `P₃` onto the 6D colour-triplet subspace `span(e₂, …, e₇) ≅ ℂ³` (indices `2..7`). -/
def projTriplet : (Fin 8 → ℚ) →ₗ[ℚ] (Fin 8 → ℚ) where
  toFun v k := if k.1 < 2 then 0 else v k
  map_add' u v := by
    funext k; dsimp; split_ifs <;> ring
  map_smul' c v := by
    funext k; dsimp; split_ifs <;> ring

@[simp] theorem projSinglet_apply (v : Fin 8 → ℚ) (k : Fin 8) :
    projSinglet v k = if k.1 < 2 then v k else 0 := rfl

@[simp] theorem projTriplet_apply (v : Fin 8 → ℚ) (k : Fin 8) :
    projTriplet v k = if k.1 < 2 then 0 else v k := rfl

/-- `projSinglet` is idempotent: `P₁ ∘ P₁ = P₁`. -/
theorem projSinglet_comp_self : projSinglet ∘ₗ projSinglet = projSinglet := by
  apply LinearMap.ext; intro v; funext k; dsimp; split_ifs <;> rfl

/-- `projTriplet` is idempotent: `P₃ ∘ P₃ = P₃`. -/
theorem projTriplet_comp_self : projTriplet ∘ₗ projTriplet = projTriplet := by
  apply LinearMap.ext; intro v; funext k; dsimp; split_ifs <;> rfl

/-- Mutual orthogonality `P₁ ∘ P₃ = 0`. -/
theorem projSinglet_comp_projTriplet : projSinglet ∘ₗ projTriplet = 0 := by
  apply LinearMap.ext; intro v; funext k; dsimp; split_ifs <;> rfl

/-- Mutual orthogonality `P₃ ∘ P₁ = 0`. -/
theorem projTriplet_comp_projSinglet : projTriplet ∘ₗ projSinglet = 0 := by
  apply LinearMap.ext; intro v; funext k; dsimp; split_ifs <;> rfl

/-- Completeness of the `1 ⊕ 3` decomposition: `P₁ + P₃ = id`. -/
theorem projSinglet_add_projTriplet : projSinglet + projTriplet = LinearMap.id := by
  apply LinearMap.ext; intro v; funext k
  change projSinglet v k + projTriplet v k = v k
  dsimp [projSinglet, projTriplet]
  split_ifs <;> ring

/-- Pointwise completeness: `projSinglet v + projTriplet v = v`. -/
theorem projSinglet_apply_add_projTriplet_apply (v : Fin 8 → ℚ) :
    projSinglet v + projTriplet v = v := by
  have h := LinearMap.congr_fun projSinglet_add_projTriplet v
  exact h

/-! ## Section 2: `Le`-Stability (`ℂ`-Linearity) of the `1 ⊕ 3` Splitting -/

/-- Left multiplication `Le` by `stdIm = e₁` commutes with `projSinglet`. -/
theorem Le_comp_projSinglet : Le ∘ₗ projSinglet = projSinglet ∘ₗ Le := by
  apply LinearMap.ext
  intro v
  funext k
  change octMul stdIm (projSinglet v) k = projSinglet (octMul stdIm v) k
  fin_cases k <;>
    (dsimp [octMul, stdIm, projSinglet]; ring)

/-- Left multiplication `Le` by `stdIm = e₁` commutes with `projTriplet`. -/
theorem Le_comp_projTriplet : Le ∘ₗ projTriplet = projTriplet ∘ₗ Le := by
  apply LinearMap.ext
  intro v
  funext k
  change octMul stdIm (projTriplet v) k = projTriplet (octMul stdIm v) k
  fin_cases k <;>
    (dsimp [octMul, stdIm, projTriplet]; ring)

/-- The 2D colour-singlet subspace `span(e₀, e₁) = range(P₁)`. -/
def singletSubmodule : Submodule ℚ (Fin 8 → ℚ) := LinearMap.range projSinglet

/-- The 6D colour-triplet subspace `span(e₂, …, e₇) = range(P₃)`. -/
def tripletSubmodule : Submodule ℚ (Fin 8 → ℚ) := LinearMap.range projTriplet

/-- `singletSubmodule` is `Le`-invariant (`ℂ`-subspace). -/
theorem Le_mem_singletSubmodule {v : Fin 8 → ℚ} (hv : v ∈ singletSubmodule) :
    Le v ∈ singletSubmodule := by
  rcases hv with ⟨u, rfl⟩
  refine ⟨Le u, ?_⟩
  exact (LinearMap.congr_fun Le_comp_projSinglet u).symm

/-- `tripletSubmodule` is `Le`-invariant (`ℂ`-subspace). -/
theorem Le_mem_tripletSubmodule {v : Fin 8 → ℚ} (hv : v ∈ tripletSubmodule) :
    Le v ∈ tripletSubmodule := by
  rcases hv with ⟨u, rfl⟩
  refine ⟨Le u, ?_⟩
  exact (LinearMap.congr_fun Le_comp_projTriplet u).symm

/-! ## Section 3: Annihilation of the Singlet `1` and Faithful 6D Colour-Triplet Restriction -/

/-- The real unit octonion `e₀ = 1` as `Pi.single 0 1`. -/
def stdReal : Fin 8 → ℚ := Pi.single 0 1

/-- Every derivation `D ∈ Der𝕆` annihilates `stdReal = e₀`. -/
theorem der_apply_stdReal_eq_zero (D : Der𝕆) : D.1 stdReal = 0 :=
  derivation_annihilates_one D.2

/-- Every colour derivation `D ∈ su3 stdIm` annihilates the fixed imaginary unit `e₁ = stdIm`. -/
theorem su3_apply_stdIm_eq_zero {D : Der𝕆} (hD : D ∈ su3 stdIm) : D.1 stdIm = 0 :=
  mem_su3_iff.mp hD

/-- Explicit expansion of `projSinglet v` in the singlet basis `{e₀, e₁}`:
`projSinglet v = v₀ • stdReal + v₁ • stdIm`. -/
theorem projSinglet_eq_linComb (v : Fin 8 → ℚ) :
    projSinglet v = v 0 • stdReal + v 1 • stdIm := by
  funext k
  fin_cases k <;>
    simp [projSinglet, stdReal, stdIm]

/-- **Singlet annihilation (`D ∘ P₁ = 0`)**: every colour derivation `D ∈ su3 stdIm` acts
by zero on the 2D singlet subspace `ℂ = span(e₀, e₁)`. -/
theorem D_comp_projSinglet_eq_zero {D : Der𝕆} (hD : D ∈ su3 stdIm) :
    D.1 ∘ₗ projSinglet = 0 := by
  apply LinearMap.ext
  intro v
  change D.1 (projSinglet v) = 0
  rw [projSinglet_eq_linComb v, map_add, map_smul, map_smul,
    der_apply_stdReal_eq_zero D, su3_apply_stdIm_eq_zero hD]
  simp

/-- Consequently, `D ∘ P₃ = D` for every `D ∈ su3 stdIm`. -/
theorem D_comp_projTriplet_eq_self {D : Der𝕆} (hD : D ∈ su3 stdIm) :
    D.1 ∘ₗ projTriplet = D.1 := by
  apply LinearMap.ext
  intro v
  change D.1 (projTriplet v) = D.1 v
  have h1 : D.1 (projSinglet v) = 0 := LinearMap.congr_fun (D_comp_projSinglet_eq_zero hD) v
  have h2 := congrArg D.1 (projSinglet_apply_add_projTriplet_apply v)
  rw [map_add, h1, zero_add] at h2
  exact h2

/-- **Anticommutativity of `stdIm` with the 6D triplet**: every vector `projTriplet v` in
`span(e₂, …, e₇)` anticommutes with `e₁ = stdIm` under the octonion product. -/
theorem octMul_stdIm_add_comm_projTriplet (v : Fin 8 → ℚ) :
    octMul stdIm (projTriplet v) + octMul (projTriplet v) stdIm = 0 := by
  funext k
  change octMul stdIm (projTriplet v) k + octMul (projTriplet v) stdIm k = 0
  fin_cases k <;>
    (dsimp [octMul, stdIm, projTriplet]; ring)

/-- For any octonion `w`, coordinate `0` of the anticommutator `e₁·w + w·e₁` is `-2 w₁`. -/
theorem octMul_stdIm_add_comm_apply_zero (w : Fin 8 → ℚ) :
    (octMul stdIm w + octMul w stdIm) 0 = -2 * w 1 := by
  change octMul stdIm w 0 + octMul w stdIm 0 = -2 * w 1
  dsimp [octMul, stdIm]
  ring

/-- For any octonion `w`, coordinate `1` of the anticommutator `e₁·w + w·e₁` is `2 w₀`. -/
theorem octMul_stdIm_add_comm_apply_one (w : Fin 8 → ℚ) :
    (octMul stdIm w + octMul w stdIm) 1 = 2 * w 0 := by
  change octMul stdIm w 1 + octMul w stdIm 1 = 2 * w 0
  dsimp [octMul, stdIm]
  ring

/-- If `w` anticommutes with `stdIm` (`e₁·w + w·e₁ = 0`), then `w 0 = 0` and `w 1 = 0`. -/
theorem singlet_coords_eq_zero_of_anticomm_stdIm {w : Fin 8 → ℚ}
    (hw : octMul stdIm w + octMul w stdIm = 0) : w 0 = 0 ∧ w 1 = 0 := by
  have h0 : (octMul stdIm w + octMul w stdIm) 0 = 0 := by rw [hw]; rfl
  have h1 : (octMul stdIm w + octMul w stdIm) 1 = 0 := by rw [hw]; rfl
  rw [octMul_stdIm_add_comm_apply_zero] at h0
  rw [octMul_stdIm_add_comm_apply_one] at h1
  constructor <;> linarith

/-- Every colour derivation `D ∈ su3 stdIm` maps `𝕆` into vectors anticommuting with `stdIm`. -/
theorem su3_anticomm_stdIm_of_projTriplet {D : Der𝕆} (hD : D ∈ su3 stdIm) (v : Fin 8 → ℚ) :
    octMul stdIm (D.1 v) + octMul (D.1 v) stdIm = 0 := by
  have hleib : ∀ x y : Fin 8 → ℚ,
      D.1 (octMulₗ x y) = octMulₗ (D.1 x) y + octMulₗ x (D.1 y) :=
    mem_ker_leibnizDefect_iff.mp D.2
  have he : D.1 stdIm = 0 := su3_apply_stdIm_eq_zero hD
  have hDv : D.1 v = D.1 (projTriplet v) :=
    (LinearMap.congr_fun (D_comp_projTriplet_eq_self hD) v).symm
  rw [hDv]
  have hanti := octMul_stdIm_add_comm_projTriplet v
  have hDanti : D.1 (octMul stdIm (projTriplet v) + octMul (projTriplet v) stdIm) = 0 := by
    rw [hanti, map_zero]
  have h1 := hleib stdIm (projTriplet v)
  have h2 := hleib (projTriplet v) stdIm
  simp only [octMulₗ_apply] at h1 h2
  have h0R : ∀ u : Fin 8 → ℚ, octMul u 0 = 0 := fun u => LinearMap.map_zero (octMulₗ u)
  rw [map_add, h1, h2, he, octMul_zero_left, h0R, zero_add, add_zero] at hDanti
  exact hDanti

/-- **Image stability (`P₁ ∘ D = 0`)**: for every `D ∈ su3 stdIm`, the image of `D.1` has
vanishing singlet coordinates (`(D v)₀ = (D v)₁ = 0`). -/
theorem projSinglet_comp_D_eq_zero {D : Der𝕆} (hD : D ∈ su3 stdIm) :
    projSinglet ∘ₗ D.1 = 0 := by
  apply LinearMap.ext
  intro v
  have ⟨h0, h1⟩ := singlet_coords_eq_zero_of_anticomm_stdIm (su3_anticomm_stdIm_of_projTriplet hD v)
  funext k
  change projSinglet (D.1 v) k = 0
  fin_cases k <;>
    simp [projSinglet, h0, h1, Fin.isValue]

/-- Consequently, `P₃ ∘ D = D` for every `D ∈ su3 stdIm`: the image of `𝕆` under `D` lies
entirely inside the 6D colour-triplet subspace `span(e₂, …, e₇)`. -/
theorem projTriplet_comp_D_eq_self {D : Der𝕆} (hD : D ∈ su3 stdIm) :
    projTriplet ∘ₗ D.1 = D.1 := by
  apply LinearMap.ext
  intro v
  change projTriplet (D.1 v) = D.1 v
  have h1 : projSinglet (D.1 v) = 0 := LinearMap.congr_fun (projSinglet_comp_D_eq_zero hD) v
  have h2 := projSinglet_apply_add_projTriplet_apply (D.1 v)
  rw [h1, zero_add] at h2
  exact h2

/-- Two-sided triplet sandwich identity: `P₃ ∘ D ∘ P₃ = D` for every `D ∈ su3 stdIm`. -/
theorem projTriplet_comp_D_comp_projTriplet {D : Der𝕆} (hD : D ∈ su3 stdIm) :
    projTriplet ∘ₗ D.1 ∘ₗ projTriplet = D.1 := by
  apply LinearMap.ext
  intro v
  change projTriplet (D.1 (projTriplet v)) = D.1 v
  have h1 : D.1 (projTriplet v) = D.1 v := LinearMap.congr_fun (D_comp_projTriplet_eq_self hD) v
  have h2 : projTriplet (D.1 v) = D.1 v := LinearMap.congr_fun (projTriplet_comp_D_eq_self hD) v
  rw [h1, h2]

/-! ### Coordinate Isomorphism `(Fin 6 → ℚ) ≃ₗ[ℚ] tripletSubmodule` and 6D Restriction -/

/-- Canonical embedding `emb6 : (Fin 6 → ℚ) →ₗ[ℚ] (Fin 8 → ℚ)` into coordinates `2..7`. -/
def emb6 : (Fin 6 → ℚ) →ₗ[ℚ] (Fin 8 → ℚ) where
  toFun u k := if h : k.1 < 2 then 0 else u ⟨k.1 - 2, by omega⟩
  map_add' u v := by
    funext k; dsimp; split_ifs <;> ring
  map_smul' c u := by
    funext k; dsimp; split_ifs <;> ring

/-- Canonical projection `π6 : (Fin 8 → ℚ) →ₗ[ℚ] (Fin 6 → ℚ)` reading coordinates `2..7`. -/
def π6 : (Fin 8 → ℚ) →ₗ[ℚ] (Fin 6 → ℚ) where
  toFun v j := v ⟨j.1 + 2, by omega⟩
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

/-- `π6 ∘ emb6 = id` on `Fin 6 → ℚ`. -/
theorem π6_comp_emb6 : π6 ∘ₗ emb6 = LinearMap.id := by
  apply LinearMap.ext; intro u; funext j
  change emb6 u ⟨j.1 + 2, by omega⟩ = u j
  fin_cases j <;> rfl

/-- `emb6 ∘ π6 = projTriplet` on `Fin 8 → ℚ`. -/
theorem emb6_comp_π6 : emb6 ∘ₗ π6 = projTriplet := by
  apply LinearMap.ext; intro v; funext k
  change emb6 (π6 v) k = projTriplet v k
  fin_cases k <;> rfl

/-- `projTriplet ∘ emb6 = emb6`. -/
theorem projTriplet_comp_emb6 : projTriplet ∘ₗ emb6 = emb6 := by
  apply LinearMap.ext; intro u; funext k
  change projTriplet (emb6 u) k = emb6 u k
  fin_cases k <;> rfl

/-- `π6 ∘ projTriplet = π6`. -/
theorem π6_comp_projTriplet : π6 ∘ₗ projTriplet = π6 := by
  apply LinearMap.ext; intro v; funext j
  change projTriplet v ⟨j.1 + 2, by omega⟩ = v ⟨j.1 + 2, by omega⟩
  fin_cases j <;> rfl

/-- Purely 8D-to-6D linear compression `T ↦ π6 ∘ T ∘ emb6`. -/
def compressToTriplet : Module.End ℚ (Fin 8 → ℚ) →ₗ[ℚ] Module.End ℚ (Fin 6 → ℚ) where
  toFun T := π6 ∘ₗ T ∘ₗ emb6
  map_add' T₁ T₂ := by
    apply LinearMap.ext; intro u
    exact map_add π6 (T₁ (emb6 u)) (T₂ (emb6 u))
  map_smul' c T := by
    apply LinearMap.ext; intro u
    exact map_smul π6 c (T (emb6 u))

/-- **6D colour-triplet restriction of `𝔰𝔲(3)`**: restricts each `D ∈ su3 stdIm` to an
endomorphism of the 6-dimensional rational colour-triplet space `(Fin 6 → ℚ) ≅ ℂ³` by
composing `compressToTriplet` with `su3ToEndOct stdIm`. -/
def su3ToEndTriplet : ↥(su3 stdIm) →ₗ[ℚ] Module.End ℚ (Fin 6 → ℚ) :=
  compressToTriplet.comp (su3ToEndOct stdIm)

@[simp] theorem su3ToEndTriplet_apply (D : ↥(su3 stdIm)) :
    su3ToEndTriplet D = π6 ∘ₗ D.1.1 ∘ₗ emb6 := rfl

/-- **Full reconstruction of `D` from its 6D triplet restriction**:
because `D` vanishes on and into the 2D singlet, `emb6 ∘ (su3ToEndTriplet D) ∘ π6 = D.1.1`. -/
theorem emb6_comp_su3ToEndTriplet_comp_π6 (D : ↥(su3 stdIm)) :
    emb6 ∘ₗ su3ToEndTriplet D ∘ₗ π6 = D.1.1 := by
  apply LinearMap.ext
  intro v
  change emb6 (π6 (D.1.1 (emb6 (π6 v)))) = D.1.1 v
  have h1 : emb6 (π6 v) = projTriplet v := LinearMap.congr_fun emb6_comp_π6 v
  have h2 : emb6 (π6 (D.1.1 (projTriplet v))) = projTriplet (D.1.1 (projTriplet v)) :=
    LinearMap.congr_fun emb6_comp_π6 (D.1.1 (projTriplet v))
  have h3 : projTriplet (D.1.1 (projTriplet v)) = D.1.1 v :=
    LinearMap.congr_fun (projTriplet_comp_D_comp_projTriplet D.2) v
  rw [h1, h2, h3]

/-- **Faithfulness of the 6D colour-triplet representation**:
if a colour derivation `D ∈ su3 stdIm` acts trivially on the 6D triplet `span(e₂, …, e₇)`,
then `D = 0` on all of `𝕆`. -/
theorem su3ToEndTriplet_injective : Function.Injective su3ToEndTriplet := by
  intro D₁ D₂ h
  have h8 : D₁.1.1 = D₂.1.1 := by
    rw [← emb6_comp_su3ToEndTriplet_comp_π6 D₁,
        ← emb6_comp_su3ToEndTriplet_comp_π6 D₂, h]
  exact Subtype.ext (Subtype.ext h8)

/-- **The 6-dimensional (`ℂ³`) colour-triplet space `(Fin 6 → ℚ)` realizes the abstract
`ColourStabilizerAction` class**, upgrading the 8D tautological base-module action of
`OctonionColourActionBaseModule` by factoring out the 2D trivial singlet `ℂ = span(1, e₁)`. -/
instance instColourStabilizerActionTriplet :
    ColourStabilizerAction ↥(su3 stdIm) (Fin 6 → ℚ) :=
  ⟨⟨su3ToEndTriplet, su3ToEndTriplet_injective⟩⟩

/-- Concrete `ColourStabilizerActionOnSU3 stdIm` witness on the 6D triplet `(Fin 6 → ℚ)`. -/
theorem colourStabilizerActionOnSU3_triplet :
    ColourStabilizerActionOnSU3 stdIm (Fin 6 → ℚ) :=
  inferInstance

/-! ### Induced Complex Structure `J6` and Bracket Preservation on the 6D Triplet -/

/-- Induced complex structure `J6 = π6 ∘ Le ∘ emb6` on the 6D colour triplet `(Fin 6 → ℚ)`. -/
def J6 : Module.End ℚ (Fin 6 → ℚ) := compressToTriplet Le

/-- Intertwining identity `emb6 ∘ J6 = Le ∘ emb6`. -/
theorem emb6_comp_J6 : emb6 ∘ₗ J6 = Le ∘ₗ emb6 := by
  apply LinearMap.ext
  intro u
  change emb6 (π6 (Le (emb6 u))) = Le (emb6 u)
  have h1 : emb6 (π6 (Le (emb6 u))) = projTriplet (Le (emb6 u)) :=
    LinearMap.congr_fun emb6_comp_π6 (Le (emb6 u))
  have h2 : projTriplet (Le (emb6 u)) = Le (projTriplet (emb6 u)) :=
    (LinearMap.congr_fun Le_comp_projTriplet (emb6 u)).symm
  have h3 : projTriplet (emb6 u) = emb6 u := LinearMap.congr_fun projTriplet_comp_emb6 u
  rw [h1, h2, h3]

/-- Intertwining identity `J6 ∘ π6 = π6 ∘ Le`. -/
theorem J6_comp_π6 : J6 ∘ₗ π6 = π6 ∘ₗ Le := by
  apply LinearMap.ext
  intro v
  change π6 (Le (emb6 (π6 v))) = π6 (Le v)
  have h1 : emb6 (π6 v) = projTriplet v := LinearMap.congr_fun emb6_comp_π6 v
  have h2 : Le (projTriplet v) = projTriplet (Le v) :=
    LinearMap.congr_fun Le_comp_projTriplet v
  have h3 : π6 (projTriplet (Le v)) = π6 (Le v) :=
    LinearMap.congr_fun π6_comp_projTriplet (Le v)
  rw [h1, h2, h3]

/-- **`J6` is a complex structure on `(Fin 6 → ℚ)`**: `J6² = -id₆`. -/
theorem J6_sq_eq_neg_id : J6 ∘ₗ J6 = -LinearMap.id := by
  apply LinearMap.ext
  intro u
  change J6 (π6 (Le (emb6 u))) = -u
  have h1 : J6 (π6 (Le (emb6 u))) = π6 (Le (Le (emb6 u))) :=
    LinearMap.congr_fun J6_comp_π6 (Le (emb6 u))
  have h2 : Le (Le (emb6 u)) = -emb6 u :=
    LinearMap.congr_fun Le_sq_eq_neg_id (emb6 u)
  have h3 : π6 (emb6 u) = u := LinearMap.congr_fun π6_comp_emb6 u
  rw [h1, h2, map_neg, h3]

/-- **The 6D colour-triplet representation acts `ℂ`-linearly**: every restricted colour
generator `su3ToEndTriplet D` commutes with the 6D complex structure `J6`. -/
theorem su3ToEndTriplet_comm_J6 (D : ↥(su3 stdIm)) :
    su3ToEndTriplet D ∘ₗ J6 = J6 ∘ₗ su3ToEndTriplet D := by
  apply LinearMap.ext
  intro u
  change π6 (D.1.1 (emb6 (J6 u))) = J6 (π6 (D.1.1 (emb6 u)))
  have h1 : emb6 (J6 u) = Le (emb6 u) := LinearMap.congr_fun emb6_comp_J6 u
  have h2 : D.1.1 (Le (emb6 u)) = Le (D.1.1 (emb6 u)) :=
    LinearMap.congr_fun (su3_comp_Le_eq_Le_comp D.2) (emb6 u)
  have h3 : π6 (Le (D.1.1 (emb6 u))) = J6 (π6 (D.1.1 (emb6 u))) :=
    (LinearMap.congr_fun J6_comp_π6 (D.1.1 (emb6 u))).symm
  rw [h1, h2, h3]

/-- The commutator Lie bracket on the colour subalgebra `↥(su3 stdIm)`. -/
def bracketSU3 (D₁ D₂ : ↥(su3 stdIm)) : ↥(su3 stdIm) :=
  ⟨bracketDer D₁.1 D₂.1, bracketDer_mem_su3 D₁.2 D₂.2⟩

/-- **The 6D colour-triplet restriction is a Lie-algebra homomorphism**:
`su3ToEndTriplet [D₁, D₂] = [su3ToEndTriplet D₁, su3ToEndTriplet D₂]`. -/
theorem su3ToEndTriplet_bracket (D₁ D₂ : ↥(su3 stdIm)) :
    su3ToEndTriplet (bracketSU3 D₁ D₂) =
      su3ToEndTriplet D₁ ∘ₗ su3ToEndTriplet D₂ -
        su3ToEndTriplet D₂ ∘ₗ su3ToEndTriplet D₁ := by
  have hcomp : ∀ (A B : ↥(su3 stdIm)) (u : Fin 6 → ℚ),
      su3ToEndTriplet A (su3ToEndTriplet B u) = π6 (A.1.1 (B.1.1 (emb6 u))) := by
    intro A B u
    change π6 (A.1.1 (emb6 (π6 (B.1.1 (emb6 u))))) = π6 (A.1.1 (B.1.1 (emb6 u)))
    have h1 : emb6 (π6 (B.1.1 (emb6 u))) = projTriplet (B.1.1 (emb6 u)) :=
      LinearMap.congr_fun emb6_comp_π6 (B.1.1 (emb6 u))
    have h2 : projTriplet (B.1.1 (emb6 u)) = B.1.1 (emb6 u) :=
      LinearMap.congr_fun (projTriplet_comp_D_eq_self B.2) (emb6 u)
    rw [h1, h2]
  apply LinearMap.ext
  intro u
  change π6 ((D₁.1.1 (D₂.1.1 (emb6 u))) - (D₂.1.1 (D₁.1.1 (emb6 u)))) =
    su3ToEndTriplet D₁ (su3ToEndTriplet D₂ u) - su3ToEndTriplet D₂ (su3ToEndTriplet D₁ u)
  rw [hcomp D₁ D₂ u, hcomp D₂ D₁ u]
  exact map_sub π6 (D₁.1.1 (D₂.1.1 (emb6 u))) (D₂.1.1 (D₁.1.1 (emb6 u)))

end QOU.StandardModel
