---
# qou-09mr
title: 'Vacuous: CrystalRMatrixSubLemma.canonical picks poleIndicator to BE the function it is compared against'
status: completed
type: bug
priority: normal
created_at: 2026-08-24T19:37:08Z
updated_at: 2026-08-24T21:04:07Z
---

`QOU/BraidKnot/CrystalRMatrixSubLemma.lean:188`, verified present 2026-08-24.

```
instance canonical (R : Type u) [CommRing R] (q : R) :
    let C := CrystalGraphRealization.canonical R q
    @CrystalRMatrixSubLemma R _ q C := by
  intro C
  exact {
    poleIndicator := fun rho => decide (rho <= -1)
    pole_indicator_correct := fun _ => rfl
  }
```

The class's data field `poleIndicator` is set to the very function the
propositional field compares it against, so `pole_indicator_correct` closes by
`rfl`. Its own docstring says so out loud — *"the indicator IS the witness
function"* — and offers that as reassurance ("this instance introduces no
`sorry`"). No `sorry` is exactly the problem: there is no visible record of what
was not established, and `#print axioms` cannot contradict prose.

## Why this is not the shape qou-fngs / qou-4els already drained

Those were **constant-data** vacuity: `PUnit`, `0`, `True`. This is
**definitional laundering** — the data is a real, non-degenerate function, and it
is still chosen to make the claim reflexive. Same defect, different tell.

`qou-4els` (completed) touched this file only as a *consumer*: it demoted
`CrystalGraphRealization.canonical` and noted that `CrystalRMatrixSubLemma.canonical`
names the demoted term explicitly. It never adjudicated this instance itself.

## Also worth knowing before you pick it up

- It is still an `instance`, so `[CrystalRMatrixSubLemma R q C]` is resolved
  everywhere and any conditional theorem taking it is unconditional.
- The upstream `let C := CrystalGraphRealization.canonical R q` binds it to the
  one-point crystal that `qou-4els` demoted to a `def` — so the instance is
  pinned to the trivial realisation as well.
- **The automated vacuity detector does not see this.**
  `checkNoVacuousInstanceData` requires a degenerate *value* (`0|1|True|PUnit.unit|...`),
  and `fun rho => decide (rho <= -1)` is none of those; the fields are also inside
  a tactic-block `exact { ... }` rather than a `where`. Filed as folio-assistant
  bean **folio-assistant-ilbh**. Do not expect the detector to regress-guard this fix.

## Disposition

Same as `ConfinementGradingCorrespondence.canonical`: demote `instance` -> `def`,
keep it as a named consistency witness, and say in the docstring that the
indicator was *chosen* to satisfy the comparison, so `[CrystalRMatrixSubLemma]`
becomes a hypothesis a real R-matrix has to discharge.


## Resolved 2026-08-24 — parameterised, not just demoted

**Consumers before the change: 11 mentions of `CrystalRMatrixSubLemma` across
`QOU/`, but only 3 real ones** — `poleIndicator_minus_one_eq_true` and
`poleIndicator_plus_one_eq_false` (both in the same file) plus the vacuous
`canonical` itself. `OperatorValuedCombiner.lean`'s two hits are an `import` and
a prose mention of the §3b-cond pattern; `CrystalGraphRealization.lean:115` was
prose. **Nothing outside the file takes `[CrystalRMatrixSubLemma …]` as a
hypothesis.** No `.ts`/`.md` content block resolves to the library decl either:
`mass-theory/crystal-r-matrix-sub-lemma.ts` has
`ref: "qou:QOU.BraidKnot.CrystalRMatrixSubLemma"`, and `export-json` resolves the
**sibling first**, so it lands on `mass-theory/crystal-r-matrix-sub-lemma.lean`.

**What was done** (`QOU/BraidKnot/CrystalRMatrixSubLemma.lean`) — the corpus
remedy from `QOU/Archimedean/JetOrderIndependence.lean`, not the fallback demote:

- New `structure PoleOrderData` carries `poleOrder : ℤ → Bool` as **data**.
- `class CrystalRMatrixSubLemma R q (P : PoleOrderData) : Prop` now takes it as a
  *parameter*, with the single field asserting `P.poleOrder ρ = decide (ρ ≤ -1)`.
  An instance can no longer choose the function it is compared against.
- The residual vacuity is a proved pair rather than a latent trap:
  `combinatorialPoleOrder_subLemma` (satisfiable, at the indicator itself) and
  `not_subLemma_of_poleOrder_ne` / `not_subLemma_alwaysPoleOrder` (fails at the
  constant-`true` assignment, already at `ρ = 0`).
- The two structural lemmas now bind `{P}` and conclude about `P.poleOrder`.

**The sharper finding, recorded in the new docstring.** The consistency witness
is free in `R`, `q` *and* the realisation `C`. A witness that holds for **every**
crystal-graph realisation says nothing about any of them — it is a fact about the
indicator function alone. The old `instance canonical` disguised that by pinning
itself to `CrystalGraphRealization.canonical R q`, which read as though a crystal
had been consulted.

**On "resolved everywhere".** Slightly overstated in the bean above. The old
instance's type zeta-reduced to `@CrystalRMatrixSubLemma R _ q
(CrystalGraphRealization.canonical R q)`, so resolution only fired when the
ambient realisation was syntactically the canonical model. Since that `def` is
the corpus's **only** realisation, every way of instantiating this class's
theorems at a concrete `R`, `q` still got the free witness — the conclusion
stands, the mechanism is narrower.

**Knock-on.** `CrystalGraphRealization.canonical`'s docstring claimed
`CrystalRMatrixSubLemma.canonical` names it explicitly. That was its only named
use, so after this change **nothing in the corpus names the `PUnit` model at
all**; the docstring is corrected to say so.

**Still open, not fixed here (worth its own bean).** The *sibling*
`content/quantum-observable-universe/mass-theory/crystal-r-matrix-sub-lemma.lean`
declares its own copy of the class with the same one-model shape
(`poleIndicator` a field, pinned by `pole_indicator_correct`). It is materially
less bad — its witness is `def trivialModel`, not an `instance`, and its
docstring says what it is — and it is the decl the content block actually
resolves to, so the parameterisation should be mirrored there. Left untouched to
keep this change to the site the bean names.

**Verification.** Fresh `lean` on `CrystalRMatrixSubLemma`,
`CrystalGraphRealization`, `OperatorValuedCombiner` and the other six
`CrystalGraphRealization` importers — all exit 0, no new warnings.
`#print axioms` on all five new/retargeted decls: *no axioms at all*, no
`sorryAx`. No `sorry` in committed work.
