# Coordination — QA staleness infra + `/integration-backlog all` drain (#1885)

**Branch:** `claude/dreamy-albattani-RKsjx` · **PR:** [#1885](https://github.com/litlfred/qou/pull/1885)
**Goal:** drain the integration-watcher QA backlog; fix lean-compile-audit staleness (SHA-based).

## Scope map (2026-06-05)

| PR | Branch | Scope | Overlap w/ #1885 | Dep | Cherry-pick |
|----|--------|-------|------------------|-----|-------------|
| **#1885** (this) | `claude/dreamy-albattani-RKsjx` | QA pipeline `.ts` (qa-checkers-extended/voice, qa-sweep, lean-compile-audit); 955 proof sidecars → `n/a`; 25 one-voice `.md` (mba + mechanical) | — | — | — |
| **#1871** | `claude/confident-newton-R8lIx` | M=Vol×Density SU(2)/SO(3) symmetry — `mass_vol_density.py`, `_li_2_q_util.py`, `MassVolDensity.lean`, `binding-manybody-jet-filtration.*`, `sw-period-residue-sum.*`, audit docs | **none** (no shared file; adjacent chapters mass-theory / brings-surface) | none | none |

## Classification (skill §2)
- **#1871:** overlap LOW/none, dependency none, cherry-pick none. Coordination point: #1885's `proof-lean-compiles` change (SHA-staleness → `n/a` for stale/missing cache) governs how #1871's **new Lean blocks** are QA'd. Both PRs billing-blocked.

## Comments posted
- #1871: intent + QA-semantics heads-up — https://github.com/litlfred/qou/pull/1871#issuecomment-4634037427

## #1885 own-PR review triage (skill §5)
- 4 threads (Gemini ×1, Copilot ×3) — all **accepted + fixed** in `657e34dc` (path.resolve + containment/`.lean` guard; hashFile reorder; `$schema` `v1|v2` union). 3 marked outdated; no open actionable threads.

## Escalations (skill §6)
- None. Findings consistent across PRs (shared billing-block diagnosis; no contradictory framing).

## main watch (skill §8)
- `origin/main` +18 since divergence (qbeta / gap-a4 activity). No main landing touches #1885's QA-pipeline files. Rebase deferred to `/prepare-merge`.

## Next non-overlapping task
- #1885 remaining authorized backlog: one-voice **author-notes-pollution** (per-case judgment, .md→.ts §4d) and **detangler** (block split/reorder). **compute axis blocked** (no Python env in this container — producers can't run to emit missing witnesses).
