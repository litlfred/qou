/-
# Markov-side discharge of the α_EM B2 "real symmetric" premise

`LoopWeightRealSymmReduction` weakened the B2 per-loop wall to
`LoopWeightIsRealSymm W := ∃ M, M.IsSymm ∧ W = complexify M` — "the loop weight is
the complexification of a real symmetric matrix." This file discharges the
**real-symmetric property** from the Markov / seminormal side: the categorical
loop weight is (the τ-image of) the Markov-trace / seminormal bilinear form's Gram
matrix, and *any* symmetric ℝ-bilinear form has a symmetric Gram matrix — so the
premise's real-symmetric requirement is met by construction, leaving only the
τ-identification.

Concretely (sorry-free, `lean`-direct exit 0):

* `toMatrix₂_isSymm_of_symm` — the Gram matrix of a **symmetric** ℝ-bilinear form
  (in any basis) is a symmetric matrix.
* `loopWeightIsRealSymm_of_symmForm` / `tauRhoHodgeLift_of_symmForm` — hence its
  complexification satisfies `LoopWeightIsRealSymm`, instantiating the B2 lift.

**The corpus witness of symmetry.** The seminormal / Specht Markov form is exactly
such a symmetric ℝ-bilinear form:
`QOU.BraidKnot.SpechtIrreducible.bilinM_isSymm` (merged) proves
`(bilinM μ).IsSymm`, and the form is real at the real substrate `q₀` (the
Young-orthogonal / seminormal representation matrices are real for real `q`). So
the "real + symmetric" requirement of the B2 premise is discharged on the Markov
side — it is not an obstruction.

**What stays OPEN (STRICT, §"Axiomatization is NOT a Proof").** The sole remaining
categorical input is the **τ-identification**: that the α_EM loop weight `W` on
`H^{1,0}(Bring)` equals `complexify` of *this* Markov Gram (at `q₀`). No such
identification is asserted here, and no `TauRhoHodgeLift` instance is registered
for the actual loop weight. This file establishes only that *whenever* the loop
weight is a real symmetric bilinear form's Gram, the lift follows — with the
symmetry supplied by the merged `bilinM_isSymm`, not fabricated. `1/(8π)` stays a
phase-4 identification; nothing is wired.

-- Ref: [manuscript] prop:em-coupling-bring-zero-mode
-- Ref: [orellana1998] https://doi.org/10.1006/jabr.1998.7437
-/
import QOU.Archimedean.LoopWeightRealSymmReduction
import Mathlib.LinearAlgebra.Matrix.SesquilinearForm

namespace QOU.Archimedean.MarkovGramRealSymm

open Matrix LinearMap
open QOU.Archimedean.HodgeGramLift
open QOU.Archimedean.LoopWeightRealSymmReduction
open QOU.Archimedean.TauRhoHodgeLiftInterface

variable {g : ℕ} {V : Type*} [AddCommGroup V] [Module ℝ V]

/-- **The Gram matrix of a symmetric ℝ-bilinear form is symmetric.** For a basis
`b` and a bilinear form `B` with `B x y = B y x`, the matrix `toMatrix₂ b b B` is
`IsSymm`. (Models: the seminormal / Markov-trace Gram, `bilinM_isSymm`.) -/
theorem toMatrix₂_isSymm_of_symm (b : Module.Basis (Fin g) ℝ V)
    (B : V →ₗ[ℝ] V →ₗ[ℝ] ℝ) (hB : ∀ x y, B x y = B y x) :
    (toMatrix₂ b b B).IsSymm := by
  show (toMatrix₂ b b B)ᵀ = toMatrix₂ b b B
  ext i j
  simp [LinearMap.toMatrix₂_apply, hB (b j) (b i)]

/-- **Markov-side discharge.** The complexified Gram of a real symmetric bilinear
form satisfies the B2 premise `LoopWeightIsRealSymm`. Instantiated by the
seminormal/Markov form (`bilinM_isSymm`), this shows the real-symmetric requirement
is met on the Markov side — the τ-identification of the loop weight with this Gram
is the only remaining input. -/
theorem loopWeightIsRealSymm_of_symmForm (b : Module.Basis (Fin g) ℝ V)
    (B : V →ₗ[ℝ] V →ₗ[ℝ] ℝ) (hB : ∀ x y, B x y = B y x) :
    LoopWeightIsRealSymm (complexify (toMatrix₂ b b B)) :=
  ⟨toMatrix₂ b b B, toMatrix₂_isSymm_of_symm b B hB, rfl⟩

/-- **The B2 lift from a symmetric-form loop weight.** If the loop weight is the
complexified Gram of a real symmetric bilinear form, `TauRhoHodgeLift` holds — the
real-symmetric hypothesis discharged by the form's symmetry. STRICT: `B` here is a
*hypothesis* (the Markov form supplies it); the τ-identification that the α_EM loop
weight *is* this Gram remains the open categorical input, not fabricated. -/
theorem tauRhoHodgeLift_of_symmForm (b : Module.Basis (Fin g) ℝ V)
    (B : V →ₗ[ℝ] V →ₗ[ℝ] ℝ) (hB : ∀ x y, B x y = B y x) :
    Nonempty (TauRhoHodgeLift g (complexify (toMatrix₂ b b B))
      (complexify (toMatrix₂ b b B))) :=
  tauRhoHodgeLift_of_realSymm (loopWeightIsRealSymm_of_symmForm b B hB)

end QOU.Archimedean.MarkovGramRealSymm
