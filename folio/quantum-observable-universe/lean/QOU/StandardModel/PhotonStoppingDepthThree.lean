/-
  `L(3) = 2` in the concrete model of `H₃(q)`: one photon does not span `H₃(q)`, two do.

  Basis `T_e, T_0, T_1, T_01, T_10, T_010`. In `F₁ = span{1, σ₀, σ₁, V}` lie `T_e`, `T_0`, `T_1`
  and `T_01 = V + h·σ₀` (`T01_mem_F1`). `T_10 = σ₁σ₀` is a product of two photons and is not in
  `F₁` (`T10_not_mem_F1`). `T_010 = Vσ₀ + h²σ₀ + h` is a combination of products of at most
  two photons (`QOU.HeckeH3Model.electron_eq`). So `F₂ = H₃(q)` and `F₁ ≠ H₃(q)`.

  -- Ref: [kassel2008] https://doi.org/10.1007/978-0-387-68548-9
-/
import QOU.StandardModel.HeckeH3Model

namespace QOU.PhotonStoppingDepthThree

open QOU.Mass.BorromeanPhotonFactorisation QOU.HeckeH3Model

variable {R : Type*} [CommRing R]

/-- `T_01 = σ₀σ₁ = V + h·σ₀`, so `T_01 ∈ F₁`. -/
theorem T01_mem_F1 (h : R) : heckeL0 h * heckeL1 h = modelV h + h • heckeL0 h := by
  rw [modelV, vertex_eq]; abel

/-- `T_10 = σ₁σ₀ ∉ F₁`. -/
theorem T10_not_mem_F1 [Nontrivial R] (h c₀ c₁ c₂ c₃ : R) :
    heckeL1 h * heckeL0 h
      ≠ c₀ • (1 : M6 R) + c₁ • heckeL0 h + c₂ • heckeL1 h + c₃ • modelV h := by
  intro hc
  have e := coord_F1 h c₀ c₁ c₂ c₃ 4
  rw [← hc] at e
  simp [coord, te, Module.End.mul_apply] at e

/-- `T_010 ∈ F₂`, in the model. -/
theorem T010_mem_F2 (h : R) :
    heckeL0 h * heckeL1 h * heckeL0 h
      = modelV h * heckeL0 h + (h ^ 2) • heckeL0 h + h • (1 : M6 R) :=
  electron_eq (model_rel h)

end QOU.PhotonStoppingDepthThree
