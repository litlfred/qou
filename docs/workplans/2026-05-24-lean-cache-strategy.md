# Lean cache strategy — hybrid (Tier 1 actions/cache + Tier 2 orphan-branch family)

**Date.** 2026-05-24
**Status.** Phase A scaffold (composite action + refresh workflow + doc) — see [PR pending].
**Owner directive.** "Can we do something like B but have family of branches w/ fixed prefix and pattern like `lake-cache/paper-stub-module` that lets us select more granular but not making > 20" (2026-05-24).

## What this replaces

The current Lake cache strategy in [`lean_ci.yml`](../../.github/workflows/lean_ci.yml) is monolithic `actions/cache@v4`:

- **One cache entry** keyed on the union-hash of every `lakefile.toml` + `lean-toolchain`
- **Pros**: simple, native to GH Actions, fast wire-up
- **Cons**:
  - 10 GB per-repo cap (Mathlib oleans are ~2 GB each, scaling per toolchain)
  - 7-day inactivity eviction (Mathlib quiet weeks → cold rebuilds = 30+ min)
  - Doesn't help local dev or MCP agents
  - Can't restore JUST one paper package — invalidating any manifest invalidates all

## Hybrid architecture

3-tier fallback chain in [`.github/actions/lake-cache-restore/action.yml`](../../.github/actions/lake-cache-restore/action.yml):

| Tier | Source | Cold-restore time | Durability | Use case |
|---|---|---:|---|---|
| **1** | `actions/cache@v4` | ~30 s | 7-day TTL, 10 GB cap | Warm runner; same-week reuse |
| **2** | `lake-cache/<pkg>-<toolchain>` orphan branch | ~2-3 min | unbounded; git-versioned | Cold runner, Tier 1 evicted, weekly rebuilds |
| **3** | `lake exe cache get` (Mathlib Reservoir) | ~1-2 min | depends on upstream | Mathlib-only fallback |

## Orphan-branch family (Tier 2)

Branch naming pattern: `lake-cache/<package>-<toolchain-slug>`

| Branch | What |
|---|---|
| `lake-cache/mathlib-v4-16-0` | Mathlib oleans (workspace root `.lake/`) |
| `lake-cache/qou-v4-16-0` | QOU paper oleans |
| `lake-cache/ugb-v4-16-0` | UGB paper oleans |
| `lake-cache/fred2005-v4-16-0` | fred2005 paper oleans |

**Granularity wins**:
- A change to `folio/quantum-observable-universe/lean/lakefile.toml` invalidates only `lake-cache/qou-*` — not the other three. Saves ~2-3× cold time on per-paper changes.
- Tier 1 still works at the global level (warm reuse); Tier 2 kicks in only when Tier 1 misses, and selects only the relevant paper.

**Branch cap = ≤ 8** (per owner directive of < 20):
- 4 packages × 2 toolchain versions retained (current + previous, to handle in-flight toolchain bumps).
- Cleanup job in [`lake-cache-refresh.yml`](../../.github/workflows/lake-cache-refresh.yml) prunes anything beyond the keep-2.

**Refresh trigger**: any main commit that touches `lean-toolchain` or any `lakefile.toml`. Manual `workflow_dispatch` available for ad-hoc refresh of a single package.

## How callers use it

Existing workflows (`lean_ci.yml`, `blueprint.yml`) replace their direct `actions/cache@v4` step with:

```yaml
- uses: ./.github/actions/lake-cache-restore
  id: cache
  with:
    package: qou
    lake-root: folio/quantum-observable-universe/lean
    manifest-files: |
      folio/quantum-observable-universe/lean/lakefile.toml
      lean-toolchain
- if: steps.cache.outputs.cache-hit == 'true'
  run: echo "Cache restored from ${{ steps.cache.outputs.source }}"
```

Outputs:
- `cache-hit: true|false`
- `source: actions-cache | orphan-branch | mathlib-upstream | none`

Subsequent `lake build` step is unchanged.

## What this gives us — answer to "works any-which-way"

| Consumer | How they hit the cache |
|---|---|
| **GitHub Actions CI** | Composite action — automatic 3-tier fallback |
| **Local dev** (`lake build` cold start) | `git fetch --depth=1 origin lake-cache/<pkg>-<toolchain>` + extract `.lake/` into Lake root. One-liner; can be wrapped in `scripts/lake-cache-restore.sh` (Phase B). |
| **MCP `paper-assistant`** | Extend the existing `lean_setup` tool to call the same fetch + extract logic (Phase B). |
| **Fresh container / Codespaces** | Same as local dev — orphan branches are durable and clone-friendly. |

## Phase A scope (this PR)

- ✅ Composite action `.github/actions/lake-cache-restore/action.yml`
- ✅ Refresh workflow `.github/workflows/lake-cache-refresh.yml`
- ✅ Cleanup job (8-branch cap)
- ✅ This doc
- ⏳ Wire `lean_ci.yml` to use the composite action (left as a follow-up commit so existing CI keeps working unchanged until the orphan-branch tier is seeded with real cache data)

## Phase B (follow-up)

| Item | Why |
|---|---|
| Wire `lean_ci.yml` + `blueprint.yml` to use the composite action | Existing workflows still use direct `actions/cache@v4`; the composite is unreferenced until they switch over. Defer until orphan branches are seeded so the first PR-use doesn't hit empty Tier-2. |
| Add `scripts/lake-cache-restore.sh` (local dev) | One-liner wrapper for local devs hitting cold starts. |
| Extend MCP `paper-assistant.lean_setup` | Call the same restore logic so an MCP session can warm the cache before `lake build`. |
| Add `lean-toolchain` bump CI gate | When `lean-toolchain` changes on a PR, run the refresh workflow against the PR branch (not main) so the orphan branch is ready by the time the PR merges. |
| LFS for `.lake/` if size becomes a problem | Currently storing `.lake/` as raw git tree. If branches grow > 2 GB per cache, migrate to git-lfs. |

## Why not Option D (MCP+GHCR)

Option D (MCP-managed cache pushed to GitHub Container Registry) was strictly more flexible but required:
- A GHCR write token in CI (extra secret to manage)
- ~2-3 hr setup vs ~30 min for hybrid A+B
- An MCP-server code change

The hybrid A+B answers the "works any-which-way" requirement at a fraction of the complexity. Phase B can layer MCP support on top using the same orphan-branch backend (MCP fetches the same way CI does).

## Cost analysis

| Path | Cost | When |
|---|---|---|
| Warm Tier 1 hit | ~30 s | Same-week PR rebuilds |
| Cold Tier 2 hit | ~2-3 min | After Tier 1 eviction (weekly) or PR on new toolchain |
| Cold Tier 3 hit | ~1-2 min | Mathlib only, no Tier 2 yet |
| Full miss | ~30 min | First build on a new toolchain × package combo |
| Refresh push | ~10-15 min | Once per main commit changing manifests; runs in background |

Estimated effective CI time improvement: **5× faster** on Tier 1 hits, **3× faster** on Tier 2 (vs 30-min full rebuild).
