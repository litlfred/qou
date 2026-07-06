# Proof-axis 629 fails — all trace to stale `lean-compile-diagnostics.json`

> Discharge-queue artefact (added to PR #1780 mid-session). Companion
> to the §3b-cond catalog and the proof-objects.json staleness audit.

## Headline

| Sidecar criterion | Open fails | Source of "fail" verdict |
|---|---:|---|
| `proof-lean-compiles` | **629** | `docs/audits/lean-compile-diagnostics.json` — **stale (May 27)** |

ALL 629 proof-axis fails reduce to a single criterion (`proof-lean-compiles`) whose evidence is sourced from a stale diagnostics JSON. The fails are not necessarily **current** Lean compile errors — they're whatever errors were caught the last time the diagnostics file was regenerated, which was 7 days ago.

## Why this matters

Sample evidence cited by the criterion:

```
content/quantum-observable-universe/braids-and-knots/reading-a-conditional-linking-weight.lean:71:
  invalid 'import' command, it must be used in the beginning of the file
```

The actual file at HEAD has imports at lines 1-3 (clean). Line 71 is inside a docstring; **there is no import at line 71 in the current source**. The "fail" is stale.

The 483 (of 629) "invalid `import` command" errors all follow this pattern — they're cached evidence from a previous file state.

## Where the stale data lives

| File | Role | Last update |
|---|---|---|
| [`docs/audits/lean-compile-diagnostics.json`](../../docs/audits/lean-compile-diagnostics.json) | Per-file Lean LSP diagnostics dump (396 KB) | `generated_at: 2026-05-27T08:55:11.875Z` |
| [`content/pipeline/script-sidecars/proof-lean-compiles.script.json`](../../content/pipeline/script-sidecars/proof-lean-compiles.script.json) | Script-hash sidecar pointing at the above | `last_run_at: 2026-06-03T18:31:25.384Z` (sweep ran on the stale source) |
| 629× `<block>.qa.json` `criteria.proof-lean-compiles[-1]` entries | Per-block sidecar `fail` records | cached from the May-27 diagnostics |

## Regen path (currently blocked)

Refreshing the diagnostics requires:

1. A working Lean LSP server with an indexed QOU project →
2. A built QOU project (`.lake/build/lib/`) →
3. Built Mathlib oleans →
4. `lake exe cache get` succeeding (currently **403** on every download — see [`infra-lean-cache-host-bypass`](../../.beans/lean-discharge-queue.json))
5. Per-file invocation of `mcp__lean-lsp__lean_diagnostic_messages`
6. Feed results to `bun run content/pipeline/lean-compile-audit.ts --ingest <diagnostics.jsonl>`
7. Sweep the affected sidecars (auto-clears once `lean-compile-diagnostics.json` updates)

**Step 4 is the singular blocker.** Without the Mathlib oleans cache, the QOU project can't be built without a 1-4h Mathlib-from-source build, after which the LSP-driven ingest still has to run per-file across ~700+ `.lean` files.

## Implication for QA-axis triage

The 629 proof-axis fails reported by `qa-sweep` at session-start are NOT all current errors. Some unknown subset:

- May have been fixed in commits since 2026-05-27 (the prose/structure/import positions could have shifted)
- May have new errors that don't appear in the stale data
- The "real" current state is unknowable without a regen

The cleanest interpretation: **all 629 entries are stale until proven otherwise**. Acting on them individually (per-block fix attempts) is mis-prioritised work; the right move is to unblock the cache-host so the diagnostics file can be regenerated.

This is **the canonical example** of the user's 2026-06-03 request "have agents redo stale sidecars witness when idle as part of their skills" (now [PR #1774](https://github.com/litlfred/qou/pull/1774) §0b item 4). The proof axis is currently being mis-served by stale data.

## Counts that ARE current (for reference)

Cross-checked via direct grep on the current `.lean` source:

| Metric | Live grep | Stale sidecar |
|---|---:|---:|
| Files with `sorry` | 241 | (n/a; sidecars don't track this) |
| Raw `sorry` text matches | 491 (good regex `\bsorry\b(?!-)`) / 653 (legacy `\bsorry\b`) | (n/a) |
| Classes with `sorry` in body (§3b-cond) | 194 | (n/a; permanent by design) |
| `axiom` declarations | 77 | (n/a) |

The grep-derived counts don't trace through the stale sidecar pipeline, so they're trustworthy.

## Recommended actions

1. **Do NOT attempt per-block fixes on the 629** until diagnostics regenerates. Pattern-match the cited error to current file content first; expect most cited line numbers to be wrong.
2. **Prioritise `infra-lean-cache-host-bypass`** (queue item, currently blocked on network policy I don't have). Same shape as PR #1755's elan-via-GitHub-releases bypass but for the Mathlib oleans CDN.
3. **Once unblocked**, the diagnostics regen is a one-shot lake-build + per-file lean_diagnostic_messages pass that should run in CI on every PR (currently does not).

## Cross-refs

- [`docs/audits/2026-06-03-lean-axiom-tractability-triage.md`](2026-06-03-lean-axiom-tractability-triage.md) — companion: 77-axiom landscape + cache-host blocker
- [`docs/audits/2026-06-03-proof-objects-json-extractor-broken.md`](2026-06-03-proof-objects-json-extractor-broken.md) — companion: `proof-objects.json` extractor stale 45 days for a different reason
- [`docs/audits/2026-06-03-lean-3b-cond-class-sorries-catalog.md`](2026-06-03-lean-3b-cond-class-sorries-catalog.md) — companion: 202 §3b-cond classes catalog (this PR)
- [PR #1774](https://github.com/litlfred/qou/pull/1774) — the idle-trigger discipline that would target exactly this kind of stale source-of-truth
- [`.beans/lean-discharge-queue.json`](../../.beans/lean-discharge-queue.json) — work queue
