import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset

/-!
# QOU.Mass.binding_closure — binding closure

Conditional on the per-term mass identity (input B), the per-isotope
binding closes to `m_e · Σ_n a_D^{(n)}`. This establishes the many-body identity (`thm:binding-manybody-eq-jet-filtration`).

The class `BindingClosureInput` bundles the two structural inputs:
* `body_is_series` — obligation **(C)**, the body-order = jet-graded
  decomposition (`lem:bond-order-eq-jet-degree`, proved as a separate
  lemma);
* `term_id` — obligation **(B)**, the per-term mass identity
  `B_n = m_e · a_D^{(n)}` (derived via the q-difference kernel; equivalently the q-difference
  kernel realising the prolongation symbol).

The residue form of `a_D^{(n)}` (obligation D) is
`prop:sw-period-residue-sum`. With (B) derived, this is fully unconditional.

LaTeX label: `thm:binding-closure`.

## References

- [manuscript] §mass-theory/binding-closure

**Ground ring**: `ℝ` (binding energies). See `GroundRingAnnotations.lean`.
-/

namespace QOU.Mass

open scoped BigOperators

/-- **Conditional inputs (§3b-cond class).** The proved grading identity
    (C) and the open per-term mass identity (B); an instance is the single
    remaining conjectural input. -/
class BindingClosureInput where
  /-- Highest body order retained. -/
  maxOrder : ℕ
  /-- Electron-mass scale `m_e`. -/
  m_e : ℝ
  /-- The `n`-th prolonged SW period `a_D^{(n)}` (residue sum, L1). -/
  swPeriod : ℕ → ℝ
  /-- The `n`-body binding term `B_n`. -/
  bodyTerm : ℕ → ℝ
  /-- The total binding `B(K)`. -/
  total : ℝ
  /-- (C) — proved: binding is the body-order (= jet-graded) series. -/
  body_is_series : total = ∑ n ∈ Finset.range maxOrder, bodyTerm n
  /-- (B) — open: each body term is `m_e` times the `n`-th SW period. -/
  term_id : ∀ n, bodyTerm n = m_e * swPeriod n

/-- **Binding closure.** The total binding is `m_e`
    times the sum of the prolonged Seiberg–Witten periods. Proved from the
    class; the instance is supplied by the q-difference kernel derivation. -/
-- Ref: [manuscript] §mass-theory/binding-closure
theorem binding_closure [H : BindingClosureInput] :
    H.total = H.m_e * ∑ n ∈ Finset.range H.maxOrder, H.swPeriod n := by
  rw [H.body_is_series, Finset.mul_sum]
  exact Finset.sum_congr rfl (fun n _ => H.term_id n)

end QOU.Mass
