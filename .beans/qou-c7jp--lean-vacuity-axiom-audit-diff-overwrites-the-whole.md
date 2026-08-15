---
# qou-c7jp
title: lean-vacuity-axiom-audit --diff overwrites the whole-corpus report with the diff scan
status: todo
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
