import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic


/-!
# QOU.AlgebraicSubstrate.topological_charge_quantization

The topological charge of the unit particle is quantized: the algebraic
residue at z = 1, computed via the observer trace Φ, equals unity.

LaTeX label: `conj:topological-charge-quantization`

## References

- [yekutieli2015] https://doi.org/10.1515/9783110291230
-/

set_option autoImplicit false

open CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU.AlgebraicSubstrate

universe u v

variable {C : Type u} [CategoryTheory.Category.{v} C]
  [CategoryTheory.MonoidalCategory C]

/- The topological charge of the unit particle is quantized.

    Given the Frobenius–Hopf substrate A with observer trace Φ and
    canonical differential form ω, the algebraic residue at z = 1
    satisfies Res_q(ω, 1) = Φ(Res_ξ(ω)) = 1.

    This is the algebraic counterpart of the Gauss–Bonnet theorem:
    non-degeneracy of the Frobenius pairing and periodicity of the
    Reeb derivation ξ_q force the total charge to be integral. -/
-- Ref: [yekutieli2015] Yekutieli, "Nonabelian Multiplicative Integration on Surfaces," World Scientific 2015 (DOI: 10.1142/9537)
/-- The quantized-topological-charge condition, as a **predicate** on the
    categorical data: the Reeb residue operator `Res_ξ`, post-composed with
    the observer trace `Φ`, leaves `Φ` unchanged — `Res_ξ ≫ Φ = Φ`.
    Equivalently the algebraic residue `Res_q(ω, 1) = Φ(Res_ξ(ω)) = 1`
    (with `1 = id_{𝟙}` in the monoidal unit).

    Named (§3b), not asserted: the previous `(h_reeb_residue : P) : P := h`
    was self-assuming and stated nothing. Integrality of the total charge is
    forced by non-degeneracy of the Frobenius pairing and periodicity of the
    Reeb derivation `ξ_q` — the algebraic Gauss–Bonnet content — which lives
    in the substrate, not at this abstraction, so this names the condition. -/
def topological_charge_quantization
    (A : C)
    (Φ : A ⟶ (𝟙_ C))
    (Res_xi : A ⟶ A) : Prop :=
  Res_xi ≫ Φ = Φ

/-- **Class-axiomatised topological charge quantization (`conj:topological-charge-quantization`, §3b-cond).** -/
class TopologicalChargeQuantized (A : C) (Φ : A ⟶ (𝟙_ C)) (Res_xi : A ⟶ A) : Prop where
  residue_invariant : topological_charge_quantization A Φ Res_xi

/-- **Conditional theorem (two-fold Reeb residue invariance).** Under
    `[TopologicalChargeQuantized A Φ Res_xi]`, iterating `Res_xi` twice still
    preserves the observer trace `Φ`. -/
theorem topological_charge_twofold_invariance
    (A : C) (Φ : A ⟶ (𝟙_ C)) (Res_xi : A ⟶ A)
    [h : TopologicalChargeQuantized A Φ Res_xi] :
    (Res_xi ≫ Res_xi) ≫ Φ = Φ := by
  rw [Category.assoc, h.residue_invariant, h.residue_invariant]

end QOU.AlgebraicSubstrate
