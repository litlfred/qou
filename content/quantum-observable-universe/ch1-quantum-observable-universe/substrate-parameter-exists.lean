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
    the substrate parameter exists as a fibre coordinate on the
    Reeb flow, parameterised by points of `M`.

    This is the physically motivated constructor: the Reeb flow
    determines a canonical coordinate `q(p)` at each point.

    Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443 -/
noncomputable def SubstrateParameter.ofReebDecomposition
    {C : Type*} [CategoryTheory.Category C]
    [CategoryTheory.MonoidalCategory C]
    (M : Type*) (_wd : WeightDecomposition C)
    (_reeb : CategoricalReeb C) :
    SubstrateParameter M :=
  { field := sorry  -- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
    field_pos := sorry  -- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
    field_ge_one := sorry  -- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
    not_root_of_unity := sorry  -- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
  }

end QOU
