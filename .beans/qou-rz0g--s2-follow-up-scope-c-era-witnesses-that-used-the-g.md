---
# qou-rz0g
title: 'S2 follow-up: scope C-era witnesses that used the Gram inverse'
status: todo
type: task
priority: normal
created_at: 2026-08-16T11:39:53Z
updated_at: 2026-08-16T11:39:53Z
---

Follow-up to `qou-cds2` (S2). Distinct from — check these before starting —
`qou-emyt` (convention C is a producer-layer problem, 70 producers / 86
witnesses), `qou-eea0` (the campaign that drained the bulk), `qou-cdh3` (the
14 structural + symbolic C witnesses that remain).

## The question

Under convention C the Gram inverse `G_INV` was computed from a **non-TL
trace**. Convention D's radical is the Temperley–Lieb ideal, so the D form
is singular and what replaces `G_INV` is the inverse **on the quotient**
`H_n/rad` (`gram_quotient_inverse`, the Moore–Penrose pseudoinverse).

Those two objects differ **exactly on the radical**. That is not a small
difference and it is not a limit: a C-era witness that consumed `G_INV` is
**not a D approximation** of anything. It is a value from a different form.

## What is and is not being claimed

**No claim is being made that any specific witness is wrong.** The survey
has not been done. This bean exists to *scope* it, and the scoping is the
whole deliverable — an agent that starts regenerating witnesses off this
bean has skipped the point.

## Why the existing C-witness beans do not cover it

`qou-emyt` / `qou-eea0` / `qou-cdh3` key on **convention-C markers** — a C
`z` value, a structural dead-block signature, a symbolic `√q` form. A
witness that consumed `G_INV` need carry **none** of those: it can record a
perfectly ordinary-looking derived number whose only C dependence is that
`G_INV` was in its call chain. The existing detectors are value-keyed; this
one has to be **call-graph-keyed**.

Compare `qou-cdh2`, which measured the reach of the `pyhecke.gram.z` symbol
(13 re-exporters + 13 consumers). The same shape of audit is needed for
`G_INV`, and it is a different symbol with a different reach.

## What to do

1. **Enumerate the consumers of the C-era `G_INV`,** not of `z` — module
   re-exports included. `qou-m7py` records that `gram.py` exported `G_INV`
   **at import** into `constants.py`, `atom.py`, `molecular.py`, `sdp.py`
   and nine corpus consumers, so the reach is import-time and wide.
   Note `G_INV` no longer exists (`test_gram_values.py:169` asserts it must
   not be resurrected), so this is a **historical** call-graph question —
   walk the git history of the consumers, not just the current tree.
2. For each consumer, find the witnesses it produced while `G_INV` was live.
3. Classify each: (a) the quantity is radical-independent, so C and D agree
   and the witness stands; (b) the quantity pairs through the radical, so
   the recorded number is a different form's answer and the witness must be
   regenerated or retired; (c) undetermined — say so.
4. **Report the survey before regenerating anything.** A regeneration
   cascade launched off an unmeasured scope is exactly what `qou-cdh3`'s
   two gates exist to prevent.

## Provenance

Filed 2026-08-16 from an agent that could not reach the `beans` CLI.
