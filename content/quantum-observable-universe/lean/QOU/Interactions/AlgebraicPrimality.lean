/-!
# QOU.Interactions.AlgebraicPrimality — magic via tensor-product irreducibility

A pure-math definition of "magic" without empirical input. For each
strand count `n` and substrate `q`, the confinement SDP gives a
canonical state `ψ_n(q)`. We say `n` is **magic at q** iff `ψ_n(q)`
is **algebraically prime**: not in the closed span of any non-trivial
tensor product `ψ_{n_1}(q) ⊗ ... ⊗ ψ_{n_k}(q)` with `k ≥ 2` and
`n_i ≥ 1`.

This file:
* defines the magic predicate as an axiom-class (the SDP machinery
  is not formalised here; only the structural primality logic);
* proves the base case `n = 1` is vacuously prime;
* exposes the conjectural empirical-match claim as a typeclass.

LaTeX labels:
  - `def:algebraic-primality`
  - `prop:n-equals-1-vacuous-magic`
  - `conj:algebraic-primality-equals-empirical-at-q0`

## References

- [mathas1999] https://doi.org/10.1090/ulect/015 — Iwahori–Hecke algebras
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2 — Quantum groups
- [manuscript] particle-interactions / algebraic-primality
- [manuscript] particle-interactions / n-equals-1-vacuous-magic
- [manuscript] particle-interactions / algebraic-primality-equals-empirical-at-q0
-/

import Mathlib.Data.List.Basic
import Mathlib.Algebra.BigOperators.Basic
import Mathlib.Tactic

namespace QOU.Interactions.AlgebraicPrimality

/-! ## §1  Confinement SDP state — abstract surrogate -/

/-- Surrogate type for the state space of an `n`-strand hadron at
    substrate `q`. Concrete instances will identify this with the
    space of `T*(n, q)`-projector images in the Hecke / Wedderburn
    decomposition. -/
opaque SDPState (n : ℕ) (q : ℝ) : Type

/-- The canonical confinement-SDP optimum state `ψ_n(q)`. -/
opaque canonicalState (n : ℕ) (q : ℝ) : SDPState n q

/-- The "is in the closed span of tensor products of canonical
    states indexed by a decomposition" predicate. Axiomatised here:
    concrete instances supply the linear-algebra content. The
    decomposition is encoded as a `List ℕ` summing to `n`. -/
opaque InTensorSpan (n : ℕ) (q : ℝ)
    (psi : SDPState n q) (decomp : List ℕ) : Prop

/-! ## §2  Decomposition predicates -/

/-- A *non-trivial* decomposition of `n`: a list of length ≥ 2,
    all entries ≥ 1, summing to `n`. -/
def NonTrivialDecomposition (n : ℕ) (decomp : List ℕ) : Prop :=
  decomp.length ≥ 2 ∧ (∀ k ∈ decomp, k ≥ 1) ∧ decomp.sum = n

/-! ## §3  The algebraic-primality definition -/

/-- **Definition (algebraic primality).** A natural number `n ≥ 1`
    is **algebraically prime** at substrate `q` if and only if
    `canonicalState n q` is *not* in the closed span of any
    non-trivial tensor-product decomposition.

    Conventions:
    - `n = 0` is *not* prime (vacuum).
    - `n = 1` is prime *vacuously* — no non-trivial decomposition
      exists.
    - For `n ≥ 2`, primality is non-trivial. -/
-- Ref: [manuscript] def:algebraic-primality
def IsAlgebraicallyPrime (n : ℕ) (q : ℝ) : Prop :=
  n ≥ 1 ∧
  ∀ (decomp : List ℕ),
    NonTrivialDecomposition n decomp →
    ¬ InTensorSpan n q (canonicalState n q) decomp

/-! ## §4  Auxiliary lemma -/

/-- **Lemma (sum dominates length under positivity).** For any list
    of natural numbers with every entry `≥ 1`, the sum is at least
    the length. -/
lemma sum_ge_length_of_all_pos
    {l : List ℕ} (h : ∀ k ∈ l, 1 ≤ k) :
    l.length ≤ l.sum := by
  induction l with
  | nil => simp
  | cons a as ih =>
    have h_a : 1 ≤ a := h a (by exact List.mem_cons_self a as)
    have h_tail : ∀ k ∈ as, 1 ≤ k :=
      fun k hk => h k (List.mem_cons_of_mem _ hk)
    have h_as := ih h_tail
    simp only [List.length_cons, List.sum_cons]
    omega

/-! ## §5  Vacuous primality at n = 1 -/

/-- **Theorem (`prop:n-equals-1-vacuous-magic`).** For every `q : ℝ`,
    the integer `n = 1` is algebraically prime — vacuously, because
    no decomposition into `k ≥ 2` parts each `≥ 1` can sum to `1`.

    The proof needs only elementary arithmetic: a list of length ≥ 2
    with all entries ≥ 1 has sum ≥ 2 > 1, contradicting `sum = 1`.
    No SDP / Hecke / tensor-product analysis is invoked. -/
-- Ref: [manuscript] prop:n-equals-1-vacuous-magic
theorem one_isAlgebraicallyPrime (q : ℝ) :
    IsAlgebraicallyPrime 1 q := by
  refine ⟨le_refl 1, ?_⟩
  intro decomp h
  obtain ⟨h_len, h_pos, h_sum⟩ := h
  exfalso
  -- Each entry ≥ 1, so sum ≥ length.
  have h_bound : decomp.length ≤ decomp.sum :=
    sum_ge_length_of_all_pos h_pos
  -- length ≥ 2, so sum ≥ 2.
  -- But sum = 1. Contradiction.
  omega

/-! ## §6  Empirical-match conjecture at q_0 -/

/-- The empirical magic ladder `{1, 2, 8, 20, 28, 50, 82, 126}`. -/
def empiricalMagicLadder : Set ℕ :=
  {1, 2, 8, 20, 28, 50, 82, 126}

/-- **Conjecture (`conj:algebraic-primality-equals-empirical-at-q0`).**
    At substrate `q = q_0` (the framework's distinguished substrate
    value), the set of algebraically-prime integers equals the
    empirical magic ladder.

    Concrete instances supply the substrate value `q_0_value` and
    the iff. -/
-- Ref: [manuscript] conj:algebraic-primality-equals-empirical-at-q0
class MagicEqualsEmpirical where
  q_0_value : ℝ
  q_0_pos : 1 < q_0_value
  prime_iff_in_ladder :
    ∀ (n : ℕ),
      IsAlgebraicallyPrime n q_0_value
        ↔ n ∈ empiricalMagicLadder

/-- Re-export forward direction: at `n` on the empirical ladder,
    `n` is algebraically prime at `q_0`. -/
-- Ref: [manuscript] conj:algebraic-primality-equals-empirical-at-q0
theorem prime_at_empirical
    [E : MagicEqualsEmpirical]
    {n : ℕ} (hn : n ∈ empiricalMagicLadder) :
    IsAlgebraicallyPrime n E.q_0_value :=
  (E.prime_iff_in_ladder n).mpr hn

/-- Re-export reverse direction: if `n` is algebraically prime at
    `q_0`, then `n` lies on the empirical magic ladder. -/
-- Ref: [manuscript] conj:algebraic-primality-equals-empirical-at-q0
theorem empirical_of_prime
    [E : MagicEqualsEmpirical]
    {n : ℕ} (hp : IsAlgebraicallyPrime n E.q_0_value) :
    n ∈ empiricalMagicLadder :=
  (E.prime_iff_in_ladder n).mp hp

end QOU.Interactions.AlgebraicPrimality
