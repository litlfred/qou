import Mathlib.Data.List.Basic

/-!
# QOU.Molecular.symmetric_assembly_projector_exists

For every strand-partition there exists the *data* of a symmetric-block
assembly projector: take the target Wedderburn block to be the one-row
partition `μ = (N)`.  The algebraic idempotency `e² = e` of the
corresponding element of `H_N(q)` is the `q`-Young-symmetriser / Wenzl
property, cited in the narrative — existence of the projector data is the
combinatorial precondition for it.

This deliberately proves only the combinatorial existence, keeping the
free (algebraic) fact distinct from the earned (physical) stability claim
made elsewhere.

## References
- [wenzl1988] https://doi.org/10.1007/BF01393695
- [kassel1995] Kassel, "Quantum Groups," GTM 155
-/

namespace QOU.Molecular

/-- Combinatorial data of an assembly projector: a strand-partition and a
    target Wedderburn block partitioning the same `N`. -/
structure AssemblyProjectorData where
  parts : List ℕ
  block : List ℕ
  block_total : block.sum = parts.sum

/-- For every strand-partition, the symmetric-block (`μ = (N)`) assembly
    projector data exists.  (Idempotency `e² = e` in `H_N(q)` is the
    `q`-Young-symmetriser property, cited in the narrative.) -/
-- Ref: [wenzl1988] https://doi.org/10.1007/BF01393695
-- Ref: [kassel1995] Kassel, "Quantum Groups," GTM 155
theorem symmetric_assembly_projector_exists (parts : List ℕ) :
    ∃ d : AssemblyProjectorData, d.parts = parts ∧ d.block = [parts.sum] :=
  ⟨{ parts := parts, block := [parts.sum], block_total := by simp }, rfl, rfl⟩

end QOU.Molecular
