---
# qou-h43i
title: lean-vacuity-axiom-audit rewrites the committed corpus audit as a side effect of running the documented per-file gate
status: todo
type: task
created_at: 2026-08-16T13:52:36Z
updated_at: 2026-08-16T13:52:36Z
---


Found while landing #5239, then **reproduced independently** rather than taken
on report.

## Reproduction

`.github/workflows/lean-content-siblings.yml:66` documents this as the gate,
and it is what you run locally to check a PR before pushing:

```sh
bun run content/pipeline/lean-vacuity-axiom-audit.ts <changed .lean files> \
  --quiet --fail-on proof-no-trivial-type-mismatch,lean-import-after-content
```

Run against a single file:

```
scanned_files BEFORE = 2911
gate exit=0
scanned_files AFTER  = 1
ARTIFACT WAS REWRITTEN
```

`docs/audits/2026-06-17-lean-vacuity-axiom-audit.json` — a committed
corpus-wide scan — is overwritten with the results of the one-file run. The
gate **exits 0**. Nothing warns.

## Why it matters

- The gate is diff-scoped **by design**, and correctly so: the workflow
  comments at lines 71-78 explain that a whole-corpus check would couple every
  PR's CI to the global inspection backlog. The scoping is right; writing the
  scoped result over the corpus artifact is not.
- In CI this is harmless — ephemeral checkout, artifact discarded. **Locally it
  silently clobbers a committed 2911-file audit**, and the damage lands in
  `git status` as an unrelated 3741-deletion diff next to the PR's real
  changes, where it is easy to `git add -A` by accident.
- The failure mode is the corpus's recurring one: **a side effect that looks
  exactly like success**. Exit 0, `--quiet`, no message.

## Not the same as a stale artifact

The file is not merely out of date — it is *actively rewritten to be wrong* by
the documented way of checking your own work. A reader of the corrupted file
has no signal: it is well-formed JSON claiming a 1-file scan, and nothing in it
says it was produced by a diff-scoped invocation.

## Disposition (needs an owner ruling on which)

1. **Write only when scanning the whole corpus.** Emit the artifact only when
   invoked without an explicit file list. Smallest change, keeps both uses.
2. **Require an explicit `--emit <path>`.** No implicit write at all; the
   corpus regeneration job passes it. Most explicit, touches the regeneration
   caller.
3. **Write to a path derived from the scope**, e.g. a scoped run writes
   nothing to `docs/audits/` and prints where it would have gone.

(1) is the least disruptive and fixes the reported harm; (2) is the one that
makes the write intentional at every call site, which is the property that was
missing here.

## Next

- [ ] Owner ruling between the three dispositions
- [ ] Implement, and add a regression check that a file-scoped run leaves
      `docs/audits/` untouched
- [ ] Check whether the committed artifact on `main` is currently a full scan
      or already a truncated one from someone's local run
