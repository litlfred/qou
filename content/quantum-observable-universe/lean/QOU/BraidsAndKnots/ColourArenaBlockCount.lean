import QOU.MathlibExt.QPartitionCombinatorics

/-!
# QOU.BraidsAndKnots.ColourArenaBlockCount
  — the block-count backbone of "no finite colour arena"

The production nuclear-mass trace is the **full Hecke / Wenzl principal
specialization** `s_λ(1, q, q², …)`, which is nonzero for **every** partition
`λ`.  A finite colour arena `ℂ^N` realizes the `N`-variable specialization
`s_λ(1, q, …, q^{N-1})`, which by the **Schur row-bound**

      s_λ(x₁, …, x_N) = 0   ⟺   rows(λ) > N

is **zero** for every `λ` with more than `N` rows.  So a finite `ℂ^N` "misses"
the trace content carried by the `>N`-row Wedderburn blocks.  The empirical
*weighted* miss-share grows with the mass number `A` (`3.4%` @⁴He → `6.0%` @⁵He,
audit `2026-06-16-keystone-arena-is-full-hecke-not-su3.md`).

This file formalizes the part that is a **theorem**: the *block-count* backbone.
The Schur row-bound itself is a classical symmetric-function fact (verified
numerically for `n = 5, 6` in `keystone_full_hecke_not_su3_arena.py` and
`colour_arena_missed_block_count.py`); here it is the **premise** defining
`missedByColourArena`, and the **counting consequence** is proved sorry-free:

  * `appendUnitRows N` injects **every** partition of size `m` into the
    colour-`ℂ^N`-MISSED partitions of size `m + (N+1)`
    (`missedEmbedding`, `missedEmbedding_injective`);
  * hence the missed-block family is **unbounded** as the size `n ∝ A` grows —
    *no finite `N` captures the trace for all `A`* (`no_finite_colour_arena`).

The witness appends `N+1` unit rows (`μ ↦ μ ++ (1^{N+1})`), extending the first
column downward by `N+1` boxes; it is **canonical** (weakly-decreasing) whenever
`μ` is, since every part of `μ` is `≥ 1`.  Rows `= List.length` (the corpus
`Partition := List ℕ` imposes no order at the type level, but the witness stays
in canonical form).

The *weighted* miss-share monotonicity (`3.4% → 6.0%`) is **not** formalized: it
is `q₀`- and braid-dependent (principal-spec weights × oscillating
`χ_λ(β_A)`), and is the weighted face of this count backbone, not a corollary.

Refs:
- [macdonald1995] Symmetric Functions and Hall Polynomials, I.3 (Schur row-bound)
- [wenzl1988] Hecke algebras of type A_n and subfactors, Invent. Math. 92
- [manuscript] docs/audits/2026-06-19-colour-arena-block-count-theorem.md
-/

open QOU.MathlibExt.QPartitionCombinatorics

namespace QOU.BraidsAndKnots.ColourArenaBlockCount

/-- A partition `λ` is **captured** by a finite colour-`ℂ^N` arena iff its
    `N`-variable principal Schur specialization is nonzero, i.e. (Schur
    row-bound) iff `rows(λ) ≤ N`.  Rows `= List.length`. -/
def capturedByColourArena (N : ℕ) (lam : Partition) : Prop := lam.length ≤ N

/-- A partition `λ` is **missed** by a finite colour-`ℂ^N` arena iff `rows(λ) > N`
    (its `N`-variable Schur specialization vanishes). -/
def missedByColourArena (N : ℕ) (lam : Partition) : Prop := N < lam.length

theorem missed_iff_not_captured (N : ℕ) (lam : Partition) :
    missedByColourArena N lam ↔ ¬ capturedByColourArena N lam := by
  unfold missedByColourArena capturedByColourArena; omega

/-- **Append `N+1` unit rows**: `μ ↦ μ ++ (1^{N+1})`.  Extends the first column
    downward by `N+1` boxes, so the row count jumps by `N+1`.  Canonical
    (weakly-decreasing) whenever `μ` is, since each part of `μ` is `≥ 1`. -/
def appendUnitRows (N : ℕ) (mu : Partition) : Partition :=
  mu ++ List.replicate (N + 1) 1

@[simp] theorem appendUnitRows_length (N : ℕ) (mu : Partition) :
    (appendUnitRows N mu).length = mu.length + (N + 1) := by
  simp [appendUnitRows, Partition.length]

@[simp] theorem appendUnitRows_sum (N : ℕ) (mu : Partition) :
    (appendUnitRows N mu).sum = mu.sum + (N + 1) := by
  simp [appendUnitRows, List.sum_replicate]

/-- The appended unit rows give a partition the colour-`ℂ^N` arena **misses**
    (it has `≥ N+1 > N` rows). -/
theorem appendUnitRows_missed (N : ℕ) (mu : Partition) :
    missedByColourArena N (appendUnitRows N mu) := by
  unfold missedByColourArena
  rw [appendUnitRows_length]
  omega

/-- `appendUnitRows N` is **injective**: distinct shapes give distinct images
    (strip the fixed `N+1` trailing unit rows). -/
theorem appendUnitRows_injective (N : ℕ) :
    Function.Injective (appendUnitRows N) := by
  intro a b h
  unfold appendUnitRows at h
  exact List.append_cancel_right h

/-- **Block-count backbone.**  For every target size `m`, `appendUnitRows N`
    embeds the partitions of size `m` into the colour-`ℂ^N`-MISSED partitions of
    size `m + (N+1)`.  Since `m` is arbitrary, the missed-block family is
    unbounded as the size (`∝ A`) grows. -/
def missedEmbedding (N m : ℕ) :
    {mu : Partition // mu.sum = m} →
      {lam : Partition // lam.sum = m + (N + 1) ∧ missedByColourArena N lam} :=
  fun mu =>
    ⟨appendUnitRows N mu.1,
      by rw [appendUnitRows_sum, mu.2],
      appendUnitRows_missed N mu.1⟩

theorem missedEmbedding_injective (N m : ℕ) :
    Function.Injective (missedEmbedding N m) := by
  intro a b h
  apply Subtype.ext
  have hv : appendUnitRows N a.1 = appendUnitRows N b.1 := by
    simpa [missedEmbedding] using congrArg Subtype.val h
  exact appendUnitRows_injective N hv

/-- **No finite colour arena.**  For every fixed colour dimension `N` and every
    shape `μ`, there is a partition of size `|μ| + (N+1)` that the colour-`ℂ^N`
    arena misses; ranging `μ` over all partitions of `m = n-(N+1)` gives (via the
    injection `missedEmbedding`) at least `p(n-N-1)` distinct missed blocks at
    size `n` — unbounded in `A`.

    This is the structural upgrade of "no finite colour arena" from the empirical
    `3.4% → 6.0%` data points to a block-count theorem: a finite `ℂ^N` cannot
    capture the full-Hecke trace for all mass numbers `A`. -/
theorem no_finite_colour_arena (N : ℕ) (mu : Partition) :
    ∃ lam : Partition,
      lam.sum = mu.sum + (N + 1) ∧ missedByColourArena N lam :=
  ⟨appendUnitRows N mu, appendUnitRows_sum N mu, appendUnitRows_missed N mu⟩

end QOU.BraidsAndKnots.ColourArenaBlockCount
