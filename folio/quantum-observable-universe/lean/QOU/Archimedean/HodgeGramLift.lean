/-
# Hodge-side instantiation of `TauRhoHodgeLift` — a NON-CLOSING wall-tightening lemma

Bean `qou-la8r` (Hodge side of the α_EM per-loop measure wall). This file shows
the B2 conjecture class `TauRhoHodgeLift` **IS instantiable by the Hodge Gram
matrix**: a real symmetric positive-semidefinite Gram `Bᵀ·B`, complexified,
satisfies BOTH class fields —

* `hermitian` — a real symmetric matrix, viewed in `ℂ`, is Hermitian;
* `conjugated` (with `Wbar = W`) — a real matrix is fixed by entrywise complex
  conjugation (**Hodge reality**: the `(1,1)` real form is `ρ`-real, so its
  weight coincides with its conjugate).

**THIS DOES NOT CLOSE THE WALL (STRICT, §"Axiomatization is NOT a Proof").**
Instantiating `TauRhoHodgeLift` by *a* Hodge Gram is a real reduction, but it
does **not** discharge the one genuine remaining identification:

> **OPEN — "loop weight = Hodge Gram":** that the *categorical* α_EM loop weight
> `W` on `H^{1,0}(Bring)` actually **equals** a Hodge Gram `Bᵀ·B` (equivalently:
> is the Gram of the Hodge inner product on the loop's mode space). Only then
> does the loop weight land inside the family this file instantiates.

So the wall is **tightened**, not removed: from "construct the τ-functor and
prove it carries ρ to Hodge conjugation" down to the single identification
"loop weight = Hodge Gram." The categorical τ-functor is still NOT constructed
and NOTHING is wired to production.

Base ring (§7c): the Gram is built over generic `ℝ` (an archimedean object — a
positive form — so `ℝ`/`ℂ` are appropriate here, past the wall). The
complexification `M ↦ M.map ofReal` is the `H^{1,0} ⊕ H^{0,1}` embedding.

-- Ref: [braden-disney-hogg-2022] https://arxiv.org/abs/2208.13692
-- Ref: [voisin2002] https://doi.org/10.1017/CBO9780511615344
-/
import QOU.Archimedean.TauRhoHodgeLiftInterface
import Mathlib.LinearAlgebra.Matrix.Symmetric

namespace QOU.Archimedean.HodgeGramLift

open Matrix
open QOU.Archimedean.TauRhoHodgeLiftInterface

/-- **Complexification** of a real matrix: entrywise `Complex.ofReal`. Models the
`H^{1,0} ⊕ H^{0,1}` embedding of a real Hodge datum into the complexified
cohomology. -/
noncomputable def complexify {g : ℕ} (M : Matrix (Fin g) (Fin g) ℝ) :
    Matrix (Fin g) (Fin g) ℂ :=
  M.map Complex.ofReal

/-- A real **symmetric** matrix, complexified, is Hermitian — the `hermitian`
field of `TauRhoHodgeLift`. -/
theorem complexify_isHermitian {g : ℕ} {M : Matrix (Fin g) (Fin g) ℝ}
    (hM : M.IsSymm) : (complexify M).IsHermitian := by
  ext i j
  simp only [complexify, Matrix.conjTranspose_apply, Matrix.map_apply, RCLike.star_def,
    Complex.conj_ofReal]
  exact congrArg _ (congrFun (congrFun hM i) j)

/-- **Hodge reality.** A real matrix (complexified) is fixed by entrywise complex
conjugation `ρ = starRingEnd ℂ`. This is the `conjugated` field with `Wbar = W`:
the `H^{0,1}` weight equals the (conjugate of the) `H^{1,0}` weight because the
underlying form is real. -/
theorem complexify_map_conj {g : ℕ} (M : Matrix (Fin g) (Fin g) ℝ) :
    (complexify M).map (starRingEnd ℂ) = complexify M := by
  ext i j
  simp [complexify, Matrix.map_apply, Complex.conj_ofReal]

/-- **NON-CLOSING Hodge-side instance.** Given ANY real symmetric matrix `M` (a
Hodge datum on `H^{1,0}`), its complexification instantiates `TauRhoHodgeLift`
with `W = Wbar = complexify M`. Reduces the wall to "loop weight = this `M`" — it
does NOT construct τ and does NOT prove the loop weight is of this form. -/
noncomputable def hodgeSymmLift {g : ℕ} {M : Matrix (Fin g) (Fin g) ℝ}
    (hM : M.IsSymm) : TauRhoHodgeLift g (complexify M) (complexify M) where
  hermitian := complexify_isHermitian hM
  conjugated := (complexify_map_conj M).symm

/-- A real **Gram** matrix `Bᵀ·B` is symmetric (`(Bᵀ·B)ᵀ = Bᵀ·B`). -/
theorem gram_isSymm {g : ℕ} (B : Matrix (Fin g) (Fin g) ℝ) : (Bᵀ * B).IsSymm := by
  show (Bᵀ * B)ᵀ = Bᵀ * B
  rw [Matrix.transpose_mul, Matrix.transpose_transpose]

/-- **The Hodge Gram instantiates `TauRhoHodgeLift`.** For any real `B` (the loop's
mode data), the Hodge Gram `Bᵀ·B` — real symmetric, positive-semidefinite — gives
an instance of the B2 lift class. This is the wall-tightening: the class is
inhabited *by a Hodge Gram*. The remaining open identification is that the actual
α_EM loop weight equals such a Gram — NOT proved here. -/
noncomputable def hodgeGramLift {g : ℕ} (B : Matrix (Fin g) (Fin g) ℝ) :
    TauRhoHodgeLift g (complexify (Bᵀ * B)) (complexify (Bᵀ * B)) :=
  hodgeSymmLift (gram_isSymm B)

/-- **The single remaining identification, as a named `Prop` (OPEN).** The wall is
now exactly this: the categorical loop weight `W` on `H^{1,0}` equals the
complexified Hodge Gram `Bᵀ·B` for some real mode data `B`. This file proves that
*whenever* this holds, `TauRhoHodgeLift` is instantiated (via `hodgeGramLift`); it
does NOT prove the identification itself. No instance/witness for the actual α_EM
weight is provided — that is the open categorical input. -/
def LoopWeightIsHodgeGram {g : ℕ} (W : Matrix (Fin g) (Fin g) ℂ) : Prop :=
  ∃ B : Matrix (Fin g) (Fin g) ℝ, W = complexify (Bᵀ * B)

/-- **Wall-tightening theorem (conditional, sorry-free).** IF the loop weight is a
Hodge Gram (the single remaining open identification `LoopWeightIsHodgeGram`),
THEN `TauRhoHodgeLift` holds for it (with `Wbar = W`). The hypothesis is exactly
the open gap; the conclusion is the B2 lift. This is a genuine reduction — it does
not discharge the hypothesis. -/
theorem tauRhoHodgeLift_of_loopWeightIsHodgeGram {g : ℕ}
    {W : Matrix (Fin g) (Fin g) ℂ} (h : LoopWeightIsHodgeGram W) :
    Nonempty (TauRhoHodgeLift g W W) := by
  obtain ⟨B, hB⟩ := h
  subst hB
  exact ⟨hodgeGramLift B⟩

end QOU.Archimedean.HodgeGramLift
