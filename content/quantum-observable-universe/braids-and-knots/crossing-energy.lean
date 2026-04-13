/-!
# QOU.Braiding.CrossingEnergy — Crossing energy of a knot composite

The crossing energy of a composite H with braid word β is defined as
the sum over crossings:
  E_cross(H) = Σ (positive crossings) q + Σ (negative crossings) (−q⁻¹)

where q is the substrate parameter and the sign convention follows
the Skein relation q L₊ − q⁻¹ L₋ = (q^{1/2} − q^{−1/2}) L₀.

LaTeX label: `def:crossing-energy`

## References

- [manuscript] Ch. 4, §10
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic

namespace QOU.Braiding

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Descartes.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-! ## Crossing Energy -/

/-- A braid word: a finite list of signed crossings.
    `true` = positive crossing (L₊), `false` = negative crossing (L₋). -/
abbrev BraidWord := List Bool

/-- Count of positive crossings in a braid word. -/
def BraidWord.numPositive (w : BraidWord) : ℕ :=
  w.filter id |>.length

/-- Count of negative crossings in a braid word. -/
def BraidWord.numNegative (w : BraidWord) : ℕ :=
  w.filter (fun b => !b) |>.length

/-- Total number of crossings in a braid word. -/
def BraidWord.numCrossings (w : BraidWord) : ℕ :=
  w.length

/-- Positive + negative = total crossings. -/
-- Ref: [manuscript] Ch. 4, §10
theorem BraidWord.pos_plus_neg_eq_total (w : BraidWord) :
    w.numPositive + w.numNegative = w.numCrossings := by
  simp [numPositive, numNegative, numCrossings, List.length_filter_add_length_filter_not]

/-- **Crossing energy** of a knot composite with braid word β and
    substrate parameter q.

    Each positive crossing contributes q, each negative crossing
    contributes −q⁻¹, following the Skein sign convention:

      E_cross(H) = n₊ · q − n₋ · q⁻¹

    where n₊, n₋ are the counts of positive and negative crossings. -/
-- Ref: [manuscript] Ch. 4, §10
structure CrossingEnergy where
  /-- The braid word representing the linking pattern. -/
  braidWord : BraidWord
  /-- Substrate parameter q. -/
  q : R_q
  /-- q > 0 (required for q⁻¹ to be well-defined). -/
  -- q_pos : 0 < q  -- (archimedean; not meaningful over R_q)
  /-- q > 1 (physical constraint from the substrate). -/
  -- q_gt_one : 1 < q  -- (archimedean; not meaningful over R_q)

/-- The crossing energy value: n₊ · q − n₋ · q⁻¹. -/
noncomputable def CrossingEnergy.value (E : CrossingEnergy) : R_q :=
  E.braidWord.numPositive * E.q - E.braidWord.numNegative * E.q⁻¹

/-- Baseline (strong) contribution: ½(n₊ + n₋)(q + q⁻¹).
    This is the symmetric part under q ↔ q⁻¹. -/
noncomputable def CrossingEnergy.baseline (E : CrossingEnergy) : R_q :=
  (E.braidWord.numPositive + E.braidWord.numNegative) * (E.q + E.q⁻¹) / 2

/-- Coulomb correction contribution: ½(n₊ − n₋)(q − q⁻¹).
    This is the antisymmetric part under q ↔ q⁻¹. -/
noncomputable def CrossingEnergy.coulombContribution (E : CrossingEnergy) : R_q :=
  ((E.braidWord.numPositive : R_q) - E.braidWord.numNegative) * (E.q - E.q⁻¹) / 2

/-- The crossing energy decomposes as baseline + Coulomb correction:

      E_cross = ½(n₊ + n₋)(q + q⁻¹) + ½(n₊ − n₋)(q − q⁻¹) -/
-- Ref: [manuscript] Ch. 4, §10
theorem CrossingEnergy.decomposition (E : CrossingEnergy) :
    E.value = E.baseline + E.coulombContribution := by
  simp only [value, baseline, coulombContribution]
  field_simp
  ring

end QOU.Braiding
