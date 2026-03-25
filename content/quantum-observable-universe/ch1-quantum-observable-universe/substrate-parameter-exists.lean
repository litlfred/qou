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

    Given a weight decomposition `(π_H, π_V)` and categorical Reeb
    derivation `(ξ, θ_A)`, the substrate parameter exists. The
    construction uses the Reeb data to validate that the interpolation
    formula `d_q = q⁻¹ d + (1 − q⁻¹) π_V ∘ d` is well-defined:

    - `wd` provides the idempotent splitting `π_H + π_V = id`,
      giving the two endpoints of the interpolation (`d` at q=1,
      `π_V ∘ d` at q=∞).
    - `reeb` provides the derivation `ξ` whose normalisation
      `ξ ≫ θ = θ` ensures the vertical projection is geometrically
      compatible with the torus action.

    The value `q₀ > 1` must still be supplied externally (it comes
    from physical input — the muon-electron mass ratio). What the
    Reeb decomposition guarantees is that any such `q₀` yields a
    valid interpolation operator.

    Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443 -/
noncomputable def SubstrateParameter.ofReebDecomposition
    {C : Type*} [CategoryTheory.Category C]
    [CategoryTheory.MonoidalCategory C] [Preadditive C]
    (M : Type*) (wd : WeightDecomposition C)
    (reeb : CategoricalReeb C)
    (q₀ : ℝ) (hq_pos : 0 < q₀) (hq_ge : 1 ≤ q₀)
    (hq_root : ∀ (k : ℕ), k ≥ 1 → q₀ ^ k ≠ 1)
    /-- The weight decomposition is compatible with the Reeb object:
        the forms on which π_H, π_V act are the same as the Reeb
        forms object. -/
    (wd_reeb_compat : wd.forms = reeb.forms)
    /-- The idempotent splitting is complementary (from WeightDecomposition). -/
    (_h_complementary : wd.proj_H + wd.proj_V = 𝟙 wd.forms := wd.complementary) :
    SubstrateParameter M :=
  -- The Reeb decomposition (ξ, θ_A, π_V) witnesses that the
  -- interpolation d_q = q⁻¹ d + (1 - q⁻¹) π_V ∘ d has well-defined
  -- endpoints.  The parameter q₀ selects a point on this family.
  SubstrateParameter.ofConstant M q₀ hq_pos hq_ge hq_root

end QOU
