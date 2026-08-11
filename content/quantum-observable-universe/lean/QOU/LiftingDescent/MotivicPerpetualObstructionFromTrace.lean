import Mathlib.Tactic
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Data.Finset.Basic

namespace QOU.LiftingDescent

/-- In ℤ, the only units are ±1. If |trace| > 1 then it's not a unit.
    This is the Route A proof: bypass the abstract Mhat and work in ℤ. -/
theorem galois_trace_not_unit (n : ℤ) (h : 1 < n.natAbs) : ¬IsUnit n := by
  intro hu
  have h1 : n.natAbs = 1 := Int.isUnit_iff_natAbs_eq.mp hu
  omega

/-- Given a trace function and a bound N past which the trace is large, 
    the trace is not a unit almost everywhere. -/
theorem perpetual_obstruction_from_trace
    (trace : Nat.Primes → ℤ)
    (N : ℕ)
    (h_bound : ∀ p : Nat.Primes, (p : ℕ) ≥ N → 1 < (trace p).natAbs) :
    ∃ S : Finset ℕ, ∀ p : Nat.Primes, (p : ℕ) ∉ S → ¬IsUnit (trace p) := by
  refine ⟨Finset.range N, ?_⟩
  intro p hpS
  have hpN : N ≤ (p : ℕ) := by
    by_contra hlt
    push_neg at hlt
    exact hpS (Finset.mem_range.mpr hlt)
  exact galois_trace_not_unit (trace p) (h_bound p hpN)

end QOU.LiftingDescent
