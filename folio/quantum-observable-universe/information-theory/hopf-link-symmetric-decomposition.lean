import Mathlib.Algebra.Ring.Units
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring


/-!
# QOU.HopfSymmetric.hopf_symmetric_decomposition

The Hopf link `𝓛_H = T_{2,2} = closure(σ₁²)` of the 2-strand inter-molecular
Hecke algebra `H_2(q)` decomposes over the two Wedderburn blocks. Writing the
(unnormalised) block projectors `E₊ = σ + q⁻¹` (symmetric / trivial rep,
`σ ↦ q`) and `E₋ = q − σ` (antisymmetric / sign rep, `σ ↦ −q⁻¹`), the Hopf
element weights them by the squared block eigenvalues `q²` and `q⁻²`:

  `[2]_q · σ² = q²·(σ + q⁻¹) + q⁻²·(q − σ)`,   `[2]_q = q + q⁻¹`,

cleared of the `[2]_q` denominator.

Equivalently `σ² = q²·e₊ + q⁻²·e₋` with the normalised idempotents
`e± = E±/[2]_q`. The symmetric (Hopf/[2]_q) block is the **van der Waals**
channel ([`def:van-der-waals-hopf-channel`](van-der-waals-hopf-channel.md)).

LaTeX label: `prop:hopf-link-symmetric-decomposition`.

**Ground ring** (AGENTS.md §7c): `ℤ[q, q⁻¹]`, i.e. a generic
`{R : Type*} [CommRing R]` with the modulus carried as a **unit** `q : Rˣ`,
so every `q⁻¹` is a `Units` coercion `↑q⁻¹` and no ring inverse, division or
field appears. The identity is purely algebraic in `σ` modulo the Hecke
relation: after substituting it, the whole content is the single unit
relation `q·q⁻¹ = 1`, which is what the `linear_combination` certificate
below records. (Previously stated over a field with `q ≠ 0` and discharged
by `field_simp`; the field was only clearing the `[2]_q` denominator that
the statement has already cleared by hand.)
-/

namespace QOU.HopfSymmetric

variable {R : Type*} [CommRing R]

/-- **Hopf-link symmetric/antisymmetric decomposition.**

    Given the 2-strand Hecke relation `σ² = (q − q⁻¹)·σ + 1`, the Hopf element
    `σ²` decomposes over the two block projectors `(σ + q⁻¹)` and `(q − σ)`
    with weights `q²` and `q⁻²` (the squared block eigenvalues), after clearing
    the `[2]_q = q + q⁻¹` denominator. Sorry-free. -/
-- Ref: [leitner2026] information-theory/hopf-link-symmetric-decomposition
theorem hopf_symmetric_decomposition (q : Rˣ) (σ : R)
    (hHecke : σ ^ 2 = ((q : R) - (↑q⁻¹ : R)) * σ + 1) :
    ((q : R) + (↑q⁻¹ : R)) * σ ^ 2
      = (q : R) ^ 2 * (σ + (↑q⁻¹ : R))
        + (↑q⁻¹ : R) ^ 2 * ((q : R) - σ) := by
  have hq : (q : R) * (↑q⁻¹ : R) = 1 := q.mul_inv
  rw [hHecke]
  linear_combination (-((q : R) + (↑q⁻¹ : R))) * hq

end QOU.HopfSymmetric
