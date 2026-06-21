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
(AGENTS.md §8) if clean; else record blocker.

**Sweep result: 5 of 7 merged; 2 flagged for author (not safe to blind-merge).**

| PR | branch | status | note |
|---|---|---|---|
| #2039 | workplan-refresh | ✅ merged (rebase) | docs-only |
| #2034 | workplan-strategic-review | ✅ merged (rebase) | docs-only workplan |
| #2055 | witness-isstale-hardening | ✅ merged (squash) | GitHub refused rebase → squash; single logical change |
| #2054 | ci-code-quality-gates | ✅ merged (rebase) | CI gates (=#2028 item 2); 3 narrowed Lean imports low-risk (CI grep-gate green) |
| #2043 | serene-babbage-5xvgde | ✅ merged (rebase) | rebased (1 sidecar conflict), gemini `$`-nits already fixed, validate ✓. ohara1991 seed + adelic prop now on main. **#2043 == serene-babbage** |
| #2030 | quirky-mendel-7osmxc | 🟥 FLAGGED | branch carries 3 merge commits + auto-moved Breit–Wheeler Ch13→Ch9 and "resolved 3 of 4 author-decision edges" — author-gated per detangler discipline (ledger C1). Needs author call. |
| #2059 | keen-feynman-SASjJ | 🟥 FLAGGED | gemini: `proof:holds` w/ unconstrained `holds:Prop` makes the "sorry-free" theorems VACUOUS (instantiable with `True`) — violates §3b-cond; 10 copilot comments; Q_β probe scope-creep. |

### 3. ✅ H₂O angle compute — REDONE with checked trace
Used the Markov trace `tr_M` (not `|v|`) per your correction. **Result
(committed):** lone pair `e⁻=σ₀σ₁σ₀` → `tr_M=hz²+z`; bond `σ` → `tr_M=z`;
so `Δtr=hz²>0` ⇒ `b>0` ⇒ angle **narrows** below tetrahedral — the
q-exact CORRECT sign (prior `|v|` probe got bond>lone → opened to ~140°).
Magnitude `hz≈10.4%` vs observed `4.5%` (same order); exact degrees need
the geometric stiffness `a` — not fitted. Files: `h2o_bond_angle_shift_phi1.py`
+ witness + `ANGLE_H2O_*` in `experimental_constants.py`.
`prop:h2o-bond-angle-shift` already exists on main; this supplies its
missing derivation of the sign of `b`.

### 4. ⏳ PR #2028 item 4 — **D10 done, D4 remaining**
- **D10 ✅** migrate 55 `not_started`→`not_checked` (committed; validate ✓).
- **D4 ⬜** de-hardcode ~25 molecular `.md` literals → experimental-constants /
  `:val` witness-pin (benzene `1.40/1.54/1.34 Å`; LP-dual + barrier tables).
  Per-literal judgment (experimental vs derived) — **the main remaining
  piece**; documented for next pass.
Handover items: 1 (#2003) done · 2 (CI gates)=#2054 **merged** · 3 (=D4) ·
4 (=D10 done) · 5/6 ops/sweep notes consumed.

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
