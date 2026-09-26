---
# qou-wsx3
title: 'Vacuity ledger: 44 of 149 genuine verdicts are stale and 4 name files that no longer exist — at least 4 are demonstrably already fixed'
status: todo
type: task
priority: normal
created_at: 2026-09-12T11:55:14Z
updated_at: 2026-09-12T11:55:55Z
---

## The measurement (2026-09-12)

`docs/audits/lean-vacuity-review-ledger.json` carries **329 entries** over **125 distinct
`.lean` files** — 149 `genuine`, 135 `legit`, 45 `advisory`. The ledger's own design is
that *"a verdict goes stale the moment the file changes"*, keyed on a 12-char
`file_sha`. Recomputing that sha against the working tree:

| genuine entries | count |
|---|---|
| **live** — recorded `file_sha` still matches the file on disk | **101** |
| **stale** — the file changed since the verdict | **44** |
| **file no longer exists** | **4** |

Stale by pattern: `prop-universe-field` 19, `borrowed-name` 7, `zero-placeholder` 6,
`field-projection` 6, `decoy-hypothesis` 3, `docstring-vs-body` 1,
`contradictory-hypotheses` 1, `lean-inhabited-no-hypotheses` 1.

Reproduce: hash each `k.split('::')[0]` with `sha256[:12]` and compare to `file_sha`.

## Why it matters, and the worked case

**At least four of the stale `genuine` entries are demonstrably already fixed**, all in
`content/quantum-observable-universe/mass-theory/knot-mass-formula-unified.lean`:

- `frobeniusCoCasimirTraceFallback` / `proof-docstring-body-mismatch` — the ledger says
  *"DOCSTRING CONTRADICTS BODY … docstring ends 'returns 0 for every n ≥ 6'; the body is
  `(n : R)`"*.
- `trivial_vortex_vacuum_mass` / `proof-vacuous-hypotheses` — *"MACHINE-CHECKED VACUOUS"*,
  at **line 262** of a file that is now shorter than that.
- `descendedMarkov`, `braneTower` / `proof-zero-placeholder` — the `0 * q` stubs.

The file's **own header** records all four as fixed on 2026-09-03 (bean `qou-08zf`, audit
`2026-08-27-unified-knot-mass-class-is-unsatisfiable.md`), including verbatim
*"previously `(n : ℝ)` under a docstring that said `0`"* — which is the
`docstring-vs-body` entry, named and closed.

**This is not a defect in the ledger**; it is the ledger working as designed — a changed
file invalidates its verdict, and `--check-ledger` should be re-seeding those as
`needs-agent`. The hazard is a **reader**, human or agent, who queries the ledger for
`verdict == "genuine"` and treats the result as a live worklist. I did exactly that, and
the first four candidates I picked were all already closed. The staleness check above is
one line and should precede any use of this file as a worklist.

## Next

Re-review the 44 and either refresh the verdict or retire the entry; check whether the 4
missing-file entries correspond to renames (retarget) or deletions (retire). Not started —
this bean records the measurement, not the drain. The drain is a per-entry judgement over
44 files and is **not** a sweep to run unasked.
