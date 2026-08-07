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
