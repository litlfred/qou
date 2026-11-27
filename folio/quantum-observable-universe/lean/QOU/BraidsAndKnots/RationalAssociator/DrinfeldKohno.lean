import Mathlib.Algebra.FreeAlgebra
import QOU.BraidsAndKnots.RationalAssociator.LowDegree
import Mathlib.Tactic.Abel
import Mathlib.Data.Fin.VecNotation

/-!
# Drinfeld–Kohno families on three and four strands, and the five cofaces

Bean `qou-3fdg` (stage 3 infrastructure of the rational-associator plan, epic `qou-dk7p`).

A *Drinfeld–Kohno family* on `n` strands in a ring `R` is a choice of elements `tᵢⱼ = tⱼᵢ`
(`i ≠ j`) satisfying the relations of the infinitesimal pure braid algebra `𝔱ₙ`:

* far: `[tᵢⱼ, tₖₗ] = 0` for `{i, j} ∩ {k, l} = ∅`;
* near: `[tᵢⱼ, tᵢₖ + tⱼₖ] = 0` for distinct `i, j, k`.

`DK3` and `DK4` record these for `n = 3, 4` with named elements. Every statement proved for all
families holds in `U(𝔱ₙ)` (the universal family) and in every representation of it.

The pentagon `φ(t₁₂, t₂₃ + t₂₄) φ(t₁₃ + t₂₃, t₃₄) = φ(t₂₃, t₃₄) φ(t₁₂ + t₁₃, t₂₄ + t₃₄) φ(t₁₂, t₂₃)`
evaluates `φ(A, B)`, with `A = t₁₂`, `B = t₂₃`, along the five cofaces `dᵢ : 𝔱₃ → 𝔱₄`
(Bar-Natan 1998, Def. 3.1: `d₄Φ · d₂Φ · d₀Φ = d₁Φ · d₃Φ`, there with the opposite order of
multiplication). This file proves that **each coface carries a `DK4` family to a `DK3` family**
(`DK4.d0` … `DK4.d4`). Statements about `DK3` families, for example the hexagon, therefore
transport to every factor of the pentagon. `eval` evaluates a noncommutative polynomial
`φ ∈ ℚ⟨X, Y⟩` at a pair. No analysis is used.
-/

namespace QOU.BraidsAndKnots.RationalAssociator

variable {R : Type*} [Ring R]

/-- Drinfeld–Kohno relations on three strands (`t₁₂, t₁₃, t₂₃`). -/
structure DK3 (t12 t13 t23 : R) : Prop where
  n12_3 : Commute t12 (t13 + t23)
  n13_2 : Commute t13 (t12 + t23)
  n23_1 : Commute t23 (t12 + t13)

/-- Drinfeld–Kohno relations on four strands. -/
structure DK4 (t12 t13 t14 t23 t24 t34 : R) : Prop where
  f12_34 : Commute t12 t34
  f13_24 : Commute t13 t24
  f14_23 : Commute t14 t23
  n12_3 : Commute t12 (t13 + t23)
  n13_2 : Commute t13 (t12 + t23)
  n23_1 : Commute t23 (t12 + t13)
  n12_4 : Commute t12 (t14 + t24)
  n14_2 : Commute t14 (t12 + t24)
  n24_1 : Commute t24 (t12 + t14)
  n13_4 : Commute t13 (t14 + t34)
  n14_3 : Commute t14 (t13 + t34)
  n34_1 : Commute t34 (t13 + t14)
  n23_4 : Commute t23 (t24 + t34)
  n24_3 : Commute t24 (t23 + t34)
  n34_2 : Commute t34 (t23 + t24)

namespace DK4

variable {t12 t13 t14 t23 t24 t34 : R} (h : DK4 t12 t13 t14 t23 t24 t34)
include h

/-- `d₄ = φ^{1,2,3}`: strands `1, 2, 3`. -/
theorem d4 : DK3 t12 t13 t23 := ⟨h.n12_3, h.n13_2, h.n23_1⟩

/-- `d₀ = φ^{2,3,4}`: strands `2, 3, 4`. -/
theorem d0 : DK3 t23 t24 t34 := ⟨h.n23_4, h.n24_3, h.n34_2⟩

/-- `d₃ = φ^{1,2,34}`: strands `3, 4` merged. -/
theorem d3 : DK3 t12 (t13 + t14) (t23 + t24) := by
  refine ⟨?_, ?_, ?_⟩
  · rw [show t13 + t14 + (t23 + t24) = (t13 + t23) + (t14 + t24) by abel]
    exact h.n12_3.add_right h.n12_4
  · rw [show t12 + (t23 + t24) = (t12 + t23) + t24 by abel]
    refine Commute.add_left (h.n13_2.add_right h.f13_24) ?_
    rw [show t12 + t23 + t24 = (t12 + t24) + t23 by abel]
    exact h.n14_2.add_right h.f14_23
  · rw [show t12 + (t13 + t14) = (t12 + t13) + t14 by abel]
    refine Commute.add_left (h.n23_1.add_right h.f14_23.symm) ?_
    rw [show t12 + t13 + t14 = (t12 + t14) + t13 by abel]
    exact h.n24_1.add_right h.f13_24.symm

/-- `d₁ = φ^{12,3,4}`: strands `1, 2` merged. -/
theorem d1 : DK3 (t13 + t23) (t14 + t24) t34 := by
  refine ⟨?_, ?_, ?_⟩
  · rw [show t14 + t24 + t34 = (t14 + t34) + t24 by abel]
    refine Commute.add_left (h.n13_4.add_right h.f13_24) ?_
    rw [show t14 + t34 + t24 = (t24 + t34) + t14 by abel]
    exact h.n23_4.add_right h.f14_23.symm
  · rw [show t13 + t23 + t34 = (t13 + t34) + t23 by abel]
    refine Commute.add_left (h.n14_3.add_right h.f14_23) ?_
    rw [show t13 + t34 + t23 = (t23 + t34) + t13 by abel]
    exact h.n24_3.add_right h.f13_24.symm
  · rw [show t13 + t23 + (t14 + t24) = (t13 + t14) + (t23 + t24) by abel]
    exact h.n34_1.add_right h.n34_2

/-- `d₂ = φ^{1,23,4}`: strands `2, 3` merged. -/
theorem d2 : DK3 (t12 + t13) t14 (t24 + t34) := by
  refine ⟨?_, ?_, ?_⟩
  · rw [show t14 + (t24 + t34) = (t14 + t24) + t34 by abel]
    refine Commute.add_left (h.n12_4.add_right h.f12_34) ?_
    rw [show t14 + t24 + t34 = (t14 + t34) + t24 by abel]
    exact h.n13_4.add_right h.f13_24
  · rw [show t12 + t13 + (t24 + t34) = (t12 + t24) + (t13 + t34) by abel]
    exact h.n14_2.add_right h.n14_3
  · rw [show t12 + t13 + t14 = (t12 + t14) + t13 by abel]
    refine Commute.add_left (h.n24_1.add_right h.f13_24.symm) ?_
    rw [show t12 + t14 + t13 = (t13 + t14) + t12 by abel]
    exact h.n34_1.add_right h.f12_34.symm

end DK4

/-- Evaluate a noncommutative polynomial `φ ∈ ℚ⟨X, Y⟩` at `X = a`, `Y = b`. -/
noncomputable def eval {R : Type*} [Ring R] [Algebra ℚ R] (a b : R) :
    FreeAlgebra ℚ (Fin 2) →ₐ[ℚ] R :=
  FreeAlgebra.lift ℚ ![a, b]

@[simp] theorem eval_X {R : Type*} [Ring R] [Algebra ℚ R] (a b : R) :
    eval a b (FreeAlgebra.ι ℚ 0) = a := by simp [eval]

@[simp] theorem eval_Y {R : Type*} [Ring R] [Algebra ℚ R] (a b : R) :
    eval a b (FreeAlgebra.ι ℚ 1) = b := by simp [eval]

/-- The pentagon for `φ ∈ ℚ⟨X, Y⟩` at a four-strand family, in Drinfeld's form (`t₁₄` does not occur). -/
def Pentagon {R : Type*} [Ring R] [Algebra ℚ R] (φ : FreeAlgebra ℚ (Fin 2))
    (t12 t13 t23 t24 t34 : R) : Prop :=
  eval t12 (t23 + t24) φ * eval (t13 + t23) t34 φ =
    eval t23 t34 φ * eval (t12 + t13) (t24 + t34) φ * eval t12 t23 φ

/-- The stage-1 associator `φ = 1 + c·[X, Y]` as a noncommutative polynomial. -/
noncomputable def phiPoly (c : ℚ) : FreeAlgebra ℚ (Fin 2) :=
  1 + c • (FreeAlgebra.ι ℚ 0 * FreeAlgebra.ι ℚ 1 - FreeAlgebra.ι ℚ 1 * FreeAlgebra.ι ℚ 0)

theorem eval_phiPoly {R : Type*} [Ring R] [Algebra ℚ R] (c : ℚ) (a b : R) :
    eval a b (phiPoly c) = phi c a b := by
  simp [phiPoly, phi]

/-- Stage 1 restated: `1 + (1/24)[X, Y]` satisfies the pentagon at every four-strand family
whose length-3 words vanish. -/
theorem pentagon_phiPoly {R : Type*} [Ring R] [Algebra ℚ R] (c : ℚ)
    {t12 t13 t14 t23 t24 t34 : R} (h : Trunc3 ({t12, t13, t14, t23, t24, t34} : Set R))
    (hDK : DK4 t12 t13 t14 t23 t24 t34) : Pentagon (phiPoly c) t12 t13 t23 t24 t34 := by
  unfold Pentagon
  simp only [eval_phiPoly]
  exact pentagon c h hDK.f12_34 hDK.f13_24

end QOU.BraidsAndKnots.RationalAssociator
