---
# qou-ty1p
title: setup-folio-assistant.sh silently declines to move a dirty platform clone
status: completed
type: bug
priority: normal
tags:
    - platform
    - tooling
    - reorg-2026-10-04
created_at: 2026-09-26T10:33:30Z
updated_at: 2026-11-21T12:30:00Z
parent: qou-n4r9
---

**Measured 2026-09-26.**

## The claim

`scripts/setup-folio-assistant.sh` prints

```
setup-folio-assistant: clone has local changes — leaving its checkout untouched
```

and **exits 0**. So when the platform clone is dirty, setup does not check out
the pinned ref, reports success, and the caller has no signal that the platform
it is about to measure against is not the pinned one.

Observed this session: the clone happened to already be **at** `df28d02`, so
nothing was wrong. That is luck, not a guarantee — the same path with the clone
on `main` would run every gate against a platform 19 days and 101 files of
harness machinery away from the pin, and say `done.`

## Why the clone was dirty, and it is benign

30 modified files, all `content/pipeline/script-sidecars/*.script.json`, plus 4
untracked ones. The diffs are run provenance only:

```
-  "script_hash": "f29b20b77d60",
-  "last_run_at": "2026-08-29T19:39:40.851Z",
+  "script_hash": "18c3500991cd",
+  "last_run_at": "2026-09-12T11:41:49.412Z",
+  "last_run_sha": "df28d02dcd3e3f51aad4690c56b2348ab52efd4c",
```

i.e. a prior session's `qa-sweep` writing back into the platform checkout. The
`last_run_sha` is the pin, so they were produced at the pin. Nothing about them
justifies skipping a checkout.

## Two things worth separating

1. **The guard is right to exist** — clobbering a dirty checkout could destroy
   local platform work. The defect is that it is silent and still exits 0.
2. **A sweep writing into the platform clone at all** is its own question: those
   sidecars are platform files, so qou's QA runs dirty a checkout qou does not
   own, which is what makes the guard fire in the first place. That is the same
   shape as `qou-v0t8` (gate runs dirty sibling witnesses) one repo over.

## Options

1. **Report the mismatch loudly**: after the guard fires, compare
   `git rev-parse HEAD` against `.folio-assistant-pin` and print a warning naming
   both when they differ. Cost: a few lines. Risk: none. Does not change the
   guard's behaviour.
2. **Exit non-zero** when dirty AND off-pin. Cost: a few lines. Risk: could break
   a workflow that tolerates a dirty clone deliberately — unmeasured.
3. **Do nothing** (the default): setup keeps reporting success on an off-pin
   platform, and the "name the platform whenever you quote a count" rule has a
   hole in exactly the tool that is supposed to establish it.

**Recommendation (agent judgement): option 1.** It closes the reporting gap
without touching the guard or anyone's workflow, and the pin file's whole purpose
is that the platform cannot move under qou unnoticed.


## 2026-11-21 — verified on main and closed (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`.

- Option 1 (the recommendation) landed: `scripts/setup-folio-assistant.sh:203-204` now calls `report_off_ref` right after the 'clone has local changes' message, so a dirty, off-pin clone reports the distance instead of saying nothing. The guard itself is unchanged, as option 1 asked.
