---
# qou-zzhw
title: PentagonUvCommutation's placeholder theorem is vacuous (∨ True) — now that it compiles, the vacuity scanner will see it
status: in-progress
pr: 8206
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T21:40:00Z
updated_at: 2026-11-16T21:22:30Z
parent: qou-5p7n
---

Surfaced while draining `QOU/QuantumBloch/PentagonUvCommutation.lean` (bean
qou-rc7b). Flagging rather than silently greening it.

## The issue

`pentagon_uv_commutation_inter_level_placeholder` concludes

    u * v = q • (v * u) ∨ True

and is proved `exact Or.inr trivial`. The right disjunct makes the statement
**assert nothing** — it is `proof-no-trivial-true` from
`.claude/skills/local/lean-proof-vacuity-audit.md` §2, in its disjunctive form.

This is not sloppiness: the file's docstring says so outright — *"Until
JetProlongation lands, we leave the inter-level identity as a placeholder
disjunction including `True`"* — because the substantive proof needs
`QOU.LiftingDescent.JetProlongation` (descent operator `τ̂_n`, the operator lift
`Ũ`, the transient kernel), none of which exists yet.

## Why it matters now

The module had **never compiled** — it was one of the 785 outside the `lake build`
import closure, and it carried three separate errors (an orphaned `/--`
docstring, a `by` block ending in a term, and a stuck `HSMul` from unannotated
`let`s). Draining it makes the vacuous theorem *live*: it now enters the build,
and `content/pipeline/lean-vacuity-axiom-audit.ts` will start reporting it.

So the drain converts an invisible vacuity into a visible one. That is the right
direction, but it should be dispositioned rather than left to surprise the next
audit run.

## Honest dispositions (per the skill's fix recipe)

- **Recipe 4 — demote to `conjecture`.** Most faithful to the docstring's own
  framing; it is explicitly a placeholder awaiting JetProlongation. Claim change,
  so needs owner sign-off.
- **Recipe 3 — state the real proposition with `sorry` + `-- Ref:`.** Drop the
  `∨ True`, state `u * v = q • (v * u)` as the intended inter-level identity, and
  carry an honest cited gap. Turns a content-free theorem into a tracked one.
- **Do nothing** — but then add the `conjecture`-carve-out annotation so the
  scanner records it as exempt-but-tracked rather than flagging it every run.

Recommend recipe 3: the statement the docstring describes is precise, and a
cited `sorry` is strictly more informative than `∨ True`. Per qou-2tkh §8, run
the small-instance check on it first — a placeholder that has never been
evaluated is exactly where a false statement hides.

## Not done here

The drain commit fixes only the three *compile* defects. The vacuity is
untouched, deliberately: changing what a theorem asserts is a claim change and
belongs to the author, not to a build-drain pass.

## Round 51 Progress (PR #8206)

- [x] Removed vacuous `u * v = q • (v * u) ∨ True := by exact Or.inr trivial` placeholder in `QOU/QuantumBloch/PentagonUvCommutation.lean` (PR #8206, HEAD `aecfe3f528c442bfb5e105f53d801fa139604119`).
- [x] Proved Step 1 (`hatV_pair_commutes_of_farCommuting`), Step 3 (`hatV_braid_quadratic_swap`), Step 4 (`PentagonInterLevelDescent`, `pentagon_uv_commutation_on_transient`, `pentagon_uv_commutation_inter_level`), and concrete `2 × 2` Weyl-pair model (`weylU_mul_weylV_eq_q_smul`, `weylU_mul_weylV_ne_comm`).
- [x] Verified 80-dps `mpmath` witness `round51-devacuify-6qbv.witness.json` (`allPassed: true`, `0` float64 values) and `0` findings across all 6 vacuity audits.
- [ ] Awaiting Merge Manager merge of PR #8206.
