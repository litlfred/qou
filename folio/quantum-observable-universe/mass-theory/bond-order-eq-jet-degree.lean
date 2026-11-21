import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# QOU.Mass.bodyorder_eq_jet_total — body order = jet degree

Workplan obligation **(C)** of `conj:binding-manybody-eq-jet-filtration`.
The canonical atomic braid's body-order (cluster) filtration coincides
with the Gröbner–Shirshov / jet-prefix filtration: the `n`-nucleon
cluster term is the degree-`n` associated-graded component `gr_n`. Hence
the body-order series equals the jet-graded total.

The grading match (Steps 1–2 of the proof) and exhaustiveness are
packaged as the structure hypothesis (`prop:gb-spectral-sequence`,
`conj:jet-prefix-gb-filtration`), so the series identity is extracted
sorry-free.

LaTeX label: `conj:bond-order-eq-jet-degree`.

## References

- [leitner2026] §mass-theory/bond-order-eq-jet-degree

**Ground ring**: `ℝ` (binding energies). See `GroundRingAnnotations.lean`.
-/

namespace QOU.Mass

open scoped BigOperators

/-- **Body-order / jet-grading data**: the body-order (cluster) terms, the
    GB/jet associated-graded components `gr_n`, the total binding, the
    degree-wise match `bodyTerm n = gradedTerm n` (Steps 1–2), and the
    exhaustiveness `total = Σ gr_n`. -/
structure BodyOrderJetGrading where
  /-- Highest cluster (body) order retained. -/
  maxOrder : ℕ
  /-- The degree-`n` GB/jet associated-graded component `gr_n`. -/
  gradedTerm : ℕ → ℝ
  /-- The `n`-nucleon cluster (body) contribution. -/
  bodyTerm : ℕ → ℝ
  /-- The total binding. -/
  total : ℝ
  /-- Step 1–2: the `n`-body term IS the degree-`n` graded component. -/
  body_eq_graded : ∀ n, bodyTerm n = gradedTerm n
  /-- Exhaustiveness: the total is the sum of graded components. -/
  total_eq : total = ∑ n ∈ Finset.range maxOrder, gradedTerm n

/-- **(C).** The total binding is the body-order series — the cluster
    filtration coincides with the jet-graded filtration. -/
-- Ref: [leitner2026] §mass-theory/bond-order-eq-jet-degree
theorem bodyorder_eq_jet_total (S : BodyOrderJetGrading) :
    S.total = ∑ n ∈ Finset.range S.maxOrder, S.bodyTerm n := by
  rw [S.total_eq]
  exact (Finset.sum_congr rfl (fun n _ => (S.body_eq_graded n))).symm

end QOU.Mass
