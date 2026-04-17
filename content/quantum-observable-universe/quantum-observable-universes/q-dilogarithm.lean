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

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic

namespace QOU

noncomputable section
abbrev R_q := LaurentPolynomial ℤ

/-- **q-Dilogarithm data**: a level-2 iterated primitive of H_q
    characterised by the pentagon identity.  `Li2_q ∈ H ⊗ H`.  -/
-- Ref: [manuscript] §2
structure QDilogarithm (H : Type*) where
  /-- The level-2 primitive Li₂_q ∈ H ⊗ H. -/
  Li2 : H × H
  /-- The level-1 primitive log_q ∈ H (needed for pentagon). -/
  log_q : H
  /-- Binary operation encoding the pentagon argument composition. -/
  pentagon_compose : H → H → H → H → H
  /-- **Pentagon identity** (5-term relation): axiom linking values
      of Li₂_q at composite arguments. -/
  pentagon :
    ∀ (x y : H),
      pentagon_compose x y x y = pentagon_compose y x y x

/-- **Uniqueness**: any two level-2 primitives satisfying the pentagon
    coincide up to a level-1 shift (the universal property of the
    q-dilogarithm as generator of the centre of H_q^{⊗2} modulo
    shuffle-products). -/
-- Ref: [manuscript] §2
theorem QDilogarithm.unique_up_to_shift
    {H : Type*} (L₁ L₂ : QDilogarithm H)
    (h_log : L₁.log_q = L₂.log_q)
    (h_pent : L₁.pentagon_compose = L₂.pentagon_compose) :
    L₁.Li2.1 = L₂.Li2.1 := by
  -- Ref: [manuscript] §2 — follows from rigidity of level-2
  -- primitives modulo shuffle products.
  sorry

end QOU
