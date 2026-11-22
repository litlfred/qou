import QOU.BraidKnot.KnotFactorSpectralDerivation


/-!
# QOU.BraidKnot.knot_factor_amphicheiral

For amphicheiral braids, the knot factor reduces to `a = 1 - h²`
where `h` is the alternating-block character ratio.

LaTeX label: `cor:knot-factor-amphicheiral`

## Base ring (AGENTS.md §7c)

Pre-archimedean, inherited: `HeckeExpansion` is now generic over its
Hecke base ring `{R : Type*} [Field R]` (see
`KnotFactorSpectralDerivation` for why a field, not a `CommRing`, is
the weakest admissible class), so the amphicheiral corollary is too.
No ordering, no `Real.*`, no archimedean input appears here.

## References

- [leitner2026] Ch. Braids and Knots, §Knot factor / amphicheiral
-/

namespace QOU.BraidKnot

variable {R : Type*} [Field R]

/-- **Amphicheirality hypothesis.**

    `β · β*` reproduces `β · β` on every block except the alternating
    block `(1^n)`, where the mirror flips sign. -/
structure Amphicheiral {n : ℕ} (β β_mirror : HeckeExpansion R n)
    (altPartition : List ℕ) : Prop where
  alt_in : altPartition ∈ β.partitions
  off_block : ∀ μ ∈ β.partitions, μ ≠ altPartition →
    β.c μ * β_mirror.c μ = β.c μ * β.c μ
  alt_block : β.c altPartition * β_mirror.c altPartition
    = -(β.c altPartition * β.c altPartition)

/-- The alternating-block character ratio. -/
def altRatio {n : ℕ} (β : HeckeExpansion R n)
    (altPartition : List ℕ) : R :=
  β.c altPartition / β.trivial altPartition

/-- **Corollary (amphicheiral knot factor).**

    Under the amphicheiral hypothesis, every non-alternating block
    contributes its own square `w_μ · (χ_μ(β)/χ_μ(𝟙))²` — the mirror
    is invisible there — while the alternating block contributes
    `-w_alt · h²`, `h = altRatio β alt`.  With the Plancherel
    normalisation `off_block_norm` on the non-alternating blocks,

      `a_K(β, β*) = 1 - w_alt · (1 + h²)` .

    **This is not the manuscript's displayed `a = 1 - h²`, and the
    difference is not a rearrangement.**  The displayed form needs the
    non-alternating blocks to sum to `1`; `off_block_norm` as stated
    (and as the `.ts` block's `computation` probe checks it) sums them
    to `1 - w_alt`, which leaves the extra `-w_alt` above.  They
    coincide only at `w_alt = 0`, where both sides are `1` and the
    corollary says nothing about `h`.  Recorded rather than reconciled:
    which of the two normalisations the chapter intends is an authoring
    question, not one this file can settle.  See `cor:knot-factor-amphicheiral`.

    The statement replaces `∃ a, a = …`, which held for every `β`,
    `β_mirror` and `altPartition` and so used neither hypothesis. -/
-- Ref: [leitner2026] Ch. Braids and Knots, §Knot factor / amphicheiral
theorem knot_factor_amphicheiral
    {n : ℕ} (β β_mirror : HeckeExpansion R n)
    (altPartition : List ℕ)
    (amphi : Amphicheiral β β_mirror altPartition)
    (off_block_norm :
      ∑ mu ∈ β.partitions.erase altPartition,
        β.weight mu * (β.c mu / β.trivial mu) ^ 2
      = 1 - β.weight altPartition) :
    knotFactor n β β_mirror
      = 1 - β.weight altPartition * (1 + (altRatio β altPartition) ^ 2) := by
  rw [knot_factor_spectral_form, ← Finset.add_sum_erase _ _ amphi.alt_in]
  have halt :
      β.weight altPartition * (β.c altPartition * β_mirror.c altPartition)
          / (β.trivial altPartition) ^ 2
        = -(β.weight altPartition * (altRatio β altPartition) ^ 2) := by
    rw [amphi.alt_block, altRatio, div_pow]
    ring
  have hoff : ∀ mu ∈ β.partitions.erase altPartition,
      β.weight mu * (β.c mu * β_mirror.c mu) / (β.trivial mu) ^ 2
        = β.weight mu * (β.c mu / β.trivial mu) ^ 2 := by
    intro mu hmu
    rw [amphi.off_block mu (Finset.mem_of_mem_erase hmu) (Finset.ne_of_mem_erase hmu),
        div_pow]
    ring
  rw [halt, Finset.sum_congr rfl hoff, off_block_norm]
  ring

end QOU.BraidKnot
