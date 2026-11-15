---
# qou-0sq1
title: 'Forward-pointing interprets edges: nine relocations, three questions'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-16T01:51:33Z
updated_at: 2026-10-04T15:19:20Z
parent: qou-hqo3
---

Audit: `docs/audits/2026-08-16-forward-interprets.md`.

Making `interprets` an editorial edge (folio-assistant `i8ad`) exposed ten
blocks placed **before** the block they interpret — a reader meeting an
interpretation of something they have not read yet.

**`detangler-no-forward-ref` does not count these.** It builds its own
`uses`-only adjacency, so they sit outside the gate. Widening it would move 195
→ ~205, a number five merged PRs were measured against, so that stays a separate
decision — and nothing here depends on it. These are wrong for the reader
whether or not a gate counts them.

## Done: one listing-order slip

`rem:collatz-parity-to-divisor` interprets `prop:collatz-contact-boundary` and
was listed immediately before it, both in `appendix-surreals §15`. Adjacent, one
section, nothing depending on the order. Swapped. Ten → nine.

## Open: nine relocations, as three questions

Every remaining one crosses a **section** boundary, so each is a relocation that
changes what a chapter argues in what order — not a tooling decision. Grouped,
they are three questions rather than nine:

1. **Three remarks in `predicted-spectra §13`** all interpret
   `prop:shell-closure-normal-form` in **§14**. One decision covers all three:
   the proposition moves up, or the remarks move down.
2. **Two remarks in `observations §3` and `§8`** interpret `prop:local-substrate-q`
   in **§17** — gaps of 180 and 117, the two largest in the corpus. A
   proposition two named experiments depend on, sitting after both.
3. **Three singles**, of which `ex:brings-surface` → `def:brings-surface` is the
   clearest in principle (an example before the definition it exemplifies) and
   the most plausibly deliberate — a scene-setting section may introduce an
   object informally before defining it. That is why it is listed rather than
   moved.

## Why this bean stays open

The one mechanical case is fixed. The nine remaining need someone to decide what
each chapter should argue first, and "the graph says it points forward" is a
reason to ask, not an answer. The audit lists section titles for each so the
question can be answered without re-deriving anything.
