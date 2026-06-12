---
name: todo-manager
roles: [reader, collaborator, owner]
description: >
  Maintain and display work-in-progress task lists using the TodoWrite
  tool. Track implementation progress, open computations, missing Lean
  files, and blocked items across content blocks.
allowed-tools: Read Grep Glob TodoWrite AskUserQuestion
---

# Todo Manager Skill

> **Disambiguation:**
> - `todo-manager` (this file) = the agent's **session work-plan**.
>   In-memory TodoWrite list of the current session's tasks.
> - `todo-review` = triage of **content feedback** stored in
>   `.beans/content-todos.ts` and surfaced via the MCP `/todos`
>   dashboard. That is paper-content scope, not session scope.
>
> See also CLAUDE.md §"agent work-plan policy" — the agent must
> start a todo list at session start, queue rather than pivot, and
> work pending todos when blocked or waiting on scripts.

## Role

Maintain structured task lists for multi-step work. Track what's done,
what's in progress, and what's blocked. Surface the current state on
request ("status", "what's left", "show todos").

## When to Use This Skill

- User asks: "status", "show status", "what's left", "todos"
- At the start of a multi-step task (3+ steps)
- When switching between tasks or returning to a paused session
- After completing a milestone, to update progress
- When the user gives a list of items to work through

## How to Use

1. **Create todos** at the start of multi-step work.
   Break complex tasks into specific, actionable items.

2. **Track progress** by marking items in_progress (one at a time)
   and completed as each finishes.

3. **Surface blockers** — if a task can't proceed, note why and
   create a follow-up todo.

4. **Clean up** — remove stale items, consolidate related tasks,
   keep the list current.

## Todo Item Format

Each todo has:
- `content`: imperative ("Write Lean for X", "Run computation Y")
- `activeForm`: present continuous ("Writing Lean for X")
- `status`: pending | in_progress | completed

## Rules

- Exactly ONE item should be `in_progress` at a time.
- Mark items `completed` immediately when done (don't batch).
- If blocked, keep as `in_progress` and add a blocker todo.
- When user asks "status", show the full list with counts.
- When user says "show todos", display the current TodoWrite state.

## Integration with Other Skills

- **formalizer**: track Lean sorry count per block
- **content-validation**: track missing .ts/.md/.lean triples
- **proof-triage**: integrate with formalization priority
- **editor**: track chapter-level writing tasks

## Status Display Format

When asked for status, present:

```
## Current Todos
- [x] Item 1 (completed)
- [>] Item 2 (in progress)
- [ ] Item 3 (pending)
- [ ] Item 4 (pending)

Progress: 1/4 complete, 1 in progress
```
