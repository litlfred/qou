# Skill gaps for work-plan reorganisation and programme tracking (folio-assistant)

Read-only analysis, 2026-10-04. Paths are relative to `/home/user/folio-assistant/cat-harness/` unless they start with `qou/`.

## What already exists (more than expected)

- **LSI over beans, with duplicate and epic-filing proposals**: `skills/kg/graph-management/lsi-indexing.md`, `scripts/lsi.ts`, `scripts/lsi-epics.ts`. These already do `nearDuplicates` (cosine ≥ 0.95) and `lsi:epics`. That second command proposes an epic for every open bean, unmerged branch and open PR, explicit evidence first (parent chain, bean id in commit messages) and latent evidence second. It prints a calibration line (59% agreement over 21 epics, 2026-09-29). It never writes a parent. **The "latent semantic index" the owner asked for exists for beans only.**
- **Hierarchy rules**: `skills/sdlc/sdlc-core/todo-manager.md` §"WHICH parent", §"A GOAL is a milestone bean", §"conflicts with every session is a Bean" (file by SUBJECT). `skills/process/workflow/release-epic-planning.md` (epic → feature → task). Guards: `scripts/check-bean-parents.ts` (every open bean is under an epic or milestone) and `scripts/milestone-status.ts` (rollup of the closure under each milestone).
- **Store health**: the `bean-store` check in `test/health/checks.ts` (duplicate titles, unhonoured claims, the open backlog). Also `scripts/check-quiet-claim-liveness.ts`, `scripts/check-bean-archive.ts`, `scripts/check-ready-to-close.ts`, and `skills/sdlc/sdlc-core/bean-coordination.md` (never delete, scrap with a pointer, re-derive from the remote).
- **GitHub / branch state**: `skills/sdlc/sdlc-core/github-state-inspection.md`, `skills/process/workflow/branch-freshness.md`, `skills/sdlc/sdlc-core/merge-queue.md` with `scripts/merge-steward.ts`, `skills/sdlc/sdlc-core/stalled-agent-triage.md`, `skills/sdlc/sdlc-core/goal-review.md` (six axes including branches), `scripts/survey.ts`, `skills/sdlc/sdlc-core/coordinate.md` (cherry-pickable work between live PRs), `skills/sdlc/sdlc-core/related-work-coordination.md`.
- **Visualisers**: `scripts/state-visualizer.ts` (a dashboard per state graph), `skills/ui/ui-core/harness-tiles.md`, `board-diagram-interchange.md`, `board-windows.md`, `skills/authoring/authoring-core/review-heatmap.md` (section-by-metric, review-scoped).
- **Formal side** (in `folio-assistant-sci/skills/content/folio-paper-adapter/`): `lean-formal-graph.md`, `lean-formal-edges.md`, `semantic-review-scoping.md`, `critical-path-analysis.md`, `proof-status-tracking.md` (`proof-objects.json`). `conjecture` is a block kind (`schemas/types.ts` `ConjectureBlock`, which has only an optional `lean` field).

## Root cause behind gap (f), found in passing

`todo-manager.md` Core Directive 1 still says *"create a parent bean (`--type milestone` or `--epic`) that represents the session"*. Its §"Status Display Format" sample shows `[epic-123] Session: <branch-name>`. A later section of the same skill contradicts this ("file by subject"). Measured in `qou/beans/defs`: **292 of the 353 `type: epic` beans have "session" in the title.** This defect sits in the skill text itself. Fix it in `todo-manager` before adding anything new.

## Gaps

### (a) Work-plan restructuring: taxonomy, reparenting, dry-run apply plan. Priority HIGH, generic
- **Instance: `cat-harness`, kg dir `cat-harness/skills/` → `sdlc/sdlc-core/work-plan-restructure.md`.** Processes go in `cat-harness/processes/`.
- **Partial:** `lsi:epics` proposes parents. `release-epic-planning` defines a release-shaped hierarchy. `check-bean-parents` guards placement.
- **Missing:**
  - a declared **taxonomy** (epic / story / task, with what each level means and its cardinality rules);
  - a **plan file** (reviewable JSON listing each move, retype, scrap-as-duplicate and new epic, with its evidence and confidence);
  - a **dry-run → owner review → batched apply** that is reversible (an inverse plan) and respects claims.
  
  `lsi-indexing` currently says "never apply in bulk". A reviewed plan is the sanctioned way between bulk application and one bean at a time. Also missing: a "story" type, and a rule for when a feature counts as a story.
- **Proposed skill: `work-plan-restructure`.** It defines the taxonomy as data, and the bean graph schema checks it. It produces `restructure-plan.json` from `lsi:epics`, the duplicate detector and the session classifier (f). It renders the plan as a reviewable diff (counts per epic before and after, plus orphans) and applies only the rows the owner approved, through a BPMN process with a confirmation gate (`deletion-requires-confirmation` applies to retype and scrap). It writes an inverse plan so the change can be rolled back.

### (b) Git archaeology: branches and PRs against main. Priority HIGH, generic
- **Instance: `cat-harness` → `skills/sdlc/sdlc-core/branch-archaeology.md`.** The script goes next to `merge-steward.ts`.
- **Partial:** `branch-freshness` covers your own branch. `stalled-agent-triage` and `goal-review` cover a window of activity. `coordinate` covers live sibling PRs. `merge-steward` covers queue order. `lsi:epics` reads branch commits.
- **Missing:** a full sweep of the remote (qou has 6,480 remote branches) that classifies each branch as one of:
  - merged;
  - landed by squash or cherry-pick (`git cherry` / `patch-id` equivalence, or a tree diff that is empty after rebase);
  - superseded (its files have since been rewritten on main);
  - orphaned with unique work (unique hunks, size, last author or session);
  - backing an open PR.
  
  The output is a **safe-delete candidate report** with sizes and ages, as `deletion-requires-confirmation` requires. The skill never deletes. Also missing: a "salvage" list of unique hunks worth a bean.
- **Proposed skill: `branch-archaeology`.** It runs with a cache keyed by branch tip sha, because 6k branches are too many to recompute each time, and writes a `branch-census` sidecar to `qa-reports`. Each branch gets a classification plus evidence (patch-ids matched, PR number, bean ids in its commits). It feeds the `staging-preview-orphans` and `repository-size` health checks, and it hands unique work to (a) as a candidate bean or parent.

### (c) Latent semantic index across graphs (beans + blocks + Lean declarations). Priority MEDIUM-HIGH, generic
- **Instance: `cat-harness` → `skills/kg/graph-management/`** for the LSI extension and `duplicate-work-detection`. The `folio`-block indexer belongs in **`folio-assistant-core`** (`core-skills`, `skills/`). The `lean-decl` indexer belongs in **`folio-assistant-sci`**.
- **Partial:** `lsi-indexing` declares `graph-kinds: library, skills, beans, docs`. **There is no content-block or Lean graph kind, and no cross-graph query.** Duplicate detection runs within one graph only.
- **Missing:**
  - indexing `folio` blocks (statement text, labels) and Lean declarations (name, docstring, statement pretty-print);
  - a **joint space**, or per-graph indexes with folding-in, so that "bean X is about block Y / declaration Z" can be scored;
  - duplicate clusters, not just pairs, with a cluster ID that is stable across runs;
  - an optional embedding back-end behind the same proposal-only contract.
- **Proposed:** extend `lsi-indexing` (don't fork it) with `folio` and `lean-decl` graph kinds and a `lsi:cross` query. Add a sibling skill **`duplicate-work-detection`** for the operational loop: clusters → keep one canonical bean → scrap the others with pointers. It should also run at **create time**, extending §"Check before you create" from title matching to latent matching. That last step is the one that stops parallel agents duplicating work.

### (d) Traceability: bean ↔ block ↔ Lean declaration ↔ PR. Priority HIGH, generic
- **Split.** The bean ↔ PR ↔ file half goes in **`cat-harness`** (`skills/sdlc/sdlc-core/work-traceability.md`). The block-label target field goes in **`folio-assistant-core`** (`schemas/`, `skills/`). The block ↔ Lean-declaration join goes in **`folio-assistant-sci`**, as an extension of `lean-formal-graph`.
- **Partial:** `lean.ref` links a block to its declarations. `lean-formal-graph` gives formal edges. Bean ids sit in commit messages, which `lsi-epics` parses. `schemas/fsh-guts.ts` and `bean-note.ts` have a `bean` field. **There is no `bean → block label` or `block → bean` relation anywhere in `schemas/types.ts`.**
- **Missing:**
  - a declared, typed link (front-matter `targets: [block-label | lean-decl]` on a bean, validated against the content graph);
  - a derived trace table joining bean → PRs/commits → touched block files → `lean.ref` → declarations;
  - "explicit vs inferred" provenance, with inferred links coming from (b) and (c).
- **Proposed skill: `work-traceability`.** It covers the schema field, the `trace:build` derivation (a sidecar, not authored), and a coverage report. The report lists blocks with no bean, beans with no target, and conjectures/sorries with no owner. It is the substrate for (e) and (g).

### (e) Programme / epic progress visualisation. Priority MEDIUM, generic
- **Instance: `cat-harness`** for the epic burn-down (`skills/ui/ui-core/`, `state-visualizer`). The math heat-map columns and the conjecture lane go in **`folio-assistant-sci`**.
- **Partial:** `milestone-status.ts` rolls up milestones. `state-visualizer` draws a dashboard per state graph. `review-heatmap` is section × metric, but scoped to review. Boards are diagrams of a folio.
- **Missing:**
  - an epic rollup over time (burn-down/up from bean status history, reconstructed via `git log` on `beans/defs`);
  - a **math-progress heat map**: chapter/section × {proved in Lean, sorry, axiom, conjecture open, has active bean, review verdict};
  - a board that draws epics/stories as notes positioned over the content graph, following `board-diagram-interchange`'s arrow rule (folio → board, never back).
- **Proposed skill: `programme-progress`.** It defines the metrics with "must not be read as" columns, in `review-heatmap` style, and states that "no data" is not zero. It adds columns to the heat map from (d)'s trace table and has `state-visualizer` render an epic burn-down for the `beans` graph. Dependencies: (d), and (g) for the conjecture lane.

### (f) Session logs vs work items. Priority HIGH, generic (and cheap)
- **Instance: `cat-harness`.** Fix `skills/sdlc/sdlc-core/todo-manager.md`, and add a `check:` gate beside `check-bean-parents.ts`.
- **Partial:** `activity-log.md` (`fsh-guts/logs/`, off the graph) and `session-intent.md` already provide the right homes for the log. `todo-manager` contradicts itself (see root cause above).
- **Missing:**
  - correct Directive 1 and the sample, so a session record is a `note`/log entry or a `session` type, never `epic`;
  - a **classifier** that flags beans that are session logs (title patterns, a body made of dated narrative, no `## Done when`, children spanning unrelated subjects);
  - a migration rule: retype, re-home the children by subject through (a), and keep the narrative as a handover note;
  - a gate rejecting a new `type: epic` whose title matches `^Session`.
- **Proposed:** a fix to `todo-manager` plus a small skill or gate, **`session-bean-separation`**. It feeds (a)'s plan.

### (g) Conjecture register as a first-class graph kind. Priority MEDIUM, mostly generic (math and paper profile)
- **Instance: `folio-assistant-sci`** (paper adapter; schema plus a `conjectures` graph kind). The graph-kind registry entry itself lives in **`cat-harness`** `schemas/`.
- **Partial:** the `conjecture` block kind (statement plus an optional Lean stub). `proof-status-tracking` (`proof-objects.json`) and `critical-path-analysis` are qou- or paper-adapter scoped.
- **Missing:** a register node per open problem, holding:
  - status (open / partial / reduced-to / refuted / proved), with the lifecycle as a DMN;
  - the source block, the Lean stub, and the `sorry`/axiom declarations it depends on;
  - the critical-path theorems that **assume** it, from `lean-formal-graph` reverse edges;
  - attempts (beans and PRs, from (d)) and evidence (witness scripts, numerics).
  
  The owner's "one umbrella epic for open conjectures" should be **derived from this register**, with one story per conjecture, rather than maintained by hand.
- **Proposed skill: `conjecture-register`.** It declares a `conjectures` graph kind (holds: `state`) under the paper adapter, a schema in `schemas/`, a `conjecture:sync` that seeds entries from `kind: conjecture` blocks and from Lean `sorry`/axioms on critical paths, and a status board lane for (e). It is generic to any paper folio. Only the qou instance data is qou-specific.

### Other gaps noticed
- **`work-plan-health` as a graph audit (MEDIUM, generic).** It would combine parent cycles, epics with zero or one child, depth > 3, a closed epic with open children, an open epic whose children are all closed, and stale `in-progress` items. Today this is spread across `check-bean-parents`, `bean-store` and `quiet-claim-liveness`. Fold it into `kg:audit` criteria rather than a new script.

## Suggested order
1. Fix (f) in `todo-manager`.
2. (b) `branch-archaeology` and (a) `work-plan-restructure` (the plan file and the apply gate).
3. (c) the cross-graph extension of LSI, plus the create-time duplicate check.
4. (d) `work-traceability`.
5. (g) `conjecture-register`.
6. (e) `programme-progress`.

Steps 4–6 depend on each other in that order.

## Instance placement note
The `needs` chain is `bootstrap` → `cat-harness` → `folio-assistant-core` → `folio-assistant-sci`. **Finding:** `folio-assistant-sci/folio-assistant-sci.json` declares **no `skills` graph-kind directory**, although `folio-assistant-sci/skills/` holds the whole paper adapter (about 70 skills). They are reached only through `cat-harness/scripts/known-skills.ts` / `partition/instance-rules.ts`. That is the `dh4f` defect inverted: a directory that is present but undeclared. Declare it before anything new lands in sci. (`folio-assistant-core` declares `core-skills: skills/`; `cat-harness` declares `skills: skills/`. `bootstrap/` is empty in this checkout.)

## qou local skills: keep vs upstream vs already-superseded
Basis: the current checkout of `/home/user/folio-assistant` (HEAD 2026-10-04) against `qou/.claude/skills/local/` (96 `.md` files, 20 `.ts` files). Each file was matched by basename. The divergence numbers are diff lines and qou-term counts (qou|substrate|hecke|braid|kashaev) in qou against f-a. **ch** = `cat-harness/skills/`. **sci** = `folio-assistant-sci/skills/content/folio-paper-adapter/`.

**Obsolete: five pointer stubs to a path that no longer exists.** These are `deployment-auth`, `editor`, `readability-editing`, `symbiotic-interaction` and `todo-review`. Each says "migrated to `folio-assistant/src/skills/…`", but `src/skills/` was removed in #760. Current homes:
- `ch/sdlc/sdlc-core/deployment-auth.md`
- `ch/authoring/authoring-core/{editor,readability-editing,todo-review}.md`
- `ch/conduct/conduct-core/symbiotic-interaction.md`

Repoint them or remove them, with confirmation.

**qou-specific: keep in qou.**
- `lean-q-substitution` and `lean-substrate-numerics` (the substrate `q`; there is no f-a counterpart).

**Generic, should go upstream (f-a lacks it).**
- `sandbox-egress` → **cat-harness** (`ch/conduct/conduct-core/` or the environment docs). The `egress` hits that exist are only incidental.
- `paper-relevance-triage` → **folio-assistant-core** (`skills/library/`), next to `document-intake` / `literature-search` in ch `library-core`.
- `.agents/rules/lean-infra-rule.md` (build the infrastructure, never `sorry`→`axiom`, bean only real conjectures) → **folio-assistant-sci**, as a rule in `lean-build-fix`/`formalizer`. Fragments already appear in `lean-proof-vacuity-audit` and `lean-proof-review`.
- `language-trap-agent-audit` exists in f-a only under the repo-root `.claude/skills/local/`, which is in no instance's kg. Move it into **cat-harness** `ch/authoring/authoring-core/`.

**Already in f-a, qou copy is a STALE FORK (f-a ahead or near-identical) → replace with a pointer.**
- **Work-plan / SDLC (cat-harness):**
  - `bean-coordination` (qou 41 lines vs 820) and `todo-manager` (150 vs 592). The qou copies lack "file by subject", the create-guard and the claim tooling.
  - `continual-progress` (81 vs 291), `session-intent` (207 vs 268), `idle-backlog` (vs `ch/sdlc/sdlc-core/idle-backlog.md`, 21-line diff), `pending-show`, `pickup`, `dispatch-agent`, `watch`, `diff`, `delivery-summary`, `test-engineer`.
- **Authoring / UI / library (cat-harness):** `block-density`, `md-authoring`, `exposition-swarm-drain`, `chapter-complexity-review`, `html-rendering-qc`, `one-voice-audit`, `one-voice-integration-watcher`, `content-graph`, `document-intake` (f-a larger), `glossary-build`, `bib-human-review`, `bib-photo-ingestion-watcher`.
- **Paper (sci):** `content-block-review`, `content-validation`, `chapter-analysis`, `category-theory`, `paper-importer`, `latex-validation`, `latex-build-cache`, `lean-build-fix`, `lean-proof-review`, `lean-substantive-pass`, `lean-mathlibext-curator`, `lean-completeness-audit`, `lean-generation`, `proof-*` (`conciseness`, `editor`, `exposition-review`, `gap-audit`, `integration-watcher`, `narrative-lean-equivalence`, `simplifier`, `status-tracking`, `triage`), `proposition-consolidation-audit`, `q-usage-watcher`, `remark-audit`, `rendering-auditor`, `simulator`, `definition-clarity-audit`.
- **The `.ts` siblings:** all 19 have f-a twins (sci, or ch for content-graph, docs-generation, ontologist, scientific-accuracy, test-engineer). `package-manifest.ts` has no twin and is qou plumbing, so keep or retire it.

**Already in f-a, but MATERIALLY DIVERGED: qou copy larger, carrying qou-specific residue.** Action: keep a thin qou **overlay**, meaning instance data/config plus qou examples on top of the f-a skill. Reconcile any generic deltas upstream first. Strongly qou-laden:
- `lean-environment-setup` (1,322 vs 180; 90 qou terms)
- `compute-author` (766 vs 266; 59)
- `formalizer` (936 vs 230; 39)
- `verify-local-substrate` (46)
- `ffi-roundtrip-audit` (28)
- `groebner-basis` (25)
- `scientific-accuracy` (26)
- `production-vs-exploratory-discipline` (652 vs 263; 22)
- `one-voice-style-guide` (546 vs 228)
- `compute-audit`, `compute-integration-watcher`, `canonical-watcher`, `lean-proof-vacuity-audit`, `lean-witness-audit`, `witnessed-values`, `critical-path-analysis` (263 vs 156; its audited paths are qou data), `bib-qa`, `ontologist`, `rendering-fixes`, `devils-advocate-watcher`, `detangler-integration-watcher`

**Diverged with few qou terms: likely GENERIC deltas, upstream to cat-harness before deleting the qou copy.** Diff each; I did not read every hunk.
- `coordinate` (760 vs 524, 0 qou terms)
- `integration-watcher` (1,677 vs 240 plus the `ch/sdlc/sdlc-core/integration-watcher/` subdir)
- `integration-watch` (0 qou terms, 245-line diff)
- `integration-backlog`, `integration-audit`, `prepare-merge-auto` (338 vs 180), `markdown-render-check` (211 vs 107), `docs-generation`
