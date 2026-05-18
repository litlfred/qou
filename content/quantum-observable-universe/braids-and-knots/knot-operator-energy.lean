/-!
# QOU.BraidKnot.KnotOperatorEnergy — knot operator energy

E(λ, q) := |y_λ(q)| where y_λ(q) = w_λ(q)/d_λ(q) - 1/[k]_q! is the
LP-dual shadow price (prop:mass-coefficient-shadow-price).

LaTeX: `\label{def:knot-operator-energy}`
-/

import QOU.Basic

namespace QOU.BraidKnot

universe u

/-- **Knot operator energy** at substrate parameter `q : R`.

    Encodes the absolute value of the shadow price `y_λ(q) ∈ R`.
    Realisations:
      * `R = ℝ`: archimedean `|·|_∞`, image `ℝ_{≥0}`.
      * `R = ℚ_p`: `p`-adic `|·|_p`.
      * `R = 𝔽_p`: no archimedean absolute value; the field
        `KnotOperatorEnergy.values` is empty and the filtration
        falls back to ILP feasibility (`def:stable-atom`). -/
structure KnotOperatorEnergy (R : Type u) [CommRing R] where
  /-- Partition λ ⊢ k indexing the Wedderburn block. -/
  partition : List ℕ
  /-- Substrate parameter. -/
  q : R
  /-- Shadow price `y_λ(q) ∈ R` (algebraic, base-ring-independent). -/
  shadowPrice : R
  /-- Energy `|y_λ(q)|` in the absolute-value image, when defined. -/
  energy : Option R := none

end QOU.BraidKnot
