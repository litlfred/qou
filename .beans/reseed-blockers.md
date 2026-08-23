# reseed-lake-cache-qou-v4-24-0
title: Reseed lake-cache/qou-v4-24-0 — build works; seed blocked by folio-assistant tooling gaps
status: in-progress
type: task
---

## Where it stands (2026-08-23)
- **Build WORKS** on the owner's Mac: `lake exe cache get` + `lake build` →
  a complete tree (2040 QOU-own oleans, 100% traced). The hard part is done.
- **Seed FAILS** on two folio-assistant tooling gaps, both now diagnosed:
  1. `lake-cache.sh seed --push` pushes the whole >2 GiB tarball in ONE pack →
     `remote: fatal: pack exceeds maximum allowed size (2.00 GiB)`. Structural,
     not transient; HTTPS doesn't help (same cap). FIXED here — batched push,
     see `scripts/patches/lake-cache-batched-seed-push.patch` (+ README).
  2. `reseed-lean-cache.sh` Phase 5 verify clones qou on macOS and dies:
     `Illegal byte sequence` on `.beans/*.md` names with math unicode
     (π, σₖ, ś, …). Blocks verify on any Mac; independent of the cache.

## Non-issues ruled out this session
- Not shallow (qou is a complete repo). Not stale refs / gc (pruned, no change).
- The `upload-pack: not our ref` spam is cosmetic — run 1 proceeded past it to
  the actual push; the real failure was always the 2 GiB pack limit.

## The fix + replicability (the owner's ask)
The batched-push fix belongs IN `folio-assistant/scripts/lake-cache.sh` so the
existing `reseed-lean-cache.sh --auto-promote` handles any cache size on any
machine. Authored + syntax-verified from this session, but this session is
scoped to `litlfred/qou` and CANNOT push to folio-assistant. Patch + apply
recipe committed at `scripts/patches/` (branch
claude/lake-cache-reseed-2026-08-21). To upstream: apply → commit → push from
a folio-assistant clone (owner has access), ideally with a
`scripts/tests/lake-cache.test.ts` >2 GiB case.

## Companion follow-ups
- qou `.beans/*.md` filename hygiene: stop minting names with `?` + math
  unicode so a fresh clone checks out on macOS (also un-blocks verify).
- Or harden `reseed-lean-cache.sh` verify to tolerate/skip un-checkout-able
  paths (it is a safety check, not the seed).
