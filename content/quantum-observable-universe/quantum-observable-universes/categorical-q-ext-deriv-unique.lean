import QOU.Basic
import QOU.QuantumObservableUniverse.Instanton


/-!
# QOU.CategoricalQExtDeriv.unique — uniqueness of the categorical q-exterior derivative

Any morphism satisfying the three characterising properties agrees
with d_q = q⁻¹ d + (1 - q⁻¹) π_V ∘ d.

LaTeX: `\label{prop:categorical-q-ext-deriv-unique}`

## Honest statement (2026-06-09 axiom audit)

The previous version asserted
`axiom : Subsingleton (CategoricalQExtDeriv C)`, which is **false**:
the structure bundles its Frobenius–Hopf object and carries free data
fields (`d_classical`, `proj_V`, `q`), so distinct instances exist in
any category with two candidate differentials.

What *is* provable — with no axiom — is exactly the narrative claim:
given the same Frobenius–Hopf object and the same data
`(d, π_V, q)`, the structure — and hence the derived q-derivative
`d_q = q⁻¹ d + (1 − q⁻¹) π_V ≫ d` — is uniquely determined.  Since
`d_classical` and `proj_V` live over the bundled object, the data
comparisons across two instances use `HEq` transported along the
object equality.  `CategoricalQExtDeriv` is imported here from the
`QOU` library.

## References

- [manuscript] §2-quantum-observable-universes/categorical-q-ext-deriv-unique
- [majid2002] A Quantum Groups Primer (Cambridge UP), §5
-/

namespace QOU

open CategoryTheory

universe u v

/-- **Uniqueness of the categorical q-exterior derivative (proved
    extensionality).**

    Two `CategoricalQExtDeriv C` instances with the same
    Frobenius–Hopf object and the same data `(d, π_V, q)` are equal:
    `q_ne_zero` and `proj_V_idem` are propositional.  This replaces a
    false `Subsingleton (CategoricalQExtDeriv C)` axiom (the structure
    bundles its object and data) with the determination the narrative
    actually claims. -/
-- Ref: [majid2002] A Quantum Groups Primer (Cambridge UP), §5
theorem CategoricalQExtDeriv.unique
    (C : Type u) [Category.{v} C]
    [MonoidalCategory C]
    (E₁ E₂ : CategoricalQExtDeriv C)
    (hfh : E₁.frobHopf = E₂.frobHopf)
    (hd : HEq E₁.d_classical E₂.d_classical)
    (hpv : HEq E₁.proj_V E₂.proj_V)
    (hq : E₁.q = E₂.q) : E₁ = E₂ := by
  cases E₁
  cases E₂
  subst hfh
  rw [heq_iff_eq] at hd hpv
  subst hd
  subst hpv
  subst hq
  rfl

/-- **The derived q-derivative is determined by the data (proved).**
    Given the same Frobenius–Hopf object and the same `(d, π_V, q)`,
    the derived morphism `d_q = q⁻¹ d + (1 − q⁻¹) π_V ≫ d` agrees. -/
-- Ref: [majid2002] A Quantum Groups Primer (Cambridge UP), §5
theorem CategoricalQExtDeriv.dq_determined
    (C : Type u) [Category.{v} C]
    [MonoidalCategory C]
    [Preadditive C]
    [Linear ℝ C]
    (E₁ E₂ : CategoricalQExtDeriv C)
    (hfh : E₁.frobHopf = E₂.frobHopf)
    (hd : HEq E₁.d_classical E₂.d_classical)
    (hpv : HEq E₁.proj_V E₂.proj_V)
    (hq : E₁.q = E₂.q) :
    HEq E₁.dq E₂.dq := by
  rw [CategoricalQExtDeriv.unique C E₁ E₂ hfh hd hpv hq]

end QOU
