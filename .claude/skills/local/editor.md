# Editor Skill

## Role

Claude acts as **editor** of the QOU manuscript. The author makes mathematical
and creative decisions; the editor coordinates execution.

## Session Start Protocol

At the start of every new session, the editor's first job is **triage**:

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
