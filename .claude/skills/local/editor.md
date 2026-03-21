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
> **Remote server:** check if `lean.litlfred.org` is running.
>
> Proceed with LaTeX-only work?

If the request is LaTeX-only, proceed normally.

**Note**: The lean-lsp-mcp server provides diagnostics, goal states,
hover docs, completions, LeanSearch, Loogle, and more — identically
whether running locally (stdio) or remotely (Streamable HTTP).

### 1. Triage

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

## Interaction style

- Questions to author: always multiple-choice (2-4 options), concise labels.
- Status updates: brief, at natural milestones.
- Never make mathematical decisions autonomously — always confirm with author.
- When delegating, provide agents with full context so they work autonomously.

## Delegation patterns

| Task | Agent | Notes |
|------|-------|-------|
| LaTeX definition/theorem edits | formalizer | Give exact file, line range, and desired content |
| Notation propagation (k→R, ℂ→K) | consistency (general-purpose) | Search-and-replace with mathematical awareness |
| New terms (P(V), archimedean) | glossary (general-purpose) | Check all files for consistency |
| Category theory content | category-theory | For adjunctions, functors, natural transformations |
| Cross-reference validation | latex-validation | After all edits complete |

## Current plan

See `/root/.claude/plans/twinkling-nibbling-treehouse.md` for the active workplan.
