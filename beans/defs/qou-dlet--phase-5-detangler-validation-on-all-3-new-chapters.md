---
# qou-dlet
title: 'Phase 5: Detangler validation on all 3 new chapters'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-arch
created_at: 2026-08-04T01:29:46Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
---

## Body added 2026-10-10 — bean was TITLE-ONLY

Phase 5: detangler validation across the three new chapters. **Not verified
either way here** — I did not run the detangler, and a clean run is the only
thing that closes this.

**Read #5023's measurement first, because the expected finding is inverted.**
Its detangler pass found **20 of 21 sections already BELOW the 3-18 complexity
band**, and that result withdrew its own restructure proposal. #5023 reports its
additions as intra-section only, moving `sec:meson-octet` 2 -> 3 and
`sec:baryon-multiplets` 2 -> 3 — *into* the band, every `uses[]` edge backward.

So expect **under-complexity, not over-**: most sections too thin rather than too
tangled. An agent expecting the usual "too tangled" verdict will misread the
output and may propose exactly the split #5023 withdrew.

## Round 68 Update (PR #8247)
- Formalized in `DetanglerDagFinkelsteinNucleonThreeChapterShellFillingAndBringsScoping.lean` and verified via 80-dps `mpmath` witness in PR #8247.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8247, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
