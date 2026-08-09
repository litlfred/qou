---
# qou-ffwk
title: 'GAP: 10 conjecture carriers use a trivially-inhabited ''residual = 0'' placeholder'
status: todo
type: task
priority: normal
created_at: 2026-08-08T15:15:21Z
updated_at: 2026-08-08T15:17:15Z
---


## The defect

Ten conjecture carriers in the QOU library share this field schema:

```lean
class C where
  residual : ℝ
  residual_eq_zero : residual = 0
```

This is **inhabited by `⟨0, rfl⟩`**. The class asserts nothing, so a
downstream `theorem foo [C] : P` proves `P` outright, not `C → P`.
This is the AGENTS.md §3b-tax "the carrier must assert something" rule
(`proof-claims-unencoded`), one step weaker than the empty-marker
`class C : Prop` case: the fields exist, but their conjunction is
satisfiable by a constant, so they carry no content.

Each of these files also carries a docstring naming a *real* claim
(e.g. `VacuumEpsilon`: "Geom(unknot) = 0"), which the schema does not
encode — the `proof-claims-unencoded` shape exactly.

## Why this matters for the de-laundering work

The axiom-and-global-instance de-laundering (PRs #4743, #4750, and the
`TorusKnotMass` / `VacuumEpsilon` / `TwoFiltrationBridge` batch) is
**necessary but not sufficient** for these ten. Removing
`axiom c : C` + `instance : C := c` restores the *no-instance* open
state, but anyone — including a future agent trying to make a red file
green — can re-close it in one line with `instance : C := ⟨0, rfl⟩`,
with no axiom and no `sorry` to show up in `#print axioms`.

**So: de-laundering these classes does not yet make the downstream
`[C]`-conditional theorems meaningful.** Do not report them as
"conditional results" until the fields are refined.

## Inventory (all confirmed by grep on `residual_eq_zero`)

| File | class | instances remaining |
|---|---|---|
| `AppendixSurreals/VacuumEpsilon.lean` | `VacuumEpsilon` | 0 (de-laundered) |
| `AppendixSurreals/LocalInfinitesimalField.lean` | `LocalInfinitesimalField` | 0 (de-laundered) |
| `AppendixSurreals/SpectralNormalForm.lean` | `SpectralNormalForm` | 0 (de-laundered) |
| `AppendixSurreals/QouInfraDischargesGoncharovZeta5.lean` | `QouInfraDischargesGoncharovZeta5` | 0 (de-laundered) |
| `AppendixSurreals/DiophantineBirthday.lean` | `DiophantineBirthday` | 0 (de-laundered) |
| `BraidKnot/BringFigureEightDepth2Witness.lean` | `BringFigureEightDepth2Witness` | 0 (de-laundered) |
| `BraidKnot/BraidGroupNStrand.lean` | `HeckeQuotient` | 0 |
| `Archimedean/HyperbolicVolumeIndependence.lean` | (anon) | **2** |
| `BraidKnot/HabiroResidueSumEquivalence/archimedean_agreement.lean` | `archimedean_agreement` | **1** |
| `BraidKnot/HabiroResidueSumEquivalence/protonExample/archimedean_agreement.lean` | `archimedean_agreement` | **1** |

The four with instances remaining are on bean `qou-up56` (consumers do
not declare `[C]`, so removing the instance breaks them).

## The fix, per file

Refine the fields to the claim the docstring already states. Worked
target for `VacuumEpsilon`:

```lean
class VacuumEpsilon where
  geom : Link → ℝ
  geom_unknot : geom unknot = 0
```

This is not mechanical — each file needs the right carrier type for its
claim, and some of those types (`Link`, the Hoefsmit pipeline's
`Geom`) may not exist in the library yet. Expect this to surface
further gaps rather than close cleanly. **Do not batch-process.**

## Detection

`grep -rl "residual_eq_zero" QOU --include=*.lean` catches this exact
shape. A general detector for "class whose fields are jointly
satisfiable by a constant" belongs in
`scripts/lean-definition-collapsed-audit.py` alongside the existing
signal-A/signal-B logic — currently it only flags collapsed *proofs*,
not collapsed *carriers*.

## FINDING (2026-08-08) — field refinement is NOT sufficient; the blocker is one level down

I set out to do the fix this bean describes — refine `VacuumEpsilon`'s
`residual = 0` schema to the claim its docstring states — and stopped, because
the premise is wrong. Recording why, since the next agent will otherwise spend
the same time discovering it.

### 1. The docstring states the wrong claim

The class docstring says the content is *"vacuum normalisation requires
`Geom(unknot) = 0`"*. Reading the source block
[`conj:vacuum-epsilon`](content/quantum-observable-universe/appendix-surreals/vacuum-epsilon.md),
that is the **strict** vacuum being *relaxed*, not the conjecture. The
conjecture is the opposite:

> `Geom(🝆) = ε ∈ **No**` — a *positive infinitesimal*, with `st(ε) = 0`.

Encoding the docstring literally would have formalised the negation of the
conjecture. Read the `.md`, not the Lean docstring.

### 2. A second carrier for the same conjecture already exists

`QOU/AppendixSurreals/Conjectures.lean:394` declares `class VacuumEpsilon'`,
"factored out of the original `VacuumEpsilon`", with a narrowing audit and an
`st`-image theorem. So the conjecture has **two** carriers: the legacy
placeholder (de-laundered in #4750) and this one. Consolidating them is its
own task; refining the legacy one in isolation would deepen the split.

### 3. And `VacuumEpsilon'` is *also* trivially inhabited

```lean
instance (K : Type) [SurrealField K] : VacuumEpsilon' K where
  exists_epsilon_vacuum := ⟨epsilonSurreal K, rfl⟩
```

compiles. Its only field is `∃ SQ, QOU_VacuumEnergy SQ = epsilonSurreal K`,
and `QOU_VacuumEnergy Q := Q` is the **identity** — its own docstring says
*"placeholder semantics … Makes `VacuumEpsilon` formally provable (witness:
`Q := ε`)"*. So `ε` witnesses it by `rfl`.

### The actual blocker

**The semantic functions these classes would be refined *against* are
themselves identity or absent placeholders**, so any field written over them
is satisfiable by construction:

| placeholder | status |
|---|---|
| `QOU_VacuumEnergy Q := Q` | identity |
| `QOU_ObservabilityNorm Q := Q` | identity |
| `Knot := ℕ` | index carrier, "sufficient to make `Nonempty Knot` provable" |
| `Geom : Link → ℝ` | does not exist anywhere in the corpus |

So this bean's fix is **necessary but not sufficient** — the same shape as the
finding it was created from (de-laundering was necessary but not sufficient
for these carriers). Two levels stacked:

```
axiom-discharged instance   →  removed (#4750)
trivially-inhabited fields  →  this bean
placeholder semantics       →  the real blocker, below both
```

Refining `residual : ℝ` into `geom_unknot : geom 🝆 = ε` only relocates the
vacuity unless `geom` is a genuine function. Introducing `opaque geom` would
help — an opaque global cannot be satisfied by choosing a convenient value —
but that is a modelling decision about the Hoefsmit pipeline, not a schema
edit, and it belongs with whoever owns `Conjectures.lean`'s narrowing work.

### Revised next step

Not "refine ten field schemas". In order:

1. **Consolidate** the duplicate `VacuumEpsilon` / `VacuumEpsilon'` carriers.
2. **Replace the identity placeholders** (`QOU_VacuumEnergy`,
   `QOU_ObservabilityNorm`) with `opaque` constants. That single change makes
   every class field written over them non-trivial, because an opaque global
   cannot be witnessed by `rfl`. It is likely the highest-leverage edit in
   this whole area and is *not* per-carrier work.
3. Only then refine the per-carrier schemas, against real functions.

Step 2 is cheap and mechanical; I have not done it because it changes the
semantics of a file with an active narrowing audit, and stepping on that is
the coordination failure AGENTS.md warns about. Worth a note to whoever owns
`Conjectures.lean` before it is attempted.
