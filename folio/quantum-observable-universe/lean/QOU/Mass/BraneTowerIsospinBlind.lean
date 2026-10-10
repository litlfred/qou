import Mathlib.Algebra.BigOperators.Group.Finset.Powerset
import Mathlib.Data.Finset.Powerset
import Mathlib.Tactic

namespace QOU.Mass.BraneTowerIsospinBlind

open Finset

variable {R : Type*} [CommRing R]

/-- The R-side brane-tower term of a braid word `β` (drawn from an index type `ι`) on `n`
strands: a sum over subsets `S` of the `n − 1` adjacent generators of `z^{|S|}` times a
per-subset weight `w β |S|`. The Markov-trace structure makes the weight depend on the subset
*size* only (within a fixed word); `w β` lets it a-priori still depend on the word `β`. -/
def braneTowerW {ι : Type*} (β : ι) (n : ℕ) (z : R) (w : ι → ℕ → R) : R :=
  ∑ S ∈ (univ : Finset (Finset (Fin (n - 1)))), z ^ S.card * w β S.card

/-- **(b)-structural exclusion — isospin-blindness of the trace-invariant tower.**
If the per-subset weight is **Markov-invariant**, i.e. reduced-word independent
(`w β₁ = w β₂` — the cited invariant `tr_M(σ_i) = z` is reduced-word independent), then two
isobars `β₁, β₂` on the same `n = 3A` strands receive an **identical** brane-tower term. Hence
the contribution of the trace-invariant brane tower to the mirror-pair binding difference is
exactly `0`: any mirror split must be carried by `T₁` (descended `tr_M`) and `T₅` (chirality),
not the brane tower. This prunes the search (synthesis
`docs/audits/2026-06-26-t2t3-trace-invariance-status-synthesis.md`, owner-selected step 2). -/
theorem braneTowerW_isospin_blind {ι : Type*} (β₁ β₂ : ι) (A : ℕ) (z : R) (w : ι → ℕ → R)
    (hMarkov : w β₁ = w β₂) :
    braneTowerW β₁ (3 * A) z w = braneTowerW β₂ (3 * A) z w := by
  unfold braneTowerW
  rw [hMarkov]

/-- The Markov-invariant (word-independent) R-side tower, weight `f` a function of subset size
only — the genuinely trace-invariant form. -/
def braneTowerR (n : ℕ) (z : R) (f : ℕ → R) : R :=
  ∑ S ∈ (univ : Finset (Finset (Fin (n - 1)))), z ^ S.card * f S.card

/-- **The trace-invariant tower collapses to a function of `(n, z, f)` only**:
`braneTowerR n z f = ∑_{k ≤ n−1} C(n−1, k) z^k f k`. There is **no** braid-word input — this is
the algebraic content behind isospin-blindness (the value is fixed by the strand count `n = 3A`,
so two isobars of the same `A` get the same tower). -/
theorem braneTowerR_eq_binom_sum (n : ℕ) (z : R) (f : ℕ → R) :
    braneTowerR n z f = ∑ k ∈ range (n - 1 + 1), (Nat.choose (n - 1) k : R) * z ^ k * f k := by
  unfold braneTowerR
  rw [← Finset.powerset_univ, Finset.sum_powerset, Finset.card_univ, Fintype.card_fin]
  apply Finset.sum_congr rfl
  intro k _
  have hinner : ∀ t ∈ (univ : Finset (Fin (n - 1))).powersetCard k,
      z ^ t.card * f t.card = z ^ k * f k := by
    intro t ht
    rw [(Finset.mem_powersetCard.mp ht).2]
  rw [Finset.sum_congr rfl hinner, Finset.sum_const, Finset.card_powersetCard,
      Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
  ring

/-- Isobar corollary of the collapse: the word-independent tower on two same-`A` isobars is
identical (the value is `∑_k C(3A−1,k) z^k f k`, with no word input). -/
theorem braneTowerR_isospin_blind (A : ℕ) (z : R) (f : ℕ → R) :
    braneTowerR (3 * A) z f = ∑ k ∈ range (3 * A - 1 + 1), (Nat.choose (3 * A - 1) k : R) * z ^ k * f k :=
  braneTowerR_eq_binom_sum (3 * A) z f

end QOU.Mass.BraneTowerIsospinBlind
