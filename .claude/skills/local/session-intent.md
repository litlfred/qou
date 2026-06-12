---
name: session-intent
description: Session-start intent declaration + session-end results recording, against the goal-scoped master ledger and queue file. Enforces the durable-handoff discipline so any agent can pick up another's thread.
roles: [reader, collaborator, owner]
user_invocable: true
---

# /session-intent — durable session intent + results

The 2026-05-31 c_k flip-flop episode (four flips in five days)
exposed a coordination failure: agents had no durable record of
which probes were in flight, what each one had already learned, or
why a "derivation" had been retracted. Each new session
re-discovered the same near-match and re-wired it, only to retract
later.

This skill enforces the **read → declare → work → record** loop so
the next session — possibly a different agent — picks up exactly
where the previous one left off.

## Where state lives

| Artifact | Purpose |
|---|---|
| [`STATUS.md`](../../../STATUS.md) | Always-current root dashboard: goals → master ledgers → active PRs |
| `docs/coordination/<goal>.md` | Per-goal **master ledger**: status table, open probes, flip-flop history, session log |
| `.beans/<goal>-queue.json` | Machine-readable **queue** of probes (typed `TodoItem[]`); committed so other agents see it |
| Per-PR body | Session intent at branch-open; EOS results appended |

## Session-start protocol (5 steps)

> Run these in order. Steps 1–3 are read-only; step 4 writes.

### 1. Read STATUS.md

Open [`STATUS.md`](../../../STATUS.md). Identify which goal row(s)
the user's current request touches. Note the active PRs column —
those are your siblings.

### 2. Read the goal's master ledger

Open `docs/coordination/<goal>.md`. Read:

- **Status table** — current canonical status of each subgoal /
  coefficient / observable. If a recent commit "derived" something
  but the ledger says NOT derived, **trust the ledger**: it's
  recording a retraction the commit doesn't reflect.
- **Flip-flop history** — every previous retraction, with the
  failure-mode signature. **Do not repeat any pattern listed here.**
- **Open probes** — what's already in flight.
- **Session log** — what previous sessions on this goal did.

### 3. Read the queue

Open `.beans/<goal>-queue.json`. Find:

- **`status: "open"`** items not yet picked up.
- **`status: "blocked"`** items waiting on dependencies — check if
  any of their `blocked_by` items have moved to "done" since the
  queue was last edited.
- **`assignee`** — agent branch currently working it (if any).
  Per "no explicit claim" process, multiple agents MAY pick the
  same item; coordinate with the user if you see this happen.

### 4. Declare intent (write)

Three places, all required:

**a. Master ledger session log** — append a row:

```markdown
| 2026-05-31 | Claude / `<branch>` | INTENT: <which probe IDs from queue + what user asked> | (filled at EOS) |
```

**b. Queue file** — set `assignee: "<branch>"` and `status: "in_progress"`
on each probe you're picking up. If a probe was already `assignee`-d
to a different branch, **leave that field alone**; just add your branch
to a `co_assignees` array (signal to coordinate with user).

**c. PR body** — at branch-open, the PR body must include:

```markdown
## Intent (session start)
- <one line per probe ID from queue you're working>
- <user's stated goal in their words>

## Session results
<filled at EOS>
```

### 5. Hand off to /coordinate

After step 4, run `/coordinate` to post intent on relevant sibling PRs
+ triage their review comments. Then start work.

## Session-end protocol (3 steps)

> Run these BEFORE pushing the final commit. The push triggers PR
> auto-subscription + sibling-coord sweep, so the EOS state must be
> visible from the push commit.

### 1. Update the queue

For each probe you worked:

- If completed: `status: "done"`, append `completedAt: <date>` and
  `completedBy: <branch>` to `data`. Add `summary_of_finding` text.
- If partial: leave `status: "in_progress"`, update `comment` field
  with: what you tried, what worked, what's left, next-step
  suggestion for the picking-up agent.
- If you discovered a NEW probe: append a new TodoItem to the queue
  with `origin: "<your-branch>"`. Mark `status: "open"`.
- If you retract a previous "derivation" claim: do NOT just edit the
  status field. Append the retraction to the ledger's flip-flop
  history (Stop Repeating Yourself).

### 2. Append results to the master ledger

The session log row from step 4a now gets its "RESULTS" column filled:

```markdown
| 2026-05-31 | Claude / `<branch>` | INTENT: probe-c3-q0-stability | RESULTS: confirmed q_0 dependence at all 3 anchors; appended new probe `probe-c3-rep-theoretic-source` for follow-up. PR #1581 opened. |
```

If the session retracted a prior claim, add a row to the
**Flip-flop history** table with the retraction reason.

### 3. Update the PR body

Replace the placeholder `## Session results` section with:

```markdown
## Session results
- Picked up: <probe IDs>
- Completed: <list>
- Partial: <list with where to pick up>
- New probes added: <list>
- Retractions: <list of any prior-claim retractions>
- Open question for user: <if any>
```

## Multi-agent same-goal coordination

Per author's 2026-05-31 directive: **multiple agents MAY attack
the same goal simultaneously**. The model is:

- **Goal** = product (user's directive).
- **Queue** = per-goal item list, all agents read + write.
- **Probes are not exclusively claimed.** Two agents may pick the
  same probe; this is allowed.
- **Coordination is with the USER on goal-level decisions**, not
  agent-to-agent on probe-level locks.

When you discover a probe you're working has been picked up by
another agent (`co_assignees` populated, or you see a sibling PR
commit touching the same scope):

1. **Do not silently abandon** — your independent attack is
   valuable (different methods may surface different findings).
2. **Post intent** on the sibling PR via `/coordinate` so the
   sibling agent sees you're also working it.
3. **Ask the user** if they want both threads or want one to
   stand down. Use `AskUserQuestion` with rich context (CLAUDE.md
   §User accessibility). Sample:

   > 🟡 Two agents attacking probe-c3-q0-stability — sibling PR
   > #XXXX is at 50% with method A (Habiro recursion); I'd attack
   > with method B (PSLQ basis sweep). Keep both threads?

4. **If user says one stands down**, the standing-down agent
   appends partial results to the ledger and updates queue
   `status: "open"` (releasing it).

## Hand-off pickup protocol

If you're the picking-up agent (someone else's `in_progress` probe
or partial result):

1. Read the previous session log row in the ledger — that's the
   handoff letter.
2. Read the queue `comment` field — that's the technical state.
3. Read the partial PR (if open) — that's the code state.
4. Declare your intent normally; the queue entry now lists you as
   `assignee`. The previous owner is recorded in `data.history`.

## Anti-patterns

- ❌ Starting work without reading the ledger first ("just-the-prompt"
  agents miss retraction history and re-derive flipped claims).
- ❌ Claiming a probe but not writing the EOS results ("silent abandon").
- ❌ Editing the queue file without also editing the ledger ("queue
  drift").
- ❌ Retracting a previous claim by quietly removing it from the queue
  without updating the flip-flop history ("erasure" — guaranteed to
  re-flip next session).
- ❌ Asking the user "should I pick this probe?" — the queue is the
  authoritative list; just pick and declare.

## See also

- CLAUDE.md §Agent work-plan policy (the TodoWrite source rule)
- CLAUDE.md §Branch + PR workflow (the ALWAYS-PR rule)
- `.claude/skills/local/coordinate.md` (sibling-PR coordination)
- `.claude/skills/local/watch.md` (main-watching)
- `.claude/skills/local/pending-show.md` (showing current pending)
