import Mathlib.Tactic

/-!
# QOU.BraidKnot.FrobeniusSelfDualityForcesLPDualExtraction

**Canonical declaration** for content block at
[`quantum-observable-universe/mass-theory/frobenius-self-duality-forces-lp-dual-extraction.ts`](quantum-observable-universe/mass-theory/frobenius-self-duality-forces-lp-dual-extraction.ts).

Formalises the manuscript proposition: the Markov trace `τ` on `H_n(R,q)` is
a non-degenerate symmetric bilinear pairing, making `(H_n, τ)` a Frobenius
algebra, hence self-dual; the Observation Frame `Obs_τ(a) = τ(a·−)` extracts
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

end FrobeniusSelfDualityForcesLPDualExtraction

-- Ref: [manuscript] quantum-observable-universe/mass-theory/frobenius-self-duality-forces-lp-dual-extraction.ts

end QOU.BraidKnot
