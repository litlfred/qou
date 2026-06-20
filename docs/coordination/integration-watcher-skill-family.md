# Integration-watcher skill family — coordination ledger

Tracks the cluster of in-flight PRs that touch the
`local/integration-watcher` parent skill, its three (now four)
children, and the routing / role tables.

## Goal

Land a coherent integration-watcher skill family on `main` with
consistent conventions across children:

1. Spawned-PR branch naming (`claude/iw-<TYPE>-<DESCRIPTIVE-STUB>`)
2. Auto-rebase spawned PRs when `origin/main` moves
3. Derivation-completion detection (§3a) + removal-over-banner
   policy (§3b) for upstream-superseding events
4. Children stay slim slot-fillers; shared mechanics in the parent

## Scope map (snapshot 2026-05-18)

| PR | Branch | Touches | Status | Author |
|----|--------|---------|--------|--------|
| **#722** | `claude/iw-meta-branch-naming` | parent §5j step 2 | open, Copilot+Gemini reviewed, fixes pushed | me (this session) |
| **#726** | `claude/iw-meta-rebase-spawned-prs` | parent §4g + §5g step 7 | open, Copilot+Gemini reviewed, 6-bug fix pushed `d0ca5d46e` | me (this session) |
| **#724** | `claude/integration-watcher-on-derivation` | parent §3a + §3b | open | sibling agent |
| **#706** | `claude/detangler-integration-watcher-afdFI` | new `local/detangler-integration-watcher.md` + AGENTS.md routing | open | sibling agent |
| **#694** | `claude/canonical-watcher-skill-UaWnQ` | `scientific-accuracy.md` §4b + baseline audit doc | open (less overlap) | sibling agent |
| **#703** | (merged) | parent skill refactor + 3 children + AGENTS.md routing | landed `260522a6` | sibling agent |

## Classification (skill §2)

| Sibling | Overlap | Dependency | Cherry-pick |
|---------|---------|------------|-------------|
| #724    | parent §3 area (mine: §4g/§5g/§5j) — **different sections, line-number drift only** | none | candidate: §3a/§3b directly applies to `lem:nucleon-mass-splitting` removal in #696; my D3 work already followed this pattern |
| #706    | child watcher — inherits parent conventions from #722, #726 | depends on parent skill conventions | none |
| #694    | sibling skill (canonical-watcher §4b) — orthogonal | none | none |

## Coordination actions taken

| Date (UTC) | Action | Link |
|------------|--------|------|
| 2026-05-18 | Posted intent on #724 noting different-section overlap + suggested merge order #724 → #722 → #726 | [comment](https://github.com/litlfred/qou/pull/724#issuecomment-4478784391) |
| 2026-05-18 | Posted intent on #706 noting inheritance of #722 branch-naming + #726 auto-rebase | [comment](https://github.com/litlfred/qou/pull/706#issuecomment-4478785510) |
| 2026-05-18 | Fixed 6 Copilot/Gemini bugs on #726 rebase-recipe (line-by-line accept) | [commit `d0ca5d46e`](https://github.com/litlfred/qou/commit/d0ca5d46e) |
| 2026-05-18 | Fixed 2 Copilot comments on #722 (sibling-naming generalisation, table-in-list rendering) | [commit `e538ebbb4`](https://github.com/litlfred/qou/commit/e538ebbb4) |

## Suggested merge order

1. **#724** (parent §3a/3b, deepest text additions) — establishes
   derivation-completion vocabulary other PRs reference.
2. **#722** (branch naming) — convention referenced by #726's
   recipe.
3. **#726** (auto-rebase) — references both #724's vocabulary (in
   §4g) and #722's branch glob (`claude/iw-[a-z0-9-]+`).

Any order works **textually** (different sections, no semantic
conflict).  The above order minimises line-number drift on later
PRs and keeps cross-references valid.

## §6 escalations

None.  No inconsistent findings between siblings; all four meta-PRs
extend the parent in compatible ways.

## Next concrete (non-overlapping) task on queue

- **Watch for #724 merge.**  Once landed, my #722 and #726 each
  need a 1-line rebase (mechanical, no conflicts expected).  The
  detangler #706 should adopt the convention in its own slot.
- **No new task spawned by this coordinate run.**

## Anti-pattern compliance check

- [x] Read sibling PRs first (read #724 + #706 file lists)
- [x] Classified each on overlap/dependency/cherry-pick
- [x] Posted one coordination comment per non-trivial sibling
      (#724, #706); skipped #694 (no overlap)
- [x] Triaged own-PR review threads (#722, #726 Copilot+Gemini)
- [x] Did not silently merge main (rebased only when prepare-merge
      ran with explicit `git rebase origin/main`)
- [x] Did not add a fresh sibling PR (#724, #706) to scope without
      author's implicit approval — both pre-existed and the user
      explicitly invoked `/coordinate with other watcher on new skills`
- [x] Ledger appended (this file)
