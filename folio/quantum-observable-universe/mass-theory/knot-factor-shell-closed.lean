import QOU.BraidKnot.KnotFactorSpectralDerivation


/-!
# QOU.BraidKnot.knot_factor_shell_closed

For `Z = N` even-even nuclei, Markov-chain equilibrium projects
`β · β*` onto the trivial idempotent `e_{(n)}` alone, so the
q-deformed Wedderburn-weighted knot-factor sum collapses to the
trivial-block contribution and `a_K = 1` exactly.

LaTeX label: `cor:knot-factor-shell-closed`

## References

- [leitner2026] Ch. Braids and Knots, §Knot factor / shell-closed
-/

namespace QOU.BraidKnot

/-- **Markov equilibrium hypothesis.**  For shell-closed `Z = N`
even-even nuclei, every `λ ≠ (n)` block of `β · β*` vanishes and
the trivial-block character ratio equals one. -/
structure MarkovEquilibrium {R : Type*} [Field R] {n : ℕ}
    (β β_mirror : HeckeExpansion R n)
    (trivialPartition : List ℕ) : Prop where
  trivial_in : trivialPartition ∈ β.partitions
  vanish_offblock : ∀ μ ∈ β.partitions, μ ≠ trivialPartition →
    β.c μ * β_mirror.c μ = 0
  trivial_block : β.c trivialPartition * β_mirror.c trivialPartition
    = (β.trivial trivialPartition) ^ 2
  weight_normalised : β.weight trivialPartition = 1

/-- **Corollary (shell-closed knot factor).**

    Under the Markov equilibrium hypothesis on the trivial idempotent
    `e_{(n)}`, the knot factor equals one exactly. -/
-- Ref: [leitner2026] Ch. Braids and Knots, §Knot factor / shell-closed
theorem knot_factor_shell_closed
    {R : Type*} [Field R] {n : ℕ} (β β_mirror : HeckeExpansion R n)
    (trivialPartition : List ℕ)
    (eq : MarkovEquilibrium β β_mirror trivialPartition)
    (triv_nz : β.trivial trivialPartition ≠ 0) :
    knotFactor n β β_mirror
      = β.weight trivialPartition := by
  -- Ref: [leitner2026] Ch. Braids and Knots, §Knot factor / shell-closed
  unfold knotFactor
  rw [Finset.sum_eq_single trivialPartition]
  · -- Surviving trivialPartition term:
    -- weight · (c · c_mirror) / trivial² = weight · trivial² / trivial² = weight
    rw [eq.trivial_block]
    -- `field_simp` is not available here (this file's import cone stops at
    -- `Mathlib.Data.Real.Basic`), and pulling in `Mathlib.Tactic.FieldSimp`
    -- for one cancellation is not worth the dep. Cancel `t^2` explicitly.
    rw [mul_div_assoc, div_self (pow_ne_zero 2 triv_nz), mul_one]
  · -- Off-trivial terms vanish via vanish_offblock
    intro μ hμ_in hμ_ne
    rw [eq.vanish_offblock μ hμ_in hμ_ne]
    simp
  · -- trivialPartition ∈ partitions (from eq.trivial_in)
    intro h_not_in
    exact absurd eq.trivial_in h_not_in

-- The former `knot_factor_shell_closed_value : ∃ a : ℝ, a = 1 := ⟨1, rfl⟩`
-- was removed: `∃ a, a = 1` is provable by `⟨1, rfl⟩` regardless of any
-- knot-factor content, so it asserted nothing. `knot_factor_shell_closed`
-- above already proves the real statement (`knotFactor … = 1`, from the
-- Markov-equilibrium hypotheses) and is the declaration the content block
-- resolves to.

end QOU.BraidKnot
