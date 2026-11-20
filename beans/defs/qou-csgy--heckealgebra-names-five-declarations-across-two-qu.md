---
# qou-csgy
title: HeckeAlgebra names five declarations across two quadratic conventions
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T13:50:38Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-k4oq
---

Found while merging #6158, and **#6158 is what made it five** — I added the second convention, so
this is a defect I contributed to rather than one I merely noticed.

## The measurement

`grep -rn -E '^\s*(class|structure|def|abbrev|noncomputable def)\s+HeckeAlgebra\b' --include=*.lean`
over `folio/quantum-observable-universe/lean/`:

| FQN | kind | file:line | quadratic relation |
|---|---|---|---|
| `QOU.Hecke.HeckeAlgebra` | class | `QOU/Hecke/Algebra.lean:47` | `σ² = (q − q⁻¹)σ + 1` |
| `QOU.MathlibExt.IwahoriHecke.HeckeAlgebra` | def | `QOU/MathlibExt/IwahoriHeckeAlgebra.lean:114` | `(T − q)(T + 1) = 0`, i.e. `T² = (q−1)T + q` |
| `QOU.PathIntegrals.HeckeAlgebra` | structure | `QOU/PathIntegrals.lean:294` | — |
| `QOU.Braiding.HeckeAlgebra` | structure | `QOU/BraidKnot/CasimirShared.lean:176` | — (carries `q⁻¹` as data) |
| `H3.HeckeAlgebra` | class | `QOU/Machinery/MarkovTraceOnHecke.lean:48` | — |

## What is NOT wrong — establish this before anyone "fixes" it

- **The fully-qualified names are all distinct.** There is no duplicate-FQN, so the guard being
  built on #6191 is unaffected and neither branch has anything to repair.
- **Neither convention is an error.** AGENTS.md §7a makes `σ² = (q − q⁻¹)σ + 1` the corpus
  Hecke–skein convention; `QOU.MathlibExt.IwahoriHecke` deliberately uses **Iwahori's** `T`-form
  `(T − Q)(T + 1) = 0`, which is why its generators are named `T` and not `σ`. The two match at
  `Q = q²`, `σ = q⁻¹T` — no `√q`, no base extension.
- **`QOU.Hecke.IwahoriHecke` is in the T-convention too** (`σ_i² = (q−1)σ_i + q`, its own docstring
  writes it as `(σ_i − q)(σ_i + 1) = 0`), which is exactly why #6158's
  `algEquiv : IwahoriHeckeOfSn K q (n+1) ≃ₐ[K] QOU.Hecke.IwahoriHecke K q n` holds **at the same
  `q` with no rescaling**. So the two spellings are not evenly split: four of the five sites and
  both `RingQuot` presentations sit on one side, and the `QOU.Hecke.HeckeAlgebra` *class* is the
  one carrying `(q − q⁻¹)`.

## Why it is worth a bean anyway

The bare name `HeckeAlgebra` now resolves to two different quadratic relations depending on which
namespace is open, and nothing in the name says which. This is the `markovZ` pattern AGENTS.md
records at length — the same name spanning two conventions, accreting declarations while the
convention question underneath is being settled, and a grep that cannot separate them. That one was
found only after a rename created a case-differing twin (`markovZC` / `markovZc`) meaning opposite
things.

The concrete near-miss: #6165's `TwFullRank.lean` and `FullRank.lean` both say *"it does not supply
a `HeckeAlgebra` instance for `IwahoriHecke`: this class's quadratic field is `σ² = (q − q⁻¹)σ + 1`
while `IwahoriHecke`'s is `σ² = (q−1)σ + q`, so the two are related by a rescaling of `q`"*. That is
**true of the class they mean** and reads as a statement about "the Hecke algebra" in general — under
which reading #6158's `algEquiv` would look like a contradiction, since it relates two of these
objects with no rescaling at all. Nothing is actually inconsistent; the sentence is just
under-qualified because the name is. Raised on #6165 (comment 5469054149).

## Proposed disposition — NOT started, and deliberately not done in #6158

Doing this inside #6158 would be widening: it touches four files owned by other arcs. Options, in
what I judge to be preference order:

1. **Qualify at the citation sites** (cheapest, ~0 risk): wherever prose or a docstring says
   `HeckeAlgebra`, write the FQN. Fixes the actual failure mode — a reader resolving the wrong
   relation — without touching any declaration.
2. **Rename by convention** (what `markovZ` eventually did): keep the bare name for one convention
   and suffix the other. Note the `markovZ` lesson: the rename is where the *new* collision gets
   created, so pick suffixes that are not case-variants of each other.
3. **Do nothing.** Defensible — the FQNs are distinct and Lean itself is never confused. The cost is
   borne entirely by human and agent readers, which is precisely where this corpus has repeatedly
   paid it.

**Default if nobody acts:** nothing breaks, the ambiguity persists, and the next agent to write
"the `HeckeAlgebra` class" has a 1-in-2 chance of meaning the other relation.

**Recommendation (my judgement, not a finding):** option 1 now, option 2 only if someone is already
touching those files. The declarations are correct; it is the prose that is ambiguous, and prose is
where the near-miss actually happened.

- Round 75 (`lane-e667`): Formalized `qou-sh62`, `qou-ss88`, `qou-t1kv`, `qou-csgy`, `qou-fq1i` in `QOU.Foundations.CoordinationPeriodSeparationDisjointBlockFactorizationScalarCascadeQuadraticConventionBridgeInvolutionTrace` with 80-dps `mpmath` 2-commit witness stamp (`c9c8117f7aa28b67e2bf3a4e9b287ae17a2e5af6` -> `6d8ea219d4427f09f7950c85f1a067b42a3dd728`, `scriptHash=3a53f4d978a21ce6466ea7c8d24a6d3d41b356bea8717db46a8c42f512a4c41e`) in PR `litlfred/qou#8402` (`status: in-progress`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8402, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
