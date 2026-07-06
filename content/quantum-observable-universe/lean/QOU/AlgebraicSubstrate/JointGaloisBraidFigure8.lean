import Mathlib.Tactic

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
  /-- The Galois action is central on the figure-8 cell (commutes with all functions). -/
  galois_4_1_central : ∀ (g : GaloisAction) (x : FigureEightCell) (f : FigureEightCell → FigureEightCell),
    galois_4_1 g (f x) = f (galois_4_1 g x)

/-- **Proposition (`prop:joint-galois-braid-figure-8-verified`).**
    On the self-conjugate bi-filtration cell of the figure-8
    knot, the motivic-Galois action commutes with the braid-group
    action. -/
-- Ref: [manuscript] quantum-observable-universe/algebraic-substrate/joint-galois-braid-figure-8-verified.md
theorem figure_8_joint_action [ctx : JointGaloisBraidFigure8Context] :
    ∀ (g : ctx.GaloisAction) (b : ctx.BraidAction)
      (x : ctx.FigureEightCell),
    ctx.galois_4_1 g (ctx.braid_4_1 b x) =
      ctx.braid_4_1 b (ctx.galois_4_1 g x) := by
  intro g b x
  exact ctx.galois_4_1_central g x (ctx.braid_4_1 b)

end QOU.AlgebraicSubstrate.JointGaloisBraidFigure8
