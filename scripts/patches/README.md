# Out-of-repo patches (folio-assistant)

Fixes to the sibling `litlfred/folio-assistant` platform that were authored
from a `qou`-scoped session (which cannot push to folio-assistant). Stored
here so they are durable and easy to apply/upstream.

## `lake-cache-batched-seed-push.patch`

**Problem.** `folio-assistant/scripts/lake-cache.sh seed --push` puts the
whole `.lake` tarball (Mathlib deps + own oleans) in ONE orphan commit → ONE
pack. GitHub rejects any push whose pack exceeds **2 GiB**
(`remote: fatal: pack exceeds maximum allowed size (2.00 GiB)`), so a real
qou cache (>2 GiB) can never be seeded. The <100 MB `split` handles the
per-BLOB limit, not the per-PACK limit.

**Fix.** Push the parts in batches across incremental commits: the first push
`-f` resets the orphan branch, each later push fast-forwards and ships only
that batch's objects. `LAKE_CACHE_SEED_BATCH` parts × 90 MB per push stays
under the cap (default 15 → ~1.35 GiB). Keeps the full-tree cache format and
the restore contract unchanged.

**Apply to a local folio-assistant clone (no diff paste):**

```sh
git -C ~/space_cats/qou fetch -q origin claude/lake-cache-reseed-2026-08-21
git -C ~/space_cats/qou show \
  origin/claude/lake-cache-reseed-2026-08-21:scripts/patches/lake-cache-batched-seed-push.patch \
  | git -C ~/space_cats/folio-assistant apply -
```

Then re-run the normal reseed:

```sh
cd ~/space_cats/folio-assistant && scripts/reseed-lean-cache.sh \
  --repo ~/space_cats/qou --lake-root content/quantum-observable-universe/lean --auto-promote
```

**To make it permanent for everyone** (folio-assistant has its own push
access; a qou-scoped agent session does not): commit + push it upstream, and
ideally add a `scripts/tests/lake-cache.test.ts` case for a >2 GiB seed.

```sh
cd ~/space_cats/folio-assistant
git commit -am "fix(lake-cache): batch seed push under GitHub's 2 GiB pack limit"
git push
```

## Known companion gap (not fixed here)

`reseed-lean-cache.sh` Phase 5 (verify) clones qou into a temp dir and dies
on macOS with `Illegal byte sequence` for `.beans/*.md` filenames carrying
math unicode (π, σₖ, ś, …). That is a qou filename-hygiene issue + a verify
robustness issue; it blocks the verify phase on macOS regardless of the cache.
Workaround: seed/promote is independent of verify; the build's own
`100% traced` status is the correctness signal.
