# Claude Code — Quantum Observable Universe

## User accessibility

The repo owner is physically disabled and types with difficulty.
Adapt ALL responses accordingly:
- **Short answers.** One-liners when possible.
- **Offer choices as numbered lists** so the user can reply "1" or "2".
- **Run commands proactively** — don't ask "shall I run X?", just run it.
- **Branch/commit/push without asking** unless destructive.
- **Interpret terse/misspelled input charitably** — infer intent, don't ask for clarification on typos.

This repository is a formal mathematics paper with:
- **Content objects** (`.ts` + `.md` + `.lean` file triples) as authoritative source
- **LaTeX** as a rendering target (generated from content objects)
- **Lean 4** formalization linked to content objects

## Agent work-plan policy (STRICT)

Every session must run from a **prioritized work-plan** maintained
via the TodoWrite tool. The plan is the agent's source of truth for
"what next" — not the user's last message, not the most recently
mentioned file.

1. **Start a todo list at session start.** As soon as you have
   enough context (after reading the user's first request, the
   SessionStart hooks, and the current branch / PR state), draft a
   TodoWrite list with the requested work decomposed into concrete
   tasks. If the request is one trivial task, you may skip — but
   any time there are ≥ 2 distinct steps, draft the list.

2. **Queue, do not pivot.** When a new request, review comment, or
   sibling-PR ask arrives mid-session, **append** it to the plan in
   priority order — do not abandon the in-progress task. Pivot only
   when the user explicitly says so ("stop", "drop that", "switch
   to X first"). Inferred urgency is not enough.

3. **Parallelize independent tasks.** When two queued tasks have no
   dependency between them (e.g. one Lean fix + one .md edit on
   different blocks), batch them into a single response with
   parallel tool calls. Use background `Agent(run_in_background=true)`
   for independent research / triage that does not block the
   foreground task.

4. **Work the queue while idle.** When you are waiting on a
   long-running script, a background agent, a Lean build, or a CI
   run, pull the next pending todo and work on it. Never just sleep
   or poll. (Exception: if the only remaining todos depend on the
   in-flight task, idle and wait for the notification.)

5. **Update the plan when upstream lands.** The session-start hook
   arms `local/watch` on `origin/main` (and `local/coordinate`
   triages sibling PRs). Whenever a `<github-webhook-activity>` or
   watcher event reports a new commit / PR / review comment that
   affects this branch, walk the §3 watch checklist; if the result
   is "queue work", insert the new todo at the right priority slot
   (do not push to the bottom blindly, do not jump above the
   current in-progress task unless it is a blocker).

6. **End-of-session: surface the plan.** If the session ends with
   pending todos and the next step is **not unambiguous**, show the
   remaining todo list to the author before closing — even if the
   user said "we're done". Use a numbered list so they can reply
   "1, 2" to pick what's next. If the next step *is* unambiguous
   (one todo, clearly the user's stated goal), skip the prompt.

This policy makes the agent durable to interruptions, sibling-PR
churn, and long async waits. It is enforced by review tooling: a
session that pivots without a `TodoWrite` update or that idles
without pulling the queue is an audit flag.

## Always provide GitHub links — default to `.md`

Whenever a skill or agent creates or modifies a file, the reply **must**
include a clickable GitHub blob URL for every affected file on the
pushed branch. This applies to all file kinds: `.md`, `.ts`, `.lean`,
`.tex`, config files, scripts, etc.

**Default link target for content blocks is always the `.md` file.**
When citing a content block (definition, proposition, remark, etc.) in
chat replies, reviews, or summaries, the primary clickable link
**must** point to the `.md` sibling — never to `.ts` or `.lean` as the
primary link.

Rationale: `.md` is the narrative/authoritative human-readable face of a
content block. `.ts` is manifest metadata; `.lean` is formalization.
Users want to read the statement, not the manifest.

Pattern (always):

```
https://github.com/litlfred/qou/blob/<branch>/<path-to>/<block>.md
```

**When to link siblings (`.ts`, `.lean`, `.tex`):**
- Only in delivery summaries for **modified** files (see
  `.claude/skills/local/delivery-summary.md`) — list every sibling that
  actually changed.
- When the user explicitly asks about the Lean formalization or TS
  manifest.
- Never as the primary citation link for a block reference.

If the branch is not yet pushed, say so explicitly and do not fabricate
URLs.

## CRITICAL: Protected Files — DO NOT MODIFY

The following files are **strictly off-limits** to all coding agents
(Claude, Copilot, etc.). Only the repo owner may edit them manually:

- `deploy/google-viewers.txt` — Google OAuth viewer whitelist
- `deploy/github-collaborators.txt` — GitHub OAuth collaborator whitelist
- `.github/CODEOWNERS` — File ownership rules

These files control authentication access to the folio deployment.
**Never** read, write, edit, or suggest changes to these files.
If asked to modify them, refuse and explain that only the repo owner
can change whitelist files manually.

## Skills

Skills are organized under `.claude/skills/`:

- **`local/`** — repo-specific skills (latex-validation, scientific-accuracy,
  readability-editing)
- **`<package-name>/`** — skills synced nightly from external packages defined
  in `skills-config.json` (mode `"sync"`)
- **Reference packages** — registered in `skills-config.json` with mode
  `"reference"`, fetched on demand via the `skill_fetch` MCP tool (not
  synced locally)

### Skill routing (quick reference)

When a user request arrives, route to the right skill(s):

| User request pattern | Primary skill(s) | Min role |
|---------------------|------------------|----------|
| "fill in / prove / remove sorry" | `local/formalizer` + `local/category-theory` | collaborator |
| "define / formalize / add structure" | `local/formalizer` + `local/lean-generation` | collaborator |
| "diagram / naturality / monoidal" | `local/category-theory` | collaborator |
| "extract / stub / from LaTeX" | `local/lean-generation` | collaborator |
| "review / check / audit Lean" | `local/lean-proof-review` | collaborator |
| "status / tracking / manifest" | `local/proof-status-tracking` | reader |
| "what next / priority / triage" | `local/proof-triage` | collaborator |
| "proof gap / missing step / unproved assertion / bridging lemma" | `local/proof-gap-audit` | reader |
| "audit proofs / review proofs / proof editor / coordinate proof review" | `local/proof-editor` | collaborator |
| "simplify exposition / revisit old proof / integrate new content" | `local/proof-exposition-review` | collaborator |
| "lean vs narrative / do they prove the same thing / equivalence audit" | `local/proof-narrative-lean-equivalence` | collaborator |
| "concise proof / tighten proof / cut verbose narrative / shorten human proof" | `local/proof-conciseness` | collaborator |
| "write / edit chapter text" | `local/scientific-accuracy` + `local/readability-editing` | reader (review) / collaborator (edit) |
| "fix lean build / lake build fails" | `local/lean-build-fix` | collaborator |
| "audit lean / completeness / coverage" | `local/lean-completeness-audit` | collaborator |
| "simplify / streamline proofs" | `local/proof-simplifier` | collaborator |
| "validate LaTeX" | `local/latex-validation` | reader |
| "validate content objects" | `local/content-validation` | reader |
| "build content → LaTeX" | `local/content-validation` | reader |
| "add / edit content block" | `local/content-validation` + relevant skill | collaborator |
| "review / audit blocks" | `local/content-block-review` | collaborator |
| "glossary / terminology / naming" | `local/ontologist` + `local/content-validation` | collaborator |
| "witnessed value / drift / numerical literal / :val / hardcoded number / pin to witness" | `local/witnessed-values` + `local/content-validation` | collaborator |
| "audit compute / compute audit / what can be sped up / find slow scripts / where is sympy.simplify / LaurentQ wiring / BlockCache wiring" | `local/compute-audit` | collaborator |
| "coordinate / coordinate with PR / sibling PR / cherry-pick / cross-PR request" | `local/coordinate` | collaborator |
| "work on todos / process feedback" | `local/todo-review` | reader |
| "missing proof (narrative)" | `local/editor` §Proof workflow | collaborator |
| "missing proof (Lean)" | `local/formalizer` + `local/proof-triage` | collaborator |
| "test / unit test / coverage" | `local/test-engineer` | collaborator |
| "deploy / auth / OAuth / roles" | `local/deployment-auth` | owner |
| "import / arxiv / upload paper" | `local/paper-importer` | collaborator |
| "import + formalize" | `local/paper-importer` + `local/formalizer` | collaborator |
| "upload / scan / intake / process document" | `local/document-intake` | collaborator |
| "WHO / guideline / L1 / L2 / normative" | `local/document-intake` | collaborator |
| "uploads/ status / what's pending" | `local/document-intake` | collaborator |
| "critical path / trace dependencies" | `local/critical-path-analysis` | collaborator |
| "archimedean vs categorical / context audit" | `local/critical-path-analysis` | reader |
| "what assumptions does X need" | `local/critical-path-analysis` | reader |
| "separate categorical / split statement" | `local/critical-path-analysis` + `local/content-validation` | collaborator |
| "simulator / simulation / interactive viz" | `local/simulator` + `local/content-validation` | collaborator |
| "set up lean / install lean / lean not working" | `local/lean-environment-setup` | collaborator |
| "generate docs / build docs / schema docs" | `local/docs-generation` | reader |
| "build paper / compile PDF / render HTML" | `local/docs-generation` | reader |
| "TypeDoc / type docs / dependency graph" | `local/docs-generation` | reader |
| "diff / changes / what changed / undo" | `local/diff` | reader |
| "watch / watch main / watch upstream / watch this PR / watch branch X / what's landing" | `local/watch` | reader |
| "chapter complexity / reorder sections / backward edges / graph energy" | `local/chapter-complexity-review` | reader |
| "verify substrate / observations trace to U / substrate connectivity" | `local/verify-local-substrate` | reader |
| "dangling remarks / audit remarks / remark backing" | `local/remark-audit` | reader |
| "promote remark / add interprets / fix dangling" | `local/remark-audit` + `local/content-validation` | collaborator |
| "review / audit chapter or paper" | Tier 0 → Tier 1 (`peer-review`) → Tier 2 (`academic-paper-reviewer`) | reader (review) / collaborator (act) |
| "full review / devil's advocate" | `skill_fetch("academic-paper-reviewer")` (Tier 2) | collaborator |
| "publication readiness / final check" | All tiers: local + `peer-review` + `skill_fetch("academic-pipeline/integrity-verification")` | collaborator |
| "check claim / evidence quality" | `local/scientific-accuracy` → `sci-critical-thinking` → `skill_fetch("deep-research")` | reader |
| "fact-check / source verification" | `skill_fetch("deep-research")` (fact-check mode) | reader |
| "audit rendering / check rendering / rendering issues" | `local/rendering-auditor` | reader |
| "rendering QC / visual check / overfull hbox" | `local/rendering-auditor` | reader |
| "notation check / symbol audit / register compliance" | `local/rendering-auditor` (pass 2) + `local/ontologist` | reader |
| "fix rendering / rendering fix / quick fix" | `local/rendering-fixes` | reader |
| "check markdown render / GitHub view / proof markdown" | `local/markdown-render-check` | reader |
| "one voice / status leak / TODO in prose / strip emoji / scholarly voice" | `local/one-voice-audit` (sweep) + `local/one-voice-style-guide` (author voice profile) | collaborator |
| "coordinate PRs / sibling PRs / cross-PR / cherry-pick / inconsistent finding" | `local/coordinate` (or `/coordinate` slash command) | collaborator |
| "watch main / watch upstream / watch this PR / watch branch X" | `local/watch` | reader |
| "session todos / work plan / what's left / track progress" | `local/todo-manager` (session work-plan, TodoWrite) | reader |
| "process feedback / review todos / triage open feedback" | `local/todo-review` (content-feedback triage) | reader |

### External skill packages

Skills come from three sources, forming a tiered escalation model:

| Tier | Source | Location | Mechanism |
|------|--------|----------|-----------|
| **0 — Local** | `.claude/skills/local/` | On disk (repo) | Always available, run on every content change |
| **1 — K-Dense** | `K-Dense-AI/claude-scientific-skills` | On disk (synced nightly) | Read `SKILL.md` from `.claude/skills/claude-scientific-skills/<skill>/` |
| **2 — Academic** | `Imbad0202/academic-research-skills` | Fetched on demand | Call `skill_fetch` MCP tool; cached for 30 min |

**Tier 1 skills** (synced, for general scientific QC): `peer-review`,
`scientific-writing`, `scientific-critical-thinking`, `citation-management`,
`literature-review`, `hypothesis-generation`, `scientific-brainstorming`,
`arxiv-database`.

**Tier 2 skills** (fetched, for deep academic review):
`academic-paper-reviewer` (7-agent multi-perspective review),
`deep-research` (13-agent evidence grading / fact-check),
`academic-pipeline` (integrity verification protocol).

See `editor.md §External Academic Review` for the full escalation protocol,
delegation flows, and review-mode mapping.

### Skill role assignments

Every skill has a `roles:` field in its YAML frontmatter listing which
user roles may invoke it. The three roles form a hierarchy:
`reader < collaborator < owner`. Each role inherits all lower-role skills.

| Role | Skills |
|------|--------|
| `reader` | editor, content-validation, latex-validation, scientific-accuracy, readability-editing, proof-status-tracking, proof-gap-audit, todo-review, docs-generation, diff, watch, chapter-complexity-review, verify-local-substrate, remark-audit, rendering-auditor, rendering-fixes, markdown-render-check, witnessed-values |
| `collaborator` | All reader skills + formalizer, category-theory, lean-generation, lean-proof-review, lean-build-fix, lean-completeness-audit, proof-triage, proof-simplifier, proof-editor, proof-exposition-review, proof-narrative-lean-equivalence, proof-conciseness, chapter-analysis, content-block-review, ontologist, paper-importer, document-intake, test-engineer, lean-environment-setup, simulator, one-voice-audit, compute-audit, coordinate |
| `owner` | All collaborator skills + deployment-auth |

When a user connects via **Folio Assist** (chat), they default to `reader`
unless authenticated via GitHub OAuth (which grants `collaborator` or `owner`).
Agents coordinating sub-skills **must** check the user's role against each
skill's `roles:` list before routing.

**Decision tree**: (1) Check the user's role — only route to skills they
can access. (2) Does it touch content objects (`.ts` + `.md`)? →
`local/content-validation` + relevant content skill. (3) Does it touch `.tex`?
→ LaTeX skills. (4) Does it touch `.lean`? → Lean skills above. (5) Both
content + Lean? → also `local/lean-generation` for cross-refs. (6) Ambiguous?
→ read the skill `.md` files, then ask the user.

See **§12 Using Skills for Content Changes** in
`.github/copilot-instructions.md` for the full authoritative mapping,
including the detailed decision tree and Lean-specific routing table.

### Coding conventions

Follow the detailed rules in `.github/copilot-instructions.md` — they govern
LaTeX structure, labeling, cross-references, prose style, notation, and skill
usage for content changes.

### LP / SDP duals — first-class infra (do not skip)

Per `prop:operator-selection-lp` § *dual program*, every operator-
selection / shadow-price / knot-operator-selection compute MUST
emit BOTH primal and dual variables in its witness JSON:

| field | meaning |
|-------|---------|
| `y0_star` | shadow price of the net constraint |
| `y_star` | shadow prices of Frobenius positivity constraints (≥ 0) |
| `active_set` (or `active_constraints` / `active_channels`) | indices `i` with `y_star[i] > 0` |
| `primal_obj` | $\sum_i t_i x_i^*$ |
| `dual_obj` | $n_{\text{target}} \cdot y_0^*$ (= primal_obj by strong duality) |
| `duality_gap` | $|\text{primal\_obj} - \text{dual\_obj}|$ |

**Canonical entry point**:
[`folio-assistant/computations/lp_dual_solver.py`](folio-assistant/computations/lp_dual_solver.py)
exposes `solve_operator_selection_lp(t, G, n_target)` and
`solve_psd_operator_selection_sdp(t, G, n_target)`. Both return
a result whose `.to_dict()` contains all required fields.

**CI enforcement**:
[`folio-assistant/computations/lp_dual_witness_validator.py`](folio-assistant/computations/lp_dual_witness_validator.py)
runs in `witness-pipeline.yml` (warn-only by default; `--strict`
fails CI). Scans every `*.witness.json` whose name or
`description`/`computation` field signals an LP/SDP/operator-
selection compute and verifies the dual fields are present.

**Why this matters**: the dual variables ARE the binding-energy
shadow prices. The active demand channels (`y_star[i] > 0`) are
the "most receptive sub-braids" — they identify which Wedderburn
blocks the bound state actually saturates. Solving only the
primal loses this structural information, which has been the
historical pattern (58 of 58 LP/SDP witnesses on `main` lacked
the dual at the time this rule was added). Do not repeat this
pattern.

**Current baseline (2026-05-08, post-LP_SDP_HINTS tightening,
PR #565 F4):** the validator's hint list was deliberately narrowed
to `lp-dual` / `operator-selection-lp` / `shadow-price` /
`primal-dual` / `lp-duality` and now flags only **3** witnesses,
**all 3** of which include the LP dual. **0 of 37 wired
LP/SDP-flagged witnesses are missing duals.** The historical 58/58
figure refers to the pre-tightening hint list (which incorrectly
matched symbolic feasibility certificates and knot-particle probes
that do not compute LP duals). Going forward, treat the 3-of-3
set as authoritative; the 14 LP-solving scripts not on the hint
list are presumed `feasibility-only` (opt-out) until reviewed
per-file.

## Writing `.lean` proofs — rules for agents

These rules apply whenever an agent creates or modifies a `.lean` file.
Agents **must** follow all of them; violations will be caught by the
`content-block-review` skill.

### 0. Standardized root Lake workspace

The repo uses a **single root Lake workspace** (`/lakefile.toml`,
`/lean-toolchain`).  Each paper is a Lake **package** declared by
`[[require]]` with a short-form name:

| Package | Paper directory | Library module |
|---------|-----------------|----------------|
| `qou` | `content/quantum-observable-universe/lean/` | `QOU` |
| `ugb` | `content/unital-groebner-bases/lean/` | `UGB` |
| `fred2005` | `content/fred2005-formal-groups/lean/` | `Fred2005` |

**Preferred build commands** (always run from repo root):

```bash
lake build           # build every paper package
lake build QOU       # single paper library
lake exe cache get   # fetch Mathlib cache for the workspace
```

Per-paper `cd content/<paper>/lean && lake build` still works, but
root-workspace commands are the standardized entry point used by CI
(`lean_ci.yml`, `blueprint.yml`) and the MCP server (`lean_build`).

### 0a. Content-block `lean.ref` is a package-qualified URI

Every `lean:` field on a content block uses a package-qualified URI
of the form `"<package>:<Decl.Path>"`:

```ts
// definition in the qou package
lean: { ref: "qou:QOU.Torsion.lifting_exists" }

// cross-paper reference (ugb package)
lean: { ref: "ugb:UGB.GrobnerShirshov.Basis" }
```

- **Package prefix** must be one of `qou`, `ugb`, `fred2005` — see
  `folio-assistant/schemas/lean-packages.ts` for the registry and
  `parseLeanRef()` helper.
- The legacy `decl:` / `file:` shape is **removed**.  Validation fails
  on blocks that still use it.
- The pipeline resolves a `.lean` source file by: (1) sibling
  `<rootName>.lean`, (2) `<lakeRoot>/<Decl/Path>.lean` under the
  package's Lake root, (3) grep fallback on current branch.

To register a **new paper** as a Lake package: add a `[[require]]`
stanza to the root `lakefile.toml`, append to `LEAN_PACKAGES` in
`lean-packages.ts`, and add the library name to `defaultTargets`.

### 0b. Rebasing across the `lean.ref` migration — instructions for agents

If you are an agent working on an older branch and you **rebase or
merge onto a commit that contains this standardization**, your
content blocks may still use the legacy `lean: { decl: "...", file? }`
shape.  Zod validation will fail with a message pointing at this
procedure.  **Run the migration, do not hand-edit each block:**

```bash
cd content
bun run migrate-lean-refs        # apply (writes in place)
bun run migrate-lean-refs:dry    # preview only (no writes)
```

The script ([content/pipeline/migrate-lean-refs.ts](content/pipeline/migrate-lean-refs.ts))
is **idempotent** — safe to re-run after any rebase, merge, or
cherry-pick.  It rewrites every `lean: { decl: "<Decl>", file? }`
into `lean: { ref: "<pkg>:<Decl>" }` using the paper directory to
choose the Lake package prefix (see `LEAN_PACKAGES` in
`folio-assistant/schemas/lean-packages.ts`).

After the migration, re-run `bun run validate` to confirm the schema
is clean before continuing your task.  **Do not add `decl` back** to
unblock a merge — that field was removed from the schema on purpose.

If new `.lean` files were added on your branch, their content-block
`lean.ref` URIs must use the correct `<package>:` prefix for the
paper they live under.  Agents authoring new blocks should always
consult `LEAN_PACKAGES` for the list of valid prefixes.

### 1. Every `sorry` requires a bibliographic citation

```lean
-- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
sorry
```

- The `[key]` must match an entry in `content/schema/references.ts` exactly (case-sensitive).
  (`references.bib` is auto-generated — run `bun run export-bibtex` in `content/`).
- If no published reference exists, use `[manuscript]` and cite chapter/section.
- A `sorry` without `-- Ref:` is always a review failure.

### 2. Naming convention: LaTeX label → Lean declaration

| LaTeX label | Lean declaration | Rule |
|---|---|---|
| `thm:lifting-exists` | `QOU.Torsion.lifting_exists` | Hyphens → underscores |
| `def:quantum-connection` | `QOU.QuantumObservableUniverse.quantum_connection` | Namespace = chapter module |
| `def:categorical-instanton` | `CategoricalInstanton` | Type-level structures use CamelCase |
| `prop:categorical-dq-squared` | `categorical_dq_squared` | Theorems/lemmas use snake_case |

All declarations live under the `QOU` root namespace.

### 3. Block kind determines Lean requirements

| Block kind | `.lean` file required? |
|---|---|
| `definition` | **Yes** — enforced; will not build without it |
| `theorem`, `lemma`, `proposition`, `corollary` | **Expected** — warning if missing |
| `conjecture` | **Optional but encouraged** — `sorry` = conjecture (see §3b) |
| `example`, `remark` | Optional |
| `simulator` | N/A |
| `prose`, `equation`, `diagram` | N/A |

### 3b. Conjectural propagation and Lean formalization of conjectures

**Conjectural propagation rule (STRICT, with conditional-class
exception per §3b-cond below):** A statement that depends on (is
downstream of) a conjecture **cannot** be a `theorem`,
`proposition`, `lemma`, or `corollary` *unless* it satisfies the
conditional-class exception (§3b-cond). Only statements proved
from established results (definitions, previously proved theorems,
axioms) — or proved from explicit conditional hypotheses — may
use provable block kinds.

- If `uses[]` contains a `conj:` label (directly or transitively),
  the block **must** be either:
  - kind `conjecture`, or
  - a provable kind satisfying the **conditional-class exception**
    (§3b-cond) — i.e. the conjecture is axiomatised as a Lean
    class and the downstream block's Lean statement carries that
    class as an explicit `[Instance]` hypothesis.
- "Proof" blocks downstream of conjectures (without conditional-
  class) become `remark` blocks with `interprets: "conj:..."`
  (proof *sketches*, not proofs).
- `remark` blocks may freely interpret conjectures (they make no
  logical claims).

#### §3b-cond — Conditional-class exception (Option B, 2026-05-02)

A `theorem`/`proposition`/`lemma`/`corollary` block whose `uses[]`
cone transitively touches a `conj:C` may keep its provable kind
**iff all of**:

1. **Class axiomatisation.** `conj:C` has a Lean
   `class C` declaration in its `.lean` file, with class fields
   encoding the conjecture's content. The class instance is
   the only `sorry` in the entire downstream chain.
2. **Explicit hypothesis on Lean side.** The downstream block's
   Lean declaration has the class as an explicit `[Instance]`
   hypothesis. Example:
   ```lean
   theorem downstream_result {M : Type*} [C M] : … := by
     -- proof uses C.field1, C.field2 as hypotheses; otherwise
     -- fully verified by Lean.
   ```
3. **Explicit conditional banner on narrative side.** The `.md`
   block opens with: **Theorem (conditional on
   [`conj:C`](path/to/C.md)).** The body cites the conjectural
   hypothesis where used.
4. **`uses[]` includes the conjecture explicitly.** The
   conditional dependency is auditable from the manifest.

When all four hold, the block represents a *rigorous conditional
result* — fully verified by Lean modulo a single, named,
class-axiomatised conjectural input. This pattern preserves the
distinction between rigorous-conditional and unproved-conjecture
content.

**Audit treatment.** The `conjectural-propagation` audit
(`content/pipeline/conjectural-propagation-audit.ts`) reports such
blocks separately as **conditional-on-class** rather than as
violations. To opt a block into this status, ensure its Lean
declaration contains a class hypothesis matching one of the
conjectures in its transitive `uses[]` cone, and confirm the
narrative banner. The audit script will detect the pattern and
classify the block accordingly.

(Pre-existing CLAUDE.md text continues from line 335.)


**Definitions and conjectures (clarification):** The propagation
rule above applies to **provable claims** (`theorem`, `proposition`,
`lemma`, `corollary`). It does **not** force `definition` blocks to
become conjectures even if their `uses[]` includes a `conj:` label.
A definition names a construction; whether the named construction
is "the right one" may itself be a conjecture, but the act of naming
is not a logical claim.

However:

- A `definition` whose well-formedness genuinely depends on a
  conjecture (e.g. defining "the unique X with property P" when P's
  uniqueness is conjectural) **should** carry an explicit narrative
  note in its `.md` flagging the conjectural backing, and should
  cite any computational witnesses available
  (`folio-assistant/computations/*.witness.json`) so empirical
  support is discoverable from the manifest.
- Any `theorem`/`proposition`/`lemma`/`corollary` whose `uses[]`
  cites such a definition **does** trigger propagation — it is
  downstream of the conjecture transitively. Track the chain via the
  definition.

Audit note: the `proof-gap-audit` skill must apply §I of its
checklist (conjectural propagation) only to provable kinds. Flagging
a definition as a propagation violation is a false positive (we have
seen this hallucinated by sub-agents). Compute the transitive cone
from any provable block; if it touches a `conj:` via any path
(including through definitions), demote the provable block.

**Lean formalization of conjectures:** Conjectures *can* (and should,
when feasible) have `.lean` files.  The convention is:

1. **The conjecture itself** is axiomatized as a Lean `class` with
   fields encoding its content.  The `sorry` in any instance is
   understood as **conjecture**, not missing proof.

2. **Downstream conjectures** (conditional on the upstream conjecture)
   take the upstream class as a `[instance]` hypothesis and prove
   the conditional result: "if the conjecture holds, then..."
   These downstream proofs are **fully verified** by Lean — the
   only unproved input is the class instance itself.

3. **The dependency chain** is visible in Lean: definitions →
   conjecture (axiom class) → downstream conjectures (conditional
   theorems).

Example pattern:
```lean
-- The conjecture (sorry = conjecture)
class MyConjecture (M : Type*) where
  functor : FooData M → BarData M
  compatibility : ∀ x, ...

-- Downstream conjecture: proved conditional on MyConjecture
theorem downstream_result {M : Type*} [MyConjecture M]
    (x : FooData M) : ... :=
  MyConjecture.compatibility x
```

### 3a. Remark authoring convention — no dangling remarks

Every `remark` block must have **formal backing**. The correct
authoring structure is:

```
definition / proposition / lemma / theorem   (.lean: formal statement)
  └→ proof block                             (.lean: formal proof)
       └→ remark block                       (.md: interpretation)
            └→ example / simulator           (concrete instances)
```

**Rules:**

1. **Interpretive remarks** must set `interprets: "prop:foo"` (or
   `"def:foo"`, `"thm:foo"`, etc.) linking to the provable block
   they interpret. The `.md` content provides physical interpretation,
   motivation, or examples — not new mathematical claims.

2. **Glossary remarks** (Ch 8 only) are exempt — they wrap Mathlib
   types and carry the `"glossary"` tag.

3. **Prose blocks** (`prose`) are for pure exposition with no logical
   content (intros, abstracts, transitions). Use `prose`, not `remark`,
   when there is no provable statement behind the text.

4. A remark that makes a **mathematical claim** without `interprets`
   is a **dangling remark**. Resolve by:
   - **Promoting** the claim to `proposition` / `lemma` (with Lean)
   - **Linking** via `interprets` to an existing provable block
   - **Demoting** to `prose` if there is no logical content

5. **Ambiguous physics terms** (energy, force, particle, degeneration,
   etc.) in remark `.md` files must reference the corresponding
   categorical definition via `uses[]`. Physics terms without
   categorical backing are flagged by the `remark-audit` skill.

**Audit tool:** `cd content && bun run pipeline/find-dangling-remarks.ts`

**Constraint rules:** `remark-interprets` (warns on missing
`interprets`), `interprets-resolve` (errors on broken reference).

### 4. Formalization status is derived, not stored

Formalization status (`not_started`, `stated`, `has_sorry`, `proved`,
`mathlib_ok`) is **not stored in `.ts` manifests**. It is derived at
build time by CI scripts from `.lean` file content and Lean build output,
then written to `proof-objects.json`. Agents must **never** add a `status`
field to content block `.ts` files.

### 4a. TodoItem lifecycle rules

Content TODOs are **external to paper content**. They live in `todos/`
(gitignored — survives branch switches), referencing content blocks via
`targetLabel`. This keeps the paper source clean and avoids confusion
between scholarly content and work-tracking metadata.

```
todos/                           ← gitignored
  content-todos.ts               ← content-related todos
  infra-todos.ts                 ← infrastructure todos (optional)
```

The `TodoItem` type is defined in `content/schema/types.ts` for reuse,
but no `todos` field exists on any content block type or schema.

The MCP server serves todos at `/api/todos` (JSON) and `/todos` (HTML
dashboard). The `check-todos.sh` SessionStart hook summarizes open
items at the start of each session.

| Action | Who may do it |
|--------|--------------|
| **Create** a TodoItem | Agent or human |
| **Update** status to `in_progress` | Agent or human |
| **Resolve / close** a TodoItem (`resolved`, `wontfix`) | **Human only** |
| **Remove** a TodoItem from the array | **Human only** |

Agents **must never** set a TodoItem's status to `resolved` or `wontfix`,
and **must never** delete a TodoItem. The author verifies completion —
even after a commit has been made — and closes the item themselves.
Agents may add new TodoItems and may move items to `in_progress`, but
closing is always a human action.

### 4b. Glossary block policy (Chapter 8)

Chapter 8 ("Glossary of Rigid Monoidal Terms") contains **glossary
blocks** — `remark` blocks with tag `"glossary"` — that map paper
terminology to canonical Mathlib declarations. These are light
terminological wrappers: **no semantic novelty**, just naming
conventions.

| Criterion | Glossary block | Definition block |
|-----------|---------------|-----------------|
| Semantic novelty | None (Mathlib synonym) | New mathematics |
| Block kind | `remark` | `definition` |
| Label pattern | `rem:glossary-<term>` | `def:<term>` |
| Lean file | Not required | **Required** |
| Chapter | Ch 8 | Relevant content chapter |

**Decision rule**: If the paper uses a term that is a synonym for (or
lightweight wrapper around) a Mathlib type, add a glossary block. If
the paper introduces genuinely new axioms/structure, add a definition.

### 4c. Glossary terms — `\defterm` / `\refterm` (every occurrence wrapped)

Every term registered in any block's `defines: [...]` field **must** be
wrapped at every occurrence — `\defterm` once at the canonical site,
`\refterm` everywhere else. Plain text and `\emph{}` are no longer
permitted for defined terms. See
`.github/copilot-instructions.md §11.0` for the full contract.

- **Markdown** (`.md`): use the `remark-directive` syntax
  `:defterm[Visible]{#slug}` / `:refterm[Visible]{#slug}` — short
  forms `:defterm[term]` / `:refterm[term]` use the bracket text as
  both label and slug.
- **LaTeX**: use `\defterm{slug}[{Visible}]` / `\refterm{slug}[{Visible}]`.
- **Validation**: `bun run validate <paper>` enforces five rules
  (`defterm-declared`, `defterm-marked`, `refterm-resolves`,
  `defterm-unique`, plus opt-in `term-mention-coverage` via `--strict`).
  Run with `--strict` once the chapter has been backfilled.
- **Codemod**: `bun run pipeline/codemod-refterm.ts <chapter-dir>`
  (dry-run by default) wraps bare-text mentions of known glossary
  slugs in `:refterm[…]{#slug}`. Mdast-based, idempotent. Pass
  `--write` to apply.
- **Glossary build**: `bun run pipeline/build-glossary.ts <paper>`
  emits `glossary.json` (committed) + `chapters/glossary.tex`
  (gitignored). `--check` mode is the CI gate.

### 5. Tactic strategy (try in order)

| Goal pattern | Try first | Then try |
|---|---|---|
| Algebraic identity (`x = y`) | `ring` | `field_simp; ring` |
| Non-negativity (`0 ≤ x`) | `positivity` | `linarith` |
| Numeric (`x < y`) | `norm_num` | `linarith` |
| Definitional equality | `rfl` | `unfold …; rfl` |
| Diagram / naturality | `aesop_cat` | `slice_lhs`, `slice_rhs` |
| Anything else | `simp` | `aesop` |

### 6. Use MCP tools, not shell commands

| Task | Use this | Not this |
|---|---|---|
| Check errors | `lean_diagnostic_messages` | `lake build` + parse |
| Read goal state | `lean_goal` | Python scripts |
| Search Mathlib | `lean_leansearch` / `lean_loogle` | grep Mathlib source |
| Try tactics | `lean_multi_attempt` | edit-build-repeat |
| Axiom audit | `lean_verify` | manual inspection |

### 7. Category theory conventions

- **Category notation**: Use bold `$\mathbf{C}$` for categories
  (Herrlich–Strecker style), never calligraphic `$\mathcal{C}$`.
  Named categories are also bold: `$\mathbf{Rep}(\mathrm{SU}_q(2))$`.
  Calligraphic letters are reserved for sheaves, sites, algebras,
  bundles, and curves (`$\mathcal{S}$` = state bundle,
  `$\mathcal{E}_q$` = elliptic curve, `$\mathcal{O}$`, `$\mathcal{A}$`).
- **Fibre functor**: Always `$\tau$` (not `$\omega$` or `$U$`).
  Minimise its appearance — write `$(\mathbf{C}, A)$` when the functor
  is not needed; write `$(\mathbf{C}, A, \tau)$` only when `$\tau$` is
  explicitly used.
- **QOU archimedean tuple**: `$(\mathbf{C}, \varTheta, G, \mathcal{S})$`.
  The old 5-tuple $(M, \varTheta, G, P, E)$ is **deprecated**.
  - $M$ (base manifold) is subordinate to $\varTheta$ (its domain).
  - $P$ (principal bundle) is subordinate to $\mathcal{S}$ (frame bundle
    of the state bundle under $G$). Mention $P$ only when discussing
    gauge structure directly.
  - $\mathcal{S} = P \times_G \mathbb{CP}^1(\mathbb{C}) \to M$ is the
    associated state bundle; replaces $E$.
- Functors are bundled: `F.obj X`, `F.map f` — never treat `F` as a function.
- Open `CategoryTheory.MonoidalCategory` for notation: `X ⊗ Y`, `𝟙_ C`,
  `α_`, `λ_`, `ρ_`, `X ◁ f`, `f ▷ X`.
- Diagram commutativity: try `aesop_cat` first, then `slice_lhs`/`slice_rhs`.
- Use `Subsingleton (X ⟶ Y)` for vanishing hom-spaces (avoids `Preadditive`).

### 7aa. Notation register (STRICT) — see content notation block

The authoritative source for every mathematical symbol used in the
paper is the front-matter **Notation** chapter, rendered into the
PDF immediately after the table of contents:

- **Per-chapter symbol tables**:
  [`content/quantum-observable-universe/notation/notation-register.md`](content/quantum-observable-universe/notation/notation-register.md)
- **Collision avoidances + conventions**:
  [`content/quantum-observable-universe/notation/notation-collisions.md`](content/quantum-observable-universe/notation/notation-collisions.md)

Agents **must** treat those `.md` files as authoritative when picking
a font/symbol for a concept. When adding a new symbol convention,
edit the content block — not this section. CLAUDE.md mirrors only a
short summary below; the content block is what readers see in the
PDF and what `rendering-auditor`, `ontologist`, and Gemini-style
review tools should cite.

#### Summary (for quick agent lookup)

The register groups symbols by the chapter where each is **first
introduced**; entries within a chapter are sorted alphabetically by
concept name. Below is a flat per-chapter summary; for the full
table with usage notes, open the content block above.

#### algebraic-substrate

| Concept | Font | Symbols |
|---------|------|---------|
| $q$-shuffle Hopf algebra | calligraphic | `$\mathcal{H}_q$` — convolution algebra of $\mathrm{End}_{\mathbf{C}}(A)$ under $\ast_q$; carries the grouplikes $\exp_q, \log_q, \mathrm{Li}_2^q$. **Never** plain `$H_q$` (collides with Hecke and Hamiltonian). |
| Vortex morphism | Greek | `$\varrho \colon \mathbf{1} \to A$` (generic closed vortex). **Never** `$\gamma$` for vortex; `$\gamma$` is reserved for Euler–Mascheroni or Dirac matrices. |

#### braids-and-knots

| Concept | Font | Symbols |
|---------|------|---------|
| Crossing energy | plain italic | `$E_{\mathfrak{H}}$` (total crossing energy of hadron $\mathfrak{H}$). `$E_{\mathfrak{H}} = \mathfrak{m}_{\mathfrak{H}} \cdot c_q^2$`. |
| Hook-length product | Latin cap + arg | `$H_q(\lambda) = \prod_{x \in \lambda} [h_x(\lambda)]_q$` — always with partition argument; unambiguous in knot/partition contexts. |
| Iwahori–Hecke algebra | Latin cap | `$H_n(q)$` — always with subscript $n$; standard knot-theory convention (Kassel, Jones). |
| Jones–Markov central coefficient | plain italic | `$y_\lambda$` — coefficient in $\mathrm{tr}_M = \sum_\lambda y_\lambda \chi_\lambda$ ([procedure](#prop:alpha-k-derivation-procedure)). Sign-indefinite at $n \geq 4$. **Never** confuse with $u_\lambda$ (LP shadow-price). |
| LP shadow-price | plain italic | `$u_\lambda, u_0$` (Schrijver linear-programming convention) for operator-selection LP dual variables ([BW shadow price](#prop:bw-coefficient-shadow-price)). Non-negative by LP duality. **Never** write `$y_\lambda$` here (collides with Jones–Markov). |
| Markov parameter | plain italic | `$z = 1/(q^{1/2} + q^{-1/2})$` |
| Mass | fraktur | `$\mathfrak{m}_{\mathcal{K}}$` (knot mass). |

#### descartes-universe

| Concept | Font | Symbols |
|---------|------|---------|
| Elliptic curve | calligraphic | `$\mathcal{E}_q$` (Descartes elliptic curve). **Never** write `$E_q$` for a curve. |
| Gravitational constant | Latin cap | `$G(q)$` (gravitational constant), `$G_{\mathrm{Planck}} = 1$` (Planck-normalised, exact). |
| Julia-set measure | Greek | `$\mu_J$` (measure on Julia set) |
| Weierstrass | fraktur cap | `$\wp(z)$` (Weierstrass elliptic function on `$\mathcal{E}_q$`). Reserved symbol — never repurpose `$\wp$`. |

#### information-theory

| Concept | Font | Symbols |
|---------|------|---------|
| Entropy (operational) | Greek | `$\eta_q = (2q-1)/q^3$` |
| Information bandwidth | calligraphic | `$\mathcal{B}(q)$` (information bandwidth per Planck time) |
| Lyapunov exponent | Greek | `$\chi_q = 1/(2q-1)$` ($q$-deformed Lyapunov). Distinct from $\chi_\zeta(c)$ (character). |

#### observations

| Concept | Font | Symbols |
|---------|------|---------|
| Derived constants | plain italic | `$c_q = 1/(q-1)$` (speed of light), `$\hbar_q = (q-1)/q$` (Planck constant), `$d_H(q) = (2q-1)^2/q^3$` (Hausdorff dimension) |
| Mass number | Latin cap | `$A = Z + N$` |
| Neutron number | Latin cap | `$N$` |
| Particles | fraktur | `$\mathfrak{u}, \mathfrak{d}, \mathfrak{s}, \mathfrak{c}, \mathfrak{b}, \mathfrak{t}$` (quarks), `$\mathfrak{p}, \mathfrak{n}$` (proton, neutron), `$\mathfrak{H}$` (hadron), `$\mathfrak{H}_p$` (localized hadron) |
| Proton number | Latin cap | `$Z$` (atomic number). **Never** use `$p$` for proton count; `$p$` is reserved for brane points. |

#### particle-interactions

| Concept | Font | Symbols |
|---------|------|---------|
| $C_5$ invariants | functional | `$p_1(c)$` (power sum), `$h_2(c), h_3(c)$` (Hermitian), `$\chi_\zeta(c)$` (character) |
| Color | plain italic | `$c$` (color vector), `$c_r, c_g, c_b$` (tube coords), `$\hat{c}, \hat{c}_r$` (chromaticity) |
| Energy | bold | `$\mathbf{E}_q$` ($q$-energy), `$\mathbf{E}_\times$` (crossing energy), `$\mathbf{E}_{\mathrm{bind}}$` (binding). **Never** `$\mathfrak{E}$`. |
| Mass (categorical) | fraktur | `$\mathfrak{m}$` (categorical mass), `$\mathfrak{m}_{\mathfrak{H}}$` (hadron mass). **Never** plain `$m$` for categorical mass. |
| $q$-Hamiltonian | hat | `$\hat{H}_q$` (operator hat, Dirac convention). **Never** plain `$H_q$`. Distinct from `$\mathcal{H}_q$` (shuffle algebra) and `$H_n(q)$` (Hecke). |

#### quantum-observable-universes

| Concept | Font | Symbols |
|---------|------|---------|
| Bundles / sheaves | calligraphic | `$\mathcal{S}, \mathcal{O}, \mathcal{L}, \mathcal{A}$` |
| State bundle fibre | calligraphic | `$\mathcal{S}_p$` — the fibre of `$\mathcal{S}$` at brane point $p$. **Never** write `$E_p$`. |

#### quantum-universes

| Concept | Font | Symbols |
|---------|------|---------|
| Categories | bold | `$\mathbf{C}$`, `$\mathbf{Rep}$` |
| Lie algebras | fraktur lc | `$\mathfrak{su}(2), \mathfrak{g}$` |

**Key collision avoidances:**
- `$c$` = color (never charm; charm is `$\mathfrak{c}$`)
- `$b$` = generic variable (never bottom quark; bottom is `$\mathfrak{b}$`)
- `$p$` = brane point (never proton number; proton number is `$Z$`)
- `$E$` alone = **not used** for exceptional divisor, energy, or elliptic curve.
  Use `$\mathcal{S}_p$`, `$\mathbf{E}$`, or `$\mathcal{E}_q$` respectively.
  `$E_{\mathfrak{H}}$` (with hadron subscript) is allowed for crossing energy.
- `$\gamma$` = Euler–Mascheroni constant or Dirac matrices only.
  **Never** use `$\gamma$` for a vortex or closed cycle; use `$\varrho$`.
- `$\chi_q$` = Lyapunov exponent (distinct from `$\chi_\zeta(c)$` = character)
- `$H_q$` alone = **not used**. Three distinct concepts share the letter $H$: `$\mathcal{H}_q$` (shuffle Hopf algebra), `$\hat{H}_q$` (Hamiltonian operator), `$H_n(q)$` or `$H_q(\lambda)$` (Hecke/hook-length, always with argument).
- `$q = 1.1097$` (or any specific numerical value of the substrate
  parameter) **must not appear** outside the introduction and
  Chapter 7 (Physical Observations). Geometry chapters use symbolic `$q$`.
  Exception: Chapter 9 (Information Theory) may use numerical `$q$` for
  falsifiability computations.

### 7ab. Observed / derived values — approximation convention (STRICT)

When stating a numerical value derived from the substrate parameter
`$q_0$` or compared to experimental data, **always** use `$\approx$`
(or `$\simeq$`), **never** `$=$`.

```latex
% WRONG — implies exact equality
$\mathfrak{m}_{\mathfrak{p}}(q_0) = 938.272\;\text{MeV}$

% RIGHT — derived approximation
$\mathfrak{m}_{\mathfrak{p}}(q_0) \approx 938.272\;\text{MeV}$
```

**Exception:** You may write `$=$` when an explicit error term is
present:

```latex
% OK — error term makes precision explicit
$\mathfrak{m}_{\mathfrak{p}}(q_0) = 938.272 + O(10^{-3})\;\text{MeV}$
```

This applies to all physical predictions, CODATA comparisons, and
numerical evaluations at `$q_0$`. Exact algebraic identities
(e.g. `$c_q = 1/(q-1)$`) use `$=$` since they hold for all `$q$`.

### 7a. Hecke-Skein convention (STRICT)

The Hecke algebra generator is **$\sigma_i$** (never $T$, never $t$ or
$A$ for the Jones polynomial variable). The Iwahori–Hecke algebra
$H_n(q)$ is presented as a quotient of the braid group algebra of
$B_n$, so the same symbol $\sigma_i$ is used for the braid group
generator and its image in $H_n(q)$ — context disambiguates.

- **Hecke relation**: $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$, equivalently
  $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$.
- **Skein relation**: Multiply the Hecke relation by $\sigma_i^{-1}$ to
  get $\sigma_i - \sigma_i^{-1} = q - q^{-1}$, which is the Skein
  relation $L_+ - L_- = (q - q^{-1})\,L_0$.
- **Translation dictionary**:
  - $\sigma_i$ = positive crossing $L_+$
  - $\sigma_i^{-1}$ = negative crossing $L_-$
  - $1$ = smoothed crossing $L_0$
  - $q$ and $-q^{-1}$ are the eigenvalues of $\sigma_i$ (symmetric and
    antisymmetric channels respectively)
- **Jones polynomial**: Always $J_K(q)$, never $V_K(t)$ or bracket
  with variable $A$.  The Jones polynomial is the Markov trace
  $J_L(q) = \mathrm{tr}_M(\rho(\beta_L))$ in $H_n(q)$.
- **Braid vs Hecke**: $\sigma_i$ denotes both the braid-group generator
  in $B_n$ and its image in $H_n(q)$; the latter satisfies the Hecke
  relation above while the former satisfies only the braid relations.
  This shared notation follows the standard knot-theory convention
  (Kassel, Jones).

### 7b. Symmetric-crystal techniques (KLR / Kashiwara) — authoring guidance

When **expanding the QOU formalization** or **updating the GS / Hecke
reduction engine**, prefer these symmetric-analogue constructions over
custom combinatorial machinery. Each one is a structural shortcut that
buys a categorical guarantee for free.

1. **Type B folding for chirality / CPT.** To enforce matter–antimatter
   pairing structurally in the reduction engine, do not write custom
   $\mathbb{Z}/2\mathbb{Z}$ rules. Fold the $\mathfrak{sl}_n$ Cartan
   datum into a Type B datum; the resulting Kashiwara graph is a
   *symmetric crystal*, and its GS normal forms are bar-involution
   ($q \mapsto q^{-1}$) invariant by construction. Stable matter =
   fixed points of the folded crystal.

2. **Decategorifying to KL bases for the classical limit.** The
   transition from quantum braiding to macroscopic statistics
   (Pauli / Bose–Einstein) is the functor mapping the KLR canonical
   basis to the Kazhdan–Lusztig basis of $S_n$. Define the classical
   limit of fluid dynamics via this functor — do not abandon the
   categorical substrate to recover ordinary statistics.

3. **Demazure sub-crystals for resonances.** Unstable intermediaries
   (W/Z bosons, hadronic resonances, virtual particles) are Demazure
   sub-crystals — incomplete topological states. Their non-symmetric
   Macdonald-polynomial evaluation under the Observation Frame
   ($\tau$ / Markov trace) reproduces the broken symmetry of a
   short-lived state without ad-hoc decay machinery.

These directives are **authoring shortcuts**, not new content. Apply
them when implementing a feature whose first instinct would be a
hand-rolled combinatorial rule; the symmetric-crystal route gives the
correct algebraic answer with less code and an audit trail to the
KLR / Kashiwara literature (Brundan–Kleshchev, Kashiwara, Lecouvey).

### 8. File hygiene

- Never commit `.lake/`, `lake-packages/`, or `build/`.
- **Pin external dependencies to commit hashes** in `lakefile.toml` —
  never use branch names (`main`, `master`) or version tags (`v4.16.0`).
  Mathlib version numbers ≠ Lean version numbers; tags can resolve to
  unexpected toolchain versions.
- **All deps must agree on the same `lean-toolchain`**. Before adding or
  updating a dep, check `cat .lake/packages/<dep>/lean-toolchain` for
  every package. If any disagree, find compatible versions first.
  See `formalizer.md § Adding New Dependencies` for the full procedure.
- To recover from broken `.lake/`, use `mv .lake /tmp/...` (not `rm -rf`).
- Keep imports minimal — only import what the file actually uses.
- The `.lean` sibling file must share the same root name as its `.ts`/`.md`
  siblings (e.g., `rigid-monoidal-category.lean`).

## Content-object architecture

Content is organized as **atomic knowledge units** — each definition,
theorem, remark, etc. is a self-contained file triple:

```
content/
  <paper-name>/
    <paper-name>.ts              ← Paper manifest (references chapter URIs)
    <chapter-dir>/
      <chapter-dir>.ts           ← Chapter manifest (sections → block refs)
      <block-name>.ts            ← Typed manifest (kind, label, lean ref, status)
      <block-name>.md            ← Narrative content (markdown + TeX snippets)
      <block-name>.lean          ← Lean formalization (when required by kind)
```

### File naming convention

Sibling files share the same root name: `rigid-monoidal-category.ts`,
`rigid-monoidal-category.md`, `rigid-monoidal-category.lean`.

### Type system

| Block kind | Lean required? | Label prefix |
|-----------|---------------|-------------|
| `definition` | **Yes** (enforced at type level) | `def:` |
| `theorem`, `lemma`, `proposition`, `corollary` | Expected (warning if missing) | `thm:`, `lem:`, `prop:`, `cor:` |
| `conjecture`, `example`, `remark` | Optional | `conj:`, `ex:`, `rem:` |
| `simulator` | N/A | `sim:` |
| `prose`, `equation`, `diagram` | N/A | — |

### Pipeline

```
.ts manifests + .md content
  → Zod schema validation (shape + types)
  → Constraint rules (file existence, cross-refs, lean requirements)
  → LaTeX rendering (markdown → LaTeX conversion)
  → AST validation (unified-latex parse of rendered output)
  → chapters/*.tex output
```

### Key files

| Path | Purpose |
|------|---------|
| `content/schema/types.ts` | TypeScript types (discriminated unions) |
| `content/schema/constraints.ts` | Zod schemas + constraint rules |
| `content/schema/builders.ts` | `definition()`, `theorem()`, `prose()`, etc. |
| `content/pipeline/validate.ts` | Three-level validation |
| `content/pipeline/render-latex.ts` | Block → LaTeX + AST validation |
| `content/pipeline/build.ts` | Full document build |
| `content/schema/references.ts` | **Bibliography source of truth** (CSL-JSON) |
| `content/pipeline/export-bibtex.ts` | Generates `references.bib` from CSL-JSON |
| `content/pipeline/validate-references.ts` | Bibliography + citation cross-checks |
| `content/pipeline/citations.ts` | `\cite{}` extraction from .md content |
| `content/pipeline/find-dangling-remarks.ts` | Audit: find remarks without `interprets` |

### Bibliography architecture

The bibliography is managed as **typed CSL-JSON** in
`content/schema/references.ts`. BibTeX (`references.bib`) is a downstream
render target, auto-generated by `bun run export-bibtex`.

- **Adding a reference**: use the `ref()` builder in `references.ts`
- **Block citations**: `cites: string[]` field on blocks (auto-extracted
  from `\cite{}` in .md by the pipeline, or set explicitly in .ts)
- **Chapter bibliography**: aggregated at build time from all block cites
- **Validation**: `bun run validate-refs` checks schema, uniqueness, DOIs,
  and cross-references against Lean `-- Ref:` and LaTeX `\cite{}`
- **Never edit `references.bib` directly** — it is regenerated on build

### Dependency graph integration

The `uses[]` field lists **immediate neighbors only** — direct
dependencies, not transitive ones.  If A→B and B→C, then A lists
only B; C is reachable by walking the graph.  Run
`bun run pipeline/prune-transitive-deps.ts` to enforce this.

The `uses[]` field in content objects + Lean import graphs form a
combined dependency DAG. Editors and proof-writers use this to:

- **Track upstream changes**: when a definition changes, find all
  theorems/lemmas that `uses` it and flag them for re-validation
- **Track downstream impact**: when proposing a change, identify all
  blocks that depend on the changed block
- **Scope test runs**: only run Lean builds / AST validation for the
  changed block and its downstream dependents
- **Prioritize formalization**: find blocks with the most dependents
  that are still `not_started`

### Cross-paper references

The `uses[]` field supports three reference scopes:

| Scope | Syntax | Example |
|-------|--------|---------|
| Same paper | bare label | `"def:quantum-universe"` |
| Same folio | `"paper-dir:label"` | `"unital-groebner-bases:cor:pbw"` |
| External folio | full URL | `"https://folio.example.org/viewer/#/view/paper-id"` |

Cross-paper refs are validated at folio level, not per-paper. The
`uses-resolve` constraint skips qualified refs (those matching
`paper-dir:label` or starting with `https://`).

Each paper in `content/folio.ts` has an optional `url` field for
viewer routing. CSL-JSON entries in `content/schema/references.ts`
for folio-hosted papers include a URL field matching the viewer hash route
(e.g. `/viewer/#/view/unital-groebner-bases`).

### Markdown content convention (in .md files)

- Inline math: `$...$`
- Display math: `$$...$$`
- Complex TeX (tikzcd, align): fenced code block with `` ```tex `` tag
- Bold → `\textbf{}`, italic → `\emph{}` in LaTeX output
- Cross-refs: `[text](#label)` → `\hyperref[label]{text}`

### TeX authoring patterns for agents

These rules prevent rendering errors in the content pipeline.
Violations produce broken LaTeX in titles, captions, and body text.

**1. Math in titles is supported.** Block titles (in `.ts` manifests)
may contain inline math. The `escapeLatex()` function preserves
`$...$` segments verbatim. Always use `$...$` delimiters:

```ts
// CORRECT — math preserved in rendered \begin{example}[{...}]
title: "Reeb derivation for $\\mathrm{SU}(2)$"

// WRONG — bare LaTeX commands will be escaped to garbage
title: "Reeb derivation for \\mathrm{SU}(2)"
```

**2. Multi-line inline math is valid.** The remark-math parser handles
`$...$` spanning multiple lines. This is the standard pattern for long
inline expressions in list items:

```md
1. **Cyclicity**: $\mathrm{tr}_{\mathrm{Ad}}(f \circ g) =
   \mathrm{tr}_{\mathrm{Ad}}(g \circ f)$, inherited from the
   Frobenius relation.
```

**3. Never use raw TeX commands in prose outside `$...$`.** The markdown
→ LaTeX converter only passes through content inside math delimiters
or `` ```tex `` fenced blocks. Bare `\mathrm{...}` outside delimiters
renders as literal text.

**4. Use `$$...$$` on separate lines for display math.** The `$$`
delimiter must be alone on its line (or at the very start/end):

```md
The formula is:

$$
  \nabla^2 \phi = 0
$$
```

**5. For complex environments (tikzcd, align), use fenced tex blocks:**

````md
```tex
\begin{tikzcd}
  A \arrow[r] & B
\end{tikzcd}
```
````

**6. Ampersands in math are fine.** The `&` character inside `$...$` or
`` ```tex `` blocks is not escaped (it's a column separator in matrices
and alignments). Only `&` in prose text causes LaTeX errors.

## Lean MCP server (lean-lsp-mcp)

The [lean-lsp-mcp](https://github.com/oOo0oOo/lean-lsp-mcp) server is
configured via `.mcp.json`. It provides Claude Code with:

- Diagnostics, goal states, hover docs, completions
- LeanSearch, Loogle, Lean Finder, Lean Hammer search tools
- Code actions ("Try This"), profiling, axiom verification
- Local project search (requires ripgrep)

### Setup (ChromeOS / Crostini)

Prerequisites: `git`, `curl`.

Use the `lean_setup` MCP tool (provided by paper-assistant). It installs:
uv, elan, the Lean toolchain pinned in the **root** `lean-toolchain`,
Mathlib cache, ripgrep, and runs `lake build` in the **root Lake
workspace**.

Alternatively, from the command line:

```bash
# Build every paper at once from the root workspace
lake exe cache get && lake build

# Or build a single paper package
lake build QOU        # quantum-observable-universe
lake build UGB        # unital-groebner-bases
lake build Fred2005   # fred2005-formal-groups
```

### Local Mathlib cache

To avoid re-cloning Mathlib from GitHub on every fresh `.lake/` build,
keep a persistent local clone one directory above the repo:

```bash
cd ..  # parent of the repo root
git clone https://github.com/leanprover-community/mathlib4.git
```

The build tools automatically detect this clone (configured in
`lean-mcp.config.json` → `lean.local_mathlib_path`) and set a git
`insteadOf` redirect so Lake fetches from the local clone instead of
GitHub. This is transparent — no changes to `lakefile.toml` needed.

| Config key | Default | Purpose |
|-----------|---------|---------|
| `lean.local_mathlib_path` | `../mathlib4` | Path to local clone (relative to repo root) |
| `lean.mathlib_git_url` | `https://github.com/leanprover-community/mathlib4` | Upstream URL to redirect |

The `lean_build` tool warns if the local clone is >7 days stale and
offers `update_local_mathlib: true` to fetch the latest commits.
Shell scripts use `scripts/lib/lean-env.sh` for the same logic.

### Remote MCP server

A Docker-based remote deployment is available in `deploy/`:

```bash
cd deploy && ./setup-remote.sh
```

All settings are driven by `lean-mcp.config.json` at the repo root.

Architecture: `Client → Caddy (TLS) → auth-gateway (dual OAuth) → lean-lsp-mcp (HTTP)`

- Docker image built by CI on every push to main (`build-lean-mcp.yml`)
- All Lean deps and oleans baked into the image for fast startup (~10-20s)
- Auth: Dual OAuth — Google (viewers) + GitHub (collaborators/owner)
- Roles: viewer (read + feedback), collaborator (edit + branches), owner (commit to main)
- Whitelists: `deploy/google-viewers.txt` + `deploy/github-collaborators.txt` (manually managed)
- Auto-update: `self-update-folio.sh` polls git + GHCR every minute via cron
- Programmatic access: bearer token via `FOLIO_API_TOKEN`
- Hosting: Hetzner CX22 (~€4.50/mo), provisioned via `provision-hetzner.sh`

To switch a client to remote mode, update `.mcp.json`:

```json
{"mcpServers":{"lean-lsp":{"url":"https://folio.litlfred.org/mcp"}}}
```

To extract the deploy infrastructure for another repo, copy `deploy/`,
`lean-mcp.config.json`, `.github/docker/Dockerfile.lean-mcp`, and
`.github/workflows/build-lean-mcp.yml`, then edit `lean-mcp.config.json`.

### Session-start hook

A `SessionStart` hook in `.claude/settings.json` runs `scripts/session-status.sh`
at the beginning of every session. It sources `scripts/lib/lean-env.sh` for
shared Lean environment detection. If Lean is not available and the user's
request requires Lean, the editor skill will suggest the `lean_setup` MCP
tool rather than silently failing.

## Project structure

| Path | Purpose |
|------|---------|
| `content/` | **Authoritative content objects** (`.ts` + `.md` + `.lean` triples) |
| `content/schema/` | Type system, Zod schemas, builder functions (re-exports from `folio-assistant/schemas/`) |
| `content/pipeline/` | Validation, rendering, build pipelines |
| `content/<paper>/` | Paper manifest + chapter directories |
| `content/<paper>/fluid-dynamics/` | Ch 7: Fluid dynamics of the brane (q-NS, NS obstruction) |
| `folio-assistant/` | **Platform package** — MCP server, auth, UI, blocks, viewer |
| `folio-assistant/src/` | Generic core (server, types, routes, tools, blocks registry) |
| `folio-assistant/adapters/paper/` | Paper content adapter (implements `ContentAdapter`) |
| `folio-assistant/schemas/` | Shared TypeScript types (proof-objects, glossary, etc.) |
| `folio-assistant/viewer/` | Paper viewer SPA + Pyodide cache Service Worker |
| `folio-assistant/ui/` | Assistant chat SPA |
| `folio-assistant/simulators/` | Interactive HTML simulators |
| `folio-assistant/feedback/` | User feedback (TypeScript files, committed to main) |
| `folio-assistant/computations/` | Computation scripts and witness data |
| `folio.config.json` | Adapter config (content type, adapter module, feedback dir) |
| `main.tex` | LaTeX preamble and document structure (rendering target) |
| `chapters/*.tex` | Generated LaTeX chapters (from content pipeline) |
| `references.bib` | BibTeX database (auto-generated from `content/schema/references.ts`) |
| `lakefile.toml`, `lean-toolchain` | **Root Lake workspace** — aggregates every paper package; `lake build` here builds all |
| `content/quantum-observable-universe/lean/` | `qou` Lake package (lib: `QOU`) |
| `content/unital-groebner-bases/lean/` | `ugb` Lake package (lib: `UGB`) |
| `content/fred2005-formal-groups/lean/` | `fred2005` Lake package (lib: `Fred2005`) |
| `folio-assistant/schemas/lean-packages.ts` | Registry mapping `lean.ref` URI prefixes → Lake packages |
| `blueprint/src/` | LeanBlueprint source (content.tex, preamble.tex, web.tex, print.tex) |
| `home_page/` | Jekyll landing page for GitHub Pages |
| `.github/workflows/` | CI/CD pipelines |
| `.github/scripts/` | Python orchestration (ontologist, extraction, stub generation) |
| `.claude/skills/local/` | Repo-specific review skills |
| `.claude/skills/<pkg>/` | Synced external skill packages |
| `uploads/` | Document intake pipeline (raw PDFs, scans, WHO guidelines → content objects) |
| `todos/` | Work-tracking TodoItems, gitignored (external to paper content) |
| `docs/` | Planning documents, migration plans, dependency graphs |
| `scripts/` | Setup and health-check scripts (Lean MCP, etc.) |
| `lean-mcp.config.json` | MCP server config (domain, image, auth, ports) |
| `deploy/` | Remote MCP server deployment (Docker Compose, auth, auto-update) |
| `skills-config.json` | Skill package subscriptions |

## Build output (gh-pages)

Three workflows deploy to the `gh-pages` branch. GitHub Pages must be
configured to **deploy from the `gh-pages` branch** (not "GitHub Actions").

### Workflow → artifact mapping

| Workflow | Artifacts deployed to gh-pages |
|----------|-------------------------------|
| `blueprint.yml` | `blueprint/` (interactive dependency graph), `blueprint.pdf`, `docs/` (doc-gen4 API), `axiom-report.txt`, manifests |
| `lean_ci.yml` | `lean/content/<paper>/lean/` (per-paper source browsers for QOU/UGB/Fred2005), `lean/.../docs/`, `axiom-report.txt`, `dependency-graph.svg`, manifests |
| `publish.yml` | `papers/<dir>/` (per-paper viewers), `index.html` (folio), `schema-docs/` (TypeDoc), `drafts/` (feature branches) |

### Expected gh-pages contents

| Path | Source | Description |
|------|--------|-------------|
| `index.html` | publish.yml | Folio landing page (links to all papers) |
| `papers/<dir>/index.html` | publish.yml | Per-paper viewer with paper/visualizer toggle |
| `papers/<dir>/paper.html` | publish.yml | Enhanced HTML paper |
| `papers/<dir>/<dir>.pdf` | publish.yml | Compiled paper PDF |
| `papers/<dir>/<dir>.md` | publish.yml | Pandoc Markdown |
| `quantum-observable-universe.pdf` | publish.yml | Backward-compat copy of first paper PDF |
| `blueprint/` | blueprint.yml | Interactive dependency graph (plasTeX HTML) |
| `blueprint.pdf` | blueprint.yml | Print blueprint |
| `docs/` | blueprint.yml | doc-gen4 API documentation with hover definitions |
| `content/quantum-observable-universe/lean/` | lean_ci.yml | Raw Lean source files |
| `content/quantum-observable-universe/lean/docs/` | lean_ci.yml | doc-gen4 or fallback source browser |
| `axiom-report.txt` | blueprint.yml / lean_ci.yml | sorry audit, axiom dependencies |
| `dependency-graph.svg` | lean_ci.yml / publish.yml | Visual proof dependency graph |
| `schema-docs/` | publish.yml | TypeDoc content-object type reference |
| `proof-objects.json` | all | Formalization status manifest |
| `glossary.json` | all | Semantic glossary |
| `mapping.json` | all | Narrative-to-Lean identifier map |
| `drafts/<branch>/` | publish.yml | Feature branch preview builds |

### Error resilience

All workflows use `continue-on-error: true` at critical points so partial
output is still deployed even when the Lean build fails:

- **Lean build fails** → proof status updates, axiom report generates, source
  browser deploys.  `proof-objects.json` records which declarations errored.
- **doc-gen4 fails** → `lean_ci.yml` generates a fallback HTML source browser.
- **Blueprint compilation fails** → other artifacts (manifests, axiom report)
  still deploy.
- **latexdiff fails** → main PDF still publishes; diff PDF is skipped.
