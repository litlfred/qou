---
# qou-a5p6
title: 'setup-folio-assistant: platform clone silently sat 65 commits off-pin; qa-sweep dirties it and freezes the checkout'
status: todo
type: task
priority: normal
created_at: 2026-08-23T13:50:54Z
updated_at: 2026-08-23T13:51:33Z
---

## The defect

`scripts/setup-folio-assistant.sh` moves the platform clone to `$REF` **only when
the clone's tree is clean** ("never clobber uncommitted local work"). When it is
dirty it prints a bare `info` line and moves on.

`qa-sweep` rewrites `content/pipeline/script-sidecars/*.script.json`
(`last_run_at`, `deps_hash`, `script_hash`) **on every run**. So any use of the
pipeline dirties the clone, and from then on the checkout step is silently
skipped forever. The more the pipeline is used, the more permanently stale it
becomes.

**Measured this session:** the clone sat at `c396c1f`, **65 commits behind the
pin** `e1030e8` (`.folio-assistant-pin`). Nothing reported it — not the setup
script, not `check-sidecars.sh`, not the session-start hook.

## The cost — a session's QA findings, wrong

Every `qa-sweep` I ran used that off-pin code, and two findings I reported were
artifacts of it:

* **RETRACTED — "a per-block `qa-sweep` degrades detangler verdicts."** I measured
  36 `detangler-* pass -> n/a` flips and one `detangler-no-forward-ref fail/major
  -> n/a`, and discarded a 10-block drain to avoid erasing a recorded major
  finding. Re-tested **at the pin**: `physics-names-knot-operations` gives
  **0 verdict changes** and retains `findings: 0 critical, 1 major`. The drain is
  safe at the pinned version. The finding was the stale clone, not the sweep.
* **STANDS — the label-less-prose enumeration gap.** `walkBlocks(walkRoot)` does
  not enumerate a `prose()` block with no label (`blocks: 0`). Fixed upstream in
  folio-assistant `b48cff7` ("walk: separate what is in the graph from what prose
  ships", adds `includeUnlabelled: true`) — but the **pin predates that commit**,
  so it is live for qou until the pin is bumped. Of the 51 criterion-stale
  sidecars, 45 are labelled (targetable) and 5 are not.

Unaffected: the 376 / 51 / 325 sidecar-state measurement on `qou-zjfs` is computed
from committed `.qa.json` bytes, not by running the pipeline, so it is independent
of clone version and stands.

## The fix in this branch

`report_off_ref()` — after the fast-forward attempt **and** on the dirty-tree
path, compare `HEAD` against the resolved `$REF` and, when they differ, `warn`
with the distance, the actual HEAD, and the one-line remedy. `$REF` may be a
branch **or a pinned SHA**, so it resolves `origin/$REF` first and falls back to
`$REF` itself — the first cut compared against `origin/<sha>`, which silently
matches nothing and never fired.

Verified both directions: silent at the pin; at `HEAD~7` + dirty it reports
*"NOT at e1030e8… (40 commit(s) behind); it is at 1dd31a3"*.

## Not done here

Bumping `.folio-assistant-pin` to pick up `b48cff7` (and 235 other commits) is an
owner call with its own blast radius — the pin exists precisely so the pipeline
does not move under the corpus. Flagged, not done.
