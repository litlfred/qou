import Mathlib.Algebra.Ring.Basic
import Mathlib.Tactic.Ring

/-!
# `QOU.CategoricalReeb.QReebFlowOnColorCoords` — the q-Reeb flow on color sectors

The q-Reeb flow `φ^q_t` advances a strand sitting at angular coordinate `ψ`
in a color sector with signed rate multiplier `k ∈ {-1,0,+1}` by `k·q·t`
(spectator `k=0`, leading strand `k=+1`, counter-rotating partner `k=-1`).
Sequential flows compose additively in the flow parameter `t`.

Algebraic content only (a real-angle specialisation lives downstream); the
construction holds over any commutative ring.

-- Ref: [leitner2026] mass-theory/q-reeb-flow-on-color-coords
-/

namespace QOU.CategoricalReeb

variable {R : Type*} [CommRing R]

/-- Angular action of the q-Reeb flow on one color sector: a strand at angle
`ψ` with signed rate multiplier `k` is advanced by `k·q·t`. -/
def qReebFlowSector (k : ℤ) (q t ψ : R) : R :=
  ψ + (k : R) * q * t

/-- **Composition.** Sequential q-Reeb flows compose additively in the flow
parameter: `φ^q_{t₁} ∘ φ^q_{t₂} = φ^q_{t₁+t₂}`. -/
theorem qReebFlowSector_comp (k : ℤ) (q t₁ t₂ ψ : R) :
    qReebFlowSector k q t₁ (qReebFlowSector k q t₂ ψ)
      = qReebFlowSector k q (t₁ + t₂) ψ := by
  unfold qReebFlowSector; ring

/-- A spectator sector (`k = 0`) is fixed by the flow. -/
theorem qReebFlowSector_spectator (q t ψ : R) :
    qReebFlowSector 0 q t ψ = ψ := by
  unfold qReebFlowSector; simp

end QOU.CategoricalReeb
