---
# qou-c7jp
title: lean-vacuity-axiom-audit --diff overwrites the whole-corpus report with the diff scan
status: completed
type: bug
created_at: 2026-08-15T23:28:36Z
updated_at: 2026-08-15T23:28:36Z
---


Found while running every CI gate against branch
`claude/fivetwo-level7-ladder-numerators` before proposing a merge.

## What happens

`content/pipeline/lean-vacuity-axiom-audit.ts` writes its report to
`docs/audits/2026-06-17-lean-vacuity-axiom-audit.json` **unconditionally**, including when
invoked in diff mode on a handful of files. Running the gate exactly as
`.github/workflows/lean-content-siblings.yml` does —

```sh
bun run content/pipeline/lean-vacuity-axiom-audit.ts <changed .lean files> \
  --quiet --fail-on proof-no-trivial-type-mismatch,lean-import-after-content
```

— replaced the committed whole-corpus record

```
scanned_files 2765,  files_flagged 169,  total_defects 94,  total_exempt 124
categories: proof-no-self-assuming-projection 46, proof-no-trivial-true 18,
            proof-no-provable-axiom 11, proof-no-unused-hypothesis-rfl 14, …
```

with the 12-file diff scan

```
scanned_files 12,  files_flagged 0,  total_defects 0
categories: {}
```

**a 3,736-line deletion.** Reverted here (`git checkout --`), so nothing was committed.

## Why it matters

The file is the corpus's standing vacuity record and other work reads it. After any
contributor runs the diff gate locally and commits with `git add -A` — which is ordinary
practice and is how it nearly happened here — the record silently reads **"0 defects"**
for the whole corpus. That is worse than a missing report: it is a passing verdict over
94 real defects, in exactly the register this audit exists to guard.

CI itself is not the victim (it does not commit the file), so this will only ever be
introduced by a human or agent running the gate locally, and will look like an unrelated
diff in an unrelated PR.

Same family as the finding already recorded in `qou-agrd`: a check that appears to pass
while protecting nothing. Here the check *works* and damages the record it reads from.

## Fix options

1. **Write only in whole-corpus mode.** Simplest and probably right — a diff scan has no
   business rewriting a corpus-wide artefact.
2. **Write diff runs to a separate path** (e.g. `…-diff.json`), leaving the corpus record
   alone.
3. **Refuse to shrink**: if the new `scanned_files` is far below the recorded one, error
   out rather than write. Guards the general case, not just diff mode.

⚠ Also worth checking whether other `--diff`-capable pipeline scripts share the pattern.
`computations/audits/q0_anchor_consistency_audit.py` likewise rewrote
`q0-anchor-consistency-audit.witness.json` on a read-only `--strict` run (9 insertions,
4 deletions — timestamps and counts, not a clobber, but the same write-on-read shape).

---
**2026-08-15 — FIXED. Option 1 + option 2 together; option 3 not needed.**

`content/pipeline/lean-vacuity-axiom-audit.ts`: the default report path is now reserved
for a **corpus-wide** scan. A partial scan (explicit paths, no `--json`) gates exactly as
before and writes nothing; a caller who names an output with `--json` may write whatever
they scanned.

### The file already carried a scar from the same defect

Above `writeFileSync` there was already a guard, added after

> a stray `--help` replaced a 1961-file / 44-defect / 105-flagged-file audit with all zeros

— and its comment says plainly *"a run that scanned NOTHING must not overwrite a real
audit"*. **The fix was scoped to `files.length === 0`.** A twelve-file scan is not zero, so
the documented CI invocation walked straight past a guard written for precisely this
failure. The new guard is the same sentence one step further out: a run that scanned
*less than the corpus* must not overwrite a corpus record either.

### Also fixed: the summary line lied

It printed the report path unconditionally —

```
docs/audits/2026-06-17-lean-vacuity-axiom-audit.json — scanned 12 .lean, 0 defect …
```

— naming a file it had not written, which is the same confusion in the output that the
write guard prevents on disk. Now prints `(partial scan — no report written)`.

### Verified, all three paths

| invocation | gates | writes |
|---|---|---|
| CI diff (explicit paths, no `--json`) | exit 0 | **nothing** — record untouched |
| partial + `--json /tmp/…` | exit 0 | the named path, 12 files |
| corpus-wide (no args) | exit 0 | the default record, **2906 files** |

The third is the regression that mattered — a guard that also disabled the real scan would
have been worse than the bug.

### ⚠ The corpus record moved, and none of it is this branch's

Refreshing it took `2765 → 2906` scanned, `169 → 170` flagged, `94 → 99` defects. The +5
are two newly flagged files, **both arriving from `main`** —
`QOU/BraidsKnots/nsi_q_deformed_kernel.lean` and `QOU/Machinery/H4Cyclicity.lean`
(`proof-docstring-sorry-mismatch` 1→3, `proof-no-trivial-true` 18→21). **Zero of this
arc's eleven modules is flagged.** Stated here because committing the refresh alongside
the fix would otherwise make the PR look like it introduced five defects.

### Still open, deliberately

`computations/audits/q0_anchor_consistency_audit.py` rewrites its witness on a read-only
`--strict` run. Not a clobber (counts and timestamps, not a truncation) but the same
write-on-read shape, and it was **not** touched here — a separate script, a separate
decision about whether a `--strict` check should be side-effecting at all.
