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

- [leitner2026] §2-quantum-observable-universes/categorical-q-ext-deriv-unique
- [majid2002] A Quantum Groups Primer (Cambridge UP), §5
-/

namespace QOU

open CategoryTheory

universe u v

/-- **Inverses are unique in a commutative monoid.**  Used below to show
    the `qinv` field is *determined* rather than free: it needs no
    hypothesis of its own. -/
private theorem inv_unique_of_mul_eq_one {R : Type*} [CommMonoid R] {q a b : R}
    (ha : q * a = 1) (hb : q * b = 1) : a = b :=
  calc a = a * (q * b) := by rw [hb, mul_one]
    _ = (a * q) * b := (mul_assoc _ _ _).symm
    _ = 1 * b := by rw [mul_comm a q, ha]
    _ = b := one_mul b

/-- **Uniqueness of the categorical q-exterior derivative (proved
    extensionality).**

    Two `CategoricalQExtDeriv C` instances with the same Frobenius–Hopf
    object and the same data `(d, π_V, q)` are equal.

    Note there is deliberately **no hypothesis about `qinv`**, even
    though it is a data field. It is determined: `q * qinv = 1` and an
    inverse in a commutative monoid is unique. The structure acquired
    `qinv` when `q_ne_zero` was replaced by `q * qinv = 1` — `R_q =
    ℤ[q, q⁻¹]` is a ring with no `Inv` instance, so the inverse must be
    carried as data — and this file's `rfl` was left behind by that
    migration. Adding a `qinv` hypothesis would have made the file
    compile while weakening the theorem; deriving it keeps the
    statement as strong as the narrative claims.

    Historically this also replaced a **false** `axiom : Subsingleton
    (CategoricalQExtDeriv C)`: the structure bundles its object and
    carries free data, so distinct instances plainly exist. -/
-- Ref: [majid2002] A Quantum Groups Primer (Cambridge UP), §5
theorem CategoricalQExtDeriv.unique
    (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    (E₁ E₂ : CategoricalQExtDeriv C)
    (hfh : E₁.frobHopf = E₂.frobHopf)
    (hd : HEq E₁.d_classical E₂.d_classical)
    (hpv : HEq E₁.proj_V E₂.proj_V)
    (hq : E₁.q = E₂.q) : E₁ = E₂ := by
  obtain ⟨fh₁, d₁, p₁, qq₁, qi₁, hqi₁, hpi₁⟩ := E₁
  obtain ⟨fh₂, d₂, p₂, qq₂, qi₂, hqi₂, hpi₂⟩ := E₂
  simp only at hfh hd hpv hq
  subst hfh
  rw [heq_iff_eq] at hd hpv
  subst hd
  subst hpv
  subst hq
  -- `qinv` is data and no hypothesis mentions it, so `rfl` alone cannot
  -- close this.  It is nonetheless determined by `q * qinv = 1`.
  obtain rfl : qi₁ = qi₂ := inv_unique_of_mul_eq_one hqi₁ hqi₂
  rfl

/-- **The derived q-derivative is determined by the data (proved).**
    Given the same Frobenius–Hopf object and the same `(d, π_V, q)`,
    the derived morphism `d_q = q⁻¹ d + (1 − q⁻¹) π_V ≫ d` agrees. -/
-- Ref: [majid2002] A Quantum Groups Primer (Cambridge UP), §5
theorem CategoricalQExtDeriv.dq_determined
    (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    [Preadditive C]
    -- `Linear ℝ C` before the ground-ring migration; `dq` is now built over
    -- `R_q = ℤ[q, q⁻¹]`, so the linearity has to be over the same ring —
    -- `failed to synthesize Linear GroundRing.R_q C` otherwise.
    [Linear QOU.GroundRing.R_q C]
    (E₁ E₂ : CategoricalQExtDeriv C)
    (hfh : E₁.frobHopf = E₂.frobHopf)
    (hd : HEq E₁.d_classical E₂.d_classical)
    (hpv : HEq E₁.proj_V E₂.proj_V)
    (hq : E₁.q = E₂.q) :
    HEq E₁.dq E₂.dq := by
  rw [CategoricalQExtDeriv.unique C E₁ E₂ hfh hd hpv hq]

end QOU
