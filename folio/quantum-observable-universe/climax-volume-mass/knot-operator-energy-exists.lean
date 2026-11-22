import QOU.Basic

/-!
# QOU.BraidKnot.KnotOperatorEnergy.exists

Existence of the knot operator energy record at a given partition and `q`.

**Previously this constructed the junk record
`{ partition := [1], q := 0, shadowPrice := 0 }`.** That proved the *type* was
inhabited, not that any partition has a shadow price — the same vacuity that
`prop:confinement-level-exists` carried. Over the refactored structure the
construction is real: given the LP-dual value map, the record is built from it
and `shadowPrice_eq` holds by `rfl`.

Note what this does and does not say. The mathematical content — that the LP
dual exists and is unique (Schrijver §7.4) — now sits explicitly in the
`dualValue` parameter the caller supplies, rather than being smuggled in by a
witness that ignored its own indices. Bean `qou-9yt9`.

LaTeX: `\label{prop:knot-operator-energy-exists}`
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

/-- The record built from the LP-dual value map. -/
-- Ref: [leitner2026] braids-and-knots/knot-operator-energy
def KnotOperatorEnergy.ofDualValue {R : Type u} [CommRing R]
    (dualValue : List ℕ → R → R) (partition : List ℕ) (q : R) :
    KnotOperatorEnergy dualValue partition q :=
  { shadowPrice := dualValue partition q, shadowPrice_eq := rfl }

/-- **Existence of the knot operator energy.** -/
-- Ref: [leitner2026] braids-and-knots/knot-operator-energy
theorem KnotOperatorEnergy.exists {R : Type u} [CommRing R]
    (dualValue : List ℕ → R → R) (partition : List ℕ) (q : R) :
    Nonempty (KnotOperatorEnergy dualValue partition q) :=
  ⟨KnotOperatorEnergy.ofDualValue dualValue partition q⟩

end QOU.BraidKnot
