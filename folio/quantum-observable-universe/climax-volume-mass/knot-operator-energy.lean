import QOU.Basic


/-!
# QOU.BraidKnot.KnotOperatorEnergy — knot operator energy

E(λ, q) := |y_λ(q)| where y_λ(q) = w_λ(q)/d_λ(q) - 1/[k]_q! is the
LP-dual shadow price (prop:mass-coefficient-shadow-price).

LaTeX: `\label{def:knot-operator-energy}`
-/

namespace QOU.BraidKnot

universe u

/-- **Knot operator energy** at substrate parameter `q : R`.

    `dualValue` is the LP-dual value map `(λ, q) ↦ y_λ(q)`, carried as a
    **parameter** — a function of the indexing data — rather than as a free
    field. That is the repair: `shadowPrice` is now pinned to it by
    `shadowPrice_eq` instead of chosen independently of `partition` and `q`.

    Until 2026-09-06 this was a plain structure with `shadowPrice : R` free,
    plus `axiom KnotOperatorEnergy.shadowPrice_canonical` asserting that two
    records agreeing on `partition` and `q` share a `shadowPrice`. **That axiom
    was false** — `⟨[], 0, 0, none⟩` and `⟨[], 0, 1, none⟩` refute it — and its
    own docstring said why: closing it *"requires ... a structure refactor
    carrying the LP-canonicity as a proof field."* Bean `qou-9yt9`.

    The determining map is a FUNCTION, not a relation with a uniqueness field:
    a structure carrying its own conclusion would be the self-assuming
    projection AGENTS.md §3b-cond item 5 forbids. Here uniqueness is a
    consequence of functionality, not an assumption. -/
-- Ref: [schrijver1986theory] Schrijver, "Theory of Linear and Integer Programming," Wiley 1986
-- Ref: [leitner2026] prop:mass-coefficient-shadow-price
structure KnotOperatorEnergy {R : Type u} [CommRing R]
    (dualValue : List ℕ → R → R) (partition : List ℕ) (q : R) where
  /-- Shadow price `y_λ(q) ∈ R` (algebraic, base-ring-independent). -/
  shadowPrice : R
  /-- and it IS the LP-dual value for this partition at this `q`. -/
  shadowPrice_eq : shadowPrice = dualValue partition q
  /-- Energy `|y_λ(q)|` in the absolute-value image, when defined. -/
  energy : Option R := none

end QOU.BraidKnot
