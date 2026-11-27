import Mathlib.Data.List.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic

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
- [leitner2026] particle-interactions / algebraic-primality
- [leitner2026] particle-interactions / n-equals-1-vacuous-magic
- [leitner2026] particle-interactions / algebraic-primality-equals-empirical-at-q0
-/

namespace QOU.Interactions.AlgebraicPrimality

/-! ## §1  Confinement SDP state — abstract surrogate -/

/-- Surrogate type for the state space of an `n`-strand hadron at
    substrate `q`. Concrete model: a record carrying the strand
    count and substrate parameter as observable fields. -/
structure SDPState (_n : ℕ) (_q : ℝ) where
  /-- Strand count `n` (recorded for downstream decomposition checks). -/
  strands : ℕ
  /-- Substrate parameter `q` at which the SDP is evaluated. -/
  qVal : ℝ

/-- The canonical confinement-SDP optimum state `ψ_n(q)`.
    Concrete model: a record pinning `strands := n`, `qVal := q`
    (the canonical observable assignment). -/
def canonicalState (n : ℕ) (q : ℝ) : SDPState n q :=
  { strands := n, qVal := q }

/-- The "is in the closed span of tensor products of canonical states
    indexed by a decomposition" predicate.  **`opaque` since
    2026-08-24**; the genuine span predicate is still the upgrade
    target.

    It was `def … : Prop := False`, ignoring all four of its arguments.
    Its own docstring drew the consequence — *"every `n ≥ 1` is
    therefore algebraically prime"* — and stopped there.  That
    consequence is not a harmless simplification; it is the negation of
    what this file exists to state.  `IsAlgebraicallyPrime n q` unfolded
    to `n ≥ 1 ∧ ∀ decomp, … → ¬False`, i.e. definitionally to `n ≥ 1`.
    So `IsKnownMagic n q` was provable in one line for **every** `n ≥ 1`,
    magic or not, and `IsKnownNotMagic n q` was *unprovable* for every
    `n ≥ 1` — while `MagicEqualsEmpirical` asserts primality holds
    exactly on `{2, 8, 20, 28, 50, 82, 126}` and
    `magicEqualsEmpirical_of_perNAxioms` needs both halves.  The model
    did not under-specify the conjecture; it contradicted it.

    Sealing the body keeps the type and every structural result that
    quantifies over the predicate (`IsAlgebraicallyPrime`,
    `not_prime_of_inTensorSpan`, `two_isAlgebraicallyPrime`) while
    removing the ability to discharge a primality claim by unfolding.
    Same remedy, and the same reason, as the three `opaque` surreal
    placeholders in `QOU/AppendixSurreals/Conjectures.lean`. -/
opaque InTensorSpan (_n : ℕ) (_q : ℝ)
    (_psi : SDPState _n _q) (_decomp : List ℕ) : Prop

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
-- Ref: [leitner2026] def:algebraic-primality
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
    have h_a : 1 ≤ a := h a (by simp)
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
-- Ref: [leitner2026] prop:n-equals-1-vacuous-magic
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

/-! ## §6  Tautological consequences of the definition -/

/-- **Lemma (decomposability negates primality).** If for some
    non-trivial decomposition `decomp` of `n`, the canonical state
    `canonicalState n q` lies in the indicated tensor span, then
    `n` is *not* algebraically prime at `q`. Direct unfolding of the
    definition. -/
-- Ref: [leitner2026] def:algebraic-primality
theorem not_prime_of_inTensorSpan
    {n : ℕ} {q : ℝ}
    {decomp : List ℕ}
    (h_dec : NonTrivialDecomposition n decomp)
    (h_in : InTensorSpan n q (canonicalState n q) decomp) :
    ¬ IsAlgebraicallyPrime n q := by
  intro ⟨_, h_prime⟩
  exact h_prime decomp h_dec h_in

/-- **Lemma (decomposability of n = 0).** Zero is *not* algebraically
    prime: it fails the `n ≥ 1` clause of the definition. -/
-- Ref: [leitner2026] def:algebraic-primality
theorem zero_not_isAlgebraicallyPrime (q : ℝ) :
    ¬ IsAlgebraicallyPrime 0 q := by
  intro ⟨h, _⟩
  exact absurd h (by decide)

/-! ## §7  Per-n typeclass machinery — incremental factorisation -/

/-- Per-n assertion that `n` is *known* to be magic at `q`.
    Used to factorise the empirical-match conjecture into per-n
    propositions, each of which can be discharged independently. -/
class IsKnownMagic (n : ℕ) (q : ℝ) : Prop where
  is_prime : IsAlgebraicallyPrime n q

/-- Per-n assertion that `n` is *known* to be non-magic at `q`. -/
class IsKnownNotMagic (n : ℕ) (q : ℝ) : Prop where
  not_prime : ¬ IsAlgebraicallyPrime n q

/-- **Proved instance.** For every `q : ℝ`, `n = 1` is known to be
    magic at `q` — discharged by `one_isAlgebraicallyPrime`.
    No additional axioms required; the proof is structural
    (vacuous primality). -/
-- Ref: [leitner2026] prop:n-equals-1-vacuous-magic
instance one_isKnownMagic (q : ℝ) : IsKnownMagic 1 q where
  is_prime := one_isAlgebraicallyPrime q

/-- **Proved instance.** For every `q`, `n = 0` is known to be
    non-magic — by the `n ≥ 1` clause of the definition. -/
-- Ref: [leitner2026] def:algebraic-primality
instance zero_isKnownNotMagic (q : ℝ) : IsKnownNotMagic 0 q where
  not_prime := zero_not_isAlgebraicallyPrime q

/-! ## §8  Empirical-match conjecture at q_0 -/

/-- The empirical magic ladder `{1, 2, 8, 20, 28, 50, 82, 126}`. -/
def empiricalMagicLadder : Set ℕ :=
  {1, 2, 8, 20, 28, 50, 82, 126}

/-- **Conjecture (`conj:algebraic-primality-equals-empirical-at-q0`).**
    At substrate `q = q_0` (the framework's distinguished substrate
    value), the set of algebraically-prime integers equals the
    empirical magic ladder.

    Concrete instances supply the substrate value `q_0_value` and
    the iff. -/
-- Ref: [leitner2026] conj:algebraic-primality-equals-empirical-at-q0
class MagicEqualsEmpirical where
  q_0_value : ℝ
  q_0_pos : 1 < q_0_value
  prime_iff_in_ladder :
    ∀ (n : ℕ),
      IsAlgebraicallyPrime n q_0_value
        ↔ n ∈ empiricalMagicLadder

/-- Re-export forward direction: at `n` on the empirical ladder,
    `n` is algebraically prime at `q_0`. -/
-- Ref: [leitner2026] conj:algebraic-primality-equals-empirical-at-q0
theorem prime_at_empirical
    [E : MagicEqualsEmpirical]
    {n : ℕ} (hn : n ∈ empiricalMagicLadder) :
    IsAlgebraicallyPrime n E.q_0_value :=
  (E.prime_iff_in_ladder n).mpr hn

/-- Re-export reverse direction: if `n` is algebraically prime at
    `q_0`, then `n` lies on the empirical magic ladder. -/
-- Ref: [leitner2026] conj:algebraic-primality-equals-empirical-at-q0
theorem empirical_of_prime
    [E : MagicEqualsEmpirical]
    {n : ℕ} (hp : IsAlgebraicallyPrime n E.q_0_value) :
    n ∈ empiricalMagicLadder :=
  (E.prime_iff_in_ladder n).mp hp

/-! ## §9  Partial proof — assembling the conjecture from per-n facts -/

/-- **Theorem (assembly).** Suppose we have, at substrate `q`:
    - For every `n ∈ empiricalMagicLadder`, an `IsKnownMagic n q`
      instance.
    - For every `n ∉ empiricalMagicLadder`, an `IsKnownNotMagic n q`
      instance.

    Then the conjecture `MagicEqualsEmpirical` holds at `q`.

    This is the *structural* conjecture: it factors the iff into
    per-n axioms. The `n = 1` axiom is **discharged** by the
    proved `one_isKnownMagic` instance; the others (n in {2, 8, 20,
    28, 50, 82, 126} and n outside the ladder) remain conjectural,
    waiting for the SDP machinery.
-/
-- Ref: [leitner2026] conj:algebraic-primality-equals-empirical-at-q0
def magicEqualsEmpirical_of_perNAxioms
    {q : ℝ} (h_q : 1 < q)
    (h_in : ∀ n ∈ empiricalMagicLadder, IsKnownMagic n q)
    (h_out : ∀ n ∉ empiricalMagicLadder, IsKnownNotMagic n q) :
    MagicEqualsEmpirical where
  q_0_value := q
  q_0_pos := h_q
  prime_iff_in_ladder n := by
    constructor
    · intro hp
      by_contra h_not
      have := (h_out n h_not).not_prime
      exact this hp
    · intro hin
      exact (h_in n hin).is_prime

/-- **Corollary.** The `n = 1` constraint of the conjecture
    `MagicEqualsEmpirical` is automatically satisfied — it is not a
    free axiom. -/
-- Ref: [leitner2026] prop:n-equals-1-vacuous-magic
theorem one_in_ladder_is_known (q : ℝ) :
    IsKnownMagic 1 q :=
  one_isKnownMagic q

/-! ## §10  n = 2 reduction — first non-trivial magic shell -/

/-- **Lemma (decomposition of 2).** The only non-trivial decomposition
    of `n = 2` (length ≥ 2, all entries ≥ 1) is `[1, 1]`. Provable
    by elementary arithmetic via `sum_ge_length_of_all_pos`. -/
-- Ref: [leitner2026] def:algebraic-primality
lemma decomp_two_eq_oneOne (d : List ℕ)
    (h : NonTrivialDecomposition 2 d) :
    d = [1, 1] := by
  obtain ⟨h_len, h_pos, h_sum⟩ := h
  -- length ≥ 2 + length ≤ sum = 2 forces length = 2.
  have h_len_eq : d.length = 2 := by
    have h_bound : d.length ≤ d.sum := sum_ge_length_of_all_pos h_pos
    omega
  -- Extract [a, b] via the length-2 destructor.
  rcases List.length_eq_two.mp h_len_eq with ⟨a, b, rfl⟩
  -- a, b ≥ 1 and a + b = 2 ⇒ a = b = 1.
  have ha : 1 ≤ a := h_pos a (by simp)
  have hb : 1 ≤ b := h_pos b (by simp)
  simp only [List.sum_cons, List.sum_nil, Nat.add_zero] at h_sum
  have : a = 1 ∧ b = 1 := by omega
  rw [this.1, this.2]

/-- **Typeclass (n = 2 binding axiom).** The single non-trivial axiom
    needed to discharge `IsKnownMagic 2 q`: at substrate `q`, the
    canonical state `ψ_2(q)` is **not** in the closed tensor span of
    `ψ_1 ⊗ ψ_1` (the unique non-trivial decomposition of 2).

    This is the minimal axiom — by `decomp_two_eq_oneOne`, proving
    primality at n = 2 reduces to this single check.

    In framework language: the SDP at n = 2 produces a *non-trivial
    bound state*, distinct from two free single-strands. Empirically
    expected at any reasonable substrate `q > 1`. -/
class NonTrivialBindingAtTwo (q : ℝ) : Prop where
  /-- ψ_2(q) is not in the tensor span via decomposition [1, 1]. -/
  not_in_oneOne_span :
    ¬ InTensorSpan 2 q (canonicalState 2 q) [1, 1]

/-- **Theorem.** Under `NonTrivialBindingAtTwo q`, `n = 2` is
    algebraically prime at `q`. The proof:

    1. Any non-trivial decomposition of 2 is `[1, 1]` (proved
       arithmetic, `decomp_two_eq_oneOne`).
    2. `ψ_2(q) ∉ tensor-span([1, 1])` is the typeclass axiom.

    Combining: the universal-quantifier in `IsAlgebraicallyPrime 2 q`
    reduces to a single check, which the typeclass provides. -/
-- Ref: [leitner2026] def:algebraic-primality
-- Ref: [leitner2026] conj:algebraic-primality-equals-empirical-at-q0
theorem two_isAlgebraicallyPrime
    (q : ℝ) [N : NonTrivialBindingAtTwo q] :
    IsAlgebraicallyPrime 2 q := by
  refine ⟨by decide, ?_⟩
  intro decomp h_decomp h_in
  have h_eq : decomp = [1, 1] := decomp_two_eq_oneOne decomp h_decomp
  rw [h_eq] at h_in
  exact N.not_in_oneOne_span h_in

/-- **Conditional instance.** `NonTrivialBindingAtTwo q` discharges the
    n = 2 case of the per-n axiom collection for `MagicEqualsEmpirical`.

    This one stays an `instance`, deliberately.  It is the §3b-cond
    pattern working as intended: the `[NonTrivialBindingAtTwo q]` binder
    *is* the dependency edge, and `is_prime` is a real derivation —
    `two_isAlgebraicallyPrime` combines `decomp_two_eq_oneOne` (proved
    arithmetic) with the class field.  It looked vacuous only because
    §11 used to supply `NonTrivialBindingAtTwo q` globally, so
    resolution chained through and answered `IsKnownMagic 2 q`
    unconditionally.  With §11 gone the chain has no free end. -/
-- Ref: [leitner2026] conj:algebraic-primality-equals-empirical-at-q0
instance two_isKnownMagic_of_nonTrivialBinding
    (q : ℝ) [NonTrivialBindingAtTwo q] :
    IsKnownMagic 2 q where
  is_prime := two_isAlgebraicallyPrime q

/-! ## §11  The n = 2 binding axiom has no model — and that is the point

Until 2026-08-24 this section read:

```lean
/-- **Trivial-model instance.**  On the concrete `InTensorSpan ≡ False`
    model, `not_in_oneOne_span` reduces to `¬ False`, which is `True`.
    Provides a Lean-verified discharge of the n = 2 axiom on every
    substrate `q`. -/
instance trivialBindingAtTwo (q : ℝ) : NonTrivialBindingAtTwo q where
  not_in_oneOne_span := not_false
```

The description was accurate and the instance was worthless: `¬ False`
is not evidence that `ψ_2(q)` fails to decompose, it is evidence that
`InTensorSpan` had been defined to hold of nothing.  Being an
`instance`, it discharged `[NonTrivialBindingAtTwo q]` at every real
`q`, and `two_isKnownMagic_of_nonTrivialBinding` chained off it, so
`IsKnownMagic 2 q` — the *first non-trivial* magic shell, the one the
whole per-n factorisation is aimed at — resolved for free.

With `InTensorSpan` now `opaque` the witness no longer typechecks, and
**no instance is provided.**  That is the honest open state (AGENTS.md
§3b-tax: "an unproved primary is honestly represented by a
content-bearing class with no instance; do not fabricate a trivial
instance to 'close' it").  Demoting the instance to a `def` would not
have been enough on its own: with `InTensorSpan ≡ False` still
unfolding, anyone could rebuild the witness inline without naming
anything, so the root had to go first and the instance then went with
it.

Nothing else in this file depended on it — `one_isKnownMagic` and
`zero_isKnownNotMagic` are real proofs (vacuous quantification at
`n = 1`; the `n ≥ 1` clause at `n = 0`) that never consult
`InTensorSpan`'s body, and this module has no importers.

What is now genuinely open, and was previously masked: a model of
`InTensorSpan` in which `IsKnownNotMagic n q` is provable for
`n ∉ empiricalMagicLadder`.  `magicEqualsEmpirical_of_perNAxioms` needs
that half too, and the `≡ False` model made it unprovable for every
`n ≥ 1`. -/

end QOU.Interactions.AlgebraicPrimality
