import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.Trace

/-!
# QOU.BraidKnot.FrobeniusSelfDualityForcesLPDualExtraction

**Canonical declaration** for content block at
[`quantum-observable-universe/mass-theory/frobenius-self-duality-forces-lp-dual-extraction.ts`](quantum-observable-universe/mass-theory/frobenius-self-duality-forces-lp-dual-extraction.ts).

Formalises the manuscript proposition for any algebra on which the trace is
non-degenerate (taken as a field of the carrier). Under convention D the Markov
trace on `H_n(R,q)` is DEGENERATE for `n ≥ 3` (`y_(1³) = 0`; radical = the
three-row blocks), so the carrier applies to the quotient `TL_n(q)`, not to
`H_n` itself (corrected 2026-11-15). On such an algebra `τ` is a
non-degenerate symmetric pairing, hence self-dual; the Observation Frame `Obs_τ(a) = τ(a·−)` extracts
the shadow-price representative of every observable. Generic ring (§7c-clean).
-/

namespace QOU.BraidKnot

/-- The Frobenius / Markov-trace data on an algebra `A`.

    A `definition` carrier: the trace `τ`, its cyclic-symmetry, and the
    non-degeneracy witness (for every `a ≠ 0` some `b` pairs non-trivially) —
    exactly the data making `(A, τ)` Frobenius, hence self-dual. -/
structure FrobeniusSelfDualityForcesLPDualExtraction (A : Type*) (R : Type*)
    [Ring A] [CommRing R] where
  /-- The Markov trace `τ : A → R`. -/
  τ : A → R
  /-- Cyclic (Markov) symmetry `τ(ab) = τ(ba)`. -/
  tau_cyclic : ∀ a b : A, τ (a * b) = τ (b * a)
  /-- `τ` is additive (bilinearity of the induced pairing). -/
  tau_add : ∀ a b : A, τ (a + b) = τ a + τ b
  /-- Non-degeneracy: a nonzero element pairs non-trivially with something. -/
  nondegenerate : ∀ a : A, a ≠ 0 → ∃ b : A, τ (a * b) ≠ 0

namespace FrobeniusSelfDualityForcesLPDualExtraction

variable {A R : Type*} [Ring A] [CommRing R]
    (F : FrobeniusSelfDualityForcesLPDualExtraction A R)

/-- The Frobenius pairing `⟨a,b⟩ = τ(ab)`. -/
def pairing (a b : A) : R := F.τ (a * b)

/-- The Observation Frame `Obs_τ(a) = τ(a · −)` (the shadow-price
    functional of the observable `a`). -/
def Obs (a : A) : A → R := fun b => F.τ (a * b)

/-- The Frobenius pairing is symmetric — the source of self-duality
    (`H_n ≅ H_n^*`). -/
theorem pairing_symm (a b : A) : F.pairing a b = F.pairing b a := by
  unfold pairing; exact F.tau_cyclic a b

/-- `Obs` is exactly pairing against the observable, so the primal element
    `a` and its dual functional `Obs a` live in the same space (LP primal ↔
    dual identification). -/
theorem Obs_eq_pairing (a b : A) : F.Obs a b = F.pairing a b := rfl

/-- The Observation Frame is additive in its argument (a linear functional). -/
theorem Obs_add (a b c : A) : F.Obs a (b + c) = F.Obs a b + F.Obs a c := by
  unfold Obs; rw [mul_add, F.tau_add]

/-- **De-axiomatisation (concrete model, bean `cy3v`).** The `n×n` matrix
    algebra over a field, with the matrix trace, is a genuine instance of the
    Frobenius carrier — the three axioms are *theorems*, not assumptions:
    cyclicity is `Matrix.trace_mul_comm` (a non-trivial fact in a
    non-commutative algebra), additivity is `Matrix.trace_add`, and
    non-degeneracy is witnessed by pairing a nonzero entry `A i j ≠ 0` against
    the elementary matrix `E_{j,i}`, which gives `tr(A · E_{j,i}) = A i j`.
    So the abstract carrier — hence the Frobenius self-duality — is realisable,
    not vacuous. -/
noncomputable def matrixModel (n : ℕ) (R : Type*) [Field R] :
    FrobeniusSelfDualityForcesLPDualExtraction (Matrix (Fin n) (Fin n) R) R where
  τ := Matrix.trace
  tau_cyclic a b := Matrix.trace_mul_comm a b
  tau_add a b := Matrix.trace_add a b
  nondegenerate A hA := by
    obtain ⟨i, j, hij⟩ : ∃ i j, A i j ≠ 0 := by
      by_contra h
      push_neg at h
      exact hA (by ext i j; simp [h i j])
    refine ⟨Matrix.single j i 1, ?_⟩
    have key : (A * Matrix.single j i 1).trace = A i j := by
      rw [Matrix.trace_mul_comm]
      simp only [Matrix.trace, Matrix.diag_apply, Matrix.mul_apply, Matrix.single,
        Matrix.of_apply, ite_and, ite_mul, one_mul, zero_mul]
      rw [Finset.sum_eq_single_of_mem j (Finset.mem_univ j)]
      · simp [Finset.sum_ite_eq]
      · intro x _ hx
        simp [Ne.symm hx]
    rw [key]; exact hij

end FrobeniusSelfDualityForcesLPDualExtraction

-- Ref: [leitner2026] quantum-observable-universe/mass-theory/frobenius-self-duality-forces-lp-dual-extraction.ts

end QOU.BraidKnot
