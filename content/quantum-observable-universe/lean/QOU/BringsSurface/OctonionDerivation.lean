import QOU.BringsSurface.OctonionAlgebra
import Mathlib.Algebra.Module.Submodule.Basic
import Mathlib.Algebra.Module.LinearMap.Basic
import Mathlib.Tactic.Abel

/-!
# QOU.BringsSurface.OctonionDerivation

**The derivation algebra `𝔤₂ = Der(𝕆)` — the Lie algebra of `G₂ = Aut(𝕆)`.**

Tier 3 of the octonion → `G₂` roadmap (PR #3671). A **derivation** of the
octonions is an `ℝ`-linear `D : 𝕆 →ₗ[ℝ] 𝕆` satisfying the Leibniz law
`D(xy) = D(x)y + x D(y)`. The derivations form the **exceptional Lie algebra
`𝔤₂`**, and `Der(𝕆) = Lie(Aut(𝕆)) = Lie(G₂)`.

This file establishes what is provable now as **finite linear algebra** (no Lie
theory): the Leibniz condition is *linear in `D`*, so `Der(𝕆)` is an
`ℝ`-**submodule** of `𝕆 →ₗ[ℝ] 𝕆` (`derivations` below, with the three closure
proofs discharged from the octonion product's bilinearity, `OctonionAlgebra`).

**The open Tier-3 goal — `dim Der(𝕆) = 14`.** This is `dim 𝔤₂ = dim G₂ = 14`. It
is a *finite* computation (an explicit `14`-derivation basis of the submodule cut
out of the `64`-dimensional `𝕆 →ₗ[ℝ] 𝕆`), elementary but long, and it needs
`Module.finrank` + a `Basis` over the derivation submodule — deferred to a
subsequent commit. It is **not** stated with `sorry` here: the honest state is
that `derivations` is defined and proved to be a submodule, and the dimension is
recorded as the open goal (audit doc + bean `qou-k5w2`), not a laundered
placeholder. (See AGENTS.md §"Axiomatization is NOT a Proof".)

Everything here is over `ℝ` (§7c), sorry-free.

-- Ref: [manuscript] docs/audits/2026-07-12-octonion-recovery-from-genus4-analysis.md
-/

namespace QOU.BringsSurface.OctonionAlgebra

open Oct

/-- **A derivation of `𝕆`** — an `ℝ`-linear map satisfying the Leibniz law
`D(xy) = D(x)·y + x·D(y)`. The derivations are the elements of the exceptional
Lie algebra `𝔤₂`. -/
def IsDerivation (D : Oct →ₗ[ℝ] Oct) : Prop :=
  ∀ x y : Oct, D (x * y) = D x * y + x * D y

/-- **`𝔤₂ = Der(𝕆)` as an `ℝ`-submodule of `𝕆 →ₗ[ℝ] 𝕆`.** The Leibniz condition is
linear in `D`, so derivations are closed under `0`, `+`, and scalar `•` — the
three proofs below reduce to the `ℝ`-bilinearity of the (non-associative) octonion
product (`Oct.zero_mul`, `Oct.add_mul`, `Oct.smul_mul`, …). This is the Lie
algebra of `G₂` realised as a concrete finite-dimensional linear subspace. -/
def derivations : Submodule ℝ (Oct →ₗ[ℝ] Oct) where
  carrier := {D | IsDerivation D}
  zero_mem' := by
    show IsDerivation (0 : Oct →ₗ[ℝ] Oct)
    intro x y
    simp [Oct.zero_mul, Oct.mul_zero]
  add_mem' := by
    intro D D' hD hD'
    intro x y
    simp only [LinearMap.add_apply]
    rw [hD x y, hD' x y, Oct.add_mul, Oct.mul_add]
    abel
  smul_mem' := by
    intro c D hD
    intro x y
    simp only [LinearMap.smul_apply]
    rw [hD x y, smul_add, Oct.smul_mul, Oct.mul_smul]

/-- Membership in `derivations` is exactly the Leibniz property. -/
theorem mem_derivations {D : Oct →ₗ[ℝ] Oct} : D ∈ derivations ↔ IsDerivation D :=
  Iff.rfl

/-- The zero map is a derivation (the additive identity of `𝔤₂`). -/
theorem isDerivation_zero : IsDerivation (0 : Oct →ₗ[ℝ] Oct) :=
  derivations.zero_mem

end QOU.BringsSurface.OctonionAlgebra
