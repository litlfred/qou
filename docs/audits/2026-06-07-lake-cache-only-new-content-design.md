# Lake-cache only-new-content design (2026-06-07)

> Design doc — captures the architecture for Lean lake-cache that
> emerges from the 2026-06-07 cache-fetcher PR thread (#1950 / #1953)
> and the author's principle:
>
> > **"Lake cache should only have new content / actually compiled
> > content, not redundant content."**
>
> Applies to **all** package cache branches (mathlib / qou / aesop /
> batteries / ...), not just QOU's.

## Principle

The cache is a **content-addressed olean store** keyed by
`(package, toolchain)`. Each branch stores ONLY what its own package's
elaboration produces. Anything derivable from sources or from other
package branches is regenerated on restore.

## Current state (anti-pattern)

`lake-cache/qou-v4-24-0` (the only populated cache branch on origin as
of 2026-06-07) is a **chunked tarball of the full workspace `.lake/`**.
It bundles mathlib (1.9 GB of oleans) + aesop + batteries + ... + QOU.

Anti-patterns:
- Mathlib oleans shipped on the QOU branch (redundant — should live in
  `lake-cache/mathlib-v4-24-0`)
- Includes `.git/` repos for every dependency (456 MB for mathlib alone)
- Includes `bin/cache` binary (172 MB; not needed for `lake build`)
- Includes `.c` codegen + `.ilean` incremental info + `.hash` + `.trace`
  files (regen-able)
- One monolithic chunked tarball: any change → full re-upload

## Target architecture

### Per-package orphan branches

| Branch | Contents |
|---|---|
| `lake-cache/mathlib-v4-24-0` | Just `.lake/packages/mathlib/.lake/build/lib/**/*.olean` + per-branch master index |
| `lake-cache/qou-v4-24-0` | Just QOU's own outputs (`.lake/build/lib/QOU/**/*.olean`) — currently NOT separated out |
| `lake-cache/aesop-v4-24-0` | aesop oleans |
| `lake-cache/batteries-v4-24-0` | batteries oleans |
| `lake-cache/Qq-v4-24-0` | Qq oleans |
| `lake-cache/proofwidgets-v4-24-0` | proofwidgets oleans |
| `lake-cache/<pkg>-v<tc>` | (one per dep referenced in `lake-manifest.json`) |

CI workflow `lake-cache-refresh.yml` already declares a 4-package
matrix (mathlib / qou / ugb / fred2005) — each matrix entry pushes its
own branch. Currently only `lake-cache/qou-v4-24-0` exists and contains
everything; the proper separation requires:
1. Reseeding mathlib alone to `lake-cache/mathlib-v4-24-0`
2. Reseeding qou alone (just its own outputs) to `lake-cache/qou-v4-24-0`
3. Workflow auto-maintenance going forward

### Per-branch contents (data + metadata + master index)

Each branch stores:

```
.lake/packages/<pkg>/.lake/build/lib/<...>/
   <Module>.olean                             ← the actual cache content
   (no .ilean, .hash, .trace, .c, .json — see below)
cache-index.json                              ← master index (regen recipe)
```

**`cache-index.json` schema** (per branch):

```json
{
  "$schema": "lake-cache-index/v1",
  "package": "mathlib",
  "toolchain": "v4.24.0",
  "source_commit": "<git-sha-of-package's-source-tree>",
  "generated_at": "2026-06-07T03:00:00Z",
  "olean_count": 3019,
  "regen_steps": [
    {"kind": "compute_hashes", "input_glob": "**/*.olean", "output_suffix": ".hash"},
    {"kind": "touch_trace",    "input_glob": "**/*.olean", "output_suffix": ".trace"},
    {"kind": "emit_lake_manifest_stub", "output": "lake-manifest.json", "data": { ... }}
  ],
  "stripped": [
    ".git/", "bin/cache", "ir/*.c", "**/*.ilean",
    "**/*.hash", "**/*.trace", "**/*.json"
  ]
}
```

### What gets stripped

| File | Storage | Regen at restore? |
|---|---:|---|
| `.git/` (mathlib alone: 456 MB) | DROP | No — only used to verify dep source revision; lake-manifest already pins it |
| `bin/cache` (172 MB) | DROP | No — `lake exe cache get` (the binary's purpose) is the broken upstream path |
| `ir/*.c` codegen (~460 MB for mathlib) | DROP | Lazily — re-emitted by `lake build` only if native compile needed |
| `**/*.ilean` incremental info (~300 MB) | DROP | Lazily — only matters for IDE incremental editing, not from-scratch builds |
| `**/*.hash` (9k files, ~few MB) | DROP | YES — `sha256sum *.olean` reconstructs them |
| `**/*.trace` (3k files, ~3 MB) | DROP | YES — `touch <olean>.trace` after restore |
| `**/*.json` lake-internal (3k files, ~50 MB) | DROP most | YES — recompose from `cache-index.json` + olean headers |
| `**/*.olean` | **KEEP** | NO — this IS the cache content |

### Compression (what git already does + what we can add)

Per the 2026-06-07 measurements:
- `.olean` files compress to **27% of raw via gzip** (high redundancy in serialized AST)
- git's pack format already applies zlib + delta compression
- Inter-blob delta compression between related Mathlib oleans is potentially huge

**Open data point**: actual git-pack wire size for the per-file format.
The 2026-06-07 measurement attempt aborted (worktree removed before
`git gc` finished); remeasuring is on the implementation checklist.
Predicted: 2.7 GB working tree → 1.0-1.5 GB pack (similar to gzip ratio
since git's zlib is roughly equivalent to standalone gzip on
incompressible-by-format binary blobs like oleans).

**Should we pre-gzip oleans?** Probably not worth it:
- Git's pack would just store the gzipped bytes as opaque blobs (no
  further compression possible)
- Loses git's delta-between-similar-blobs gain
- Adds gunzip-on-restore step (CPU + complexity)
- Working-tree size goes down but the practically relevant metric (pack
  wire size) does NOT
- EXCEPTION: if we use plain-file blob storage (e.g., GitHub release
  asset instead of orphan branch), pre-gzip wins. See "Alternative
  storage" below.

### What "store one thing and regen rest" looks like

Author's question: *"is any of it quickly renderable from the others so
we can only store one thing?"*

| File class | Derivable from? | Cost |
|---|---|---|
| `.olean` | Source `.lean` files + Lean elaborator | **HOURS** (this is the whole reason for the cache) |
| `.hash` | `.olean` | sha256sum, ~1 sec for 3019 files |
| `.trace` | `.olean` | `touch`, instant |
| `.c` | Lean elaborator with codegen | minutes per package |
| `.ilean` | NOT derivable from `.olean` (separate output of elab) | not regen-able cheaply |
| Mathlib's own source | Mathlib upstream | git clone (already done by lake) |

So the minimal-storage candidate is **just `.olean` files** + a tiny
manifest. Everything else regens in seconds on restore (except `.c` and
`.ilean`, which we skip entirely since they're not needed for from-scratch
builds).

### Restore-time regen script

A ~50-line Python (or bash) step in the fetcher:

```python
# After git archive extracts .lake/packages/<pkg>/.lake/build/lib/**/*.olean:
for olean in glob('.lake/packages/<pkg>/.lake/build/lib/**/*.olean'):
    h = sha256(read_bytes(olean)).hexdigest()[:32]
    write_text(olean + '.hash', h + '\n')
    Path(olean).with_suffix('.olean.trace').touch()
    # Reconstruct the lake-internal .json from cache-index + olean header bytes
```

## Realistic savings (combined)

Compared to the current "strip .git + bin/cache" approach (2.7 GB
working tree, 32,444 blobs):

| Action | Working tree | Blob count | Pack-size (estimated) |
|---|---:|---:|---:|
| Current (per-file, .git + bin stripped) | 2.7 GB | 32,444 | ~1.0-1.5 GB (zlib) |
| + Strip `.c` (ir/) | 2.3 GB | ~29k | ~0.9-1.3 GB |
| + Strip `.ilean` | 2.0 GB | ~26k | ~0.8-1.1 GB |
| + Strip `.hash`, `.trace`, most `.json` (master-index regen) | 1.95 GB | **~3,020** | **~0.7-1.0 GB** |
| + Per-package separation (this branch = just mathlib) | 1.9 GB | ~3,019 | ~0.7-1.0 GB |

Best case: **~1.9 GB tree, ~3k blobs, ~0.7-1.0 GB pack** for the
mathlib branch alone. QOU-only branch becomes **~30 MB / ~30 blobs / few
MB pack**.

10× fewer blobs vs current per-file format means git pack-resolution
goes 10× faster on push + clone-time linking.

## Alternative storage (deferred for now)

Instead of git orphan branches, GitHub Releases assets:
- Single download URL per package (no per-file walk needed)
- Better CDN (releases hosted on a different CDN than git fetch)
- No 100 MB per-blob limit
- Pre-gzipped tarball at producer time = transferred-as-gzipped
- BUT: requires `gh` auth tokens for downloads (anonymous OK for public repos)
- BUT: GitHub Actions UI for releases is more cumbersome to inspect

Recommendation: stick with orphan-branch (already half-built) + per-file
blobs + master-index. Releases is a follow-up optimization if pack wire
size proves problematic.

## Migration plan

Steps (each its own PR):

1. **Land #1950 (chunked-tgz consumer fetcher) + #1953 (per-file
   format support + producer).** Already merged-ready modulo
   in-flight Copilot fixes.
2. **Master-index design doc (this PR).** Reviews architecture before
   any code lands.
3. **Implement per-package + master-index producer.** Rewrite
   `scripts/lake-cache-produce.sh` to:
   - Read `lake-manifest.json` to discover packages
   - For each package: create `lake-cache/<pkg>-<toolchain>` orphan
     branch with just that package's `.olean` files + `cache-index.json`
   - Strip `.git/`, `bin/cache`, `ir/*.c`, `**/*.ilean`, `**/*.hash`,
     `**/*.trace`, redundant `.json`
4. **Implement regen-on-restore in fetcher.** Update
   `scripts/lake-cache-fetch.sh` to:
   - Read `lake-manifest.json` of the current repo
   - For each package: fetch its orphan branch, extract, run regen
     steps from its `cache-index.json`
5. **Reseed all production branches** with the new format. Owner-driven
   (force-push affects everyone).
6. **Deprecate the chunked-tgz format.** Mark the fetcher's
   chunked-tgz path as legacy; remove after a transition period.

## Open questions for the author

1. **Which packages should have cache branches?** Just dependencies
   (mathlib, aesop, batteries, Qq, proofwidgets, plausible,
   importGraph, LeanSearchClient = 8 packages), or also our own
   (qou)? Recommendation: **all 9**, even though qou's branch is
   tiny.
2. **Toolchain bump policy** when `lean-toolchain` rev changes: keep
   old branches (`lake-cache/mathlib-v4-24-0`) or force-delete?
   Recommendation: keep N=2 most-recent per package (the existing
   workflow's cap), prune older ones automatically.
3. **Reservoir fallback** when an orphan branch is empty? Currently
   the action falls through to `lake exe cache get` (Tier 3) which
   403s. With per-package branches, missing one branch means rebuild
   just that package from source. Reasonable.

## Cross-refs

- [PR #1950](https://github.com/litlfred/qou/pull/1950) — agent-side
  chunked-tgz fetcher (consumer)
- [PR #1953](https://github.com/litlfred/qou/pull/1953) — producer +
  dual-format fetcher (consumer extended)
- [`.github/workflows/lake-cache-refresh.yml`](../../.github/workflows/lake-cache-refresh.yml)
  — existing 4-package matrix refresh workflow
- [`.github/actions/lake-cache-restore/action.yml`](../../.github/actions/lake-cache-restore/action.yml)
  — CI-side 3-tier fallback Action
- [`docs/workplans/2026-05-24-lean-cache-strategy.md`](../workplans/2026-05-24-lean-cache-strategy.md)
  — original hybrid-cache workplan
