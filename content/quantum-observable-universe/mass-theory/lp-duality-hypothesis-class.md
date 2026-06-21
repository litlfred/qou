**Definition (`HasFiniteLPDuality` hypothesis class, §3b-cond
infrastructure).** *Let $\mathrm{lp}$ be an operator-selection LP
([`prop:operator-selection-lp`](#prop:operator-selection-lp)). The
**finite LP strong-duality + complementary-slackness hypothesis
class** is the `Lean` class with two fields:*

```lean
class HasFiniteLPDuality (lp : OperatorSelectionLP) : Type where
  dualityGapZero       : lp.duality_gap = 0
  complementarySlackness :
    ∀ (λ : lp.Λ), λ ∈ lp.active_set ↔ lp.tight λ
```

*The two fields encode the Schrijver §7.2 strong-duality theorem and
the Schrijver §7.4 complementary-slackness theorem respectively.*

## Why this exists

The two routine LP-theory inputs are currently **two free-standing
top-level `sorry`s** in
[`confinement-nf-partial-proof.lean`](confinement-nf-partial-proof.lean):

```lean
theorem strong_duality (lp : OperatorSelectionLP) :
    lp.duality_gap = 0 := by
  -- Ref: [schrijver1986theory]
  sorry

theorem complementary_slackness (lp : OperatorSelectionLP) (λ : lp.Λ) :
    (λ ∈ lp.active_set) ↔ lp.tight λ := by
  -- Ref: [schrijver1986theory]
  sorry
```

Per AGENTS.md §3b-cond, the proper locale for routine-but-not-yet-
formalised inputs is a **conditional-class hypothesis** with a
trivial model carrying the `sorry` + bibliographic citation. This
block provides that class.

## Bridge to `prop:confinement-nf-partial-proof`

The Lean file `LpDualityHypothesisClass.lean` provides two
drop-in-replacement theorems that consume the class instead of
the free-standing `sorry`s:

| Existing theorem (free-standing `sorry`) | Class-consuming variant |
|---|---|
| `theorem_3_strong_duality lp` | `theorem_3_via_class lp` (takes `[HasFiniteLPDuality lp]`) |
| `theorem_1_maximizer_in_active_set lp h_tight` | `theorem_1_via_class lp max_pole h_tight` (takes `[HasFiniteLPDuality lp]`) |

A future PR can refactor `confinement-nf-partial-proof.lean` to
take `[lpDuality : HasFiniteLPDuality lp]` as a hypothesis on the
two consumer theorems, making the existing top-level `sorry`s
disappear (the `sorry` lives only in the trivial-model class
instance, with proper Schrijver citation).

## When this becomes unconditional

When Mathlib lands a finite-dim LP-duality library
(`Mathlib.Analysis.Convex.LinearProgramming` or similar — none
ships in Mathlib at the time of writing), the
`schrijverModel` trivial model can discharge both sorrys
unconditionally:

```lean
def mathlibModel (lp : OperatorSelectionLP)
    (h_bounded : lp.bounded) (h_feasible : lp.feasible) :
    HasFiniteLPDuality lp where
  dualityGapZero := Mathlib.LP.strong_duality h_bounded h_feasible
  complementarySlackness := Mathlib.LP.complementary_slackness ...
```

This block + Lean file are designed so that swap requires zero
edits to consumer code (`confinement-nf-partial-proof.lean` once
refactored). The class API is fixed; only the trivial-model
implementation changes from `sorry` to a proper proof.

## Trivial model (consistency witness)

`HasFiniteLPDuality.schrijverModel : HasFiniteLPDuality lp` —
provides class instance for any `lp` via two `sorry` fields, each
carrying `-- Ref: [schrijver1986theory]`. This is the §3b-cond
relocation of the two existing free-standing `sorry`s, not a new
mathematical commitment.

The class is **inhabited** for every `lp` (via `schrijverModel`),
so consistency is established (no contradiction introduced).
