---
# 9h6x
title: 'Reseed lake-cache/qou-v4-24-0: archive truncated (6 uniform 94MB parts, gzip EOF — parts beyond part05 missing); restore yields partial oleans (1649/~2919 mathlib, no ProofWidgets/Plausible pkgs)'
status: in-progress
type: task
priority: normal
created_at: 2026-07-02T17:35:24Z
updated_at: 2026-08-07T00:00:00Z
---

## Verification 2026-08-07 — premise no longer holds; recommend closure

The truncation reported here was fixed by a reseed on **2026-08-07 00:11 UTC**
(`lake-cache/qou-v4-24-0` @ `3068be7b`, *"seed lean cache @ v4-24-0:
lake-oleans.tgz.part17 (fresh f897ebc, incl ZetaValues cone)"*). Re-checked
every claim in the title:

| Claim in title | Status now | Evidence |
|---|---|---|
| "6 uniform 94MB parts" | **false** — 18 parts | `part00`–`part17` |
| "parts beyond part05 missing" | **false** | 17 × 94371840 B + a 42552933 B tail = 1646874213 B (1.53 GB); a short final part is the normal `split` signature, not truncation |
| "gzip EOF" | **false** | streamed all 18 parts through `gzip -t` → **exit 0** (no bytes written to disk) |
| "no ProofWidgets/Plausible pkgs" | **false** | `.lake/packages/` carries `proofwidgets` and `plausible` |
| "1649/~2919 mathlib oleans" | **false** | restore in this container yields **6990** mathlib oleans |

Reproduce the integrity check cheaply (streams from git, no 1.5 GB on disk):

```sh
git fetch --depth=1 origin lake-cache/qou-v4-24-0
for i in $(seq -w 0 17); do git show "FETCH_HEAD:lake-oleans.tgz.part$i"; done | gzip -t
```

Status left `in-progress` for the author to close (agents do not close others'
items). **Not fixed by this reseed:** the archive carries **0 `.trace` files**
against 6990 oleans — measured in this container — so `lake` still treats every
restored olean as stale and evicts it on build. That is bean `02kc`, which
remains the live defect; this bean's truncation premise is resolved.

## Root cause of the trace deficit (`02kc`) — TWO independent blockers

Traced to code on 2026-08-07. Neither blocker alone explains it; both must be
fixed, and fixing only one changes nothing observable.

**Blocker 1 — the artifacts never exist.** `.trace` files are a *lake*
bookkeeping artifact; only `lake build` writes them. The live branch was
hand-seeded from a **lean-direct** (`lean -o`) build, which never produces
them — so there was nothing to seed. `.github/workflows/lake-cache-refresh.yml`
:114 states this outright: *"the live branches were seeded by hand instead"*
(the workflow path itself does run `lake build` at :94–97, so it would have
them). Measured here: `find .lake -name '*.trace'` → **0**, against 6990 oleans.

**Blocker 2 — the seeder drops them anyway.** `scripts/lean-olean-cache-seed.sh`
enumerates artifacts by extension and `trace` is absent from all three sites:

| Line | Code | Missing |
|---|---|---|
| :38 | `for ext in olean ilean; do` | `trace` |
| :57 | `find "$d" -name '*.olean' -o -name '*.ilean'` | `-o -name '*.trace'` |
| :61 | same, under `SEED_PAPER=1` | same |

So even seeding from a real `lake build`, traces would be filtered out.

**Where the fix goes — NOT this repo.** As of `lake-cache-refresh.yml`:120–124
the workflow no longer calls `lean-olean-cache-seed.sh`; it resolves `SVC` from
`scripts/lake-cache.sh` → `folio-assistant/scripts/lake-cache.sh`. The first
does not exist in qou, so **the authoritative seeder lives in
`litlfred/folio-assistant`** and must be fixed there. `lean-olean-cache-seed.sh`
is now a secondary/legacy path.

**Explicitly NOT done here, and why.** No glob was added. Whether lake writes
traces beside the olean in `.lake/build/lib/lean/` or elsewhere under
`.lake/build/` could not be verified — this container has zero traces to
inspect, and the authoritative seeder is in a repo not checked out here. A
guessed `-name '*.trace'` under the wrong directory would silently seed nothing
while *appearing* to fix the bug, which is the failure mode this bean already
cost a month to. Validation needs one `lake build` → seed → restore →
`lake build` cycle to confirm oleans survive.
