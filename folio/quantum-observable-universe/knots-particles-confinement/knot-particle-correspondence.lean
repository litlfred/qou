import Mathlib.Data.Fintype.Card
import Mathlib.Data.Finset.Card
import Mathlib.SetTheory.Cardinal.Finite
import Mathlib.Tactic

/-!
# QOU.Braiding — knot–particle correspondence (corrected 2026-11-15)

The old file asserted, as an axiom over opaque types, that the Markov trace
gives a **bijection** between the irreducible summands of `V^{⊗n}` and the
link types of `n`-strand braid closures. That is false: for `V` the
fundamental `U_q(sl₂)` module there are `⌊n/2⌋ + 1` summands, while for
`n ≥ 2` the closures include infinitely many link types (the torus links
`T(2, k)`). The axioms are removed.

What holds, and is stated in the `.md`: the Markov trace is a weighted sum of
the irreducible characters, `tr_M = Σ_λ y_λ χ_λ`, so every summand contributes
to the invariant of every closure.
-- Ref: [jones1987] §3–§4

Proved here: the summands are counted by two-row partitions
(`card_twoRowPartition`), and no map from them onto an infinite type is
surjective (`no_surjection_onto_infinite`).
-/

namespace QOU.Braiding

/-- Two-row partitions of `n`: pairs `(a, b)` with `a ≥ b` and `a + b = n`,
    indexed by the second row `b ≤ n / 2`. These label the irreducible summands
    of `V^{⊗n}` for `V` the fundamental `U_q(sl₂)` module. -/
def TwoRowPartition (n : ℕ) : Type := Fin (n / 2 + 1)

instance (n : ℕ) : Fintype (TwoRowPartition n) := inferInstanceAs (Fintype (Fin _))
instance (n : ℕ) : Finite (TwoRowPartition n) := inferInstanceAs (Finite (Fin _))

/-- The row lengths of the partition with second row `b`. -/
def TwoRowPartition.rows {n : ℕ} (b : TwoRowPartition n) : ℕ × ℕ :=
  (n - (b : Fin _).val, (b : Fin _).val)

theorem TwoRowPartition.rows_valid {n : ℕ} (b : TwoRowPartition n) :
    b.rows.1 + b.rows.2 = n ∧ b.rows.2 ≤ b.rows.1 := by
  have hb : (b : Fin (n / 2 + 1)).val ≤ n / 2 := Nat.lt_succ_iff.mp b.isLt
  unfold TwoRowPartition.rows
  constructor <;> omega

theorem card_twoRowPartition (n : ℕ) : Fintype.card (TwoRowPartition n) = n / 2 + 1 :=
  Fintype.card_fin _

/-- **No bijection.** A finite set of summands cannot map onto an infinite set
    of link types. Closures of `n`-strand braids, `n ≥ 2`, include the torus
    links `T(2, k)` for every `k`, which are pairwise distinct. -/
theorem no_surjection_onto_infinite (n : ℕ) (K : Type*) [Infinite K]
    (f : TwoRowPartition n → K) : ¬ Function.Surjective f := fun hf =>
  haveI := Finite.of_surjective f hf; not_finite K

end QOU.Braiding
