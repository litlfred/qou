---
# qou-aq9i
title: '[TOOLS T11] Reconcile and retire 8 forked scripts, 3 forked pipeline modules and lake-cache-refresh.yml'
status: todo
type: feature
priority: normal
tags:
    - migration
    - tools
created_at: 2026-10-04T16:35:45Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-k3er
---

From the TOOLS migration analysis (2026-10-04), story T11. Full report: docs/audits/2026-10-04-workplan-and-migration/TOOLS_report.md.

| T11 | Reconcile and retire 8 forked scripts, 3 forked pipeline modules and `lake-cache-refresh.yml` | each qou-only delta is either upstreamed or recorded as qou-specific; afterwards qou calls the f-a path | M | — |

Owner hard rule: no math or physics content is changed. Done-when must include the content-parity check.


## 2026-10-04 (session_01NdDGeP1SyShmoUssLuRZ91): ledger done; retirement mostly needs platform PRs first
Ledgers: docs/audits/2026-10-04-workplan-and-migration/T11_fork_deltas_{scripts,pipeline}.tsv.
- Done: qa-agent-drain-queue fork retired to fsh-guts (it was broken; the platform copy runs on qou). Fixed lean_leanpath (content/ → folio/) and install-beans (`beans version`).
- KEY FINDING: the platform's lean-build-bg.sh, setup-lean-toolchain.sh and lib/lean-env.sh are old, un-generalised copies of the qou scripts (/tmp/qou-* names, folio/quantum-observable-universe/lean; REPO_ROOT resolves to cat-harness/, which has no lean-toolchain). Retiring them needs a platform PR that absorbs the qou changes and makes the paths configurable. qou is strictly ahead on setup-lean-toolchain.
- Upstream deltas (platform PRs): install-beans (absolute GOBIN, BEANS_BIN_DIR, smoke test); lean-build-bg (no-trace restored-cache guard qou-r13s, has-curl check); lean-env (merge both function sets, read LEAN_DIR from env, fix the `python -c '$config'` quoting); qa-agent-entry (evidence required for fail/warn; lean + lean_statement in the field hash); refresh-authors-note (lean-coverage.json witness).
- Owner-gated: language-trap-audit and qa-agent-entry switch the verdict location from sibling .qa.json to test/results (one-way); git config --global vs --local for the mathlib insteadOf.
- HAZARD: lake-cache-refresh.yml cleanup (both repos) keeps the newest 2 lake-cache/<pkg>-* by date and would delete 7 of the 9 live qou cache branches, including qou-v4-24-0, if a push trigger is armed. Dormant today (dispatch-only).
- Remaining qou bugs, not fixed here: session-start-coord-sweep has an unguarded flock under set -e, points to an archived STATUS.md, and uses '4b' twice; refresh-authors-note write mode succeeds on a missing pattern; build-pdf callers point at ../folio-assistant/scripts/split-pdf-by-chapter.py, which does not exist.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.


## 2026-11-21 — status check (bean drain wave 1, cat-harness-migr)

Session: https://claude.ai/code/session_01Qmmkt7b8yRZEmMY5Qwa33W. Checked against `origin/main` `2ae54ab4010`. Status unchanged.

- Not started. This story is owner-gated (AGENTS.md 'ask the owner before changing things') and needs work in a platform repo as well as qou, so it was not started in the wave-1 drain.
