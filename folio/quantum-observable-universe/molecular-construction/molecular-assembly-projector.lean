import Mathlib.Data.List.Basic

/-!
# QOU.Molecular.AssemblyProjector — molecular assembly projector

The canonical idempotent $e_{\lambda,\mu} \in H_N(q)$ projecting a
composite assembled over the parabolic $H_\lambda$ onto a Wedderburn
block $\mu \vdash N$ — the $q$-Young symmetriser / Wenzl projector.
Projection onto the one-row symmetric block $\mu = (N)$ is
delocalisation.

The structure records the combinatorial pair $(\lambda,\mu)$; the
algebraic idempotency $e^2 = e$ in $H_N(q)$ is the Wenzl property cited
in the narrative and in `assembly-projector-exists`.

## References
- [wenzl1988] https://doi.org/10.1007/BF01393695
- [leitner2026] Ch. 12, Definition: Molecular assembly projector
-/

namespace QOU.Molecular

/-- An assembly projector, recorded by the strand-partition `parts` and
    the target Wedderburn block `block`, which partition the same `N`. -/
-- Ref: [wenzl1988] https://doi.org/10.1007/BF01393695
structure AssemblyProjector where
  /-- Strand-partition (per-sub-unit counts). -/
  parts : List ℕ
  /-- Target Wedderburn block `μ ⊢ N`. -/
  block : List ℕ
  /-- `μ` partitions the same total `N` as `λ`. -/
  block_total : block.sum = parts.sum

namespace AssemblyProjector

/-- Delocalised: projection onto the one-row symmetric block `μ = (N)`. -/
def isDelocalized (e : AssemblyProjector) : Prop := e.block = [e.parts.sum]

/-- The benzene symmetric-block projector `e_{(2,2,2),(6)}`. -/
def benzene : AssemblyProjector := ⟨[2, 2, 2], [6], by decide⟩

/-- The benzene projector is delocalised onto the symmetric block. -/
theorem benzene_isDelocalized : benzene.isDelocalized := by
  unfold isDelocalized benzene; decide

end AssemblyProjector
end QOU.Molecular
