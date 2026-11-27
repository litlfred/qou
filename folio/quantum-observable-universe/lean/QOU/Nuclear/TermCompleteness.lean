import Mathlib.Data.Finset.Prod
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import HeckeTemperleyLieb.TemperleyLiebTower
import QOU.Nuclear.BlockChargeSectorTrace

/-!
# When is a list of mass, binding or decay terms complete?

Bean `qou-myts` (accuracy epic). Carl, 2026-11-27: *"how do we know that we have all the terms
when doing mass/binding/decay etc? we should be able to determine when we are complete, where to
identify the gaps … are all repn and characters covered? all partitions?"*

## The criterion

An observable of `n` strands (`n = 3A` quark strands for a nucleus of mass number `A`) is a
finite sum over a known index set. A formula is **complete** when it has a summand, with its own
free coefficient, for every element of that index set. A gap is then a *named missing summand*,
not a numerical residual (`residual_eq_missing`), and every missing summand is detected by one
test vector (`complete_iff_no_residual`).

The index set has three coordinates.

1. **Block** `k ∈ {0, …, ⌊n/2⌋}`: the two-row partition `λ = (n − k, k)` of `n`, i.e. the isospin
   `T = (n − 2k)/2`. These are *all* the partitions the convention-D trace sees: every `λ` with
   three or more rows has weight `0` (`TemperleyLiebTower.conventionD_kills_antisymmetriser`, and
   at every `n`, `CrossNucleonPairWedderburnZRemoval` / `OcneanuWeight`), and every two-row block
   has strictly positive weight `y = [n−2k+1]_q/[2]_qⁿ` for `q > 1` (`braid_block_weight_pos`).
   So no two-row block may be dropped, and no other partition needs a term. The block count is
   `⌊n/2⌋ + 1` (`card_blocks`), linear in `n`, not `p(n)`.
2. **Tensor rank** `r` of the operator inside the isospin multiplet `V_λ` (Wigner–Eckart). A
   `b`-body operator has rank `r ≤ b`, and a multiplet of isospin `T` carries ranks `r ≤ 2T` only.
   The `T_z` dependence inside a multiplet is therefore a polynomial of degree `≤ min(b, 2T)`.
3. **Channel**, with its maximal rank:
   * `braid` — the convention-D trace of a braid word. By quantum Schur–Weyl duality the Hecke
     algebra acts as the commutant of `U_q(sl₂)`, so these operators are isospin scalars:
     rank `0`. At `n = 3` the rank-1 part is proved to vanish for **every** word
     (`braid_channel_has_no_np_split`, from `BlockChargeSectorTrace.sectorTrace_eq`).
   * `flavour` — a one-body isospin-breaking operator (the `u`/`d` strand label): rank `≤ 1`.
   * `em` — the two-body charge–charge operator `Σ_{i<j} Q_i Q_j`: rank `≤ 2` (isoscalar,
     isovector, isotensor).

Distinct index entries carry independent reduced matrix elements. Each needs its own coefficient,
and in particular its own energy scale. This is the structural content behind PR #9654 (one map
`E` for the flavour and EM rank-1 terms forces a ratio the data reject): the nucleon block has
**two** independent rank-1 entries (`nucleon_rank_one_entries`), so one scale cannot serve both.

## What this file proves and what it does not

Proved, over any ring or field, with no measured value: the index set, its cardinalities at the
levels used in the audit, the residual identity, the detection criterion, the positivity of every
two-row braid weight, and the vanishing of the braid channel's rank-1 (`n`−`p`) part at `n = 3`.

Not proved here: Wigner–Eckart for `U_q(sl₂)` tensor operators (the rank caps of `flavour` and
`em` are encoded in `Channel.maxRank`, not derived), and the general-`n` statement that braid
traces are rank `0` (proved at `n = 3` only). The per-formula audit is
`docs/audits/2026-11-27-term-completeness-ledger.md`.
-/

namespace QOU.Nuclear.TermCompleteness

open Finset

/-! ## The index set -/

/-- The three operator channels, by maximal isospin tensor rank. -/
inductive Channel
  /-- Convention-D trace of a braid word: commutant of `U_q(sl₂)`, an isospin scalar. -/
  | braid
  /-- One-body isospin-breaking operator (the strand flavour label). -/
  | flavour
  /-- Two-body charge–charge operator `Σ_{i<j} Q_i Q_j`. -/
  | em
  deriving DecidableEq, Fintype, Repr

/-- The largest tensor rank a channel can carry (`b`-body ⟹ rank `≤ b`). -/
def Channel.maxRank : Channel → ℕ
  | .braid => 0
  | .flavour => 1
  | .em => 2

theorem Channel.maxRank_le_two (c : Channel) : c.maxRank ≤ 2 := by cases c <;> decide

/-- The two-row blocks at level `n`: `k` indexes `λ = (n − k, k)`. -/
def blocks (n : ℕ) : Finset ℕ := range (n / 2 + 1)

/-- **The block count is linear in `n`.** -/
theorem card_blocks (n : ℕ) : (blocks n).card = n / 2 + 1 := card_range _

/-- Twice the isospin of block `k` at level `n`: `2T = n − 2k`. -/
def twoT (n k : ℕ) : ℕ := n - 2 * k

/-- An index entry `(channel, block, rank)`. -/
abbrev Entry := Channel × ℕ × ℕ

/-- **The complete index set at level `n`.** An entry `(c, k, r)` is present when `k` is a
two-row block, `r ≤ c.maxRank` (body count) and `r ≤ 2T` (multiplet size). -/
def index (n : ℕ) : Finset Entry :=
  ((univ : Finset Channel) ×ˢ (blocks n ×ˢ range 3)).filter
    (fun e => e.2.2 ≤ e.1.maxRank ∧ e.2.2 ≤ twoT n e.2.1)

theorem mem_index {n : ℕ} {e : Entry} :
    e ∈ index n ↔ e.2.1 ≤ n / 2 ∧ e.2.2 ≤ e.1.maxRank ∧ e.2.2 ≤ twoT n e.2.1 := by
  obtain ⟨c, k, r⟩ := e
  simp only [index, blocks, mem_filter, mem_product, mem_univ, mem_range, true_and]
  constructor
  · rintro ⟨⟨hk, -⟩, hr, hT⟩; exact ⟨by omega, hr, hT⟩
  · rintro ⟨hk, hr, hT⟩
    exact ⟨⟨by omega, by have := c.maxRank_le_two; omega⟩, hr, hT⟩

/-- The braid channel carries rank `0` only, at every level and on every block. -/
theorem braid_rank_zero {n k r : ℕ} (h : (Channel.braid, k, r) ∈ index n) : r = 0 := by
  have := (mem_index.mp h).2.1
  simpa [Channel.maxRank] using this

/-! ## Ledgers, residuals and detection -/

/-- A formula's ledger: the index entries it has a term for. -/
structure Ledger (n : ℕ) where
  covered : Finset Entry

namespace Ledger

variable {n : ℕ}

/-- The entries the formula has no term for. -/
def missing (L : Ledger n) : Finset Entry := index n \ L.covered

/-- A formula is complete when it covers the whole index set. -/
def Complete (L : Ledger n) : Prop := index n ⊆ L.covered

theorem complete_iff_missing_eq_empty (L : Ledger n) : L.Complete ↔ L.missing = ∅ := by
  simp [Complete, missing, sdiff_eq_empty_iff_subset]

end Ledger

section Residual

variable {R : Type*} [AddCommGroup R] {n : ℕ}

/-- The full observable, given one reduced coefficient per index entry. -/
def full (n : ℕ) (c : Entry → R) : R := ∑ e ∈ index n, c e

/-- What a formula with ledger `L` evaluates: the sum over the entries it covers. -/
def covSum (L : Ledger n) (c : Entry → R) : R := ∑ e ∈ index n ∩ L.covered, c e

/-- **A gap is a missing summand.** The residual of a formula is exactly the sum of the terms it
does not have, whatever the coefficients are. -/
theorem residual_eq_missing (L : Ledger n) (c : Entry → R) :
    full n c - covSum L c = ∑ e ∈ L.missing, c e := by
  unfold full covSum Ledger.missing
  rw [← sum_inter_add_sum_diff (index n) L.covered c]
  abel

end Residual

/-- **Detection.** A formula is complete exactly when its residual vanishes for every choice of
reduced coefficients. If an entry `e` is missing, the test vector supported on `e` (the block's
central idempotent tensored with the rank-`r` component) gives residual `1`. -/
theorem complete_iff_no_residual {R : Type*} [Ring R] [Nontrivial R] {n : ℕ} (L : Ledger n) :
    L.Complete ↔ ∀ c : Entry → R, full n c = covSum L c := by
  constructor
  · intro hL c
    have h0 := residual_eq_missing L c
    rw [(L.complete_iff_missing_eq_empty).mp hL, sum_empty] at h0
    exact sub_eq_zero.mp h0
  · intro h
    by_contra hL
    rw [L.complete_iff_missing_eq_empty] at hL
    obtain ⟨e, he⟩ := nonempty_iff_ne_empty.mpr hL
    have h0 := residual_eq_missing L (fun x => if x = e then (1 : R) else 0)
    rw [h _, sub_self, sum_ite_eq' L.missing e, if_pos he] at h0
    exact zero_ne_one h0

/-! ## The braid channel: every block weighs, and no `n`−`p` split at `n = 3` -/

/-- **Every two-row block has positive convention-D weight.** For `q > 1` and every block
`k ≤ ⌊n/2⌋`, `y₍ₙ₋ₖ,ₖ₎ = [n−2k+1]_q/[2]_qⁿ > 0`. So a formula that drops a two-row block drops a
summand with nonzero weight; it cannot be justified by "that block has weight zero". -/
theorem braid_block_weight_pos {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    (q : R) (hq : 1 < q) {n k : ℕ} (_hk : k ∈ blocks n) :
    0 < QOU.QBeta.TemperleyLiebTower.yw q n (n - 2 * k + 1) :=
  QOU.QBeta.TemperleyLiebTower.yw_pos q hq n (Nat.succ_pos _)

/-- **Braid words cannot split the neutron from the proton.** On three strands, for every braid
word `w` and every `q ≠ 0`, the trace on the charge sector with one `u` strand equals the trace on
the sector with two `u` strands. That is the rank-1 (`T_z`-odd) part of the braid channel on the
nucleon block vanishing identically, as `braid_rank_zero` records. A restatement of
`BlockChargeSectorTrace.sectorTrace_eq`. -/
theorem braid_channel_has_no_np_split {K : Type*} [Field K] (q : K) (hq : q ≠ 0)
    (w : List QOU.QBeta.BlockChargeSectorTrace.Letter) :
    (QOU.QBeta.BlockChargeSectorTrace.wordMat q true w).trace
      - (QOU.QBeta.BlockChargeSectorTrace.wordMat q false w).trace = 0 :=
  sub_eq_zero.mpr (QOU.QBeta.BlockChargeSectorTrace.sectorTrace_eq q hq w)

/-! ## The index set at the levels the audit uses -/

/-- Level 3 (one nucleon): blocks `(3)` (`T = 3/2`, the Δ) and `(2,1)` (`T = 1/2`, the nucleon);
the sign block `(1,1,1)` has three rows and weight `0`. Eleven entries in all. -/
theorem card_index_three : (index 3).card = 11 := by decide

/-- **The nucleon block has exactly two rank-1 entries**: one flavour, one EM. They are
independent reduced matrix elements, so `m_n − m_p` needs two coefficients (two scales). -/
theorem nucleon_rank_one_entries :
    (index 3).filter (fun e => e.2.1 = 1 ∧ e.2.2 = 1)
      = {(Channel.flavour, 1, 1), (Channel.em, 1, 1)} := by decide

/-- The nucleon (`T = 1/2`) has no isotensor entry; the Δ block (`T = 3/2`) does. -/
theorem nucleon_no_isotensor :
    (Channel.em, 1, 2) ∉ index 3 ∧ (Channel.em, 0, 2) ∈ index 3 := by decide

/-- **`A = 12`: 19 blocks, not `p(36) = 17,977`.** The caveat in `mass_table_comprehensive.py`
("the correct sum over partitions of 3A is infeasible beyond A ≈ 12 — p(36) ≈ 18,000") counts
partitions the convention-D trace gives weight zero. The block index is linear in `A`. (Each
block's character can still be large; the count of *summands* is what is small.) -/
theorem card_blocks_A12 : (blocks 36).card = 19 := card_blocks 36

/-- A level-3 formula reused at level `3A` misses blocks: already at `A = 2` the braid entry of
block `(4,2)` exists at level 6 and has no counterpart at level 3. -/
theorem level_three_misses_level_six :
    (Channel.braid, 2, 0) ∈ index 6 ∧ (Channel.braid, 2, 0) ∉ index 3 := by decide

/-! ## Ledgers of formulas on record (details in the audit) -/

/-- Every braid-trace-only formula: the `T³` weight-trace `Q_β` split, the closed-form binding
`tr_M(𝓑_K)`, the Q-CLT proxy. It covers the braid entries and nothing else. -/
def traceOnly (n : ℕ) : Ledger n := ⟨(index n).filter (fun e => e.1 = Channel.braid)⟩

/-- A trace-only formula misses both rank-1 nucleon entries, so its `n`−`p` split is not a small
number to be corrected: it is identically zero (`braid_channel_has_no_np_split`), and the split
must come entirely from the two missing summands. -/
theorem traceOnly_misses_np :
    (Channel.flavour, 1, 1) ∈ (traceOnly 3).missing ∧
      (Channel.em, 1, 1) ∈ (traceOnly 3).missing := by decide

/-- The mass facade (`canonical_mass`): braid entries plus the flavour split `δ` on the nucleon.
It misses the EM rank-1 entry of the nucleon block. -/
def massFacade : Ledger 3 :=
  ⟨(index 3).filter (fun e => e.1 = Channel.braid) ∪ {(Channel.flavour, 1, 1)}⟩

theorem massFacade_misses_em : (Channel.em, 1, 1) ∈ massFacade.missing := by decide

theorem traceOnly_not_complete (n : ℕ) : ¬ (traceOnly n).Complete := by
  intro h
  have hmem : (Channel.flavour, 0, 0) ∈ index n := mem_index.mpr ⟨Nat.zero_le _, by decide,
    Nat.zero_le _⟩
  have := h hmem
  simp [traceOnly] at this

end QOU.Nuclear.TermCompleteness
