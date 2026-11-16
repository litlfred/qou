---
# qou-w61k
title: prop:volume-from-rigidity refs the WEAKER of two formalisations
status: in-progress
pr: 8206
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-23T10:38:07Z
updated_at: 2026-11-16T21:22:30Z
parent: b9cj
---

## The ref points at the weaker of two formalisations

`folio/quantum-observable-universe/quantum-observable-universes/volume-from-rigidity.ts`
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

## Round 51 Progress (PR #8206)

- [x] Unified `QOU/volume_from_rigidity.lean` and `quantum-observable-universes/volume-from-rigidity.lean`: added `VolumeFormFactorisation` + `volume_form_is_nondegen`, defined `exteriorSquareDim d = d * (d - 1) / 2` and proved `exteriorSquareDim_eq_one_iff : exteriorSquareDim d = 1 ↔ d = 2`, replaced self-assuming `claim_rank_eq_two` with `exterior_rank_eq_one` + `neg_involutive`, derived `volume_from_rigidity` and `symplectic_neg_phiDual_eq_phi`, and constructed `canonicalSymplecticSelfDualContext` on `ℤ × ℤ` (PR #8206, HEAD `aecfe3f528c442bfb5e105f53d801fa139604119`).
- [x] Verified 80-dps `mpmath` witness `round51-devacuify-6qbv.witness.json` (`allPassed: true`, `0` float64 values) and `0` findings across all 6 vacuity audits.
- [ ] Awaiting Merge Manager merge of PR #8206.
