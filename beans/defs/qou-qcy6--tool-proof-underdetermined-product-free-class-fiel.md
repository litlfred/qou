---
# qou-qcy6
title: 'TOOL: proof-underdetermined-product — free class fields that occur only as a product'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T07:09:37Z
updated_at: 2026-10-04T15:14:15Z
parent: b9cj
---

Raised by a sibling on PR #6097, relayed as a coordination comment on #6093,
and VERIFIED here before being accepted (a sibling's comment is not a primary
source — AGENTS.md §corpus-grep).

## The shape

A conditional class carries two free fields that appear together in exactly one
equation, multiplied. An equation on the PRODUCT `y_λ · χ^λ` pins NEITHER
factor, so an instance can realise any value at all. #6097 machine-checked it:

```lean
theorem yLambda_not_pinned (n : ℕ) (c : ℚ) (hc : c ≠ 0) :
    ∃ WD : WedderburnDecomp (R := ℚ) n 1 ℚ, ∀ lam, WD.y_lambda lam = c
```

Every nonzero rational is realised as the weight at every partition, by a
witness satisfying the whole class.

## Why it needs a new criterion — measured, not assumed

The carrier is not empty, not `: True`, not under-specified against its
docstring, and every field is a true sentence about a genuine Wedderburn
decomposition. So `proof-no-empty-prop-carrier`, `proof-claims-unencoded` and
the trivial-true detector all pass it, CORRECTLY. Confirmed by measurement on
2026-08-30: `WedderburnDecomp` appears **0 times** in the 368-entry vacuity
ledger and **0 times** among the audit's 133 candidates.

It is also outside what THIS session added. `valueOnlyProjects` (PR #6093, batch
9) reads the PROOF TERM; this defect is in the CLASS'S FIELD STRUCTURE, with no
proof term involved. Three distinct detectors now, on three distinct halves of a
declaration: statement (`defeqCollapse`), value (`valueOnlyProjects`), and
class-field graph (this one).

## Second instance, found while verifying the first

`QOU.Mathlib.HeckeAlgebra.WedderburnDecomposition` (line 118) is a different
member of the same family and is ALSO uncaught:

```lean
  /-- The sum `Σ_λ p_λ = 1`. -/
  blocks_sum_to_one : Prop
  blocks_sum_holds : blocks_sum_to_one
  /-- Pairwise orthogonality: `p_λ · p_μ = 0` for `λ ≠ μ`. -/
  blocks_orthogonal : Prop
  blocks_orthogonal_holds : blocks_orthogonal
```

The docstring states the equation; the field is an UNCONSTRAINED `Prop`
variable, so an instance may take `blocks_sum_to_one := True` and discharge
`blocks_sum_holds := trivial`. The audit reports 0 candidates for this file, so
this shape is invisible too. Whether one criterion covers both or they are two
(`underdetermined-product` vs `prop-valued-field-plus-its-own-proof`) is the
first design question.

## What is mechanical here

Both are decidable from the class's field graph without an agent verdict, which
makes this unusually cheap for this audit family:

- a field of type `Prop` (not a Prop-VALUED proposition, a bare `Prop`) whose
  only use is as the type of one sibling field;
- a field occurring in exactly one equation, multiplied by another field that
  also occurs only there.

## Note on where the verdict lives

Both classes are library Lean under `content/**/lean/QOU/**`, so neither has a
`.qa.json` sidecar and the verdict has nowhere to live except
`docs/audits/lean-vacuity-review-ledger.json`.

Deliberately NOT done on #6093: that PR drains the borrowed-name tiers and adds
two kernel predicates; a third detector is new scope.


## 2026-09-06 — HALF LANDED: the self-discharged `Prop` pair, 17 candidates

Commit `dccab733a7`, PR #6930.

### What shipped

`detectSelfDischargedPropField` in
`content/pipeline/lean-vacuity-axiom-audit.ts`, emitting under
`proof-claims-unencoded` with pattern **`prop-field-self-discharged`**
(MAJOR — a high-recall candidate for an agent verdict, matching the rest of
this family; no new `Category` entry, so the registry is untouched).

**The blind spot is in `detectPropUniverseField`'s exemption, not in its
existence.** That detector fires only on an *unconsumed* `Prop`-universe field,
and it is right to: firing on any `Prop` field over-reported 6× (101 carriers).
But the exemption is satisfied by a consumer that adds nothing. When the only
sibling mentioning `p` has type *literally `p`* —

    blocks_sum_to_one : Prop
    blocks_sum_holds  : blocks_sum_to_one

— the instance still chooses the proposition and `⟨True, True.intro⟩` inhabits
the pair. It asserts exactly what a bare `p : Prop` asserts, while looking
twice as populated.

**Narrower than "has a bare-assertion consumer", deliberately.** A field with a
bare assertion *and* a relating sibling keeps its content and stays silent —
which is what preserves `QOU.Torsion.BraneBoundaryContext`, the counter-example
`detectPropUniverseField` is calibrated against (`brane_boundary_regular`
carries `boundary_active : brane_boundary_regular` **and** an implication
field, so the `every` test fails). The refinement narrows that exemption
without overturning its calibration, and that was the design constraint.

### 17 candidates, and the Hecke stack is in them

`IwahoriHeckeAlgebra` (`hecke_relation`, `braid_relation`), `MarkovTrace`
(`markov_axiom`), `WedderburnDecomposition` (`blocks_sum_to_one`,
`blocks_orthogonal`), `WenzlBridge` (`bridge_identity`), `MarkovTraceRecursion`,
`HasGeneratorAction`, `NonAbelianStokes`, `LieValuedStokes`,
`OperatorSelectionLP`, `CanonicalKnotIdSDP`, `BorromeanQuark`,
`BringWPlaneMonodromy`, `VorticityLowerBoundContext`,
`EInfinityIdentificationsContext`, `SpectralSequenceH3ExplicitContext`,
`QmnRecursiveMemoizedContext`, `WenzlQmnSynergyContext`.

Several **say so in their own docstrings** — *"the bridge identity (placeholder
Prop; instances discharge)"*, *"the Markov axiom (placeholder shape)"* — and
`HeckeAlgebra.lean`'s `triv_wedderburn` discharges both Wedderburn fields with
`:= True` / `:= True.intro` twelve lines below the class. The source is honest;
nothing could see it.

### Audit witness delta, and what is NOT mine

    scanned_files            3658 -> 3686   (+28 landed on main since 2026-09-05)
    proof-claims-unencoded     37 -> 54     (+17, this detector)
    total_defects              75 -> 90

`proof-no-unused-hypothesis-rfl` and `proof-no-provable-axiom` each went
**1 → 0**. That is **not** this change: the diff adds one function and one
`push` call, and `push` does not dedupe (`if (h && …) hits.push(h)`), so it can
only add. Those two come from the 28 files.

### STILL OPEN — the product shape, and the design question is answered

They are **two criteria, not one**. The shape shipped here is decidable from
the field graph by name lookup. The product shape —

    y_lambda : Partition n → R        (free)
    chi      : … → R                  (free)
    frobenius_pairing : tr_M w = Σ_λ y_lambda λ * chi λ w

— needs the *equation* parsed, and needs "occurs only as a factor of one
product" rather than "occurs in a sibling's type". It is the more
false-positive-prone of the two and it is left on this bean.

### Ledger

All 17 are library Lean under `content/**/lean/QOU/**` or content-block
siblings, so verdicts belong in `docs/audits/lean-vacuity-review-ledger.json`.
**Not seeded here** — seeding 17 `needs-agent` rows is a separate pass, and
each wants the citing carrier read before a verdict.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-06 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (Round 58 — PR #8304)
- **Status:** `in-progress` (opened `litlfred/qou#8304`, branch `claude/round58-devacuify-6qbv-b9cj`, HEAD `e72e4e04168ffebca669be8e58b6df711ee7f5ed`, C1 `e3528dd09222e2ddccf5556168d0aa31aca7f5d7`).
- **Target:** `folio/quantum-observable-universe/lean/QOU/ProofHygiene/SelfAssumingContexts.lean` + 80-dps witness `computations/probes/round58-devacuify-6qbv-b9cj.witness.json` (`scriptHash = a44d91e59ddc`, `allPassed = true`, `0` `float64`).
- **Updated at:** `2026-11-17T10:34:25Z`.
