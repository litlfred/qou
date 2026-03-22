---
name: todo-review
roles: [reader, collaborator, owner]
description: >
  Monitor and triage open feedback todos across all content blocks.
  Surface actionable items at session start and on demand. Uses
  context-aware selection: scoped to current block when context exists,
  otherwise presents structured choices (priority, chapter, section).
allowed-tools: Read Edit Bash Grep Glob WebFetch AskUserQuestion Agent
---

# Todo Review Skill

## Role

Monitor open feedback/todos across the manuscript. Surface them at session
start and provide triage workflows so nothing falls through the cracks.

## When to Use This Skill

- **Session start** (automatic): check for open todos, present summary
- User asks: "show todos", "what feedback is pending", "review todos"
- User asks: "what needs attention", "any open items", "work on todos"
- After completing a block of work, to check if related todos can be closed

## Todo Storage

Todos live in `todos/` at the repo root (**gitignored** — survives branch
switches). They reference content blocks by `targetLabel` but are
**external to paper content** — no `todos` field exists on any content
block type.

Files:
- `todos/content-todos.ts` — content-related todos (array of `TodoItem`)
- `todos/infra-todos.ts` — infrastructure / feature request todos (optional)

### Todo structure

```typescript
import type { TodoItem } from "../content/schema/types";

export const todos: TodoItem[] = [
  {
    id: "todo-001",
    summary: "Short description (≤80 chars)",
    comment: "Full markdown description of the issue",
    status: "open",               // open | in_progress | blocked
    priority: "medium",           // critical | high | medium | low
    origin: "agent",              // agent | human | qc | extracted
    targetLabel: "def:quantum-universe",  // links to a content block
    assignee: "editor-agent",
    createdAt: "2026-03-22T00:00:00Z",
  },
];
```

## Context-Aware Todo Selection

When the user asks to "work on todos" or "process todos", follow this
decision tree:

### Step 1 — Check for active context

Does the current conversation have a **focus block** (e.g. the user is
editing `def:rigid-monoidal-category`, or just committed changes to a
specific definition)?

- **Yes** → filter todos to those whose `targetLabel` matches the
  current block (or blocks in the same section). Show those directly.
  Skip to **Step 3**.

- **No** → proceed to **Step 2**.

### Step 2 — Ask the user (structured questions)

Use `AskUserQuestion` with structured multiple-choice options so the
user doesn't have to type. Present **two questions**:

**Question 1: Scope** — "How would you like to select todos?"
  - "High priority" — show all `critical` and `high` priority todos
  - "By chapter" — follow up with chapter list
  - "By section" — follow up with section list (from a specific chapter)
  - "Show all" — show everything, sorted by priority

**Question 2 (conditional):** If the user chose "By chapter", present
the chapter list as options:
  - "Ch 0: Introduction"
  - "Ch 1: Quantum Observable Universe"
  - "Ch 2: Bring's Surface"
  - etc. (populated dynamically from the paper manifest)

If "By section", first ask for chapter, then list sections within it.

### Step 3 — Present selected todos

Show the filtered todo set as a summary table:

```
## Open Todos (3 items)

| # | Priority | Target | Summary |
|---|----------|--------|---------|
| 1 | high | def:quantum-universe | Missing Lean formalization |
| 2 | medium | thm:su2-emergence | Unresolved cross-reference |
| 3 | low | rem:notation-note | Clarify notation convention |
```

Then ask: "Which todo(s) would you like to work on?" with multi-select.

### Step 4 — Hand off to editor for triage

For each selected todo:

1. **Read the todo** — show summary, comment, priority, assignee, age
2. **Read the block** — load the `.ts` manifest and `.md` content
3. **Assess actionability** — can this be addressed with a text/code edit?
4. **Route to the appropriate skill**:
   - Content/prose issues → `scientific-accuracy` or `readability-editing`
   - Lean formalization → `formalizer` or `proof-triage`
   - Validation errors → `content-validation`
   - Cross-reference issues → `content-block-review`
5. **Execute the fix** (or explain why it can't be done now)
6. **Update todo status** to `in_progress` (agents may do this)
7. **Report outcome** — what was changed, what remains
8. **Offer "what next?"** — context-aware follow-up (see below)

### Step 5 — "What next?" (after each todo)

After completing a todo, immediately offer context-aware next steps
via `AskUserQuestion`. Options are derived from the current scope:

1. **More todos on this block?** → "Next todo on `<block>`"
2. **Related blocks in same section?** → "Next in §`<section>`"
3. **More todos in this chapter?** → "Other Ch `<N>` todos"
4. **Always include** → "Something else"

Keep to 3–4 options. If all todos in the current scope are done,
congratulate briefly and offer to move to the next chapter or switch
to a different kind of work (proofs, glossary, validation).

This ensures the user stays in flow without having to re-navigate
the todo landscape after each item.

## Seeding Todos

When `todos/` is empty or doesn't exist, the skill can bootstrap an
initial set by scanning for issues:

### Sources for auto-generated todos

| Source | How to scan | Priority |
|--------|-------------|----------|
| Content validation errors | `content_validate` MCP tool | high |
| Unresolved `uses[]` refs | Validation output | high |
| Missing `.lean` files | Definitions without Lean | medium |
| Missing `.md` files | Blocks without narrative | medium |
| `sorry` in Lean files | `grep sorry lean/` | medium |
| Lean `not_started` status | `.ts` manifests with `status: "not_started"` | low |
| Lean `stated` status | `.ts` manifests with `status: "stated"` | low |

### Seeding workflow

1. Run `content_validate` on all chapters
2. Parse validation output for errors and warnings
3. Group by `targetLabel` (one todo per block, not per issue)
4. Create `todos/content-todos.ts` with the generated items
5. Present summary to user

## Creating Todos (Agent-originated)

Agents create todos by appending to `todos/content-todos.ts`:

```typescript
{
  id: `todo-${Date.now().toString(36)}`,
  summary: "Short description",
  comment: "Full description of the issue",
  status: "open",
  priority: "medium",
  origin: "agent",
  targetLabel: "def:block-label",
  assignee: "editor-agent",
  createdAt: new Date().toISOString(),
}
```

## Resolving Todos

**Only the human author** may resolve or remove a TodoItem (see CLAUDE.md §4a).
Agents must never set status to `resolved` or `wontfix`, and must never
delete items. Agents *may* set status to `in_progress`.

## Integration with Other Skills

| Skill | Integration |
|-------|-------------|
| `editor` | Session start triage includes todo check |
| `formalizer` | Creates todos when sorry bridges need attention |
| `proof-status-tracking` | Todos track formalization gaps |
| `content-validation` | Validation errors seed todos |
| `scientific-accuracy` | Review comments become todos |
| `proof-triage` | Lean sorry stubs generate high-priority todos |
| `content-block-review` | Cross-reference issues become todos |
