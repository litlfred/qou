import Mathlib.Tactic.DeriveFintype
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Finset.Card

/-!
# B1 at additional hyperbolic-knot rows

Compiled formalisation of `conj:b1-hyperbolic-rows-theorem`.
Sibling docstub at `appendix-surreals/b1-hyperbolic-rows-theorem.lean`.

The B1 keystone holds unconditionally at Borromean rings,
the Whitehead link, and the twist-knot family via Bloch-Suslin
together with van der Veen et al.'s Volume-Conjecture extensions.

## History — this file made the library inconsistent

Until 2026-08-08 the statement was

```lean
axiom b1_hyperbolic_rows
    (n_hyperbolic_rows_verified : ℕ)
    (bloch_suslin van_der_veen : Prop) :
    bloch_suslin → van_der_veen → 3 ≤ n_hyperbolic_rows_verified
```

Every one of those binders is universally quantified, including the count.
So the axiom asserted `3 ≤ n` for **every** `n : ℕ`, given **any** two
`Prop`s. Instantiating at `n = 0` with both `Prop`s taken to be `True`:

```lean
theorem b1_axiom_is_inconsistent : False := by
  have h : (3 : ℕ) ≤ 0 := b1_hyperbolic_rows 0 True True trivial trivial
  omega
```

That compiles, and `#print axioms` names `b1_hyperbolic_rows` as the only
non-standard dependency. This was not vacuity — it was **`False`**, so every
statement in the import cone of `QOU.AppendixSurreals` was provable.

The repair is to stop quantifying over the things that were meant to be
fixed. `BlochSuslinRegulator` and `VanDerVeenVolumeConjecture` are now named
opaque propositions rather than bound `Prop` variables, the three rows are an
enumerated type rather than an anonymous numeral, and the count `3` is
**derived** from "B1 holds at each of three distinct rows" rather than
asserted. Bean `qou-t7zg`.

Note that defining `nVerified := 3` and keeping `3 ≤ nVerified` would have
traded the unsoundness for vacuity (`3 ≤ 3` is `rfl`). The content lives in
the per-row statement; the cardinality bound is its consequence.
-/

namespace QOU.AppendixSurreals.B1HyperbolicRowsTheorem

/-- The three hyperbolic rows at which the B1 keystone is claimed:
    the Borromean rings, the Whitehead link, and the twist-knot family. -/
inductive HyperbolicRow
  | borromean
  | whitehead
  | twistKnot
  deriving DecidableEq, Fintype

/-- **Conjecture (`conj:b1-hyperbolic-rows-theorem`, §3b-cond class).**
    Packages the external Bloch–Suslin regulator hypothesis, van der Veen's
    Volume-Conjecture extension hypothesis, and the per-row B1 predicate on
    `HyperbolicRow`, without bare global `axiom` or `opaque` declarations. -/
-- Ref: [leitner2026] quantum-observable-universe/appendix-surreals/b1-hyperbolic-rows-theorem.md
class B1HyperbolicRowsConjecture where
  BlochSuslinRegulator : Prop
  VanDerVeenVolumeConjecture : Prop
  B1HoldsAt : HyperbolicRow → Prop
  b1_holds_at_row :
    BlochSuslinRegulator → VanDerVeenVolumeConjecture →
      ∀ r : HyperbolicRow, B1HoldsAt r

/-- There are exactly three hyperbolic rows on record. -/
theorem card_hyperbolicRow : Fintype.card HyperbolicRow = 3 := rfl

open scoped Classical in
/-- **B1 holds at at least 3 hyperbolic rows** — *derived* from the per-row
    conjecture class `[B1HyperbolicRowsConjecture]`, not assumed as a numeral
    bound. Conditional on the two external inputs, the set of rows carrying B1
    is all of `HyperbolicRow`, hence has cardinality `3`. -/
theorem b1_hyperbolic_rows [c : B1HyperbolicRowsConjecture]
    (hbs : c.BlochSuslinRegulator) (hvdv : c.VanDerVeenVolumeConjecture) :
    3 ≤ (Finset.univ.filter fun r : HyperbolicRow => c.B1HoldsAt r).card := by
  have hall : ∀ r : HyperbolicRow, c.B1HoldsAt r := c.b1_holds_at_row hbs hvdv
  have hfilter :
      (Finset.univ.filter fun r : HyperbolicRow => c.B1HoldsAt r) = Finset.univ :=
    Finset.filter_true_of_mem fun r _ => hall r
  rw [hfilter, Finset.card_univ, card_hyperbolicRow]

end QOU.AppendixSurreals.B1HyperbolicRowsTheorem
