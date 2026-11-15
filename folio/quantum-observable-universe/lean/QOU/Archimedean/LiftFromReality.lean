/-
# Lift-from-reality — an instance CONSTRUCTOR for the B2 lift, and the wall's final form

Bean `qou-tq20` (B2 lift), third tranche: the honest attempt at the
`TauRhoHodgeLift` instance, delivered as a **constructor theorem**: any
hermitian operator on the conjugate-doubled space `H^{1,0} ⊕ H^{0,1}` that
commutes with the doubling's antilinear swap-conjugation `C(x,y) = (ȳ, x̄)`
induces a LEGITIMATE lift instance on its diagonal blocks — the two class
fields are *proved* from the reality premise, not assumed.

Consequences:

* `conjugated_of_real` — reality (`C M C = M`, matrix form
  `P · (M.map star) · P = M` with `P` the block swap) FORCES the lower
  diagonal block to be the entrywise conjugate of the upper one: the lift's
  `conjugated` field is *automatic* for real operators.
* `hermitian_block_of_isHermitian` — self-adjointness of the full operator
  passes to the `H^{1,0}` block: the `hermitian` field is automatic too.
* `TauRhoHodgeLift.of_real_operator` — the constructor: reality +
  self-adjointness ⟹ the lift instance on the diagonal blocks. This is a
  THEOREM producing instances from a premise (never a fabricated
  `instance` declaration): whoever supplies a real self-adjoint loop weight
  operator on `H¹(Bring)` gets the lift — and with it, via the merged
  bricks, the per-loop measure `½·a₀` — legitimately.

**The wall's final form.** Combining with the merged plan (B1 #3955, B2s
#3960, B3 #3969, B4a #3973, B4b #3977, B5 #3982, interface #3985, ℂ-model
#3992), the entire α_EM per-loop wall reduces to ONE named premise:

  *(Reality realization)* — the α_EM loop weight operator on `H¹(Bring)`
  is real self-adjoint and commutes with the Hodge swap-conjugation, with
  `H^{1,0}`-block equal to the τ-image of the canonical Markov channel
  weight.

For a Laplacian-derived weight (any real metric's heat weight — the B3
route) the reality premise HOLDS by construction; what remains open is
exactly the τ-identification of the categorical Markov weight with such a
Laplacian-derived weight. Nothing here derives that identification; no
`instance` is declared; nothing is wired; `1/(8π)` stays phase-4.

-- Ref: [braden-disney-hogg-2022] https://arxiv.org/abs/2208.13692
-/
import Mathlib.Data.Matrix.Block
import QOU.Archimedean.TauRhoHodgeLiftInterface

namespace QOU.Archimedean.LiftFromReality

open Matrix
open QOU.Archimedean.TauRhoHodgeLiftInterface

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- The block swap `P` on the doubled space `V ⊕ V̄` — the linear part of the
antilinear swap-conjugation `C(x,y) = (ȳ, x̄)` (matrix form: `C = P ∘ conj`). -/
def swapP (n : Type*) [Fintype n] [DecidableEq n] : Matrix (n ⊕ n) (n ⊕ n) ℂ :=
  Matrix.fromBlocks 0 1 1 0

/-- Conjugating a block operator by the swap-conjugation `C`: matrix form
`P · (M.map star) · P` exchanges the diagonal blocks and conjugates entries. -/
theorem swap_conj_blocks (M : Matrix (n ⊕ n) (n ⊕ n) ℂ) :
    swapP n * M.map (starRingEnd ℂ) * swapP n =
      Matrix.fromBlocks ((M.toBlocks₂₂).map (starRingEnd ℂ))
        ((M.toBlocks₂₁).map (starRingEnd ℂ))
        ((M.toBlocks₁₂).map (starRingEnd ℂ))
        ((M.toBlocks₁₁).map (starRingEnd ℂ)) := by
  have hM : M.map (starRingEnd ℂ) =
      Matrix.fromBlocks ((M.toBlocks₁₁).map (starRingEnd ℂ))
        ((M.toBlocks₁₂).map (starRingEnd ℂ))
        ((M.toBlocks₂₁).map (starRingEnd ℂ))
        ((M.toBlocks₂₂).map (starRingEnd ℂ)) := by
    rw [← Matrix.fromBlocks_map, Matrix.fromBlocks_toBlocks]
  rw [swapP, hM, Matrix.fromBlocks_multiply, Matrix.fromBlocks_multiply]
  simp

/-- **Reality forces the `conjugated` field.** If the full operator commutes
with the swap-conjugation (`C M C = M`), its lower diagonal block is the
entrywise conjugate of its upper diagonal block. -/
theorem conjugated_of_real (M : Matrix (n ⊕ n) (n ⊕ n) ℂ)
    (hreal : swapP n * M.map (starRingEnd ℂ) * swapP n = M) :
    M.toBlocks₂₂ = (M.toBlocks₁₁).map (starRingEnd ℂ) := by
  have h := congrArg Matrix.toBlocks₂₂ ((swap_conj_blocks M).symm.trans hreal)
  simpa [Matrix.toBlocks_fromBlocks₂₂] using h.symm

omit [Fintype n] [DecidableEq n] in
/-- Self-adjointness of the full operator passes to the `H^{1,0}` block. -/
theorem hermitian_block_of_isHermitian (M : Matrix (n ⊕ n) (n ⊕ n) ℂ)
    (hM : M.IsHermitian) : (M.toBlocks₁₁).IsHermitian := by
  have h := congrArg Matrix.toBlocks₁₁ hM.eq
  rw [← Matrix.fromBlocks_toBlocks M, Matrix.fromBlocks_conjTranspose,
    Matrix.toBlocks_fromBlocks₁₁, Matrix.toBlocks_fromBlocks₁₁] at h
  exact h

/-- **The instance constructor (the honest discharge path).** Any hermitian
operator on the doubled space commuting with the swap-conjugation induces a
legitimate `TauRhoHodgeLift` on its diagonal blocks — both class fields are
PROVED from the reality premise. The open wall is exactly the premise: that
the actual α_EM loop weight operator on `H¹(Bring)` is such an operator with
`H^{1,0}`-block the τ-image of the canonical Markov channel weight. -/
theorem tauRhoHodgeLift_of_real_operator {g : ℕ}
    (M : Matrix (Fin g ⊕ Fin g) (Fin g ⊕ Fin g) ℂ)
    (hM : M.IsHermitian)
    (hreal : swapP (Fin g) * M.map (starRingEnd ℂ) * swapP (Fin g) = M) :
    TauRhoHodgeLift g M.toBlocks₁₁ M.toBlocks₂₂ :=
  ⟨hermitian_block_of_isHermitian M hM, conjugated_of_real M hreal⟩

/-- With the constructor in hand, the conditional measure conclusions of the
interface apply to any real self-adjoint loop operator: its two Hodge-block
weights split equally — the ½ of `½·a₀`, end to end. -/
theorem equal_split_of_real_operator {g : ℕ}
    (M : Matrix (Fin g ⊕ Fin g) (Fin g ⊕ Fin g) ℂ)
    (hM : M.IsHermitian)
    (hreal : swapP (Fin g) * M.map (starRingEnd ℂ) * swapP (Fin g) = M) :
    (M.toBlocks₂₂).trace = (M.toBlocks₁₁).trace :=
  letI := tauRhoHodgeLift_of_real_operator M hM hreal
  TauRhoHodgeLift.equal_split

end QOU.Archimedean.LiftFromReality
