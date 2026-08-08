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
