---
# qou-n4r9
title: 'EPIC: migrate qou onto the cat-harness platform (folio-assistant post-split)'
status: in-progress
type: epic
priority: high
tags:
    - platform
    - migration
created_at: 2026-09-26T11:18:14Z
updated_at: 2026-10-04T15:10:14Z
parent: qou-5vkl
---

**Owner direction, 2026-09-26, verbatim:** *"In middle of migration/refactoring
of folio-assistant. Be careful. Do it properly."* / *"Part of reeval of
bean/workplan is plan for qou platform migration to New folio-assistant
cat-harness"* / *"Can move content/ for to folio/ to match. Align to f-asst
unless specific reason not to"*.

This epic is that plan. Six stories, ordered. `qou-ty42` remains the record of
where the PREVIOUS attempt stopped and why; this epic supersedes it as the
forward plan and does not contradict its two owner rulings.

## 🛑 THE TARGET IS MOVING — measure before every step

Platform main went **e53bba80284 → 42ccfb38b63, 80 commits, in about one hour**
(both measured this session). Anything this epic says about platform internals
has a shelf life of hours. **Re-measure at the commit you are actually going to
pin**, and record that sha in whatever you write.

Concrete instance of the cost, from this session: a sibling read of
`harness-config.ts` said *"`<name>.config.json` is the declaration too since
`harness.json` was excised"*. Eighty commits later there are **two** functions,
`instanceConfigFilename` (`<name>.config.json`) and `instanceDeclarationFilename`
(`<name>.json`) — the declaration was not folded in, it was **renamed**. A plan
written on the first reading would have produced one file where two are needed.

## What "align to f-asst unless specific reason not to" changes

It **reverses the premise of `harness.json`**. That file exists, in its own
words, because *"folio-assistant retired `content/` as the folio-root convention
in favour of `folio/` … qou keeps `content/` … so rather than move the tree, it
SAYS where the tree is."* The owner now says the tree may move. So the
declaration stops being a workaround for a divergence and becomes just a
declaration — see `qou-yqko`.

## The ordering, and why

1. **`qou-yf1y`** — the declaration + config pair. Everything else is invisible
   to the platform until an instance is discoverable, and it is the cheapest
   step.
2. **`qou-utbr`** — beans to `beans/`. Independent of the platform pin, and it
   is the half of "reeval of bean/workplan" that is structural rather than
   editorial.
3. **`qou-yqko`** — `content/` → `folio/`. Large and mechanical; do it when
   nothing else is in flight.
4. **`qou-8321`** — the pin bump. Owner-gated, and the step that makes 1-3
   load-bearing rather than preparatory.
5. **`qou-pwp9`** — `build.yml` off `@main`. Should land BEFORE the bump, because
   it is the hole the pin exists to close.
6. **`qou-w5av`** — rendering → justthepages. **Blocked on a definition**: no
   repo named `justthepages` exists and the platform does not mention it.

## What is NOT in scope here

The `.folio-assistant-pin` header's own rule still binds: when the pin moves,
**state the before/after issue counts in the commit message**. And `qou-ty42`'s
ruling that `folio.config.json` must not be deleted holds until `qou-yf1y`
replaces it deliberately rather than as a side effect.



## Reorganisation 2026-10-04

Now the epic for MIG under Platform, tooling and hygiene.
