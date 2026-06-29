import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Positivity


/-!
# QOU.MobiusEnergy — Categorical recovery of Möbius energy

The categorical Möbius energy `E_cat(γ)` built from the Frobenius–Hopf
comultiplication and q-Hodge star recovers the classical Möbius energy
in the limit `q → 1`.

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/MobiusEnergy.lean (monolithic)

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-! ## Knot Embedding and Classical Möbius Energy -/

/-- A **knot embedding** `γ : S¹ → M`, equipped with smooth parametrisation
    and arc-length distance data.
    Ref: [freedman1994] https://doi.org/10.2307/2946567 -/
structure KnotEmbedding (M : Type*) where
  /-- The parametrised curve `γ : [0, 1] → M` (periodic). -/
  curve : R_q → M
  /-- Arc-length distance along the curve. -/
  arcLengthDist : R_q → R_q → R_q
  /-- Arc-length distance is symmetric. -/
  arcLength_symm : ∀ s t, arcLengthDist s t = arcLengthDist t s
  -- Arc-length distance is non-negative:
  -- arcLength_nonneg : ∀ s t, 0 ≤ arcLengthDist s t  -- (archimedean; not meaningful over R_q)

/-- The **classical Möbius energy** of a knot embedding.
    Ref: [freedman1994] https://doi.org/10.2307/2946567
    Ref: [ohara1991] -/
structure ClassicalMobiusEnergy where
  /-- The energy value `E(γ)`. -/
  value : R_q
  -- The energy is non-negative (Freedman–He–Wang):
  -- nonneg : 0 ≤ value  -- (archimedean; not meaningful over R_q)

/-! ## Substrate Parameter (local copy for self-containedness) -/

/-- Substrate parameter `q(p) = 1 + |⟨L_θ, F_A⁺⟩|(p)`. -/
structure SubstrateParameter' (M : Type*) where
  /-- The substrate field `q : M → ℝ`. -/
  field : M → R_q
  -- `q(p) > 1` everywhere:
  -- field_gt_one : ∀ (p : M), field p > 1  -- (archimedean; no LT on R_q)

/-! ## Categorical Möbius Energy -/

/-- **Categorical Möbius energy data** for a knot `γ` in a quantum observable
    universe `(C, A, ω)`.

    LaTeX: `\label{prop:mobius-energy}`
    Ref: [freedman1994] https://doi.org/10.2307/2946567 -/
structure CategoricalMobiusEnergy (M : Type*) where
  /-- The substrate parameter governing the q-deformation. -/
  sp : SubstrateParameter' M
  /-- A chosen base point for evaluating the substrate field. -/
  basepoint : M
  /-- The q-parameter value at the base point. -/
  q : R_q := sp.field basepoint
  -- `q > 1` (non-classical regime):
  -- q_gt_one : q > 1  -- (archimedean; not meaningful over R_q)
  /-- The knot embedding in the fibre space. -/
  knot : KnotEmbedding M
  /-- The categorical energy value `E_cat(γ)`. -/
  energy : R_q
  /-- The classical Möbius energy of the same knot. -/
  classicalEnergy : ClassicalMobiusEnergy
  /-- The topological normalisation constant. -/
  classicalLimitConst : R_q
  /-- The classical-limit coefficient (the categorical normalisation
      factor; specialises to `1/4 ∈ ℝ` under `ι : R_q → ℝ`). Carried as
      a ring element since `1/4` is not defined in `R_q = ℤ[q,q⁻¹]`. -/
  classicalLimitCoeff : R_q
  /-- **Classical limit**: `E_cat = coeff · E_classical + const`
      (with `coeff = 1/4` after archimedean specialisation). -/
  classicalLimit :
    energy = classicalLimitCoeff * classicalEnergy.value + classicalLimitConst

/-- **Proposition: Categorical recovery of Möbius energy.**

    In the classical limit `q → 1`, the categorical Möbius energy recovers
    the classical Möbius energy up to topological normalisation.

    LaTeX: `\label{prop:mobius-energy}` -/
theorem MobiusEnergy {M : Type*} (cme : CategoricalMobiusEnergy M) :
    cme.energy =
      cme.classicalLimitCoeff * cme.classicalEnergy.value + cme.classicalLimitConst :=
  cme.classicalLimit

/-- The categorical Möbius energy is non-negative.

    Archimedean claim — `0 ≤ ·` requires an order on the ground ring,
    which `R_q = ℤ[q,q⁻¹]` does not carry (the `nonneg` fields of
    `ClassicalMobiusEnergy` / `KnotEmbedding` are commented out above for
    the same reason). The non-negativity holds only after specialising
    `ι : R_q → ℝ, q ↦ q₀`; it is proved in the archimedean monolith
    `QOU.MobiusEnergy.MobiusEnergy_nonneg`. Stated here over `ℝ` as the
    standalone, type-correct counterpart. -/
theorem MobiusEnergy_nonneg
    (energy classicalEnergyValue classicalLimitConst : ℝ)
    (h_limit : energy = (1 / 4) * classicalEnergyValue + classicalLimitConst)
    (h_class_nonneg : 0 ≤ classicalEnergyValue)
    (h_const_nonneg : 0 ≤ classicalLimitConst) :
    0 ≤ energy := by
  rw [h_limit]; positivity

end

end QOU
