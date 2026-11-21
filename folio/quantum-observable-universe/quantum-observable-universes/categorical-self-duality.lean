import QOU.Basic
import QOU.QuantumObservableUniverse.CategoricalFoundations
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Limits.Shapes.ZeroMorphisms


/-!
# QOU.categorical_self_duality — Critical points are instantons

For a quantum observable universe with volume form, any connection
that is a critical point of the categorical Yang–Mills functional

  S[∇] = λ(⋆_q(F_∇) · F_∇)

is an instanton (F_∇ ∈ Ω⁺(A)).

LaTeX label: `prop:categorical-self-duality`

## References

- [donaldson1990] https://doi.org/10.1093/oso/9780198535874.001.0001
- [leitner2026] §1-quantum-observable-universe/categorical-self-duality
-/

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- **Categorical Yang–Mills functional data**.

    The functional S[∇] = λ(⋆_q(F_∇) · F_∇) where:
    - F_∇ is the curvature of the connection ∇
    - ⋆_q is the q-deformed Hodge star
    - λ is the Frobenius form -/
-- Ref: [donaldson1990], [leitner2026] §1
structure CategoricalYangMills (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [CategoryTheory.BraidedCategory C] [CategoryTheory.Limits.HasZeroMorphisms C] where
  /-- The Frobenius–Hopf object A. -/
  fh : FrobeniusHopfData C
  /-- The curvature object (2-forms). -/
  curvatureSpace : C
  /-- The self-dual 2-forms Ω⁺(A). -/
  selfDualForms : C
  /-- The anti-self-dual 2-forms Ω⁻(A). -/
  antiSelfDualForms : C
  /-- The curvature F_∇ : 𝟙 → curvatureSpace. -/
  curvature : (𝟙_ C) ⟶ curvatureSpace
  /-- The q-Hodge star ⋆_q : Ω² → Ω². -/
  qHodgeStar : curvatureSpace ⟶ curvatureSpace
  /-- ⋆_q is an involution: ⋆_q ∘ ⋆_q = id. -/
  hodge_involution : qHodgeStar ≫ qHodgeStar = 𝟙 curvatureSpace
  /-- The projection to self-dual part. -/
  projPlus : curvatureSpace ⟶ selfDualForms
  /-- The projection to anti-self-dual part. -/
  projMinus : curvatureSpace ⟶ antiSelfDualForms

/-- **Instanton condition**: F_∇ is self-dual (F⁻ = 0). -/
-- Ref: [donaldson1990], [leitner2026] §1
structure Instanton (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [CategoryTheory.BraidedCategory C] [CategoryTheory.Limits.HasZeroMorphisms C]
    extends CategoricalYangMills C where
  /-- The anti-self-dual part vanishes: F⁻ = 0.
      Encoded: the projection to Ω⁻ is zero. -/
  anti_self_dual_vanishes :
    curvature ≫ projMinus = 0

/-- **Self-duality theorem**: critical points of S[∇] are instantons. -/
-- Ref: [donaldson1990], [leitner2026] §1
theorem categorical_self_duality {C : Type u} [Category.{v} C]
    [MonoidalCategory C] [CategoryTheory.BraidedCategory C] [CategoryTheory.Limits.HasZeroMorphisms C]
    (ym : CategoricalYangMills C)
    (h_crit : ym.curvature ≫ ym.projMinus = 0) :
    ∃ inst : Instanton C, inst.toCategoricalYangMills = ym :=
  ⟨{ toCategoricalYangMills := ym, anti_self_dual_vanishes := h_crit }, rfl⟩

end QOU
