# QA-sidecar refresh — teamwork plan (2026-06-16)

**Goal:** refresh every **stale + missing** QA sidecar across
`content/quantum-observable-universe/` — **2275 `.qa.json` over 34 chapters** —
all axes, **mechanical (script) + agent**.

## ⚠ Critical constraint — the QA pipeline migrated out of qou

The FolioAssistant migration (commits `39fc90f6`, `8e8a2d17`, `ada4c209`) moved
the QA pipeline — `qa-sweep.ts`, `qa-staleness.ts`, `integration-audit.ts`,
`qa-checkers-*.ts`, `qa-criteria-registry.ts` — to the **FolioAssistant** repo.
`content/pipeline/` retains only `qa-agent-drain-queue.ts`, and the
`content/package.json` `qa-*` scripts are now stale references. **The sidecars
themselves still live in qou** (`content/**/*.qa.json`).

→ Every mechanical sweep below runs from a **FolioAssistant-enabled checkout**
(which has the pipeline) with **qou `content/` as the content root**.
*Fallback:* recover the TS pipeline + `folio-assistant/schemas/` from git history
(`git archive <deletion-commit>^ …`), as was done this session for the Python
deps (`qou_substrate`/`pyhecke`) — it works but fights the migration; prefer the
proper env.

## Census (2026-06-16, rough)

- 2275 sidecars, 34 chapters (lane table below).
- Missing-**criterion** is modest: q-usage **5**, proof **68**, bibliography **69**
  uncovered.
- **The real driver is hash-drift staleness** — `source_hashes.{md,ts,lean}` and
  `criteria.<crit>[-1].reviewer.script_hash` drifted from current source. The
  precise per-axis × per-chapter stale counts need `qa-staleness` → **WS0**.

## Axes

| axis | kind | env | representative criteria |
|---|---|---|---|
| one-voice | mechanical | bun | voice-status-leak, voice-emoji, ai-slop, wall-side-correct |
| canonical | mechanical | bun | no-numerology, ck-tiered-not-binary, witness-pinned |
| compute | mechanical | bun (+witness reads) | lp-dual-present, … |
| detangler | mechanical | bun | … |
| q-usage | mechanical | bun | q-usage-archimedean-in-categorical-chapter |
| **proof** | agent + script | **Lean toolchain** | proof-no-conj-propagation, proof-statement-integrity |
| **bibliography** | agent + script | **network** (DOI/screenshots) | bib-cite-resolves |
| **(needs-agent)** | agent | reasoning | voice-statement-no-interpretation, fit-section-chapter, wall-side-statement, wall-side-proof |

## Workstreams

**WS0 — census (gates everything).** Run `qa-staleness` over the paper → the
authoritative per-axis × per-chapter stale/missing table (replaces the rough
census above). 1 agent · FolioAssistant env · ~minutes.

**WS1 — mechanical bulk (the volume; ~5 parallel lanes).** Re-run
`qa-sweep --axis one-voice,canonical,compute,detangler,q-usage` per chapter;
commit per-chapter bulk (batch-audit exception). No Lean/network → fast. Lanes
balanced by sidecar count:

| lane | chapters | ~sidecars |
|---|---|---|
| A | mass-theory | 442 |
| B | quantum-observable-universes, models-of-qous, quantum-universes | 372 |
| C | particle-interactions, observations | 358 |
| D | predicted-spectra, brings-surface, braids-and-knots, climax-volume-mass | 387 |
| E | lifting-and-descent, information-theory, mass-endomorphism, fluid-dynamics, molecular-construction, q-geometric-langlands, appendices + remaining small | ~380 |

Each lane → own branch; chapter-batched PRs ≤ 49 files (Gemini review limit) **or**
one bulk PR per chapter (batch-audit exception). Findings (criticals/majors) are
**recorded, not fixed** here — fixing is `/integration-backlog`.

**WS2 — proof axis (Lean-gated). 1 agent.** Needs the Lean toolchain (lake-cache
restore per `lean-environment-setup.md`). Per-chapter proof-criterion re-sweep,
scoped by WS0. Slower.

**WS3 — bibliography axis (network-gated). 1 agent.** Needs network (DOI
resolution + screenshots). bib-criterion re-sweep + `validate-bib`.

**WS4 — agent-only criteria. 1–2 agents.** The needs-agent criteria
(`fit-section-chapter`, `wall-side-statement/proof`, `voice-statement-no-interpretation`)
require per-block semantic reasoning — not scriptable. Drain per chapter.

## Sequencing

`WS0` first → then `WS1` (5 lanes) ∥ `WS2` ∥ `WS3` ∥ `WS4` in parallel, each
env-gated. WS1 is highest-volume + lowest-cost → start there once WS0 scopes it.

## Coordination protocol

- **Ledger:** `todos/qa-sidecar-refresh-ledger.md` — per-chapter × per-axis
  status; an agent **claims a chapter** (writes a row) before sweeping, because
  sidecars are shared files and concurrent sweeps collide.
- **Branch naming:** `claude/qa-refresh-<lane>-2026-06-16`.
- **Drift hygiene:** exclude shared `content/pipeline/script-sidecars/*.script.json`
  timestamp drift from commits (as in #2319 / #2324) — commit only substantive
  block `.qa.json` changes; revert the script-sidecar churn.
- **CI:** GitHub Actions is billing-blocked → validate locally (`qa-staleness`),
  tag `[skip-ci]`.
- **Merge:** rebase-merge per CLAUDE.md §8; `/prepare-merge` before each merge.

## Execution-routing summary

| workstream | env beyond bun |
|---|---|
| WS0 census, WS1 mechanical | FolioAssistant pipeline (no Lean/network) |
| WS2 proof | + Lean toolchain |
| WS3 bibliography | + network |
| WS4 agent criteria | agent reasoning |

All operate on qou `content/` as the content root; refreshed sidecars commit back
to qou.

---

*Sibling commands (when the pipeline is available): `/integration-audit` (invalidate
+ re-sweep), `/integration-watch` (monitor), `/integration-backlog` (drain findings
→ PRs). This plan is the audit half, decomposed for parallel execution.*
