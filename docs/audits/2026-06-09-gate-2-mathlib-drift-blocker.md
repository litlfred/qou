# Gate #2 (lean-compile-diagnostics regen) — scope hit Mathlib drift wall

**Date:** 2026-06-09
**Status:** Gate #2 helper staged + run; full regen blocked by Mathlib API drift in QOU Lake-tree library (separate scope).
**Branch:** `claude/lean-compile-diagnostics-regen-2026-06-09` (PR #2060).
**Cross-refs:**
[`scripts/lean-compile-diagnostics-regen-helper.py`](../../scripts/lean-compile-diagnostics-regen-helper.py),
[`content/pipeline/lean-compile-audit.ts`](../../content/pipeline/lean-compile-audit.ts),
queue item `lean-compile-diagnostics-regen` in `todos/lean-discharge-queue.json`.

---

## What Gate #2 was supposed to do

Per the `lean-compile-diagnostics-regen` queue item (priority `high`), the
`proof-lean-compiles` QA criterion sources its evidence from
`docs/audits/lean-compile-diagnostics.json`, which has been stale since
2026-05-27. **All 629 currently-open proof-axis fails reduce to this stale
source.** Regenerating the file would clear the stale fails in one sweep
and surface any *real* fails as fresh actionable items.

The plan (per the queue item):
1. `lake build QOU` (~1–3 hrs from source, cached ~min with `lake-cache-fetch.sh`)
2. Loop `mcp__lean-lsp__lean_diagnostic_messages` over every `.lean` file with
   sibling `.ts` under `content/quantum-observable-universe/`
3. Feed results as JSONL to `bun run content/pipeline/lean-compile-audit.ts --ingest`
4. `bun run content/pipeline/qa-sweep.ts content/quantum-observable-universe --only proof-lean-compiles`

## What this session built

A helper script at
[`scripts/lean-compile-diagnostics-regen-helper.py`](../../scripts/lean-compile-diagnostics-regen-helper.py)
that converts a lake build log to the JSONL format expected by
`lean-compile-audit.ts --ingest`. Two modes:

- `--all-clean` — for the lake-build-green case (1041 content-block files →
  1041 empty-diagnostic JSONL entries → clear all 629 stale fails)
- `--from-lake-log <log>` — for the lake-build-broken case (parse per-file
  errors out of lake stdout; assign empty diagnostics to the remainder)

The helper is tested and idempotent. It is intentionally a *thin* shim
between lake's output and the audit script — the audit pipeline owns the
schema (`lean-compile-diagnostics/v2`) and the staleness logic.

## Why the regen didn't land

`lake build QOU` against current `main` (rebased; rev
`c9fae0854d`) **fails** with `EXIT=1`:

- **340 errors across 78 unique files** in the QOU Lake-tree library
  (`content/quantum-observable-universe/lean/QOU/*.lean`).
- Error families:
  - `bad import 'Mathlib.Algebra.BigOperators.Basic'` — Mathlib API
    drift (the module was relocated; the import needs updating to
    `Mathlib.Algebra.BigOperators.<NewLocation>`)
  - `unexpected token 'λ'` — Lean parser change (use `fun` or `λ` was
    forbidden in a specific context; 20+ Lean v4.24.0 repair commits on
    main touch this pattern)
  - `failed to synthesize` — typeclass-resolution failures after Mathlib
    structural changes
  - `motive is not type correct` — `rewrite` failures, possibly from
    `LinearOrderedField` deprecation
  - `unsolved goals` — tactic changes (`norm_num`, `decide`, etc.)

These are part of the **Lean v4.24.0 repair surge** that's still
in flight on `main` (per the workplan agent's earlier triage:
"20+ Lean fix commits 2026-06-08, PR #2001/#2024 land repairs;
`scripts/lake-cache-fetch.sh` closes Gate #1"). The toolchain bump
is complete (`lean-toolchain` reads `leanprover/lean4:v4.24.0`), but
the Mathlib-side imports + tactic invocations need per-file fixes.

## Why `--from-lake-log` mode didn't extract content-block diagnostics

The 78 broken files all live under the QOU Lake-tree library path
(`content/quantum-observable-universe/lean/QOU/...`); lake reports
them with the Lake-tree-relative path `QOU/MathlibExt/SDPEmptyConstraints.lean`,
not the repo-relative path the QA pipeline tracks.

The 1041 content-block `.lean` files (sibling-of-`.ts` under
`content/quantum-observable-universe/<chapter>/<block>.lean`) are NOT
in the Lake-tree, and lake didn't emit diagnostics for them in this
run. Whether they compile is a separate question that requires
per-file LSP probing.

Net result: the helper's `--from-lake-log` mode correctly extracted
**0 diagnostics for QA-tracked files** (none of the 78 broken Lake-tree
files map to QA-tracked content-block paths), which is honest but
not useful for clearing the 629 stale fails.

## Path forward (two-step)

**Step A — fix the Mathlib drift (separate branch).** Update the 78
broken files' imports + tactic calls to match current Mathlib. Estimated
1–3 sessions; needs per-error triage + possibly a Mathlib version pin
review (lakefile.toml currently pins `mathlib` at
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`). This is the Lean v4.24.0
repair surge that's already underway — PR #2001/#2024 touched some of it;
the remaining 78-file slice needs its own PR.

**Step B — run Gate #2 regen.** After Step A makes `lake build QOU`
green, EITHER:
- Run the helper with `--all-clean` → 1041 empty-diagnostic entries →
  clear 629 stale fails in one sweep, OR
- Per-file LSP probing via `mcp__lean-lsp__lean_diagnostic_messages`
  to capture any residual content-block-specific fails (1041 calls,
  ~1.5h serial; more honest but heavier).

The helper script is staged on this branch (`scripts/lean-compile-diagnostics-regen-helper.py`)
for whichever agent picks up Step B.

## This PR's contribution

PR #2060 lands:
- The helper script (idempotent, tested both modes, exits cleanly)
- This audit doc explaining what's blocking Gate #2 closure
- A clear handoff for Step A + Step B

It does NOT land a regenerated `lean-compile-diagnostics.json` — that's
deferred until Step A clears the Mathlib drift.

## Follow-up todo entry

Adding to `todos/lean-discharge-queue.json` after this PR:

```json
{
  "id": "lean-mathlib-drift-fix-2026-06-09",
  "summary": "Fix Mathlib API drift in 78 QOU Lake-tree files (Lean v4.24.0 repair surge tail)",
  "priority": "high",
  "blocks": ["lean-compile-diagnostics-regen"],
  "data": {
    "error_count": 340,
    "file_count": 78,
    "error_families": ["bad import 'Mathlib.Algebra.BigOperators.Basic'", "unexpected token 'λ'", "failed to synthesize", "motive is not type correct"],
    "log_artifact": "/tmp/lake-build-full.log (ephemeral; regenerate via `lake build QOU`)"
  }
}
```
