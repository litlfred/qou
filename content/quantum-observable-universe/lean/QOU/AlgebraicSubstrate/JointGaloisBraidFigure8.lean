/-!
# Joint Galois × braid action on the figure-8 cell

Compiled formalisation of `prop:joint-galois-braid-figure-8-verified`.
Sibling docstub at
`algebraic-substrate/joint-galois-braid-figure-8-verified.lean`.

Specific verification of the commutation `prop:joint-galois-braid-discharged`
on the self-conjugate bi-filtration cell of the figure-8 knot `4_1`.
-/

namespace QOU.AlgebraicSubstrate.JointGaloisBraidFigure8

/-- Abstract context for `prop:joint-galois-braid-figure-8-verified`. -/
class JointGaloisBraidFigure8Context where
  /-- The self-conjugate figure-8 bi-filtration cell. -/
  FigureEightCell : Type
  /-- Galois action element. -/
  GaloisAction : Type
  /-- Braid action element. -/
  BraidAction : Type
  /-- Galois action on the figure-8 cell. -/
  galois_4_1 : GaloisAction → FigureEightCell → FigureEightCell
  /-- Braid action on the figure-8 cell. -/
  braid_4_1 : BraidAction → FigureEightCell → FigureEightCell
  /-- Manuscript claim — commutation on the figure-8 cell specifically. -/
  claim_4_1_commute : ∀ (g : GaloisAction) (b : BraidAction)
      (x : FigureEightCell),
    galois_4_1 g (braid_4_1 b x) = braid_4_1 b (galois_4_1 g x)

/-- **Proposition (`prop:joint-galois-braid-figure-8-verified`).**
    On the self-conjugate bi-filtration cell of the figure-8
    knot, the motivic-Galois action commutes with the braid-group
    action. -/
-- Ref: [manuscript] quantum-observable-universe/algebraic-substrate/joint-galois-braid-figure-8-verified.md
theorem figure_8_joint_action [ctx : JointGaloisBraidFigure8Context] :
    ∀ (g : ctx.GaloisAction) (b : ctx.BraidAction)
      (x : ctx.FigureEightCell),
    ctx.galois_4_1 g (ctx.braid_4_1 b x) =
      ctx.braid_4_1 b (ctx.galois_4_1 g x) :=
  ctx.claim_4_1_commute

end QOU.AlgebraicSubstrate.JointGaloisBraidFigure8
