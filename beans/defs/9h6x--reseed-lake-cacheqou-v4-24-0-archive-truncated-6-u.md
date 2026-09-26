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

### Measured artifact set (2026-08-07) — it is bigger than `.trace`

Resolved empirically with two throwaway `lake init` projects at the pinned
`v4.24.0`, using **olean mtime** as the oracle (the `✔`-line heuristic is
unreliable). A **library-only** package is the right model — mathlib and QOU
are libraries, and an exe-coupled package behaves differently (there,
deleting traces was still a no-op, which is how a first pass mis-concluded
that traces do not matter):

| restored content (lib-only) | `lake build` |
|---|---|
| `lib` + `ir`, everything | **no-op** |
| `lib` + `ir`, `.trace` deleted | REBUILT ← `.trace` **required** |
| `lib` + `ir`, `.hash` deleted | no-op — `.hash` not needed |
| `lib` + `ir/*.setup.json`, no `ir/*.c` | REBUILT ← `ir/*.c` **required** |
| `lib` only, no `ir/` | REBUILT |
| `lib` only, olean+ilean (the old seeder) | REBUILT |

Minimal honoured set: **`.olean`, `.ilean`, `.trace`, `ir/*.c`,
`ir/*.setup.json`.** The `.trace` framing in `02kc` is correct but incomplete —
each module job records three outputs (`o`, `i`, **`c`**), so dropping the `ir/`
C output invalidates the module just as dropping the trace does.

### Where the fix went

**Not** folio-assistant. `folio-assistant/scripts/lake-cache.sh` (`:520`) seeds
with `tar czf - -C "$root" .lake` — the **whole** `.lake` tree — so it cannot
miss an artifact class, and it already refuses to seed below 90% trace
coverage. It is correct as written, and it is what
`lake-cache-refresh.yml`:120–124 actually invokes.

The defect was the qou-local legacy seeder `scripts/lean-olean-cache-seed.sh`,
which hand-picks by extension. Fixed in this branch: `trace` added to the
mathlib ext loop, `ir/{*.c,*.setup.json}` collected, package/paper `find`
expressions widened (and their `-o` alternatives parenthesised — unparenthesised,
`-type f` bound to the last `-name` only), plus a trace-coverage guard mirroring
the service script's. Verified: `bash -n` clean; the guard refuses this
container's 0%-trace tree; and the new set restores to a **no-op** end-to-end
while the old set rebuilds.

**Still open:** the live branch itself is unchanged. Reseeding it needs a real
`lake build` of mathlib at the pinned rev (30–60 min) — the guard now makes a
bad reseed fail loudly instead of publishing silently-useless oleans, but it
does not fix the already-published branch.

**Not a gap — corrected.** An earlier revision of this note called the restored
tree's lack of sources (0 `.lean` outside `build/`, no `.git`, every package)
a second defect. It is not: `folio-assistant/scripts/lake-cache.sh`'s header
states the cache restores *prebuilt `.lake/` artifacts* only, and lake fetches
package sources itself from the manifest. A restore is meant to overlay a tree
where that fetch has already happened. Retracted so the next reader does not
chase it.

## Trap: `lake build QOU` PRUNES `lake-manifest.json` — do not commit it

Observed 2026-08-07 while running the reseed build. `lake build QOU` resolves
only the `QOU` target's dependency cone, then **rewrites**
`content/quantum-observable-universe/lean/lake-manifest.json` with the
unvisited packages removed — here `doc-gen4`, `Cli`, `UnicodeBasic`,
`BibtexQuery`, `MD4Lean` (11 insertions, **51 deletions** of pinned revisions).

Committing that would drop the pins the blueprint / doc-gen4 workflows build
from. It shows up as an innocuous single-file `M` in `git status` after any
targeted build, so the stop-hook "commit your changes" prompt points the wrong
way here. **Revert it** (`git checkout -- <path>`), do not commit, and re-check
after a build finishes — lake may rewrite it again on completion.

Build a superset target (or plain `lake build`) if the manifest must stay
intact.
