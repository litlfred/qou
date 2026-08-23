---
# qou-w61k
title: prop:volume-from-rigidity refs the WEAKER of two formalisations
status: todo
type: task
priority: normal
created_at: 2026-08-23T10:38:07Z
updated_at: 2026-08-23T10:40:20Z
---

## The ref points at the weaker of two formalisations

`content/quantum-observable-universe/quantum-observable-universes/volume-from-rigidity.ts`
has `lean.ref = "qou:QOU.volume_from_rigidity"`. That declaration exists, in
`QOU/volume_from_rigidity.lean` — but resolution takes the sibling
`volume-from-rigidity.lean` first, and the sibling declares
`VolumeFormFactorisation` + `volume_form_is_nondegen`, not
`volume_from_rigidity`. So this is the same mis-aimed-ref shape as the three
fixed in PR #5533.

**It must NOT be fixed the same way.** For those three the library held the
better formalisation. Here it holds the worse one:

- **Library** `SymplecticSelfDualContext` is a `Type`-level cartoon —
  `V : Type`, `Vdual : Type`, `rank : Type → ℕ`, and a **free** `simple : Prop`
  field — with `claim_rank_eq_two : simple → rank V = 2`. The antecedent is an
  uninterpreted `Prop`, so the conditional constrains nothing.
- **Sibling** `VolumeFormFactorisation` lives in a genuine
  `[Category C] [MonoidalCategory C]`, with real morphisms and the actual
  factorisation equation `(V ◁ phi) ≫ eval = proj ≫ epsilon`, plus
  `epsilon_epi : Epi epsilon`.

Deleting the sibling and letting the ref resolve to the library would
**downgrade** the block from a monoidal-category statement to a `Type`-level
one. That is why PR #5533 left it alone.

## The sibling is not clean either

`volume_form_is_nondegen (vff) : Epi vff.epsilon := vff.epsilon_epi` is a pure
field projection, which is why it sits in the vacuity ledger. Non-degeneracy is
independent of the factorisation, so `epsilon_epi` is a legitimate hypothesis
field and there is nothing to derive it from — the projection adds only a name.

## What would close it

Move the sibling's monoidal-category content into the library under the name
`volume_from_rigidity` (or retarget the ref to the sibling's own declaration),
drop the bare projection, and reconcile the two `simple`/`Epi` framings so the
block has one formalisation rather than two disagreeing ones.
