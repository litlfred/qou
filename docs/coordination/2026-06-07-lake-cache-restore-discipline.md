# Coordination — Lean build-cache restore/seed discipline (lake-cache/qou-*)

**Date:** 2026-06-07 · **Branch:** `claude/lake-cache-restore-coordination-2026-06-07`
· **Audience:** any session that will run `lake build` / verify `.lean` (proof
work, `lean-proof-review`, `formalizer`, content blocks with `lean.ref`).

This is **preventive coordination**, not an incident report. Prior ledger
mentions of the cache (`1ppq-qbeta.md`, `2026-06-05-integration-backlog-qa.md`)
are post-hoc incident notes; this entry is the standing restore/seed playbook
plus the one known gotcha that silently defeats it.

## Why (this session's evidence)

A multi-day HOMFLY/Borromean tranche (PRs #1792, #1947, #1789, #1784, #1777,
#1790) repeatedly hit a **cold Mathlib cache** in the sandbox — every Lean
verification step was blocked, so `field_simp; ring`-level lemmas had to be
written and merged on "CI will verify" rather than locally checked. **This was
avoidable**: a usable preserved cache exists.

## The cache is CURRENT — restore, do not rebuild

- **Branch:** `lake-cache/qou-v4-24-0` (slug = pinned `lean-toolchain`
  `v4.24.0`; derive with `cut -d: -f2 lean-toolchain | tr -d '\r' | tr . -`).
- **Last reseed:** 2026-06-04 (`d21ef6e748`, "reseed lean cache: qou+mathlib
  oleans @ lean v4.24.0 (incl MassVolDensity §6)").
- **Artifacts:** `lake-oleans.tgz.part00`..`part04` (all 5 present).
- **Verdict:** ready for restore; ~2 min vs ~30+ min cold rebuild.

**Restore (AGENTS.md §"Mathlib cache 403 fallback" Step 0):**
```bash
ROOT=$(git rev-parse --show-toplevel); TGZ=$(mktemp)
SLUG=$(cut -d: -f2 "$ROOT/lean-toolchain" | tr -d '\r' | tr . -)   # v4.24.0 -> v4-24-0
git fetch --depth=1 origin "lake-cache/qou-$SLUG" \
  && git ls-tree --name-only FETCH_HEAD | grep '^lake-oleans\.tgz\.part' | sort \
     | while read -r p; do git show "FETCH_HEAD:$p"; done > "$TGZ" \
  && tar xzf "$TGZ" -C "$ROOT" && echo "restored from lake-cache/qou-$SLUG"
```

## ⚠ KNOWN GOTCHA — the restore can silently fall back to a full cold rebuild

Per `docs/coordination/1ppq-qbeta.md` (flagged to PR #1871): a restore seeded
with a `git config url."file://…".insteadOf` redirect (introduced in #1857)
can make a *restoring* container re-materialise Mathlib **from source** instead
of using the oleans — defeating the whole point. The mitigation is to
**re-apply / normalise the package-URL redirect** (see the checklist).

> **⛔ Do NOT run `lake env true` / `lake update` / `lake exe cache get` to
> "fix" a restore.** `docs/coordination/2026-06-05-integration-backlog-qa.md`
> (now in `formalizer.md §7c`) is explicit: *"never `lake env true` /
> `lake update` / `cache get` — they wipe"* the restored oleans by
> re-resolving the manifest. And `lean-environment-setup.md` §"global
> `insteadOf` … destructive re-clone loop" warns the redirect itself can loop.
> Keep the mitigation to **remote/redirect** fixes only; never the
> manifest-touching commands.

**Restorer checklist (do all before concluding "Lean unavailable"):**
1. Run the Step 0 restore above.
2. If Lake still tries to fetch Mathlib: re-apply the local redirect
   `git config --global url."file:///home/user/mathlib4".insteadOf
   "https://github.com/leanprover-community/mathlib4"` (AGENTS.md
   §"Mathlib cache 403 fallback" Step 2) — or shallow-clone Mathlib locally.
3. Verify via the LSP on a Mathlib-importing file (first query is slow/cold but
   must return real diagnostics, not the timeout sentinel).
4. **Do NOT** declare Lean unavailable until both the restore and the redirect
   have been tried (AGENTS.md STRICT "route, don't give up").

## SEED after a successful build (so the next session restores)

After a clean `lake build`, reseed the branch so the cache stays current —
especially after a Mathlib bump or a large new module.

**Production seed path: bash one-liner OR `lake-cache-refresh.yml`** —
both write the monolithic `lake-cache/qou-v4-24-0` branch in formats
the current fetcher can consume (chunked-tgz or raw `.lake/` tree).
Recipe + slug rules:
[`.claude/skills/local/lean-environment-setup.md` §"PRESERVE THE BUILD"](../../.claude/skills/local/lean-environment-setup.md).
A reseed commit names the toolchain + what changed (e.g. the
`d21ef6e748` "incl MassVolDensity §6" pattern).

**Per-package seed path (PR #1957 producer + PR #1967 consumer): wired
end-to-end.** `scripts/lake-cache-produce.py` writes per-package orphan
branches with per-file `.olean.xz` blobs + a `cache-index.json`
master-index; `scripts/lake-cache-fetch-multi.py` consumes them:

```bash
# Dry-run produce all 9 packages — safe:
./scripts/lake-cache-produce.py
# Push one package to a test branch + fetch it back to verify:
./scripts/lake-cache-produce.py --packages Qq --push --branch-suffix test
./scripts/lake-cache-fetch-multi.py --packages Qq --branch-suffix test
# Push live (cutover from monolithic format):
./scripts/lake-cache-produce.py --push
```

Mathlib gets its own branch (~140 MB after strip + xz, down from ~1.8 GB
raw); small packages (aesop / Qq / batteries / proofwidgets) get tiny
branches. Verified end-to-end 2026-06-07 on Qq: 13 oleans round-tripped
through produce → push → fetch → restore → regen, with .olean / .hash /
.trace files all materialized in place.

Architecture details, strip rationale, and compression head-to-head data:
[`docs/audits/2026-06-07-lake-cache-only-new-content-design.md`](../audits/2026-06-07-lake-cache-only-new-content-design.md).
(The design doc's migration plan still references
`scripts/lake-cache-produce.sh`; the producer is now
`lake-cache-produce.py` since the .sh was deleted as a duplicate in
PR #1967. Tracked for a follow-up doc refresh.)

## Open coordination item

A future Lean-env hardening could **normalise the package URLs in the seed
itself** so restorers never need step 2 (eliminates the gotcha). Tracked here;
owner/`lean-environment-setup` maintainer to decide. Until then, restorers must
run the checklist above. The PR #1957 producer's `cache-index.json` step is a
natural place to add per-package URL normalisation (currently records the
package's git rev + URL as provenance; a normaliser would re-write the local
restorer's package URL to match before lake re-resolves).
