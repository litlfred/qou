---
# qou-85wn
title: he4-two-row-dominance quotes pre-regeneration numbers — thesis survives, every table value is stale, one contribution flips sign
status: todo
type: task
created_at: 2026-09-06T12:44:43Z
updated_at: 2026-09-06T12:44:43Z
---


## The finding

`content/quantum-observable-universe/mass-theory/he4-two-row-dominance.md` is a
**reader-facing** content block whose table was computed against the
`chi-helium-4-h12-at-q0-50dps` cache as it stood before the 2026-09-06
regeneration (`qou-92u9`, owner ruling "regen").  Content blocks are not
re-run by any witness sweep, so nothing caught this.

## What SURVIVES — and it is the block's actual thesis

- The `y_λ` column is **identical**: `1.7441e-3`, `1.1941e-3`, `2.3704e-3`,
  `6.9619e-4`.  `w` is a function of the partition and `q` alone, so it could
  not move — the same invariance that held across the whole O3′ arc.
- The structural claim — *"the two-row-stratum ratio is **exactly 1**; all 70
  partitions of 12 with more than two rows contribute 0"* — **still holds**,
  measured 1.0 exactly.  The `≥ 0.80` bound is still satisfied.

**So the block's conclusion is not in question.**  Two-row dominance survives.

## What is STALE — every number in the table

    quantity            block says        regenerated      note
    tr_M(β_4He)(q0)     0.160974145442    0.0112374176598  factor 14.3248
    χ(9,3)              +27.3348          +4.14962
    χ(8,4)              +30.2676          −2.97948         SIGN FLIP
    χ(10,2)             +10.4630          +0.543341
    χ(7,5)              +21.7770          +0.424982
    contribution (9,3)  29.617 %          64.406 %
    contribution (8,4)  22.452 %          −31.659 %        NOW NEGATIVE
    contribution (10,2) 15.407 %          11.461 %
    contribution (7,5)  9.418 %           2.6329 %

## 🛑 The sign flip is not just a number — it changes the picture

Under the old data the table read as five positive blocks sharing the trace.
Under the regenerated data `(8,4)` contributes **−31.7 %**: the "dominance" is
now a partial cancellation between a large positive `(9,3)` and a large negative
`(8,4)`, not a straightforward concentration.  The *ratio* is still exactly 1,
so the stated claim is untouched — but a reader given the new table would draw a
different qualitative conclusion from the same sentence.

## Why this is not being edited unilaterally

Three reasons, in order of weight:

1. **It is the paper.** A math-bearing `.md` table is reader-facing content, and
   AGENTS.md gates such edits behind the render-QA battery (balanced delimiters,
   the align-family fencing rule, the expository pass) plus sidecar refresh.
2. **The sign flip is an interpretive change, not a transcription.** Rewriting
   `+22.452 %` to `−31.659 %` inside prose about "dominance" is a judgement about
   what the block should now *say*, which is the author's call.
3. The numbers can be regenerated mechanically at any time; the sentence around
   them cannot.

## What to check next

Whether other content blocks quote chi-cache-derived numbers.  The scan that
found this one covered `content/`, `docs/audits`, `docs/coordination` and
`.beans` for citations of the 78 witnesses this branch refreshed: **176 files
cite one**, of which **6 are under `content/`**.  Most citations are references
rather than quoted values — this block is the one confirmed to quote numbers
that moved.  The other five are unchecked.
