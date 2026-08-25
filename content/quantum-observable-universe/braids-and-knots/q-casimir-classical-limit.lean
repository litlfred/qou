import Mathlib.Tactic
import Mathlib.Topology.Algebra.Order.Field
import Mathlib.Order.Filter.Basic
import QOU.MathlibExt.QIntegerCanonical

/-!
# QOU.QCasimir — Classical limit (q → 1) of the q-Casimir eigenvalue

The **archimedean specialisation** (CLAUDE.md §7c) of the generic
q-Casimir construction [`def:q-casimir`](./q-casimir.md): as `q → 1`
over the real field `ℝ`, the symmetric q-number `[n]_q` converges to
`n`, and the Casimir eigenvalue `[j]_q · [j+1]_q` converges to
`j · (j+1)` — the eigenvalue of the classical `𝔰𝔲(2)` Casimir.

This block lives on the **archimedean side of the substrate wall**: it
evaluates the generic `qNumberSym` / `QCasimirEigenvalue` of
`def:q-casimir` at `K := ℝ` and takes the punctured-neighbourhood
limit `𝓝[≠] 1` in the real-order topology (`Tendsto`). Per §7c the
generic algebraic construction stays ℝ-free in `q-casimir.lean`; the
real-analytic limit is separated here.

LaTeX label: `prop:q-casimir-classical-limit`

## References

- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2 §VI.4
- [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9

## Build context

Content-block stub (not in the Lake `QOU/…` graph). It re-states the
`K := ℝ` specialisations of the generic `qNumberSym` /
`QCasimirEigenvalue` of the sibling `q-casimir.lean` (`def:q-casimir`)
locally, so the file typechecks standalone rather than relying on a
cross-block reference the content-block layer cannot resolve as a live
import.
-/

namespace QOU

open Filter Topology
open QOU.QInteger

/-- Symmetric q-number over `ℝ` — the `K := ℝ` specialisation of the
    generic `qNumberSym` of `def:q-casimir`:
    `[n]_q = (qⁿ - q⁻ⁿ)/(q - q⁻¹)`. Re-stated locally so this block
    typechecks standalone. -/
noncomputable abbrev qNumberSym (q : ℝ) (n : ℤ) : ℝ :=
  QOU.QInteger.qIntBalZ q n

/-- q-Casimir eigenvalue over `ℝ` — the `K := ℝ` specialisation of the
    generic `QCasimirEigenvalue` of `def:q-casimir`: `[j]_q · [j+1]_q`. -/
noncomputable def QCasimirEigenvalue (q : ℝ) (j : ℤ) : ℝ :=
  qNumberSym q j * qNumberSym q (j + 1)

/- **Classical limit**: as `q → 1`, the symmetric q-number `[n]_q`
    converges to `n`.  Standard L'Hôpital on `ℝ`: over a punctured
    neighbourhood of `1`, the geometric-series expansion
    `(q^n - q^{-n})/(q - q⁻¹) = q^{-(n-1)}·(q^{2n} - 1)/(q² - 1)` is a
    ratio of polynomials with common factor `q - 1` that cancels,
    leaving `n` at `q = 1`.  Here `qNumberSym` is the generic symmetric
    q-number of `def:q-casimir`, specialised to `K := ℝ`. -/
theorem qNumberSym_classical_limit_nat (n : ℕ) :
    Tendsto (fun q : ℝ => qNumberSym q n) (𝓝[≠] 1) (𝓝 (n : ℝ)) := by
  have h_pos : ∀ᶠ q : ℝ in 𝓝 1, 0 < q := by
    apply IsOpen.mem_nhds isOpen_Ioi
    exact (by positivity : (0 : ℝ) < 1)
  have h_pos2 : ∀ᶠ q : ℝ in 𝓝[≠] 1, 0 < q := nhdsWithin_le_nhds h_pos
  
  have h_eq : (fun q : ℝ => q⁻¹ ^ (n - 1) * ∑ i ∈ Finset.range n, (q ^ 2) ^ i) =ᶠ[𝓝[≠] 1] (fun q => qNumberSym q n) := by
    filter_upwards [h_pos2, self_mem_nhdsWithin] with q hq0' hq1'
    have hq0 : q ≠ 0 := ne_of_gt hq0'
    have hq1 : q ^ 2 ≠ 1 := by
      intro h
      have h2 : q = 1 ∨ q = -1 := sq_eq_one_iff.mp h
      rcases h2 with rfl | rfl
      · exact hq1' rfl
      · linarith
    rw [qNumberSym, qIntBalZ_natCast, qIntBal_eq_twist_canonical q n hq0 hq1, qIntGeo_def]
  
  have h_lim : Tendsto (fun q : ℝ => q⁻¹ ^ (n - 1) * ∑ i ∈ Finset.range n, (q ^ 2) ^ i) (𝓝[≠] 1) (𝓝 ((1 : ℝ)⁻¹ ^ (n - 1) * ∑ i ∈ Finset.range n, ((1 : ℝ) ^ 2) ^ i)) := by
    apply Tendsto.mul
    · refine Tendsto.pow ?_ _
      exact (continuousAt_inv₀ one_ne_zero).tendsto.mono_left nhdsWithin_le_nhds
    · refine tendsto_finset_sum _ (fun i _ => ?_)
      refine Tendsto.pow ?_ _
      refine Tendsto.pow ?_ _
      exact continuous_id.continuousAt.tendsto.mono_left nhdsWithin_le_nhds

  have h_eval : ((1 : ℝ)⁻¹ ^ (n - 1) * ∑ i ∈ Finset.range n, ((1 : ℝ) ^ 2) ^ i) = (n : ℝ) := by
    simp
  
  rw [h_eval] at h_lim
  exact Tendsto.congr' h_eq h_lim

/-- **Theorem (L'Hôpital / polynomial continuity):
    symmetric q-number classical limit `[n]_q → n` as `q → 1`.**
    For `n ≥ 0`, `[n]_q = q^{-(n-1)} (q^{2n} - 1)/(q² - 1) = q^{-(n-1)} ∑ q^{2k}`.
    For `n < 0`, similar logic applies. -/
-- Ref: [kassel1995] §VI.4
-- Ref: [lusztig1993]
theorem qNumberSym_classical_limit (n : ℤ) :
    Tendsto (fun q : ℝ => qNumberSym q n) (𝓝[≠] 1) (𝓝 (n : ℝ)) := by
  cases n with
  | ofNat n => exact qNumberSym_classical_limit_nat n
  | negSucc n =>
      have h_eq : (fun q : ℝ => qNumberSym q (Int.negSucc n)) = fun q : ℝ => -qNumberSym q (n + 1) := by
        ext q
        have : Int.negSucc n = -((n + 1 : ℕ) : ℤ) := rfl
        rw [this, qNumberSym, qNumberSym, qIntBalZ_neg]
        push_cast
        rfl
      rw [h_eq]
      have H := qNumberSym_classical_limit_nat (n + 1)
      have H2 := Tendsto.neg H
      have H3 : -((n + 1 : ℕ) : ℝ) = (Int.negSucc n : ℝ) := by
        push_cast
        rfl
      rw [H3] at H2
      exact H2

/-- **Classical limit of the Casimir eigenvalue**: as `q → 1`,
    `[j]_q · [j+1]_q → j · (j+1)`.  Combines two instances of
    `qNumberSym_classical_limit` with `Filter.Tendsto.mul`. -/
-- Ref: [kassel1995] §VI.4
-- Ref: [lusztig1993]
theorem QCasimirEigenvalue_classical_limit (j : ℤ) :
    Tendsto (fun q : ℝ => QCasimirEigenvalue q j) (𝓝[≠] 1)
      (𝓝 ((j : ℝ) * (j + 1))) := by
  unfold QCasimirEigenvalue
  have hj := qNumberSym_classical_limit j
  have hj1 := qNumberSym_classical_limit (j + 1)
  have hCast : ((j + 1 : ℤ) : ℝ) = (j : ℝ) + 1 := by push_cast; ring
  rw [hCast] at hj1
  exact hj.mul hj1

end QOU
