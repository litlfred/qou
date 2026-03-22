---
name: todo-review
description: >
  Monitor and triage open feedback todos across all content blocks.
  Surface actionable items at session start and on demand.
allowed-tools: Read Edit Bash Grep Glob WebFetch
---

# Todo Review Skill

## Role

Monitor open feedback/todos across the manuscript. Surface them at session
start and provide triage workflows so nothing falls through the cracks.

## When to Use This Skill

- **Session start** (automatic): check for open todos, present summary
- User asks: "show todos", "what feedback is pending", "review todos"
- User asks: "what needs attention", "any open items"
- After completing a block of work, to check if related todos can be closed

## Todo Storage

Todos live in `.qou-feedback/<paperId>/<rootName>.json` (gitignored).
They reference content blocks by `paperId` + `rootName` but are not
part of the content tree — they survive branch switches.

### Todo structure

```typescript
{
  id: string,           // "todo-<base36-timestamp>"
  summary: string,      // Short description (≤80 chars)
  comment: string,      // Full description
  status: "open" | "resolved" | "wontfix",
  priority: "low" | "medium" | "high",
  origin: "human" | "agent",
  assignee: "editor-agent" | "author" | "formalizer",
  createdAt: string     // ISO 8601
}
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/feedback/all?status=open` | GET | All open todos across papers |
| `/api/feedback?paperId=X&rootName=Y` | GET | Todos for one block |
| `/api/feedback` | POST | Create a new todo |

## Session Start Workflow

At session start, the `scripts/check-todos.sh` hook runs and outputs
a JSON summary. The editor should then:

1. **If todos exist**: present a summary to the user and ask:
   - "Review open todos" — walk through each, decide action
   - "Start a new task" — proceed normally, todos stay open
   - "Do research" — explore codebase, read content, no edits

2. **If no todos**: skip straight to normal triage.

### Summary format

```
Open todos: 3
  high:   1  (def:quantum-reeb-graph — "Fix functor coherence")
  medium: 2  (thm:spectral-convergence, rem:notation-note)
```

## Review Workflow

When reviewing todos:

1. **Read the todo** — show summary, comment, priority, assignee, age
2. **Read the block** — show the content block the todo references
3. **Ask the user** (multiple-choice):
   - **Address now** — fix the issue, then mark resolved
   - **Reassign** — change assignee (author, formalizer, editor-agent)
   - **Defer** — keep open, move to next
   - **Won't fix** — mark as wontfix with reason

4. After addressing, update the todo status in the `.json` file directly.

## Creating Todos (Agent-originated)

The editor can create todos during work when it notices issues:

```bash
curl -s -X POST http://localhost:3200/api/feedback \
  -H 'Content-Type: application/json' \
  -d '{
    "paperId": "quantum-observable-universe",
    "rootName": "block-name",
    "summary": "Short description",
    "comment": "Full description of the issue",
    "priority": "medium",
    "assignee": "editor-agent"
  }'
```

Or write directly to `.qou-feedback/<paperId>/<rootName>.json`.

## Resolving Todos

To resolve a todo, read the JSON file, find the todo by `id`, set
`status` to `"resolved"` or `"wontfix"`, and write back:

```typescript
// In .qou-feedback/quantum-observable-universe/block-name.json
[
  { "id": "todo-abc123", "status": "resolved", ... }
]
```

## Integration with Other Skills

| Skill | Integration |
|-------|-------------|
| `editor` | Session start triage includes todo check |
| `formalizer` | Creates todos when sorry bridges need attention |
| `proof-status-tracking` | Todos track formalization gaps |
| `content-validation` | Validation errors can become todos |
| `scientific-accuracy` | Review comments become todos |
