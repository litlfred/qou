---
# qou-gkrt
title: docs site renders 3017 of 3082 sources — 64 pages unaccounted for
status: todo
type: bug
created_at: 2026-09-26T19:52:40Z
updated_at: 2026-09-26T19:52:40Z
---

The docs site builds and is correct as far as it goes — run
[36266675464](https://github.com/litlfred/qou/actions/runs/36266675464) is green,
just-the-docs v0.12.0, all assertions passed. But the numbers do not close:

    staged markdown sources   3082
    rendered HTML pages       3017
    gap                         65

The workflow asserts only `> 2000`, so the gap passes the gate silently. **This is
not a regression from the PR that found it** (#7467) — it is a property of the
docs site as first built, and nothing is published yet (`docs-site.yml` is
`workflow_dispatch`-only with `publish` defaulting false).

## What is RULED OUT, measured locally against the staged tree

| hypothesis | measured |
|---|---|
| output-path collisions (same dir + stem → same `.html`) | **0** |
| case-insensitive stem collisions within a directory | **0** |
| basenames with more than one dot | **1** |
| `README.md` / `index.md` in the same directory | **1** — `docs/` itself |

The one README/index collision accounts for **one** page (`jekyll-readme-index`
maps `README.md` → `index.html`, and `docs/index.md` wants the same output path).
So **64 remain unexplained.**

`docs/` holds 6 `README.md` total, which is nowhere near 64, and only the one in
`docs/` collides.

## What has NOT been tried, and why

The definitive method is to diff the build log's ~3,000 `Writing:` lines against
the staged `.md` list. Not done here: the full log is large enough to be worth a
deliberate pass rather than a side-quest, and the artifact cannot be downloaded
from this container — `productionresultssa15.blob.core.windows.net` is refused by
the egress proxy (`connect_rejected`, organization policy), so
`actions/upload-artifact`'s output is unreachable and `get_job_logs` with
`return_content` is the only route.

## Suggested fix — make the gap a tracked number, not an unknown

Replace the `> 2000` floor with a **coverage comparison**: count staged `.md`,
count rendered `.html`, print both and the difference, and fail if coverage drops
below a recorded floor. That converts an unexplained 65 into a number that cannot
grow silently — which is the same discipline AGENTS.md applies to the
raw-float64 ratchet (baselines drain, never grow).

Do that **before** publishing, since a published site missing 64 pages is worse
than an unpublished one: `nav_exclude`d audit pages are reached only by direct
link, so a missing one 404s with no sidebar entry to reveal it.

## Blast radius if left

Bounded and low today: the site is not published. If published as-is, up to 64
`docs/` pages would be unreachable, and because 2,584 of the 3,082 are
`nav_exclude`d audits reached by link, a missing page is invisible to navigation —
including `AUDIT-DEEP-2026-05.md`, which 19 `computations/*.witness.json`
`"audit_reference"` fields point at.
