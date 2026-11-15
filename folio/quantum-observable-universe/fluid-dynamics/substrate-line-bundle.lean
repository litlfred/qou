import Mathlib.Data.Real.Basic

-- Ref: [leitner2026] Ch. 7, §substrate-line-bundle
-- Substrate line bundle L_θ

/-- The **substrate line bundle** L_θ associated to the substrate
    parameter field θ : M → ℝ_{>1}.

    This is the pullback of the canonical line bundle on ℝ_{>1}
    along θ. Sections of L_θ encode q-dependent quantities. -/
structure SubstrateLineBundle where
  /-- Base manifold dimension. -/
  dim : Nat
  /-- The substrate parameter is bounded below by 1. -/
  q_lower_bound : ℝ := 1
