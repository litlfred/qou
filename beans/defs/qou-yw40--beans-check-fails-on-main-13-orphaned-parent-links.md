---
# qou-yw40
title: 'beans check fails on main: 13 orphaned parent links to two IDs that never existed'
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T15:59:30Z
updated_at: 2026-10-04T15:16:40Z
---

Measured 2026-08-29 while running /prepare-merge-auto on PR #6009. Not caused by
that PR -- established, not assumed: `beans check` produces the IDENTICAL 13
issues in a clean tree extracted from origin/main (`git archive origin/main
.beans .beans.yml` into a temp dir), and #6009's diff touched none of the 13.

WHAT FAILS. `beans check` exits 1 with 13 broken parent links, against exactly
two missing parent IDs:

  parent 0yqu  (11 children)
    qou-abel  completed     qou-g2wr  completed     qou-b7cy  in-progress
    qou-rstq  todo          qou-clx8  completed     qou-mlbg  todo
    qou-8v3k  in-progress   qou-rhyp  completed     qou-fivt  completed
    qou-trns  in-progress   qou-r7ml  completed
  parent krvm  (2 children)
    m015      in-progress   rvnc      in-progress

SEVEN OF THE THIRTEEN ARE STILL LIVE (todo / in-progress): qou-b7cy, qou-rstq,
qou-mlbg, qou-8v3k, qou-trns, m015, rvnc. That is what makes this more than
cosmetic -- those seven are invisible to any roll-up that walks children by
parent, so a milestone view will under-report open work.

WHAT I COULD NOT ESTABLISH, AND WHY. `git log --all --diff-filter=A/D` over
`.beans/0yqu--*` and `.beans/krvm--*` reports zero adds AND zero deletes, which
reads as "these IDs never existed". DO NOT QUOTE THAT AS ESTABLISHED: this
container's clone is SHALLOW (`.git/shallow` present), so absence from the
fetched history cannot distinguish

  (a) the IDs never existed -- the children were created against a parent that
      was never minted, so the fix is to re-point or clear `parent:`; from
  (b) the parents existed before the shallow boundary and were deleted -- the
      fix is to restore them.

The two have different fixes, so settle this on a full clone before acting.
This is the same shallow-boundary trap AGENTS.md records for the ~49 % of
witnesses whose `commitSha` "resolves to nothing": 46 of 376 were confirmed
rewritten and 330 were cause-undetermined for exactly this reason.

NOT FIXED HERE, DELIBERATELY. #6009 was a four-line status-flip PR; repairing 13
orphaned links would have widened it, and the fix is not yet determined (see
above). Filed rather than fixed.

CHEAPEST NEXT STEP: on a full clone, `git log --all -- '.beans/0yqu--*'`. If
empty there too, (a) holds and the 13 `parent:` fields are simply wrong -- decide
per child whether it belongs to a live parent or to none.



## Reasons for Scrapping

Duplicate of `qou-2cyi` (work-plan reorganisation 2026-10-04). Evidence: [B] both: 13 broken parent links to two never-existing IDs (0yqu, krvm)
Content is untouched; only this work item is closed.
