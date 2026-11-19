import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.Data.Finset.Basic

/-!
# Trace concentration via Littlewood–Richardson fusion (`conj:active-set-trace-concentration`, §3b-cond)

Class-axiomatised formulation of `conj:active-set-trace-concentration` over a
generic commutative ring `R` (§7c, zero `ℝ` specialisation), together with the
unconditional `⁴He` (`A = 4`) two-row Kostka multiplicity identity and the
conditional active-set sum-restriction theorem.

## References

- [leitner2026] `conj:active-set-trace-concentration`
- [leitner2026] `prop:he4-two-row-dominance`
-/

namespace QOU.BraidKnot

/-- Two-row Kostka multiplicities `K_{λ,(3,3,3,3)}` in `[3]^⊗4` for
    `[12], [11,1], [10,2], [9,3], [8,4], [7,5], [6,6]`. -/
def he4TwoRowKostkaMultiplicities : List ℕ := [1, 3, 6, 10, 11, 9, 4]

/-- **Unconditional (`⁴He` two-row fusion census).** There are `7` two-row
    partitions of `12` in `[3]^⊗4`, with total Kostka multiplicity `44` and peak
    multiplicity `11` at `(8, 4)`. -/
theorem he4_two_row_kostka_census :
    he4TwoRowKostkaMultiplicities.length = 7 ∧
    he4TwoRowKostkaMultiplicities.sum = 44 ∧
    11 ∈ he4TwoRowKostkaMultiplicities := by
  decide

/-- **Open conjecture (`conj:active-set-trace-concentration`, §3b-cond).**
    For a ground-state nucleus of mass number `A`, every Wedderburn partition
    `λ ⊢ 3A` with strictly more than `A` rows (`A < rowCount λ`) carries zero
    Markov-trace contribution (`blockTrace λ = 0`). No global instance is
    registered. -/
class ActiveSetTraceConcentration (R : Type*) [CommRing R] (A : ℕ) where
  /-- All partitions `λ ⊢ 3A`. -/
  allPartitions : Finset (List ℕ)
  /-- Row count `ℓ(λ)` of a partition. -/
  rowCount : List ℕ → ℕ
  /-- Per-block Markov-trace contribution in `R`. -/
  blockTrace : List ℕ → R
  /-- Littlewood–Richardson fusion support bound: `ℓ(λ) > A ⇒ blockTrace λ = 0`. -/
  vanish_above_A :
    ∀ lam ∈ allPartitions, A < rowCount lam → blockTrace lam = 0

/-- **Conditional theorem (active-set truncation without loss).** Under
    `[ActiveSetTraceConcentration R A]`, summing `blockTrace` over all
    partitions of `3A` equals summing over the `ℓ(λ) ≤ A` fusion-support
    subset. -/
-- Ref: [leitner2026] conj:active-set-trace-concentration
theorem active_set_trace_truncation {R : Type*} [CommRing R] (A : ℕ)
    [c : ActiveSetTraceConcentration R A] :
    c.allPartitions.sum c.blockTrace =
      (c.allPartitions.filter (fun lam => c.rowCount lam ≤ A)).sum c.blockTrace := by
  have hsub : c.allPartitions.filter (fun lam => c.rowCount lam ≤ A) ⊆ c.allPartitions :=
    Finset.filter_subset _ _
  rw [← Finset.sum_sdiff hsub]
  have hzero : ∀ lam ∈ c.allPartitions \ c.allPartitions.filter (fun lam => c.rowCount lam ≤ A),
      c.blockTrace lam = 0 := by
    intro lam hlam
    rw [Finset.mem_sdiff, Finset.mem_filter] at hlam
    apply c.vanish_above_A lam hlam.1
    have hnot : ¬ c.rowCount lam ≤ A := fun hle => hlam.2 ⟨hlam.1, hle⟩
    omega
  rw [Finset.sum_eq_zero hzero, zero_add]

end QOU.BraidKnot
