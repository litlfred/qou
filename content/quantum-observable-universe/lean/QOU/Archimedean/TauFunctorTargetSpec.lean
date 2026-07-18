/-
# The archimedean τ-functor target specification — what must be built, and why nothing less

Bean `qou-tq20` (B2 lift), tranche 8 — the categorical scaffold closing
today's arc. The parameter-free numerical program is exhausted (#4022,
#4027, #4030): the identification's dictionary is the archimedean τ-functor
itself. This file states the **typed target** of that construction and
machine-checks two facts that frame it honestly:

* `ArchimedeanTauRealization` — the interface data the measure derivation
  needs: a loop-weight operator on the doubled space `H^{1,0} ⊕ H^{0,1}`
  that is real (swap-conjugation-commuting), self-adjoint, and whose
  `H^{1,0}`-block trace carries a prescribed channel weight.
* `discharge` — ANY realization yields the `TauRhoHodgeLift` instance via
  the #3999 constructor, and with it (through the merged bricks) the
  per-loop measure `½·a₀`: **inhabiting this type with functorial
  provenance discharges the wall.**
* `interface_alone_is_trivially_inhabitable` — the interface WITHOUT
  functorial provenance is inhabited by a bare diagonal matrix. This is the
  point, machine-checked: the wall is NOT the interface, the numerics, or
  the reality structure (all free) — it is EXCLUSIVELY the functorial
  provenance: constructing the archimedean τ-functor from the framework's
  braided category with
    F(channel pair e₊/e₋ at the degenerate locus) = (H^{1,0}, H^{0,1})
      (shadow FORCED, #3960; ℂ-model #3992),
    F ∘ ρ = Hodge conjugation ∘ F        (B1 dictionary, #3955),
    F(canonical Markov weight) = the loop weight operator's H^{1,0}-block
      (the Reality-realization premise, #3999),
  natural in the categorical data — which no interface field can encode
  without the category itself.

Per §"Axiomatization is NOT a Proof": nothing here asserts the functor
exists; the trivial inhabitant is labeled as demonstrating NON-sufficiency
of the interface, never as progress on the wall; nothing wired; `1/(8π)`
stays phase-4.

-- Ref: [braden-disney-hogg-2022] https://arxiv.org/abs/2208.13692
-/
import Mathlib.Data.Matrix.Block
import QOU.Archimedean.TauRhoHodgeLiftInterface
import QOU.Archimedean.LiftFromReality

namespace QOU.Archimedean.TauFunctorTargetSpec

open Matrix
open QOU.Archimedean.TauRhoHodgeLiftInterface
open QOU.Archimedean.LiftFromReality

/-- The interface data the measure derivation needs from the archimedean
τ-functor. `w` is the prescribed `H^{1,0}` channel-weight trace (the τ-image
of the canonical Markov weight — the functorial provenance requirement lives
OUTSIDE this type, in the category; see the module docstring). -/
structure ArchimedeanTauRealization (g : ℕ) (w : ℂ) where
  loopWeight : Matrix (Fin g ⊕ Fin g) (Fin g ⊕ Fin g) ℂ
  real : swapP (Fin g) * loopWeight.map (starRingEnd ℂ) * swapP (Fin g) = loopWeight
  herm : loopWeight.IsHermitian
  channelTrace : (loopWeight.toBlocks₁₁).trace = w

/-- **Discharge.** Any realization induces the `TauRhoHodgeLift` on its
diagonal blocks (via the #3999 constructor) — with functorial provenance for
`w`, inhabiting `ArchimedeanTauRealization` closes the wall. -/
theorem discharge {g : ℕ} {w : ℂ} (T : ArchimedeanTauRealization g w) :
    TauRhoHodgeLift g T.loopWeight.toBlocks₁₁ T.loopWeight.toBlocks₂₂ :=
  tauRhoHodgeLift_of_real_operator T.loopWeight T.herm T.real

/-- The equal-split consequence, end to end: any realization's conjugate
block carries the same weight — the ½ of `½·a₀` for the realized operator. -/
theorem discharge_equal_split {g : ℕ} {w : ℂ} (T : ArchimedeanTauRealization g w) :
    (T.loopWeight.toBlocks₂₂).trace = w := by
  have h := (discharge T).conjugated
  rw [h, trace_map_star_eq_of_isHermitian (hermitian_block_of_isHermitian _ T.herm),
    T.channelTrace]

/-- **The interface alone is trivially inhabitable** — machine-checking why
the wall is EXCLUSIVELY the functorial provenance: for any REAL prescribed
weight, a bare diagonal matrix satisfies every interface field. (Labeled
non-sufficiency demonstration; NOT progress on the wall.) -/
theorem interface_alone_is_trivially_inhabitable (g : ℕ) (s : ℝ) :
    Nonempty (ArchimedeanTauRealization g ((g : ℂ) * (s : ℝ))) := by
  refine ⟨⟨Matrix.diagonal (fun _ => ((s : ℝ) : ℂ)), ?_, ?_, ?_⟩⟩
  · ext i j
    rcases i with i | i <;> rcases j with j | j <;>
      simp [swapP, Matrix.fromBlocks, Matrix.mul_apply, Matrix.diagonal,
        Fintype.sum_sum_type, Matrix.one_apply, apply_ite (starRingEnd ℂ),
        Matrix.map_apply, eq_comm]
  · exact Matrix.isHermitian_diagonal_of_self_adjoint _
      (by funext x; exact Complex.conj_ofReal _)
  · simp [Matrix.toBlocks₁₁, Matrix.trace, Matrix.diag, Matrix.diagonal,
      Finset.sum_const, nsmul_eq_mul]

end QOU.Archimedean.TauFunctorTargetSpec
