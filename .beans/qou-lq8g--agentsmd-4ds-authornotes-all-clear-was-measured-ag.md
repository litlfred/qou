---
# qou-lq8g
title: AGENTS.md §4d's authorNotes all-clear was measured against a platform this repo does not use
status: todo
type: task
priority: normal
created_at: 2026-09-05T09:03:22Z
updated_at: 2026-09-05T09:04:18Z
---

## The claim

AGENTS.md §4d carries a block headed *"The `authorNotes` half of this is FIXED …
RE-MEASURED 2026-09-03"*, with a table reporting **`authorNotes` dropped: 0 —
fixed upstream 2026-08-24**, measured *"against `folio-assistant` `93e476b`"*.

**That platform is not the one this repo runs.** `scripts/setup-folio-assistant.sh`
pins the platform to the SHA in `.folio-assistant-pin`, currently
**`428ca5c` (2026-08-23 09:52)**. The upstream grant — `affcec4` *"schema: grant
authorNotes to prose, equation, diagram and table"* — landed **after** it.

So an agent following AGENTS.md's own instruction (run the setup script, then
validate) gets the pinned platform and still sees the warnings the correction
records as fixed.

## The evidence

Measured 2026-09-05, fresh clone created by the setup script at 09:00:04:

    .folio-assistant-pin                 428ca5c98c107191303878eb98b6bfbc61f2f066
    pinned commit                        428ca5c  2026-08-23 09:52:06 +0200
    folio-assistant origin/main          2026-09-05 08:24:56 +0200  (169 ahead)
    upstream fix                         affcec4  "grant authorNotes to prose,
                                                   equation, diagram and table"

`bun run scripts/run-validate.ts content/quantum-observable-universe` against the
pin reports **5 `authorNotes` warnings + 1 `computation`** — the same six the
superseded §4d text lists, in the same blocks.

## What is NOT wrong

**The pin is correct and deliberate; do not "fix" it by tracking main.** Its
rationale is in the script's own header: the checkers live in the platform repo,
so every count this repo quotes is a function of two inputs, and defaulting to
`main` let two agents on the same corpus commit measure different numbers and
each be right (bean `vbase`). Moving the platform is meant to be a reviewable
one-line commit to `.folio-assistant-pin`.

**The upstream fix is also real.** Both halves are true; they describe different
platforms.

## The defect, precisely

§4d's *"live state, measured 2026-09-03"* table reads as a statement about this
repo and is a statement about unpinned upstream. It is the same class as
everything else that section documents — a measurement quoted without the
context that determines what it measures — one level up.

## Options

1. **Annotate §4d** with the pin caveat: say the table was measured against
   unpinned `main`, and that the pinned platform still drops these fields until
   the pin advances past `affcec4`. Cheap, no behaviour change, keeps both facts.
2. **Advance `.folio-assistant-pin`** past `affcec4`. Makes the all-clear true
   here — but moves the platform 169 commits, which changes every count this
   repo quotes and is exactly the reviewable decision the pin exists to force.
   Not an idle-pass action.
3. **Do nothing.** The six fields stay silently dropped, and the next agent to
   validate sees warnings a corpus-grep tells them are fixed.

**Recommendation (my judgement, not a finding): option 1 now, and option 2 only
as its own PR with the count deltas measured.** The annotation costs a
paragraph; the pin bump needs someone to look at what 169 commits of checker
changes do to `validate: N issues` and `wall-side M/1190`.

**Default if nobody acts:** nothing breaks. The warnings are advisory, the
dropped fields were already dropped, and the only cost is a future agent losing
time to the contradiction.

## Blast radius in real terms

The six dropped fields are five `authorNotes` (on `fine-structure-data`,
`tm-interaction-completeness`, `millennium-bounds-via-surreals-intro`,
`hecke-log-decomposition-table-data`, `q-beta-form-a-n1-symbolic-table-data`) and
one `computation` on `knot-periodic-table` — that last one is the block's link to
its producer, so it is the only one with a downstream consumer rather than being
author-facing prose.

Found while running the render-QA and validate gates for `qou-bk77`.
