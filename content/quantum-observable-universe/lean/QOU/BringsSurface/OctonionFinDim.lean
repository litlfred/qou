import QOU.BringsSurface.OctonionAlgebra
import Mathlib.LinearAlgebra.Dimension.Constructions
import Mathlib.LinearAlgebra.FiniteDimensional.Defs

/-!
# QOU.BringsSurface.OctonionFinDim

**`𝕆` is an 8-dimensional `ℝ`-vector space (`finrank ℝ 𝕆 = 8`).**

The finite-dimensionality prerequisite for the Tier-3 `dim Der(𝕆) = 14` goal: only
once `𝕆` is known to be finite-dimensional is `Module.finrank ℝ (Der 𝕆)` a
*meaningful* number (rather than the junk `0` the `finrank` convention assigns to
infinite-dimensional or unresolved spaces). It also gives
`FiniteDimensional ℝ (𝕆 →ₗ[ℝ] 𝕆)` (`dim 64`), inside which `Der(𝕆)` is the
submodule whose dimension is the open goal.

The proof avoids `Fin 8`/`Matrix` notation (absent from the sandbox olean cache)
by walking the Cayley–Dickson tower as a chain of **product linear-equivs**, each
a definitional `⟨fst, snd⟩ ↔ (fst, snd)` isomorphism:

`Cplx ≃ₗ ℝ×ℝ`  ⇒ `finrank = 2`;  `Quat ≃ₗ Cplx×Cplx` ⇒ `4`;
`Oct ≃ₗ Quat×Quat` ⇒ `8`.

Everything over `ℝ` (§7c), sorry-free.

-- Ref: [manuscript] docs/audits/2026-07-12-octonion-recovery-from-genus4-analysis.md
-/

namespace QOU.BringsSurface.OctonionAlgebra

/-- `Cplx ≃ₗ[ℝ] ℝ × ℝ` — the real/imaginary coordinate isomorphism. -/
def cplxEquivProd : Cplx ≃ₗ[ℝ] ℝ × ℝ where
  toFun x := (x.re, x.im)
  map_add' _ _ := rfl
  map_smul' _ _ := rfl
  invFun p := ⟨p.1, p.2⟩
  left_inv _ := rfl
  right_inv _ := rfl

/-- `Quat ≃ₗ[ℝ] Cplx × Cplx` — the Cayley–Dickson `⟨fst, snd⟩` splitting. -/
def quatEquivProd : Quat ≃ₗ[ℝ] Cplx × Cplx where
  toFun p := (p.fst, p.snd)
  map_add' _ _ := rfl
  map_smul' _ _ := rfl
  invFun v := ⟨v.1, v.2⟩
  left_inv _ := rfl
  right_inv _ := rfl

/-- `Oct ≃ₗ[ℝ] Quat × Quat` — the Cayley–Dickson `⟨fst, snd⟩` splitting. -/
def octEquivProd : Oct ≃ₗ[ℝ] Quat × Quat where
  toFun a := (a.fst, a.snd)
  map_add' _ _ := rfl
  map_smul' _ _ := rfl
  invFun v := ⟨v.1, v.2⟩
  left_inv _ := rfl
  right_inv _ := rfl

instance : FiniteDimensional ℝ Cplx := Module.Finite.equiv cplxEquivProd.symm
instance : FiniteDimensional ℝ Quat := Module.Finite.equiv quatEquivProd.symm
instance : FiniteDimensional ℝ Oct := Module.Finite.equiv octEquivProd.symm

/-- `dim_ℝ Cplx = 2`. -/
theorem finrank_cplx : Module.finrank ℝ Cplx = 2 := by
  rw [cplxEquivProd.finrank_eq, Module.finrank_prod, Module.finrank_self]

/-- `dim_ℝ Quat = 4`. -/
theorem finrank_quat : Module.finrank ℝ Quat = 4 := by
  rw [quatEquivProd.finrank_eq, Module.finrank_prod, finrank_cplx]

/-- **`dim_ℝ 𝕆 = 8`.** The octonions are an 8-dimensional real vector space — the
finite-dimensional ambient in which `Der(𝕆) = 𝔤₂` (Tier-3 goal `dim = 14`) is cut
out of the 64-dimensional `𝕆 →ₗ[ℝ] 𝕆`. -/
theorem finrank_oct : Module.finrank ℝ Oct = 8 := by
  rw [octEquivProd.finrank_eq, Module.finrank_prod, finrank_quat]

end QOU.BringsSurface.OctonionAlgebra
