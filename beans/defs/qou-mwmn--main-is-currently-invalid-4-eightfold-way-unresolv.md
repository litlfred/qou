---
# qou-mwmn
title: 'main is currently INVALID: 4 eightfold-way unresolved-uses errors — PR #4640 owns the fix'
status: completed
type: task
priority: normal
created_at: 2026-08-07T10:41:28Z
updated_at: 2026-09-13T12:30:26Z
parent: qou-kemt
---

run-validate on the folio-assistant pipeline, 2026-08-07: 4 HARD errors, all in the eightfold-way chapter, all 'Unresolved uses':\n  a2-from-three-strands  -> def:hecke-algebra\n  schur-weyl-eightfold   -> def:hecke-algebra\n  color-su3-from-g2      -> def:octonion-algebra\n  meson-mass-splitting   -> prop:q-deformation-weight-lattice\n\nDO NOT FIX HERE -- draft PR #4640 (copilot/eight-fold) already owns these and has the fuller fix. Its body names them exactly: 'def:hecke-algebra (3 blocks, doesn't exist)', 'def:octonion-algebra does not exist anywhere in the corpus', a prop:/rem: prefix mismatch, and '8 hard validation errors -> 0'. It also fixes the ROOT CAUSE that a point fix would miss: a schema violation where 'lean:' was a bare string instead of { ref: ... } on three blocks, so q-deformation-weight-lattice failed to IMPORT entirely, silently unregistering its label and cascading -- which is why meson-mass-splitting cannot resolve prop:q-deformation-weight-lattice.\n\nACTION: get #4640 reviewed and merged rather than patching main piecemeal. Duplicating its fix would conflict with it.\n\nNOTE FOR THE RECORD: main being invalid is not caught by CI as a blocker today (validate is not gating), which is how it persisted.


## Re-measured 2026-09-13 on MAIN's exact content tree — 0 errors, gate GREEN

```
corpus   : origin/main @ 9510d3d04   (content/ checked out verbatim into the tree)
platform : df28d02  (= .folio-assistant-pin, byte-for-byte)

bun run scripts/run-validate.ts content/quantum-observable-universe
  ℹ [(bibliography)]: no reference registry configured — cites-resolve did not run
  ⚠ [piece-a-corner-removal-obligation]: no Lean declaration yet
✓ Valid — 2 issue(s)                                exit 0, 3m33s wall
```

**Zero errors. Neither issue is one this bean names**, and neither is an error:
one info line about `cites-resolve` (off by design outside `--strict`, documented
at length in `scripts/run-validate.ts`) and one advisory about a lemma with no
Lean declaration yet.

### Why this is a measurement of main and not of a branch

Measured from `claude/clever-goodall-iwc6b9`, so the identity was established
rather than assumed before the number was taken:

- `git diff --name-only` between branch and main over `content/**/*.ts` and
  `content/**/*.md`: **0 files, both directions.** The entire content difference
  is 5 `.lean` files.
- `schemas/`, `scripts/run-validate.ts`, `content/values/`, `content/schema/` —
  validate's own inputs — **identical**.
- `.folio-assistant-pin` identical on both, and the clone is at exactly that SHA.

Then, rather than rest on that, `git checkout origin/main -- content/` was run and
the gate re-executed against main's literal tree; the tree was restored afterwards
(`git status --porcelain` empty, HEAD unmoved at `5d40d4480`).

### The gate was SELFTESTED before the green was believed

2 issues is a large drop from the 27 (2026-08-16) and 36 (2026-08-25) recorded in
`qou-mln9`, and in this repo a collapsing count is more often a detector that
stopped looking than a corpus that got fixed. So `uses-resolve` — the exact rule
both beans turn on — was fired against a known positive first:

```
inject  uses: ["def:selftest-label-that-does-not-exist", ...]  into schur-weyl-eightfold.ts
  ✗ [schur-weyl-eightfold]: Unresolved uses: "def:selftest-label-that-does-not-exist"
✗ Invalid — 3 issue(s)                              exit 1
```

The rule fires, the count moves 2 → 3, and the exit code flips. Reverted from a
backup; tree clean. So the green is a real clean bill, not silence.

### What accounts for the drop 36 → 2

Not mysterious, and mostly already on the record. `.folio-assistant-pin` documents
the 2026-09-07 bump `428ca5c → df28d02` as taking the same corpus from "9 issue(s)"
to "3 issue(s)" by fixing four block schemas that restated `BlockBaseSchema` instead
of extending it (upstream `a117daa`), which retired the "Unknown field" warnings.
The remaining `no Lean declaration yet` advisories drained as Lean landed over the
month. The nine-error `lean_direct_exit_0` enum cascade that `qou-mln9` recorded on
2026-08-25 is gone — PR #5761's fix, or an equivalent, has landed.

### Status left at `todo` deliberately — this is the author's call

Both beans carry an explicit prior deferral ("closing is an owner action") from
earlier agents, and overriding another agent's stated deferral is not mine to do.
The **stated blocking condition is now satisfied**: `qou-mln9` said it would stay
open "until it lands, [because] main stays validate-RED for every branch" — main
is green. Nothing remains to do on either symptom.



## CLOSED 2026-09-13 on author authorisation

The author authorised closing both gate beans in session, against the
measurement above: `main @ 9510d3d04` / platform `df28d02` →
**`✓ Valid — 2 issue(s)`, 0 errors, exit 0**, with `uses-resolve` selftested
against a known positive first. Nothing remains on either symptom.
