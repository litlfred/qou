import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring


/-!
# QOU.HopfSymmetric.hopf_symmetric_decomposition

The Hopf link `𝓛_H = T_{2,2} = closure(σ₁²)` of the 2-strand inter-molecular
Hecke algebra `H_2(q)` decomposes over the two Wedderburn blocks. Writing the
(unnormalised) block projectors `E₊ = σ + q⁻¹` (symmetric / trivial rep,
`σ ↦ q`) and `E₋ = q − σ` (antisymmetric / sign rep, `σ ↦ −q⁻¹`), the Hopf
element weights them by the squared block eigenvalues `q²` and `q⁻²`:

  `[2]_q · σ² = q²·(σ + q⁻¹) + q⁻²·(q − σ)`,   `[2]_q = q + q⁻¹`,

cleared of the `[2]_q` denominator (so it holds over any field with `q ≠ 0`).
Equivalently `σ² = q²·e₊ + q⁻²·e₋` with the normalised idempotents
`e± = E±/[2]_q`. The symmetric (Hopf/[2]_q) block is the **van der Waals**
channel ([`def:van-der-waals-hopf-channel`](van-der-waals-hopf-channel.md)).

LaTeX label: `prop:hopf-link-symmetric-decomposition`.
**Ground ring**: a field `R` (so `q⁻¹` exists); the identity is purely
algebraic in `σ` modulo the Hecke relation.
-/

namespace QOU.HopfSymmetric

variable {R : Type*} [Field R]

/-- **Hopf-link symmetric/antisymmetric decomposition.**

    Given the 2-strand Hecke relation `σ² = (q − q⁻¹)·σ + 1`, the Hopf element
    `σ²` decomposes over the two block projectors `(σ + q⁻¹)` and `(q − σ)`
    with weights `q²` and `q⁻²` (the squared block eigenvalues), after clearing
    the `[2]_q = q + q⁻¹` denominator. Sorry-free. -/
-- Ref: [manuscript] information-theory/hopf-link-symmetric-decomposition
theorem hopf_symmetric_decomposition (q σ : R) (hq : q ≠ 0)
    (hHecke : σ ^ 2 = (q - q⁻¹) * σ + 1) :
    (q + q⁻¹) * σ ^ 2 = q ^ 2 * (σ + q⁻¹) + (q⁻¹) ^ 2 * (q - σ) := by
  rw [hHecke]
  field_simp
  ring

end QOU.HopfSymmetric
