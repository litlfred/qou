import QOU.BringsSurface.OctonionDerivation
import Mathlib.LinearAlgebra.BilinearMap

/-!
# QOU.BringsSurface.OctonionLeibnizMap

**`Der(𝕆) = ker L` for an explicit linear Leibniz operator `L` (Tier 3).**

Upgrades `derivations` (the predicate-defined submodule of `OctonionDerivation`)
to the **kernel of a concrete `ℝ`-linear map**

`L : (𝕆 →ₗ[ℝ] 𝕆) →ₗ[ℝ] (𝕆 →ₗ[ℝ] 𝕆 →ₗ[ℝ] 𝕆)`,
`L(D)(x, y) = D(x·y) − D(x)·y − x·D(y)`  (the Leibniz defect).

`L` is linear in `D`, and `L(D)` is bilinear in `(x, y)` (the octonion product is
`ℝ`-bilinear even though non-associative — `OctonionAlgebra`). `D` is a derivation
iff its Leibniz defect vanishes, so

`derivations = LinearMap.ker L`  (`derivations_eq_ker`).

**Why this matters for `dim = 14`.** With `𝕆` finite-dimensional (`finrank ℝ 𝕆 = 8`,
`OctonionFinDim`), `Der(𝕆) = ker L` sits inside the `64`-dimensional `𝕆 →ₗ[ℝ] 𝕆`,
and `dim 𝔤₂ = dim Der(𝕆) = 14` is exactly the statement **`nullity L = 14`**
(equivalently `rank L = 50`) — a *finite* linear-algebra fact about the explicit
operator `L`, not a claim needing extrinsic `G₂` theory. This file provides the
operator and the kernel identity; the rank/nullity value `14` remains the open
computation (the explicit `14`-dimensional solution space / a spanning argument),
recorded in the audit + bean `qou-k5w2`. Nothing here asserts `dim = 14` (per
AGENTS.md §"Axiomatization is NOT a Proof").

Over `ℝ` (§7c), sorry-free.

-- Ref: [manuscript] docs/audits/2026-07-12-octonion-recovery-from-genus4-analysis.md
-/

namespace QOU.BringsSurface.OctonionAlgebra

open scoped BigOperators

/-- The **Leibniz defect** of `D` as a bilinear map
`(x, y) ↦ D(x·y) − D(x)·y − x·D(y)`. Bilinear because the octonion product is
`ℝ`-bilinear and `D` is linear. -/
def leibnizBilin (D : Oct →ₗ[ℝ] Oct) : Oct →ₗ[ℝ] Oct →ₗ[ℝ] Oct :=
  LinearMap.mk₂ ℝ (fun x y => D (x * y) - D x * y - x * D y)
    (by intro x₁ x₂ y; simp only [Oct.add_mul, map_add]; abel)
    (by intro c x y; simp only [Oct.smul_mul, map_smul, smul_sub])
    (by intro x y₁ y₂; simp only [Oct.mul_add, map_add]; abel)
    (by intro c x y; simp only [Oct.mul_smul, map_smul, smul_sub])

@[simp] theorem leibnizBilin_apply (D : Oct →ₗ[ℝ] Oct) (x y : Oct) :
    leibnizBilin D x y = D (x * y) - D x * y - x * D y := rfl

/-- The **Leibniz operator** `L : (𝕆 →ₗ 𝕆) →ₗ (𝕆 →ₗ 𝕆 →ₗ 𝕆)`, linear in `D`. Its
kernel is `Der(𝕆) = 𝔤₂`. -/
def leibnizMap : (Oct →ₗ[ℝ] Oct) →ₗ[ℝ] (Oct →ₗ[ℝ] Oct →ₗ[ℝ] Oct) where
  toFun := leibnizBilin
  map_add' D D' := by
    refine LinearMap.ext fun x => LinearMap.ext fun y => ?_
    simp only [leibnizBilin_apply, LinearMap.add_apply, Oct.add_mul, Oct.mul_add]
    abel
  map_smul' c D := by
    refine LinearMap.ext fun x => LinearMap.ext fun y => ?_
    simp only [leibnizBilin_apply, LinearMap.smul_apply, RingHom.id_apply,
      Oct.smul_mul, Oct.mul_smul, smul_sub]

@[simp] theorem leibnizMap_apply (D : Oct →ₗ[ℝ] Oct) (x y : Oct) :
    leibnizMap D x y = D (x * y) - D x * y - x * D y := rfl

/-- **`Der(𝕆) = ker L`.** A linear map is a derivation of `𝕆` iff its Leibniz
defect vanishes identically — so the derivation algebra `𝔤₂` is exactly the kernel
of the explicit operator `L`. This is the object whose dimension is the Tier-3
goal (`dim = 14`). -/
theorem derivations_eq_ker : derivations = LinearMap.ker leibnizMap := by
  ext D
  simp only [mem_derivations, LinearMap.mem_ker]
  constructor
  · intro hD
    refine LinearMap.ext fun x => LinearMap.ext fun y => ?_
    simp only [leibnizMap_apply, LinearMap.zero_apply]
    rw [hD x y]; abel
  · intro hker x y
    have h := LinearMap.congr_fun (LinearMap.congr_fun hker x) y
    simp only [leibnizMap_apply, LinearMap.zero_apply] at h
    -- h : D (x*y) - D x * y - x * D y = 0
    rw [sub_sub, sub_eq_zero] at h
    exact h

end QOU.BringsSurface.OctonionAlgebra
