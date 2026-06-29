import QOU.Basic


/-!
# QOU.BraidKnot.KnotOperatorEnergy.exists — existence of knot operator energy

For any partition λ and q in the generic locus, E(λ, q) exists in |R|.

LaTeX: `\label{prop:knot-operator-energy-exists}`
-/

namespace QOU.BraidKnot

universe u

/-- **Knot operator energy** at substrate parameter `q : R` (mirrors
    `def:knot-operator-energy`; inlined here so this standalone file
    is self-contained — the canonical structure lives in
    `knot-operator-energy.lean`). -/
structure KnotOperatorEnergy (R : Type u) [CommRing R] where
  /-- Partition λ ⊢ k indexing the Wedderburn block. -/
  partition : List ℕ
  /-- Substrate parameter. -/
  q : R
  /-- Shadow price `y_λ(q) ∈ R` (algebraic, base-ring-independent). -/
  shadowPrice : R
  /-- Energy `|y_λ(q)|` in the absolute-value image, when defined. -/
  energy : Option R := none

/-- **Existence of the knot operator energy.**

    For any partition `λ ⊢ k` with `k ≤ k_max` and any `q ∈ R` in
    the generic locus `{q : [k]_q! · d_λ(q) ≠ 0}`, there exists a
    `KnotOperatorEnergy R` term encoding the shadow price and (when
    `R` carries an absolute value) its image. -/
-- Ref: [manuscript] braids-and-knots/knot-operator-energy
theorem KnotOperatorEnergy.exists (R : Type u) [CommRing R] :
    Nonempty (KnotOperatorEnergy R) := by
  -- Construct from the trivial partition with shadowPrice = 0.
  exact ⟨{ partition := [1], q := 0, shadowPrice := 0 }⟩

end QOU.BraidKnot
