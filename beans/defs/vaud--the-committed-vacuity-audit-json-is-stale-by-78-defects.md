---
# vaud
title: The committed vacuity-audit JSON is stale by 78 defects — it reports 44 where the corpus has 122
status: completed
type: bug
priority: medium
tags:
    - lean
    - vacuity
    - data-integrity
created_at: 2026-08-08T16:20:00Z
updated_at: 2026-08-19T21:17:20Z
---

Found while measuring an unrelated detector change (`vrfw`), and filed
separately so that change stays reviewable.

`docs/audits/2026-06-17-lean-vacuity-axiom-audit.json` is the committed output
of `content/pipeline/lean-vacuity-axiom-audit.ts`. Regenerating it against the
current corpus, **with the detector unmodified**:

| | hits | exempt | defects |
|---|---|---|---|
| committed on `main` | 126 | 82 | **44** |
| regenerated, same detector | 203 | 81 | **122** |

Set-diff on `(file, line, category, decl)`: **96 added, 15 removed.**

The 15 removals are mostly the same declarations under a changed `decl`
spelling — `A5Irrep.reebCasimir_not_injective` → `reebCasimir_not_injective`,
`JonesBirthday.exists_knot` → `exists_knot` — i.e. a namespace-qualification
change in the emitter, not findings that went away. The 96 additions are corpus
drift: real candidates that have landed since the file was last regenerated.

## Why it matters

The committed artifact **understates the corpus by 78 defects**, and it is what
a reader consults. Anyone sizing the vacuity backlog from this file gets 44, and
the true figure is 122. Bean `qou-z3k1`'s method note already learned the
adjacent lesson the hard way — *"Grepping audit prose is not the same as running
the gate"* — and this is the same hazard one layer down: reading the committed
output is not the same as regenerating it.

## Reproduce

```sh
bun run content/pipeline/lean-vacuity-axiom-audit.ts content
git diff --stat docs/audits/2026-06-17-lean-vacuity-axiom-audit.json
```

## What this needs, and why it was not just done

Regenerating is one command. Committing the result is not a mechanical act:

- it moves the reported defect count 44 → 122, which will read as a regression
  unless the drift is stated where the number is;
- 96 candidates arrive uninspected, and the `--check-ledger` CI gate is
  diff-scoped precisely so an inspection backlog does not block unrelated PRs.
  Landing them all at once does not break that gate, but it does hand the
  drain queue a large batch with no triage;
- the file's own name pins it to `2026-06-17`, while the emitter writes to that
  path regardless of date. Whether refreshing means overwriting a dated audit or
  starting a new one is a convention question for whoever owns the artifact.

None of that is hard; all of it is a decision about the audit's contract rather
than a fix. Filed rather than swept into a detector PR.



## RESOLVED 2026-08-19 (verified on current main @ 5b158ef0)
The committed docs/audits/2026-06-17-lean-vacuity-axiom-audit.json is now a FRESH FULL-CORPUS scan: scanned_files=2911, files_flagged=170, total_defects=99, generated 2026-08-15T23:26:52 — regenerated the same day the clobbering root cause (qou-c7jp) was fixed. The stale '44 vs 122' state this bean reported is gone. Root cause fixed + regression-tested under qou-h43i.
