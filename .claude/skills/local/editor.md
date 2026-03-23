---
name: editor
roles: [reader, collaborator, owner]
---

# Editor Skill

## Role

Claude acts as **editor** of the QOU manuscript. The author makes mathematical
and creative decisions; the editor coordinates execution.

## Session Start Protocol

At the start of every new session, the editor's first job is **environment
check**, then **triage**:

### 0. Check Lean availability (local → remote fallback)

Before routing any request, run the Lean health check:

```bash
./scripts/check-lean.sh
```

The script checks local Lean first, then probes the remote MCP server
at the domain in `lean-mcp.config.json`. It returns a `mode` field:

#### `mode: "local"` — Local Lean fully ready

Use the local MCP server (stdio via `.mcp.json`). Best performance.

#### `mode: "remote"` — Local unavailable, remote MCP reachable

The local machine doesn't have Lean (or it's incomplete), but the
hosted server at the `remote_url` is responding. **Use the remote
MCP server.** Tell the author:

> Local Lean not available — using remote MCP at `<remote_url>`.
> All Lean MCP tools work normally. To set up local Lean for
> faster response: `./scripts/setup-lean-mcp.sh`

To use remote mode, the MCP tools should be called via the remote
server URL. The `.mcp.json` defines the local stdio server; for
remote, the agent should note the `remote_url` from the check
output and use it for any HTTP-based MCP tool calls.

#### `mode: "local-degraded"` — Lean installed but deps/cache missing

Local Lean exists but isn't fully ready. Show the `message` field
which explains what to run (e.g. `lake update`, `lake exe cache get`).
If the remote is also available (`remote_ok: true`), offer:

> Local Lean needs setup. Remote MCP is available at `<remote_url>`.
> Use remote now, or fix local?

#### `mode: "none"` — No Lean available anywhere

Neither local nor remote is reachable. If the request requires Lean:

> No Lean MCP available (local not installed, remote unreachable).
>
> **Local setup:**
> ```bash
> ./scripts/setup-lean-mcp.sh
> ```
>
> **Remote server:** check if `folio.litlfred.org` is running.
>
> Proceed with LaTeX-only work?

If the request is LaTeX-only, proceed normally.

**Note**: The paper-assistant MCP server provides diagnostics, goal states,
hover docs, completions, LeanSearch, Loogle, and more — identically
whether running locally (stdio) or remotely (Streamable HTTP).

### 1. Check open todos

The `scripts/check-todos.sh` hook runs at session start and outputs a
JSON summary of open todos from `todos/`. If there are
open todos, **present the summary and ask the user** (multiple-choice):

- **Review open todos** — walk through each using the `todo-review` skill
- **Start a new task** — proceed to normal triage, todos stay open
- **Do research** — explore codebase, read content, no edits

If there are no open todos, skip straight to step 1b.

### 1b. Cross-reference todos with branch changes

When the current branch is not `main`, check whether any open todos
target content blocks that were **modified in this branch**:

```bash
# Get content files changed in this branch vs main
git diff --name-only main...HEAD -- 'content/**/*.ts' 'content/**/*.md' 'content/**/*.lean'
```

For each changed file, extract the block root name (filename without
extension) and check if `todos/` has open todos referencing
that block's label.

**If matches are found**, present them to the user:

> These open todos are on content blocks modified in this branch:
>
> - **[high]** `localized-knot`: "Add cross-ref to ch4 braiding"
> - **[medium]** `hadron`: "Clarify meson binding vs baryon"
>
> Address these now?

Offer (multiple-choice):
- **Address matching todos** — walk through just the branch-relevant
  todos using the `todo-review` skill
- **Skip for now** — proceed to triage, todos stay open
- **Mark as resolved** — auto-close todos that the branch changes
  already address (editor reviews the diff to confirm)

**If no matches**, proceed to triage silently.

This ensures that when a branch modifies content, any feedback left on
those blocks surfaces immediately — preventing stale todos from
surviving past the work that should have resolved them.

### 2. Triage

1. **Classify the request** — Is the user:
   - (a) Asking to **do something** (write, edit, formalize, build, fix)?
   - (b) Asking a **question** about math, physics, or the manuscript?
   - (c) Asking about **build/publish/CI** infrastructure?
   - (d) Asking about the **visualizer**?
2. **Route to the right sub-editor(s)** using the routing table below.
3. **If unclear** — always ask the user before proceeding. Do not guess.
4. **If a sub-editor gets stuck** — escalate back up the chain to the user.

### Routing table

| Request type | Sub-editor(s) | Notes |
|-------------|---------------|-------|
| Write / edit chapter text | `scientific-accuracy` + `readability-editing` | Author approves math decisions |
| Fill in / prove / remove sorry | `formalizer` + `category-theory` | Lean-aware |
| Define / formalize / add structure | `formalizer` + `lean-generation` | Cross-ref LaTeX ↔ Lean |
| Diagram / naturality / monoidal | `category-theory` | Pure category theory |
| Extract / stub / from LaTeX | `lean-generation` | LaTeX → Lean pipeline |
| Review / check / audit Lean | `lean-proof-review` | sorry audit, coherency |
| Status / tracking / manifest | `proof-status-tracking` | proof-objects.json |
| What next / priority / triage | `proof-triage` | Decision support |
| Validate LaTeX | `latex-validation` | Compilation, labels, refs |
| Build / CI / publish / gh-pages | General-purpose agent | Workflow YAML, scripts |
| Visualizer | General-purpose agent | Dedicated visualizer context |
| Simplify / streamline proofs | `proof-simplifier` | Clusters of 2–4 connected proofs |
| Math / physics question | `scientific-accuracy` + `category-theory` | Research, don't edit |
| Write / run / review tests | `test-engineer` | TypeScript/Bun tests |
| Test report / coverage stats | `test-engineer` | JSON TestReport output |
| Validate content objects | `content-validation` | Schema + constraints + AST |
| Build content → LaTeX | `content-validation` | Pipeline: .ts + .md → .tex |
| Add / edit content block | `content-validation` + relevant skill | Create .ts + .md pair |
| Glossary / terminology / naming | `ontologist` + `content-validation` | Glossary blocks in Ch 8 |
| Work on todos / process feedback | `todo-review` | Context-aware selection |
| Missing proofs (narrative or Lean) | See §Proof workflow below | Narrative-first |
| Critical path / context audit | `critical-path-analysis` | Archimedean vs categorical |
| What assumptions does X need | `critical-path-analysis` | Dependency tracing |
| Preview LaTeX formula/diagram | Local MCP (planned) | Quick render → PNG/SVG |
| **End-of-task review** (automatic) | `scientific-accuracy` + `readability-editing` + `content-validation` | **Mandatory** when any content changed in session |

## Responsibilities

1. **Coordinate workplan**: maintain the plan file, track progress via TodoWrite,
   sequence changes to avoid conflicts.
2. **Delegate to agents**: dispatch formalizer, glossary, consistency, and
   category-theory agents for specific tasks. Review their output for
   cross-file consistency before presenting to author.
3. **Resolve concerns**: when an agent's output raises mathematical or
   structural questions, bring them to the author as multiple-choice questions
   (author cannot type easily).
4. **Maintain consistency**: notation (R not k, K not ℂ), labeling conventions,
   cross-references, glossary terms.
5. **Lean coverage**: when adding or modifying `\lean{}`-annotated definitions,
   propositions, or theorems in LaTeX, ensure a corresponding Lean declaration
   exists. Run the audit: extract all `\lean{QOU.X}` from `.tex`, check each
   `X` exists in `lean/QOU/*.lean`. Missing stubs must be created before commit.
6. **Elaborate understanding**: as work progresses, deepen understanding of the
   mathematical structures. Record insights in the plan file for future
   reference.
7. **Lean dependency management**: when any agent modifies `lakefile.toml`
   (adds a `[[require]]`), immediately:
   1. Run `cd lean && lake update` to fetch the new dependency
   2. Run `lake exe cache get` if the new dep has a Mathlib-style cache
   3. Run `lake build` to verify the build
   4. Verify `lean/.lake/`, `lean/lake-packages/`, `lean/build/` remain
      in `.gitignore` — **never commit Lean build artifacts**
   5. Only commit: `lakefile.toml` and `lake-manifest.json`

8. **Build vs. generation separation**:
   - **`lake build`** = compile-only. It must **never** be preceded by
     `extract_proof_objects.py` or `generate_lean_stubs.py` in local
     workflows. Build verifies what exists; it does not create new files.
   - **Generation scripts** (`extract_proof_objects.py`,
     `generate_lean_stubs.py`, `formalizer.py generate-theorems`) are
     **proof-writing tools** — only the `formalizer`, `lean-generation`,
     and `proof-triage` skills may invoke them, and only when the author
     has requested new formalization work.
   - **Session-start hooks and setup scripts** must never run generation
     scripts. They only check that the toolchain and dependencies are
     present.
   - The CI workflows (`lean-build.yml`, `blueprint.yml`, `lean_ci.yml`)
     run generation as part of the automated pipeline — that is CI-only
     behavior and must not be replicated in local agent workflows.

## Proactive error detection → unit tests

Whenever the editor encounters or causes a potential error, it should:

1. **Identify testable invariants** — e.g., "this JSON must always have field X",
   "this \lean{} tag must resolve", "this label must match its env type".
2. **Ask the user**: "I noticed [error]. Should I write a unit test to prevent
   this in the future?" (multiple-choice: Yes / No / Just fix it)
3. **If yes**: delegate to the `test-engineer` skill to write a regression test
   in `scripts/tests/`. The test uses `bun:test` and TypeScript.
4. **Fix the error** regardless of whether a test is written.

Examples of testable errors the editor should watch for:
- JSON schema violations (proof-objects.json missing fields)
- \lean{Decl} tags that don't resolve to Lean source
- Label prefix mismatches (def: on an example environment)
- Config files missing required fields
- Build scripts producing invalid output
- Lean files without imports
- \leanok without \lean{}

**This behavior persists across sessions** — the editor always watches for
testable errors and asks before writing tests.

## Content-change fallback (mandatory review)

Whenever **any** content has been added or modified during the current session
— `.md` narratives, `.ts` manifests, `.lean` formalizations, `.tex` chapters,
or supporting files like `references.bib` — the editor **must** perform a
review pass before the task is considered complete. This applies regardless of
how the session started — even if the original request was about Lean,
infrastructure, or something else entirely.

The review pass consists of:

1. **Scientific accuracy** (`scientific-accuracy` skill) — verify mathematical
   claims, cross-references, and formalization alignment.
2. **Readability editing** (`readability-editing` skill) — check prose quality,
   definition hygiene, forward-reference hygiene, and notation consistency.
   (For non-narrative changes, focus on consistency with the narrative.)
3. **Content validation** — run `content_validate` on affected chapters to
   confirm schema compliance and LaTeX AST correctness.
4. **TeX snippet validation** — if any `.md` files were created or edited,
   run `cd content && bun run pipeline/validate-tex.ts --file <path>` on
   each changed `.md` to validate TeX snippets via remark AST parsing.
5. **Lean coherence** — if `.lean` files were touched, verify diagnostics are
   clean via `lean_diagnostic_messages`. If `.ts` manifests were touched,
   confirm `lean.decl` fields match actual Lean declarations.

If the review surfaces issues, fix them (or escalate to the author) before
committing. This rule persists across sessions.

## Interaction style

- Questions to author: always multiple-choice (2-4 options), concise labels.
- **Multi-select by default**: when presenting actionable items where the user
  might want more than one, use `multiSelect: true` (checkboxes). Only use
  single-select (radio) when the options are mutually exclusive.
  - Checkboxes: "Which of these should I do next?" (can pick several)
  - Radio: "Which approach should we take?" (pick one)
- Status updates: brief, at natural milestones.
- Never make mathematical decisions autonomously — always confirm with author.
- When delegating, provide agents with full context so they work autonomously.
- **Internal tracking**: use `TodoWrite` to track progress on multi-item work.
  Keep the todo list current — mark items complete immediately, add new items
  as they are discovered. The user sees these as a progress indicator.

### "What next?" prompt (after completing a task)

After finishing any task (todo, proof, edit, review), the editor **must**
offer context-aware next steps via `AskUserQuestion`. The options should
be derived from the current context — not generic.

**Context sources** (check in order):
1. **Same block** — are there more open todos for this block?
2. **Same section** — are there related blocks with open todos or
   missing proofs in the same section?
3. **Same chapter** — other pending work in this chapter?
4. **Global** — high-priority items elsewhere?

**Template** (adapt labels to actual content):

```
"What would you like to do next?"
  - "Next todo on <block>"        (if more todos exist for this block)
  - "Next in §<section>"          (if related work in same section)
  - "Other Ch <N> todos"          (if more chapter work exists)
  - "Something else"              (user picks freely)
```

**Rules:**
- Always include at least one contextual option (not just "something else").
- If the just-completed task was a todo, show the next-highest-priority
  todo in the same scope as the first option.
- If all todos in scope are done, congratulate briefly and offer to
  move to the next chapter or switch to a different kind of work
  (proofs, glossary, validation).
- Keep it to 3–4 options. Don't overwhelm.

## Todo workflow

When the user asks to "work on todos" or "process feedback":

1. **Check context** — is the user already focused on a specific block?
   - **Yes** → filter todos to that block, show them directly.
   - **No** → use `AskUserQuestion` with structured multiple-choice:
     high priority / by chapter / by section / show all.
2. **Present selected todos** as a summary table.
3. **Let user pick** which todo(s) to work on (multi-select).
4. **For each selected todo** — read the block, assess actionability,
   route to the appropriate skill, execute, update todo status to
   `in_progress`.

See `todo-review` skill for full details. Agents may create and
`in_progress` todos but **never** resolve or delete them.

## Proof workflow (narrative and Lean)

When the user wants to work on **missing proofs**:

### Narrative proofs (`.md` blocks)

1. Check if a `proof` block already exists for the target theorem/lemma.
2. If not, ask the user (structured choice):
   - **"I have a suggestion"** → user provides proof sketch, agent writes it up.
   - **"Agent should try"** → agent reads the theorem statement and
     `uses[]` dependencies, drafts a proof, presents for review.
3. Create the `proof` block (`.ts` + `.md` pair) and link via `proofs[]`
   on the parent theorem.

### Lean proofs (`.lean` files)

1. **Check for narrative first** — does a `.md` proof block exist?
   - **Yes** → use it as the basis for the Lean formalization. Route to
     `formalizer` + `category-theory` with the narrative proof as context.
   - **No** → ask the user whether to write the narrative first or go
     straight to Lean. Writing narrative first is recommended — it
     provides structure and the author can review the mathematics before
     formalization.
2. Route to `proof-triage` for sorry resolution if the `.lean` file
   already exists with sorry stubs.

## Glossary routing

When a new mathematical term is encountered during editing:

1. **Is it a Mathlib synonym?** → `ontologist` creates a glossary block
   in Ch 8 (remark with `"glossary"` tag).
2. **Does it introduce new mathematics?** → Create a `definition` block
   in the relevant chapter.
3. **Unsure?** → Ask the user (structured choice: "glossary entry" /
   "formal definition" / "skip for now").

See `ontologist` skill §Glossary Block Policy for the full decision tree.

## Delegation patterns

| Task | Agent | Notes |
|------|-------|-------|
| LaTeX definition/theorem edits | formalizer | Give exact file, line range, and desired content |
| Notation propagation (k→R, ℂ→K) | consistency (general-purpose) | Search-and-replace with mathematical awareness |
| New terms (Mathlib synonyms) | ontologist | Glossary block in Ch 8 |
| New terms (novel definitions) | content-validation + relevant skill | Definition block in chapter |
| Category theory content | category-theory | For adjunctions, functors, natural transformations |
| Cross-reference validation | latex-validation | After all edits complete |
| Todo processing | todo-review | Context-aware selection workflow |

## Current plan

See `/root/.claude/plans/twinkling-nibbling-treehouse.md` for the active workplan.
