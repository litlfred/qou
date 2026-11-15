---
# qou-8plu
title: 'canonical-mass guard: reach --strict green and wire into CI (2 .md hits + no workflow)'
status: completed
type: task
priority: normal
created_at: 2026-08-08T22:41:51Z
updated_at: 2026-08-09T02:14:09Z
---


Leftover from `qou-efcv` (PR #4826), which triaged the docstring pass and
turned it on by default. Two steps remain, both blocked on a decision rather
than on effort:

## 1. `--strict` is 2 hits short

Both in `docs/precision-goals.md`:

- `:51` — `| **σ_theory(O, N)** … | m_p: 242 ppb (μ-p floor); m_avg: 2.89 % bare → 819 ppm spectral |`
- `:225` — `> … the *bare* categorical value (Family-A Borromean tower, m_p = 965.38 MeV, +2.89% open gap) …`

Neither is stale. Both are the careful bare-vs-anchored distinction the
guardrail asks authors to make, and `:225` explicitly contrasts them with the
live `+1.35 ppb`. So clearing them means **loosening the .md pass**, and that
pass is the guard's primary surface — the 2026-08-01 recurrence was prose.

The obvious loosening does not work: the `.py` pass clears such lines with
`NAMES_THE_GAP`, but the recurrence itself read "m_p misses ~437× / 2.89 %
Vol·ρ gap", which *also* names a gap. Applying that rule to .md would have
missed the exact defect the guard exists for.

Options, none free: (a) allowlist the two lines by exact content, so any edit
re-flags them; (b) an inline `<!-- guard-ok: … -->` marker convention; (c) leave
`--strict` red and use the guard warn-only. Needs a call.

## 2. Nothing runs the guard

No workflow invokes `canonical_mass_status_guard.py`, and repo CI auto-triggers
are disabled (AGENTS.md: `build.yml` is `workflow_dispatch`-only, billing).
There is no `witness-pipeline.yml` in the tree despite AGENTS.md referencing
one. So "wire into CI" has no host today — it wants either a
`workflow_dispatch` job or a pre-commit hook, and per AGENTS.md §"QA is
agent-owned; CI is a backup" the agent-run path is the real gate anyway.

## 2026-08-08 — item 1 done: `--strict` is green (PR #4833)

Resolved by option (a′): a per-LINE, **content-hashed** exemption
(`LINE_EXEMPTIONS`, sha256/12 of the stripped line) rather than any loosening
of the .md pass. Matches how `.qa.json` sidecars and `*.witness.json` pin their
sources — edit the sentence and the exemption lapses, which a path- or
line-number exemption cannot promise, and unlike an `ALLOWLIST_SUBSTR` entry it
does not blind the guard to the rest of the file.

Documented bar for adding one: the line must state the deprecated figure *and*
its correct scope. Both entries qualify ("2.89 % bare", "+2.89% open gap", each
beside the live +1.35 ppb). Two test cases enforce it — the exemptions must
still match live lines, and a mutated line must re-flag.

**Item 2 (CI wiring) remains open** and is unchanged: nothing runs this guard,
`build.yml` is `workflow_dispatch`-only, and there is no `witness-pipeline.yml`
in the tree. Needs either a dispatch job or a pre-commit hook.

## 2026-08-09 — item 2 resolved: hosted in the preflight, not in CI

There is nowhere in CI to wire this. **Every** workflow in `.github/workflows`
is `workflow_dispatch`-only — `build.yml`, `doc-gen4.yml`,
`lean-content-siblings.yml`, `pyhecke-native-wheel.yml`, `witness-staleness.yml`,
`build-lean-mcp.yml`, `lake-cache-refresh.yml` — auto-triggers having been
disabled repo-wide on 2026-06-30 for Actions billing. A new workflow would
never fire on a push and would only *look* like coverage.

So the guard now runs from [`scripts/check-sidecars.sh`](../scripts/check-sidecars.sh),
the documented pre-commit preflight, which is the path agents actually walk
(AGENTS.md §"QA is agent-owned; CI is a backup"). It fires only when the change
touches a covered surface (`computations/**.py`, `content|docs/**.md`), and the
guard is stdlib-only (ast/re/hashlib) so the preflight gains no dependency. The
two regression suites need mpmath and are deliberately left out of the
preflight; they are named in the comment for anyone touching the guard itself.

Verified both directions: a planted stale docstring trips it (⚠ + the hit list,
`action=1`), and the clean tree is silent.

If auto-triggers are ever re-enabled, add a `workflow_dispatch` +
`pull_request` job that runs `python3 computations/canonical_mass_status_guard.py --strict`
plus the two suites — it is a three-line job with no dependencies beyond mpmath.
