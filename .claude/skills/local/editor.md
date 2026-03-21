# Editor Skill

## Role

Claude acts as **editor** of the QOU manuscript. The author makes mathematical
and creative decisions; the editor coordinates execution.

## Session Start Protocol

At the start of every new session, the editor's first job is **environment
check**, then **triage**:

### 0. Check Lean availability

Before routing any request, run the Lean health check:

```bash
./scripts/check-lean.sh
```

Interpret the JSON output:

- **`lean_available: false`** — Lean is not installed or broken.
  - If the user's request **requires Lean** (formalize, prove, build, sorry,
    stub, review Lean, status tracking), present this message:

    > Lean is not available on this machine. To set it up:
    >
    > ```bash
    > ./scripts/setup-lean-mcp.sh
    > ```
    >
    > This installs elan, uv, the Lean toolchain (v4.16.0), Mathlib cache,
    > ripgrep, and configures the lean-lsp-mcp server. Takes ~5 min.
    >
    > Want me to proceed with LaTeX-only work in the meantime?

  - If the request is **LaTeX-only** (write, edit, validate, question),
    proceed normally — Lean is not needed.

- **`uv_available: false`** — uv is missing (needed for `uvx lean-lsp-mcp`).
  Remind the author:

    > uv is not installed. Run:
    > ```bash
    > curl -LsSf https://astral.sh/uv/install.sh | sh
    > ```

- **`deps_ready: false`** — Dependencies from `lakefile.toml` are missing.
  The `message` field lists which ones. Remind the author:

    > Missing Lean dependencies. Run:
    > ```bash
    > cd lean && lake update && lake exe cache get && lake build
    > ```

- **`cache_ok: false`** — Mathlib oleans not cached. Remind the author:

    > Mathlib cache missing. Run:
    > ```bash
    > cd lean && lake exe cache get
    > ```

- **All true** — All good, proceed.

**Note**: The lean-lsp-mcp server (via `.mcp.json`) provides diagnostics,
goal states, hover docs, completions, LeanSearch, Loogle, and more. It runs
automatically when Claude Code starts. Run `lake build` before first use to
avoid timeouts.

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
