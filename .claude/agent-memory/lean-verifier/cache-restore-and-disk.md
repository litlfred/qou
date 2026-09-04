# lean-verifier — the olean cache: restoring it, not destroying it, and disk

Read before any build step, and whenever a cache looks warm but nothing
mathematical compiles. `MEMORY.md` carries the four rules; this file carries the
evidence and the recipes.

## The recipe

Canonical text: `.claude/skills/local/lean-environment-setup.md`
§"PROVEN sandbox build recipe" / §"PRESERVE THE BUILD". **Read it there rather
than reconstructing it**, and derive the branch slug from `lean-toolchain`
(`leanprover/lean4:v4.24.0` → `lake-cache/qou-v4-24-0`) rather than hardcoding.

Order is **RESTORE → verify `lean`-direct → SEED**. A from-source Mathlib build
is the last resort, not the first move: restore is ~2 min against 30–60 min.

Two hazards in the recipe itself:

- **`FETCH_HEAD` is global.** The parts are resolved through it, so a concurrent
  `git fetch` (a background job, a parallel agent) repoints it mid-loop, the
  assembled tarball is truncated, and `tar` fails looking exactly like a corrupt
  cache (cost a session 2026-06-22). Run the restore **serially**, or fetch into
  a private ref: `git fetch --depth=1 origin "$BR:refs/restore-tmp"` and read
  `refs/restore-tmp:$p` in the loop.
- **`trap 'rm -f "$TGZ"' EXIT INT TERM` is load-bearing** — see §Disk.

## TRAP — the restore SKIPS on a cache that is warm-looking and useless

`scripts/lean-cache-restore.sh` no-ops at `>= 2000` mathlib oleans. Measured
2026-09-02: **6990** present and the restore skipped — and every one was
`Mathlib/Tactic/**` or `Mathlib/Lean/**` infrastructure, with `Data`, `Order`
and `Logic` **absent**. Nothing mathematical compiled. The threshold counts
files, not coverage, and this failure mode reads exactly like a warm cache.

`.github/workflows/lean-axiom-guard.yml` gates on the same `-lt 2000` test, so
it neutral-skips on this state in CI too — a gate that silently declines.

**Test for a module you actually import, never a count:**

```sh
test -f .lake/packages/mathlib/.lake/build/lib/lean/Mathlib/Data/Nat/Choose/Basic.olean
```

Force past the skip by concatenating the parts and extracting by hand (the
script's own recipe, minus the guard).

## TRAP — a partial restore is normal; the aggregator is often missing

Seeds capture the import cone QOU needed **at seed time**. Measured coverage on
`lake-cache/qou-v4-24-0-new`: 2970 of Mathlib's 6996 modules — 58 % absent. A
file importing outside that cone fails with `object file … does not exist`, and
**that is a cache gap, not a defect in the file under test** (discriminate
against a rename with the source-tree grep in `v4-24-0-renames.md`).

The aggregator `Mathlib.olean` is frequently among the missing, so a literal
`import Mathlib` errors on an otherwise-fine file. Verify such a file via a
byte-identical-tactics temp copy with **narrowed** imports (a strict subset of
`Mathlib`), and say in the verdict that that is what you did.

## STABLE — a leaked `/tmp/tmp.*` from an earlier session may BE the cache

Check before fetching 1.6 GB you may already have. Measured 2026-09-04 on
`/tmp/tmp.1qCCxhNguJ` (dated 2026-08-16): `tar tzf` listed **11 786** entries,
`tar xzf -C "$ROOT"` succeeded, tree went to **9721** oleans with
`Mathlib.Tactic` present. Saved the whole fetch.

Take two numbers first, because 5.14 GB does not always fit:
`gzip -dc "$f" | wc -c` for the uncompressed size (~2 min, no disk) and
`df -h /`. Net growth on 2026-09-04 was only ~400 MB because most entries
already existed — budget for the full figure anyway.

**Then still reap it.** See §Disk.

## Disk

The restore streams every `lake-oleans.tgz.part` into **one temp file** before
untarring, and nothing reaped it until 2026-08-28: one leaked `/tmp/tmp.*` from
2026-08-15 survived thirteen days and drove the container to **92 K free**,
where the Bash harness cannot write its output capture and *every* command
fails — including the `rm` that would fix it.

`df` reads deceptively: ~252 G nominal at 100 % with ~38 G used, because the
real limit is a per-session quota near 38 G. **"Avail 0, low Used" = allowance
spent, not machine broken.**

Sizes seen: tarball 1.6–2.3 G compressed, 5.14 G uncompressed (2026-09-04).
2026-08-30 the restore ran out at ~2.2 G free and cut off the QOU library files
— mathlib's 3407 oleans still sufficed for a Mathlib-only cone. 2026-09-03 disk
was 2.1 G free: **too little for a re-restore**, so a "restore first" reflex
would have failed and the already-present cache was the right answer.

## The per-paper `.lake` decoy — the second measurement

`MEMORY.md` carries the 2026-09-04 numbers. The same shape 2026-08-29: root
**3407** mathlib + **2275** QOU-library oleans, with `Mathlib.Tactic.olean` and
`Matrix/Trace.olean` present, against a
`content/quantum-observable-universe/lean/.lake/packages/**` tree holding ~726
mathlib and **zero** QOU. (The "6990 mathlib" in an older log was a different
seed, not what that restore produced; 3407 is the QOU-cone partial and it was
sufficient for QOU + `Mathlib.Tactic` files.)

## TRAP — absence of the marker ≠ absence of the restore

`.lake/RESTORED-NO-TRACES` is touched by the recipe, but a cache can be present
without it (measured 2026-09-03: 3470 mathlib oleans, no marker). **Check the
olean count and a specific module, not the marker.** The marker's job is the
other direction: if it *is* there, do not `lake build`.

## TRAP — seeding route depends on how you built

- Built with `lake build` → seed the monolithic branch via
  `scripts/lean-olean-cache-seed.sh`.
- Built `lean`-direct → **no `.trace` files are written**, so that script's
  guard correctly *refuses*. Never force it past: Lake treats untraced oleans as
  stale, rebuilds, and evicts them (bean `02kc`). Preserve lean-direct output as
  a plain `tar` addon orphan branch instead (e.g.
  `lake-cache/qou-v4-24-0-h4-wedderburn-cone`), restored with `tar xzf` and
  consumed via `LEAN_PATH`.

This is the *seeding* face of the eviction hazard `MEMORY.md` records for the
*consuming* side; the two are one mechanism seen from both ends.

## `lake exe cache get` is useless here regardless

`lakecache.blob.core.windows.net` is denied by organization policy — 476
attempts, 476 failures, 2026-09-02. The orphan branch is over GitHub and works.
The blocked host is **not** one the restore ever uses, so "cache get is broken"
never implies "restore is broken" (confirmed 2026-08-29).
