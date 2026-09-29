---
# qou-gkrt
title: docs site rendered 3017 of 3082 sources — RESOLVED, all 65 were audits/_deprecated/
status: completed
type: bug
created_at: 2026-09-26T19:52:40Z
updated_at: 2026-09-26T20:15:00Z
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

--------

## RESOLVED 2026-09-26 — the 65 are `docs/audits/_deprecated/`, and the per-source step found it on its first run

**Read the body above as the PRE-DIAGNOSIS state.** It says "64 remain
unexplained" and proposes replacing the `> 2000` floor with a coverage
comparison. Both halves are now superseded: the count is **0**, and the gate
that replaced the floor is a different shape from the one proposed.

### The cause

| | |
|---|---|
| `docs/audits/_deprecated/` | **65** `.md` |
| the page-count gap | **65** (3082 sources − 3017 rendered) |

Exactly the 65. **Jekyll skips any underscore-prefixed directory at ANY depth**,
and `docs/_config.yml` listed only `_archive` under `include:`. The top-level
`_archive` was known; a SECOND underscore directory one level down inside
`audits/` was not.

Run [36267907685](https://github.com/litlfred/qou/actions/runs/36267907685)
named it in one line, and the by-directory grouping is why: the step was written
on the reasoning that *"a systematic cause shows up as ONE directory and a
scatter of one-offs does not"*, and every miss came back under one directory.
The four local hypotheses in the body above — output-path collisions, case
collisions, multi-dot basenames, README/index contention — were all ruled out
and none of them was the cause. **A page count could not have produced this
diagnosis; a per-source list grouped by directory produced it on its first run.**

### Whether to render them was the corpus's call, not mine

`docs/audits/_deprecated/README.md` states the intent in its own words: the
directory *"keeps the documents discoverable for archaeology while removing them
from the top-level `docs/audits/` list"*. That is `nav_exclude`, **not** "do not
render" — identical to the argument for `_archive` — and **13** files reference
paths under it. So `_deprecated` is now in `include:`, and it was already
`nav_exclude: true`: `front_matter()` keys that on `parts[0] == "audits"`, which
these paths are, verified by CALLING it rather than by reading it.

### The gate is `--max-missing 0`, NOT the floor this bean proposed

The body above asks for "a recorded floor". That is the weaker instrument and the
measurement is what showed it: **a floor on `covered` RISES when documents are
added**, so a newly-added source that renders to nothing slips straight past it.
A cap on MISSES does not. `--floor` exists and is deliberately not passed.

The `> 2500` catastrophe floor stays, so a collapsed build still fails at the
cheap check before the expensive one.

### Verified, not assumed

Run [36268479821](https://github.com/litlfred/qou/actions/runs/36268479821), the
coverage step's own output:

    staged .md sources : 3082
    covered by a page  : 3082
    NOT covered        : 0
    total .html in site: 3082

All 7 live steps green; `Publish to gh-pages/docs` correctly skipped
(`publish: false`). `docs/index.md`'s 2,584 audits figure needed no correction —
2,519 + 65 = 2,584, so `_deprecated` was always inside it; only the line naming
where those 65 live was missing.

### Completing this bean is legitimate under §13a

AGENTS.md §13a forbids closing a bean whose subject is an **open conjecture**.
This one's subject is a build-coverage defect: cause identified, fix landed,
invariant asserted in CI at 0. No mathematics is open behind it.
