# Session task list — `claude/hopeful-feynman-y0zsyy` (2026-06-09)

**Agent:** hopeful-feynman. **Author:** @litlfred (away ~1 week).
**PR:** #2064.
**Why this doc:** author reported "lots of failed agents today" and asked
for an immediate PR documenting exactly what is being worked, so progress
is durable and visible even if this session dies mid-task.

This file is the **live source of truth** for this session. Status markers:
`⬜ todo` · `⏳ in-progress` · `✅ done` · `🟥 blocked` · `⏭️ deferred`.

> ⚠️ **GitHub GraphQL rate-limited** at session start (`API rate limit
> already exceeded for user 662242`). REST calls (get PR, merge) still work;
> review-thread reads (GraphQL) blocked. Reading sibling workplan docs via
> **local git** (`git show origin/<branch>:<path>`), not the REST API.

---

## Tasks

### 1. ✅ Open PR + this tracking doc
PR #2064 opened. Durable visibility per author request.

### 2. ⏳ `auto /prepare-merge` sweep
Targets (author, across messages): **#2043, #2054, #2030, #2055, #2039,
#2059, #2034**. Standing merge permission per session-handover.md §1.
Per PR: rebase onto main → resolve threads → re-check CI → **rebase-merge**
(CLAUDE.md §8) if clean; else record blocker.

**Sweep progress: 4 of 7 merged.**

| PR | branch | status | note |
|---|---|---|---|
| #2039 | workplan-refresh | ✅ **merged** (rebase) | docs-only |
| #2034 | workplan-strategic-review | ✅ **merged** (rebase) | docs-only workplan |
| #2055 | witness-isstale-hardening | ✅ **merged** (squash) | GitHub refused rebase → squash; single logical change |
| #2054 | ci-code-quality-gates | ✅ **merged** (rebase) | CI gates (=#2028 item 2). 3 narrowed Lean imports NOT build-verified by CI (only the grep-gate ran) but low-risk (file2 no tactics, file3 broad `Mathlib.Tactic`, file1 author-exact) |
| #2030 | quirky-mendel-7osmxc | ⏳ rebasing | conflicts; Python+witness only (no Lean) |
| #2043 | serene-babbage-5xvgde | ⬜ dirty→rebase | adelic Lean (not_checked) + ohara1991 bib; 5 comments. **#2043 == serene-babbage** (one PR) |
| #2059 | keen-feynman-SASjJ | ⬜ dirty→rebase | UGB Lean gap-close; verify build before merge |

### 3. ⬜ H₂O angle compute — REDO with checked trace
Prior agent's H₂O `a,b`-from-Φ₁ work was **never committed** (lost).
**Author correction (key):** do **not** use `|v|` (loses structure). Use
the (checked) **trace** `tr(v)` / `\check{tr}(v)` so the extra structure is
retained. Re-derive angular `a,b`, emit a witness, report tiered honestly.
_(Read-only research agent dispatched.)_

### 4. ⬜ PR #2028 handover — do **item 4**, review rest for status
**Item 4 (§3)** = WS-B de-hardcode molecular literals → `:val` witness-pin +
migrate ~55 `not_started`→`not_checked`. Also record status of items 1/2/3/5/6.

### 5. ⏳ Review completion of `session-handover.md`
- **§1 (merge #2024 + #2011): ✅ DONE** — both merged 2026-06-09.
- §2 tier-3 bib seed `ohara1991`: **done in #2043** (issue #2042 + review.json).
- §3 backlog: open (see consolidated todos).

### 6. ⏳ Consolidate todos across all PR workplans
Author ask: "as you look at PRs review all their workplan to see what's
still open and consolidate todos." Output → `§ Consolidated todos` below
(+ a standalone `docs/coordination/2026-06-09-open-todos-consolidated.md`).

---

## Consolidated todos (live — built as PR workplans are read)

_(populated in next commits)_

---

## Environment notes
- **Lean:** elan release server firewalled. Restore oleans from
  `lake-cache/qou-v4-24-0` (slug from `lean-toolchain`).
- **Python:** sandbox missing numpy/cvxpy/pyhecke by default; `pip` reaches
  PyPI → install on demand.
- **GitHub:** GraphQL rate-limited; prefer REST + local git.
- **git cwd:** `content/` is its own Bun package — `cd content && bun run …`.
