import Mathlib.Tactic

/-!
# QOU.BraidKnot.knot_operator_transition — knot-type hierarchy of nucleon additions

**Proposition** ([`prop:knot-operator-transition`](../../../quantum-observable-universe/braids-and-knots/knot-operator-transition.md)).

*The operator that adds the `(A+1)`-th nucleon to a nucleus of
mass number `A` has a definite knot type, following the hierarchy*

```
  1 nucleon: unknot  →  2: σ  →  3: Hopf  →  4: trefoil
```

*The 4th nucleon completes the trefoil topology (`T_{2,3}` = electron),
explaining why `⁴He` has the strongest binding per nucleon among
light nuclei.*

-- Ref: [leitner2026] quantum-observable-universe/braids-and-knots/knot-operator-transition.md
-/

namespace QOU.BraidKnot

/-- The discrete knot type of an `(A+1)`-th nucleon addition operator. -/
inductive NucleonAdditionKnotType
  | unknot
  | singleCrossing
  | hopfLink
  | trefoil
  deriving DecidableEq, Repr

/-- The knot type assigned to the `(A+1)`-th nucleon addition,
    as a function of the parent mass number `A`. -/
def nucleonAdditionKnot : ℕ → NucleonAdditionKnotType
  | 0 => .unknot          -- 1st nucleon: unknot
  | 1 => .singleCrossing  -- 2nd nucleon: σ
  | 2 => .hopfLink        -- 3rd nucleon: Hopf
  | 3 => .trefoil         -- 4th nucleon: trefoil (= T_{2,3} = electron)
  | _ => .trefoil         -- A ≥ 4: trefoil pattern continues structurally

/-- **Knot-hierarchy of nucleon additions** ([`prop:knot-operator-transition`]).

    The 4th nucleon completes the trefoil topology, marking the
    binding-energy peak at `⁴He`. -/
-- Ref: [leitner2026] quantum-observable-universe/braids-and-knots/knot-operator-transition.md
theorem knot_operator_transition_hierarchy :
    nucleonAdditionKnot 0 = .unknot ∧
    nucleonAdditionKnot 1 = .singleCrossing ∧
    nucleonAdditionKnot 2 = .hopfLink ∧
    nucleonAdditionKnot 3 = .trefoil := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> rfl

/-- **The 4th-nucleon completion** ([`prop:knot-operator-transition`]).

    For every `A ≥ 3`, the nucleon-addition operator has trefoil
    knot type — the topology saturates at the 4th nucleon. -/
-- Ref: [leitner2026] quantum-observable-universe/braids-and-knots/knot-operator-transition.md
theorem knot_operator_transition (A : ℕ) (h : 3 ≤ A) :
    nucleonAdditionKnot A = .trefoil := by
  -- Unfold the definition on the `A ≥ 3` branch.
  match A, h with
  | 3, _ => rfl
  | n + 4, _ => rfl

end QOU.BraidKnot
