import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset

/-!
# QOU.Mass.BindingManyBodyJetFiltration — binding series = jet filtration

Conjecture (`conj:binding-manybody-eq-jet-filtration`, step-9b of the
binding-closure workplan): the per-isotope binding energy is the
body-order series whose `n`-th term is `m_e` times the `n`-th prolonged
Seiberg–Witten period (itself a residue sum, `prop:sw-period-residue-sum`),
the body order `n` being the vertical/jet degree.

Per AGENTS.md §3b, the conjecture is **axiomatised as a Lean `class`**:
the existence of an instance is the conjecture; the conditional corollary
below is proved *from* the class hypothesis (fully verified, no `sorry`).

LaTeX label: `conj:binding-manybody-eq-jet-filtration`.

## References

- [manuscript] §mass-theory/binding-manybody-jet-filtration
- [seiberg1994] https://doi.org/10.1016/0550-3213(94)90124-4

**Ground ring**: generic `[CommRing R]` for the algebraic identity; the
SW periods are realised over `ℝ`/`ℂ` post-`τ`. See `GroundRingAnnotations.lean`.
-/

namespace QOU.Mass

open scoped BigOperators

/-- **Conjecture class.** Encodes
    `B(K) = Σ_{n<maxOrder} B_n`, `B_n = m_e · a_D^{(n)}`, with the SW
    periods `a_D^{(n)}` supplied by `prop:sw-period-residue-sum`. An
    instance asserts the conjecture for the carrier `R`. -/
class BindingManyBodyJetFiltration (R : Type*) [CommRing R] where
  /-- The electron-mass scale `m_e`. -/
  m_e : R
  /-- Highest body order retained in the truncation. -/
  maxOrder : ℕ
  /-- The `n`-th prolonged SW period `a_D^{(n)} = ∮ λ_SW^{(n)}`
      (a residue sum over hyperbolic components, `prop:sw-period-residue-sum`). -/
  swPeriod : ℕ → R
  /-- The `n`-body binding term `B_n`. -/
  bodyTerm : ℕ → R
  /-- The total binding `B(K)`. -/
  binding : R
  /-- Each `n`-body term is `m_e` times the `n`-th SW period. -/
  term_eq : ∀ n, bodyTerm n = m_e * swPeriod n
  /-- Binding is the body-order series (= the jet-order filtration). -/
  series_eq : binding = ∑ n ∈ Finset.range maxOrder, bodyTerm n

/-- **Conditional corollary** (proved from the conjecture class, no `sorry`):
    binding equals `m_e` times the truncated sum of Seiberg–Witten periods. -/
theorem binding_eq_me_sw_series {R : Type*} [CommRing R]
    [B : BindingManyBodyJetFiltration R] :
    B.binding = B.m_e * ∑ n ∈ Finset.range B.maxOrder, B.swPeriod n := by
  rw [B.series_eq, Finset.mul_sum]
  exact Finset.sum_congr rfl (fun n _ => B.term_eq n)

end QOU.Mass
