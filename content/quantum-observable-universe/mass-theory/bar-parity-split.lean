import Mathlib.Algebra.Module.LinearMap.Basic
import Mathlib.Tactic.Abel

/-!
# QOU.Mass.bar_parity_split — one Habiro element, two parities

The keystone trace `τ = tr B` (binding, cosh, bar-EVEN) and the `Q_β`
residue-A / `c_k` ladder (bar-ODD Habiro dual of α_EM, sinh) are the two
parities of a SINGLE element under the bar-involution `σ` (`q ↦ q⁻¹`,
`σ² = id`). This file proves the elementary decomposition that makes that
precise: under any linear involution `σ`, every `x` splits as a `σ`-fixed
(even) part plus a `σ`-anti (odd) part, and `evenPart + oddPart = 2·x`.

So: `F = F_even + F_odd`, with `τ` read off `F_even` (cosh, binding) and the
`Q_β` residue read off `F_odd` (sinh, β-decay) — one object, two observables.

LaTeX label: `prop:bar-parity-split`.

**Ground ring**: generic `[CommRing R]`. See `GroundRingAnnotations.lean`.
-/

namespace QOU.Mass

variable {R : Type*} [CommRing R] {V : Type*} [AddCommGroup V] [Module R V]

/-- bar-even part `x + σx` (un-normalised; `σ`-fixed). -/
def evenPart (σ : V →ₗ[R] V) (x : V) : V := x + σ x

/-- bar-odd part `x − σx` (un-normalised; `σ`-anti). -/
def oddPart (σ : V →ₗ[R] V) (x : V) : V := x - σ x

/-- The two parities reconstruct `2·x` (so `x` is half their sum). -/
theorem evenPart_add_oddPart (σ : V →ₗ[R] V) (x : V) :
    evenPart σ x + oddPart σ x = (2 : ℕ) • x := by
  simp only [evenPart, oddPart]; abel

/-- The even part is `σ`-fixed (bar-even, cosh sector). -/
theorem evenPart_fixed (σ : V →ₗ[R] V) (hσ : ∀ y, σ (σ y) = y) (x : V) :
    σ (evenPart σ x) = evenPart σ x := by
  simp only [evenPart, map_add, hσ]; abel

/-- The odd part is `σ`-anti (bar-odd, sinh sector). -/
theorem oddPart_anti (σ : V →ₗ[R] V) (hσ : ∀ y, σ (σ y) = y) (x : V) :
    σ (oddPart σ x) = - oddPart σ x := by
  simp only [oddPart, map_sub, hσ]; abel

end QOU.Mass
