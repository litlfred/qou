# Integration-watch queue idle-sweep — coordination ledger

Tracks the concurrent PRs working through the
`local/integration-watcher` audit queue (1,074-item backlog) plus
the CI infrastructure fixes that unblock the `validate` gate for all
of them.

## Goal

Land the next slice of audit-queue cleanup with `validate` CI green
again across the repo. PR #773 silently broke `validate` (CLASS-A
banner placement → `SyntaxError` in 42 Python files); every PR
opened since has shown the same red `validate` check and has been
merging through it. PR #775 repairs that, alongside three smaller
witness-pipeline drift fixes inherited from upstream rebase.

## Scope map (snapshot 2026-05-18 20:50 UTC)

| PR | Branch | Touches | Status | Author |
|----|--------|---------|--------|--------|
| **#775** | `claude/i7-stale-probe-rerun-2026-05-18` | I7 stale-probe witnesses (13→0) + 4 CI infra fixes | open, Copilot approved | me (this session) |
| **#776** | `claude/plan-integration-watch-queue-tSPKt` | I12 lake-root mismatches (9 items, 349→341) + 3 skill prefs | open, CI in flight | sibling agent |
| **#774** | `claude/iw-meta-tighten-guarded-off-heuristic` | i3 guarded-off audit script + witness (23→0 false positives) | open, CI in flight | sibling agent |
| **#751** | `claude/workplan-0b-mn-substrate` | Workplan-0b/M_N substrate R&D (Routes A/B/C) | open, exploratory | sibling agent |
| **#761** | `claude/combine-all-open-prs` | Hoefsmit/GP Rust kernel + chirality + audits (combined 10 PRs) | open | sibling agent |

## Classification (skill §2)

| Sibling | Overlap | Dependency | Cherry-pick |
|---------|---------|------------|-------------|
| #776 | none (disjoint audit items: I7 stale-probe vs I12 lake-root) | benefits from #775's CI unblock | none |
| #774 | none (audit script — `guarded_off_audit.py`; disjoint from my files) | benefits from #775's CI unblock | none |
| #751 | none (workplan-0b R&D; touches `probe_workplan_0b_*` scripts I don't touch) | none (my e0 witness already captured PR #758/#763's Q_BETA_MEV migration which is the bridge to this workstream) | none |
| #761 | none (Rust + Hoefsmit kernel) | none | none |

## Coordination actions taken

| Date (UTC) | Action | Link |
|------------|--------|------|
| 2026-05-18 20:50 | Posted intent on #776 — explain CI unblock + ask if they want to merge first | https://github.com/litlfred/qou/pull/776#issuecomment-4482030366 |
| 2026-05-18 20:50 | Posted intent on #774 — explain CI unblock | https://github.com/litlfred/qou/pull/774#issuecomment-4482031682 |

## Cherry-picks

None — all sibling PRs touch disjoint files. The `validate` CI fix
in #775 is universally beneficial but not portable as a cherry-pick
(it's already on the lightest-touch branch and would create a merge
race if duplicated).

## Open items

1. Wait for `validate` CI on #775's latest push (`5c4b8a9fb`) — if
   green, this ledger closes once #775 lands.
2. If a sibling lands first and #775 needs a rebase, the
   docstring-merge + workflow-exclusion changes are mechanical and
   should re-apply cleanly.
3. Witness-pipeline drift detector is exposing a recurring pattern:
   when a PR retargets a witness field (PR #762's contentBlock) or
   migrates a script to use a new symbol (PR #763's Q_BETA_MEV), the
   committed witness and producer script disagree until both are
   updated. Worth a meta-skill note on `local/coordinate.md` §10 —
   but out of scope for #775.
