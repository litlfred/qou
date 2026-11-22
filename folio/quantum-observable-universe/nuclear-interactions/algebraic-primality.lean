import Mathlib.Data.List.Basic
import Mathlib.Algebra.Order.BigOperators.Group.List

/-!
# `QOU.Interactions.AlgebraicPrimality.IsAlgebraicallyPrime`

A strand count `n` is **algebraically prime at `q`** when the canonical SDP
state `ψ_n(q)` is not contained in the closed span of any product of canonical
states indexed by a nontrivial decomposition `n = n₁ + … + n_k` (`k ≥ 2`,
each `nᵢ ≥ 1`). By convention the vacuum `n = 0` is not prime.

The analytic content — the SDP states and closed-span membership — is supplied
by `closed_form_tau_M.py`; here it is abstracted into a span-membership
predicate `inSpan n parts`, so the *combinatorial* structure of the predicate
(quantifying over nontrivial decompositions) is formalised exactly. The
vacuous primality of `n = 1` is proved sorry-free.

-- Ref: [leitner2026] particle-interactions/algebraic-primality
-/

namespace QOU.Interactions.AlgebraicPrimality

/-- A **nontrivial decomposition** of `n`: a list of at least two positive
parts summing to `n`. -/
def NontrivialDecomp (n : ℕ) (parts : List ℕ) : Prop :=
  2 ≤ parts.length ∧ (∀ p ∈ parts, 1 ≤ p) ∧ parts.sum = n

/-- `n` is **algebraically prime** with respect to a span-membership predicate
`inSpan n parts` (encoding `ψ_n(q) ∈ closed-span of the product over `parts`)
iff `n ≠ 0` and no nontrivial decomposition places `ψ_n` in the corresponding
span. -/
def IsAlgebraicallyPrime (inSpan : ℕ → List ℕ → Prop) (n : ℕ) : Prop :=
  n ≠ 0 ∧ ∀ parts, NontrivialDecomp n parts → ¬ inSpan n parts

/-- **Vacuous primality at `n = 1`.** No nontrivial decomposition can sum to
`1` (two parts each `≥ 1` already sum to `≥ 2`), so `1` is algebraically prime
for any span predicate. -/
theorem one_isAlgebraicallyPrime (inSpan : ℕ → List ℕ → Prop) :
    IsAlgebraicallyPrime inSpan 1 := by
  refine ⟨one_ne_zero, ?_⟩
  intro parts hd _
  obtain ⟨hlen, hpos, hsum⟩ := hd
  -- a list whose entries are all ≥1 has sum ≥ its length ≥ 2, contradicting sum = 1
  have h2 : parts.length ≤ parts.sum := by
    apply List.length_le_sum_of_one_le
    intro p hp
    exact hpos p hp
  omega

end QOU.Interactions.AlgebraicPrimality
