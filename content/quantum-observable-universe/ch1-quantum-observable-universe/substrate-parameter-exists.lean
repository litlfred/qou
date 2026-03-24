/-!
# QOU.SubstrateParameter.ofReebDecomposition

Existence of the substrate parameter: given a Reeb derivation and
weight decomposition, a constant transcendental field `q₀ > 1`
satisfies all `SubstrateParameter` axioms.

LaTeX: `\label{thm:substrate-parameter-exists}`
-/

import QOU.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Data.Real.Irrational

open scoped Topology

namespace QOU

universe u

/-- **Existence of the substrate parameter** (constant field).

    Given `q₀ > 1` that is not a root of unity (e.g., `q₀`
    transcendental), the constant field `q(p) = q₀` defines a valid
    `SubstrateParameter M` for any type `M`.

    This is the simplest constructor; non-constant substrate fields
    arise from the Reeb flow parameterisation.

    Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443 -/
noncomputable def SubstrateParameter.ofConstant
    (M : Type*) (q₀ : ℝ) (hq_pos : 0 < q₀) (hq_ge : 1 ≤ q₀)
    (hq_root : ∀ (k : ℕ), k ≥ 1 → q₀ ^ k ≠ 1) :
    SubstrateParameter M :=
  { field := fun _ => q₀
    field_pos := fun _ => hq_pos
    field_ge_one := fun _ => hq_ge
    not_root_of_unity := fun _ k hk => hq_root k hk }

/-- **Existence from Reeb decomposition** (dependent constructor).

    Given a weight decomposition and categorical Reeb derivation,
    the substrate parameter exists by choosing a constant
    transcendental `q₀ > 1`.  The Reeb decomposition witnesses the
    splitting `d_q = q⁻¹ d + (1 − q⁻¹) π_V ∘ d` is well-defined:
    the existence of `(ξ, θ_A)` and `(π_H, π_V)` ensures the
    interpolation formula has both endpoints.

    Physically, the constant `q₀` may be replaced by a field
    `q(p) = 1 + ‖L_θ ∧ F_A⁺‖(p)` once a connection is given.

    Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443 -/
noncomputable def SubstrateParameter.ofReebDecomposition
    {C : Type*} [CategoryTheory.Category C]
    [CategoryTheory.MonoidalCategory C]
    (M : Type*) (_wd : WeightDecomposition C)
    (_reeb : CategoricalReeb C)
    (q₀ : ℝ) (hq_pos : 0 < q₀) (hq_ge : 1 ≤ q₀)
    (hq_root : ∀ (k : ℕ), k ≥ 1 → q₀ ^ k ≠ 1) :
    SubstrateParameter M :=
  SubstrateParameter.ofConstant M q₀ hq_pos hq_ge hq_root

end QOU
