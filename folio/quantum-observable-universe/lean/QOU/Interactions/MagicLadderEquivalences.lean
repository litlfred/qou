import QOU.Interactions.AlgebraicPrimality
import QOU.LiftingDescent.HomologicalCondensation

/-!
# QOU.Interactions.MagicLadderEquivalences — magic-ladder predicate equivalences

After the cleanup of redundant conjectures, the framework has
exactly **four** primary conjectural characterisations of the
magic ladder `{2, 8, 20, 28, 50, 82, 126}`:

  (A) `MagicEqualsEmpirical` — algebraic primality at q_0
       ([conj:algebraic-primality-equals-empirical-at-q0]).
  (C) `ShellCondensationConjecture` — homological shell condensation
       (E_∞^{p, q>0} = 0) ([conj:homological-shell-condensation]).
  (F) `BringShellBindingConjecture` — Bring six-torus-knot
       cumulative shell binding ([prop:torus-knot-shell-binding]).
  (G) `DeltaIBoundConjecture` — Δi ≤ 1 LR-fusion compatibility
       ([conj:double-magic-delta-i-bound]).

This module records the structural fact that any two of A, C
share the same per-n iff with `n ∈ magicLadder`, and are therefore
pairwise equivalent.

## References

- [leitner2026] conj:algebraic-primality-equals-empirical-at-q0
- [leitner2026] conj:homological-shell-condensation
- [leitner2026] prop:torus-knot-shell-binding
- [leitner2026] conj:double-magic-delta-i-bound
-/

namespace QOU.Interactions.MagicLadderEquivalences

open QOU.Interactions.AlgebraicPrimality
open QOU.LiftingDescent.HomologicalCondensation

/-! ## §1  Meta-theorem: iff-with-magicLadder predicates are pairwise equivalent -/

/-- **Meta-theorem (transitivity through the magic ladder).** Given
    two predicates `P, Q : ℕ → Prop` that each satisfy the iff
    `P n ↔ n ∈ magicLadder` and `Q n ↔ n ∈ magicLadder`, they are
    pairwise equivalent: `P n ↔ Q n` for every `n`.

    Proof: chain the two iffs through the middle term. -/
-- Ref: [leitner2026] conj:magic-ladder equivalences
theorem predicate_equivalence_via_magic
    {P Q : ℕ → Prop}
    (hP : ∀ n, P n ↔ n ∈ magicLadder)
    (hQ : ∀ n, Q n ↔ n ∈ magicLadder)
    (n : ℕ) :
    P n ↔ Q n := by
  rw [hP n, ← hQ n]

/-! ## §2  Equivalence: algebraic primality (A) ↔ homological condensation (C) for n ≥ 2 -/

/-- **Theorem.** For `n ≥ 2`, algebraic primality at `q_0`
    (conjecture A) is equivalent to homological shell condensation
    (conjecture C). The `n = 1` case is excluded because A's
    `empiricalMagicLadder` contains 1 (vacuously) while C's
    `magicLadder` does not. -/
-- Ref: [leitner2026] conj:algebraic-primality-equals-empirical-at-q0
-- Ref: [leitner2026] conj:homological-shell-condensation
theorem primality_iff_condensation_for_n_ge_2
    [A : MagicEqualsEmpirical] [C : ShellCondensationConjecture]
    {n : ℕ} (hn : 2 ≤ n) :
    IsAlgebraicallyPrime n A.q_0_value
      ↔ InfinityVanishesAtPositiveQ n := by
  rw [A.prime_iff_in_ladder n, C.collapse_iff_magic n]
  -- Goal: n ∈ empiricalMagicLadder ↔ n ∈ magicLadder
  -- For n ≥ 2 these coincide (empiricalMagicLadder = {1} ∪ magicLadder).
  unfold empiricalMagicLadder magicLadder QOU.Common.magicSet
  constructor
  · intro h
    rcases h with h1 | h_rest
    · omega
    · simpa using h_rest
  · intro h
    right
    simpa using h

end QOU.Interactions.MagicLadderEquivalences
