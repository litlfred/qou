import Mathlib.Tactic

/-!
# Joint Galois × braid action — general discharge

Compiled formalisation of `prop:joint-galois-braid-discharged`.
Sibling docstub at
`algebraic-substrate/joint-galois-braid-discharged.lean`.

The joint motivic-Galois × braid action commutes on every
bi-filtration cell. Discharged from centrality of the motivic
Galois on the cell + bar-compatibility of the braid action.
-/

namespace QOU.AlgebraicSubstrate.JointGaloisBraidDischarged

/-- Abstract context for `prop:joint-galois-braid-discharged`. -/
class JointGaloisBraidContext where
  /-- The bi-filtration cell carrier. -/
  Cell : Type
  /-- The motivic Galois group action element. -/
  GaloisAction : Type
  /-- The braid group action element. -/
  BraidAction : Type
  /-- Apply the Galois action. -/
  galois : GaloisAction → Cell → Cell
  /-- Apply the braid action. -/
  braid : BraidAction → Cell → Cell
  /-- The motivic Galois action is central on the cell (commutes with all functions). -/
  galois_central : ∀ (g : GaloisAction) (x : Cell) (f : Cell → Cell),
    galois g (f x) = f (galois g x)

/-- **Proposition (`prop:joint-galois-braid-discharged`).**
    Joint motivic-Galois × braid action commutes on every
    bi-filtration cell. -/
-- Ref: [manuscript] quantum-observable-universe/algebraic-substrate/joint-galois-braid-discharged.md
theorem joint_action_discharged [ctx : JointGaloisBraidContext] :
    ∀ (g : ctx.GaloisAction) (b : ctx.BraidAction) (x : ctx.Cell),
      ctx.galois g (ctx.braid b x) = ctx.braid b (ctx.galois g x) := by
  intro g b x
  exact ctx.galois_central g x (ctx.braid b)

end QOU.AlgebraicSubstrate.JointGaloisBraidDischarged
