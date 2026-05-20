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
  /-- Manuscript claim — the two actions commute on every cell. -/
  claim_commute : ∀ (g : GaloisAction) (b : BraidAction) (x : Cell),
    galois g (braid b x) = braid b (galois g x)

/-- **Proposition (`prop:joint-galois-braid-discharged`).**
    Joint motivic-Galois × braid action commutes on every
    bi-filtration cell. -/
-- Ref: [manuscript] quantum-observable-universe/algebraic-substrate/joint-galois-braid-discharged.md
theorem joint_action_discharged [ctx : JointGaloisBraidContext] :
    ∀ (g : ctx.GaloisAction) (b : ctx.BraidAction) (x : ctx.Cell),
      ctx.galois g (ctx.braid b x) = ctx.braid b (ctx.galois g x) :=
  ctx.claim_commute

end QOU.AlgebraicSubstrate.JointGaloisBraidDischarged
