---
# qou-fngs
title: 'Vacuous: instance canonical makes GBFiltrationCollapsesAtE2 free for every R'
status: in-progress
type: bug
priority: high
created_at: 2026-08-24T14:13:08Z
updated_at: 2026-08-24T14:13:08Z
---

`QOU/Mathlib/SpectralSequence.lean:125`:

```lean
instance canonical (R : Type u) : GBFiltrationCollapsesAtE2 R where
  ss := trivial R          -- every cell PUnit, every differential zero
  collapses := trivial_collapses_at_E2 R
```

The file says it outright: *"the trivial spectral sequence **vacuously**
discharges the §3b-cond hypothesis."* Because it is an `instance`, typeclass
resolution supplies it for **every** `R` — so any downstream theorem taking
`[GBFiltrationCollapsesAtE2 R]` is unconditional, and the substrate axiom
`S-GB-spectral-collapse` asserts nothing.

Same self-assuming shape `main` removed twice this week:
`hasDqSquaredNonvanishing_of_fact` and
`hasCategoricalIrreducibility_of_subsingleton`, both deleted for producing a
class from a trivial witness of its own conclusion.

Four more instances have the same shape: `trivial_converges`,
`gb_trivial_converges`, `wedderburnSS_n2_converges`,
`gb_wedderburn_generic_converges`.

## Blast radius is small — fix it before anything is built on it

Only `UpstreamSubstrateBridge.lean` and `Summary.lean` reference the classes,
and both are *about* the API rather than doing mathematics with it. Nothing
substantive consumes the hypothesis yet, which is exactly why now is the time.

## The fix, in the corpus's own idiom

`TauFunctorTargetSpec.interface_alone_is_trivially_inhabitable` is the
precedent: keep the trivial model, **demote it from `instance` to `def`**, and
state its triviality as a named theorem so a reader sees how little it costs to
inhabit. Then `[GBFiltrationCollapsesAtE2 R]` becomes a real hypothesis that a
genuine GB filtration must discharge.

## Fixed 2026-08-24

Seven `instance` declarations demoted to `def` in
`QOU/Mathlib/SpectralSequence.lean` — `canonical` (renamed
`canonicalTrivial`), `trivial_converges`, `gb_trivial_converges`,
`wedderburnSS_n2_converges`, `gb_wedderburn_n2_converges`,
`wedderburnSS_generic_converges`, `gb_wedderburn_generic_converges`. The file
now declares **no instances at all**, so `[GBFiltrationCollapsesAtE2 R]` is a
real hypothesis again.

### `collapse_is_definitional`

Added in the idiom of `TauFunctorTargetSpec.interface_alone_is_trivially_inhabitable`:
every spectral sequence constructed in this file has `differential _ _ := default`,
so `CollapsesAt` holds by `rfl` at every page. Collapse is **built into the
models, not proved of anything** — including `wedderburnSS_n2`, whose cells are
genuinely `Fin 2 → R` at the origin but whose differentials are still constant.

### The rename that mattered most

`UpstreamSubstrateBridge.gb_spectral_collapse_at_E2_discharged` →
`exists_collapsing_spectralSequence`. The old name read as though the substrate
axiom `S-GB-spectral-collapse` had been discharged. The statement is
`∃ S, CollapsesAtE2 S` — it never mentions the Gröbner filtration, and the
witness performs no computation. Four call sites updated; no block `lean.ref`
pointed at it.

`Summary.inventory_check` used `inferInstance` for the spectral-sequence
conjunct; it now names `canonicalTrivial R` explicitly, so a reader sees the
witness is `PUnit`.

    SpectralSequence.lean         exit 0
    UpstreamSubstrateBridge.lean  exit 0

## Found alongside, NOT caused here: `QOU.Mathlib.Summary` is red on `main`

`inventory_check` asserts `Nonempty (IwahoriHeckeAlgebra R 2 q)` and
`Nonempty (WedderburnIsomorphism R 2 q)` via `inferInstance`, and
**`IwahoriHeckeAlgebra` has no instance anywhere in the corpus** — so the
theorem cannot have compiled. Verified red at `origin/main`, independent of
this change (`lean-direct-cone.sh QOU.Mathlib.Summary` → exit 1 both before and
after my edits).

It went unnoticed because `Summary.lean` is one of the **871 of 2085 modules
not reachable from `QOU.lean`** — the root target never builds it. That is
exactly the "green by omission" hazard `prepare-merge` §4 warns about: a module
you touched can be green because nothing compiles it.

Not fixed here: the honest repair is either a real `IwahoriHeckeAlgebra`
instance or dropping an inventory line that claims one exists, and both are
owner calls about what the upstream bundle is asserting.
