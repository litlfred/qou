# Session task list — `claude/hopeful-feynman-y0zsyy` (2026-06-09)

**Agent:** hopeful-feynman. **Author:** @litlfred (away ~1 week).
**Why this doc:** author reported "lots of failed agents today" and asked
for an immediate PR documenting exactly what is being worked, so progress
is durable and visible even if this session dies mid-task.

This file is the **live source of truth** for this session. Status markers:
`⬜ todo` · `⏳ in-progress` · `✅ done` · `🟥 blocked` · `⏭️ deferred`.

---

## Tasks

### 1. ⏳ Open PR + this tracking doc
First commit of the session. Durable visibility per author request.

### 2. ⬜ `auto /prepare-merge` sweep
Targets (author, two messages): **#2043, #2054, #2030, #2055, #2039, #2059**
+ branch **`claude/serene-babbage-5xvgde`**.
Per session-handover.md §1, author granted standing merge permission
("auto /prepare-merge all open PRs IMMEDIATELY", 2026-06-09).
Per PR target: rebase onto main → resolve review threads → re-check CI →
rebase-merge (CLAUDE.md §8 default) if clean; else report blocker here.

| PR / branch | state | mergeable | CI | action | status |
|---|---|---|---|---|---|
| #2043 | — | — | — | — | ⬜ |
| #2054 | — | — | — | — | ⬜ |
| #2030 | — | — | — | — | ⬜ |
| #2055 | — | — | — | — | ⬜ |
| #2039 | — | — | — | — | ⬜ |
| #2059 | — | — | — | — | ⬜ |
| `claude/serene-babbage-5xvgde` | — | — | — | — | ⬜ |

### 3. ⬜ H₂O angle compute — REDO with checked trace
Prior agent's H₂O `a,b`-from-Φ₁ work was **never committed** (working tree
clean, branch 0 ahead of main → lost). Restart.
**Author correction (key):** do **not** use `|v|` (absolute value loses
structure). Use the (checked) **trace** `tr(v)` / `\check{tr}(v)` so the
extra structure is retained. Re-derive the angular `a,b` with the
trace-based weight, emit a witness, report tiered (derivation vs
near-match) — honestly.

### 4. ⬜ PR #2028 handover — do **item 4**, review rest for status
Doc: `docs/handover/2026-06-09-affectionate-hopper-handover.md` (on branch
`claude/handover-2026-06-09`). **Item 4 (§3)** = WS-B de-hardcode molecular
literals + migrate ~55 `not_started`→`not_checked`. Also review items
1/2/3/5/6 and record their status.

### 5. ⬜ Review completion of `session-handover.md`
Verify which items are done: §1 (merge #2024 + #2011), §2 (tier-3 bib seed
`ohara1991`), §3 backlog, §4 context, §5 ops notes. Record findings.

---

## Environment notes (from prior handovers — confirmed this session)
- **Lean:** elan release server firewalled (`release.lean-lang.org` parse
  error at SessionStart). Restore oleans from `lake-cache/qou-v4-24-0`.
- **Python:** sandbox missing numpy/cvxpy/pyhecke by default; `pip` reaches
  PyPI, so install on demand (prior agent confirmed this works).
- **git cwd:** `content/` is its own Bun package — run pipeline scripts as
  `cd content && bun run pipeline/<x>.ts`.
