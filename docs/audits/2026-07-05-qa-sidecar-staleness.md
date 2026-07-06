# QA Sidecar Staleness Drain — 2026-07-05

Branch: `claude/qa-sidecar-drain-2026-07-05` · PR #3338
Beans: **qsb3** (refresh stale `.qa.json`), **12zf**, **koos**, **ktrw** (block-specific flags).

## Pipeline availability

`scripts/setup-folio-assistant.sh` **succeeded** in this sandbox — the
`litlfred/folio-assistant` platform cloned and symlinked at
`folio-assistant/`. The QA pipeline (`qa-staleness.ts`, `qa-sweep.ts`,
criteria registry) ran normally. **Machine refresh was NOT blocked.**

## Staleness scan (`qa-staleness.ts content/quantum-observable-universe --json`)

| Bucket | Count |
|---|---|
| Blocks scanned | 2704 |
| Fresh (all watched criteria current) | 0 |
| **Stale** (≥1 criterion hash/`script_hash` drifted) | **163** |
| **Missing sidecar** (never audited) | **36** |
| Partial (fresh on present criteria, others never run) | 2505 |

**Root cause of the churn:** the voice checker (`qa-checkers-voice.ts`)
`script_hash` bumped (`d735760f2b64` → `badc8fb0888e`,
`script_commit_sha` `0c745a…` → `e28e45…`) since the last sweep, plus
genuine `.md`/`.lean` content drift on the 163.

## Action taken (this PR)

Refreshed **199 sidecars** = 163 stale (in-place hash + reviewer +
timestamp refresh, plus population of automated criteria absent from the
stale block) + 36 newly created missing sidecars, via
`bun run folio-assistant/content/pipeline/qa-sweep.ts content/quantum-observable-universe`.
The `paths` field (which the pipeline rewrites to the running worktree
dir) was restored to the canonical `../qou/…` form; the committed diff
is otherwise pure hash/reviewer/timestamp refreshes and newly-run
automated-criterion entries.

**Scoped deliberately to the 199 genuinely-stale + missing blocks.** The
2505 `partial` blocks (fresh on the criteria they carry, merely missing
some *never-run* automated criteria) were reverted — populating a fresh
automated-criteria set across the whole corpus is a distinct, much
larger operation (+1.1 M lines) outside qsb3's "refresh stale" scope,
and belongs to a dedicated coverage pass, not this drain.

## Block-specific beans

Dry-run sweep of the three target sections. **Automated `fail`s and
`needs-agent` verdicts that require editing `.ts`/`.md`/`.lean`/`.py`
content are out of this cluster's lane (sidecars only)** — recorded here
for the owning agents.

### 12zf — `particle-interactions/shell-closure-stability`
- **Genuine automated CRITICAL:** `compute-witness-exists` fails at
  `shell-closure-stability.ts:1` — the block manifest declares a
  computation whose witness JSON does not exist. **Fix requires a
  `.ts`/witness change (compute-integration lane), not a sidecar edit.**
- Remainder are `needs-agent` criteria (proof-rater-*, wall-side-*,
  da-*, python-checker set) — agent-review verdicts, no automated fail.
- Block is `partial` (not source-hash stale), so not in the stale-199 set.

### koos — `appendix-surreals/b1-hyperbolic-rows-theorem`
- No automated fails (crit=0/maj=0/min=0). 25 `needs-agent` criteria
  pending agent verdicts. Not source-hash stale.

### ktrw — `appendix-knot-periodic-table/recursive-atom-knot-atlas` (family)
- No automated fails on any of the 4 family blocks.
- **3 family sidecars WERE stale and are refreshed in this PR**
  (`recursive-atom-knot-atlas.qa.json`, `-open-problems.qa.json`,
  `-sdp-uniqueness-wiring.qa.json`).
- Residual `needs-agent` criteria pending agent verdicts.

## Verified vs blocked

- **Verified:** pipeline ran; 199 sidecars refreshed; all valid JSON;
  no worktree-path pollution; only `.qa.json` files touched.
- **Out of lane (flagged, not fixed):** the `shell-closure-stability`
  `compute-witness-exists` critical (needs `.ts`/witness), and all
  `needs-agent` verdicts (agent-review passes on content this cluster
  does not own).
