---
# qou-a30t
title: 'Self-assuming context classes: one machine-checked criterion for four ledger patterns (46 live genuine entries)'
status: in-progress
type: task
priority: normal
created_at: 2026-09-12T12:02:39Z
updated_at: 2026-09-12T12:06:50Z
---

## The criterion (2026-09-12, PR #7208)

`QOU/ProofHygiene/SelfAssumingContexts.lean` — Mathlib-only, no QOU imports, citable from
anywhere in the tree. Sorry-free; of its 16 declarations **14 depend on no axioms at all**
and 2 only on `propext`.

  `Contentless K C  :=  Nonempty K ↔ C`

The class is inhabited exactly when the conclusion holds, so instantiating it is logically
identical to assuming `C` — **however the conclusion is extracted**: by projection, by
application, or by a chain of either. That "however" is what lets one criterion cover
shapes that four separate detectors see differently.

| ledger pattern | shape | theorem |
|---|---|---|
| `field-projection`, `exact-field-projection` | a field of the conclusion's own type | `selfAssuming_contentless` |
| `tuple-projection` | several conclusions bundled, one projected | `tuple_contentless` |
| `decoy-hypothesis` | `⟨P : Prop, hP : P, impl : P → C⟩`, extracted by **application** | `decoy_contentless` |

**46 live `genuine` entries** between them, measured against the recorded `file_sha` so
stale verdicts are excluded (bean `qou-wsx3`).

`selfAssuming_contentless` is what AGENTS.md §3b-cond item 5 calls a *"vacuous
self-assuming projection"* — stated there in prose since the rule was written, now
machine-checked.

## The test a reviewer can actually run

`not_contentless_of_witness` — **exhibit an instance without already having the
conclusion**, and the class carries something. `conditional_not_contentless` runs it on the
shape that should pass: a genuine §3b-cond `ConditionalContext H C` carries the implication
and *not* the antecedent, so at `H = C = False` it is inhabited while the conclusion fails.

The operative question, and it has a definite answer: **does the class supply its own
antecedent?**

## Why the existing detector misses the decoy shape

`proof-no-self-assuming-projection` looks for a field *of the conclusion's type* being
projected. `DecoyContext` has no such field — it has `P → C`, and `ctx.impl ctx.active` is
an **application**. A field-projection scan is structurally blind to it, which all 13 decoy
ledger entries say in nearly identical words. That is a detector blind spot of the same
family the taxonomy in `2026-08-15-detector-blindness-taxonomy.md` catalogues.

## A Lean detail worth not rediscovering

A structure all of whose fields are `Prop`s lands in **`Prop`**, not `Type`. Three of the
four shapes here are therefore `Prop`s (`DecoyContext` is not — its `premise : Prop` field
is `Type`-valued), so `Contentless` must quantify over `Sort*`. With `Type*` the file does
not compile, and the error names a sort mismatch rather than anything about the
mathematics.

## Deliberately NOT done

- **No claim that the 46 conclusions are false or doubtful.** Several are plainly intended
  as honest §3b axiomatisations of open inputs. The claim is narrower and entirely about
  the Lean: *as structured, those declarations prove nothing beyond assuming their
  conclusions*, so they may not be cited as evidence for them.
- **No file restructured.** Each fix is a per-file mathematical judgement about what the
  genuine sub-hypotheses are — the conclusion *composed* from fields rather than applied
  from one — which is the author's call, and doing 46 of them is a sweep the ASK-OWNER
  directive gates.

Left in-progress: the artifact exists; the 46 entries are not drained.


## Correction and a fifth pattern (same day)

**The count above is wrong. It is 48, not 46** — `field-projection` 22 +
`exact-field-projection` 2 + `tuple-projection` 11 + `decoy-hypothesis` 13. The 46 came
from my own arithmetic, not from a stale measurement, and it reached the Lean docstring,
a commit message and this bean before being re-counted. Recount with the script rather
than quoting any of the three.

**A fifth pattern is now covered: `prop-universe-field` (19 live), for 67 across five.**
It is the sharpest of them and the only one that is a *type-level* error rather than a
judgement about intent. The ledger states it identically in all 19:

> *"Every field of this carrier is typed bare `: Prop` — the UNIVERSE of propositions, not
> a proposition. An instance therefore supplies a proposition rather than a proof of one,
> so `instance := ⟨True⟩` type-checks and discharges the class."*

Proved rather than trusted:

- `propUniverse_inhabited` — the carrier is inhabited **outright**, `⟨True⟩`.
- `propUniverse_contentless` — so it is contentless for **`True`**: it asserts nothing
  whatever, which is strictly worse than the self-assuming shapes, which at least assert
  their conclusion.
- `conditional_on_propUniverse_is_unconditional` — **the harm, exactly**: every theorem
  stated conditional on such a carrier is unconditional, because the hypothesis discharges
  itself. A `[C]`-conditional result downstream of one of these 19 is conditional on
  nothing, and the §3b-cond exception does not apply to it however the block is labelled.
- `propUniverse_vs_propField` — the discriminator is the field's **type**, mechanically:
  `PropUniverseContext` is always inhabited, `SelfAssumingContext False` never is. So
  `claim : Prop` versus `claim : C` is the whole difference, settled by looking at the
  field rather than the docstring.

All five new declarations depend on **no axioms at all**.
