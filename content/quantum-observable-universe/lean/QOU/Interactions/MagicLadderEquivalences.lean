/-!
# QOU.Interactions.MagicLadderEquivalences — structural equivalence chain

The framework states five conjectural characterisations of the
magic ladder `{2, 8, 20, 28, 50, 82, 126}`:

  (A) `MagicEqualsEmpirical` — algebraic primality at q_0
       ([conj:algebraic-primality-equals-empirical-at-q0]).
  (B) `MagicShellRankConjecture` — SDP rank-1 collapse at q_0
       ([conj:sdp-rank-collapse-magic-shell]).
  (C) `ShellCondensationConjecture` — homological shell condensation
       (E_∞^{p, q>0} = 0) ([conj:homological-shell-condensation]).
  (D) `MagicRequiresHigherCohomology` — SDP optimum has E^{p, q≥1}
       contribution ([conj:magic-requires-higher-cohomology]).
  (E) `MagicEmergesIteratively` — brane-tower threshold crosses at
       magic n ([conj:magic-from-iterative-brane-tower]).

This module records the structural fact that all five typeclass
classes refer to the SAME `magicLadder` set. Any two characterisations
that *additionally* agree on a per-n predicate (modulo conjugate
ambiguities) are forced to be equivalent.

The equivalence chain is largely tautological at the abstract level:
each conjecture asserts an iff with `n ∈ magicLadder`, so two of
them are equivalent iff their respective predicates `P_i(n) ↔ P_j(n)`
modulo the magic-ladder reference.

This module provides:

1. A meta-theorem: any two iff-with-magicLadder predicates are
   pairwise equivalent **as predicates** (i.e., `P_i(n) ↔ P_j(n)`
   for all n).
2. Concrete corollaries deriving equivalence between specific
   conjectures' predicates when both typeclass instances are in
   scope.

LaTeX label: cross-cutting; cross-references all five conjectures.

## References

- [manuscript] conj:algebraic-primality-equals-empirical-at-q0
- [manuscript] conj:sdp-rank-collapse-magic-shell
- [manuscript] conj:homological-shell-condensation
- [manuscript] conj:magic-requires-higher-cohomology
- [manuscript] conj:magic-from-iterative-brane-tower
-/

import QOU.Interactions.AlgebraicPrimality
import QOU.Interactions.SDPRankCollapse
import QOU.LiftingDescent.HomologicalCondensation
import QOU.LiftingDescent.HigherCohomology
import QOU.LiftingDescent.IterativeBraneTower

namespace QOU.Interactions.MagicLadderEquivalences

open QOU.Interactions.AlgebraicPrimality
open QOU.Interactions.SDPRankCollapse
open QOU.LiftingDescent.HomologicalCondensation
open QOU.LiftingDescent.HigherCohomology
open QOU.LiftingDescent.IterativeBraneTower

/-! ## §1  Meta-theorem: iff-with-magicLadder predicates are pairwise equivalent -/

/-- **Meta-theorem (transitivity through the magic ladder).** Given
    two predicates `P, Q : ℕ → Prop` that each satisfy the iff
    `P n ↔ n ∈ magicLadder` and `Q n ↔ n ∈ magicLadder`, they are
    pairwise equivalent: `P n ↔ Q n` for every `n`.

    Proof: chain the two iffs through the middle term. -/
-- Ref: [manuscript] conj:magic-ladder equivalences
theorem predicate_equivalence_via_magic
    {P Q : ℕ → Prop}
    (hP : ∀ n, P n ↔ n ∈ magicLadder)
    (hQ : ∀ n, Q n ↔ n ∈ magicLadder)
    (n : ℕ) :
    P n ↔ Q n := by
  rw [hP n, ← hQ n]

/-! ## §2  Equivalence: SDP rank collapse ↔ homological condensation -/

/-- **Theorem.** Given the SDP rank-collapse conjecture (B) and
    the homological shell-condensation conjecture (C) at the same
    substrate `q`, the two predicates `IsRankOneAtMagicShell n q`
    and `InfinityVanishesAtPositiveQ n` are equivalent at every
    `n` (where genericity holds for q). -/
-- Ref: [manuscript] conj:sdp-rank-collapse-magic-shell
-- Ref: [manuscript] conj:homological-shell-condensation
theorem rank_collapse_iff_condensation
    [B : MagicShellRankConjecture] [C : ShellCondensationConjecture]
    {q : ℝ} (hq : B.IsGeneric q) (n : ℕ) :
    IsRankOneAtMagicShell n q ↔ InfinityVanishesAtPositiveQ n :=
  predicate_equivalence_via_magic
    (fun n => B.rank_one_iff_magic q hq n)
    (fun n => C.collapse_iff_magic n)
    n

/-! ## §3  Equivalence: homological condensation ↔ higher cohomology -/

/-- **Theorem.** Given homological shell-condensation (C) and the
    higher-cohomology conjecture (D), the predicates
    `InfinityVanishesAtPositiveQ n` and
    `OptimumHasHigherCohomologyContribution n q_0` are equivalent
    via their joint magic-ladder characterisation. -/
-- Ref: [manuscript] conj:homological-shell-condensation
-- Ref: [manuscript] conj:magic-requires-higher-cohomology
theorem condensation_iff_higher_cohom
    [C : ShellCondensationConjecture]
    [D : MagicRequiresHigherCohomology]
    (n : ℕ) :
    InfinityVanishesAtPositiveQ n
      ↔ OptimumHasHigherCohomologyContribution n D.q_0_value :=
  predicate_equivalence_via_magic
    (fun n => C.collapse_iff_magic n)
    (fun n => D.magic_iff_higher_cohom n)
    n

/-! ## §4  Equivalence: SDP rank collapse ↔ iterative emergence -/

/-- **Theorem.** Given the SDP rank-collapse conjecture (B) and
    the iterative-brane-tower conjecture (E) at compatible
    substrate values, their predicates are equivalent. -/
-- Ref: [manuscript] conj:sdp-rank-collapse-magic-shell
-- Ref: [manuscript] conj:magic-from-iterative-brane-tower
theorem rank_collapse_iff_iterative
    [B : MagicShellRankConjecture]
    [E : MagicEmergesIteratively]
    {q : ℝ} (hq : B.IsGeneric q) (n : ℕ) :
    IsRankOneAtMagicShell n q
      ↔ Threshold E.q_0_value (E.stateAt n) :=
  predicate_equivalence_via_magic
    (fun n => B.rank_one_iff_magic q hq n)
    (fun n => E.threshold_iff_magic n)
    n

/-! ## §5  Equivalence: algebraic primality ↔ rank collapse (modulo n=1) -/

/-- **Theorem (modulo n = 1).** For `n ≥ 2`, algebraic primality at
    `q_0` (conjecture A) is equivalent to SDP rank-1 collapse
    (conjecture B). The `n = 1` case is excluded because A's
    `empiricalMagicLadder` contains 1 (as a vacuous case) while
    B's `magicLadder` does not.

    Note: this is the cleanest place to see the n=1 indexing
    discrepancy between the two conjecture statements. -/
-- Ref: [manuscript] conj:algebraic-primality-equals-empirical-at-q0
-- Ref: [manuscript] conj:sdp-rank-collapse-magic-shell
theorem primality_iff_rank_collapse_for_n_ge_2
    [A : MagicEqualsEmpirical] [B : MagicShellRankConjecture]
    {q : ℝ} (hq_B : B.IsGeneric q)
    {n : ℕ} (hn : 2 ≤ n) :
    IsAlgebraicallyPrime n A.q_0_value
      ↔ IsRankOneAtMagicShell n q := by
  -- Both are equivalent to "n is empirically magic" via:
  --   A: prime ↔ n ∈ empiricalMagicLadder = {1, 2, 8, 20, 28, 50, 82, 126}
  --   B: rank-1 ↔ n ∈ magicLadder = {2, 8, 20, 28, 50, 82, 126}
  -- For n ≥ 2 these coincide.
  rw [A.prime_iff_in_ladder n, B.rank_one_iff_magic q hq_B n]
  -- Goal: n ∈ empiricalMagicLadder ↔ n ∈ magicLadder
  -- empiricalMagicLadder = {1} ∪ magicLadder, so for n ≥ 2 they
  -- agree.
  unfold empiricalMagicLadder magicLadder
  constructor
  · intro h
    rcases h with h1 | h2 | h8 | h20 | h28 | h50 | h82 | h126
    · -- n = 1 contradicts hn : 2 ≤ n
      omega
    all_goals simp_all
  · intro h
    -- n ∈ {2, 8, 20, 28, 50, 82, 126} ⇒ n ∈ {1, 2, 8, 20, 28, 50, 82, 126}
    rcases h with h2 | h8 | h20 | h28 | h50 | h82 | h126
    all_goals simp_all

/-! ## §6  Coverage statement -/

/-- **Coverage theorem.** Any two of the five conjectural
    characterisations of the magic ladder produce equivalent
    per-n predicates (modulo the n=1 indexing discrepancy between
    `empiricalMagicLadder` and `magicLadder`).

    This is the abstract content of "the framework's five magic-
    ladder conjectures are mutually equivalent." -/
-- Ref: [manuscript] conj:magic-ladder equivalence chain
theorem all_five_conjectures_share_magic_ladder
    [A : MagicEqualsEmpirical] [B : MagicShellRankConjecture]
    [C : ShellCondensationConjecture]
    [D : MagicRequiresHigherCohomology]
    [E : MagicEmergesIteratively]
    {q : ℝ} (hq : B.IsGeneric q)
    {n : ℕ} (hn : 2 ≤ n) :
    -- Five-way conjunction: all predicates equivalent.
    (IsAlgebraicallyPrime n A.q_0_value)
      ↔ (IsRankOneAtMagicShell n q
        ∧ InfinityVanishesAtPositiveQ n
        ∧ OptimumHasHigherCohomologyContribution n D.q_0_value
        ∧ Threshold E.q_0_value (E.stateAt n)) := by
  -- Each is equivalent to "n is empirically magic" — for n ≥ 2,
  -- empiricalMagicLadder ∋ n ↔ magicLadder ∋ n.
  rw [A.prime_iff_in_ladder n]
  constructor
  · intro h
    -- h : n ∈ empiricalMagicLadder
    -- For n ≥ 2, this gives n ∈ magicLadder, which gives all four.
    have h' : n ∈ magicLadder := by
      unfold empiricalMagicLadder at h
      unfold magicLadder
      rcases h with h1 | h_rest
      · omega
      · exact h_rest
    refine ⟨?_, ?_, ?_, ?_⟩
    · exact (B.rank_one_iff_magic q hq n).mpr h'
    · exact (C.collapse_iff_magic n).mpr h'
    · exact (D.magic_iff_higher_cohom n).mp h'
    · exact (E.threshold_iff_magic n).mpr h'
  · intro ⟨h_rank, _, _, _⟩
    -- Reverse: rank-1 ⇒ magic ⇒ empirically magic.
    have h' : n ∈ magicLadder :=
      (B.rank_one_iff_magic q hq n).mp h_rank
    -- Now show n ∈ empiricalMagicLadder.
    unfold empiricalMagicLadder
    right; exact h'

end QOU.Interactions.MagicLadderEquivalences
