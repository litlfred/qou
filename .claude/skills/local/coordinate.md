---
name: coordinate
description: Coordinate work across multiple in-flight Claude PRs working toward a shared goal (e.g. 1ppb mass-prediction). Post intent + asks on related PRs, identify cherry-pickable work, escalate inconsistent findings to the author, and keep a coordination ledger up to date.
roles: [reader, collaborator, owner]
user_invocable: true
---

# /coordinate — multi-agent / multi-PR coordination

When several Claude branches are converging on the same long-term goal
(e.g. "reach 1 ppb on mass predictions", "close all §3b violators",
"compute-infrastructure overhaul"), each agent has only its own
context.  Without coordination they will:

- duplicate work (two agents both class-axiomatising
  `conj:knot-factor-frobenius-pairing`),
- silently diverge (one renames `HA → delta_q`, another keeps `HA`,
  the merge conflicts),
- miss cherry-picks (one agent already wrote the Lean class template
  the others need),
- accept inconsistent findings without flagging them to the author.

`/coordinate` is the protocol that prevents this.  None of the agents
has all the answers; they look to the author for clarification on
inconsistencies, and they cherry-pick from each other.

## When to invoke

- Start of a session where the user mentioned **other branches/PRs**
  by name (e.g. "coordinate with `claude/foo` and `claude/bar`").
- Whenever you start a new substantive task in a multi-PR effort —
  before making code changes, post intent on the relevant PRs.
- When you finish a substantive task — post progress + concrete
  cherry-pickable artefacts (file paths, function names, Lean class
  templates, witness fixtures).
- When you encounter a **finding that contradicts another PR's
  framing** — write the disagreement up explicitly, post it to both
  PRs, and tag the author for resolution.

## Inputs

- The current PR number (your branch).
- A list of sibling branch names or PR numbers (the user gives this,
  or read `gh pr list --label "in-flight"`).
- The shared goal in 1–2 sentences (e.g. "reach 1 ppb on
  D…⁴⁰Ca masses without deriving Q_β").

## Protocol

### 1.  Read sibling PRs first

For each sibling PR:

```bash
gh pr view <N> --json number,title,body,state,headRefName,updatedAt
gh pr view <N> --json files --jq '.files[].path'
```

Use `gh`'s embedded `--jq` (don't pipe to an external `jq`; it
isn't a guaranteed dependency in every Claude Code environment).
Read the **full** file list, not a truncated head — partial scope
maps cause silent overlaps later. File paths are cheap.

Or via MCP: `mcp__github__list_pull_requests` /
`mcp__github__pull_request_read` (with paginated `get_files`).

Build a **scope map**: which PR owns which workplan phase,
which files, which conjectures, which compute scripts.

### 2.  Identify three relationships per sibling

For every sibling PR, classify yourself on three axes:

| Axis | Values |
|------|--------|
| **Overlap** | none / additive (different files, same goal) / conflicting (same file or same conjecture) |
| **Dependency** | independent / I depend on theirs / they depend on mine |
| **Cherry-pick opportunity** | none / I want X / they probably want Y |

A sibling that is `(none, independent, none)` doesn't need a
coordination comment.  Anything else does.

### 3.  Post intent before working

Use `mcp__github__add_issue_comment` (or `gh pr comment`) on each
sibling PR with non-trivial relationship.  Format:

```markdown
## Coordination from #<your PR>

**Picking up:** <one sentence — which workplan phase / task>

**Scope confirmation:**
- I will touch: `path/to/file:line-range`, `path/to/other`, …
- I will not touch: `<the sibling's territory>`

**Cherry-pick from you:**
- <what you need from them; e.g. "Lean class template you used for
  `conj:crystal-graph-realization`">

**Cherry-pick for you:**
- <what you'll produce that they may want; e.g. "the witness reader
  for `term6-residues-at-roots.witness.json` is the same shape they
  need for the canonical T6 path">

**Asks (small):** <questions they can answer in one line>

**Escalation to author:** <if any; see §5>
```

Keep it short.  One ask per ask.  No prose.

### 4.  Post progress at task boundaries

When you commit something cherry-pickable, post a follow-up:

```markdown
## Progress from #<your PR> · `<short-task-name>`

- Landed in `<commit-sha>`: <one sentence>
- Cherry-pick file pointers: `path/file.py:fn`, `path/file.lean:Decl`
- Updated [`<your-audit-or-plan-doc>.md`](…) §<section>: <what
  changed> — and/or appended a row to
  [`docs/coordination/<goal-slug>.md`](…)
- Next: <next task on your queue>
```

Cherry-pick file pointers are the load-bearing part — the sibling
agent should be able to copy/cite without reading your whole diff.

### 5.  Inconsistent findings → escalate, do not paper over

If a sibling PR's finding contradicts yours (e.g. they say T6 is
already canonical, you say it consumes a non-canonical witness;
they say the framework has one calibration, you found three), do
NOT silently change your framing to match theirs.  Post on both
PRs:

```markdown
## ⚠️ Inconsistent finding — author input requested

- This PR's claim: <yours, file_path:line cited>
- Sibling #<N>'s claim: <theirs, file_path:line cited>
- Likely cause: <best guess, ≤ 2 sentences>
- Resolution requested: <which framing to adopt going forward>

Tagging @<author>.  Will hold downstream work blocked on this.
```

The author owns the resolution.  Do not "split the difference" or
guess.  Inconsistent findings are an audit flag in the same way
that conjectures-not-class-axiomatised are.

### 6.  Coordination ledger

Maintain a single shared ledger at:

```
docs/coordination/<goal-slug>.md
```

Each PR appends a row (no rewrites of others' rows):

```markdown
| Date | PR | Phase | Status | Cherry-pick |
|------|----|-------|--------|-------------|
| 2026-05-08 | #564 | P4′ T6 wire-up | landed `<sha>` | `t6_canonical_MeV` reader |
| 2026-05-08 | #565 | F8 pickle migration | in-progress | — |
| 2026-05-08 | #567 | crystal R-matrix Sub-lemma 2.1 | landed `<sha>` | `conj:crystal-graph-realization` Lean class |
```

The ledger lives on the branch where the coordinator is currently
posting; final state can be merged to main when the goal completes.

### 7.  Cherry-picking

`/coordinate` explicitly authorises cross-PR cherry-picks under
these constraints:

1. **Cite the source PR** in your commit message
   (`Co-authored-by:` or `Cherry-pick of #<N>:<sha>`).
2. **Do not silently diverge** the cherry-picked code from the
   source — if you adapt, post a coordination comment back so the
   source can match.
3. **Match the author's voice / style** (one-voice rule still
   applies).

### 8.  Asks and responses

Asks are a first-class artefact.  Format every cross-PR ask as:

```markdown
**Q from #<your PR>:** <question>

(answers as inline replies on the destination PR)
```

If a sibling has not answered an ask after 1 calendar day in an
async setting, restate the ask in a fresh comment and tag the
author.  Do not block indefinitely.

## Output

After invocation, you should have:

- Read every sibling PR's body and changed-files list.
- Posted at most one coordination comment per sibling PR (intent +
  asks), unless you've made progress that warrants a separate
  progress comment.
- Identified the next concrete, non-overlapping task on your own
  workplan and started on it.
- (Optional) Created or updated `docs/coordination/<goal-slug>.md`
  with the current state.

## Anti-patterns

- ❌ Post a coordination comment that just summarises your own PR.
  Sibling agents already read your PR body.
- ❌ Pick the same task as a sibling without posting first.  Even
  if their PR has been quiet, the human author may have given them
  a verbal lead.
- ❌ "Resolve" an inconsistency by rewriting your finding.  Escalate
  to the author.
- ❌ Long prose.  Coordination comments are tables, file pointers,
  and one-line asks.

## Related skills

- `local/delivery-summary` — what to post **after** a feature lands
  (one PR scope).
- `local/watch` — passive monitoring of upstream branches.
- `local/diff` — per-block change report (one PR scope).

`/coordinate` complements them: it is the **active** cross-PR
protocol, not a passive watcher and not a single-PR summary.
