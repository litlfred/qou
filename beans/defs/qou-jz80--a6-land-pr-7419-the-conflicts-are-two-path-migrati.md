---
# qou-jz80
title: 'A6: land PR #7419 — the conflicts are TWO PATH MIGRATIONS, not a content conflict'
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-10-10T07:03:50Z
updated_at: 2026-10-11T07:00:00Z
parent: qou-3e6w
---

Parent epic `qou-3e6w`.  Mechanical, but it is what stands between the arc's last tranche and the
corpus.

## State, measured 2026-10-10

PR [#7419](https://github.com/litlfred/qou/pull/7419): **open**, 5 commits, 2,131 additions,
6 files, `mergeable_state: **dirty**`, 0 review threads.  Head
`39329828903c4c1a6c7094f9074a8c80cc5d7afa` on `claude/xbot-upper-bound-2026-09-15`.  Base was
`4cbb6d128ea`; `main` is now ~5,056 commits on.

## 🛑 The conflicts are TWO PATH MIGRATIONS, not a content conflict

Do not start by reading diffs of the Lean or the probe — nothing in them is contested.  Both
conflicting files were **moved out from under the branch**:

| branch path | path on `main` now | move |
|---|---|---|
| `.beans/qou-hok7--….md` | `beans/defs/qou-hok7--….md` | `58a1f3231c` — the bean-reorg store move (bean `qou-utbr`) |
| `content/quantum-observable-universe/lean/QOU/BraidKnot/SupergradientCertificate.lean` | `folio/quantum-observable-universe/lean/QOU/BraidKnot/SupergradientCertificate.lean` | the `content/` → `folio/` Lean tree rename |

`computations/deltalambda/*` is **unchanged** on `main`, so the three probe files and the witness
rebase cleanly.

## The bean-file half is already handled

The 167-line append of `5df5d36f943` has been **re-applied to `beans/defs/`** as part of this
arc's 2026-10-10 reorganisation, so that hunk should be **dropped** on rebase rather than
re-resolved — re-applying it would duplicate the section.  Check before resolving: a bean is an
append-only ledger and concurrent appends collide on essentially every landing (`qou-hok7` is one
of the two most contended files in the store).

## Verification owed before merge (there is no CI)

Repo-wide auto-triggers are disabled (`workflow_dispatch`-only), so the agent's own verification
**is** the gate.  For this PR that means:

- **Lean changed** → `lean`-direct exit 0 on `SupergradientCertificate.lean` at its **new** path,
  against its real import cone, plus `#print axioms` on the three added declarations showing no
  `sorryAx`.  Note the file is a **library** file with no `.qa.json` sidecar, so nothing but the
  agent checks it.
- **`computations/` changed** → `scripts/precision-gates.sh --changed`, and re-run the relaxation
  probe to completion (its final `B_allT`, λ scan, `pe0` and the G1-free cut were only partially
  observed before a container restart).
- A Copilot review **does** arrive and is **rationed** — request once, do not re-request after
  every push, and do not read `get_check_runs: total_count: 0` as "no review is coming".

## Already fixed on the branch, do not re-litigate

`rev_e_infinity_g1_bottom_edge_cap_probe.py` was the corpus's **one LOSSY module constant** — a
40-digit literal built while `mp.dps` was set by *another file's* source several lines up, so
reordering the two would have truncated it to 15 digits with no error and no diff.  Fixed at the
producer by pinning `mp.dps = 60` before the literal; `module_const_precision_audit --strict`
LOSSY **1 → 0**, exit 0.  Fixed at the file, **not** by widening a baseline.

## Merge policy

`/prepare-merge` first, rebase-merge (never squash without explicit per-PR permission), and
**explicit owner merge permission** — "looks good" is not it.

## 2026-10-11 — done

PR #7419 merged as a merge commit (`6e6d992da2`): the branch carried merges and the clone is
shallow, so a rebase-merge was not available. Content unchanged by the merge.
