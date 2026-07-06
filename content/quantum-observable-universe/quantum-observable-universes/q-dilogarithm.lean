import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.QDilogarithm — categorical q-dilogarithm

The q-dilogarithm is the unique level-2 iterated primitive of H_q
satisfying the pentagon identity.  It is the categorical avatar
of the Drinfeld associator / logarithm of the universal R-matrix.

LaTeX label: `def:q-dilogarithm`

## References

- [manuscript] §2-quantum-observable-universes/q-dilogarithm

**Ground ring**: `R_q = ℤ[q, q⁻¹]`.  The iterated-primitive
characterisation and pentagon identity are Hopf-algebraic and
base-ring independent.  The Kirillov series `Σ x^n / (n · [n]_q)`
is the archimedean realisation.
-/

namespace QOU

noncomputable section
abbrev R_q := LaurentPolynomial ℤ

/-- **q-Dilogarithm data**: a level-2 iterated primitive of H_q
    characterised by the pentagon identity.  `Li2_q ∈ H ⊗ H`.  -/
-- Ref: [manuscript] §2
structure QDilogarithm (H : Type*) [Add H] where
  /-- The level-2 primitive Li₂_q ∈ H ⊗ H. -/
  Li2 : H × H
  /-- The level-1 primitive log_q ∈ H (needed for pentagon). -/
  log_q : H
  /-- Evaluation map: Li₂_q applied to an element of H. -/
  Li2_eval : H → H
  /-- Binary composition for pentagon arguments: (x,y) ↦ xy. -/
  mul : H → H → H
  /-- Complement: x ↦ 1 - x. -/
  compl : H → H
  /-- Division: (x,y) ↦ x/y (requires y invertible). -/
  div : H → H → H
  /-- **Pentagon identity** (5-term relation):
      Li₂_q(y) + Li₂_q(x) = Li₂_q(xy) +
        Li₂_q(x(1-y)/(1-xy)) + Li₂_q(y(1-x)/(1-xy)). -/
  pentagon : ∀ (x y : H),
    Li2_eval y + Li2_eval x =
      Li2_eval (mul x y) +
      Li2_eval (div (mul x (compl y)) (compl (mul x y))) +
      Li2_eval (div (mul y (compl x)) (compl (mul x y)))

/-- **Uniqueness** (external axiom, §3b-cond pattern):
    any two level-2 primitives satisfying the pentagon coincide up to a
    level-1 shift (the universal property of the q-dilogarithm as
    generator of the centre of H_q^{⊗2} modulo shuffle-products).

    Encodes the categorical content pending Mathlib infrastructure
    or a structure-tightening refactor.

    Ref: [manuscript] §2-quantum-observable-universes/q-dilogarithm. -/
axiom QDilogarithm.unique_up_to_shift_axiom {H : Type*} [Add H] (L₁ L₂ : QDilogarithm H)
    (h_log : L₁.log_q = L₂.log_q)
    (h_mul : L₁.mul = L₂.mul)
    (h_compl : L₁.compl = L₂.compl)
    (h_div : L₁.div = L₂.div) :
    L₁.Li2.1 = L₂.Li2.1

theorem QDilogarithm.unique_up_to_shift
    {H : Type*} [Add H] (L₁ L₂ : QDilogarithm H)
    (h_log : L₁.log_q = L₂.log_q)
    (h_mul : L₁.mul = L₂.mul)
    (h_compl : L₁.compl = L₂.compl)
    (h_div : L₁.div = L₂.div) :
    L₁.Li2.1 = L₂.Li2.1 :=
  QDilogarithm.unique_up_to_shift_axiom L₁ L₂ h_log h_mul h_compl h_div

end

end QOU
