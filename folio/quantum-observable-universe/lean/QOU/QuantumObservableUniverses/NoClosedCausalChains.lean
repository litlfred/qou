import Mathlib.Logic.Relation
import Mathlib.Order.WellFounded

/-!
# No closed chains under a well-founded precedence relation

Pure order theory, used by `rem:no-goedel-closed-chains`.

Let `r` be any relation on a type `α`, read as "immediately precedes".
A *closed chain* through `p` is a finite `r`-chain from `p` back to `p`,
i.e. `Relation.TransGen r p p`. *Total chronology* means every point
reaches every point (itself included) by a finite chain; this is the
order-theoretic shape of Gödel's rotating universe, where the
chronological future of every event is the whole spacetime.

If `r` is well-founded, then:

* `not_closedChainAt_of_wellFounded`: no point lies on a closed chain;
* `not_totalChronology_of_wellFounded`: on a nonempty type, total
  chronology fails.

Nothing here uses a braiding, a metric or any physical input. The
application to `≺_c` is in the content file
`quantum-observable-universes/braiding-induced-ordering.lean`
(`QOU.degLex_no_closedChain`).
-/

namespace QOU.Chronology

variable {α : Type*}

/-- A closed `r`-chain through `p`: a finite chain `p r … r p`. -/
def ClosedChainAt (r : α → α → Prop) (p : α) : Prop :=
  Relation.TransGen r p p

/-- Total chronology: every point reaches every point by a finite `r`-chain.
This is the order-theoretic content of `I⁺(p) = M` for all `p`. -/
def TotalChronology (r : α → α → Prop) : Prop :=
  ∀ p q : α, Relation.TransGen r p q

/-- A well-founded relation has no closed chains. -/
theorem not_closedChainAt_of_wellFounded {r : α → α → Prop}
    (hwf : WellFounded r) (p : α) : ¬ ClosedChainAt r p := by
  have h' : WellFounded (Relation.TransGen r) := hwf.transGen
  exact h'.induction (C := fun x => ¬ Relation.TransGen r x x) p
    (fun x ih hx => ih x hx hx)

/-- A well-founded relation on a nonempty type is not totally chronological. -/
theorem not_totalChronology_of_wellFounded {r : α → α → Prop} [Nonempty α]
    (hwf : WellFounded r) : ¬ TotalChronology r := fun h =>
  not_closedChainAt_of_wellFounded hwf (Classical.arbitrary α) (h _ _)

end QOU.Chronology
