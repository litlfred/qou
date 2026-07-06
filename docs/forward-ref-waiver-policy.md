# Forward-reference waiver policy

> **Superseded (2026-05-29) by the logical-vs-storytelling severity
> model.** The headline metric is now the **logical-defect count**, not
> the A–F "actionable" count described below. See
> [`docs/forward-ref-logical-analysis.md`](forward-ref-logical-analysis.md)
> for the current model: a forward reference is a *defect* only when the
> reader must **rely on** the target's content to follow the argument
> made here (logical/expository); references that merely motivate,
> interpret, or cite later content are storytelling and benign. The only
> sanctioned logical forward reference is into the surreal-number lift
> (`appendix-surreals`) plus the `FOUNDATIONAL_LATE` allowlist. The A–F
> categories below are retained for historical continuity.

A **forward reference** is a content block in chapter N whose `uses[]`
or `interprets` field points at a block defined in chapter M > N. Not
all forward refs are defects — many are structurally inherent to a
connected scholarly paper. This document defines the six categories,
which are waived, and why.

Authoritative classifier:
[`computations/forward_ref_classifier.py`](../computations/forward_ref_classifier.py).
Run it to regenerate
[`forward-ref-classification.witness.json`](../computations/forward-ref-classification.witness.json).

## Categories

| Cat | Name | Waived? | Rationale |
|-----|------|---------|-----------|
| **A** | proof-dep (provable→provable) | **Actionable** (with exception) | A provable block (`def`/`prop`/`thm`/`lem`/`cor`/`prf`) `uses[]` a provable block in a later chapter. These are genuine ordering tensions. **Exception:** if the target is on the `FOUNDATIONAL_LATE` allowlist (e.g. `def:habiro-ring`), the edge is waived — the object is intentionally used early but formally developed late. |
| **B** | definition-consumer | **Actionable** | A block `uses[]` a `def:` that lives later. The definition can often move earlier without cost. |
| **C** | remark-interprets-later | **Waived** | A `remark` interprets a proposition proved later. The interpretation is placed where it reads naturally in the narrative; the proof belongs in its formal chapter. Moving the remark would divorce it from its context. |
| **D** | framing/preview | **Waived** | An intro, overview, or framing-chapter block previews later content. Framing chapters (`models-of-qous`, `notation`) and section intros exist precisely to preview the arc. |
| **E** | observational consumer | **Waived** | The `observations` / `molecular-construction` / `organic-chemistry` chapters cite predictions or dynamics proved upstream in narrative but downstream in the manifest (cross-Part story arc). |
| **F** | appendix/surreal/framing target | **Waived** | The target is an appendix, the surreal lift (`appendix-surreals`), or the `models-of-qous` gallery. Appendices and the surreal lift are deliberately terminal — everything may reference them; they reference little. |

## Current counts

Regenerate with `python3 computations/forward_ref_classifier.py`.
As of the policy's introduction:

```
Total:      277
Waived:     171  (C: 54, D: 70, E: 8, F: 34, A-foundational: 5)
Actionable: 106  (A: 104, B: 2)
```

## Why waived categories are excluded from stats

The detangler's headline metric is the **actionable** forward-ref
count — the number of edges a block-move or chapter-reorder could
remove without breaking the paper's narrative or pedagogy. Waived
edges (C–F + the foundational-A exception) are structurally inherent:
removing them would require either moving an interpretation away from
its context (C), gutting a framing chapter (D), reordering Parts (E),
or relocating an appendix into the main body (F). None of those are
improvements, so they are excluded from the metric the detangler
optimizes.

## Adding a foundational-late exception

If a proof-dep (category A) edge is genuinely structural — the target
is a foundational object intentionally introduced late — add the
target label to `FOUNDATIONAL_LATE` in `forward_ref_classifier.py`
with a one-line comment explaining why. The edge then reclassifies
from actionable-A to waived-A. Do **not** add a label merely to lower
the count; the test is "is this object used before its formal home by
design?"
