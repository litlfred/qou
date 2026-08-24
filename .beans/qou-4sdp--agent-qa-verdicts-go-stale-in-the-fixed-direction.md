---
# qou-4sdp
title: Agent QA verdicts go stale in the FIXED direction and no sweep can clear them
status: todo
type: task
created_at: 2026-08-24T21:17:34Z
updated_at: 2026-08-24T21:17:34Z
---

`qou-h1p7` established that a `.qa.json` criterion holds a HISTORY of entries,
and that a stale `pass` from July looks authoritative until something re-runs
the checker. This is the mirror case, and it is worse to spot: a stale **fail**
from an AGENT, quoting prose that has since been deleted.

`qa-sweep.ts` re-runs SCRIPT criteria only. It cannot touch an agent verdict,
so an agent `fail` survives every sweep, every edit, and every fix — the block
goes on reporting a problem that no longer exists, and the only way to tell is
to open the evidence and grep the quoted string.

## Three found so far, all while fixing something else

| block | criterion | agent verdict | quotes prose that is now |
|---|---|---|---|
| `rem:markov-axioms-primitive` | `trap-meta-commentary` | 2026-08-15 | deleted (`qou-h1p7`) |
| `rem:bar-involution-c5-algebraic-identities` | `trap-meta-commentary` | 2026-08-15 | deleted (`qou-spud`) |
| `rem:qou-motivic-galois-instance-verification` | `trap-superlative` | 2026-08-22 | deleted 2026-08-23 |

Each verified by grepping the verdict's own quoted string against the current
`.md`: 0 matches in all four strings checked.

The third is the sharpest. `trap-superlative` quotes *"conj:motivic-perpetual-
obstruction **becomes an unconditional theorem** for the QOU substrate"* and
*"almost_everywhere_nontrivial **functions as a substrate axiom**"*. The block's
own `authorNotes` entry, dated **the very next day**, records that both were
corrected. So the block simultaneously carries a note saying "fixed" and a
verdict saying "broken", and the verdict is the one a QA reader sees first.

## Why it matters more than a cosmetic staleness

A stale agent `fail` is indistinguishable from a live one, so it consumes
exactly the attention a real finding would — and it trains a reader to discount
the axis. Three of the small number of blocks I happened to open were in this
state; the corpus-wide rate is **unmeasured**, and measuring it is the first
step, not fixing them one at a time.

## What would settle it

A sweep that, for every agent verdict carrying `evidence` with a quoted string,
checks whether that string still occurs in the block's current `.md` / `.lean`.
A verdict whose evidence has vanished is not necessarily wrong — the criterion
may have other grounds — but it is certainly unverified, and should be
re-queued for adjudication rather than left presenting as current. The queue
already exists (`content/pipeline/qa-agent-drain-queue.ts`); what is missing is
the detector that feeds it.

Not attempted here: this is a corpus-wide measurement plus an adjudication
pass, and both are their own work.

