# TARGET — what folio-assistant requires of each node kind a folio must be expressed as

**Source.** `origin/main` @ `0b7b9e44e` (2026-10-04), exported read-only to `scratchpad/famain/`.
Submodules were read at their pinned SHAs: `bootstrap` @ `5761204`, `bootstrap-tools` @ `7ac5150`.

**Provenance.**
- [M] = I read it in code or counted it.
- [D] = it comes from a doc or skill.
- Citations are `file:line` at that commit.
- Examples come from `folio-assistant-sci` (sci) and from `litlfred/folio-test`
  `origin/claude/ojcx-edit-handbook`.

## 0. Instance contract

**Declaration: `<slug>.json`.** The filename stem must equal `name`. Schema:
`CatHarnessDeclarationSchema`, `cat-harness/schemas/cat-harness.ts:2789`.
- `directories[]` (`:2885`).
- `needs: string[]` (`:2950`). It holds names only.
- `contentAdapters[]` (`:2961`) and `nodeSchemas` (`:2881`).

**Directory entry** (`:1492`, which extends `:945`):
- Required: `id`, `path`, `graphKinds[]`.
- Optional: `coverage{docs,skill,process,visualiser}`, `storage{branch,keyedBy}`, `source`,
  `instanceRoot`, `tile`.
- `dependents` was **retired 2026-09-30** (`:890`). Inheritance is automatic, and `perInstance`
  on the kind decides whether a dependent gets its own copy.
- Overrides match on `id`.
- `DEFAULT_DIRECTORIES` (`:1854`) is always seeded, but only for directories that exist:
  `tools/ schemas/ skills/ scenarios/ processes/ beans/ todos/ uploads/ library/ skills/voices/`.

**Config: `<slug>.config.json`.** Schema: `HarnessConfigSchema`, `harness-config.ts:327`.
- Fields: `contentType`, `adapter`, `adapterModule`, `contributes`, `dependencies`, `site`.
- The schema is not strict. Extra keys such as `viewer` and `simulators` are tolerated but not
  validated.

**Dependency:** `{name, path?|git?, ref?, version?, provides?}` (`harness-config.ts:198`).
- `needs` and `dependencies` are reconciled by `dependenciesFromNeeds` (`:813`).
- Gate: `check:needs-dependencies`.

**Stack [M].**
- bootstrap needs nothing.
- bootstrap-tools needs bootstrap.
- cat-harness needs bootstrap and bootstrap-tools.
- cat-harness-tools needs cat-harness.
- core needs cat-harness and cat-harness-tools.
- sci needs core.
- Sci declares the `paper` adapter (`extends: document`, module `adapters/paper/index.ts`).

**What `init-folio` writes for a paper today [M]** (`cat-harness/scripts/init-folio.ts:1112–1300`):
- `<slug>.json` declaring only `{id:"folio", path:"folio/", graphKinds:["folio"]}` (`:269`).
- `<slug>.config.json` with `dependencies.folioAssistant:[{name:"folio-assistant-sci", path}]`.
  It writes no git/ref and no `needs` (`:213`, `:306`).
- `.mcp.json`.
- `.claude/settings.json`, whose SessionStart hook runs
  `<platform>/cat-harness/scripts/session-start-coord-sweep.sh`.
- `.beans.yml` (`path: beans`) and `todos/todos.json`.
- `AGENTS.md`, plus `CLAUDE.md`/`GEMINI.md` stubs.
- The `folio/schema/{builders,types}.ts` shim.
- `folio/<slug>/<slug>.ts` and `introduction/{introduction.ts,overview.ts,overview.md}`.
- `uploads/README.md` and `library/README.md`.
- `staging.yml`. For a paper its `build_command` is unset and erroring (`:646–656`).
- Dispatch-only Lean workflows and `.github/scripts/folio_lean/*.py`. The default Lake package is
  `folio/<paper>/lean`.
- The QA workflows.

## 1. Content nodes: kind `folio` (renderable, holds `content`, perInstance)

**Registration.** `cat-harness/schemas/folio-graph-kind.ts:40`, with `layer:"core"`. It is
registered on import.

**Manifests.**
- Document: `folio/<doc>/<doc>.ts` → `paper({title, authors, date, chapters:[chapterRef({dir})]})`.
- Chapter: `folio/<doc>/<ch>/<ch>.ts` → `chapter({title, label, sections:[section({title, label, blocks:[<root>…]})]})`.
- A block renders only if some section lists it.
- Types: `Paper` `types.ts:1210`, `Chapter` `:1175`, `Section` `:1122`.

**Block = triple** (`agent-onboarding.md:102`) [D]:
- `<root>.ts` is the manifest. It imports `../../schema/builders` and never the platform.
- `<root>.md` holds the narrative.
- `<root>.lean` is there when the kind needs it.
- Block QA lives under `test/results/block-qa/<mirrored path>` (`validate.ts:113–140`).
- `BlockBase` (`types.ts:391`): `label` (required), plus `uses[]`, `cites[]`, `defines[]`,
  `foreshadows[]`, `simulator`, `computation`, `authorNotes`.

**Kinds.**
- `BLOCK_KINDS` (`block-kinds.ts:42`, 16 kinds) and `MATH_BLOCK_KINDS` (`:232`).
- `DOCUMENT_BLOCK_KINDS` (`:256`) is derived.
- Profiles are `document|paper`.
- **There is no `computation` kind.** It is a field on blocks.

**Lean.**
- `LeanRef{ref, sorryFree?, validation?, leanHash?, witnessed?}` (`types.ts:91`).
- `ref` is `<package>:<Decl.Path>` (`LEAN_REF_PATTERN`, `lean-packages.ts:133`).
- `definition` requires `lean` (`types.ts:691`). Other provable kinds take it optionally.
- `lean-file-exists` (`constraints.ts:738`) passes on a sibling `.lean` OR on a Lake-tree file
  resolved through a package `{name, paperDir, lakeRoot, lib}` (`lean-packages.ts:44`).
- `md-exists` (`constraints.ts:726`) exempts proof, algorithm, equation, diagram, table and
  figure [M].

**Computation** (`types.ts:259`): `{engine, script, witness?, status, requires?}`.
- The witness is a `.witness.json` that follows `ComputationWitness` (`:205`). That is a
  TypeScript interface; **no Zod schema exists** [M].

**Simulator** (`types.ts:895`): `{html, defaultView, views?}`. Constraints:
`simulator-html-exists` and `simulator-ref-resolve`.

**Library: kind `library`, holds `derived`.**
- Layout: `library/<entry>/{manifest.jsonld, licence.json, blocks/, structure.json}`.
- A reference dataset adds `values.json` (`{quantity, value, uncertainty, unit, exact}` per slug)
  and `tabular.jsonld`.
- Values are addressed as `{{ <instance>.library.<entry>.<slug> }}`.
- Example: `folio-assistant-sci/library/codata-2022/`.

**Witnesses are NOT a graph kind [M].**
- Computation witnesses live wherever `computation.witness` points.
- `qa-witness/v1` is a family inside `qa` (`graph-kind-registry.ts:1055–1074`).
- Lean witnesses and `proof-objects.json` come from the template's `update_proof_status.py`.

**Validation.**
- `content/pipeline/validate.ts` (CLI `:926`; MCP `content_validate`): Zod builders plus
  `constraints.ts`.
- `profile-check.ts`.
- `qa-sweep.ts` axes.
- The `uses-*` and `lean-ref-owns-decl` criteria.
- `check:orphan-verdicts`.
- The `folio` kind declares no `nodeSchemas`, so `check:kind-validators` does not judge it.

**Render.**
- `folio-assistant-core/scripts/build-document-site.ts` (remark-html, an anchor per label).
- Paper PDF: `publish.yml` (LaTeX).
- `folio:viz` gives the graph view.
- **No just-the-docs emitter exists for `folio` content.** Just-the-docs renders the `docs` kind
  (`compose-docs.ts`).

## 2. Tool nodes: kind `tools`

**Schema:** `ToolDefinitionSchema` (`cat-harness/schemas/tool.ts:414`), written with `defineTool`.
- Required:
  - `id`, `title`, `description`.
  - `install{cli|container|service|none}`.
  - `invoke` (`:214`): at least one of shell, container, inProcess or manual (`mcp` is also allowed).
  - `io{inputs,outputs}`, using `tool-types.ts` IRIs.
  - `satisfies[]`: at least one skill.
- Optional: `maintains[]`, `renders[]`, `subprocesses[]`.

**Placement.**
- A declared `tools` directory whose `index.ts` exports `tools(baseUrl)`.
- Example: `folio-assistant-core/tools/index.ts` (5 Tools [M], for example `dublin-core-render`,
  `invoke.shell: bun run folio-assistant-core/scripts/dc-render.ts`).
- The script itself sits in a `graphKinds:["code"]` directory.

**MCP.**
- A Tool reaches MCP through `invoke.inProcess` or `invoke.mcp`.
- Sci's `contributions.ts:88` registers MCP tools through `contributes`. Those are not Tool nodes.

**Discovery and gates.**
- `cat-harness/tools/discover.ts:114` scans declared `tools` directories, but only across the
  platform checkout (`:52,123`).
- `check:tools` checks that `satisfies` resolves and that modules load.
- `check:tools-closure`.
- A gate's docblock carries `@covers <kinds>`, read by `audit:coverage`
  (`audit-coverage.md:48–53`).

## 3. Process nodes: kind `processes` (alias `workflows`)

**Layout.** BPMN/DMN under `processes/<concern>/`. Example:
`folio-assistant-sci/processes/content/authoring-a-paper.bpmn` and `decisions/lean-build-gate.dmn`.

**What an activity carries.**
- `<bootstrap.processes:skill ref>`, or `<cat-harness.processes:no-skill reason>`.
- Optionally `<cat-harness.processes:bean op>`.
- Lanes carry `<bootstrap.processes:role ref>`.
- The process carries `<cat-harness.processes:policy enforcement>`.
- Gateways carry `:decision ref` → DMN.
- Census [M]: ≥696 skill refs, 140 bean marks, 12 DMN files.

**Execution.**
- `workflow_*` resolve a diagram by stem across dependencies plus the root; the root shadows
  (`src/tools/workflow.ts:83–107`).
- Discovery: `known-skills.ts:818`.
- State: `beans/workflows/` (`store.ts:40`), as `folio-workflow-instance/v1`.

**Gates:** `check:workflow-policy`, `check:process-bindings`, `check:workflow-coverage`,
`check:raci`, `kg:audit`, `render:bpmn:check`.

**A folio's own processes** go in its `processes/`, which the defaults reach.

## 4. Skill nodes: kind `skills` (`kg` is an alias of `cat-harness`)

**Layout.**
- `skills/<group>/<pkg>/<name>.md` plus `package-manifest.json`, whose `skills[]` you
  hand-maintain.
- An optional `<name>.ts` holds a `SkillDefinition` (`skill-package.ts:301`).
- Subgraphs are declared in `skills/skills.json` (`subgraph:true`). Example: sci's `voices`,
  `lean` and `data`.

**Front matter.**
- Conventionally `name` and `description`, plus `allowed-tools`, `user_invocable` and `inherits`.
- **There is no Zod schema** [M].
- `check:retired-front-matter` bans `roles:`.

**Registration.** `bun run skill:register`. `skill:register:check` is the gate. The manifest entry
is the author's to add (`skill-registration.md:34–69`).

**Overlay.** `resolveSkillDirs` (`harness-config.ts:1570`) orders dependencies, then sibling
instances, then the root LAST. **The root wins a name collision.**

**How a qou-local skill should look.**
- *Shadow* (same name) replaces the upstream skill wholesale and loses upstream edits.
- *Thin specialisation* is a new name with `inherits: <pkg>/<skill>`, as `canonical-watcher.md:4`
  does. **No code reads `inherits` for skills** [M]. Prefer thin specialisation, plus a role
  extension (§5).

## 5. Roles / actors / permissions

**Schemas.**
- `scenarios/roles.json` → `RoleGraphSchema{name, roles[], actors?, extensions?}`
  (`role-graph.ts:497`).
- `RoleDef` requires `id`, `title`, `description` and `actorKinds` (`:423`).
- `RoleExtension{role, skills[]}` (`:386`).
- Actors: `scenarios/actors/*.json` (`skill-package.ts:173`).
- Permissions: `skills/permissions/permissions.json` and ODRL `policies/`.

**A downstream instance EXTENDS roles; it does not declare them.** Sci has `roles: []` and 9
`extensions` [M]. A folio should do the same, adding a role only for a genuinely new lane. Checks:
`kg:audit` and `check:actor-reach`.

## 6. Other kinds (registered set, measured by import)

**Work tracking.**
- `beans`: `bean-defs`, `bean-notes`, `workflow-state`, `merge-queue`, `session-survey`. Holds
  state, under `beans/beans.json`.
- `todos`: reader/reviewer feedback.

**QA and health.**
- `qa`: state. Stored on branch `cat/cat-harness/qa-reports`, keyed by commit.
- `attestations`: judgements that cannot be regenerated, kept on main.
- `health`: only when the folio runs `bun run health`.

**Context** (read, never written by a process).
- `interaction`: session-start context.
- `memory` and `waiver`.
- `methodology`: cite sci's methodologies; do not copy them.

**Content and ingestion.**
- `glossary`: the term ledger.
- `uploads`: the raw-intake queue.
- `library`: holds `derived`.
- `docs`: **renderable**. Use it for the folio's own docs pages.
- `code`: `scripts/` and `computations/`.

**`fsh-guts`.** "Delete" means relocate here.

## Docs ↔ code disagreements

1. `AGENTS.md:33` says the "`kg` entry maps to `skills/`". In code, `kg` is an alias of
   `cat-harness` (`graph-kind-registry.ts:2556`).
2. `AGENTS.md:107–109` says `init-folio` writes `content/` and a `content/schema/` shim. It
   actually writes `folio/` and `folio/schema/` (`init-folio.ts:1267`).
3. `agent-onboarding.md:112` says formalisation status is "never stored in the manifest", yet
   `LeanRef` carries `sorryFree`, `validation`, `leanHash` and `witnessed` (`types.ts:91`).
4. `no-orphan-lean` is a stated rule (`content-validation.md:47`) with **no constraint**. It
   appears only in a comment (`validate.ts:122`).
5. `lean-packages.ts` says the `lean.ref` grammar is "core", while `formal-ref.ts` records the
   owner ruling "sci". **`configureLeanPackages` has 0 callers** [M], so the Lake-tree branch of
   `lean-file-exists` is dead unless a folio injects packages.
6. Path bases disagree: `Computation.script` is relative to the paper root, `witness` to the repo
   root (`folio-assistant/computations/`) (`types.ts:262–275`). No kind declares `computations/`.
7. Tool discovery:
   - The root `tools/index.ts` is described as merging every instance, but it imports only
     cat-harness.
   - `cat-harness/tools/index.ts` (~`:2011`) still says collection is "import-bound".
   - Discovery misses a downstream folio's `tools/`.
8. "`folio` is the one renderable kind" (`folio-graph-kind.ts:39`), yet `docs` is
   `renderable:true` (`graph-kind-registry.ts:774`).
9. `AGENTS.md:195` refers to an orphan `qa-reports` branch. The live branch is
   `cat/cat-harness/qa-reports`.
10. `AGENTS.md:708` names `agentic-harness` and says core "declares only folio/". Core declares 11
    directories [M].
11. `init-folio` writes `.beans.yml path: beans` with no `beans.json` (`:896`). The platform and
    qou use `beans/defs`.
12. The `init-folio` comment (~`:241`) and folio-test's `cold-chain.json` still use the retired
    `dependents`.
13. The just-the-docs ruling for qou has no platform support for papers: `staging.yml`
    `build_command` is unset (`init-folio.ts:646–656`).
14. qou-specific artefacts still live in the platform [M]:
    - `folio-assistant-sci/processes/content/atomic-mass-drift-check.bpmn`.
    - The workflows `atomic-mass-gen-check`, `hecke-engine-wasm`, `pyhecke*`, `snappea_wasm`,
      `witness-pipeline` and `witness-refresh`.
15. Measured against this yardstick, qou's own config [M]:
    - **`qou.config.json`'s `adapterModule` points to `folio-assistant/cat-harness/adapters/paper/index.ts`, which is absent on main.** The adapter now lives in sci.
    - It has no `dependencies`.
    - `qou.json` uses `dependents`.
    - A retired `folio.config.json` sits beside it.

## Proposed stories

**T1 — Re-point qou's instance contract.** Size S. Depends on: none.
- Work:
  - Set `adapterModule` to the sci adapter.
  - Declare `dependencies.folioAssistant` on folio-assistant-sci (with `git`/`ref` or `path`)
    and add `needs`.
  - Drop `dependents`.
  - Retire `folio.config.json`.
- Done when, run from qou:
  - `check:instance-config`, `check:needs-dependencies` and `check:instance-graph` are green.
  - `git diff --stat folio/ library/ computations/ '*.lean'` is empty.

**T2 — Inject Lean packages.** Size M. Depends on: T1.
- Work: either a `contributes` call to `configureLeanPackages`, or a declarative `leanPackages`
  config field. The second is platform work for sci.
- Done when:
  - `lean-file-exists` resolves through the Lake tree for a probe block with its sibling removed
    in a scratch copy.
  - The `.lean` bytes are unchanged.

**T3 — Witness kind and Zod `ComputationWitnessSchema`.** Size M. Target: cat-harness.
- Work: declare `computations/` under the new kind.
- Done when:
  - `check:kind-validators` judges every `*.witness.json`.
  - No witness file differs byte-for-byte from before.

**T4 — Implement `no-orphan-lean`, report-only.** Size S. Target: sci.
- Done when its output equals the ORPH lean rows. No file moves.

**T5 — Paper just-the-docs builder.** Size L. Targets: core and sci.
- Work: also scaffold the paper `build_command`.
- Done when:
  - Every listed qou block label has an anchor on the staging page.
  - The block `.md` sha256 values are unchanged.

**T6 — Downstream Tool discovery.** Size M. Target: cat-harness.
- Work: make `discoverTools` walk the folio root and its dependencies.
- Done when qou's Tools appear in `check:tools` run from qou.

**T7 — Move qou-specific CI and BPMN (item 14) out of the platform.** Size M. Depends on: T6.
- Done when:
  - The moves are pure renames.
  - `check:workflow-coverage` is green in both repositories.

## Skill gaps

- **Skill front matter.** There is no front-matter schema. A machine-read `inherits` contract
  (thin specialisation plus a parent-drift warning) is needed.
- **Lean packages.** There is no skill on declaring Lean packages or a Lake-root layout.
  `lean-environment-setup` predates the `formal-ref` dependency injection.
- **Computation witnesses.** There is no kind or skill for them. `compute-author` and
  `lean-witness-audit` assume `folio-assistant/computations/`.
- **Paper sites.** There is no paper-folio site-render skill under the just-the-docs ruling.
- **Old-layout folios.** `repo-conversion` does not cover upgrading one: renaming
  `folio.config.json`, the retired `dependents`, or the moved adapter path.
