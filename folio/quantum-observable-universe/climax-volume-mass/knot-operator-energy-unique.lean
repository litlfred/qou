import QOU.Basic

/-!
# QOU.BraidKnot.KnotOperatorEnergy.shadowPrice_unique

The shadow price `y_λ(q) ∈ R` is uniquely determined by the partition and the
substrate parameter.

**This file previously carried `axiom KnotOperatorEnergy.shadowPrice_canonical`
and derived uniqueness from it.** That axiom was FALSE: the old plain structure
had `shadowPrice` as a free field, so `⟨[], 0, 0, none⟩` and `⟨[], 0, 1, none⟩`
agreed on `partition` and `q` while differing in `shadowPrice`. Its own
docstring named the repair as pending — *"a structure refactor carrying the
LP-canonicity as a proof field"* — which is now done in
`def:knot-operator-energy`. Uniqueness below is a **theorem** over the
refactored structure and depends on no axioms. Bean `qou-9yt9`.

LaTeX: `\label{prop:knot-operator-energy-unique}`
-/

namespace QOU.BraidKnot

universe u

/-! The structure is inlined from `def:knot-operator-energy` so this standalone
content-block file elaborates on its own; there is no library module for it. -/

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

/-- **Uniqueness of the shadow price** — a theorem, not an axiom.

    Both records pin `shadowPrice` to the same `dualValue partition q`, so they
    agree. Uniqueness is a consequence of `dualValue` being a function; nothing
    assumes it. -/
-- Ref: [schrijver1986theory] Schrijver, "Theory of Linear and Integer Programming," Wiley 1986
-- Ref: [leitner2026] braids-and-knots/knot-operator-energy
theorem KnotOperatorEnergy.shadowPrice_unique {R : Type u} [CommRing R]
    {dualValue : List ℕ → R → R} {partition : List ℕ} {q : R}
    (E₁ E₂ : KnotOperatorEnergy dualValue partition q) :
    E₁.shadowPrice = E₂.shadowPrice := by
  rw [E₁.shadowPrice_eq, E₂.shadowPrice_eq]

end QOU.BraidKnot
