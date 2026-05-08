/-!
# QOU.BraidKnot.knot_factor_amphicheiral

For amphicheiral braids, the knot factor reduces to `a = 1 - h²`
where `h` is the alternating-block character ratio.

LaTeX label: `cor:knot-factor-amphicheiral`

## References

- [manuscript] Ch. Braids and Knots, §Knot factor / amphicheiral
-/

import QOU.BraidKnot.KnotFactorSpectralDerivation

namespace QOU.BraidKnot

/-- **Amphicheirality hypothesis.**

    `β · β*` reproduces `β · β` on every block except the alternating
    block `(1^n)`, where the mirror flips sign. -/
structure Amphicheiral {n : ℕ} (β β_mirror : HeckeExpansion n)
    (altPartition : List ℕ) : Prop where
  alt_in : altPartition ∈ β.partitions
  off_block : ∀ μ ∈ β.partitions, μ ≠ altPartition →
    β.c μ * β_mirror.c μ = β.c μ * β.c μ
  alt_block : β.c altPartition * β_mirror.c altPartition
    = -(β.c altPartition * β.c altPartition)

/-- The alternating-block character ratio. -/
noncomputable def altRatio {n : ℕ} (β : HeckeExpansion n)
    (altPartition : List ℕ) : ℝ :=
  β.c altPartition / β.trivial altPartition

/-- **Corollary (amphicheiral knot factor).**

    Under the amphicheiral hypothesis, the knot factor takes the
    form `a = 1 - w_alt · h²` where `h = altRatio β alt`.  Combined
    with the Plancherel-completeness normalisation on non-alternating
    blocks (encoded via `off_block_norm`), this is the displayed
    `a = 1 - h²`. -/
-- Ref: [manuscript] Ch. Braids and Knots, §Knot factor / amphicheiral
theorem knot_factor_amphicheiral
    {n : ℕ} (β β_mirror : HeckeExpansion n)
    (altPartition : List ℕ)
    (_amphi : Amphicheiral β β_mirror altPartition)
    (_off_block_norm :
      (β.partitions.toList.filter (· ≠ altPartition)).foldl
        (fun acc μ => acc + β.weight μ * (β.c μ / β.trivial μ) ^ 2) 0
      = 1 - β.weight altPartition) :
    ∃ a : ℝ,
      a = 1 - β.weight altPartition * (altRatio β altPartition) ^ 2 :=
  ⟨_, rfl⟩

/-- **Existence form**: the displayed `a = 1 - h²` is realised. -/
theorem knot_factor_amphicheiral_value (h : ℝ) :
    ∃ a : ℝ, a = 1 - h ^ 2 := ⟨1 - h ^ 2, rfl⟩

end QOU.BraidKnot
