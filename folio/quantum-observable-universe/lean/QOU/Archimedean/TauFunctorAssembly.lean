/-
# T5 assembly, first brick — the target is now PARAMETER-FREE: w = 5/2 derived from T1×T4

F-construction milestone `qou-a46k` (T1 #4039 dims, T2 #4040 module, T3 deck
reality, T4 weight values — all merged). This file assembles the T1
Chevalley–Weil dims (3,1) with the T4 canonical weight values (¾,¼) into the
canonical loop-weight operator and DERIVES the channel trace

    w  =  3·y₂(1) + 1·y₁₁(1)  =  3·(3/4) + 1·(1/4)  =  5/2,

eliminating the last free parameter of `ArchimedeanTauRealization`: the T5
obligation is no longer "inhabit the interface for some w" but "supply
functorial provenance for the SPECIFIC parameter-free target
`ArchimedeanTauRealization 4 (5/2)` with the T1-structured (3,1) block
operator".

HONESTY (STRICT, per the target spec's own `interface_alone_is_trivially_
inhabitable`): interface inhabitation carries NO weight — the spec proves a
bare diagonal matrix inhabits it for any real w. The `assembled` instance
below is therefore labeled a PACKAGING, never progress on the wall. The
content of this file is exclusively:

* `channelWeight_derived` — the prescribed weight is now a THEOREM of the
  T4 value module paired with the T1 dims (3 moving, 1 invariant), not a
  chosen parameter;
* `assembled` — the specific T1-structured operator (block-scalar ¾ on the
  3-dim moving block, ¼ on the invariant line, conjugate blocks equal per
  the shape T3's deck-reality equivariance forces) packages into the target
  type at the derived weight — so T5's residual obligation is now typed
  against a parameter-free target.

What remains open (THE wall, unchanged): functorial provenance — that the
framework's τ (F1–F5 of `TauFunctorReduction`) actually assigns this
operator to the canonical Markov weight. Nothing here asserts it; nothing
wired; `1/(8π)` stays phase-4.

-- Ref: [braden-disney-hogg-2022] https://arxiv.org/abs/2208.13692
-/
import QOU.Archimedean.TauFunctorTargetSpec
import QOU.Archimedean.MarkovWeightValueTransport

namespace QOU.Archimedean.TauFunctorAssembly

open Matrix
open QOU.Archimedean.TauFunctorTargetSpec
open QOU.Archimedean.TauRhoHodgeLiftInterface
open QOU.Archimedean.LiftFromReality
open QOU.Archimedean.MarkovWeightValueTransport

/-- The canonical channel-weight profile on H¹(Bring): the T4 value ¾ on the
T1 moving block (dims 3), ¼ on the invariant line (dim 1). -/
noncomputable def weightProfile (j : Fin 4) : ℝ := if (j : ℕ) < 3 then 3 / 4 else 1 / 4

/-- **The derived channel weight**: `Σ_j weightProfile j = 5/2` — and this is
exactly the T1-dims × T4-values pairing `3·y₂(1) + 1·y₁₁(1)`, a theorem of
the merged modules, not a chosen parameter. -/
theorem channelWeight_derived :
    3 * y2 1 + 1 * y11 1 = 5 / 2 ∧ (∑ j : Fin 4, weightProfile j) = 5 / 2 := by
  refine ⟨by rw [y2_at_one, y11_at_one]; norm_num, ?_⟩
  rw [Fin.sum_univ_four]
  norm_num [weightProfile]

/-- The per-factor block: the weight profile as a (real-entried) diagonal
operator on one Hodge factor. -/
noncomputable def weightBlock : Matrix (Fin 4) (Fin 4) ℂ :=
  Matrix.diagonal (fun j => ((weightProfile j : ℝ) : ℂ))

lemma weightBlock_map_star : weightBlock.map (starRingEnd ℂ) = weightBlock := by
  unfold weightBlock
  ext i j
  by_cases h : i = j <;>
    simp [Matrix.map_apply, Matrix.diagonal, h, Complex.conj_ofReal]

lemma weightBlock_conjTranspose : weightBlockᴴ = weightBlock := by
  unfold weightBlock
  rw [Matrix.diagonal_conjTranspose]
  congr 1
  funext j
  exact Complex.conj_ofReal _

/-- The assembled loop-weight operator on `H^{1,0} ⊕ H^{0,1}`: the weight
block on each factor, conjugate blocks equal (the shape T3's deck-reality
equivariance forces), off-diagonal blocks zero. -/
noncomputable def canonicalLoopWeight :
    Matrix (Fin 4 ⊕ Fin 4) (Fin 4 ⊕ Fin 4) ℂ :=
  Matrix.fromBlocks weightBlock 0 0 weightBlock

/-- **Packaging (labeled, per the spec's honesty rule): the parameter-free
target.** The T1-structured operator inhabits `ArchimedeanTauRealization` at
the DERIVED weight `w = 5/2`. Inhabitation itself is trivial (the spec proves
so); the content is that no free parameter remains — T5's obligation is now
provenance for THIS target. -/
noncomputable def assembled : ArchimedeanTauRealization 4 (5 / 2 : ℂ) where
  loopWeight := canonicalLoopWeight
  real := by
    rw [swap_conj_blocks]
    unfold canonicalLoopWeight
    simp only [Matrix.toBlocks_fromBlocks₁₁, Matrix.toBlocks_fromBlocks₁₂,
      Matrix.toBlocks_fromBlocks₂₁, Matrix.toBlocks_fromBlocks₂₂,
      weightBlock_map_star, Matrix.map_zero _ (map_zero (starRingEnd ℂ))]
  herm := by
    show canonicalLoopWeightᴴ = canonicalLoopWeight
    unfold canonicalLoopWeight
    rw [Matrix.fromBlocks_conjTranspose]
    simp only [weightBlock_conjTranspose, Matrix.conjTranspose_zero]
  channelTrace := by
    show (canonicalLoopWeight.toBlocks₁₁).trace = (5 / 2 : ℂ)
    unfold canonicalLoopWeight
    rw [Matrix.toBlocks_fromBlocks₁₁]
    unfold weightBlock
    rw [Matrix.trace_diagonal, Fin.sum_univ_four]
    norm_num [weightProfile]

/-- The equal-split consequence at the derived weight, end to end: the
conjugate block of the assembled operator also carries `5/2` — the ½ of
`½·a₀` instantiated at the parameter-free target (via the spec's
`discharge_equal_split`). -/
theorem assembled_equal_split :
    (assembled.loopWeight.toBlocks₂₂).trace = (5 / 2 : ℂ) :=
  discharge_equal_split assembled

end QOU.Archimedean.TauFunctorAssembly
