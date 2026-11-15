import Mathlib.Algebra.Module.LinearMap.Basic
import Mathlib.Tactic.Abel

/-!
# QOU.Mass — even/odd decomposition under a linear involution

Under any linear involution `σ` (`σ² = id`) of an `R`-module `V`, every `x`
splits as a `σ`-fixed (even) part plus a `σ`-anti (odd) part, and
`evenPart + oddPart = 2·x`. This is the bar-parity decomposition used with the
bar-involution `q ↦ q⁻¹` of `def:bar-involution`.

LaTeX label: `lem:bar-involution-parity-decomposition`.

**Scope.** These are generic facts, true of every element of every module with
an involution. They do NOT establish that the binding trace and the `Q_β`
residue are the even and odd parts of one fibre element. That claim is the
conjecture `conj:bar-parity-split`, which uses this lemma but is not proved by
it. Until 2026-11-15 this file carried the label `prop:bar-parity-split` and a
docstring stating the identification as if proved; it was demoted because the
Lean is generic and no `Q_β` functional on record is bar-odd
(`docs/audits/2026-11-15-one-sided-weak-vertex.md` §4).

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

/-- The even part is `σ`-fixed. -/
theorem evenPart_fixed (σ : V →ₗ[R] V) (hσ : ∀ y, σ (σ y) = y) (x : V) :
    σ (evenPart σ x) = evenPart σ x := by
  simp only [evenPart, map_add, hσ]; abel

/-- The odd part is `σ`-anti. -/
theorem oddPart_anti (σ : V →ₗ[R] V) (hσ : ∀ y, σ (σ y) = y) (x : V) :
    σ (oddPart σ x) = - oddPart σ x := by
  simp only [oddPart, map_sub, hσ]; abel

end QOU.Mass
